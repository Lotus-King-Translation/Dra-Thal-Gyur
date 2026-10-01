"""Independent coverage, preservation, display and publication-gate checks."""
from pathlib import Path
import argparse, collections, hashlib, json, re, subprocess, sys, urllib.parse
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
B=ROOT/'translations/2026-09-26-full-draft'; R=B/'golden-review'
OUT=ROOT/'translations/2026-10-01-golden-aligned'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(x,message):
    if not x: raise ValueError(message)
def q(x): return '`'+json.dumps(x,ensure_ascii=False).replace('`','\\u0060')+'`'
def validate_data(m,g,e,d,plan):
    seq=m['reading_sequence']; gold=g['reading_sequence']; originals={u['id']:u for u in g['original_units']}
    require(len(seq)==5484 and [s['id'] for s in seq]==[s['id'] for s in gold],'Missing, duplicated or reordered golden objects')
    require(len({s['id'] for s in seq})==5484,'Duplicate identifier')
    require([s['id'] for s in seq if s['id'] in originals]==list(originals),'Original anchor coverage/order')
    require(len(originals)==len(e)==5466,'Original count')
    changed={i for i,u in originals.items() if next(s['text'] for s in gold if s['id']==i)!=u['tibetan']}
    require(changed==set(plan['changed_anchor_ids']) and len(changed)==110,'Exact difference set changed')
    require({s['id'] for s in gold if s['id'] not in originals}==set(plan['extra_object_ids']),'Golden extra set changed')
    notes=d['anchor_decisions']+d['extra_decisions']+d['supplemental_notes']
    bynote={n['note_id']:n for n in notes}; require(len(notes)==len(bynote)==173,'Note count/uniqueness')
    require({n['id'] for n in d['anchor_decisions']}==changed,'Missing changed-anchor review')
    require({n['id'] for n in d['extra_decisions']}==set(plan['extra_object_ids']),'Missing extra-object review')
    direct={n['id']:n for n in notes if n['id']!='C2-BOUNDARY-METADATA'}
    require({n['note_id']:n for n in m['endnotes']}==bynote and len(m['endnotes'])==173,'Endnote export changed')
    refs=collections.defaultdict(list)
    for n in notes: refs[n.get('attach_to',n['id'])].append(n['note_id'])
    original_ann={}
    for layer in g['source_annotation_layers']:
        for a in layer['annotations']: original_ann[a.get('id',a.get('record_id'))]=(layer['chapter'],a)
    anns=m['source_annotations']
    require(anns==d['source_annotation_components'] and len(anns)==65,'Source annotation export changed')
    require({a['id'] for a in anns}==set(original_ann),'Source annotation lost/duplicated')
    for a in anns:
        chapter,record=original_ann[a['id']]
        require(a['golden_record']==record and a['chapter']==chapter,'Golden annotation record changed')
        require(bool(a['english'].strip()) and a['endnote_owner'] in bynote,'Missing source-note English or owner')
        for u in record['units']: refs[u].append(a['endnote_owner'])
    restored=0; empty=0; uncertain=0; en_changes=0
    for s,t in zip(seq,gold):
        uid=s['id']; old=e.get(uid); dec=direct.get(uid)
        require(s['golden_tibetan']==t['text'] and s['golden_role']==t['role'],'Golden string or layer drift: '+uid)
        require(s['chapter']==t['chapter'],'Wrong chapter: '+uid)
        expected_part=7 if uid in originals and int(uid[1:])>=5449 else t['chapter']
        require(s['part']==expected_part,'Wrong closing/chapter boundary: '+uid)
        require(s['golden_uncertainty_refs']==t.get('uncertainty_refs',[]),'Hidden/inflated uncertainty: '+uid)
        if old:
            for field,prior in [('original_tibetan','tibetan'),('original_english','english'),('legacy_note_ids','notes'),('legacy_english_provenance','english_provenance')]:
                require(s[field]==old[prior],'Original translation/metadata changed: '+uid+' '+field)
            require(old['tibetan']==originals[uid]['tibetan'],'Baseline source discrepancy: '+uid)
        else: require(s['original_tibetan'] is None and s['original_english'] is None,'Invented original for extra')
        expected=dec['english_selected'] if dec else old['english']
        require(s['english']==expected,'Unrecorded English change: '+uid)
        require(s['endnote_ids']==list(dict.fromkeys(refs[uid])),'Missing/misplaced note reference: '+uid)
        if s['golden_uncertainty_refs']: uncertain+=1; require(bool(s['endnote_ids']),'Unannotated golden uncertainty')
        if old and s['english']!=old['english']: en_changes+=1
        if t['role']=='restored_main_text':
            count=len(t['text'].splitlines()); restored+=count
            require(len(s['english'].splitlines())==count and all(x.strip() for x in s['english'].splitlines()),'Lost restored English verse: '+uid)
        if t['role'] in ['source_annotation_anchor','joined_anchor']:
            empty+=1; require(s['english']=='','Non-main text returned to root: '+uid)
        else: require(bool(s['english'].strip()),'Missing English or unresolved marker: '+uid)
        if dec and 'adzom_tibetan' in dec:
            require(dec['adzom_tibetan']==originals[uid]['tibetan'] and dec['golden_tibetan']==t['text'],'Wrong exact note quotations: '+uid)
            require(dec['english_current']==old['english'],'Old English quotation changed: '+uid)
    require(restored==23 and empty==16 and uncertain==72,'Restoration, non-main, or uncertainty count')
    require(m['additional_golden_metadata']==g['additional_preserved_metadata'],'Boundary metadata changed')
    require(len([s for s in seq if s['part']==7])==18,'Lost full-work closing material')
    require(not m['independent_human_qc'] and not m['unchanged_passages_fresh_semantic_qc'],'Unsupported QC claim')
    require(m['counts']==d['counts'] and m['provisional_usages']==d['provisional_usages'],'Counts/usages export drift')
    require(m['golden_release']=='root-tantra-v1.0.0','Wrong golden version')
    return {'original_anchors':5466,'reading_objects':5484,'changed_Tibetan_anchors_endnoted':110,
        'extra_golden_objects':18,'restored_English_verses':restored,'source_annotations':65,
        'golden_uncertainty_objects':uncertain,'new_endnotes':173,'English_anchor_strings_changed_including_layer_moves':en_changes,
        'non_main_or_joined_anchors':empty,'closing_anchors':18}
