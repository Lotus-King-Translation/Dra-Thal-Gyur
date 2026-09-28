#!/usr/bin/env python3
"""Preserve at most five verified native scan pages and lossless reading tiles.

Requires Pillow, unlike the standard-library chapter builder. Does not perform
OCR, infer glyphs, edit readings, fetch sources, or publish Git changes. A new
batch directory is required; interrupted packets must be preserved, not reset.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import re
import subprocess
import zipfile
from pathlib import Path
from PIL import Image, __version__ as pillow_version


def sha256(path: Path) -> str:
    with path.open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()


def write_once(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as handle:
        handle.write(data)


def dump_once(path: Path, data: object) -> None:
    write_once(path, (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode())


def tile_origins(size: int, limit: int, overlap: int = 100) -> list[int]:
    if size < 1 or overlap < 0 or limit <= overlap:
        raise ValueError('Invalid tile geometry')
    if size <= limit:
        return [0]
    positions = list(range(0, size - limit + 1, limit - overlap))
    if positions[-1] != size - limit:
        positions.append(size - limit)
    return positions


def prepare(repo: Path, edition: str, task: str, batch: str,
            pages: list[int], start_unit: int, end_unit: int) -> Path:
    repo = repo.resolve()
    if not re.fullmatch(r'[a-zA-Z0-9-]+', edition):
        raise ValueError('Invalid edition directory name')
    if not all(re.fullmatch(r'[A-Z0-9-]+', value) for value in (task, batch)):
        raise ValueError('Task and batch IDs must be explicit safe names')
    if not 1 <= len(pages) <= 5 or len(set(pages)) != len(pages):
        raise ValueError('A packet must contain one to five distinct pages')
    if pages != sorted(pages) or not 1 <= start_unit <= end_unit <= 2635:
        raise ValueError('Pages must be ordered; reference anchors must be valid')
    source = repo / 'editions' / edition
    if not source.resolve().is_relative_to(repo):
        raise ValueError('Source directory escapes the repository')
    metadata = json.loads((source / 'image-manifest.json').read_text())
    entries = {entry['pdf_page']: entry for entry in metadata['images']}
    if len(entries) != len(metadata['images']):
        raise ValueError('Duplicate physical pages in source manifest')
    if not set(pages) <= entries.keys():
        raise ValueError('Requested page absent from acquired source manifest')
    assets = []
    for name, key in [('sgra-thal-gyur.pdf', 'pdf_sha256'),
                      ('original-images.zip', 'zip_sha256')]:
        path = source / name
        if not path.resolve().is_relative_to(repo):
            raise ValueError('Source path escapes the repository')
        digest = sha256(path)
        if digest != metadata[key]:
            raise ValueError(f'Source hash mismatch or LFS pointer: {path}')
        assets.append({'path': str(path.relative_to(repo)), 'sha256': digest,
                       'bytes': path.stat().st_size})
    baseline = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
    data_dir = repo / 'diplomatic/collation/chapter-01'
    references = {}
    for name in ['reading-units.json', 'ch1-scan-insertions.json',
                 'additional-interventions.json']:
        path = data_dir / name
        relative = str(path.relative_to(repo))
        payload = path.read_bytes()
        committed = subprocess.check_output(
            ['git', 'show', f'{baseline}:{relative}'], cwd=repo)
        if committed != payload:
            raise ValueError('Publish canonical inputs before preparing a packet')
        references[name] = {'path': relative,
                            'sha256': hashlib.sha256(payload).hexdigest(),
                            'data': json.loads(payload)}
    target = repo / 'diplomatic/evidence/chapter-01/continuation' / task / batch
    if not target.resolve().is_relative_to(repo):
        raise ValueError('Packet destination escapes the repository')
    target.mkdir(parents=True, exist_ok=False)
    record = {'schema_version': 1, 'task_id': task, 'batch_id': batch,
              'baseline_commit': baseline, 'edition': edition,
              'generator': {'path': str(Path(__file__).resolve().relative_to(repo)),
                            'sha256': sha256(Path(__file__)),
                            'pillow_version': pillow_version},
              'requested_pdf_pages': pages, 'source_assets': assets,
              'source_manifest_sha256': sha256(source / 'image-manifest.json'),
              'status': 'preparing_not_inspected', 'pages': [], 'views': [],
              'coordinates': 'Zero-based half-open native raster pixels',
              'reading_claim': 'None: hashes and tiles do not establish glyphs'}
    manifest_path = target / 'manifest.json'
    def save_progress() -> None:
        manifest_path.write_text(json.dumps(record, ensure_ascii=False,
                                           indent=2) + '\n', encoding='utf-8')
    save_progress()
    with zipfile.ZipFile(source / 'original-images.zip') as archive:
        for page_number in pages:
            entry = entries[page_number]
            payload = archive.read(entry['file'])
            if hashlib.sha256(payload).hexdigest() != entry['sha256']:
                raise ValueError(f'Archive member hash mismatch: {entry["file"]}')
            suffix = Path(entry['file']).suffix.lower()
            if suffix not in {'.png', '.jpg', '.jpeg'}:
                raise ValueError('Unsupported native image format; preserve source')
            image = Image.open(io.BytesIO(payload))
            image.load()
            if image.size != (entry['width'], entry['height']):
                raise ValueError('Native dimensions differ from acquisition record')
            native = target / f'p{page_number:03d}-native{suffix}'
            write_once(native, payload)
            location = {'pdf_page': page_number, 'bdrc_image': entry['image'],
                        'source_member': entry['file'],
                        'source_member_sha256': entry['sha256']}
            record['pages'].append({**location, 'path': str(native.relative_to(repo)),
                                    'sha256': entry['sha256'],
                                    'dimensions': list(image.size)})
            save_progress()
            for top in tile_origins(image.height, 1400):
                for left in tile_origins(image.width, 2000):
                    bounds = [left, top, min(left + 2000, image.width),
                              min(top + 1400, image.height)]
                    crop = image.crop(bounds)
                    buffer = io.BytesIO()
                    crop.save(buffer, format='PNG')
                    output = target / f'p{page_number:03d}-x{left:04d}-y{top:04d}.png'
                    write_once(output, buffer.getvalue())
                    decoded = Image.open(output)
                    if decoded.convert('RGBA').tobytes() != crop.convert('RGBA').tobytes():
                        raise ValueError('Lossless tile verification failed')
                    record['views'].append({**location,
                        'path': str(output.relative_to(repo)), 'sha256': sha256(output),
                        'native_bounds': bounds, 'dimensions': list(crop.size),
                        'derivation': 'Unscaled native crop; no enhancement or OCR',
                        'pixel_identity_verified': True})
                    save_progress()
    units = references['reading-units.json']['data']
    chosen = [unit for unit in units if start_unit <= int(unit['id'][1:]) <= end_unit]
    selected_ids = {unit['id'] for unit in chosen}
    insertions = references['ch1-scan-insertions.json']['data']
    notes = references['additional-interventions.json']['data']
    reference = {'baseline_commit': baseline, 'anchor_range': [start_unit, end_unit],
                 'warning': 'Base reference only, never evidence of comparison-witness agreement',
                 'base_units': chosen,
                 'insertions': [item for item in insertions if item['after_unit'] in selected_ids],
                 'separate_annotations': [
                     {key: item[key] for key in ('id', 'units', 'annotation',
                         'annotation_status', 'reading_uncertainty') if key in item}
                     for item in notes if set(item['units']) & selected_ids and
                     (item.get('annotation') or item.get('reading_uncertainty'))],
                 'source_inputs': [{key: value for key, value in item.items() if key != 'data'}
                                   for item in references.values()]}
    dump_once(target / 'base-reference.json', reference)
    record['base_reference'] = {'path': str((target / 'base-reference.json').relative_to(repo)),
                               'sha256': sha256(target / 'base-reference.json')}
    record['status'] = 'ready_for_visual_review_not_collated'
    save_progress()
    return manifest_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--edition', required=True)
    parser.add_argument('--task', required=True)
    parser.add_argument('--batch', required=True)
    parser.add_argument('--pages', type=int, nargs='+', required=True)
    parser.add_argument('--start-unit', type=int, required=True)
    parser.add_argument('--end-unit', type=int, required=True)
    args = parser.parse_args()
    try:
        path = prepare(args.repo, args.edition, args.task, args.batch,
                       args.pages, args.start_unit, args.end_unit)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f'Packet incomplete; preserve any partial files: {error}\n')
    print(json.dumps({'packet_manifest': str(path), 'pages': args.pages,
                      'visual_reading_performed': False}, indent=2))


if __name__ == '__main__':
    main()
