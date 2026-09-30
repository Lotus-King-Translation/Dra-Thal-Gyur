"""Independent data, assembly, link and preservation checks for bounded Chapter 1 v1.
Passing these checks does not certify unexamined source glyphs or all witnesses.
"""
from pathlib import Path
import argparse, collections, hashlib, json, re, subprocess, sys
from urllib.parse import unquote
sys.dont_write_bytecode=True

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def require(test, message):
    if not test: raise ValueError(message)

def validate_data(machine, app, units, insertions, loci, diffs, choices, scans):
    anchors=machine['source_anchors']; sequence=machine['reading_sequence']
    require(len(anchors)==2635 and len({u['id'] for u in anchors})==2635,'Anchor loss or duplication')
    for old,new in zip(units,anchors):
        for key in ['id','source_tibetan','reading_tibetan','status']:
            require(old[key]==new[key],'Changed canonical anchor field: '+old['id']+'/'+key)
    ids=[s['id'] for s in sequence]; require(len(ids)==len(set(ids)),'Duplicate reading-sequence ID')
    require([s['id'] for s in sequence if s['id'].startswith('U')]==[u['id'] for u in units],'Original anchor order changed')
    byid={s['id']:s for s in sequence}
    for u in units: require(byid[u['id']]['text']==u['reading_tibetan'],'Selected reading changed: '+u['id'])
    require(machine['insertions']==insertions,'Insertion metadata or text changed')
    restored=[]
    for n in insertions:
        s=byid[n['id']]
        require(s.get('lines')==n['tibetan_lines'],'Restored line lost or changed: '+n['id'])
        require(s['text']=='\n'.join(n['tibetan_lines']),'Restored sequence text changed')
        require(ids.index(n['after_unit']) < ids.index(n['id']),'Insertion placed before its anchor')
        if n['before_unit'] in ids:
            require(ids.index(n['id']) < ids.index(n['before_unit']),'Insertion crosses its following anchor')
        if n['kind']=='main_text_restoration':
            require(s['role']=='restored_main_text','Restored verse misclassified')
            restored.extend(n['tibetan_lines'])
        elif n['kind']=='source_heading_restoration': require(s['role']=='source_heading','Restored heading counted as verse')
        elif n['kind']=='source_caption_provisional': require(s['role']=='provisional_caption','Caption in main text')
        elif n['kind']=='scan_only_unresolved': require(s['role']=='unresolved_inscription' and not s['text'],'Inscription conjecturally filled')
    heading_records=[n for n in app['scan_interventions'] if (n.get('annotation') or '').strip().startswith('དྲིས་ལན་')]
    expected_ids={u['id'] for u in units}|{n['id'] for n in insertions}|{n['id'] for n in heading_records}
    require(set(ids)==expected_ids,'Unexpected or missing reading-sequence content')
    for n in heading_records:
        s=byid[n['id']]
        require(s['text']==n['annotation'] and s['role']=='source_heading','Separate heading altered or misclassified')
    for u in units:
        uid=u['id']; t=u['reading_tibetan']; expected_role='main_text'
        if int(uid[1:])<=6: expected_role='opening_title_or_sign'
        elif uid in {'U00011','U00029'} or t.strip().startswith('དྲིས་ལན་'): expected_role='source_heading'
        elif uid=='U02635': expected_role='chapter_colophon'
        if not t: expected_role='joined_anchor' if uid=='U01812' else 'source_annotation_anchor'
        require(byid[uid]['role']==expected_role,'Original reading layer changed: '+uid)
    require(len(restored)==13,'Not thirteen restored main verses')
    groups=collections.defaultdict(list)
    for n in insertions: groups[n['after_unit']].append(n)
    for group in groups.values():
        ordered=sorted(group,key=lambda n:n['anchor_sequence'])
        require([n['id'] for n in sorted(group,key=lambda n:ids.index(n['id']))]==[n['id'] for n in ordered],'Insertion order changed')
    require(byid['U01812']['role']=='joined_anchor' and not byid['U01812']['text'],'Joined anchor duplicated')
    for uid in ['U00317','U00318','U01144','U01286','U01668','U01776','U01806','U01829','U02615','U02620']:
        require(not byid[uid]['text'] and byid[uid]['role']=='source_annotation_anchor','Note incorrectly enters main verse: '+uid)
    require(app['electronic_loci']==loci and app['exact_transcript_differences']==diffs,'A/B/S source data altered')
    require(app['release_choices']==choices['loci'],'Release choices not faithfully exported')
    require(app['comparison_scan_observations']==scans,'Comparison records altered or lost')
    require(len(app['scan_interventions'])==88 and len({n['id'] for n in app['scan_interventions']})==88,'Intervention missing or duplicated')
    for ident,c in app['release_choices'].items():
        require(bool(c['rationale']) and bool(c['evidence']),'Missing release rationale: '+ident)
    body_roles={'opening_title_or_sign','main_text','restored_main_text','source_heading','chapter_colophon'}
    expected='\n'.join(s['text'] for s in sequence if s['text'] and s['role'] in body_roles)
    require(expected==machine['main_and_headings_tibetan'],'Combined machine reading is inconsistent')
    require(not machine['exhaustive_witness_collation'],'False exhaustive witness certification')
    return {'source_anchors':2635,'restored_main_verses':13,'loci':183,'exact_differences':359,
            'interventions':88,'comparison_observations':len(scans),'sequence_items':len(sequence)}
