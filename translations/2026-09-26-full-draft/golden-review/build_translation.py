"""Render the reviewed English revision with actual Markdown footnotes/endnotes."""
from pathlib import Path
import argparse, collections, hashlib, json, os, re, sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
B=ROOT/'translations/2026-09-26-full-draft'; R=B/'golden-review'
OUT=ROOT/'translations/2026-10-01-golden-aligned'
GOLD=ROOT/'diplomatic/root-tantra-v1/release'
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def js(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def quoted(x): return '`'+json.dumps(x,ensure_ascii=False).replace('`','\\u0060')+'`'
def link(path,fromfile,label):
    path,sep,frag=str(path).partition('#')
    return '['+label+']('+os.path.relpath(path,fromfile.parent).replace(os.sep,'/')+(sep+frag if sep else '')+')'
def legacy(text,fromfile):
    return re.sub(r'\[(N-[A-Za-z0-9-]+)\]',lambda m:link(str(OUT/'LEGACY-NOTES.md')+'#'+m[1].lower(),fromfile,m[1]),text)
def pname(n): return f'chapter-{n:02d}' if n<7 else 'closing-material'
def title(n): return f'Chapter {n}' if n<7 else 'Full-work colophon and closing material'
def part(s): return 7 if s['id'].startswith('U') and int(s['id'][1:])>=5449 else s['chapter']
def make():
    for path,h in load(R/'INPUTS.json')['input_hashes'].items():
        if sha(ROOT/path)!=h: raise ValueError('Protected input changed: '+path)
    D=load(R/'DECISIONS.json'); G=load(GOLD/'reading.json')
    E={r['id']:r for r in (json.loads(l) for l in (B/'ALIGNED.jsonl').read_text().splitlines() if l.strip())}
    historical_scan=[json.loads(l) for l in (B/'data/scan-only-units.jsonl').read_text().splitlines() if l.strip()]
    notes=D['anchor_decisions']+D['extra_decisions']+D['supplemental_notes']
    bynote={n['note_id']:n for n in notes}; direct={n['id']:n for n in notes if n['id']!='C2-BOUNDARY-METADATA'}
    annotations=D['source_annotation_components']; owners=collections.defaultdict(list)
    for a in annotations: owners[a['endnote_owner']].append(a)
    refs=collections.defaultdict(list)
    for n in notes: refs[n.get('attach_to',n['id'])].append(n['note_id'])
    for a in annotations:
        for uid in a['golden_record']['units']: refs[uid].append(a['endnote_owner'])
    sequence=[]
    for s in G['reading_sequence']:
        uid=s['id']; old=E.get(uid); note=direct.get(uid)
        en=note['english_selected'] if note else old['english']
        if not old and not note: raise ValueError('Missing extra translation: '+uid)
        status=('non_main_anchor_endnoted' if s['role']=='source_annotation_anchor' else 'joined_anchor_endnoted' if s['role']=='joined_anchor' else 'unresolved_nonmain_graphic' if not s['text'] else 'provisional_restoration_translation' if s['role']=='restored_main_text' else 'provisional_caption' if s['role']=='provisional_caption' else 'translated_with_source_qualification' if s.get('uncertainty_refs') else 'translated')
        sequence.append({'id':uid,'chapter':s['chapter'],'part':part(s),'golden_role':s['role'],
          'golden_tibetan':s['text'],'original_tibetan':old['tibetan'] if old else None,
          'original_english':old['english'] if old else None,'english':en,'coverage_status':status,
          'golden_uncertainty_refs':s.get('uncertainty_refs',[]),'endnote_ids':list(dict.fromkeys(refs[uid])),
          'legacy_note_ids':old['notes'] if old else [],'legacy_english_provenance':old['english_provenance'] if old else [],
          'review_scope':'source-difference/qualification review' if note else 'source compared; prior translation inherited, not independently retranslated'})
    order={s['id']:i for i,s in enumerate(sequence)}
    notes.sort(key=lambda n:(order[n.get('attach_to',n['id'])],n['note_id']))
    machine={'schema_version':1,'version':'translation-golden-aligned-v1.0.0','golden_release':'root-tantra-v1.0.0',
      'scope':D['scope'],'translation_baseline_commit':D['translation_baseline'],'reading_sequence':sequence,
      'source_annotations':annotations,'additional_golden_metadata':G['additional_preserved_metadata'],
      'historical_scan_only_records':historical_scan,'endnotes':notes,'provisional_usages':D['provisional_usages'],
      'counts':D['counts'],'independent_human_qc':False,'unchanged_passages_fresh_semantic_qc':False}
    def evidence(n,fromfile):
        c=n['chapter']; app=ROOT/('diplomatic/release-v1/apparatus.json' if c==1 else f'diplomatic/chapter-{c:02d}-v1/release/apparatus.json')
        return link(app,fromfile,'released chapter apparatus')+'; '+link(str(GOLD/'reading.md')+'#'+n.get('attach_to',n['id']).lower(),fromfile,'golden reading')+'; '+link(R/'DECISIONS.json',fromfile,'review decision record')
    def note_text(n,fromfile):
        lines=['**'+n['note_id']+' — '+n['id']+'**','',n['reason'],'']
        if 'adzom_tibetan' in n: lines += ['**Supplied Adzom e-text:** '+quoted(n['adzom_tibetan']),'']
        if 'golden_tibetan' in n: lines += ['**Golden selected text / layer:** '+quoted(n['golden_tibetan']),'']
        if 'english_current' in n: lines += ['**Previous English, preserved:** '+quoted(n['english_current']),'']
        if 'english_selected' in n: lines += ['**Current English:** '+quoted(n['english_selected']),'']
        if n['id'] in ['A2000-C01-S08','A2000-C01-S09']:
            oldscan=next(x for x in historical_scan if x['id']==('S0001' if n['id'].endswith('S08') else 'S0002'))
            lines += ['**Earlier scan-only record (not a second occurrence):** '+quoted(oldscan['id'])+' — '+quoted(oldscan['english']),'']
        if n.get('golden_uncertainty_refs'): lines += ['**Inherited golden qualifications:** '+', '.join(n['golden_uncertainty_refs']),'']
        if n.get('golden_metadata'): lines += ['**Preserved non-main metadata:** '+quoted(n['golden_metadata']),'']
        for a in owners[n['note_id']]:
            s=a['golden_record']; lines += ['**Separate source note '+a['id']+':**','']
            for field in ['text','annotation','scan_annotation']:
                if s.get(field) is not None: lines += [field+': '+quoted(s[field]),'']
            lines += ['English: '+a['english'],'','Source qualification: '+s.get('remaining_uncertainty',s.get('status','Qualified source layer')),'']
        others={a['endnote_owner'] for a in annotations if a['id'] in n.get('annotation_ids',[]) and a['endnote_owner']!=n['note_id']}
        if others: lines += ['**Related source-note records:** '+', '.join(link(str(OUT/'ENDNOTES.md')+'#'+i.lower(),fromfile,i) for i in sorted(others)),'']
        refs=E.get(n['id'],{}).get('notes',[])
        if refs: lines += ['**Earlier translation notes:** '+', '.join(link(str(OUT/'LEGACY-NOTES.md')+'#'+i.lower(),fromfile,i) for i in refs)+'. Earlier source statements are historical where superseded by this golden-source note.','']
        lines += ['**Confidence / limit:** '+n['confidence'],'','**Evidence:** '+evidence(n,fromfile),
                  '', '**Review boundary:** No new scan reading or change to the golden Tibetan/glossary is made. Interpretive supplies and unresolved components remain open where stated.']
        return '\n'.join(lines)
    def footnotes(ids,fromfile):
        blocks=[]
        for n in notes:
            if n['note_id'] not in ids: continue
            lines=note_text(n,fromfile).splitlines()
            blocks.append('[^'+n['note_id']+']: '+lines[0]+'\n'+'\n'.join(('    '+l) if l else '' for l in lines[1:]))
        return '\n\n'.join(blocks)+'\n'
    def render_reading(items,fromfile,heading):
        lines=['# '+heading,'','**Golden-aligned annotated English revision — translation-golden-aligned-v1.0.0**','',
          'Based on the fixed root-tantra-v1.0.0. The earlier English draft is preserved unchanged. The comparison covers all 5,466 original anchors; every changed source string and added golden object is endnoted.','',
          'Adzom e-text means the supplied digital transcription, not the facsimile itself. Many golden changes recover the Adzom scan or separate its smaller notes. Footnotes retain the old wording and explain the selected treatment.','',
          'This is a complete source-difference reconciliation, not independent human certification of every inherited translation. Bracketed supplies, unresolved source forms, and provisional interpretations remain visible.','',
          link(OUT/'ENDNOTES.md',fromfile,'All golden-source endnotes')+' · '+link(OUT/'SOURCE-ANNOTATIONS.md',fromfile,'Source annotations')+' · '+link(OUT/'REVIEW.md',fromfile,'Review scope and results'),'']
        used=set(); current=None
        for s in items:
            if s['part']!=current:
                current=s['part']; lines += ['<a id="part-'+str(current)+'"></a>','## '+title(current),'']
            lines += ['<a id="'+s['id'].lower()+'"></a>','']
            en=legacy(s['english'],fromfile).replace('\n','<br />\n'); role=s['golden_role']
            note_refs=''.join('[^'+i+']' for i in s['endnote_ids']); used.update(s['endnote_ids'])
            if role=='source_annotation_anchor': lines += ['*Source annotation moved to endnotes; no root verse at '+s['id']+'.*'+note_refs,'']
            elif role=='joined_anchor': lines += ['*Joined source fragment; no additional root text at '+s['id']+'.*'+note_refs,'']
            elif role=='source_heading': lines += ['**'+en+'**'+note_refs,'']
            elif role=='restored_main_text': lines += ['*Scan-restored main verses:*'+note_refs,'',en,'']
            elif role in ['provisional_caption','unresolved_inscription','unresolved_source_graphic']: lines += ['*'+en+'*'+note_refs,'']
            else: lines += [en+note_refs,'']
        lines += ['## Golden-source footnotes and endnotes','',footnotes(used,fromfile)]
        return '\n'.join(lines)
    outputs={'edition.json':js(machine),'Dra-Thal-Gyur-English.md':render_reading(sequence,OUT/'Dra-Thal-Gyur-English.md','Dra Thal Gyur — golden-aligned English translation')}
    for n in range(1,8):
        name='chapters/'+pname(n)+'.md'
        outputs[name]=render_reading([s for s in sequence if s['part']==n],OUT/name,title(n))
    endfile=OUT/'ENDNOTES.md'
    outputs['ENDNOTES.md']='# Golden-edition reconciliation endnotes\n\nAll 173 records are also actual footnotes in the annotated reading. Earlier English is preserved verbatim; source-note translations and unresolved components remain distinct from root text.\n\n'+'\n\n'.join('<a id="'+n['note_id'].lower()+'"></a>\n\n## '+n['note_id']+'\n\n'+note_text(n,endfile) for n in notes)
    for n in range(1,8):
        name='alignment/'+pname(n)+'.md'; here=OUT/name
        lines=['# '+title(n)+' — Adzom / golden / English alignment','',
          'Exact source strings and both English versions. An unchanged Tibetan unit is not a claim of fresh independent semantic QC.','']
        for s in sequence:
            if s['part']!=n: continue
            lines += ['<a id="'+s['id'].lower()+'"></a>','## '+s['id']+' — '+s['golden_role'],'',
              '**Original Adzom e-text:** '+quoted(s['original_tibetan']),'',
              '**Golden selected string:** '+quoted(s['golden_tibetan']),'',
              '**Earlier English:** '+quoted(s['original_english']),'',
              '**Current English:** '+quoted(s['english']),'',
              '**Coverage:** '+s['coverage_status']+'. '+s['review_scope']+'.','',
              '**Endnotes:** '+', '.join(link(str(OUT/'ENDNOTES.md')+'#'+i.lower(),here,i) for i in s['endnote_ids']),'']
        outputs[name]='\n'.join(lines)
    here=OUT/'SOURCE-ANNOTATIONS.md'; lines=['# Separate source annotations','',
        'All 65 golden annotation components remain present. Transcriptions with unresolved lettering remain qualified. Quotations at more than one note do not imply multiple physical occurrences.','']
    for a in annotations:
        s=a['golden_record']; lines += ['<a id="'+a['id'].lower()+'"></a>','## '+a['id'],'',
            '**Locations:** '+', '.join(s['units'])+'.','',
            '**Complete golden source record:**','```json',js(s).rstrip(),'```','',
            '**English source-note rendering:** '+a['english'],'',
            '**Owning endnote:** '+link(str(OUT/'ENDNOTES.md')+'#'+a['endnote_owner'].lower(),here,a['endnote_owner']),'']
    outputs['SOURCE-ANNOTATIONS.md']='\n'.join(lines)
    outputs['SOURCE-ANNOTATIONS.json']=js(annotations)
    coverage=[{k:s[k] for k in ['id','chapter','part','golden_role','coverage_status','review_scope','endnote_ids','golden_uncertainty_refs']} for s in sequence]
    outputs['COVERAGE.json']=js({'scope':D['scope'],'counts':D['counts'],'sequence':coverage})
    outputs['USAGES.json']=js({'new_canonical_glossary_assignments':0,'glossary_unchanged':True,'records':D['provisional_usages']})
    legacy_source=(B/'REVIEW-NOTES.md').read_text(encoding='utf-8')
    legacy_ids=re.findall(r'<a id="(n-[^"]+)"></a>',legacy_source)
    labels={m[1].lower():m[2] for m in re.finditer(r'^## (N-[^ ]+) — (.+)$',legacy_source,re.M)}
    updates=collections.defaultdict(set)
    for n in notes:
        uid=n['id'] if n['id'] in E else n.get('after_unit',n.get('attach_to'))
        if uid in E:
            for i in E[uid]['notes']: updates[i.lower()].add(n['note_id'])
    here=OUT/'LEGACY-NOTES.md'; lines=['# Earlier translation notes and golden-source updates','',
       'The earlier notes remain unchanged at their original paths. They are preserved research, not automatically current source conclusions. The linked golden-source notes supersede older claims about missing verses, source-layer priority, or the selected wording where stated; other interpretive questions remain open.','']
    for ident in legacy_ids:
        lines += ['<a id="'+ident+'"></a>','## '+ident.upper()+' — '+labels.get(ident,'earlier note'),' ',
           link(str(B/'REVIEW-NOTES.md')+'#'+ident,here,'Read the original note, unchanged'),'',
           'Current golden-source updates: '+(', '.join(link(str(OUT/'ENDNOTES.md')+'#'+i.lower(),here,i) for i in sorted(updates[ident])) or 'No new source-difference disposition attached; the earlier note remains an inherited review item.'),'']
    outputs['LEGACY-NOTES.md']='\n'.join(lines).replace('\n \n','\n\n')
    review=['# Golden-source reconciliation — review report','',
        '**Version:** translation-golden-aligned-v1.0.0. **Golden source:** root-tantra-v1.0.0.','',
        '**Mode:** complete comparison of all original anchors and golden additions; source-impact review of every difference with relevant English/context. Unchanged-source passages retain their earlier translation rather than being certified by a new whole-corpus semantic QC.','',
        '**Preservation:** the original English draft, its raw batches and decision logs, the Tibetan golden release, and the established glossary remain unchanged. This is a separate annotated revision.','',
        '## Completed source reconciliation','',
        'All 110 changed original strings, all 18 added golden objects (including 23 main verses), all 42 uncertainty-only passages, two adjacent sentence-continuity revisions, and the Chapter 2 graphic metadata are represented in 173 endnotes. All 65 source-annotation components are retained and rendered separately.','',
        'The changed-original-anchor dispositions are: 41 English retentions with notes, 10 meaning/assembly revisions, 43 source-note relocations, and 16 non-main/joined anchors preserved through notes. Two further adjacent English units change for continuity with restored text. These are not counts of confirmed lexical errors.','',
        '## Meaningful findings','',
        'U00187 no longer treats purpose and the annotation formula as additional root content. U01803 no longer expands ya bzhi to four million after the golden release rejected the required sa/ya split. U02887 follows the selected main clause toward space while preserving smaller rig pa as an unresolved gloss/addition. U03802–U03803 exclude the smaller alternative numbers from the root. U05106 follows main yas gzhi rather than selecting the note ye gzhi.','']
    review += ['## Retained uncertainty and limits','',
       'The printed source and interpretation are distinct. For example, stong at U00039 is the selected source reading, while a thousand [stamens] is a contextual interpretation; yas gzhi at U05106 is selected main text, while upper basis is provisional. The uplift/praise construction at U04312 is not certified here. Newly restored compressed clauses and sound forms retain explicit provisional notes.','',
       'All 72 uncertainty-bearing golden objects retain their flags in the machine edition and linked endnotes. Original omission queries are kept as source annotations, not presented as proof that restored text remains missing. The first portrait-caption line and boundary graphics are represented without invented decipherments.','',
       'This review does not alter or certify the exhaustive manuscript-comparison project, perform new scan reading, approve new glossary entries, or claim independent human palaeographic review. Validation measures preservation, coverage and internal consistency rather than a translation-accuracy percentage.','',
       'Build and check with '+link(R/'build_translation.py',OUT/'REVIEW.md','build_translation.py')+'. Validation results are recorded in VALIDATION.json.']
    outputs['REVIEW.md']='\n'.join(review)
    readme=['# Dra Thal Gyur — golden-aligned annotated English','',
      '**Translation revision:** translation-golden-aligned-v1.0.0. **Tibetan edition:** root-tantra-v1.0.0.','',
      '[Read the complete annotated translation](Dra-Thal-Gyur-English.md) · [Endnotes](ENDNOTES.md) · [Review report](REVIEW.md) · [Machine edition](edition.json)','',
      '| Part | Annotated reading |','|---|---|']
    for n in range(1,8): readme += ['| '+title(n)+' | [Read](chapters/'+pname(n)+'.md) |']
    readme += ['', 'The endnotes compare the original Adzom digital text with the fixed golden reading, quote the previous English, explain the treatment, and retain source evidence and uncertainties. The 23 restored main verses are translated in position, not merely listed in the notes.','',
      'All 5,466 original anchors and 18 added golden objects remain accounted for. All 65 separate source-note components are available in [Source annotations](SOURCE-ANNOTATIONS.md). The original English draft and all established glossary assignments are unchanged.','',
      '**Scope:** complete source-difference reconciliation and annotation. This is not a claim that every unchanged English passage has received independent fresh semantic QC or that all retained source/interpretive questions are resolved. See [the review boundaries](REVIEW.md).','',
      '[Coverage data](COVERAGE.json) · [Earlier notes and updates](LEGACY-NOTES.md) · [Provisional usages](USAGES.json)']
    outputs['README.md']='\n'.join(readme)
    outputs={n:t.rstrip()+'\n' for n,t in outputs.items()}
    manifest={'schema_version':1,'version':'translation-golden-aligned-v1.0.0','golden_tag':'root-tantra-v1.0.0',
       'builder_sha256':sha(Path(__file__)),'review_inputs':{str(p.relative_to(ROOT)):sha(p) for p in [R/'INPUTS.json',R/'PLAN.json',R/'AUDIT.json',R/'DECISIONS.json',R/'authored.py']},
       'output_hashes':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in outputs.items()},'counts':D['counts']}
    outputs['MANIFEST.json']=js(manifest)
    return outputs
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); args=ap.parse_args(); outputs=make()
    if args.check:
        bad=[n for n,t in outputs.items() if not (OUT/n).is_file() or (OUT/n).read_bytes()!=t.encode()]
        if bad: raise SystemExit('Stale outputs: '+', '.join(bad))
    else:
        for n,t in outputs.items(): (OUT/n).parent.mkdir(parents=True,exist_ok=True); (OUT/n).write_text(t,encoding='utf-8')
    print(js({'reproducible':args.check,'output_files':len(outputs),'new_endnotes':173,'original_anchors':5466,'restored_main_verses':23}))
