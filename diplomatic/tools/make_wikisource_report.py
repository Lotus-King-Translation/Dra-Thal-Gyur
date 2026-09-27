from pathlib import Path
import json,hashlib,re,difflib,argparse
parser=argparse.ArgumentParser(description='Render the Chapter 1 Wikisource comparison report from generated data.')
parser.add_argument('--repo',required=True,type=Path,help='Repository root containing the exact collated input files.')
parser.add_argument('--out',required=True,type=Path,help='Directory containing wikisource-ch1-diffs.json and raw ledger; report is written here.')
parser.add_argument('--baseline-commit',default='e17a496ad7532cc627f9ba288b541f7a53efd002',help='Input baseline commit, preserved as provenance; not a claim about current HEAD.')
args=parser.parse_args()
root=args.repo.resolve()
out=args.out.resolve()
p=out/'wikisource-ch1-diffs.json'
ledger=json.loads((out/'wikisource-ch1-raw-ledger.json').read_text())
conversion_note=('Diagnostic pyewts conversions of all 2,558 web root-text lines are preserved in `wikisource-ch1-raw-ledger.json`, with conversion warnings at lines '+', '.join(map(str,ledger['conversion_warning_lines']))+'. The Unicode output is diagnostic only, not an adopted reading or a claim about exact printed Tibetan.' if ledger['pyewts_available'] else 'Diagnostic Unicode conversion was not enabled for this run; exact web Wylie is preserved without pretending to recover printed Tibetan from it.')
x=json.loads(p.read_text())
x['input_git_commit']=args.baseline_commit
x['source_unit_validation']='Concatenating all Tibetan source units exactly reproduces source/W1KG11703_7.txt (157288 characters). Chapter 1 U00001-U02635 is source characters [0,76376). No source normalization is required for this equality.'
x['input_sha256']={s:hashlib.sha256((root/s).read_bytes()).hexdigest() for s in ['editions/adzom-wikisource/source.wikitext','editions/adzom-wikisource/sgra-thal-gyur.wikitext','source/W1KG11703_7.txt','translations/2026-09-26-full-draft/data/source-units.json']}
p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
o=['# Chapter 1: Wikisource comparison and uncertainty report','',
'## Scope and evidence','',
'Compared all opening material and Chapter 1 in `source/W1KG11703_7.txt`, stable source units **U00001–U02635**, against `editions/adzom-wikisource/source.wikitext` **lines 1–2664**. The website chapter marker `@2` is line 2665; no Chapter 2 or later text was collated. The Chapter 1 closing formula is line 2664, website page marker **102**. These website page markers are locators within the transcription, not independently verified facsimile page identities.','',
'Input commit: `'+x['input_git_commit']+'`. Concatenating the Tibetan of all source units exactly reproduces the source TXT, 157,288 Unicode characters. Chapter 1 occupies characters `[0, 76376)`.','',
'Wikisource provenance: revision **439571**, timestamp **2015-09-09T14:02:11Z**, [revision URL](https://wikisource.org/w/index.php?oldid=439571); [contributor history](https://wikisource.org/w/index.php?title=Sgra%20thal%20%E2%80%99gyur%20%28A-%27dzom%20blocks%29&action=history). Its declared role is a searchable Wylie reference associated with Adzom blocks, **not a newly independent witness or verified diplomatic transcription**. Both repository wikitext copies have identical bytes. Reuse must retain attribution and applicable [Wikimedia terms](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use), including applicable share-alike requirements.','',
'`source/README.md` says the Adzom printed scan governs readings and the cleaned e-text has not been proofread diplomatically. This report collates the two digital transcriptions; it does not settle printed readings. No facsimile was inspected for this report.','',
'## Method and limits','',
'The source-unit EWTS was compared to the exact website Wylie text, excluding numeric page labels, `@1`, poem wrappers and two bracketed website editorial annotations. For line alignment only, `/`, `_`, `*`, `#`, and `@` signs were removed and whitespace collapsed. All source Tibetan, exact EWTS, exact website lines, source offsets, and web line/page locators remain in the JSON and full apparatus below. The `*` represents the source nonbreaking tsek `༌` in these occurrences; its suppression is an alignment operation, not an editorial deletion. The website omits source-style shad punctuation throughout its verse-line presentation. This is a systematic presentation difference, not evidence that the print has no punctuation.','',
'Line alignment uses Python `difflib.SequenceMatcher` with `autojunk=False`. Contiguous unequal line blocks are recorded exhaustively. A separate token comparison in each JSON conflict identifies changed Wylie spans. Some blocks mix several phenomena (for example a source heading and a word variant); the category is a finding aid, not a claim that everything in the block has one cause.','',
conversion_note+' “Romanization or spacing difference” is a candidate category based on lowercasing, plus-sign spacing and selected apostrophe joining, not proof of the printed Tibetan form. Sanskrit orthography and vowel quantity remain unresolved when the web transcription underspecifies them.','',
'No translation was made or altered; no glossary term was proposed. Relevant repository source-authority and annotation rules were applied.','',
'## Coverage counts','',
'| Measure | Count |','| --- | ---: |']
for k,v in x['stats'].items():
 if k!='categories':o.append(f'| {k} | {v} |')
