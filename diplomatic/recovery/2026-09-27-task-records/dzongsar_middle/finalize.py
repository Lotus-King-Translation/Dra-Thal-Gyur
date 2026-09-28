import json,hashlib
from pathlib import Path
r=Path('/workspace/scratch/a117ee885aff');p=r/'base-signs-middle.json';d=json.loads(p.read_text());out=r/'base-signs-middle-crops'
F={f['id']:f for f in d['findings']}
def ev(f,name,bounds):
 f['target_crop']=str(out/(name+'.png'));f['target_bounds']=bounds;f['targeted_crop_inspected']=True
for f in d['findings']:
 if f.get('target_crop'):f['targeted_crop_inspected']=True
for key in ['AS-M-005','AS-M-007']:
 F[key].update(layer='main',kind='confirmed_shad_count_mismatch',current_count=1,observed_count=2,status='confirmed_in_targeted_crop')
ev(F['AS-M-007'],'AS-M-007-p044',[820,600,1800,820])
F['AS-M-002'].update(layer='heading',kind='confirmed_shad_count_mismatch',status='confirmed_in_targeted_crop',current_count=1,observed_count=2,detail='Focused inspection distinguishes a separate initial heading shad from the dris stack. Two strokes follow heading pa: the terminal and the next main leading stroke.',decision='Propose retaining two shads after U00910. Earlier allocation query resolved by targeted inspection.')
ev(F['AS-M-002'],'h910-single',[2748,620,5400,840])
F['AS-M-012'].update(layer='main',kind='confirmed_shad_count_mismatch',status='confirmed_in_targeted_crop',current_count=1,observed_count=2,detail='Targeted crop shows a separate initial shad immediately before dris lan nyer bzhi, in addition to the preceding bya\'o terminal. The overview statement of one was incorrect.',decision='Propose retaining two shads after U01270. Targeted finding supersedes earlier overview statement.')
ev(F['AS-M-012'],'h1271start',[3960,890,5360,1110])
F['AS-M-014']['observation']='Focused crop confirms one terminal vertical stroke on each smaller annotation: se yi yang byung (U1414), bsdebs kyang byung (U1417), and rin chen bse\'i yang byung (U1422). Dotted leaders and these note terminals belong to annotation layer.'
F['AS-M-019'].update(kind='confirmed_shad_count_mismatch',unit='U01595',layer='main_before_heading',current_count=2,observed_count=1,status='confirmed_in_targeted_crop',observation='The first small dris stack has no separate preceding shad. There is one terminal stroke after main zin, then the heading, then two strokes after heading pa\'o. Thus physical allocation is U1595:1 and U1596:2, versus electronic 2+2.',proposed_change='Reduce U01595 to one shad; retain U01596 two. This is a local observed absence of the heading initial stroke, not a general heading rule.')
# Refine overview paragraphs: targeted findings govern.
for page in d['pages']:
 n=page['pdf_page']
 if n==37:page['detail'] += ' TARGETED REFINEMENT: a separate initial shad before dris is visible; U910 needs two terminal boundary strokes (AS-M-002).'
 if n==39:page['detail'] += ' TARGETED REFINEMENT: U948 has a separate initial heading shad as well as its terminal and next main lead; the earlier three-stroke description omitted the initial heading stroke. U948 needs two terminal strokes.'
 if n==46:page['detail'] += ' TARGETED REFINEMENT: the heading U1147 has its own initial shad and two following strokes; preserve note U1144 terminal separately. The three-layer description is not a total stroke count.'
 if n==50:page['detail'] += ' TARGETED CORRECTION: U1270 has TWO strokes before the small heading, including a separate initial heading shad (AS-M-012). The earlier single-ending statement is superseded.'
 if n==51:page['detail'] += ' TARGETED REFINEMENT: U1286 is small annotation text; an independent terminal shad cannot be distinguished from the adjacent frame. Do not certify the electronic final shad or keep the note as a main verse solely because reading-units retains it.'
 if n==56:page['detail'] += ' TARGETED REFINEMENT: all three small notes U1414/U1417/U1422 show one terminal stroke each.'
 if n==61:page['detail'] += ' TARGETED REFINEMENT: U1540 has no separate initial heading shad: U1539 has one terminal, U1540 has two following strokes. U1557 is wholly at row6 left after carried byed, not row5/right; two following strokes are clear, but the abraded initial heading boundary remains uncertain.'
 if n==63:page['detail'] += ' TARGETED REFINEMENT: U1595 has one physical boundary stroke before the small heading; U1596 retains two following strokes. The allocation query is resolved locally by AS-M-019.'
 if n==66:page['detail'] += ' TARGETED REFINEMENT: no separate initial shad before small U1689; U1688 has one terminal stroke, U1689 has two following strokes.'

def add(f):
 f['id']=f"AS-M-{len(d['findings'])+1:03d}";f['bdrc_image']=f['pdf_page']+2;d['findings'].append(f);return f
