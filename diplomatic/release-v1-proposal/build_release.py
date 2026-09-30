"""Build the bounded Chapter 1 v1 from preserved canonical data and explicit choices.
This serializer makes no Tibetan substitutions and performs no new scan reading.
"""
from pathlib import Path
import argparse, collections, hashlib, json, os, re, sys, unicodedata
sys.dont_write_bytecode = True

def load(path): return json.loads(path.read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def js(value): return json.dumps(value, ensure_ascii=False, indent=2)+'\n'
def text(value): return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
def anchor(value): return '<a id="'+value.lower()+'"></a>'
def fence(value):
    rendered=text(value)
    if isinstance(value,str) and any(line != line.rstrip(' \t') for line in value.split('\n')):
        return '\n```json\n'+json.dumps(value,ensure_ascii=False)+'\n```\n'
    return '\n```text\n'+rendered+'\n```\n'

def make(root):
    dip=root/'diplomatic'; col=dip/'collation/chapter-01'
    work=dip/'release-v1-proposal'; dest=dip/'release-v1'
    plan=load(work/'PLAN.json'); choices=load(work/'DECISIONS.json')
    state=load(work/'RELEASE-STATE.json'); recon=load(work/'RECONCILIATION.json')
    extra=load(work/'RELEASE-EXCEPTIONS.json')
    assert choices['scope_approved'] and recon['all_checks_passed']
    units=load(col/'reading-units.json'); loci=load(col/'chapter1-loci.json')
    insertions=load(col/'ch1-scan-insertions.json')
    scans=load(col/'scan-comparison-loci.json'); web=load(col/'wikisource-diffs.json')
    raw_diffs=load(col/'chapter1-conflicts.json')
    assert set(choices['loci']) == {l['id'] for l in loci}
    assert len(units)==2635 and len(loci)==183 and len(raw_diffs)==359
    for rec in recon['input_files']:
        assert sha(root/rec['path']) == rec['sha256'], rec['path']
    notes=[]
    for n in load(col/'ch1-opening-corrections.json'):
        notes.append({**n,'units':[n['unit']],'evidence':n['evidence_images'],
                      'locator':f"PDF{n['pdf_page']}; BDRC{n['bdrc_image']}; {n['scan_location']}"})
    for n in load(col/'ch1-key-scan-checks.json')['items']:
        notes.append({**n,'old':n['original_tibetan'],'new':n['adopted_tibetan'],
            'annotation':n['separate_unchanged_transcript_annotation'],
            'scan_annotation':n.get('scan_annotation_tibetan'),
            'evidence':n['evidence_crop'],'locator':text(n['scan_locator'])})
    notes += load(col/'additional-interventions.json')
    assert len(notes)==88 and len({n['id'] for n in notes})==88
    byunit=collections.defaultdict(list); bylocus=collections.defaultdict(list)
    scanbyunit=collections.defaultdict(list); insertby=collections.defaultdict(list)
    for n in notes:
        for uid in n['units']: byunit[uid].append(n)
    for l in loci:
        for uid in l['source_units']: bylocus[uid].append(l['id'])
    for s in scans:
        for uid in s['units']: scanbyunit[uid].append(s['id'])
    for n in insertions: insertby[n['after_unit']].append(n)
    for group in insertby.values(): group.sort(key=lambda n:n['anchor_sequence'])
    flags=collections.defaultdict(list)
    for u in units:
        if 'uncertain' in u['status'] or 'unverified' in u['status']:
            flags[u['id']].append('canonical:'+u['status'])
    for e in extra['exceptions']:
        for uid in e['units']: flags[uid].append(e['id'])
    def link(path, label=None):
        file, sep, fragment=path.partition('#')
        return '['+(label or Path(file).name)+']('+os.path.relpath(root/file,dest).replace(os.sep,'/')+(sep+fragment if sep else '')+')'
    def evidence(paths):
        return ', '.join(link('diplomatic/'+p) for p in paths)
    sequence=[]; anchor_records=[]; emitted_headings=set()
    for u in units:
        uid=u['id']; t=u['reading_tibetan']; role='main_text'
        if int(uid[1:]) <= 6: role='opening_title_or_sign'
        elif uid in {'U00011','U00029'} or t.strip().startswith('དྲིས་ལན་'): role='source_heading'
        elif uid=='U02635': role='chapter_colophon'
        if not t: role='joined_anchor' if uid=='U01812' else 'source_annotation_anchor'
        anchor_records.append({**u,'role':role,'uncertainty_refs':flags[uid],
            'intervention_ids':[n['id'] for n in byunit[uid]],'locus_ids':bylocus[uid]})
        sequence.append({'id':uid,'anchor_id':uid,'role':role,'text':t,
                         'uncertainty_refs':flags[uid]})
        for n in byunit[uid]:
            note=n.get('annotation','')
            if note and note.strip().startswith('དྲིས་ལན་') and n['id'] not in emitted_headings:
                sequence.append({'id':n['id'],'anchor_id':uid,'role':'source_heading',
                    'text':note,'uncertainty_refs':flags[uid],'derived_from':'separate source-heading record'})
                emitted_headings.add(n['id'])
        for n in insertby[uid]:
            role={'main_text_restoration':'restored_main_text','source_heading_restoration':'source_heading',
                  'source_caption_provisional':'provisional_caption','scan_only_unresolved':'unresolved_inscription'}[n['kind']]
            sequence.append({'id':n['id'],'anchor_id':uid,'role':role,
                'text':'\n'.join(n['tibetan_lines']),'lines':n['tibetan_lines'],
                'uncertainty_refs':[n['id']] if role in {'provisional_caption','unresolved_inscription'} else [],
                'confidence':n['confidence'],'remaining_uncertainty':n['remaining_uncertainty']})
    body_roles={'opening_title_or_sign','main_text','restored_main_text','source_heading','chapter_colophon'}
    machine={'schema_version':1,'title':plan['title'],'release_state':state['status'],
        'sequence_semantics':'Editorial reading order, not physical lineation. Never infer original witness verse numbers from U identifiers. Source annotations are separate; caption and inscription are not main verses.',
        'source_anchors':anchor_records,'reading_sequence':sequence,'insertions':insertions,
        'source_annotations':[{'record_id':n['id'],'units':n['units'],'annotation':n['annotation'],
            'status':n.get('annotation_status','qualified in source record'),
            'scan_annotation':n.get('scan_annotation'),'rationale':n['rationale']}
            for n in notes if n.get('annotation')],
        'main_and_headings_tibetan':'\n'.join(s['text'] for s in sequence if s['text'] and s['role'] in body_roles),
        'original_sources_unchanged':True,'unicode_normalization':'none','exhaustive_witness_collation':False}
    label='Released bounded v1' if state['status']=='released_bounded_v1' else 'Release candidate — final gate pending'
    reading=['# Chapter 1 — corrected Adzom-based reading','', '**'+label+'**','',
        'The text includes the 13 accepted scan restorations. Source headings are set apart; smaller variant notes are in the apparatus. “Uncertain” marks retained reading questions, not proposed replacements. Caption and inscription material is explicitly non-main.', '',
        '[Apparatus](apparatus.md) · [Changes](CHANGES.md) · [Coverage and uncertainty](COVERAGE.md) · [Machine-readable edition](reading.json)','',
        'Stable U labels refer to the supplied e-text, not manuscript verse numbers. Paragraph breaks and trimmed boundary whitespace are editorial display choices; the machine-readable anchors preserve exact strings.','']
    for s in sequence:
        ident=s['id']; uid=s['anchor_id']; role=s['role']; t=s['text'].strip()
        reading += [anchor(ident),'']
        ref='[†](apparatus.md#'+(ident if ident.startswith('A2000') else uid).lower()+')'
        uncertain=' **[uncertain](COVERAGE.md#reading-questions)**' if s['uncertainty_refs'] else ''
        if role in {'joined_anchor','source_annotation_anchor'}:
            reading += ['*'+('Joined with the preceding adopted clause.' if role=='joined_anchor' else 'Separate source annotation; see apparatus.')+'* '+ref+uncertain,'']
        elif role=='source_heading': reading += ['### '+t,'',ref+uncertain,'']
        elif role=='provisional_caption': reading += ['**Provisional source caption — not a main verse**', '',t,'',ref+uncertain,'']
        elif role=='unresolved_inscription': reading += ['**Unresolved source inscription — no wording supplied.** '+ref,'']
        else:
            needed=byunit[uid] or bylocus[uid] or scanbyunit[uid] or role=='restored_main_text' or s['uncertainty_refs']
            reading += [t+(' '+ref if needed else '')+uncertain,'']
    app=['# Chapter 1 — comparative apparatus','', '**'+label+'**','',
        'A, B and S are the exact supplied Adzom, Tharpaling and Sichuan transcripts. Their differences are not automatically verified readings of the corresponding print. The chosen reading is Adzom-based; every retained or adopted choice below is a bounded v1 decision, not a reconstructed original.', '',
        '[Reading](reading.md) · [Coverage](COVERAGE.md) · [Full comparison-scan records](comparison-scans.md) · [Complete structured apparatus](apparatus.json)','',
        'The separate '+link('diplomatic/reviews/chapter-01/wikisource.md','273-block Wikisource apparatus')+' preserves its exact related Wylie transcription and attribution. It is not an additional independent print witness. Its complete structured data is also included in apparatus.json.','', '## Anchor index','']
    for u in units:
        uid=u['id']; refs=['[reading](reading.md#'+uid.lower()+')']
        refs += ['['+n['id']+'](#'+n['id'].lower()+')' for n in byunit[uid]]
        refs += ['['+i+'](#'+i.lower()+')' for i in bylocus[uid]]
        refs += ['['+n['id']+'](#'+n['id'].lower()+')' for n in insertby[uid]]
        refs += ['['+i+'](comparison-scans.md#'+i.lower()+')' for i in scanbyunit[uid]]
        app += [anchor(uid), uid+': '+ ' · '.join(refs)+(' — **reading question retained**' if flags[uid] else ''),'']
    app += ['## Accepted scan interventions and source layers','',
        'All 88 baseline records remain. Original and adopted strings, smaller annotations, and uncertainty-only records are distinct. Read the stated confidence and locator; a retained annotation can have unresolved printed provenance.','']
    for n in notes:
        app += [anchor(n['id']),'### '+n['id'],'','Anchors: '+', '.join(n['units'])+'.','',
            '**Supplied text:**'+fence(n.get('old',n.get('original_units'))),
            '**Adopted reading or recorded state:**'+fence(n.get('new',n.get('replacement_units','No replacement; uncertainty record only.')))]
        if n.get('annotation'):
            app += ['**Separate annotation:**'+fence(n['annotation']), '**Annotation status:** '+text(n.get('annotation_status','See exact source record.')),'']
        if n.get('scan_annotation'):
            app += ['**Separately recorded scan wording (not the unchanged transcript quotation):**'+fence(n['scan_annotation'])]
        app += ['**Reason:** '+n['rationale'],'','**Locator:** '+text(n.get('locator','See source record.')),'',
            '**Confidence and limits:** '+text(n.get('confidence','See linked record.')),'',
            '**Evidence:** '+evidence(n['evidence']), '']
    app += ['## Restorations and other scan-only material','']
    for n in insertions:
        app += [anchor(n['id']),'### '+n['id']+' — '+n['kind'],'',
            'After '+n['after_unit']+'; before '+n['before_unit']+'; ordered position '+str(n['anchor_sequence'])+'.','',
            fence('\n'.join(n['tibetan_lines']) if n['tibetan_lines'] else 'Unresolved: no Tibetan wording supplied.'),
            '**Reason:** '+n['rationale'],'','**Confidence:** '+text(n['confidence']),'',
            '**Remaining limits:** '+n['remaining_uncertainty'],'',
            '**Punctuation:** '+n.get('punctuation_policy','See recorded inventory.'),'',
            '**Evidence:** '+evidence(n['evidence_images']),'']
    app += ['## The 183 explicit release choices','',
        'All 359 exact transcript differences are represented in these loci. Offsets are zero-based half-open Unicode-character positions in the unmodified full source files. The source quotations below are not changed to match the corrected reading. A quotation containing trailing spaces is rendered as a JSON string so its boundary whitespace stays explicit and round-trippable.','']
    for l in loci:
        c=choices['loci'][l['id']]
        app += [anchor(l['id']),'### '+l['id'],'',
            'Anchors: '+', '.join(l['source_units'])+'. Exact differences: '+', '.join(l['exact_conflicts'])+'.','',
            '**V1 disposition:** '+c['status'],'','**Reason:** '+c['rationale'],'',
            '**Current adopted anchor text:**'+fence(c['release_reading'])]
        for siglum in ['A','B','S']:
            app += ['**'+siglum+' '+str(l['offsets'][siglum])+':**'+fence(l['readings'][siglum])]
        app += ['**Evidence and decision record:** '+', '.join(link(p) for p in c['evidence']),'']
    scanmd=['# Chapter 1 — scoped comparison-scan records','',
        str(len(scans))+' records, including provisional readings, rechecks, rejected hypotheses and uncertainty. This is neither a confirmed-variant count nor exhaustive witness coverage.','',
        '[Reading](reading.md) · [Apparatus](apparatus.md) · [Coverage](COVERAGE.md)','']
    for s in scans:
        scanmd += [anchor(s['id']),'## '+s['id']+' — '+s['witness'],'',
            'Anchors: '+', '.join(s['units'])+'. **Status:** '+s['status']+'.','',
            '**Observed or qualified comparison:**'+fence(s['comparison_reading']),
            '**Reason:** '+s['rationale'],'','**Disposition:** '+s['decision'],'',
            '**Locator:** '+s['locator'],'','**Confidence:** '+text(s['confidence']),'',
            '**Evidence:** '+evidence(s['evidence'])+'. '+link('diplomatic/'+s['review'],'Review')+'.','']
    changes=[u for u in units if u['source_tibetan']!=u['reading_tibetan']]
    letters=lambda t: ''.join(c for c in t if unicodedata.category(c)[0] in 'LM')
    effects=collections.Counter('letter_or_source_layer_change' if letters(u['source_tibetan'])!=letters(u['reading_tibetan']) else 'punctuation_or_spacing_only' for u in changes)
    changemd=['# Chapter 1 — what changed from the supplied Adzom e-text','',
        'The release preserves the accepted corrected reading; no new canonical Tibetan was changed during the bounded v1 integration and acceptance work. The improvements below were accumulated in the preserved source-reviewed edition and are now released together.','',
        '**13 main verses restored; one reply heading restored; 88 intervention/source-layer/uncertainty records retained.** '+str(len(changes))+' original anchor strings differ from the supplied e-text. These are not independent error counts.','',
        'Mechanical string effects: '+text(dict(effects))+'. Letter-bearing changes include removal of source annotations from the main layer and the joining of two anchors; they are not all spelling corrections. No accuracy percentage is inferred.','',
        'At U00180 a long annotation was removed from inside tha mi … dad and preserved separately. U00542 smras became spras; U00039 stod became stong; U01598 the split kun rdzo ba became kun rdzob; U02522 restores par and its separator. Consult the linked records for exact evidence and confidence.','',
        '[Reading](reading.md) · [Apparatus](apparatus.md) · [Coverage](COVERAGE.md)','', '## Restored material','']
    for n in insertions:
        changemd += ['### '+n['id']+' — '+n['kind'],'',
            'After '+n['after_unit']+'. '+(' / '.join(n['tibetan_lines']) if n['tibetan_lines'] else 'Unresolved marker, not guessed text.'),'',
            '[Evidence and limits](apparatus.md#'+n['id'].lower()+')','']
    changemd += ['## Exact changed-anchor ledger','',
        'The original strings below are unchanged source testimony. Empty adopted text means a joined anchor or separate source annotation, not discarded evidence. The machine edition retains all 2,635 anchors.','']
    for u in changes:
        changemd += ['### '+u['id'],'','**Original:**'+fence(u['source_tibetan']),
                    '**Current:**'+fence(u['reading_tibetan']),
                    '[Reason and source](apparatus.md#'+u['id'].lower()+')','']
    changemd += ['## Changes made during bounded v1 preparation','',
        'Two captured comparison packets were integrated, adding 15 bounded/provisional records without changing Adzom wording. Six packets were explicitly deferred without collation credit. All 183 release choices were written individually; 88 baseline intervention records and all 13 restored verses were reconciled. The complete original reports and superseded hypotheses remain in repository history.','']
    qdata={'scope':plan['scope'],'exhaustive_witness_collation':False,
        'base_reading_questions':[{'anchor':u['id'],'status':u['status'],'release_flags':flags[u['id']]} for u in units if flags[u['id']]],
        'release_exceptions':extra,'packet_deferrals':choices['packet_deferrals'],
        'scan_insertions_with_qualifications':insertions,'continuation_reports':[]}
    taskids={t['id'] for t in load(dip/'WORK-QUEUE.json')['tasks']}
    for task in sorted(taskids):
        path=dip/'reviews/chapter-01/continuation'/(task+'.json')
        if not path.is_file(): continue
        report=load(path); batches=[]
        for b in report.get('batches',[]):
            fields={k:v for k,v in b.items() if any(s in k for s in ['unread','uncertain','unexamined','remaining','question'])}
            batches.append({'batch_id':b['batch_id'],'status':b.get('status'),
                'recorded_limits':fields,'independent_scope':b.get('independent_review',{}).get('scope')})
        qdata['continuation_reports'].append({'task_id':task,'path':str(path.relative_to(root)),
            'sha256':sha(path),'status':report.get('status'),'batches':batches,
            'top_level_limits':{k:v for k,v in report.items() if k!='batches' and any(s in k for s in ['unread','uncertain','unexamined','remaining','question'])}})
    cov=['# Chapter 1 v1 — coverage and retained uncertainty','', '**'+label+'**','',
        '**This is a completed-deliverable scope, not an exhaustive-witness claim.** The governing base remains Adzom. All 183 supplied-transcript loci have explicit release choices; unresolved letters and uncollated witnesses have not been turned into agreement.','',
        '[Reading](reading.md) · [Apparatus](apparatus.md) · [Detailed structured limits](coverage.json)','',
        '## What this release includes','',
        'All 2,635 original anchors, 13 restored main verses, one restored reply heading, all 88 accepted intervention/source-layer/uncertainty records, every one of 359 exact A/B/S differences in 183 loci, the related 273-block Wylie comparison, and '+str(len(scans))+' scoped comparison-scan observations. A comparison observation is not necessarily a confirmed variant.','',
        'The preserved Adzom main lexical pass and Dzongsar main lexical comparison are reused. Physical signs, foreign-script material and smaller source layers retain their recorded limits. Textual improvement means a more complete and traceable representation than the supplied Adzom e-text, not proof of superiority to the Adzom printing or recovery of an original.','',
        '## Frozen packet dispositions','',
        'Eight records were closed for v1: **two integrated and six explicitly deferred**. Five deferred jobs have no saved reading body or final agent message; one has a preserved Adzom1973 report whose final integration was deferred after a supplemental tool request failed. No deferred packet receives collation credit.','']
    for packet in plan['pending_packets']:
        key=packet['task']+'/'+packet['batch']; defer=choices['packet_deferrals'].get(key)
        cov += ['### '+packet['scope'],'', ('**Deferred, not collated.** '+defer['rationale']) if defer else '**Integrated within the report’s explicit limits.**', '',
                link('diplomatic/reviews/chapter-01/continuation/'+packet['task']+'.json','Preserved report and batch status'),'']
    cov += [anchor('reading-questions'),'## Reading questions','',
        'The reading flags canonical uncertainties and seven release-only qualifications. A flag does not replace the Tibetan string with a conjecture. Fine physical-sign questions may also remain in the page ledgers even where no inline lexical flag is shown.','',
        'Named base concerns include the title/invocation, U00014 graphics, U01239, U01286, U01522, U01557 initials, the small U02489 heading terminal, U02615/U02620 note allocation, the provisional S08 caption, and the unread S09 inscription. Unread or partial source wording is not an omitted passage.','']
    for q in qdata['base_reading_questions']:
        cov += ['- ['+q['anchor']+'](reading.md#'+q['anchor'].lower()+'): '+', '.join(q['release_flags'])]
    cov += ['', '### Pending proposals retained without adoption','']
    for e in extra['exceptions']:
        cov += [anchor(e['id']),'**'+e['id']+' — '+', '.join(e['units'])+'**', '',e['rationale'],'']
    cov += ['### Source-caption and inscription limits','']
    for n in insertions:
        if n['kind'] in {'source_caption_provisional','scan_only_unresolved'}:
            cov += ['**'+n['id']+'**: '+n['remaining_uncertainty'],'']
    cov += ['## What is not completed','',
        'The exhaustive comparison/physical-proofreading project remains unfinished. Adzom has bounded physical ledgers through PDF16 plus title and local later reviews; Tingkye through PDF16, Tsamdrak through PDF26, and Degé through PDF14 have integrated continuation reports with unresolved components. These frontiers are not whole-page certainty or full-witness percentages. Tharpaling, Gadkar, Zhichen, W1ER119, Langtang, Adzom1973 and Gcn retain the exact partial coverage and boundary/gap limits in their ledgers.','',
        'No complete Sichuan facsimile is acquired in the source directory; S remains exact transcript evidence. W is a related reference transcription, not a new independent printing. Unfinished source coverage is disclosed rather than labelled inaccessible.','',
        'The older complete-witness gate remains false. It is not the approved bounded v1 gate. Future work may refine physical punctuation, resolve local glyphs and extend witness comparison; this release does not require it or silently credit it.','',
        '## Traceable coverage ledgers','']
    for r in qdata['continuation_reports']:
        cov += ['- '+link(r['path'],r['task_id'])+' — '+str(r['status'])]
    cov += ['',link('diplomatic/collation/chapter-01/scan-coverage.json','Canonical source coverage')+' · '+link('diplomatic/SOURCES.md','Source register')+' · '+link('diplomatic/release-v1-proposal/RECONCILIATION.json','Accepted-content reconciliation'),'']
    qdata['canonical_source_coverage']=load(col/'scan-coverage.json')
    structured_app={'schema_version':1,'scope':plan['scope'],'electronic_loci':loci,
        'exact_transcript_differences':raw_diffs,'release_choices':choices['loci'],
        'scan_interventions':notes,'scan_insertions':insertions,
        'comparison_scan_observations':scans,'wikisource_reference':web,
        'unmodified_source_scope':load(col/'chapter1-summary.json')}
    readme=['# Chapter 1 — bounded v1','', '**'+label+'**','',
        'A corrected Adzom-based reading with a scoped comparative apparatus. This release preserves uncertainty and does not claim exhaustive manuscript collation or reconstruction of an original text.','',
        '| Deliverable | Contents |','|---|---|',
        '| [Reading](reading.md) | Corrected text, restored verses and separate headings |',
        '| [Apparatus](apparatus.md) | 183 explicit choices, exact A/B/S quotations and accepted interventions |',
        '| [Machine reading](reading.json) | All 2,635 original anchors, ordered restorations and separate source layers |',
        '| [Changes](CHANGES.md) | Restorations and exact changed-anchor ledger |',
        '| [Coverage](COVERAGE.md) | What was compared, deferred and left uncertain |','',
        'The [comparison-scan supplement](comparison-scans.md), [structured apparatus](apparatus.json) and [structured coverage](coverage.json) preserve the full supporting records. Evidence images and historical reports remain linked in the repository. These files are not a standalone scan archive.','',
        'Rebuild or verify from the repository root with `python3 diplomatic/release-v1-proposal/build_release.py --repo . --check`. Run the release validator before recording final signoff.','']
    outputs={'reading.md':'\n'.join(reading),'apparatus.md':'\n'.join(app),
        'reading.json':js(machine),'CHANGES.md':'\n'.join(changemd),'COVERAGE.md':'\n'.join(cov),
        'comparison-scans.md':'\n'.join(scanmd),'apparatus.json':js(structured_app),
        'coverage.json':js(qdata),'README.md':'\n'.join(readme)}
    inputs=[col/n for n in ['reading-units.json','chapter1-loci.json','chapter1-conflicts.json',
        'ch1-scan-insertions.json','ch1-opening-corrections.json','ch1-key-scan-checks.json',
        'additional-interventions.json','scan-comparison-loci.json','scan-coverage.json','wikisource-diffs.json','chapter1-summary.json']]
    inputs += [work/n for n in ['PLAN.json','DECISIONS.json','RECONCILIATION.json','RELEASE-EXCEPTIONS.json','RELEASE-STATE.json']]
    inputs += [root/r['path'] for r in qdata['continuation_reports']]
    manifest={'schema_version':1,'release_state':state['status'],'scope':plan['title'],
        'source_snapshot_commit':state['source_snapshot_commit'],'audited_baseline':plan['audited_commit'],
        'input_hashes':{str(p.relative_to(root)):sha(p) for p in inputs},
        'generator':{'path':str(Path(__file__).resolve().relative_to(root)),'sha256':sha(Path(__file__))},
        'output_hashes':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in outputs.items()},
        'counts':{'source_anchors':len(units),'accepted_interventions':len(notes),
            'restored_main_verses':sum(len(n['tibetan_lines']) for n in insertions if n['kind']=='main_text_restoration'),
            'restored_source_headings':sum(len(n['tibetan_lines']) for n in insertions if n['kind']=='source_heading_restoration'),
            'release_loci':len(choices['loci']),'exact_transcript_differences':len(raw_diffs),
            'comparison_observations_including_uncertainty':len(scans),'changed_anchor_strings':len(changes),
            'mechanical_string_effects':dict(effects)},
        'exhaustive_witness_collation':False,'new_canonical_reading_changes_since_audited_baseline':False,
        'final_editorial_signoff_recorded':bool(choices.get('final_editorial_signoff'))}
    outputs['release-manifest.json']=js(manifest)
    return outputs, manifest

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',required=True,type=Path)
    ap.add_argument('--check',action='store_true')
    a=ap.parse_args(); root=a.repo.resolve(); outputs,manifest=make(root)
    dest=root/'diplomatic/release-v1'
    if a.check:
        stale=[name for name,value in outputs.items() if not (dest/name).is_file() or (dest/name).read_bytes()!=value.encode()]
        if stale: raise SystemExit('Release outputs differ: '+', '.join(stale))
    else:
        dest.mkdir(exist_ok=True)
        for name,value in outputs.items(): (dest/name).write_text(value,encoding='utf-8')
    print(js({'outputs_reproducible':True if a.check else None,'files':len(outputs),'counts':manifest['counts'],
        'release_state':manifest['release_state'],'exhaustive_witness_collation':False}))

if __name__=='__main__': main()
