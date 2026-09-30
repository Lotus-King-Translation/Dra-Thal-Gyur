"""Serialize the bounded Chapter 5 edition without new Tibetan decisions."""
from pathlib import Path
import argparse, collections, hashlib, json, os, sys
sys.dont_write_bytecode = True

def load(path): return json.loads(path.read_text(encoding='utf-8'))
def js(value): return json.dumps(value, ensure_ascii=False, indent=2)+'\n'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def payload_hash(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def anchor(ident): return '<a id="'+ident.lower()+'"></a>'
def fence(value):
    if not isinstance(value,str): return '\n```json\n'+js(value).rstrip('\n')+'\n```\n'
    if any(line!=line.rstrip(' \t') for line in value.split('\n')):
        return '\n```json\n'+json.dumps(value,ensure_ascii=False)+'\n```\n'
    return '\n```text\n'+value+'\n```\n'

def make(root):
    c=root/'diplomatic/chapter-05-v1'; dest=c/'release'
    p=load(c/'PLAN.json'); d=load(c/'DECISIONS.json'); state=load(c/'STATE.json')
    units=load(c/'source-units.json'); col=load(c/'collation.json'); w=load(c/'wikisource.json')
    interventions=load(c/'INTERVENTIONS.json'); insertions=load(c/'INSERTIONS.json')
    review=load(c/'SOURCE-REVIEW.json')
    assert len(units)==p['original_anchor_count']==434
    assert set(d['loci'])==set(p['frozen_locus_ids'])
    assert set(d['W'])==set(p['frozen_W_ids'])
    assert set(d['source_checks'])=={t['id'] for t in p['source_check_targets']}
    for name,h in p['collation_hashes'].items(): assert sha(c/name)==h, name
    for s in p['sources'].values(): assert sha(root/s['path'])==s['full_sha256']
    assert sha(root/p['W']['path'])==p['W']['sha256']
    payload={k:v for k,v in d.items() if k!='final_signoff'}
    if state['status']=='released_bounded_v1':
        sig=d['final_signoff']; assert sig['scope']=='bounded_chapter_5_v1'
        assert sig['decision_payload_sha256']==payload_hash(payload)
        for path,h in sig['input_hashes'].items(): assert sha(root/path)==h, path
    def link(path,label=None):
        file,sep,frag=path.partition('#')
        return '['+(label or Path(file).name)+']('+os.path.relpath(root/file,dest).replace(os.sep,'/')+(sep+frag if sep else '')+')'
    def evidence(paths): return ', '.join(link(path) for path in paths)
    byid={u['id']:u for u in units}; replacements={}; notes=[]
    byunit=collections.defaultdict(list); flags=collections.defaultdict(list)
    for rec in interventions:
        for uid,t in rec['original_units'].items(): assert byid[uid]['tibetan']==t
        for uid,t in rec['replacement_units'].items():
            assert uid not in replacements, 'Overlapping intervention'
            replacements[uid]=t
        for uid in rec['units']: byunit[uid].append(rec['id'])
        for uid in rec.get('uncertain_units',[]): flags[uid].append(rec['id'])
        for n,note in enumerate(rec['annotations'],1):
            notes.append({'id':rec['id']+'-N'+str(n),'intervention_id':rec['id'],'units':rec['units'],**note})
    loci_by_unit=collections.defaultdict(list); w_by_unit=collections.defaultdict(list)
    for locus in col['loci']:
        choice=d['loci'][locus['id']]
        assert choice['source_units']==locus['source_units']
        assert choice['release_reading']=={u:replacements.get(u,byid[u]['tibetan']) for u in locus['source_units']}
        for uid in locus['source_units']: loci_by_unit[uid].append(locus['id'])
        for uid in choice.get('uncertain_units',[]): flags[uid].append(locus['id'])
    for block in w['conflicts']:
        for uid in block['source_units']: w_by_unit[uid].append(block['id'])
    after=collections.defaultdict(list)
    for ins in insertions: after[ins['after_unit']].append(ins)
    role_overrides={u:r for rec in interventions for u,r in rec.get('roles',{}).items()}
    anchors=[]; sequence=[]
    for u in units:
        uid=u['id']; chosen=replacements.get(uid,u['tibetan'])
        role='source_heading' if chosen.lstrip().startswith(('ཞུས་དོན་','ཞུས་ལན་')) else 'main_text'
        if uid in {'U05196','U05197'}: role='chapter_colophon'
        role=role_overrides.get(uid,role)
        item={'id':uid,'source_tibetan':u['tibetan'],'selected_tibetan':chosen,
              'source_wylie':u['wylie'],'role':role,'uncertainty_refs':flags[uid],
              'intervention_ids':byunit[uid],'locus_ids':loci_by_unit[uid],'W_ids':w_by_unit[uid]}
        anchors.append(item)
        sequence.append({'id':uid,'anchor_id':uid,'role':role,'text':chosen,'uncertainty_refs':flags[uid]})
        for ins in sorted(after[uid],key=lambda v:v['anchor_sequence']):
            sequence.append({'id':ins['id'],'anchor_id':uid,'role':'restored_main_text',
                'text':'\n'.join(ins['tibetan_lines']),'lines':ins['tibetan_lines'],
                'uncertainty_refs':[],'punctuation_policy':ins['punctuation_policy']})
    ending=next(r for r in review['items'] if r['id']=='C5-END')['transition_graphic']
    sequence.append({'id':ending['id'],'anchor_id':'U05197','role':'unresolved_source_graphic',
                     'text':'','uncertainty_refs':['C5-END']})
    machine={'schema_version':1,'chapter':5,'release_state':state['status'],'original_units':units,
        'anchors':anchors,'reading_sequence':sequence,'source_annotations':notes,'scan_insertions':insertions,
        'main_and_headings_tibetan':'\n'.join(s['text'] for s in sequence if s['text']),
        'transition_graphic':ending,'original_sources_preserved':True,'unicode_normalization':'none',
        'full_base_scan_proofread':False,'exhaustive_witness_collation':False,
        'scope':'Corrected Adzom-based reading. Untargeted text remains the supplied transcript, not independently proofread source text. Restored lineation and delimiters follow the explicit editorial policy.'}
    label='Released bounded v1' if state['status']=='released_bounded_v1' else 'Release candidate — final gate pending'
    reading=['# Chapter 5 — corrected Adzom-based reading','', '**'+label+'**','',
        'All 434 original anchors are retained, with two scan-attested main verses restored and source notes separated. This is not a complete scan proofread: untargeted wording remains the supplied Adzom transcript. A heading role does not certify every printed heading glyph.','',
        'Paragraph breaks and outer-whitespace trimming are editorial display choices. Exact source and selected strings remain in the machine edition. Restored verses use explicitly editorial single-shad delimiters, not a facsimile sign inventory.','',
        '[Apparatus](apparatus.md) · [Reference comparison](wikisource.md) · [Changes](CHANGES.md) · [Coverage](COVERAGE.md) · [Machine edition](reading.json)','']
    for s in sequence:
        reading += [anchor(s['id']),'']
        ref='[note](apparatus.md#'+s['id'].lower()+')'
        flag=' **[uncertain](COVERAGE.md#questions)**' if s['uncertainty_refs'] else ''
        if s['role']=='unresolved_source_graphic':
            reading += ['*Compact source graphic at the chapter boundary: undecoded; no wording supplied.* '+ref,'']
        elif s['role']=='source_heading':
            reading += ['### '+s['text'].strip(),'',ref+flag,'']
        elif s['role']=='restored_main_text':
            reading += ['**Scan-restored main verses**', '',s['text'],'',ref,'']
        else:
            needed=byunit[s['id']] or loci_by_unit[s['id']] or w_by_unit[s['id']] or flag
            reading += [s['text'].strip()+(' '+ref if needed else '')+flag,'']
    app=['# Chapter 5 — comparative apparatus','', '**'+label+'**','',
        'A/B/S quote the exact supplied Adzom, Tharpaling and Sichuan transcripts, not automatically certified print variants. All 48 differences appear in 27 readable loci with explicit release decisions. The corrected Adzom reading is distinct from the unchanged A quotation.','',
        '[Reading](reading.md) · [W reference](wikisource.md) · [Coverage](COVERAGE.md) · [Complete structured apparatus](apparatus.json)','', '## Anchor index','']
    for a in anchors:
        uid=a['id']; refs=['[reading](reading.md#'+uid.lower()+')']
        refs += ['['+i+'](#'+i.lower()+')' for i in a['intervention_ids']+a['locus_ids']]
        refs += ['['+i+'](wikisource.md#'+i.lower()+')' for i in a['W_ids']]
        refs += ['['+i['id']+'](#'+i['id'].lower()+')' for i in after[uid]]
        app += [anchor(uid),uid+': '+' · '.join(refs),'']
    app += ['## Source-supported interventions','']
    for rec in interventions:
        app += [anchor(rec['id']),'### '+rec['id'],'', '**Original:**'+fence(rec['original_units']),
            '**Selected replacements (empty means wording unchanged):**'+fence(rec['replacement_units']), '**Explicit layer roles:**'+fence(rec.get('roles',{})), '**Separate annotations:**'+fence(rec['annotations']),
            '**Reason:** '+rec['rationale'],'','**Limits:** '+rec['remaining_uncertainty'],'',
            '**Evidence:** '+evidence(rec['evidence']),'']
    app += ['## Restored main text','']
    for ins in insertions:
        app += [anchor(ins['id']),'### '+ins['id'],'', 'After '+ins['after_unit']+'; before '+ins['before_unit']+'.',
            fence('\n'.join(ins['tibetan_lines'])),'**Reason:** '+ins['rationale'],'',
            '**Punctuation:** '+ins['punctuation_policy'],'','**Limits:** '+ins['remaining_uncertainty'],'',
            '**Evidence:** '+evidence(ins['evidence']),'']
    app += [anchor(ending['id']),'## Unresolved chapter-boundary graphic','',
        'The compact source graphic after U05197 is preserved by image evidence, with no supplied wording. It is not counted as a main verse or deciphered from B’s closing formula.','',
        '**Evidence:** '+evidence(ending['evidence']),'','## The 27 release choices','',
        'Offsets are zero-based, end-exclusive Unicode-character positions. Exact source strings are not normalized. JSON quotation is used where needed to preserve boundary whitespace.','']
    for l in col['loci']:
        dec=d['loci'][l['id']]
        app += [anchor(l['id']),'### '+l['id'],'','Anchors: '+', '.join(l['source_units'])+'.',
            'Exact differences: '+', '.join(l['exact_conflicts'])+'.','',
            '**Disposition:** '+dec['status'],'','**Reason:** '+dec['rationale'],'',
            '**Selected anchor strings:**'+fence(dec['release_reading'])]
        if dec.get('insertion_ids'):
            app += ['**Also include:** '+', '.join('['+i+'](#'+i.lower()+')' for i in dec['insertion_ids'])+'.','']
        for sig in ['A','B','S']:
            app += ['**'+sig+' '+str(l['full_source_offsets'][sig])+':**'+fence(l['readings'][sig])]
        app += ['**Evidence and decision:** '+evidence(dec['evidence']),'']
    wm=['# Chapter 5 — related Wikisource reference comparison','', '**'+label+'**','',
        'W is the stored related Wylie transcription, not an independent printing. All 40 non-equal alignment blocks have explicit decisions. Exact original W lines and source Wylie remain quoted; stripped signs and collapsed spaces were used for alignment only.','',
        link('editions/adzom-wikisource/PROVENANCE.json','Stored provenance')+' · [Reading](reading.md) · [Apparatus](apparatus.md)','',
        'Attribution: Wikisource revision 439571 and its contributor history, retained in the provenance file. The related text retains its applicable attribution/share-alike terms; this edition grants no additional rights.','']
    for b in w['conflicts']:
        dec=d['W'][b['id']]
        loc=', '.join(b['source_units']) or 'between '+str(b['source_before'])+' and '+str(b['source_after'])
        wm += [anchor(b['id']),'## '+b['id']+' — '+loc,'',
            '**Original A Tibetan:**'+fence(b['A_tibetan']),'**Original A Wylie:**'+fence(b['A_wylie']),
            '**Exact W lines and locations:**'+fence(b['W_lines']),
            '**Alignment differences:**'+fence(b['token_differences']),
            '**Decision:** '+dec['rationale'],'','**Evidence:** '+evidence(dec['evidence']),'']
    changed=[a for a in anchors if a['selected_tibetan']!=a['source_tibetan']]
    change=['# Chapter 5 — changes from the supplied Adzom text','',
        '**Two main verses restored; three source-note components separated; one section-heading role clarified without changing its string.** Three original anchor strings change. Four intervention records are not four corrected words. These are documented editorial operations, not an independently measured error rate.','',
        'At U05094, U05106 and U05132, smaller alternate wording is preserved separately from the larger main clauses. U04951 retains its exact wording as a source-section heading. U04923 skyur and the U05079/colophon punctuation remain qualified. Every original source string is preserved.','',
        '[Reading](reading.md) · [Apparatus](apparatus.md) · [Coverage](COVERAGE.md)','']
    for ins in insertions:
        change += ['## '+ins['id'],'','After '+ins['after_unit']+'; before '+ins['before_unit']+'.',
            fence('\n'.join(ins['tibetan_lines'])),ins['punctuation_policy'],'',
            '[Evidence](apparatus.md#'+ins['id'].lower()+')','']
    for a in changed:
        change += ['## '+a['id'],'','**Original:**'+fence(a['source_tibetan']),
                   '**Selected:**'+fence(a['selected_tibetan']),
                   '[Reason and notes](apparatus.md#'+a['id'].lower()+')','']
    change += ['## Unchanged-string role clarification', '', 'U04951 is displayed as a section heading. Its exact original string is unchanged and remains in the machine edition.', '', '[Evidence and decision](apparatus.md#c5-i-u04951)', '']
    cov=['# Chapter 5 v1 — coverage and retained uncertainty','', '**'+label+'**','',
        'The bounded scope contains 434 original anchors, all 48 A/B/S differences in 27 loci, all 40 related W comparison blocks, and twelve targeted Adzom source-check dispositions. It does not claim a continuous scan proofread or exhaustive comparison of acquired witnesses.','',
        'The two restored verses after U05079 are attested in the larger main text of Adzom PDF191. Their displayed lineation and single shads are editorial reading conventions, not reproduction of exact physical punctuation.','',
        'Untargeted wording remains the supplied Adzom transcript. Similar readings in several digital sources are not independent print attestations. Previous translation source consultation is not counted as a new complete proofread.','',
        '[Reading](reading.md) · [Apparatus](apparatus.md) · '+link('diplomatic/chapter-05-v1/SOURCE-REVIEW.json','Complete source-review ledger'),' ',
        anchor('questions'),'## Explicit reading qualifications','',
        'The root-letter question at U04923 remains unresolved: supplied skyur is retained rather than replaced by W/S sgyur. Compact annotations at U05094, U05106 and U05132 retain their exact supplied quotations without full printed-letter certification. U05079 keeps its original triple shad with an explicit allocation uncertainty.','',
        'The colophon punctuation at U05197 remains qualified. The following compact graphic has no invented transcription and is not counted as a verse. Other fine sign questions are outside this release, not silently certified.','']
    for a in anchors:
        if a['uncertainty_refs']:
            cov += ['- ['+a['id']+'](reading.md#'+a['id'].lower()+'): '+', '.join(a['uncertainty_refs'])]
    cov += ['', '## The twelve targeted checks','']
    for rec in review['items']:
        cov += ['### '+rec['id'],'', 'Anchors: '+', '.join(rec['units'])+'. Actual source: PDF'+str(rec['pdf_page'])+', row '+str(rec['physical_row'])+'.','',
            rec['rationale'],'','**Limits:** '+rec['remaining_uncertainty'],'',
            '**Evidence:** '+evidence(rec['evidence']),'']
    cov += ['## Deferred research, not a hidden release prerequisite','',
        'No continuous Chapter 5 comparison of the other acquired scan witnesses is claimed. B and S remain supplied-transcript evidence in this release. W remains a related reference. Complete physical-sign reproduction, every compact source glyph and a reconstructed original are outside the bounded scope. Source images being available does not mean the unexamined spans are collated.','',
        'Actual target locations differ from several historical hints: the summary notice is on PDF186, the restoration and first note on PDF191, yas gzhi and its alternate on PDF192, and the later alternate on PDF193. The exact view-allocation ledger excludes exploratory or mislocated crops from accepted anchor evidence. Hash verification of an image does not certify its label or a reading. Prepared context pages receive no whole-page coverage credit.','',
        'Chapters 1–4 remain unchanged. Chapter 6 is not started by this release.','']
    cov=[s if s!=' ' else '' for s in cov]
    readme=['# Chapter 5 — bounded v1','', '**'+label+'**','',p['title'],'',
        '| Deliverable | Contents |','|---|---|',
        '| [Reading](reading.md) | Selected text, restored verses and distinct headings |',
        '| [Apparatus](apparatus.md) | Exact transcript quotations, source notes and decisions |',
        '| [Machine edition](reading.json) | All original anchors, ordered restorations and annotation layers |',
        '| [Changes](CHANGES.md) | Exact original and selected strings |',
        '| [Coverage](COVERAGE.md) | Targeted checks, unresolved readings and uncollated scope |','',
        '[W reference comparison](wikisource.md) · [Structured apparatus](apparatus.json)','',
        'This is a corrected Adzom-based reading, not a complete scan proofread or reconstructed original. Images remain linked in the repository; this directory alone is not a standalone evidence archive.','',
        'Reproduce with `python3 diplomatic/chapter-05-v1/build_release.py --repo . --check`.','']
    if state['status']=='released_bounded_v1':
        readme += ['Version: **chapter-05-v1.0.0**. [Final validation](VALIDATION.json) records the scoped checks.','']
    structured={'schema_version':1,'scope':p['scope'],'collation':col,'wikisource':w,
        'release_decisions':d,'interventions':interventions,'insertions':insertions,'source_review':review}
    outputs={'reading.md':'\n'.join(reading),'apparatus.md':'\n'.join(app),'wikisource.md':'\n'.join(wm),
        'reading.json':js(machine),'apparatus.json':js(structured),'CHANGES.md':'\n'.join(change),
        'COVERAGE.md':'\n'.join(cov),'README.md':'\n'.join(readme)}
    names=['PLAN.json','DECISIONS.json','source-units.json','collation.json','wikisource.json',
        'INTERVENTIONS.json','INSERTIONS.json','SOURCE-REVIEW.json','STATE.json','W-REVIEW.md','evidence/VIEW-ALLOCATION.json']
    inputs=[c/n for n in names]+[root/s['path'] for s in p['sources'].values()]+[root/p['W']['path']]
    inputs += [root/'translations/2026-09-26-full-draft/data/source-units.json']
    inputs += sorted((c/'evidence').glob('*/manifest.json'))
    if (c/'FINAL-REVIEW.md').exists(): inputs.append(c/'FINAL-REVIEW.md')
    counts={'source_anchors':len(units),'transcript_loci':len(col['loci']),'exact_differences':len(col['differences']),
        'W_blocks':len(w['conflicts']),'source_checks':len(review['items']),'interventions':len(interventions),
        'changed_anchor_strings':len(changed),'source_annotations':len(notes),
        'restored_main_verses':sum(len(i['tibetan_lines']) for i in insertions),'reading_sequence_items':len(sequence)}
    manifest={'schema_version':1,'chapter':5,'state':state['status'],'baseline_commit':p['baseline_commit'],
        'input_hashes':{str(x.relative_to(root)):sha(x) for x in inputs},
        'output_hashes':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in outputs.items()},
        'generator_sha256':sha(Path(__file__)),'counts':counts,'full_base_scan_proofread':False,
        'exhaustive_witness_collation':False,'final_signoff_recorded':bool(d['final_signoff'])}
    outputs['MANIFEST.json']=js(manifest)
    return outputs,manifest

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--check',action='store_true'); a=ap.parse_args(); root=a.repo.resolve()
    outputs,manifest=make(root); dest=root/'diplomatic/chapter-05-v1/release'
    if a.check:
        bad=[n for n,t in outputs.items() if not (dest/n).is_file() or (dest/n).read_bytes()!=t.encode()]
        if bad: raise SystemExit('Stale release outputs: '+', '.join(bad))
    else:
        dest.mkdir(exist_ok=True)
        for n,t in outputs.items(): (dest/n).write_text(t,encoding='utf-8')
    print(js({'reproducible':a.check,'files':len(outputs),'state':manifest['state'],'counts':manifest['counts']}))

if __name__=='__main__': main()