for k,v in x['stats']['categories'].items():o.append(f'| {k} | {v} |')
o += ['', 'Counts describe the mechanical comparison under the stated normalization. They do not certify print accuracy or independence of witnesses.','',
'## Priority uncertainty flags','',
'1. **Source inline apparatus is flattened into the e-text.** For example U00180 places `sdud pa po zhu ba rang byung gi bkod pa` inside the verse `de nas gcig dang tha mi … dad`; U00192 begins with a long apparent note before the question; U00328 has `spel yang byung`; U00596 has `glu yang gdung yang byung`. Wikisource omits these intrusions. Their placement in the print must determine separation into root text and annotation; the website’s shorter verse is evidence for investigation, not independent authority to excise them.','',
'2. **Possible missing root lines:** Wikisource has the following unmatched runs; facsimile examination must decide whether they fill e-text omissions or reflect another transcription state.','',
'| Between source units | Web lines | Web page marker | Exact Wylie |','| --- | --- | --- | --- |']
for d in x['conflicts']:
 if d['category']=='web_text_absent_in_source_units':
  w=d['wikisource_lines'];o.append(f"| {d['source_before']} / {d['source_after']} | {w[0]['line']}–{w[-1]['line']} | {w[0]['page_marker']} | "+' / '.join('`'+z['raw']+'`' for z in w)+' |')
