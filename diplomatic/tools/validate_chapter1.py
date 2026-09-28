#!/usr/bin/env python3
"""Check lossless source accounting, curated interventions, evidence and edition links."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
from continuation_state import load_continuation


def verify_archives(root, out):
    """Check preserved bytes; historical links are evidence, not current navigation."""
    recovery = out / 'recovery'
    inventory_path = recovery / 'ARCHIVE-INVENTORY.json'
    inventory = json.loads(inventory_path.read_text())
    assert inventory['schema_version'] == 1, 'Unsupported archive inventory schema'
    assert inventory['file_count'] == len(inventory['files']), 'Archive file count differs'
    assert inventory['total_bytes'] == sum(entry['bytes'] for entry in inventory['files']), 'Archive total size differs'
    active = {inventory_path, recovery / 'README.md', recovery / 'CLOUD-INCIDENT.md'}
    paths = set()
    for entry in inventory['files']:
        path = (root / entry['path']).resolve()
        assert path.is_relative_to(recovery) and path not in active, path
        assert path not in paths, 'Duplicate archive inventory path: ' + str(path)
        payload = path.read_bytes()
        assert len(payload) == entry['bytes'], 'Archive size changed: ' + str(path)
        assert hashlib.sha256(payload).hexdigest() == entry['sha256'], 'Archive hash changed: ' + str(path)
        paths.add(path)
    actual = {p for p in recovery.rglob('*') if p.is_file()} - active
    assert paths == actual, {'uninventoried_archives': sorted(str(p) for p in actual - paths),
                             'absent_archives': sorted(str(p) for p in paths - actual)}
    return paths


def verify_work_queue(root, out, continuation):
    """Check resumable work identities and references, not scholarly conclusions."""
    queue = json.loads((out / continuation['work_queue']).read_text())
    assert queue['schema_version'] == 1, 'Unsupported work queue schema'
    assert queue['canonical_branch'] == continuation['canonical_branch']
    assert queue['current_chapter'] == 1
    assert queue['chapter_status'] == 'in_progress_not_ready'
    tasks = {task['id']: task for task in queue['tasks']}
    assert len(tasks) == len(queue['tasks']), 'Duplicate task IDs'
    states = {'pending', 'in_progress', 'blocked', 'done'}

    def state_check(item):
        ident = item['id']
        assert item['status'] in states, (ident, item['status'])
        if item['status'] == 'pending':
            assert item.get('owner') is None, 'Pending work cannot retain an owner: ' + ident
        if item['status'] == 'in_progress':
            assert item.get('owner'), 'In-progress work needs an owner: ' + ident
        if item['status'] == 'blocked':
            blocker = item.get('blocker')
            assert isinstance(blocker, dict) and blocker.get('reason') and blocker.get('next_step'), 'Blocked work needs a reason and next step: ' + ident

    def path_check(name, exists=True):
        assert isinstance(name, str) and not Path(name).is_absolute(), name
        path = (root / name).resolve()
        assert path.is_relative_to(root), name
        if exists:
            assert path.is_file(), 'Missing queue input/report/evidence: ' + name

    next_id = queue['next_task_id']
    assert next_id in tasks and tasks[next_id]['status'] != 'done', next_id
    assigned_candidates = {}
    for task in tasks.values():
        state_check(task)
        for dependency in task.get('depends_on', []):
            assert dependency in tasks and dependency != task['id'], (task['id'], dependency)
        for name in task.get('input_paths', []):
            path_check(name)
        for name in task.get('output_paths', []):
            path_check(name, exists=task['status'] == 'done')
        for name in task.get('report_paths', []):
            path_check(name)
        if task['status'] == 'in_progress':
            assert task.get('report_paths'), 'In-progress task needs a saved partial report: ' + task['id']
        if task['status'] == 'done':
            assert task.get('report_paths'), 'Completed task needs saved reports: ' + task['id']
            assert re.fullmatch('[a-f0-9]{40}', task.get('checkpoint_commit') or ''), 'Completed task needs a prior verified checkpoint commit: ' + task['id']
            if task.get('dependency_policy') == 'all_required_for_completion':
                assert all(tasks[ident]['status'] == 'done' for ident in task.get('depends_on', [])), 'Completion gate has unfinished dependencies: ' + task['id']
        for ident in task.get('candidate_ids', []):
            assert ident not in assigned_candidates, 'Candidate assigned twice: ' + ident
            assigned_candidates[ident] = task['id']

    candidates = queue['punctuation_candidates']
    expected = json.loads((out / 'reviews/chapter-01/readiness-audit-20260927.json').read_text())
    expected = expected['base_sign_candidate_work']['remaining_candidate_units']
    assert len({c['id'] for c in candidates}) == len(candidates), 'Duplicate candidate IDs'
    assert collections.Counter(c['anchor'] for c in candidates) == collections.Counter(expected)
    assert set(assigned_candidates) == {c['id'] for c in candidates}, 'Punctuation batch coverage differs'
    for candidate in candidates:
        ident = candidate['id']
        state_check(candidate)
        assert assigned_candidates[ident] == candidate['batch_id'], ident
        for name in candidate.get('historical_evidence_paths', []) + candidate.get('evidence_paths', []):
            path_check(name)
        path_check(candidate['historical_record']['path'])
        historical = json.loads((root / candidate['historical_record']['path']).read_text())
        pointer = candidate['historical_record']['json_pointer']
        assert pointer.startswith('/'), (ident, pointer)
        for part in pointer[1:].split('/'):
            part = part.replace('~1', '/').replace('~0', '~')
            historical = historical[int(part)] if isinstance(historical, list) else historical[part]
        if candidate.get('report_path'):
            path_check(candidate['report_path'])
        if candidate['status'] in {'in_progress', 'blocked'}:
            assert candidate.get('report_path'), 'Started or blocked candidate needs a saved partial report: ' + ident
        if candidate['status'] == 'done':
            assert candidate.get('report_path') and candidate.get('evidence_paths') and candidate.get('disposition'), ident
            assert candidate['disposition'] in queue['status_rules']['candidate_dispositions'] and candidate['disposition'] != 'unresolved', ident
        if tasks[candidate['batch_id']]['status'] == 'done':
            assert candidate['status'] == 'done', 'Completed batch has unfinished candidate: ' + ident
    return {'tasks_checked': len(tasks), 'punctuation_candidates_tracked': len(candidates),
            'punctuation_candidates_unfinished': sum(c['status'] != 'done' for c in candidates),
            'next_task_id': next_id}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--check', action='store_true',
                    help='Validate without writing VALIDATION.json or any other file')
    args=ap.parse_args();root=args.repo.resolve();out=root/'diplomatic';data=out/'collation/chapter-01'
    read=lambda n:json.loads((data/n).read_text())
    meta=read('chapter1-summary.json');texts={}
    for k,v in meta['sources'].items():
        raw=(root/v['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==v['full_file_sha256'],k
        texts[k]=raw.decode()[v['start']:v['end']]
        assert hashlib.sha256(texts[k].encode()).hexdigest()==v['chapter_sha256'],k
    src=json.loads((root/'translations/2026-09-26-full-draft/data/source-units.json').read_text())[:2635]
    original={x['id']:x['tibetan'] for x in src};assert ''.join(original.values())==texts['A']
    raw_loci=read('chapter1-conflicts.json');whole=read('chapter1-loci.json')
    patch_checks=[]
    for name,loci in [('minimal',raw_loci),('whole_unit',whole)]:
        for k in ('B','S'):
            cursor=0;result=[]
            for q in loci:
                a,b=q['offsets']['A'];c,e=q['offsets'][k]
                assert cursor<=a<=b, (name,k,q['id'])
                assert texts['A'][a:b]==q['readings']['A'],q['id']
                assert texts[k][c:e]==q['readings'][k],q['id']
                result.extend([texts['A'][cursor:a],q['readings'][k]]);cursor=b
            result.append(texts['A'][cursor:]);assert ''.join(result)==texts[k],(name,k)
            patch_checks.append(name+'_'+k+'_exact')
    refs=[i for q in whole for i in q['exact_conflicts']]
    assert collections.Counter(refs)==collections.Counter(q['id'] for q in raw_loci)
    proposed={};unit_note_ids=[]
    for q in read('ch1-opening-corrections.json'):
        assert original[q['unit']]==q['old'];proposed[q['unit']]=q['new'];unit_note_ids.append(q['id'])
    for q in read('ch1-key-scan-checks.json')['items']:
        assert all(original[k]==v for k,v in q['original_units'].items());unit_note_ids.append(q['id'])
        for j,uid in enumerate(q['units']):
            assert uid not in proposed;proposed[uid]=q['adopted_tibetan'] if j==0 else ''
    for q in read('additional-interventions.json'):
        assert all(original[k]==v for k,v in q['original_units'].items()),q['id'];unit_note_ids.append(q['id'])
        for uid,v in q['replacement_units'].items():assert uid not in proposed;proposed[uid]=v
    actual=read('reading-units.json');assert [x['id'] for x in actual]==list(original)
    for q in actual:
        assert q['source_tibetan']==original[q['id']]
        assert q['reading_tibetan']==proposed.get(q['id'],original[q['id']]),q['id']
    insertions=read('ch1-scan-insertions.json');assert len({x['id'] for x in insertions})==len(insertions)
    assert sum(len(x['tibetan_lines']) for x in insertions if x['kind']=='main_text_restoration')==13
    chapter=(out/'chapter-01.md').read_text()
    ids=re.findall(r'<a id="([^"]+)"',chapter);assert len(ids)==len(set(ids))
    for uid in original:assert uid.lower() in ids
    for uid in unit_note_ids+[x['id'] for x in insertions]+[x['id'] for x in read('scan-comparison-loci.json')]:assert uid.lower() in ids,uid
    for ins in insertions:
        start=chapter.index('<a id="'+ins['after_unit'].lower()+'"></a>')
        nextid=ins.get('before_unit')
        end=chapter.index('<a id="'+nextid.lower()+'"></a>') if nextid in original else chapter.index('## Scan interventions')
        segment=chapter[start:end]
        assert ']('+ '#'+ins['id'].lower()+')' in segment,ins['id']
        for line in ins['tibetan_lines']:assert line in segment,ins['id']
    # Active links are validated independently of the renderer. Historical files
    # retain their bytes, including obsolete paths; their integrity is checked
    # against the explicit archive inventory instead of rewriting those paths.
    archival_files = verify_archives(root, out)
    archival_context = {}
    for manifest in (out/'recovery').rglob('manifest-in-progress.json'):
        for entry in json.loads(manifest.read_text()).get('files', []):
            if not all(key in entry for key in ('original_path', 'recovered_path', 'sha256', 'bytes')):
                continue
            archived = (manifest.parent/entry['recovered_path']).resolve()
            assert archived.is_relative_to(out/'recovery'), archived
            payload = archived.read_bytes()
            assert len(payload) == entry['bytes'], archived
            assert hashlib.sha256(payload).hexdigest() == entry['sha256'], archived
            marker = '/Dra-Thal-Gyur/'
            assert marker in entry['original_path'], entry['original_path']
            logical = (root/entry['original_path'].split(marker, 1)[1]).resolve()
            assert logical.is_relative_to(root), logical
            archival_context[archived] = logical
    links=0;broken=[];historical_markdown=0;anchor_cache={}
    for p in out.rglob('*.md'):
        if p in archival_files:
            historical_markdown += 1
            continue
        logical = p
        for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',p.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
            name,_,frag=target.partition('#');dest=(logical.parent/name).resolve() if name else logical
            links+=1
            if not dest.exists():broken.append((str(p.relative_to(out)),target))
            elif frag and dest.suffix=='.md':
                if dest not in anchor_cache:
                    content=dest.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',content))
                    for h in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
                        h=re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-');anchors.add(h)
                    anchor_cache[dest]=anchors
                if frag not in anchor_cache[dest]:broken.append((str(p.relative_to(out)),target))
    assert not broken,broken
    insertion_map={x['id']:x for x in insertions}
    for rec in read('scan-comparison-loci.json'):
        start=chapter.index('<a id="'+rec['id'].lower()+'"></a>')
        end=chapter.find('<a id="',start+1)
        section=chapter[start:end if end!=-1 else len(chapter)]
        for ident in rec.get('insertion_ids',[]):
            assert ident in insertion_map,(rec['id'],ident)
            assert ']('+'#'+ident.lower()+')' in section,(rec['id'],ident)
            for line in insertion_map[ident]['tibetan_lines']:
                assert line in section,(rec['id'],ident,line)
    evidence_count=0
    def check_evidence(x):
        nonlocal evidence_count
        if isinstance(x,dict):
            for k,v in x.items():
                if k.startswith('evidence/') and isinstance(v,str) and re.fullmatch('[a-f0-9]{64}',v):
                    assert hashlib.sha256((out/k).read_bytes()).hexdigest()==v,k
                check_evidence(v)
        elif isinstance(x,list):
            for v in x:check_evidence(v)
        elif isinstance(x,str) and x.startswith('evidence/') and '\n' not in x and x.endswith(('.png','.jpeg','.jpg')):
            assert (out/x).is_file(),x;evidence_count+=1
    for p in data.glob('*.json'):check_evidence(json.loads(p.read_text()))
    status=json.loads((out/'STATUS.json').read_text());digest=hashlib.sha256((out/'chapter-01.md').read_bytes()).hexdigest()
    continuation = load_continuation(out)
    for key, value in continuation.items():
        assert status.get(key) == value, 'STATUS metadata is stale: ' + key
    queue_checks = verify_work_queue(root, out, continuation)
    assert status['chapter_markdown_sha256']==digest
    assert status['complete_chapters']==[] and status['next_chapter_started'] is False
    result={'scope':'Chapter 1 structural and preservation checks; not a complete-witness certificate','source_hashes_unchanged':True,'exact_reconstruction_checks':patch_checks,'base_units_accounted_for':len(actual),'curated_replacement_anchors':len(proposed),'scan_intervention_records':len(unit_note_ids),'restored_main_verses':13,'abc_exact_conflicts':len(raw_loci),'abc_readable_loci':len(whole),'local_comparison_findings_including_candidates':len(read('scan-comparison-loci.json')),'archival_files_hash_checked':len(archival_files),'original_manifest_files_hash_checked':len(archival_context),'historical_markdown_files_integrity_checked_not_link_checked':historical_markdown,'active_local_markdown_links_resolve':True,'local_links_checked':links,'evidence_references_checked':evidence_count,'continuation_metadata_matches':True,'chapter_complete':False,'all_witnesses_collated':False,'next_chapter_started':False,'markdown_sha256':digest}
    result['work_queue'] = queue_checks
    if not args.check:
        (out/'VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
