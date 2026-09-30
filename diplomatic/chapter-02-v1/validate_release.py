#!/usr/bin/env python3
"""Independent bounded-release consistency checks; not manuscript certification."""
from pathlib import Path
from urllib.parse import unquote
import argparse, collections, copy, hashlib, json, re, subprocess, sys
sys.dont_write_bytecode=True

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(value,message):
    if not value: raise ValueError(message)

def check_data(machine,app,units,decisions,interventions):
    require(machine['original_units']==units,'Original source units changed')
    seq=machine['reading_sequence']; ids=[u['id'] for u in seq]
    require(ids==[u['id'] for u in units] and len(ids)==987,'Original anchor loss/order change')
    require(app['decisions']=={k:decisions[k] for k in ['loci','W','source_checks']},'Decisions changed on export')
    require(app['interventions']==interventions,'Interventions lost or altered')
    chosen={u['id']:u for u in seq}; originals={u['id']:u for u in units}
    expected={u['id']:u['tibetan'] for u in units}; changed=set(); needed=collections.defaultdict(set)
    for rec in interventions:
        for uid,t in rec['original_units'].items(): require(originals[uid]['tibetan']==t,'Wrong original intervention text')
        for uid,t in rec['replacement_units'].items():
            require(uid not in changed,'Overlapping intervention'); expected[uid]=t; changed.add(uid)
        for uid in rec.get('uncertain_units',[]): needed[uid].add(rec['id'])
    for ident,c in decisions['loci'].items():
        for uid in c.get('uncertain_units',[]): needed[uid].add(ident)
    role_overrides={u:r for i in interventions for u,r in i.get('roles',{}).items()}
    for uid,item in chosen.items():
        require(item['text']==expected[uid],'Selected text changed: '+uid)
        require(set(item['uncertainty_refs'])==needed[uid],'Uncertainty flag lost/added: '+uid)
        role='main_text'
        if expected[uid].strip().startswith('དྲིས་ལན་'): role='source_heading'
        if uid in ['U03621','U03622']: role='chapter_colophon'
        if not expected[uid]: role=role_overrides.get(uid,'source_annotation_anchor')
        require(item['role']==role,'Wrong source layer: '+uid)
    notes=machine['source_annotations']
    expected_notes=[(i['id'],n['text'],n['role']) for i in interventions for n in i['annotations']]
    require([(n['record_id'],n['text'],n['role']) for n in notes]==expected_notes,'Source annotation lost or altered')
    require(len(notes)==len({n['id'] for n in notes})==9,'Duplicate/missing annotation identity')
    require(not machine['new_main_verse_restorations'],'Invented main verse')
    require(machine['transition_graphic']['reading'] is None and machine['transition_graphic']['not_main_verse'],'Invented graphic reading')
    require(not machine['full_base_scan_proofread'] and not machine['exhaustive_witness_collation'],'Inflated coverage claim')
    require(machine['text_with_headings']=='\n'.join(expected[u['id']] for u in units if expected[u['id']]),'Combined reading inconsistent')
    for l in app['collation']['loci']:
        c=decisions['loci'][l['id']]
        require(c['source_units']==l['source_units'] and c['exact_conflicts']==l['exact_conflicts'],'Decision misaligned')
        require(c['release_reading']=={u:expected[u] for u in l['source_units']},'Stale release choice')
    for b in app['W_reference']['conflicts']:
        c=decisions['W'][b['id']]
        require(c['source_units']==b['source_units'] and c['W_lines']==[q['line'] for q in b['W_lines']],'W decision misaligned')
    return {'source_anchors':len(ids),'changed_anchors':sum(originals[u]['tibetan']!=t for u,t in expected.items()),
            'source_annotations':len(notes),'uncertain_anchor_flags':sum(bool(v) for v in needed.values())}

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repo',required=True,type=Path)
    p.add_argument('--require-final',action='store_true'); p.add_argument('--output',type=Path)
    args=p.parse_args(); root=args.repo.resolve(); c=root/'diplomatic/chapter-02-v1'; out=c/'release'
    plan=load(c/'PLAN.json'); decisions=load(c/'DECISIONS.json'); state=load(c/'STATE.json')
    machine=load(out/'reading.json'); app=load(out/'apparatus.json'); manifest=load(out/'MANIFEST.json')
    units=load(c/'source-units.json'); interventions=load(c/'INTERVENTIONS.json')
    checks=check_data(machine,app,units,decisions,interventions)
    require(app['collation']==load(c/'collation.json'),'Frozen collation changed on export')
    require(app['W_reference']==load(c/'wikisource.json'),'W source ledger altered on export')
    require(app['source_review']==load(c/'SOURCE-REVIEW.json'),'Source observation lost')
    for path,h in manifest['input_hashes'].items(): require(sha(root/path)==h,'Input hash changed: '+path)
    for path,h in manifest['output_hashes'].items(): require(sha(out/path)==h,'Output hash changed: '+path)
    require(sha(root/manifest['generator']['path'])==manifest['generator']['sha256'],'Generator changed')
    for key,ids in [('loci',plan['frozen_locus_ids']),('W',plan['frozen_W_ids']),('source_checks',[s['id'] for s in plan['source_check_targets']])]:
        require(set(decisions[key])==set(ids),'Unfinished or expanded scope: '+key)
        for ident,item in decisions[key].items():
            require(item.get('status') and item.get('rationale') and item.get('evidence'),'Missing decision: '+ident)
            for path in item['evidence']: require((root/path.split('#')[0]).is_file(),'Missing evidence: '+path)
    texts={k:(root/s['path']).read_bytes().decode('utf-8') for k,s in plan['sources'].items()}
    chapter={}
    for k,s in plan['sources'].items():
        require(hashlib.sha256(texts[k].encode()).hexdigest()==s['full_sha256'],'Original transcript changed')
        chapter[k]=texts[k][s['start']:s['end']]
    require(''.join(u['tibetan'] for u in units)==chapter['A'],'Original chapter not completely accounted')
    for layer in ['differences','loci']:
        for k in ['B','S']:
            parts=[]; pos=0
            for item in app['collation'][layer]:
                a,b=item['chapter_offsets']['A']; require(a>=pos,'Overlapping source patch')
                for sig,(x,y) in item['chapter_offsets'].items():
                    require(chapter[sig][x:y]==item['readings'][sig],'Source quotation wrong')
                parts.extend([chapter['A'][pos:a],item['readings'][k]]); pos=b
            parts.append(chapter['A'][pos:]); require(''.join(parts)==chapter[k],'Failed exact reconstruction')
    wraw=(root/plan['W']['path']).read_bytes().decode('utf-8'); wl=wraw.splitlines(keepends=True)
    require(hashlib.sha256(wraw.encode()).hexdigest()==plan['W']['sha256'],'W source changed')
    ledger=app['W_reference']['line_ledger']; lo,hi=plan['W']['lines_inclusive']
    require([q['line'] for q in ledger]==list(range(lo,hi+1)),'Missing W source line')
    for q in ledger:
        require(q['raw']==wl[q['line']-1]==wraw[q['start']:q['end']],'W quotation mismatch')
    require(''.join(q['raw'] for q in ledger)==''.join(wl[lo-1:hi]),'W scope incomplete')
    checks['reconstruction_paths']=4; checks['W_source_lines_checked']=len(ledger)
    image_count=0
    for path in (c/'evidence').rglob('manifest.json'):
        m=load(path); entries=m if isinstance(m,list) else m['pages']+m['views']
        for item in entries:
            target=root/item['path'] if item['path'].startswith('diplomatic/') else c/item['path']
            require(sha(target)==item['sha256'],'Evidence image changed: '+str(target)); image_count+=1
    checks['evidence_image_hashes_checked']=image_count
    contents={p:p.read_text() for p in out.glob('*.md')}
    anchors={p:set(re.findall(r'<a id="([^"]+)"></a>',t)) for p,t in contents.items()}
    link_count=0
    for path,text in contents.items():
        ids=re.findall(r'<a id="([^"]+)"></a>',text); require(len(ids)==len(set(ids)),'Duplicate display anchor')
        visible=re.sub(r'```.*?```','',text,flags=re.S)
        for target in re.findall(r'\[[^\]\n]*\]\(([^)]+)\)',visible):
            if re.match(r'^[a-z]+:',target): continue
            file,sep,frag=unquote(target).partition('#'); resolved=(path.parent/file).resolve() if file else path
            require(resolved.is_relative_to(root) and resolved.is_file(),'Broken release link: '+target)
            if frag and resolved in anchors: require(frag in anchors[resolved],'Broken fragment: '+target)
            link_count+=1
    reading=contents[out/'reading.md']
    for u in machine['reading_sequence']:
        marker='<a id="'+u['id'].lower()+'"></a>'; require(marker in reading,'Missing displayed anchor')
        block=reading.split(marker,1)[1].split('<a id=',1)[0]
        if u['text']: require(u['text'].strip() in block,'Reading display changed')
        if u['uncertainty_refs']: require('[uncertain]' in block,'Uncertainty concealed in reading')
    rendered=contents[out/'apparatus.md']; source_quotes=0
    for l in app['collation']['loci']:
        block=rendered.split('<a id="'+l['id'].lower()+'"></a>',1)[1].split('<a id=',1)[0]
        quotes=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',block,re.S)]
        require(quotes==[decisions['loci'][l['id']]['release_reading']]+[l['readings'][s] for s in ['A','B','S']],'Displayed locus quotation changed')
        source_quotes+=3
    checks['release_links_checked']=link_count; checks['exact_displayed_transcript_quotes']=source_quotes
    rendered=contents[out/'wikisource.md']
    for b in app['W_reference']['conflicts']:
        block=rendered.split('<a id="'+b['id'].lower()+'"></a>',1)[1].split('<a id=',1)[0]
        quotes=[json.loads(x) for x in re.findall(r'```json\n(.*?)\n```',block,re.S)]
        require(quotes==[b['A_tibetan'],b['A_wylie'],b['W_lines'],b['token_differences']],'Displayed W comparison changed')
    checks['W_display_blocks_checked']=105
    for script in ['collate.py','build_release.py']:
        result=subprocess.run([sys.executable,str(c/script),'--repo',str(root),'--check'],cwd=root,text=True,capture_output=True)
        require(result.returncode==0,'Reproducibility failed: '+result.stdout+result.stderr)
    require(machine['release_state']==state['status']==manifest['release_state'],'Release states disagree')
    unchanged=subprocess.check_output(['git','diff','chapter-01-v1.0.0','--','diplomatic/release-v1'],cwd=root)
    require(not unchanged,'Chapter1 tagged deliverables changed')
    receipts=subprocess.check_output(['git','diff',plan['baseline_commit'],'--','diplomatic/release-v1-proposal'],cwd=root)
    require(not receipts,'Chapter1 working records changed since Chapter2 intake')
    signed=bool(decisions['final_signoff'])
    if args.require_final:
        require(signed and state['status']=='released_bounded_v1','Final editorial signoff missing')
        require(plan['status']=='released_bounded_v1','Plan not released')
    result={'schema_version':1,'checks_passed':True,'counts':checks,
        'transcript_loci':56,'W_blocks':105,'source_checks':10,'deliverable_groups':5,
        'source_data_and_reconstruction_passed':True,'build_reproducible':True,'chapter1_release_unchanged':True,
        'completed_for_approved_scope':bool(args.require_final and signed),
        'full_base_scan_proofread':False,'exhaustive_witness_collation':False,
        'limits':'Exact data, decisions, layer assembly, display and link checks; not an accuracy measurement or complete manuscript proofread.'}
    if args.output: args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