single=json.loads((out/'heading-single-bounds.json').read_text());singlemap={a:(n,b) for a,n,b in single}
heads=[(948,'h948'),(1023,'h1023'),(1147,'h1147'),(1186,'h1186'),(1239,'h1239'),(1257,'h1257'),(1308,'h1308end'),(1353,'h1353'),(1476,'h1476'),(1540,'h1540'),(1557,'h1557end'),(1634,'h1634'),(1661,'h1661'),(1727,'h1727')]
for u,name in heads:
 n,b=singlemap[name];f=add(dict(unit=f'U{u:05d}',pdf_page=n,layer='heading',kind='confirmed_shad_count_mismatch',status='confirmed_in_targeted_crop',current_count=1,observed_count=2,observation='The heading terminal shad and a separate following main-text leading shad are both visible. This finding concerns the boundary after the heading; preceding boundary is considered separately.',proposed_change='Retain the two observed strokes after this heading.'))
 ev(f,name+'-single',b)
 if u==1557:f['bounded_uncertainty']='Initial heading boundary after U1556 byed is abraded; the following pair is visible, but this does not certify a separate initial heading stroke.'
for u,n,name,b,desc in [(1539,61,'h1540focus',[1800,390,2590,580],'One stroke after min before small dris lan so gnyis pa; no separate initial heading shad.'),(1688,66,'h1689-focused',[3340,770,4440,985],'One stroke after grub before small dris lan so brgyad pa\'o; no separate initial heading shad.')]:
 f=add(dict(unit=f'U{u:05d}',pdf_page=n,layer='main_before_heading',kind='confirmed_shad_count_mismatch',status='confirmed_in_targeted_crop',current_count=2,observed_count=1,observation=desc,proposed_change='Retain one stroke before this heading; retain the separately observed pair after the heading.'));ev(f,name,b)
f=add(dict(unit='U01556',pdf_page=61,layer='main_before_heading',kind='bounded_initial_heading_query',observation='After carried byed and before small U1557 dris lan, the area is abraded. One prior terminal stroke is visible; an independent initial heading shad cannot be certified or denied from this impression.',decision='Keep bounded uncertainty for the U1556/U1557 initial boundary; do not call current two shads agreement.'));ev(f,'h1557focus',[720,875,1630,1045])
for u,n,name,b,desc in [(1067,43,'n1067-correct',[1450,605,3350,850],'One terminal stroke after small brgya yang byung in row4 middle.'),(1090,44,'n1090',[4100,510,5370,735],'One terminal stroke after small bcu gcig kyang byung in row3 far right.'),(1144,46,'n1144',[900,530,3200,755],'One terminal stroke after small tshig chad song, consistent with its already retained annotation terminal.'),(1233,49,'n1233',[2700,740,4650,970],'One terminal stroke after the ONE shared chags \'jig stongs pa gloss linked to U1233/U1237; do not duplicate the physical note.')]:
 f=add(dict(unit=f'U{u:05d}',pdf_page=n,layer='annotation',kind='annotation_terminal_sign',observation=desc,decision='Preserve this annotation terminal separately from main-text boundary strokes.'));ev(f,name,b)
f=add(dict(unit='U01286',pdf_page=51,layer='annotation',kind='annotation_layer_and_terminal_query',current='reading-units retains chu\'i byer snyoms gnyis chad followed by one shad as a main unit.',observation='The phrase is visibly small annotation at row4 far right. The final chad is adjacent to the frame; an independent final shad is not securely distinguishable. Main surrounding row continues the four-element discussion.',decision='Separate the note from the main reading. Preserve the observed note wording, with explicit uncertainty for terminal punctuation; do not manufacture absence or agreement.'));ev(f,'n1286',[4500,635,5320,805])
# Register contrasting heading controls rather than infer by lexical ending.
controls=[]
for name,n,b in json.loads((out/'heading-focused-bounds.json').read_text()):
 u=int(name[1:]);controls.append(dict(unit=f'U{u:05d}',pdf_page=n,bdrc_image=n+2,crop=str(out/(name+'-focused.png')),native_bounds=b,observation=('No separate initial heading shad; see U1688 local correction.' if u==1689 else 'Separate initial shad before dris, terminal shad after heading, and following main leading shad are visible. Retain the heading two-shad boundary.')))
