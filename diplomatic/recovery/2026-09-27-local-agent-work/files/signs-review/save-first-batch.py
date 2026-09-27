from pathlib import Path
import json,hashlib,shutil
repo=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur');w=Path(__file__).parent
prefix='signs-recovery-review-20260927'
out=repo/'diplomatic/reviews/chapter-01';ev=repo/'diplomatic/evidence/chapter-01'/prefix;ev.mkdir(parents=True,exist_ok=True)
units={x['id']:x for x in json.loads((repo/'diplomatic/collation/chapter-01/reading-units.json').read_text())};imgmeta=json.loads((repo/'editions/adzom-2000/image-manifest.json').read_text());cropmeta=json.loads((w/'first-five-crops.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
notes={
'U00030':('two detached shads after na: first immediately after the syllable, second after a blank interval before dga; neither joins the neighboring letters.',4,'AS-E-006.png'),
'U00035':("two detached shads after pa'i before rang snang: the first follows the final vowel-bearing syllable; a second vertical is separated by blank space before rang.",2,'AS-E-007.png'),
'U00105':('two detached shads after du: one after the completed du glyph, another before sprul. The du vowel stroke remains attached beneath its letter and is not counted as a shad.',1,'AS-E-008.png'),
'U00252':('two detached shads after gcod on the following page: one after final da, another before bcud. The left vertical belonging to the initial gcod glyph is not counted.',1,'AS-E-013.png'),
'U00372':("one detached shad after no before the smaller dris lan heading. The later upright at the heading's start joins the lower stroke of the initial dra form; it is not a second detached main-text shad.",4,None)
}
records=[];proposals=[]
for ident,(observed,row,prior) in notes.items():
 m=cropmeta[ident];n=m['pdf_page'];source=next(x for x in imgmeta['images'] if x['pdf_page']==n);old=units[ident]['reading_tibetan'];new=old[:-1]+'། །' if ident!='U00372' else old[:-2]
 assert new!=old
 path=ev/f'{ident}.png';shutil.copyfile(w/f'{ident}-native-crop.png',path)
 evidence=[{'path':str(path.relative_to(repo/'diplomatic')),'sha256':sha(path),'pixel_bounds':m['native_bounds'],'native_dimensions':m['native_image_dimensions'],'derivation':'unscaled rectangular crop of original-images.zip native image, no enhancement','source_archive':'editions/adzom-2000/original-images.zip','source_member':source['file'],'source_member_sha256':source['sha256'],'pdf_page':n,'bdrc_image':n+2}]
 if prior:
  pp=repo/'diplomatic/evidence/chapter-01/extension/base-signs-early'/prior;evidence.append({'path':str(pp.relative_to(repo/'diplomatic')),'sha256':sha(pp),'role':'earlier retained crop also visually inspected; fresh native crop controls this judgment'})
 uncertainty='Only the terminal sign count at this boundary is certified; this is not full punctuation or lexical proofreading. Unicode spacing represents separated strokes, not measured facsimile spacing.'
 locator=f'Adzom 2000 PDF {n}; BDRC I1KG11710 image {n+2}; main text row {row}; terminal boundary of {ident}'
 if ident=='U00252':locator+='; preceding words continue from PDF 12 into initial gcod on PDF 13'
 r={'id':f'SIGNS-RECOVERY-20260927-{ident}','units':[ident],'original_units':{ident:old},'replacement_units':{ident:new},'finding':'confirmed terminal punctuation mismatch','category':'source punctuation','disposition':'proposed; not integrated','confidence':'high for stated local sign allocation','locator':locator,'observed_strokes':observed,'uncertainty':uncertainty,'evidence':evidence,'source_tibetan_unchanged':units[ident]['source_tibetan'],'context_units':{x:units[x]['reading_tibetan'] for x in [f'U{int(ident[1:])-1:05d}',f'U{int(ident[1:])+1:05d}']}}
 records.append(r)
 proposals.append({'id':r['id'],'units':r['units'],'original_units':r['original_units'],'replacement_units':r['replacement_units'],'old':old,'new':new,'rationale':observed,'locator':locator,'evidence':[x['path'] for x in evidence],'evidence_sha256':{x['path']:x['sha256'] for x in evidence},'confidence':{'punctuation':'high for this terminal boundary only'},'source_record':f'reviews/chapter-01/{prefix}.json#{r["id"]}','uncertainty':uncertainty,'status':'proposed; not integrated'})
report={'id':prefix,'status':'provisional checkpoint; first five candidates reviewed','scope':'Guided fresh image check of first five integrated_original_unit_changes from recovery packet. No blind or continuous punctuation pass; no English translation QC. Canonical files and Tibetan source unchanged.','guidance':'guidelines/tibetan_translation_standard_v2.md Parts I and II; original glossary assignments retained; no terminology changes','source_pdf':'editions/adzom-2000/sgra-thal-gyur.pdf','source_pdf_sha256':sha(repo/'editions/adzom-2000/sgra-thal-gyur.pdf'),'candidate_source':'diplomatic/recovery/2026-09-27.json#local_punctuation_work','reviewed_units':list(notes),'remaining_integrated_candidates':['U00578','U00594','U00710','U01757','U02080','U02090','U02172','U02183','U02484','U02489'],'records':records,'method':'Read unchanged neighboring transcript anchors; visually inspect existing early sign crops and fresh unscaled native image crops. Native source files checked against stored SHA256. Count detached strokes locally, distinguishing letter strokes and smaller heading text. No automatic candidate acceptance or global normalization.','missing_inputs':'Earlier full sign-review reports remain unavailable; this checkpoint supplies new bounded evidence rather than reconstructing their wording.'}
(out/f'{prefix}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(out/f'{prefix}-additional-interventions.proposed.json').write_text(json.dumps(proposals,ensure_ascii=False,indent=2)+'\n')
lines=['# Adzom signs recovery review - 2026-09-27','','Provisional checkpoint: five guided candidate checks. Four terminal one-to-two shad corrections and one two-to-one correction are supported by fresh native-image inspection. No canonical file or source changed.','','| Anchor | Locator | Local finding |','| --- | --- | --- |']
for r in records:lines.append(f'| {r["units"][0]} | {r["locator"]} | {r["observed_strokes"]} |')
lines+=['','Each JSON record preserves original and proposed units, exact crop coordinates, native-image and evidence SHA-256, neighboring anchors, and uncertainty. The proposal file is separate for coordinator review/integration.','', 'This is a guided five-boundary check, not a continuous punctuation pass or chapter-completion certificate. Printed spacing is not measured by the Unicode space used between shads. Ten prior integrated candidates, middle candidates, insertions, and U01286 remain outside this checkpoint.']
(out/f'{prefix}.md').write_text('\n'.join(lines)+'\n')
print('saved',len(records),'records');print(json.dumps([{r['units'][0]:r['replacement_units'][r['units'][0]]} for r in records],ensure_ascii=False))