def footnote_check(text,expected):
    definitions=re.findall(r'^\[\^(G-[^\]]+)\]:',text,re.M)
    uses=re.findall(r'\[\^(G-[^\]]+)\](?!:)',text)
    require(len(definitions)==len(set(definitions)),'Duplicate footnote definition')
    require(set(definitions)==set(uses)==set(expected),'Missing/orphan/undefined footnote')
    return len(definitions)
def no_code(text):
    text=re.sub(r'(?ms)^\s*```[^\n]*\n.*?^\s*```\s*$', '',text)
    return re.sub(r'`[^`\n]*`','',text)
def explicit_anchors(text): return set(re.findall(r'<a id="([^"]+)"></a>',text))
def check_links(files):
    cache={}; count=0
    for path,text in files.items():
        for raw in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',no_code(text)):
            if re.match(r'^[A-Za-z]+:',raw): continue
            href,sep,fragment=raw.partition('#'); target=(path.parent/urllib.parse.unquote(href)).resolve() if href else path
            require(target.is_file(),'Missing link target: '+str(path)+' -> '+raw)
            if sep:
                if target not in cache:
                    t=target.read_text(encoding='utf-8'); anchors=explicit_anchors(t)
                    for heading in re.findall(r'^#{1,6} (.+)$',t,re.M):
                        slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-'); anchors.add(slug)
                    cache[target]=anchors
                require(urllib.parse.unquote(fragment) in cache[target],'Missing link fragment: '+str(path)+' -> '+raw)
            count+=1
    return count
