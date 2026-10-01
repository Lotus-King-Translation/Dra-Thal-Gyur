#!/usr/bin/env python3
"""Independent preservation and release-gate checks for Chapter 6 plus closing material."""
from pathlib import Path
import argparse, collections, hashlib, json, re, subprocess, sys
sys.dont_write_bytecode=True
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def req(x,m):
    if not x: raise ValueError(m)

def validate_data(m,app,units,ints,ins,d,col,w,review):
    req(m['original_units']==units,'Original source units altered')
    req(len(m['anchors'])==269 and [a['id'] for a in m['anchors']]==[u['id'] for u in units],'Anchor loss/order')
    byid={u['id']:u for u in units}; flags=collections.defaultdict(list)
    ilinks=collections.defaultdict(list); lmap=collections.defaultdict(list); wmap=collections.defaultdict(list)
    for rec in ints:
        req(not rec['replacement_units'],'Unexpected anchor replacement')
        for uid,t in rec['original_units'].items(): req(byid[uid]['tibetan']==t,'Intervention original drift')
        for uid in rec['units']: ilinks[uid].append(rec['id'])
        for uid in rec.get('uncertain_units',[]): flags[uid].append(rec['id'])
    req(set(d['loci'])=={x['id'] for x in col['loci']},'Missing/invented A/B/S decision')
    for l in col['loci']:
        dec=d['loci'][l['id']]
        req(dec['source_units']==l['source_units'] and dec['exact_conflicts']==l['exact_conflicts'],'Locus mapping drift')
        req(dec['release_reading']=={u:byid[u]['tibetan'] for u in l['source_units']},'Release reading drift')
        for uid in l['source_units']: lmap[uid].append(l['id'])
        for uid in dec.get('uncertain_units',[]): flags[uid].append(l['id'])
    req(set(d['W'])=={x['id'] for x in w['conflicts']},'Missing/invented W decision')
    for b in w['conflicts']:
        dec=d['W'][b['id']]
        req(dec['source_units']==b['source_units'],'W anchor mapping drift')
        req(dec['source_before']==b['source_before'] and dec['source_after']==b['source_after'],'W flank drift')
        req(dec['W_lines']==[x['line'] for x in b['W_lines']],'W line mapping drift')
        for uid in b['source_units']: wmap[uid].append(b['id'])
    req(d['loci']['L6-0011'].get('insertion_ids')==['A2000-C06-S01'],'A/B/S restoration link absent')
    req(d['W']['W-C06-021'].get('insertion_ids')==['A2000-C06-S01'],'W restoration link absent')
    for u,a in zip(units,m['anchors']):
        uid=u['id']
        if uid in d['closing_units']: role=d['closing_units'][uid]['role']
        elif uid in {'U05447','U05448'}: role='chapter_colophon'
        elif u['tibetan'].lstrip().startswith('ཞུས་ལན་'): role='source_heading'
        else: role='main_text'
        req(a['source_tibetan']==u['tibetan'] and a['selected_tibetan']==u['tibetan'],'Anchor string changed')
        req(a['source_wylie']==u['wylie'] and a['role']==role,'Role/source Wylie drift')
        req(a['uncertainty_refs']==flags[uid],'Uncertainty hidden/inflated')
        req(a['intervention_ids']==ilinks[uid] and a['locus_ids']==lmap[uid] and a['W_ids']==wmap[uid],'Anchor links drift')
    req(m['source_annotations']==[],'Invented source annotations')
    req(m['scan_insertions']==ins,'Restoration metadata drift')
    expected=[]
    after=collections.defaultdict(list)
    for x in ins: after[x['after_unit']].append(x)
    for a in m['anchors']:
        expected.append({'id':a['id'],'anchor_id':a['id'],'role':a['role'],'text':a['selected_tibetan'],'uncertainty_refs':a['uncertainty_refs']})
        for x in sorted(after[a['id']],key=lambda q:q['anchor_sequence']):
            expected.append({'id':x['id'],'anchor_id':a['id'],'role':'restored_main_text','text':'\n'.join(x['tibetan_lines']),
                             'lines':x['tibetan_lines'],'uncertainty_refs':[],'punctuation_policy':x['punctuation_policy']})
    req(m['reading_sequence']==expected,'Sequence/restoration order drift')
    req(len(expected)==270 and sum(len(x['tibetan_lines']) for x in ins)==2,'Sequence/restoration count')
    req(m['main_and_closing_tibetan']=='\n'.join(x['text'] for x in expected if x['text']),'Combined reading drift')
    req(app['collation']==col and app['wikisource']==w and app['release_decisions']==d,'Apparatus/decision export drift')
    req(app['interventions']==ints and app['insertions']==ins and app['source_review']==review,'Evidence export drift')
    req(len(d['closing_units'])==18 and set(d['closing_units'])=={f'U{x:05d}' for x in range(5449,5467)},'Closing coverage drift')
    for uid,dec in d['closing_units'].items():
        req(dec['source_tibetan']==byid[uid]['tibetan'] and dec['selected_tibetan']==byid[uid]['tibetan'],'Closing string drift')
    req(not m['full_base_scan_proofread'] and not m['exhaustive_witness_collation'],'Inflated coverage')
    return {'original_anchors':269,'reading_sequence_items':270,'restored_main_verses':2,'closing_anchors':18,'choices_cross_checked':13}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True,type=Path); ap.add_argument('--require-final',action='store_true'); ap.add_argument('--output',type=Path)
    a=ap.parse_args(); root=a.repo.resolve(); c=root/'diplomatic/chapter-06-v1'; dest=c/'release'
    p=load(c/'PLAN.json'); d=load(c/'DECISIONS.json'); units=load(c/'source-units.json'); col=load(c/'collation.json')
    w=load(c/'wikisource.json'); ints=load(c/'INTERVENTIONS.json'); ins=load(c/'INSERTIONS.json'); review=load(c/'SOURCE-REVIEW.json'); state=load(c/'STATE.json')
    m=load(dest/'reading.json'); app=load(dest/'apparatus.json'); manifest=load(dest/'MANIFEST.json')
    for path,h in manifest['input_hashes'].items(): req(sha(root/path)==h,'Input hash mismatch: '+path)
    for name,h in manifest['output_hashes'].items(): req(sha(dest/name)==h,'Output hash mismatch: '+name)
    req(manifest['generator_sha256']==sha(c/'build_release.py'),'Serializer hash mismatch')
    counts=validate_data(m,app,units,ints,ins,d,col,w,review)
    global_units=load(root/'translations/2026-09-26-full-draft/data/source-units.json')
    req(units==global_units[5197:5466],'Immutable source-anchor slice changed')
    streams={}
    for k,s in p['sources'].items():
        req(sha(root/s['path'])==s['full_sha256'],'Original transcript changed '+k)
        streams[k]=(root/s['path']).read_text()[s['start']:s['end']]
        req(hashlib.sha256(streams[k].encode()).hexdigest()==s['chapter_sha256'],'Chapter slice changed '+k)
    req(''.join(u['tibetan'] for u in units)==streams['A'],'A assembly mismatch')
    recon=0
    for records in [col['differences'],col['loci']]:
        for k in ['B','S']:
            parts=[]; at=0
            for rec in records:
                x,y=rec['chapter_offsets']['A']
                for sig in ['A','B','S']:
                    lo,hi=rec['chapter_offsets'][sig]; req(rec['readings'][sig]==streams[sig][lo:hi],'Exact quote drift')
                parts += [streams['A'][at:x],rec['readings'][k]]; at=y
            parts.append(streams['A'][at:]); req(''.join(parts)==streams[k],'Exact reconstruction failed '+k); recon+=1
    counts['exact_reconstruction_paths']=recon
    raw=(root/p['W']['path']).read_text(); lines=raw.splitlines(keepends=True)
    req(''.join(x['raw'] for x in w['line_ledger'])==''.join(lines[p['W']['lines_inclusive'][0]-1:p['W']['lines_inclusive'][1]]),'W line accounting drift')
    counts['W_raw_lines_checked']=len(w['line_ledger'])
    for group in ['loci','W','source_checks','closing_units']:
        for dec in d[group].values():
            req(bool(dec['status']) and bool(dec['rationale']) and bool(dec['evidence']),'Incomplete disposition')
            for path in dec['evidence']: req((root/path).is_file(),'Missing evidence '+path)
    for tag,path in [('chapter-01-v1.0.0','diplomatic/release-v1'),('chapter-02-v1.0.0','diplomatic/chapter-02-v1/release'),
                     ('chapter-03-v1.0.0','diplomatic/chapter-03-v1/release'),('chapter-04-v1.0.0','diplomatic/chapter-04-v1/release'),
                     ('chapter-05-v1.0.0','diplomatic/chapter-05-v1/release')]:
        changed=subprocess.check_output(['git','diff','--name-only',tag,'--',path],cwd=root,text=True)
        req(not changed,'Previous release changed: '+changed)
    proc=subprocess.run([sys.executable,str(c/'build_release.py'),'--repo',str(root),'--check'],cwd=root,text=True,capture_output=True)
    req(proc.returncode==0,'Release build not reproducible: '+proc.stdout+proc.stderr)
    if a.require_final:
        req(state['status']=='released_bounded_v1' and bool(d['final_signoff']),'Final signoff absent')
        req(d['final_signoff']['scope']=='bounded_chapter_6_v1','Wrong final signoff scope')
        req(p['status']=='released_bounded_v1','Plan final state mismatch')
    result={'schema_version':1,'checks_passed':True,'counts':counts,'transcript_loci':13,'W_blocks':28,'source_checks':13,
            'closing_anchors':18,'deliverable_groups':5,'original_source_preservation':True,'prior_releases_unchanged':True,
            'completed_for_approved_scope':bool(a.require_final),'full_base_scan_proofread':False,'exhaustive_witness_collation':False,
            'limits':'Preservation, exact reconstruction, explicit decisions, restoration order and closing-role checks; not a manuscript-accuracy score.'}
    if a.output: a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
