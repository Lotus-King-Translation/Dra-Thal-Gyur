"""Prepare four bounded image-reading requests and claims; no textual adoption."""
import hashlib
import json
import subprocess
from pathlib import Path

R = Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
D = R / 'diplomatic'
V = D / 'reviews/chapter-01/continuation'
S = V / 'SESSION-20260928-CONTINUE2'
load = lambda p: json.loads(p.read_text())
def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

record = load(S / 'session-plan.json')
base = record['baseline_commit']
assert subprocess.check_output(['git','rev-parse','HEAD'], cwd=R, text=True).strip() == base
plans = record['plans']
queue = load(D / 'WORK-QUEUE.json')
tasks = {item['id']: item for item in queue['tasks']}
common = (S / 'reading-instructions.txt').read_text()
notes = {
 'C1-BASE-UNCERTAINTIES': 'Search PDF101 all rows for the actual note strings. U02615 transcript note is མདོག་གི་ཡང་བྱུང་།; U02620 is དེ་དག་གི་ཞབས་སྡུད་པའོ། །. Both are currently outside main verse and print-uncertain. Do not assign the same cluster twice to fit both phrases. Establish main-text flanks, literal note components, layer, punctuation and precise unresolvable shapes. Search coverage may replace full main-text transcription in this targeted task. Non-identification is not proof of historical absence.',
 'C1-BASE-PHYSICAL': 'Target is ADZOM PDF3 all four rows, all boundaries, margins, ornaments and fillers. PDF2/4 are boundary context only. Existing lexical pass remains authoritative within its scope. Earlier physical report assessed only U00015/U00016 double-shad boundaries and left the rest partial. Finish the other physical regions with source-ordered Tibetan and sign inventory. Every unit boundary and every physical row ending must be recorded, including internal row turns. A full native column resolves any clipped row band.',
 'C1-TINGKYE': 'Target is TINGKYE PDF4 rows4-7, printed389/BDRC397/member0397.png. Restart U00106 ས་བོན, following སྤྲུལ་པའི at row3 end. Earlier rows1-3 already have a saved partial comparison; do not claim them new. PDF5 first row is outgoing context. Read the four rows in full, including all lexical differences, compound signs and notes. Retain exact unresolved suffixes with bounds. Do not advance the continuous frontier to the old isolated PDF6 check.',
 'C1-TSAMDRAK': 'Target is TSAMDRAK PDF14 all seven main rows and non-main regions; PDF13 is preceding context only. Existing ledger ends U00349 and begins U00350 at PDF13 row7. Follow actual source into PDF14; do not infer page mapping by proportion. Transcribe all seven rows, exact differences and signs. Keep unaligned words, local omissions with both flanks, and source layers separate. The opening U00012 vowel and U00148 suffix limits remain in the earlier report and are not re-opened here.'
}
for p in plans:
    prefix = p['task'] + '-' + p['batch'] + '-reader'
    assert not (V / (prefix + '-request.txt')).exists()
    report = load(V / (p['task'] + '.json'))
    assert not any(b.get('batch_id') == p['batch'] for b in report['batches'])
for p in plans:
    m = load(R / p['manifest'])
    folder = (R / p['manifest']).parent
    images = m['pages'] + m['views'] + load(folder / 'focused-views.json')['views']
    reference = load(folder / 'base-reference.json')
    prefix = p['task'] + '-' + p['batch'] + '-reader'
    request_path = V / (prefix + '-request.txt')
    request = common + '\nTASK: ' + p['task'] + '\nBATCH: ' + p['batch']
    request += '\n' + p['target'] + '\n' + notes[p['task']]
    request += '\nATTACHMENTS IN ORDER\n' + json.dumps([{'image':i+1,**x} for i,x in enumerate(images)], ensure_ascii=False)
    request += '\nBASE REFERENCE, NOT WITNESS TESTIMONY\n' + json.dumps(reference, ensure_ascii=False)
    request_path.write_text(request)
    spec_path = V / (prefix + '-spec.json')
    spec = {'task_id':p['task'], 'batch_id':p['batch'], 'source_pages':p['pages'],
            'request_path':str(request_path.relative_to(R)),
            'output_stem':str((V / prefix).relative_to(R)), 'images':images}
    dump(spec_path, spec)
    p.update(specification=str(spec_path.relative_to(R)), output_stem=spec['output_stem'])
    report_path = V / (p['task'] + '.json')
    report = load(report_path)
    owner = 'independent-reader-' + prefix
    report['batches'].append({'batch_id':p['batch'], 'baseline_commit':base,
        'status':'claimed_prepared_not_read', 'owner':owner, 'scope':p['target'],
        'source_manifest':p['manifest'], 'specification':p['specification'],
        'rows_actually_compared':[], 'observations':[], 'canonical_record_ids':[]})
    report['current_batch_id'] = p['batch']
    report['status'] = 'in_progress'
    dump(report_path, report)
    task = tasks[p['task']]
    task['prior_owner_at_reassignment'] = task.get('owner')
    task.update(owner=owner, status='in_progress', current_batch_id=p['batch'], checkpoint_commit=base)
    task['reassignment_note'] = 'Previous reader finished and was published at b3b10d5; its report remains unchanged. No orphan reader or unpublished inherited work was found.'
    print('CLAIMED', p['task'], p['batch'], len(images), 'images')
dump(D / 'WORK-QUEUE.json', queue)
record.update(status='requests_ready_pending_checkpoint', plans=plans)
dump(S / 'session-plan.json', record)