def validate_display(m,d):
    seq=m['reading_sequence']; notes=m['endnotes']; count=0; displayed=0
    readers=[OUT/'Dra-Thal-Gyur-English.md']+sorted((OUT/'chapters').glob('*.md'))
    require(len(readers)==8,'Missing chapter reader')
    note_by={n['note_id']:n for n in notes}
    for path in readers:
        text=path.read_text(encoding='utf-8'); body=text.split('## Golden-source footnotes and endnotes',1)[0]
        if path.parent.name=='chapters':
            n=7 if path.stem=='closing-material' else int(path.stem.split('-')[1]); items=[s for s in seq if s['part']==n]
        else: items=seq
        expected_ids={i for s in items for i in s['endnote_ids']}
        count+=footnote_check(text,expected_ids)
        ids=re.findall(r'<a id="([^"]+)"></a>',body); actual=[i for i in ids if not i.startswith('part-')]
        require(actual==[s['id'].lower() for s in items],'Reader omits/reorders source anchors: '+path.name)
        for s in items:
            start=body.index('<a id="'+s['id'].lower()+'"></a>'); end=body.find('<a id=',start+10)
            block=body[start:end if end!=-1 else None]
            require(re.findall(r'\[\^(G-[^\]]+)\]',block)==s['endnote_ids'],'Reader note misplaced: '+s['id'])
            plain=re.sub(r'\[(N-[^\]]+)\]\([^)]+\)',r'[\1]',block).replace('<br />\n','\n')
            if s['english']: require(s['english'] in plain,'Reader English differs from machine: '+s['id'])
            displayed+=1
        definitions=re.split(r'^\[\^(G-[^\]]+)\]: ',text,flags=re.M)
        for i in range(1,len(definitions),2):
            n=note_by[definitions[i]]; block=definitions[i+1]
            require(n['reason'] in block,'Missing footnote reason')
            for key in ['adzom_tibetan','golden_tibetan','english_current','english_selected']:
                if key in n: require(q(n[key]) in block,'Exact footnote quotation changed: '+n['id']+' '+key)
    text=(OUT/'ENDNOTES.md').read_text(encoding='utf-8')
    require(explicit_anchors(text)=={n['note_id'].lower() for n in notes},'Endnote inventory mismatch')
    require(len(re.findall(r'<a id=',text))==173,'Duplicate endnote anchor')
    for n in notes:
        start=text.index('<a id="'+n['note_id'].lower()+'"></a>'); end=text.find('<a id=',start+10)
        block=text[start:end if end!=-1 else None]
        for key in ['adzom_tibetan','golden_tibetan','english_current','english_selected']:
            if key in n: require(q(n[key]) in block,'Exact endnote quotation changed: '+n['id']+' '+key)
        for a in m['source_annotations']:
            if a['endnote_owner']==n['note_id']: require(a['english'] in block,'Missing source annotation English: '+a['id'])
    for a in m['source_annotations']:
        require(a['english'] in (OUT/'SOURCE-ANNOTATIONS.md').read_text(encoding='utf-8'),'Source-note rendering missing')
    require(load(OUT/'SOURCE-ANNOTATIONS.json')==m['source_annotations'],'Source-note machine file changed')
    return {'reader_footnote_definitions_checked':count,'reader_objects_checked':displayed,'exact_endnote_records_checked':173}
def final_gate():
    path=R/'SIGNOFF.json'; require(path.is_file(),'Final editorial signoff absent')
    signoff=load(path); require(signoff.get('scope')=='golden_source_difference_reconciliation','Wrong signoff scope')
    require(signoff.get('unchanged_verses_fresh_semantic_qc') is False,'Signoff overstates semantic QC')
    for p,h in signoff['input_hashes'].items(): require(sha(ROOT/p)==h,'Signed input changed: '+p)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--require-final',action='store_true'); ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    inputs=load(R/'INPUTS.json')
    for p,h in inputs['input_hashes'].items(): require(sha(ROOT/p)==h,'Protected baseline changed: '+p)
    manifest=load(OUT/'MANIFEST.json')
    for name,h in manifest['output_hashes'].items(): require(sha(OUT/name)==h,'Rendered file changed: '+name)
    for p,h in manifest['review_inputs'].items(): require(sha(ROOT/p)==h,'Reviewed input changed: '+p)
    require(sha(R/'build_translation.py')==manifest['builder_sha256'],'Builder changed')
    m=load(OUT/'edition.json'); g=load(ROOT/'diplomatic/root-tantra-v1/release/reading.json'); d=load(R/'DECISIONS.json'); plan=load(R/'PLAN.json')
    e={r['id']:r for r in (json.loads(l) for l in (B/'ALIGNED.jsonl').read_text().splitlines() if l.strip())}
    counts=validate_data(m,g,e,d,plan); counts.update(validate_display(m,d))
    counts['local_links_checked']=check_links({p:p.read_text(encoding='utf-8') for p in OUT.rglob('*.md')})
    history=[json.loads(l) for l in (B/'data/scan-only-units.jsonl').read_text().splitlines() if l.strip()]
    require(m['historical_scan_only_records']==history,'Old scan-only records changed')
    p=subprocess.run([sys.executable,'-B',str(R/'build_translation.py'),'--check'],capture_output=True,text=True,cwd=ROOT)
    require(p.returncode==0,'Nonreproducible translation: '+p.stdout+p.stderr)
    require(subprocess.check_output(['git','diff','root-tantra-v1.0.0','--','diplomatic/root-tantra-v1/release'],cwd=ROOT)==b'','Golden release changed')
    counts['protected_input_hashes']=len(inputs['input_hashes'])
    if args.require_final: final_gate()
    report={'schema_version':1,'checks_passed':True,'final_gate_passed':args.require_final,'counts':counts,
       'source_comparison_complete':True,'all_changed_source_anchors_endnoted':True,'original_English_preserved':True,
       'golden_edition_and_glossary_unchanged':True,'reproducible':True,'unchanged_passages_fresh_semantic_qc':False,
       'limits':'Coverage, exact preservation, display, references and source-impact reconciliation; not an independent human translation-accuracy certification.'}
    if args.output: args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