o += ['| Before U02309, within replacement block W-C01-232 | 2344–2345 | 90 | `rdo rje gsang ba\'i gnas gzung bya\'o` / `yang ni lha dbang dga\' byed nyon` |','',
'3. **Explicit e-text missing-text notices:** U01144 `tshig chad song /`; U01286 `chu\'i byer snyoms gnyis chad/`. Do not reproduce these as unmarked root-text verses. The water-element web addition at lines 1296–1298 is relevant to the latter, but the exact relationship needs scan verification.','',
'4. **Opening differences:** The web omits source U00002 and the Sanskrit title U00006; U00005 also contains prefatory characters absent from the web. Its omission of Sanskrit is not a reason to remove material from the diplomatic edition. U00001 and U00003 are source ornamental signs without lexical web counterparts.','',
'5. **Website editorial citations at U01529–U01530:** Source U01529 has `sems ni thog ma byung ba dang`; web line 1554 has `sems ni thog ma byung sa dang`. Source U01530 has `bar du gnas pa tha mar \'gro`; web line 1556 has `bar du gnas pa tha ma \'gro`. The two bracketed notes below cite other works, but these are unverified claims by the website editor. They cannot be counted as another directly collated witness or imported into root text.','']
for a in x['website_editorial_annotations']:o += [f"**Web line {a['line']}, page marker {a['page_marker']}:**",'',a['raw'],'']
o += ['## Recommended editorial treatment','',
'The golden edition should use one chosen printed witness as its diplomatic base, preserve its readings including difficult or apparently wrong forms, and document every verified departure. Until a print reading is checked, record the present base e-text and website alternatives as **unresolved transcription differences**. Do not choose the web form merely because it reads more fluently, and do not label two Adzom transcriptions as two independent votes. Where source strings are printed marginal or interlinear notes, preserve their wording in the apparatus with print location while removing their accidental insertion into the root-text sentence only after the layout is verified.','',
'The complete apparatus below records the pre-scan digital comparison. Its dispositions remain provisional because this comparison did not inspect the governing scan. Subsequent scan-attested intervention notes in the chapter reading text supersede these provisional dispositions, including where they restore text absent from A. This report does not reject or undo such restorations. Exact supplied readings remain preserved as comparative evidence; no source or edition input was changed.','',
'## Complete lexical difference apparatus','',
'`∅` means no counterpart in this normalized alignment, not proof of omission in the printed book. Exact source Tibetan/EWTS is supplied with each source unit. Web locators identify repository file lines and website page markers.','']
reason={
 'textual_difference':'Retain as an unresolved transcription conflict until checked against the governing print. The web is a related digital transcription; this disagreement alone cannot justify emendation.',
 'source_heading_or_label_absent_in_web_transcription':'Treat the absent web counterpart as a structural difference. Verify the source label’s printed status and placement before assigning it to root text or editorial apparatus.',
 'source_text_absent_in_web_transcription':'Retain the source string as evidence and verify its printed status. Absence in the related website does not authorize deletion; the string may be an opening formula or a source annotation.',
 'web_text_absent_in_source_units':'Record as possible missing source text, pending facsimile verification. Do not insert solely on the authority of the website transcription.',
 'romanization_or_spacing_difference':'Preserve exact source and web spellings; do not infer different Tibetan solely from these transliteration conventions. Check the print if stack, vowel or spacing affects the adopted reading.'}
for d in x['conflicts']:
 o += [f"### {d['id']}",'',f"Category: `{d['category']}`. Alignment: `{d['operation']}`.",'']
 for u in d['source_units']:o += [f"- Source **{u['id']}**, characters [{u['start']}, {u['end']}): {u['tibetan']}",f"  - Exact EWTS: `{u['wylie']}`"]
 if not d['source_units']:o += [f"- Source: ∅ between **{d['source_before']}** and **{d['source_after']}**."]
 for w in d['wikisource_lines']:o += [f"- Web line **{w['line']}**, page marker **{w['page_marker']}**: `{w['raw']}`"]
 if not d['wikisource_lines']:o += [f"- Web: ∅ between lines {d['wikisource_before']} and {d['wikisource_after']}."]
 o += ['', '**Provisional comparison disposition and reason:** '+d.get('rationale',reason[d['category']]),'']
o += ['## Nonlexical source signs preserved outside alignment','',
'The source `༌`/EWTS `*` occurs in the following 177 chapter units. Its removal from matching strings does not delete it from the source or adopted text. The JSON preserves the complete Tibetan and EWTS for each occurrence.','', ', '.join('`'+a['id']+'`' for a in x['source_units_containing_asterisk']), '',
'Ornamental-only source units:','']
for a in x['source_only_sign_units']:o += [f"- {a['id']}: `{a['tibetan']}` / EWTS `{a['wylie']}`."]
o += ['','## Input checksums','', '| File | SHA-256 |','| --- | --- |']
for k,v in x['input_sha256'].items():o.append(f'| `{k}` | `{v}` |')
o += ['','Companion machine-readable files: `wikisource-ch1-diffs.json` has all 273 lexical conflicts; `wikisource-ch1-raw-ledger.json` preserves every exact web line 1–2664 including its newline, all source units U00001–U02635, and the full lexical alignment. All web wrappers, markers, annotations, whitespace and punctuation survive in this ledger. Reproduction scripts: `collate_wikisource_ch1.py` and `make_wikisource_report.py`. Source and edition inputs were not changed by this comparison.','']
(out/'wikisource-ch1.md').write_text('\n'.join(o))
print('report bytes',(out/'wikisource-ch1.md').stat().st_size)
