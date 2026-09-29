"""Prepare explicitly planned bounded native-image tasks; no adoption or publication."""
from pathlib import Path
import copy
import hashlib
import json
import subprocess
import sys
from PIL import Image

R = Path(__file__).resolve().parents[2]
D = R / 'diplomatic'
V = D / 'reviews/chapter-01/continuation'
W = (R / sys.argv[1]).resolve()
assert W.is_relative_to(V.resolve()), 'Plan must remain in active project reviews'
sys.path.insert(0, str(D / 'tools'))
from prepare_native_packet import prepare
from prepare_composite_packet import prepare as prepare_composite
load = lambda p: json.loads(p.read_text())
def dump(p, x):
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + '\n')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=R, text=True).strip()
assert subprocess.check_output(['git', 'ls-remote', 'origin', 'refs/heads/main'], cwd=R, text=True).split()[0] == base
plan = load(W / 'plan.json')
common = (W / 'instructions.txt').read_text()
q = load(D / 'WORK-QUEUE.json')
tasks = {t['id']: t for t in q['tasks']}
for item in plan['plans']:
    task, batch = item['task'], item['batch']
    destination = D / 'evidence/chapter-01/continuation' / task / batch
    assert not destination.exists(), 'Preserve partial packet before any retry'
    report_path = V / (task + '.json')
    if report_path.exists():
        assert not any(b['batch_id'] == batch for b in load(report_path)['batches'])
    stem = V / (task + '-' + batch + '-reader')
    assert not Path(str(stem) + '-request.txt').exists()
    manifest_path = (prepare_composite(R, item) if 'source_pdf' in item else
                     prepare(R, item['edition'], task, batch, item['pages'], item['lo'], item['hi']))
    manifest = load(manifest_path)
    targets = [im for im in manifest['pages'] if im['pdf_page'] in item['target_pages']]
    target_views = [im for im in manifest['views'] if im['pdf_page'] in item['target_pages']]
    flanks = [im for im in manifest['pages'] if im['pdf_page'] not in item['target_pages']]
    flank_views = []
    for flank in flanks:
        views = [im for im in manifest['views'] if im['pdf_page'] == flank['pdf_page']]
        flank_views.append(views[-1] if flank['pdf_page'] < min(item['target_pages']) else views[0])
    images = targets + flanks + target_views + flank_views
    item['manifest'] = str(manifest_path.relative_to(R))
    item['output_stem'] = str(stem.relative_to(R))
    item['specification'] = str(Path(str(stem) + '-spec.json').relative_to(R))
    reference = load(destination / 'base-reference.json')
    text = common + '\nTASK: ' + task + '\nBATCH: ' + batch
    text += '\nTARGET PAGES: ' + json.dumps(item['target_pages']) + '\n' + item['scope']
    text += '\nATTACHMENTS\n' + json.dumps([{'image': i + 1, **x} for i, x in enumerate(images)], ensure_ascii=False)
    text += '\nBASE ALIGNMENT AID, NOT SOURCE TESTIMONY\n' + json.dumps(reference, ensure_ascii=False)
    request = Path(str(stem) + '-request.txt')
    request.write_text(text)
    dump(R / item['specification'], {'task_id': task, 'batch_id': batch,
         'source_pages': item['pages'], 'target_pages': item['target_pages'],
         'images': images, 'request_path': str(request.relative_to(R)),
         'output_stem': item['output_stem']})
    report = load(report_path) if report_path.exists() else {
        'task_id': task, 'status': 'in_progress', 'baseline_commit': base,
        'declared_scope': tasks[task]['scope'], 'chapter_complete': False,
        'coverage_complete': False, 'batches': []}
    report['batches'].append({'batch_id': batch, 'status': 'claimed_prepared_not_read',
        'owner': 'reader-' + task + '-' + batch, 'baseline_commit': base,
        'target_pages': item['target_pages'], 'source_pages': item['pages'],
        'scope': item['scope'], 'source_manifest': item['manifest'],
        'specification': item['specification'], 'rows_actually_compared': [],
        'observations': [], 'canonical_record_ids': []})
    report['current_batch_id'] = batch
    dump(report_path, report)
    md = report_path.with_suffix('.md')
    if not md.exists():
        md.write_text('# ' + task + ' — bounded continuation\n\nIn progress. Prepared sources are not read or certified.\n')
    tasks[task]['report_paths'] = [str(report_path.relative_to(R)), str(md.relative_to(R))]
    plan['status'] = 'preparing_not_read'
    dump(W / 'plan.json', plan)
    dump(D / 'WORK-QUEUE.json', q)
    print('PREPARED', task, batch, len(images), 'images', flush=True)
plan['status'] = 'prepared_requests_pending_checkpoint'
plan['prepared_at_commit'] = base
plan['chapter_complete'] = False
dump(W / 'plan.json', plan)
