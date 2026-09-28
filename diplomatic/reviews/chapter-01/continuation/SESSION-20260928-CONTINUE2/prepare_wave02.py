"""Prepare eight separate one-page reading packets, preserving prior scopes."""
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
plans = []
for page, batch, lo, hi in [(4,'B03-P0004',25,53),(5,'B04-P0005',49,80),(6,'B05-P0006',74,106),(7,'B06-P0007',100,130)]:
    plans.append({'task':'C1-BASE-PHYSICAL','batch':batch,'edition':'adzom-2000', 'target_page':page,'pages':[page-1,page,page+1],'lo':lo,'hi':hi,
        'scope':f'Complete physical inventory of ADZOM PDF{page} only, all main rows, source layers, ornaments, filler signs and marginal inscriptions. Adjacent pages are boundary context only. Existing main lexical pass is retained; record every boundary and any newly observed mismatch without grammatical normalization.'})
plans += [
 {'task':'C1-BASE-UNCERTAINTIES','batch':'B03-P0102-S09','edition':'adzom-2000','target_page':102,'pages':[101,102],'lo':2625,'hi':2635,
  'scope':'Adzom PDF102 chapter1 boundary and S09 compact inscription only. Locate the actual U02635 closing and subsequent next-chapter incipit to delimit S09. Transcribe the inscription only as far as individual shapes support; distinguish its script, source layer, signs and exact remaining components. PDF101 is incoming context. Do not transcribe or collate Chapter2 beyond the minimal boundary incipit. Prior S09 remains explicitly unresolved, not a guessed heading.'},
 {'task':'C1-TINGKYE','batch':'B03-P0005','edition':'tingkye-1973','target_page':5,'pages':[4,5,6],'lo':125,'hi':185,
  'scope':'TINGKYE PDF5 all seven main rows, margins, notes and signs. Previous continuous report ends PDF4 row7 U00127 through པར, with a questioned outgoing word on PDF5 row1. Establish that word from pixels, then continue U00128 onward across the entire page. PDF4 and PDF6 are boundary context only. No inherited whole-page agreement is inferred from the earlier PDF6 isolated junction. Give actual source-ordered rows, every local conflict, precisely bounded unread components and true outgoing anchor.'},
 {'task':'C1-TSAMDRAK','batch':'B03-P0015','edition':'tsamdrak-1982','target_page':15,'pages':[14,15,16],'lo':380,'hi':445,
  'scope':'TSAMDRAK PDF15 all seven main rows, non-main regions and signs. PDF14 ended at U00383 དམིགས་པ་ཡུལ་གྱི་བློ་རྣམས་ལ. Establish the next actual source anchor rather than infer proportional mapping. PDF14/16 are boundary context only. Preserve physical notes/numerals separately, including local absence of a base heading rather than calling it an omitted main verse. Inspect every row despite isolated unclear glyphs.'},
 {'task':'C1-DEGE','batch':'B01-P0003','edition':'dege-W1ER7','target_page':3,'pages':[2,3,4],'lo':1,'hi':250,
  'scope':'DEGE PDF3: establish actual opening/closing anchors, then inspect all seven main rows and all interlinear/marginal source material and signs. PDF2/4 are contextual flanks only; earlier opening reports did not certify them fully. Broad U1-250 base range is a locator aid, NOT an inferred page mapping. Read source independently wherever it disagrees. Retain faint letter components with exact bounds rather than treating the entire page as unavailable. Native color images are authoritative; any explicitly labeled channel view is only a deterministic contrast aid, not new pixels or another witness.'}
]
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
    report['current_wave_id'] = 'CONTINUE2-W02'
    dump(rp, report)
    md = V / (p['task'] + '.md')
    if not md.exists():
        md.write_text('# ' + p['task'] + ' — bounded continuation\n\nIn progress. Earlier opening and boundary reports remain preserved; this packet is prepared, not yet read. No witness-completion claim.\n')
    task = tasks[p['task']]
    task.update(status='in_progress', owner='separate-page-readers-CONTINUE2-W02', current_wave_id='CONTINUE2-W02')
    task['current_batch_id'] = next(x['batch'] for x in plans if x['task']==p['task'])
    task['report_paths'] = [str(rp.relative_to(R)),str(md.relative_to(R))]
    task['bounded_parallel_policy'] = 'Each reader owns one target page and at most three source pages including context; coordinator alone publishes and no unfinished page is inferred complete from a neighbor.'
dump(D / 'WORK-QUEUE.json', queue)
dump(S / 'wave02-plan.json', {'wave_id':'CONTINUE2-W02','baseline_commit':BASE,
    'status':'requests_ready_pending_checkpoint','plans':plans,'maximum_parallel_readers':8,
    'prior_wave_integration_verified':'2382179fb648e4ec59fbe1633d83a23df5b6e620',
    'chapter_complete':False})
