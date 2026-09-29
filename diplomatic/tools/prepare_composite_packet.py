#!/usr/bin/env python3
"""Preserve bounded full-composite PDF evidence, never just its background image.

Requires Pillow and PyMuPDF. No OCR, source mutation, reading adoption or Git
publication. Render scale accounts for displayed raster components. Provider
page numbers are not inferred BDRC image indices. Interrupted outputs are kept.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import pymupdf
from PIL import Image, __version__ as pillow_version
from prepare_native_packet import tile_origins


def sha(path: Path) -> str:
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def prepare(repo: Path, plan: dict) -> Path:
    repo = repo.resolve()
    source = (repo / plan['source_pdf']).resolve()
    if not source.is_relative_to(repo / 'editions'):
        raise ValueError('Source must be an acquired project edition')
    pages = plan['pages']
    if not 1 <= len(pages) <= 5 or pages != sorted(set(pages)):
        raise ValueError('Require one to five ordered, distinct provider pages')
    if not all(re.fullmatch(r'[A-Z0-9-]+', plan[k]) for k in ('task', 'batch')):
        raise ValueError('Invalid task or batch identity')
    if sha(source) != plan['source_sha256']:
        raise ValueError('Source hash mismatch or unmaterialized LFS pointer')
    base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
    data_dir = repo / 'diplomatic/collation/chapter-01'
    references = {}
    for name in ('reading-units.json', 'ch1-scan-insertions.json', 'additional-interventions.json'):
        path = data_dir / name
        committed = subprocess.check_output(['git', 'show', base + ':' + str(path.relative_to(repo))], cwd=repo)
        if committed != path.read_bytes():
            raise ValueError('Publish canonical references before preparing new evidence')
        references[name] = {'path': str(path.relative_to(repo)), 'sha256': sha(path),
                            'data': json.loads(path.read_text(encoding='utf-8'))}
    dest = repo / 'diplomatic/evidence/chapter-01/continuation' / plan['task'] / plan['batch']
    dest.mkdir(parents=True, exist_ok=False)
    manifest_path = dest / 'manifest.json'
    record = {'schema_version': 1, 'task_id': plan['task'], 'batch_id': plan['batch'],
              'baseline_commit': base, 'status': 'preparing_not_inspected',
              'source_assets': [{'path': str(source.relative_to(repo)), 'sha256': sha(source)}],
              'generator': {'path': str(Path(__file__).resolve().relative_to(repo)),
                            'sha256': sha(Path(__file__)), 'pymupdf': pymupdf.VersionBind,
                            'pillow': pillow_version},
              'coordinates': 'Half-open full-composite raster pixel bounds at the recorded matrix',
              'pages': [], 'views': [], 'reading_claim': 'None: rendering does not establish glyph readings'}
    dump(manifest_path, record)
    with pymupdf.open(source) as document:
        if any(not 1 <= n <= len(document) for n in pages):
            raise ValueError('Requested provider page does not exist')
        record['provider_container_page_count'] = len(document)
        for number in pages:
            page = document[number - 1]
            components = page.get_image_info(hashes=True, xrefs=True)
            scale = 1.0
            for item in components:
                rect = pymupdf.Rect(item['bbox'])
                if not rect.is_empty and rect.intersects(page.rect):
                    scale = max(scale, item['width'] / rect.width, item['height'] / rect.height)
            if max(page.rect.width, page.rect.height) * scale > 24000:
                raise ValueError('Very large composite: review scale explicitly instead of downsampling')
            pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False, annots=True)
            output = dest / f'p{number:03d}-composite.png'
            pixmap.save(output)
            image = Image.open(output)
            image.load()
            info = {'pdf_page': number, 'bdrc_image': None,
                    'source_member': f'provider-PDF-page-{number}-full-composite',
                    'source_pdf_sha256': plan['source_sha256'],
                    'path': str(output.relative_to(repo)), 'sha256': sha(output),
                    'dimensions': list(image.size), 'page_rect_points': list(page.rect),
                    'page_rotation': page.rotation, 'render_matrix': [scale, 0, 0, scale, 0, 0],
                    'displayed_raster_components': [{k: x[k] for k in
                        ('number', 'bbox', 'width', 'height', 'bpc', 'xref')} for x in components],
                    'referenced_image_resources': [list(x) for x in page.get_images(full=True)],
                    'derivation': 'Complete page rendering, including all visible composited layers and annotations',
                    'exposure_count': 'Requires visual inventory; image-resource count is not exposure count'}
            record['pages'].append(info)
            dump(manifest_path, record)
            for top in tile_origins(image.height, 1400):
                for left in tile_origins(image.width, 2000):
                    bounds = [left, top, min(left + 2000, image.width), min(top + 1400, image.height)]
                    cropped = image.crop(bounds)
                    tile = dest / f'p{number:03d}-x{left:04d}-y{top:04d}.png'
                    cropped.save(tile)
                    if Image.open(tile).convert('RGBA').tobytes() != cropped.convert('RGBA').tobytes():
                        raise ValueError('Composite crop failed lossless verification')
                    record['views'].append({'pdf_page': number, 'bdrc_image': None,
                        'source_member': info['source_member'], 'path': str(tile.relative_to(repo)),
                        'sha256': sha(tile), 'native_bounds': bounds, 'coordinate_space': 'composite raster',
                        'dimensions': list(cropped.size), 'parent_composite_sha256': info['sha256'],
                        'derivation': 'Unscaled lossless crop of the complete composite rendering',
                        'pixel_identity_verified_against_composite': True})
                    dump(manifest_path, record)
    lo, hi = plan['lo'], plan['hi']
    if not 1 <= lo <= hi <= 2635:
        raise ValueError('Invalid alignment-aid anchor range')
    chosen = [u for u in references['reading-units.json']['data'] if lo <= int(u['id'][1:]) <= hi]
    ids = {u['id'] for u in chosen}
    reference = {'baseline_commit': base, 'anchor_range': [lo, hi],
                 'warning': 'Alignment aid only, not evidence of this comparison witness',
                 'base_units': chosen,
                 'insertions': [u for u in references['ch1-scan-insertions.json']['data'] if u['after_unit'] in ids],
                 'separate_annotations': [{k: u[k] for k in ('id', 'units', 'annotation',
                     'annotation_status', 'reading_uncertainty') if k in u}
                     for u in references['additional-interventions.json']['data']
                     if set(u['units']) & ids and (u.get('annotation') or u.get('reading_uncertainty'))],
                 'source_inputs': [{k: v for k, v in u.items() if k != 'data'} for u in references.values()]}
    reference_path = dest / 'base-reference.json'
    dump(reference_path, reference)
    record['base_reference'] = {'path': str(reference_path.relative_to(repo)), 'sha256': sha(reference_path)}
    record['status'] = 'ready_for_visual_review_not_collated'
    dump(manifest_path, record)
    return manifest_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--plan', type=Path, required=True)
    args = parser.parse_args()
    print(prepare(args.repo, json.loads(args.plan.read_text(encoding='utf-8'))))
