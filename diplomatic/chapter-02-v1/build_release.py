#!/usr/bin/env python3
"""Assemble bounded Chapter2 outputs from exact sources and explicit decisions."""
from pathlib import Path
import argparse, collections, hashlib, json, os, sys
sys.dont_write_bytecode=True

def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def js(v): return json.dumps(v,ensure_ascii=False,indent=2)+'\n'
def digest(v): return hashlib.sha256(js(v).encode()).hexdigest()
def aid(i): return '<a id="'+i.lower()+'"></a>'
def quote(s): return '\n```json\n'+json.dumps(s,ensure_ascii=False)+'\n```\n'
def document(lines): return '\n'.join(lines).rstrip('\n')+'\n'

def assemble(root):
    c=root/'diplomatic/chapter-02-v1'; out=c/'release'
    plan=load(c/'PLAN.json'); decisions=load(c/'DECISIONS.json'); state=load(c/'STATE.json')
    units=load(c/'source-units.json'); col=load(c/'collation.json'); w=load(c/'wikisource.json')
    interventions=load(c/'INTERVENTIONS.json'); source=load(c/'SOURCE-REVIEW.json')
    assert set(decisions['loci'])==set(plan['frozen_locus_ids'])
    assert set(decisions['W'])==set(plan['frozen_W_ids'])
    assert set(decisions['source_checks'])=={s['id'] for s in plan['source_check_targets']}
    byid={u['id']:u for u in units}; replacements={}; flags=collections.defaultdict(list)
    links=collections.defaultdict(list); explicit_roles={}; annotations=[]
    for record in interventions:
        for uid,old in record['original_units'].items(): assert byid[uid]['tibetan']==old
        for uid,new in record['replacement_units'].items():
            assert uid not in replacements, 'Overlapping intervention '+uid
            replacements[uid]=new
        explicit_roles.update(record.get('roles',{}))
        for uid in record['units']: links[uid].append(record['id'])
        for uid in record.get('uncertain_units',[]): flags[uid].append(record['id'])
        for n,note in enumerate(record['annotations'],1):
            annotations.append({**note,'id':record['id']+'-N'+str(n),'record_id':record['id'],
                'units':record['units'],'evidence':record['evidence'],'remaining_uncertainty':record['remaining_uncertainty']})
    for ident,choice in decisions['loci'].items():
        for uid in choice.get('uncertain_units',[]): flags[uid].append(ident)
    selected=[]
    for u in units:
        text=replacements.get(u['id'],u['tibetan']); role='main_text'
        if text.strip().startswith('དྲིས་ལན་'): role='source_heading'
        if u['id'] in ['U03621','U03622']: role='chapter_colophon'
        if not text: role=explicit_roles.get(u['id'],'source_annotation_anchor')
        selected.append({'id':u['id'],'text':text,'role':role,'uncertainty_refs':flags[u['id']],
            'intervention_ids':links[u['id']],'source_status':'Supplied Adzom scaffold except specifically documented targeted interventions; no complete scan proofread.'})
    for l in col['loci']:
        choice=decisions['loci'][l['id']]
        assert choice['source_units']==l['source_units'] and choice['exact_conflicts']==l['exact_conflicts']
        assert choice['release_reading']=={uid:replacements.get(uid,byid[uid]['tibetan']) for uid in l['source_units']}
    payload={k:decisions[k] for k in ['loci','W','source_checks']}
    if state['status']=='released_bounded_v1':
        sig=decisions['final_signoff']; assert sig['scope']=='bounded_chapter_2_v1'
        assert sig['decision_payload_sha256']==digest(payload)
        assert sig['interventions_sha256']==sha(c/'INTERVENTIONS.json')
        assert sig['review_sha256']==sha(c/'FINAL-REVIEW.md')
    def link(p,title=None):
        return '['+(title or Path(p).name)+']('+os.path.relpath(root/p,out).replace(os.sep,'/')+')'
    def ev(paths): return ', '.join(link(p) for p in paths)
    title='Released bounded v1' if state['status']=='released_bounded_v1' else 'Release candidate - final gate pending'
    reading=['# Chapter 2 - corrected Adzom-based reading','', '**'+title+'**','',
        'The supplied Adzom text is preserved except for documented targeted source-layer corrections. This is not a complete scan proofread or a reconstructed original.','',
        'Smaller notes remain in the apparatus. An uncertainty flag marks a bounded question; an unflagged line is not automatically scan-verified.','',
        '[Apparatus](apparatus.md) - [W reference](wikisource.md) - [Changes](CHANGES.md) - [Coverage](COVERAGE.md) - [Machine reading](reading.json)','',
        'U identifiers remain stable. Paragraph breaks and outer whitespace trimming are display choices; exact strings remain in the machine edition.','']
    for u in selected:
        text=u['text'].strip(); uid=u['id']; reading += [aid(uid),'']
        ref='[note](apparatus.md#'+uid.lower()+')'
        flag=' **[uncertain](COVERAGE.md#questions)**' if u['uncertainty_refs'] else ''
        if not text:
            label='Joined with U02887.' if u['role']=='joined_anchor' else 'Source note preserved in the apparatus.'
            reading += ['*'+label+'* '+ref+flag,'']
        elif u['role']=='source_heading': reading += ['### '+text,'',ref+flag,'']
        else: reading += [text+' '+ref+flag,'']
    reading += [aid('C2-TRANSITION'),'**Unresolved boundary graphic, not a main verse.** The compact graphic after the Chapter2 colophon remains in the [source record](apparatus.md#c2-end); no wording is supplied.','']
    machine={'schema_version':1,'chapter':2,'release_state':state['status'],
        'scope':plan['scope'],'original_units':units,'reading_sequence':selected,'source_annotations':annotations,
        'transition_graphic':next(i['transition_graphic'] for i in source['items'] if i['id']=='C2-END'),
        'text_with_headings':'\n'.join(u['text'] for u in selected if u['text']),
        'unicode_normalization':'none','new_main_verse_restorations':[],
        'full_base_scan_proofread':False,'exhaustive_witness_collation':False}
    lookup=collections.defaultdict(list)
    for l in col['loci']:
        for uid in l['source_units']: lookup[uid].append('['+l['id']+'](#'+l['id'].lower()+')')
    for b in w['conflicts']:
        for uid in b['source_units']: lookup[uid].append('['+b['id']+'](wikisource.md#'+b['id'].lower()+')')
    app=['# Chapter 2 - comparative apparatus','', '**'+title+'**','',
        'A, B, S identify supplied Adzom, Tharpaling and Sichuan transcripts. Exact differences do not automatically establish printed-witness variants. [Reading](reading.md) - [Coverage](COVERAGE.md)','',
        '## Anchor index','']
    for u in selected:
        refs=['[reading](reading.md#'+u['id'].lower()+')']+lookup[u['id']]
        refs += ['['+i+'](#'+i.lower()+')' for i in u['intervention_ids']]
        app += [aid(u['id']),u['id']+': '+' | '.join(refs),'']
    app += ['## Source-layer interventions and retained uncertainty','']
    for i in interventions:
        app += [aid(i['id']),'### '+i['id'],'',i['rationale'],'',
            '**Original anchors:**'+quote(i['original_units']),
            '**Selected main text:**'+quote(i['replacement_units']),
            '**Separate source annotations:**'+quote(i['annotations']),
            '**Limits:** '+i['remaining_uncertainty'],'','**Evidence:** '+ev(i['evidence']),'']
    app += ['## Targeted source observations','',
        'These are bounded source checks, not completed whole-page readings. Original images, exact hashes and approximate native bounds are preserved.','']
    for s in source['items']:
        app += [aid(s['id']),'### '+s['id'],'',
            'PDF '+str(s['pdf_page'])+'; row '+str(s['physical_row'])+'; native bounds '+str(s['approx_native_bounds'])+'.','',
            '**Observed sequence:**'+quote(s['observed_sequence']),s['rationale'],'',
            '**Limits:** '+s['remaining_uncertainty'],'','**Evidence:** '+ev(s['evidence']),'']
    app += ['## All 56 transcript-locus decisions','',
        'All 116 exact differences are represented. Source offsets are zero-based, half-open character positions in the original full files. JSON strings preserve whitespace and exact Tibetan punctuation.','']
    for l in col['loci']:
        choice=decisions['loci'][l['id']]
        app += [aid(l['id']),'### '+l['id']+' - '+', '.join(l['source_units']),'',
            '**Decision:** '+choice['status'],'',choice['rationale'],'',
            '**Chosen anchor text:**'+quote(choice['release_reading'])]
        for k in ['A','B','S']: app += ['**'+k+' '+str(l['full_source_offsets'][k])+':**'+quote(l['readings'][k])]
        app += ['**Evidence:** '+ev(choice['evidence']),'']
    wm=['# Chapter 2 - Wikisource reference comparison','', '**'+title+'**','',
        '105 blocks compare stored Adzom EWTS with the exact related Wylie reference. This is not a further independent printing. Normalization is for alignment only; the raw lines and all source positions remain preserved.','',
        'Source attribution and revision: '+link('editions/adzom-wikisource/PROVENANCE.json','preserved provenance')+'. The source revision is 439571. Existing attribution and reuse terms remain those recorded in the repository method and source documentation.','',
        '[Reading](reading.md) - [Apparatus](apparatus.md) - [Structured comparison](apparatus.json)','']
    for b in w['conflicts']:
        choice=decisions['W'][b['id']]
        wm += [aid(b['id']),'## '+b['id']+' - '+', '.join(b['source_units']),'',
            '**Original Adzom Tibetan:**'+quote(b['A_tibetan']),
            '**Original source Wylie:**'+quote(b['A_wylie']),
            '**Exact W lines:**'+quote(b['W_lines']),
            '**Alignment differences:**'+quote(b['token_differences']),
            '**Decision:** '+choice['rationale'],'','**Evidence:** '+ev(choice['evidence']),'']
    changed=[(old,new) for old,new in zip(units,selected) if old['tibetan']!=new['text']]
    changes=['# Chapter 2 - changes from the supplied Adzom e-text','',
        str(len(changed))+' original anchor strings changed by eight source-layer corrections. One additional record retains uncertainty without changing Tibetan. These are not independently measured error counts. No new main verses are supplied.','',
        'All 987 original strings remain unchanged in the machine edition. The interleaved passage at U02887-U02889 is reassembled as a larger-letter main clause; its smaller rig pa is preserved separately with unresolved gloss/addition status.','',
        '[Reading](reading.md) - [Apparatus](apparatus.md)','']
    for old,new in changed:
        changes += ['## '+old['id'],'','**Original:**'+quote(old['tibetan']),
            '**Selected main text:**'+quote(new['text']),
            '[Source evidence and reason](apparatus.md#'+old['id'].lower()+')','']
    changes += ['## Unchanged but explicitly uncertain','',
        'U03240 retains the supplied dkar gleg reading without a guessed replacement. The chapter-closing compact graphic remains undecoded. Minor sign and source-note wording questions stay in the evidence records.','']
    cov=['# Chapter 2 - coverage and retained uncertainty','', '**'+title+'**','',
        '**Complete for the bounded release scope is not complete manuscript proofreading.** The chapter has 987 original anchors, 56 A/B/S locus decisions covering 116 exact differences, 105 W reference decisions, and ten fixed source-check dispositions.','',
        'Eight source-layer corrections separate notes from root text, including one multi-anchor reconstruction. An additional uncertainty-only record does not alter Tibetan. No new main verse is reconstructed.','',
        'The ten checks are localized in SOURCE-REVIEW.json. A further focused PDF113 observation belongs to already frozen loci L2-0018/0019, not a new all-witness reading queue. No repeated crop is counted as an independent source.','',
        'The previous translation recorded scan consultations, not a reusable complete Chapter2 diplomatic proofread. Untargeted main wording remains the exact supplied Adzom scaffold. The other printed witnesses have not received continuous Chapter2 collation in this release.','',
        'Chapter2 extends from the observed PDF102 opening to the PDF138 colophon. Native packets also include contextual pages; full pages were not thereby collated. All regions outside the explicitly recorded target bounds remain unreviewed for this release.','',
        '[Reading](reading.md) - [Apparatus](apparatus.md) - [Exact source review](../SOURCE-REVIEW.json)','',
        aid('questions'),'## Bounded questions','']
    for s in source['items']:
        cov += ['### '+s['id'],'',s['remaining_uncertainty'],'',
            '[Observed context and evidence](apparatus.md#'+s['id'].lower()+')','']
    cov += ['## Electronic evidence limits','',
        'A/B/S are transcripts, not three newly verified print witnesses. W is related Wylie reference transcription. Its alignment normalization strips specified punctuation and collapses spacing but never changes the stored source lines; normalized equality does not certify punctuation or foreign-script equivalence.','',
        'The precise source files, offsets, hashes and original website line ledger are included in the structured apparatus. Both exact patches and whole-passage loci reconstruct B and S exactly from A.','',
        'No accuracy percentage or remaining-error estimate is inferred from counts. Future source proofreading may revise an explicitly qualified reading without changing this versioned release. Chapter1 is unchanged and Chapter3 has not started.','']
    apparatus={'schema_version':1,'scope':plan['scope'],'sources':plan['sources'],
        'collation':col,'W_reference':w,'decisions':payload,'interventions':interventions,'source_review':source}
    counts={'source_anchors':len(units),'exact_differences':len(col['differences']),
        'transcript_loci':len(col['loci']),'W_blocks':len(w['conflicts']),
        'fixed_source_checks':len(decisions['source_checks']),'intervention_records':len(interventions),
        'changed_anchor_strings':len(changed),'source_annotations':len(annotations),
        'new_main_verses':0,'source_layer_corrections':sum(bool(i['replacement_units']) for i in interventions)}
    readme=['# Chapter 2 - bounded v1','', '**'+title+'**','',plan['title'],'',
        '| Deliverable | Contents |','|---|---|',
        '| [Reading](reading.md) | Corrected main text with separate headings and uncertainty flags |',
        '| [Apparatus](apparatus.md) | Exact A/B/S quotations, decisions, source notes and image evidence |',
        '| [Machine reading](reading.json) | All original anchors, selected text and separate source annotations |',
        '| [Changes](CHANGES.md) | Exact original and changed-anchor text |',
        '| [Coverage](COVERAGE.md) | Targeted checks and precise limits of this release |','',
        'The [W reference comparison](wikisource.md) and [structured apparatus](apparatus.json) preserve the related website text and all underlying comparison data.','',
        'This is a source-controlled bounded reading, not a complete scan proofread or exhaustive critical edition. Evidence links require the repository; this directory alone is not a scan archive.','',
        'Reproduce with `python3 diplomatic/chapter-02-v1/build_release.py --repo . --check`.','']
    if state['status']=='released_bounded_v1':
        readme += ['Version: **chapter-02-v1.0.0**. [Final validation](VALIDATION.json) records the scoped publication checks.','']
    values={'reading.md':document(reading),'apparatus.md':document(app),'wikisource.md':document(wm),
        'reading.json':js(machine),'apparatus.json':js(apparatus),'CHANGES.md':document(changes),
        'COVERAGE.md':document(cov),'README.md':document(readme)}
    inputs=[c/n for n in ['PLAN.json','DECISIONS.json','STATE.json','INTERVENTIONS.json',
        'SOURCE-REVIEW.json','source-units.json','collation.json','wikisource.json']]
    inputs += [root/m['path'] for m in plan['sources'].values()]+[root/plan['W']['path']]
    if (c/'FINAL-REVIEW.md').exists(): inputs.append(c/'FINAL-REVIEW.md')
    manifest={'schema_version':1,'chapter':2,'release_state':state['status'],'counts':counts,
        'input_hashes':{str(p.relative_to(root)):sha(p) for p in inputs},
        'generator':{'path':str(Path(__file__).resolve().relative_to(root)),'sha256':sha(Path(__file__))},
        'output_hashes':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in values.items()},
        'full_base_scan_proofread':False,'exhaustive_witness_collation':False}
    values['MANIFEST.json']=js(manifest)
    return values,manifest

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True); p.add_argument('--check',action='store_true')
    args=p.parse_args(); root=args.repo.resolve(); values,manifest=assemble(root)
    dest=root/'diplomatic/chapter-02-v1/release'
    if not args.check: dest.mkdir(exist_ok=True)
    for name,text in values.items():
        if args.check: assert (dest/name).read_bytes()==text.encode('utf-8'), 'Stale output '+name
        else: (dest/name).write_bytes(text.encode('utf-8'))
    print(js({'reproducible':args.check,'files':len(values),'state':manifest['release_state'],'counts':manifest['counts']}))

if __name__=='__main__': main()
