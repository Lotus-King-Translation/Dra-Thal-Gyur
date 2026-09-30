"""Independent preservation, assembly and release-gate checks for Chapter 4."""
from pathlib import Path
import argparse, collections, hashlib, json, re, subprocess, sys
from urllib.parse import unquote
sys.dont_write_bytecode=True

def load(path): return json.loads(path.read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def require(test,message):
    if not test: raise ValueError(message)
def inside(root,value):
    path=(root/value.split('#')[0]).resolve()
    require(path.is_relative_to(root),'Reference escapes repository')
    return path

def validate_data(machine,app,units,ints,insertions,d,col,w,review):
    require(machine['original_units']==units,'Original source units altered')
    anchors=machine['anchors']; seq=machine['reading_sequence']
    require(len(anchors)==458 and [a['id'] for a in anchors]==[u['id'] for u in units],'Original anchors lost, duplicated or reordered')
    byid={u['id']:u for u in units}; replacements={}; links=collections.defaultdict(list)
    flags=collections.defaultdict(list); expected_notes=[]
    for rec in ints:
        for uid,text in rec['original_units'].items(): require(byid[uid]['tibetan']==text,'Intervention original mismatch')
        for uid,text in rec['replacement_units'].items():
            require(uid not in replacements and uid in byid,'Overlapping or unknown replacement')
            replacements[uid]=text
        for uid in rec['units']: links[uid].append(rec['id'])
        for uid in rec.get('uncertain_units',[]): flags[uid].append(rec['id'])
        for n,note in enumerate(rec['annotations'],1):
            expected_notes.append({'id':rec['id']+'-N'+str(n),'intervention_id':rec['id'],'units':rec['units'],**note})
    locusmap=collections.defaultdict(list); wmap=collections.defaultdict(list)
    require(set(d['loci'])=={l['id'] for l in col['loci']},'Release choices missing or invented')
    for l in col['loci']:
        dec=d['loci'][l['id']]
        require(dec['status'] in {'retain_base','adopt_evidenced_correction','retain_with_explicit_uncertainty'},'Invalid choice status')
        require(dec['source_units']==l['source_units'] and dec['exact_conflicts']==l['exact_conflicts'],'Choice mapped to wrong passage')
        require(dec['release_reading']=={uid:replacements.get(uid,byid[uid]['tibetan']) for uid in l['source_units']},'Choice reading drift')
        require(bool(dec['rationale']) and bool(dec['evidence']),'Missing choice justification')
        for uid in l['source_units']: locusmap[uid].append(l['id'])
        for uid in dec.get('uncertain_units',[]): flags[uid].append(l['id'])
    require(set(d['W'])=={b['id'] for b in w['conflicts']},'Missing W decisions')
    for b in w['conflicts']:
        dec=d['W'][b['id']]
        require(dec['source_units']==b['source_units'] and dec['W_lines']==[x['line'] for x in b['W_lines']],'W decision mapping drift')
        require(dec['source_before']==b['source_before'] and dec['source_after']==b['source_after'],'W flank mapping drift')
        for uid in b['source_units']: wmap[uid].append(b['id'])
    require(d['W']['W-C04-003']['insertion_ids']==['A2000-C04-S01'],'W restoration link absent')
    require(d['loci']['L4-0002']['insertion_ids']==['A2000-C04-S01'],'A/B/S restoration link absent')
    for old,a in zip(units,anchors):
        uid=old['id']; text=replacements.get(uid,old['tibetan'])
        role='source_heading' if text.lstrip().startswith(('ཞུས་དོན་','ཞུས་ལན་')) else 'main_text'
        if uid in {'U04762','U04763'}: role='chapter_colophon'
        require(a['source_tibetan']==old['tibetan'] and a['source_wylie']==old['wylie'],'Original anchor quotation changed')
        require(a['selected_tibetan']==text and a['role']==role,'Selected text or layer altered')
        require(a['uncertainty_refs']==flags[uid],'Reading uncertainty concealed or inflated')
        require(a['intervention_ids']==links[uid] and a['locus_ids']==locusmap[uid] and a['W_ids']==wmap[uid],'Reading links lost')
    require(machine['source_annotations']==expected_notes,'Separate source annotation altered, lost or duplicated')
    require(len(expected_notes)==2,'Wrong annotation count')
    require(machine['scan_insertions']==insertions,'Restoration metadata changed')
    expected_sequence=[]
    for a in anchors:
        expected_sequence.append({'id':a['id'],'anchor_id':a['id'],'role':a['role'],
            'text':a['selected_tibetan'],'uncertainty_refs':a['uncertainty_refs']})
        for ins in sorted([i for i in insertions if i['after_unit']==a['id']],key=lambda i:i['anchor_sequence']):
            require(ins['before_unit'] in byid,'Restoration following anchor absent')
            expected_sequence.append({'id':ins['id'],'anchor_id':a['id'],'role':'restored_main_text',
                'text':'\n'.join(ins['tibetan_lines']),'lines':ins['tibetan_lines'],
                'uncertainty_refs':[],'punctuation_policy':ins['punctuation_policy']})
    end=next(r for r in review['items'] if r['id']=='C4-END')['transition_graphic']
    expected_sequence.append({'id':end['id'],'anchor_id':'U04763','role':'unresolved_source_graphic','text':'','uncertainty_refs':['C4-END']})
    require(seq==expected_sequence,'Reading sequence, insertion order or undecoded boundary changed')
    require(len({s['id'] for s in seq})==len(seq),'Duplicated reading-sequence ID')
    require(machine['transition_graphic']==end and end['reading'] is None,'Invented boundary reading')
    require(machine['main_and_headings_tibetan']=='\n'.join(s['text'] for s in seq if s['text']),'Combined text is inconsistent')
    require(app['collation']==col and app['wikisource']==w and app['release_decisions']==d,'Apparatus or decision export changed')
    require(app['interventions']==ints and app['insertions']==insertions and app['source_review']==review,'Source apparatus evidence lost')
    require(not machine['full_base_scan_proofread'] and not machine['exhaustive_witness_collation'],'Inflated coverage claim')
    require(machine['unicode_normalization']=='none','Unapproved normalization claim')
    return {'original_anchors':len(anchors),'reading_sequence_items':len(seq),'source_annotations':len(expected_notes),
            'restored_main_verses':sum(len(i['tibetan_lines']) for i in insertions),'choices_cross_checked':len(d['loci'])}
def check_sources(root,c,p,units,col,w):
    global_units=load(root/'translations/2026-09-26-full-draft/data/source-units.json')
    require(units==global_units[4305:4763],'Chapter units differ from immutable source anchors')
    streams={}
    for k,m in p['sources'].items():
        path=inside(root,m['path']); require(sha(path)==m['full_sha256'],'Original transcript changed')
        streams[k]=path.read_bytes().decode('utf-8')[m['start']:m['end']]
        require(hashlib.sha256(streams[k].encode()).hexdigest()==m['chapter_sha256'],'Chapter slice changed')
    require(''.join(u['tibetan'] for u in units)==streams['A'],'A anchor assembly differs')
    checks=0
    for records in [col['differences'],col['loci']]:
        for k in ['B','S']:
            pieces=[]; pos=0
            for rec in records:
                x,y=rec['chapter_offsets']['A']
                require(x>=pos and y>=x,'Overlapping apparatus spans')
                for sig in ['A','B','S']:
                    lo,hi=rec['chapter_offsets'][sig]
                    require(rec['readings'][sig]==streams[sig][lo:hi],'Apparatus quotation changed')
                    require(rec['full_source_offsets'][sig]==[lo+p['sources'][sig]['start'],hi+p['sources'][sig]['start']],'Global offsets changed')
                pieces.extend([streams['A'][pos:x],rec['readings'][k]]); pos=y
            pieces.append(streams['A'][pos:]); require(''.join(pieces)==streams[k],'Exact reconstruction failed')
            checks+=1
    rawpath=inside(root,p['W']['path']); require(sha(rawpath)==p['W']['sha256'],'W source changed')
    raw=rawpath.read_text(); rawlines=raw.splitlines(keepends=True); lo,hi=p['W']['lines_inclusive']
    require(''.join(x['raw'] for x in w['line_ledger'])==''.join(rawlines[lo-1:hi]),'W line accounting changed')
    for x in w['line_ledger']:
        require(raw[x['start']:x['end']]==x['raw'] and rawlines[x['line']-1]==x['raw'],'W line offset mismatch')
    return {'exact_reconstruction_paths':checks,'W_raw_lines_checked':len(w['line_ledger'])}

def check_display(root,dest,machine,col,w):
    docs={p:p.read_text(encoding='utf-8') for p in dest.glob('*.md')}
    allids={p:set(re.findall(r'<a id="([^"]+)"></a>',text)) for p,text in docs.items()}
    links=0
    for path,text in docs.items():
        ids=re.findall(r'<a id="([^"]+)"></a>',text); require(len(ids)==len(set(ids)),'Duplicate HTML anchor')
        visible=re.sub(r'```.*?```','',text,flags=re.S)
        for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)',visible):
            if re.match(r'^[a-z]+:',target): continue
            file,sep,frag=unquote(target).partition('#'); other=(path.parent/file).resolve() if file else path.resolve()
            require(other.is_relative_to(root) and other.is_file(),'Broken local link: '+target)
            if frag and other in allids: require(frag in allids[other],'Broken release fragment: '+target)
            links+=1
    def blocks(text):
        matches=list(re.finditer(r'<a id="([^"]+)"></a>',text))
        return {m.group(1):text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)] for i,m in enumerate(matches)}
    displayed=blocks(docs[dest/'reading.md'])
    for s in machine['reading_sequence']:
        require(s['id'].lower() in displayed,'Reading segment missing')
        text=displayed[s['id'].lower()]
        if s['text']: require(s['text'].strip() in text,'Selected display text changed')
        if s['uncertainty_refs'] and s['role']!='unresolved_source_graphic':
            require('[uncertain]' in text,'Inline uncertainty concealed')
    appblocks=blocks(docs[dest/'apparatus.md']); quotes=0
    for l in col['loci']:
        pairs=re.findall(r'```(text|json)\n(.*?)\n```',appblocks[l['id'].lower()],re.S)
        require(len(pairs)==4,'Wrong number of locus quotations')
        values=[json.loads(v) if typ=='json' else v for typ,v in pairs[-3:]]
        require(values==[l['readings'][sig] for sig in ['A','B','S']],'Rendered transcript quotation changed')
        quotes+=3
    wb=blocks(docs[dest/'wikisource.md'])
    for b in w['conflicts']:
        values=[json.loads(v) for v in re.findall(r'```json\n(.*?)\n```',wb[b['id'].lower()],re.S)]
        require(values==[b['A_tibetan'],b['A_wylie'],b['W_lines'],b['token_differences']],'Rendered W block changed')
    return {'local_release_links_checked':links,'exact_displayed_transcript_quotes':quotes,'W_display_blocks_checked':len(w['conflicts'])}

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--require-final',action='store_true'); ap.add_argument('--output',type=Path)
    a=ap.parse_args(); root=a.repo.resolve(); c=root/'diplomatic/chapter-04-v1'; dest=c/'release'
    p=load(c/'PLAN.json'); d=load(c/'DECISIONS.json'); units=load(c/'source-units.json')
    col=load(c/'collation.json'); w=load(c/'wikisource.json'); ints=load(c/'INTERVENTIONS.json')
    ins=load(c/'INSERTIONS.json'); review=load(c/'SOURCE-REVIEW.json'); state=load(c/'STATE.json')
    m=load(dest/'reading.json'); app=load(dest/'apparatus.json'); manifest=load(dest/'MANIFEST.json')
    for path,h in manifest['input_hashes'].items(): require(sha(inside(root,path))==h,'Input hash mismatch: '+path)
    for name,h in manifest['output_hashes'].items(): require(sha(dest/name)==h,'Output hash mismatch: '+name)
    require(manifest['generator_sha256']==sha(c/'build_release.py'),'Serializer hash mismatch')
    counts=validate_data(m,app,units,ints,ins,d,col,w,review)
    counts.update(check_sources(root,c,p,units,col,w)); counts.update(check_display(root,dest,m,col,w))
    image_count=0
    for path in sorted((c/'evidence').glob('E*/manifest.json')):
        packet=load(path)
        for item in packet['pages']+packet['views']:
            require(sha(inside(root,item['path']))==item['sha256'],'Evidence image hash mismatch'); image_count+=1
    for item in load(c/'evidence/focused/manifest.json'):
        require(sha(c/item['path'])==item['sha256'],'Focused image changed')
        require(sha(c/'evidence'/item['source'])==item['source_sha256'],'Focus source changed'); image_count+=1
    counts['evidence_image_hashes_checked']=image_count
    for group in ['loci','W','source_checks']:
        for ident,dec in d[group].items():
            require(bool(dec['status']) and bool(dec['rationale']) and bool(dec['evidence']),'Incomplete disposition')
            for path in dec['evidence']: require(inside(root,path).is_file(),'Missing decision evidence')
    require(set(d['source_checks'])=={t['id'] for t in p['source_check_targets']},'Source-check task missing')
    require({r['id'] for r in review['items']}==set(d['source_checks']),'Source report/disposition mismatch')
    require(len(review['items'])==8,'Duplicated source review')
    ids=[s['id'] for s in m['reading_sequence']]
    for item in ins:
        require(ids.index(item['after_unit'])<ids.index(item['id'])<ids.index(item['before_unit']),'Restoration outside its flanks')
    require(sum(len(i['tibetan_lines']) for i in ins)==3,'Restored verse loss or duplication')
    require(m['release_state']==state['status']==manifest['state'],'Release state mismatch')
    build_results=[]
    for script in ['collate.py','build_release.py']:
        proc=subprocess.run([sys.executable,str(c/script),'--repo',str(root),'--check'],cwd=root,text=True,capture_output=True)
        require(proc.returncode==0,script+' failed: '+proc.stderr+proc.stdout)
        build_results.append(json.loads(proc.stdout))
    for tag,path in [('chapter-01-v1.0.0','diplomatic/release-v1'),('chapter-02-v1.0.0','diplomatic/chapter-02-v1/release'),
                     (p['baseline_commit'],'diplomatic/release-v1-proposal'),(p['baseline_commit'],'diplomatic/chapter-02-v1'),
                     ('chapter-03-v1.0.0','diplomatic/chapter-03-v1/release'),(p['baseline_commit'],'diplomatic/chapter-03-v1')]:
        changed=subprocess.check_output(['git','diff','--name-only',tag,'--',path],cwd=root,text=True)
        require(not changed,'Previous release changed: '+changed)
    if a.require_final:
        require(state['status']=='released_bounded_v1' and bool(d.get('final_signoff')),'Final scoped signoff absent')
        require(d['final_signoff']['scope']=='bounded_chapter_4_v1','Wrong signoff scope')
        require(p['status']=='released_bounded_v1','Plan does not match final release')
    result={'schema_version':1,'checks_passed':True,'counts':counts,'transcript_loci':33,'W_blocks':55,
        'source_checks':8,'deliverable_groups':5,'original_source_preservation':True,'prior_releases_unchanged':True,
        'build_checks':build_results,'completed_for_approved_scope':bool(a.require_final),
        'full_base_scan_proofread':False,'exhaustive_witness_collation':False,
        'limits':'Checks source preservation, reconstruction, explicit decisions, annotation/restoration assembly and display. Not a character-accuracy estimate or independent human manuscript certification.'}
    if a.output:
        target=a.output.resolve(); require(target.is_relative_to(c),'Validation output outside chapter directory')
        target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