def check_markdown(root,dest,machine):
    paths=list(dest.glob('*.md')); contents={p:p.read_text(encoding='utf-8') for p in paths}
    explicit={p:set(re.findall(r'<a id="([^"]+)"></a>',t)) for p,t in contents.items()}
    count=0; fragment_count=0
    for path,content in contents.items():
        ids=re.findall(r'<a id="([^"]+)"></a>',content)
        require(len(ids)==len(set(ids)),'Duplicate Markdown anchor: '+path.name)
        visible=re.sub(r'```.*?```','',content,flags=re.S)
        for target in re.findall(r'\[[^\]\n]*\]\(([^)]+)\)',visible):
            if re.match(r'^[a-z]+:',target): continue
            target=unquote(target); file,sep,frag=target.partition('#')
            resolved=(path.parent/file).resolve() if file else path.resolve()
            require(resolved.is_relative_to(root),'Link escapes repository')
            require(resolved.is_file(),'Broken link: '+path.name+' -> '+target)
            count+=1
            if frag and resolved in explicit:
                require(frag in explicit[resolved],'Broken release fragment: '+path.name+' -> '+target)
                fragment_count+=1
    reading=contents[dest/'reading.md']; matches=list(re.finditer(r'<a id="([^"]+)"></a>',reading))
    blocks={m.group(1):reading[m.end():matches[i+1].start() if i+1<len(matches) else len(reading)] for i,m in enumerate(matches)}
    for s in machine['reading_sequence']:
        require(s['id'].lower() in blocks,'Reading display segment absent: '+s['id'])
        block=blocks[s['id'].lower()]
        if s['text']: require(s['text'].strip() in block,'Tibetan display text changed: '+s['id'])
        if s['uncertainty_refs'] and s['role']!='unresolved_inscription':
            require('[uncertain]' in block,'Uncertainty flag missing from display: '+s['id'])
    return {'local_links_checked':count,'release_fragments_checked':fragment_count,
            'reading_segments_checked':len(machine['reading_sequence'])}
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--require-final',action='store_true')
    ap.add_argument('--output',type=Path)
    a=ap.parse_args(); root=a.repo.resolve(); dest=root/'diplomatic/release-v1'
    work=root/'diplomatic/release-v1-proposal'; col=root/'diplomatic/collation/chapter-01'
    machine=load(dest/'reading.json'); app=load(dest/'apparatus.json'); manifest=load(dest/'release-manifest.json')
    choices=load(work/'DECISIONS.json'); state=load(work/'RELEASE-STATE.json')
    units=load(col/'reading-units.json'); insertions=load(col/'ch1-scan-insertions.json')
    for path,digest in manifest['input_hashes'].items(): require(sha(root/path)==digest,'Input hash mismatch: '+path)
    for path,digest in manifest['output_hashes'].items(): require(sha(dest/path)==digest,'Output hash mismatch: '+path)
    checks=validate_data(machine,app,units,insertions,load(col/'chapter1-loci.json'),
        load(col/'chapter1-conflicts.json'),choices,load(col/'scan-comparison-loci.json'))
    require(app['wikisource_reference']==load(col/'wikisource-diffs.json'),'W reference data changed')
    expected_annotations={n['id']:n['annotation'] for n in app['scan_interventions'] if n.get('annotation')}
    require({n['record_id']:n['annotation'] for n in machine['source_annotations']}==expected_annotations,'Separate annotation lost')
    require(len(machine['source_annotations'])==len(expected_annotations),'Duplicated source annotation record')
    checks.update(check_markdown(root,dest,machine))
    rendered=(dest/'apparatus.md').read_text(encoding='utf-8')
    source_quotes=0
    for locus in app['electronic_loci']:
        marker='<a id="'+locus['id'].lower()+'"></a>'
        block=rendered.split(marker,1)[1].split('<a id="',1)[0]
        quoted=re.findall(r'```(text|json)\n(.*?)\n```',block,re.S)
        require(len(quoted)==4,'Unexpected quotation count at '+locus['id'])
        values=[json.loads(payload) if kind=='json' else payload for kind,payload in quoted[-3:]]
        require(values==[locus['readings'][s] for s in ['A','B','S']],'Rendered source quotation changed at '+locus['id'])
        source_quotes+=3
    checks['exact_rendered_source_quotations_checked']=source_quotes
    coverage=load(dest/'coverage.json')
    require(coverage['packet_deferrals']==choices['packet_deferrals'],'Deferrals concealed or changed')
    require(coverage['release_exceptions']==load(work/'RELEASE-EXCEPTIONS.json'),'Retained proposals absent')
    for name in ['U01239','U01286','U01522','U01557','U02489','U02615','U02620']:
        require(any(q['anchor']==name for q in coverage['base_reading_questions']),'Named uncertainty omitted: '+name)
    results=[]
    for script,extra in [('diplomatic/tools/validate_chapter1.py',['--check']),
                         ('diplomatic/tools/build_chapter1.py',['--check']),
                         ('diplomatic/release-v1-proposal/build_release.py',['--check'])]:
        p=subprocess.run([sys.executable,str(root/script),'--repo',str(root),*extra],cwd=root,text=True,capture_output=True)
        require(p.returncode==0,script+' failed: '+p.stdout+p.stderr)
        results.append({'command':script+' '+' '.join(extra),'result':json.loads(p.stdout)})
    sys.path.insert(0,str(root/'diplomatic/tools'))
    from release_progress import report as progress_report
    progress=progress_report(root)
    require(progress['packets']['remaining']==0,'Undispositioned frozen packet')
    require(progress['release_locus_acceptance']['remaining']==0,'Missing release choice')
    require(not progress['release_locus_acceptance']['invalid_entry_ids'],'Invalid release choice')
    require(progress['release_artifacts']['present']==5,'Missing deliverable group')
    signed=bool(choices.get('final_editorial_signoff'))
    if a.require_final:
        require(signed and state['status']=='released_bounded_v1','Final scoped signoff absent')
        require(choices['final_editorial_signoff']['scope']=='bounded_chapter_1_v1','Wrong signoff scope')
    result={'schema_version':1,'checks_passed':True,'counts_and_checks':checks,
        'hash_checked_inputs':len(manifest['input_hashes']),'hash_checked_outputs':len(manifest['output_hashes']),
        'reconstruction_and_build_checks':results,'progress':progress,
        'completed_for_approved_scope':a.require_final and signed,
        'exhaustive_witness_collation_complete':False,'accuracy_claim':None,
        'limits':'Validates exact data preservation, explicit release choices, layer assembly, links and reproducibility. Does not certify every manuscript reading or independently measure character accuracy.'}
    if a.output:
        path=a.output.resolve(); require(path.is_relative_to(root/'diplomatic'),'Output outside edition')
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
