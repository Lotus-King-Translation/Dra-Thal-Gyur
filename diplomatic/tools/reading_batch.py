#!/usr/bin/env python3
"""Prepare hash-checked native evidence or capture a bounded image-reading attempt.

Neither command adopts a reading, completes coverage, stages files, or publishes.
The coordinator must inspect results, record exact limits, and checkpoint them.
Preparation uses Pillow; capture uses the locally authorized Codex CLI unchanged.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import datetime
import zipfile


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Path leaves repository: ' + relative)
    return path


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def prepare(root: Path, edition: str, pages: list[int], destination: str) -> None:
    from PIL import Image
    import io
    if not pages or len(set(pages)) != len(pages) or len(pages) > 5:
        raise ValueError('Require one to five distinct source pages.')
    source = inside(root, 'editions/' + edition)
    dest = inside(root, destination)
    if not dest.is_relative_to(root / 'diplomatic/evidence'):
        raise ValueError('Evidence destination must be inside diplomatic/evidence.')
    dest.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((source / 'image-manifest.json').read_text())
    record = {'status': 'preparing_not_inspected', 'edition': edition,
              'requested_pages': pages, 'sources': {}, 'pages': [], 'tiles': [],
              'coordinates': 'zero-based half-open native left/top/right/bottom'}
    target = dest / 'manifest.json'
    dump(target, record)
    for name, key in [('sgra-thal-gyur.pdf', 'pdf_sha256'),
                      ('original-images.zip', 'zip_sha256')]:
        path = source / name
        value = digest(path)
        if value != manifest[key]:
            raise ValueError('Source hash mismatch: ' + str(path.relative_to(root)))
        record['sources'][str(path.relative_to(root))] = value
        dump(target, record)
    images = {entry['pdf_page']: entry for entry in manifest['images']}
    with zipfile.ZipFile(source / 'original-images.zip') as archive:
        for page in pages:
            entry = images[page]
            payload = archive.read(entry['file'])
            if hashlib.sha256(payload).hexdigest() != entry['sha256']:
                raise ValueError('Native member hash mismatch: ' + entry['file'])
            image = Image.open(io.BytesIO(payload))
            if image.size != (entry['width'], entry['height']):
                raise ValueError('Native dimensions mismatch')
            native = dest / (f'p{page:03d}-native' + Path(entry['file']).suffix)
            native.write_bytes(payload)
            item = {'path': str(native.relative_to(root)), 'pdf_page': page,
                    'bdrc_image': entry['image'], 'source_member': entry['file'],
                    'sha256': entry['sha256'], 'dimensions': list(image.size)}
            record['pages'].append(item)
            dump(target, record)
            width, height = image.size
            tw, th = min(2000, width), min(1600, height)
            xs = sorted({min(x, width-tw) for x in range(0, width, max(1, tw-100))})
            ys = sorted({min(y, height-th) for y in range(0, height, max(1, th-100))})
            for x in xs:
                for y in ys:
                    bounds = [x, y, x+tw, y+th]
                    tile = dest / f'p{page:03d}-x{x:04d}-y{y:04d}.png'
                    image.crop(bounds).save(tile)
                    record['tiles'].append({**item,
                        'path': str(tile.relative_to(root)), 'bounds': bounds,
                        'sha256': digest(tile), 'derivation': 'unscaled native crop'})
                    dump(target, record)
    record['status'] = 'prepared_not_visually_inspected'
    dump(target, record)
    print(json.dumps({'manifest': str(target.relative_to(root)), 'pages': len(pages)}))


def capture(root: Path, specification: str) -> None:
    spec = json.loads(inside(root, specification).read_text())
    if not 1 <= len(set(spec['source_pages'])) <= 5:
        raise ValueError('A reader receives at most five source pages.')
    request = inside(root, spec['request_path'])
    stem = inside(root, spec['output_stem'])
    if not stem.is_relative_to(root / 'diplomatic/reviews'):
        raise ValueError('Reading outputs must remain inside diplomatic/reviews.')
    outputs = {key: Path(str(stem) + suffix) for key, suffix in {
        'reading': '-reading.txt', 'events': '-session.jsonl',
        'stderr': '-stderr.txt', 'execution': '-execution.json'}.items()}
    if any(path.exists() for path in outputs.values()):
        raise FileExistsError('Preserve the prior attempt; use a new output stem.')
    args = ['codex', 'exec', '--sandbox', 'read-only', '--color', 'never',
            '--json', '-C', str(root)]
    for item in spec['images']:
        image = inside(root, item['path'])
        if digest(image) != item['sha256']:
            raise ValueError('Attachment hash mismatch: ' + item['path'])
        args.extend(['-i', str(image)])
    args.extend(['-o', str(outputs['reading']), '-'])
    receipt = {'status': 'running_not_accepted', 'specification': specification,
               'request_sha256': digest(request), 'images': spec['images'],
               'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'source_pages': spec['source_pages'], 'sandbox': 'read-only',
               'editorial_decisions_made_by_wrapper': False}
    dump(outputs['execution'], receipt)
    try:
        with outputs['events'].open('x') as events, outputs['stderr'].open('x') as errors:
            result = subprocess.run(args, input=request.read_text(), text=True,
                                    stdout=events, stderr=errors, cwd=root)
        receipt['returncode'] = result.returncode
        receipt['status'] = 'captured_requires_coordinator_review'
        receipt['unexpected_tool_items'] = []
        receipt['unparseable_event_lines'] = 0
        for line in outputs['events'].read_text().splitlines():
            try:
                item = json.loads(line).get('item', {})
            except json.JSONDecodeError:
                receipt['unparseable_event_lines'] += 1
                continue
            if item.get('type') not in {None, 'agent_message', 'reasoning', 'error'}:
                receipt['unexpected_tool_items'].append(item.get('type'))
    except BaseException as error:
        receipt['status'] = 'interrupted_or_failed_not_accepted'
        receipt['error'] = str(error)
        raise
    finally:
        receipt['finished_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        receipt['output_hashes'] = {str(path.relative_to(root)): digest(path)
            for key, path in outputs.items() if key != 'execution' and path.exists()}
        dump(outputs['execution'], receipt)
    print(json.dumps({'receipt': str(outputs['execution'].relative_to(root)),
                      'returncode': receipt['returncode'], 'accepted': False}))
    if receipt['returncode']:
        raise RuntimeError('Reader failed; preserve the captured attempt.')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'))
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('--edition', required=True)
    prep.add_argument('--pages', type=int, nargs='+', required=True)
    prep.add_argument('--output', required=True)
    reader = commands.add_parser('capture')
    reader.add_argument('--specification', required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    if args.command == 'prepare':
        prepare(root, args.edition, args.pages, args.output)
    else:
        capture(root, args.specification)


if __name__ == '__main__':
    main()