d['heading_controls']=controls
# Metadata and a complete evidence manifest.
d.update(status='assigned_page_inspection_complete',assigned_page_inspection_complete=True,complete=False,completion_meaning='Every main row of the assigned PDF35–68 span was visually inspected for boundary signs and paratext. complete:false and exact_diplomatic_certification:false mean that this report does not certify every tsheg, worn micro-sign, spatial feature or ornamental glyph as a strict diplomatic transcription; they do not mean that assigned pages were left uninspected.',exact_diplomatic_certification=False,scope_start=d['pages'][0]['start'],scope_end=d['pages'][-1]['end'],base_reading_sha256=hashlib.sha256((r/'Dra-Thal-Gyur/diplomatic/collation/chapter-01/reading-units.json').read_bytes()).hexdigest())
d['method'] += ' Focused native crops supersede provisional overview stroke allocations where explicitly marked. The electronic convention here assigns the terminal stroke and next unit leading stroke to the preceding unit. A separate initial shad is not inferred merely from the first dris glyph. Physical page-opening signs are described separately. No repo files were edited.'
d['bounded_uncertainties']=[dict(unit='U01522',pdf_page=60,span='leading word of small note ending kyang byung, and underlying main pa\'i rgyu cluster',evidence='AS-M-016-p060.png'),dict(unit='U01556/U01557',pdf_page=61,span='initial boundary before small dris lan after abraded carried byed',evidence='h1557focus.png'),dict(unit='U01286',pdf_page=51,span='independent final shad versus immediately adjacent frame',evidence='n1286.png'),dict(scope='all assigned pages',span='Exact tsheg census, fine damaged signs, point-filler counts, and all marginal/ornamental glyphs are not fully certified. Individual page records identify especially worn areas.')]
allfiles={}
for f in d['findings']:
 if f.get('target_crop'):allfiles[f['target_crop']]={'pdf_page':f['pdf_page'],'native_bounds':f['target_bounds'],'inspected':True}
for c in controls:allfiles[c['crop']]={'pdf_page':c['pdf_page'],'native_bounds':c['native_bounds'],'inspected':True}
d['targeted_evidence']=[dict(path=k,sha256=hashlib.sha256(Path(k).read_bytes()).hexdigest(),**v) for k,v in sorted(allfiles.items())]
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Human-readable report.
lines=['# Adzom Chapter 1: signs and paratext, PDF35–68','',d['completion_meaning'],'',f"Source: `{d['source_pdf']}`. SHA256 `{d['source_sha256']}`. PDF N = BDRC image N+2. Native image 5696×1344.",'','All 34 pages and six main rows per page were inspected with overlapping native halves; targeted crops resolve local boundary counts. The corrected reading and scan insertions were the comparison base. No repository text was changed.','', '## Confirmed local boundary differences','', '| Unit | PDF / BDRC | Layer | Current → observed shads | Evidence |','|---|---|---|---|---|']
for f in d['findings']:
 if f.get('kind')=='confirmed_shad_count_mismatch':
  lines.append(f"| {f['unit']} | {f['pdf_page']} / {f['bdrc_image']} | {f['layer']} | {f['current_count']} → {f['observed_count']} | `{Path(f['target_crop']).name}` |")
lines += ['', 'The boundary convention counts the terminal stroke and the next unit’s independent leading stroke at the preceding electronic unit. This is not a count of physical row-end signs. In particular, a final ga descender remains a letter stroke. Headings are not normalized wholesale: U1596 and U1689 have no separate initial shad, while the contrasting controls listed in JSON do. U1540 likewise lacks an initial shad; the U1557 initial area is abraded.', '', '## Annotation signs and remaining questions','']
for f in d['findings']:
 if f.get('layer') in ['annotation','annotation_and_main_query'] or f.get('type')=='annotation_terminal_stroke' or f.get('kind')=='bounded_initial_heading_query':
  unit=f.get('unit',', '.join(f.get('units',[])));detail=f.get('observation',f.get('detail',''));lines.append(f"- {unit}, PDF{f['pdf_page']}: {detail} Evidence `{Path(f['target_crop']).name}`.")
lines += ['', 'U1286 remains in reading-units but is physically a small annotation; this report proposes separating its layer. Its terminal shad is uncertain next to the frame. U1522 remains a bounded main/note reading query, although small text ending *kyang byung* and its own terminal stroke are clearly present. U1556/U1557 has a locally abraded initial heading boundary. These are not recorded as agreement.', '', '## Page coverage','', '| PDF / BDRC | Start | End | Rows |','|---|---|---|---|']
for q in d['pages']:lines.append(f"| {q['pdf_page']} / {q['bdrc_image']} | {q['start']} | {q['end']} | 6 |")
lines += ['', '## Page observations','']
for q in d['pages']:lines += [f"### PDF{q['pdf_page']} / BDRC{q['bdrc_image']}",'',q['detail'],'']
lines += ['The JSON gives native crop bounds, source hash, targeted image hashes, control observations, and bounded uncertainties. Retained single-shad ga endings are documented throughout. Margin legends, curl ornaments, horizontal fillers, pointed row-end clusters and frame projections are paratext, not mechanically converted to main-text punctuation.']
(r/'base-signs-middle.md').write_text('\n'.join(lines)+'\n')
print('pages',len(d['pages']),'findings',len(d['findings']),'targeted_evidence',len(d['targeted_evidence']))
print('confirmed changes',[(f['unit'],f['current_count'],f['observed_count']) for f in d['findings'] if f.get('kind')=='confirmed_shad_count_mismatch'])
