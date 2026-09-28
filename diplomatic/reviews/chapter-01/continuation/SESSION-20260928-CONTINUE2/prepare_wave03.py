"""Prepare twenty-one separate one-page reading packets, preserving prior scopes."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image

R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
D = R / 'diplomatic'
V = D / 'reviews/chapter-01/continuation'
S = V / 'SESSION-20260928-CONTINUE2'
sys.path.insert(0, str(D / 'tools'))
from prepare_native_packet import prepare, tile_origins
load = lambda p: json.loads(p.read_text())
def dump(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
BASE = subprocess.check_output(['git','rev-parse','HEAD'], cwd=R, text=True).strip()
assert subprocess.check_output(['git','ls-remote','origin','refs/heads/main'], cwd=R, text=True).split()[0] == BASE
assert not subprocess.check_output(['git','diff','--name-only'], cwd=R, text=True).strip()
common = (S / 'reading-instructions.txt').read_text()
plans = load(S / 'wave03-plan-input.json')['plans']
queue = load(D / 'WORK-QUEUE.json')
tasks = {x['id']:x for x in queue['tasks']}
for p in plans:
    report_path = V / (p['task'] + '.json')
    if report_path.exists():
        assert not any(x.get('batch_id') == p['batch'] for x in load(report_path)['batches'])
    prefix = p['task'] + '-' + p['batch'] + '-reader'
    assert not (V / (prefix + '-request.txt')).exists()
    assert not (D / 'evidence/chapter-01/continuation' / p['task'] / p['batch']).exists()
for p in plans:
    mp = prepare(R, p['edition'], p['task'], p['batch'], p['pages'], p['lo'], p['hi'])
    p['manifest'] = str(mp.relative_to(R))
    m = load(mp)
    target = next(x for x in m['pages'] if x['pdf_page'] == p['target_page'])
    im = Image.open(R / target['path']); im.load()
    extra = []
    # Overlapping bands are neutral viewing aids, not asserted physical rows.
    band_height = 300 if im.height > 1100 else 250 if im.height > 800 else 180
    step = band_height - 100
    tops = list(range(150 if im.height > 800 else 30, im.height - 50, step))
    for top in tops:
        for left in tile_origins(im.width, 2000):
            bounds = [left, top, min(left+2000,im.width), min(top+band_height,im.height)]
            view = mp.parent / ('band-x%04d-y%04d.png' % (left,top))
            crop = im.crop(bounds); crop.save(view)
            assert Image.open(view).convert('RGBA').tobytes() == crop.convert('RGBA').tobytes()
            extra.append({'path':str(view.relative_to(R)), 'sha256':sha(view),
                'pdf_page':p['target_page'], 'bdrc_image':target['bdrc_image'],
                'source_member':target['source_member'], 'source_member_sha256':target['sha256'],
                'native_bounds':bounds, 'dimensions':list(crop.size),
                'derivation':'Exact unscaled overlapping native band; its label is not a physical-row assignment', 'pixel_identity_verified':True})
    # Rotated edge is explicitly an aid and may include neighboring main letters.
    edge_bounds = [0,0,min(900,im.width),im.height]
    edge = mp.parent / 'left-edge-rotated90.png'
    im.crop(edge_bounds).transpose(Image.Transpose.ROTATE_90).save(edge)
    extra.append({'path':str(edge.relative_to(R)), 'sha256':sha(edge), 'pdf_page':p['target_page'],
        'source_member':target['source_member'], 'native_bounds':edge_bounds,
        'derivation':'Lossless 90-degree counterclockwise rotation of native left edge; not automatically all marginal text'})
    if p['task'] == 'C1-BASE-UNCERTAINTIES':
        for label, bounds in [('S09-context',[1900,370,3300,645]),('S09-native-detail',[2220,425,2710,595])]:
            view = mp.parent / (label + '.png'); im.crop(bounds).save(view)
            extra.append({'path':str(view.relative_to(R)), 'sha256':sha(view), 'pdf_page':102,
                'source_member':target['source_member'], 'native_bounds':bounds,
                'derivation':'Exact unscaled native locus crop; label not proof of correspondence'})
    dump(mp.parent / 'reading-views.json', {'task_id':p['task'],'batch_id':p['batch'], 'views':extra})
    context_pages = [x for x in m['pages'] if x['pdf_page'] != p['target_page']]
    target_views = [x for x in m['views'] if x['pdf_page'] == p['target_page']]
    boundary_views = []
    for n in p['pages']:
        if n == p['target_page']:
            continue
        candidates = [x for x in m['views'] if x['pdf_page'] == n]
        boundary_views.append(candidates[-1] if n < p['target_page'] else candidates[0])
    images = [target] + context_pages + target_views + boundary_views + extra
    prefix = p['task'] + '-' + p['batch'] + '-reader'
    request = V / (prefix + '-request.txt')
    text = common + '\nTASK: ' + p['task'] + '\nBATCH: ' + p['batch'] + '\n' + p['scope']
    text += '\nThe target page is attachment1. Bands overlap and may cross rows; do not trust band names as row numbers. Use the full native page to establish actual rows and preserve every glyph. The rotated edge is not a new witness.'
    text += '\nATTACHMENTS\n' + json.dumps([{'image':i+1,**x} for i,x in enumerate(images)],ensure_ascii=False)
    text += '\nBASE REFERENCE, NOT WITNESS TESTIMONY\n' + json.dumps(load(mp.parent/'base-reference.json'),ensure_ascii=False)
    request.write_text(text)
    p['output_stem'] = str((V / prefix).relative_to(R))
    p['specification'] = str((V / (prefix+'-spec.json')).relative_to(R))
    dump(R / p['specification'], {'task_id':p['task'],'batch_id':p['batch'], 'source_pages':p['pages'], 'images':images, 'request_path':str(request.relative_to(R)), 'output_stem':p['output_stem']})
    print('PREPARED', p['task'], p['batch'], len(images), 'images', flush=True)
    rp = V / (p['task'] + '.json')
    report = load(rp) if rp.exists() else {'task_id':p['task'], 'status':'in_progress',
        'baseline_commit':BASE,'declared_scope':tasks[p['task']]['scope'],
        'chapter_complete':False,'coverage_complete':False,'batches':[]}
    report['batches'].append({'batch_id':p['batch'],'status':'claimed_prepared_not_read',
        'owner':'reader-'+prefix,'baseline_commit':BASE,'scope':p['scope'],
        'target_page':p['target_page'],'source_manifest':p['manifest'],
        'specification':p['specification'],'rows_actually_compared':[],
        'observations':[],'canonical_record_ids':[]})
    report['current_wave_id'] = 'CONTINUE2-W03'
    dump(rp, report)
    md = V / (p['task'] + '.md')
    if not md.exists():
        md.write_text('# ' + p['task'] + ' — bounded continuation\n\nIn progress. Earlier opening and boundary reports remain preserved; this packet is prepared, not yet read. No witness-completion claim.\n')
    task = tasks[p['task']]
    task.update(status='in_progress', owner='separate-page-readers-CONTINUE2-W03', current_wave_id='CONTINUE2-W03')
    task['current_batch_id'] = next(x['batch'] for x in plans if x['task']==p['task'])
    task['report_paths'] = [str(rp.relative_to(R)),str(md.relative_to(R))]
    task['bounded_parallel_policy'] = 'Each reader owns one target page and at most three source pages including context; coordinator alone publishes and no unfinished page is inferred complete from a neighbor.'
dump(D / 'WORK-QUEUE.json', queue)
dump(S / 'wave03-plan.json', {'wave_id':'CONTINUE2-W03','baseline_commit':BASE,
    'status':'requests_ready_pending_checkpoint','plans':plans,'maximum_parallel_readers':21,
    'previous_reading_reference_commit':'2382179fb648e4ec59fbe1633d83a23df5b6e620',
    'chapter_complete':False})
