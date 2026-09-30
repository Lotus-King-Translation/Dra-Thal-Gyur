"""Audit whole-root source accounting without creating editorial decisions."""
from pathlib import Path
import argparse, hashlib, json, subprocess

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok, message):
    if not ok: raise ValueError(message)
def audit(root):
    base=root/'diplomatic'; original=load(root/'translations/2026-09-26-full-draft/data/source-units.json')
    require(len(original)==5466,'Unexpected original-anchor universe')
    ranges=[(1,2635),(2636,3622),(3623,4305),(4306,4763),(4764,5197),(5198,5466)]
    parts=[]; source_spans={k:[] for k in ['A','B','S']}; restored=[]; prior_files={}
    for n,(first,last) in enumerate(ranges,1):
        folder=base/('release-v1' if n==1 else f'chapter-{n:02d}-v1/release')
        plan=(load(base/'collation/chapter-01/chapter1-summary.json') if n==1
              else load(base/f'chapter-{n:02d}-v1/PLAN.json'))
        expected=original[first-1:last]; machine_path=folder/'reading.json'
        machine=load(machine_path) if machine_path.exists() else None
        if n==1:
            require([a['id'] for a in machine['source_anchors']]==[a['id'] for a in expected],'Chapter1 anchor order')
            require([a['source_tibetan'] for a in machine['source_anchors']]==[a['tibetan'] for a in expected],'Chapter1 original words')
        elif machine:
            require(machine['original_units']==expected,f'Chapter{n} original units')
        else:
            require(load(base/f'chapter-{n:02d}-v1/source-units.json')==expected,'Unreleased source slice mismatch')
        for sig,meta in plan['sources'].items():
            path=root/meta['path']; h=meta.get('full_sha256',meta.get('full_file_sha256'))
            require(digest(path)==h,'Original source hash changed: '+sig)
            text=path.read_bytes().decode('utf-8')[meta['start']:meta['end']]
            require(hashlib.sha256(text.encode()).hexdigest()==meta['chapter_sha256'],'Source slice hash')
            source_spans[sig].append({'chapter':n,'start':meta['start'],'end':meta['end'],'path':meta['path']})
        ins=(machine['insertions'] if n==1 else load(base/f'chapter-{n:02d}-v1/INSERTIONS.json')) if n!=2 else []
        for item in ins:
            if item['kind']!='main_text_restoration': continue
            if machine:
                matches=[s for s in machine['reading_sequence'] if s['id']==item['id']]
                require(len(matches)==1,'Restoration omitted or duplicated: '+item['id'])
            restored.append({'chapter':n,'id':item['id'],'verses':len(item['tibetan_lines']),
                'after':item['after_unit'],'before':item['before_unit'],'assembled':bool(machine)})
        tag=f'chapter-{n:02d}-v1.0.0'
        proc=subprocess.run(['git','rev-parse','--verify',tag+'^{commit}'],cwd=root,text=True,capture_output=True)
        released=proc.returncode==0 and bool(machine)
        if released:
            diff=subprocess.check_output(['git','diff','--name-only',tag,'--',str(folder.relative_to(root))],cwd=root,text=True)
            require(not diff,'Tagged release has changed: '+tag)
            prior_files[str(machine_path.relative_to(root))]=digest(machine_path)
        parts.append({'chapter':n,'first_anchor':expected[0]['id'],'last_anchor':expected[-1]['id'],
            'original_anchors':len(expected),'released':released,'tag':tag if released else None,
            'release_commit':proc.stdout.strip() if released else None,
            'closing_anchors_included':18 if n==6 else 0})
    for sig,spans in source_spans.items():
        full=(root/spans[0]['path']).read_bytes().decode('utf-8'); pos=0; pieces=[]
        for span in spans:
            require(span['start']==pos,'Gap or overlap in '+sig); pos=span['end']
            pieces.append(full[span['start']:span['end']])
        require(pos==len(full) and ''.join(pieces)==full,'Unaccounted source tail: '+sig)
    ids=[u['id'] for u in original]
    require(ids==[f'U{i:05d}' for i in range(1,5467)],'Original anchors not complete')
    require(''.join(u['tibetan'] for u in original)==(root/source_spans['A'][0]['path']).read_text(),'Original A reconstruction')
    first=load(base/'release-v1/reading.json')
    opening=[s['id'] for s in first['reading_sequence'] if s['role']=='opening_title_or_sign']
    require(opening,'Opening/title material missing')
    last=load(base/'chapter-06-v1/DECISIONS.json')['closing_units']
    require(set(last)=={f'U{i:05d}' for i in range(5449,5467)},'Closing decisions missing')
    return {'schema_version':1,'inventory_checks_passed':True,'editorial_completion':all(p['released'] for p in parts),
        'original_anchor_count':5466,'unallocated_original_anchors':0,'source_gaps_or_overlaps':0,
        'source_characters':{s:v[-1]['end'] for s,v in source_spans.items()},'source_spans':source_spans,
        'parts':parts,'opening_title_or_sign_anchors':opening,'closing_anchor_count':18,
        'restored_main_verses':sum(x['verses'] for x in restored),'restorations':restored,
        'verified_unchanged_release_files':prior_files,'missing_additional_chapter':False,
        'limits':'Inventory proves source-span and anchor accounting, not exhaustive scan proofreading or correctness of every glyph. Unreleased part and unassembled restorations remain explicitly identified.'}

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--check',action='store_true'); a=p.parse_args(); root=a.repo.resolve()
    value=audit(root); text=json.dumps(value,ensure_ascii=False,indent=2)+'\n'
    target=root/'diplomatic/root-tantra-v1/INVENTORY.json'
    if a.check: require(target.read_text()==text,'Inventory is stale')
    else: target.write_text(text,encoding='utf-8')
    print(json.dumps({k:value[k] for k in ['inventory_checks_passed','editorial_completion','original_anchor_count','unallocated_original_anchors','source_gaps_or_overlaps','restored_main_verses']},indent=2))

if __name__=='__main__': main()
