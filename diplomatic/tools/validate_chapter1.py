#!/usr/bin/env python3
"""Check lossless source accounting, curated interventions, evidence and edition links."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
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
    # Validate paths independently of the renderer, across the complete documentation tree.
    links=0;broken=[]
    for p in out.rglob('*.md'):
        for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',p.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
            name,_,frag=target.partition('#');dest=(p.parent/name).resolve() if name else p
            links+=1
            if not dest.exists():broken.append((str(p.relative_to(out)),target))
            elif frag and dest.suffix=='.md':
                content=dest.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',content))
                for h in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
                    h=re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-');anchors.add(h)
                if frag not in anchors:broken.append((str(p.relative_to(out)),target))
    assert not broken,broken
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
    assert status['chapter_markdown_sha256']==digest
    assert status['complete_chapters']==[] and status['next_chapter_started'] is False
    result={'scope':'Chapter1 second-reading checkpoint; not a complete-witness certificate','source_hashes_unchanged':True,'exact_reconstruction_checks':patch_checks,'base_units_accounted_for':len(actual),'curated_replacement_anchors':len(proposed),'scan_intervention_records':len(unit_note_ids),'restored_main_verses':13,'abc_exact_conflicts':len(raw_loci),'abc_readable_loci':len(whole),'local_comparison_findings_including_candidates':len(read('scan-comparison-loci.json')),'all_local_markdown_links_resolve':True,'local_links_checked':links,'evidence_references_checked':evidence_count,'chapter_complete':False,'all_witnesses_collated':False,'next_chapter_started':False,'markdown_sha256':digest}
    (out/'VALIDATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
