import json,hashlib,shutil,zipfile,io,subprocess
from pathlib import Path
from PIL import Image
r=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur');w=Path('/Users/mikkokotila/Documents/Codex/2026-09-27/first-find-this-cloud-chatgpt-chat/work/independent-signs-late');e=r/'diplomatic/evidence/chapter-01/independent-signs-late-20260927';e.mkdir(exist_ok=True)
srcunits={x['id']:x['tibetan'] for x in json.loads((r/'translations/2026-09-26-full-draft/data/source-units.json').read_text())}
old=json.loads((r/'diplomatic/reviews/chapter-01/signs-recovery-review-20260927.json').read_text())
manifest=json.loads((r/'editions/adzom-2000/image-manifest.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copye(name, page, bounds=None):
 shutil.copyfile(w/name,e/name)
 return {'path':str((e/name).relative_to(r/'diplomatic')),'sha256':sha(e/name),'pdf_page':page,'bdrc_image':page+2,'source_member':f'{page+2:04}.png','pixel_bounds':bounds or [0,0,5696,1344],'derivation':'byte-identical archived PNG' if bounds is None else 'unscaled rectangular native crop; no enhancement','coordinates':'zero-based half-open source pixels'}
configs=[
 ('U00594',25,6,(840,1010),'p025-opening-sequence.png',[1375,245,3375,440],
  "Printed first main fragment ཀྱིས་སྤྲས (U00569 tail), followed by the complete U00570 འདོད་པའི་ཡོན་ཏན་རྣམས་ཀྱིས་བརྒྱན; no inferred whole-page anchor range.",
  [('U00593','row6, preceding complete verse འཆར་ཁ་ཆུན་འཕྱང་རྣམས་ཀྱིས་བརྒྱན'),('U00595','row6 following begins སྟོན་པའི་བསྟན་པ; remainder of this following unit not newly certified')],
  'Two separated detached vertical shads follow final འབྱིན before སྟོན. The first is immediately after the completed final letter, the second precedes the following phrase after blank space.',
  'འབྲུག་སྒྲོགས་གློག་དམར་ལྕེ་རྣམས་འབྱིན'),
 ('U00710',30,3,(500,725),'p030-opening-corrected.png',[550,320,2700,505],
  "Printed opening བསྟན་རྗེས་འཛིན་སེམས་ཀྱི་གནད (U00698 tail), followed by complete U00699 འགྲོ་བ་བདག་སྐྱོབ་རླུང་གི་ལྷ. Initial lung of U00698 belongs before this page and is not inserted into its opening.",
  [('U00709','row3 preceding བརྡའ་ཡི་འཇུག་པ་ཐམས་ཅད་སྣང'),('U00711','row3 following རང་བཞིན་རྫོགས་པས་རྫོགས་པ་ཆེ')],
  'A separate triangular tsheg stands at headline level after the completed final nga of གང and before the first detached shad. Two detached shads follow. The source annotation beneath the main line is not part of this terminal sequence.',
  'སོ་སོའི་ནུས་པས་བསྒྱུར་བ་གང'),
 ('U01757',69,2,(380,610),'p069-opening.png',[550,240,2550,430],
  "Printed first fragment ཀྱིས (U01749 tail), then U01750 ལས་ཀྱི་མཐའ་རྣམས་བསྒྱུར་བར་བྱའོ and a smaller heading. The complete U01757 target is separately identifiable on row2.",
  [('U01756','row2 preceding མཆོག་ཏུ་གནས་པ་བཅུ་དྲུག་ཉིད'),('U01758','row2 following རང་ངོ་དག་པ་བཞི་ཡིས་ནི')],
  'Two detached shads follow འགྱུར before རང་ངོ. The first stands after the final ra stroke; the second is separated before rang. The curved lower stroke belongs to neighboring letter material, not an additional delimiter.',
  'ཕོ་མོའི་སྡེབས་ཀྱིས་བརྒྱད་དུ་འགྱུར'),
 ('U02080',81,4,(620,810),'p081-opening.png',[550,240,2550,430],
  "Printed first complete main phrase U02064 ཡེ་ཤེས་དབང་བསྐུར་གྱིས་བརྒྱན་ཏེ, followed by U02065 opening དངོས་གྲུབ. The target is on row4, not the similarly sized phrase group in a neighboring row.",
  [('U02079','row4 preceding ཡན་ལག་འདུས་པའི་ཆོ་ག་ལས'),('U02081','row4 following གསལ་བར་རྣལ, continued row5 opening འབྱོར་ལུས་གནས་ཏེ')],
  'Two detached shads follow ནི before གསལ. The second vertical is separated from the following ga body; neighboring lower curved strokes are excluded from the sign count.',
  'ལྷ་མོའི་མདོག་དང་ཞལ་ཕྱག་ནི')
]
records=[]
with zipfile.ZipFile(r/'editions/adzom-2000/original-images.zip') as z:
 for uid,page,row,ys,op,bounds,opening,neighbors,observed,main in configs:
  m=next(x for x in manifest['images'] if x['pdf_page']==page)
  b=z.read(m['file']);assert hashlib.sha256(b).hexdigest()==m['sha256']==sha(w/f'p{page:03}.png')
  oldrec=next(x for x in old['records'] if x['units']==[uid]);oe=oldrec['evidence'][0]
  native=Image.open(io.BytesIO(b));oldcrop=Image.open(r/'diplomatic'/oe['path'])
  assert native.crop(oe['pixel_bounds']).convert('RGB').tobytes()==oldcrop.convert('RGB').tobytes()
  ev=[copye(f'p{page:03}.png',page),copye(op,page,bounds)]
  for j,(a,bx) in enumerate(((550,2200),(2100,3800),(3700,5350))):ev.append(copye(f'p{page:03}-targetrow-{j}.png',page,[a,ys[0],bx,ys[1]]))
  ev.append({'path':oe['path'],'sha256':sha(r/'diplomatic'/oe['path']),'source_member':m['file'],'pixel_bounds':oe['pixel_bounds'],'derivation':'historical native crop; independently reidentified and pixels reverified','coordinates':'zero-based half-open source pixels'})
  if uid=='U00710':ev.append(copye('p030-gang-terminal.png',page,[3490,550,3820,675]))
  if uid=='U02080':ev.append(copye('p081-next-anchor-continuation.png',page,[630,755,1800,965]))
  original=oldrec['original_units'][uid]
  proposed=main+('་། །' if uid=='U00710' else '། །')
  rec={'id':f'SIGNS-INDEPENDENT-LATE-20260927-{uid}','units':[uid],'source_tibetan_unchanged':srcunits[uid],'original_units':{uid:original},'replacement_units':{uid:proposed},'main_lexical_sequence_identified_from_native':main,'page_opening_observed_before_sign_count':opening,'neighboring_anchors_identified':[{'unit':u,'observed_scope':t} for u,t in neighbors],'target_correspondence':'independently confirmed from native page and row context; not accepted from crop label','finding':'confirmed local punctuation mismatch','category':'source punctuation','disposition':'supported proposal; coordinator adoption pending; no canonical edit by reviewer','confidence':{'target_identification':'high for complete target main wording and stated neighboring scope','sign_allocation':'high for this local boundary only'},'locator':f'Adzom 2000 PDF{page} / BDRC I1KG11710 image{page+2} / main row{row}','observed_signs':observed,'terminal_shad_count':2,'terminal_tsheg_confirmed':True if uid=='U00710' else None,'native_source':{'archive':'editions/adzom-2000/original-images.zip','member':m['file'],'sha256':m['sha256'],'native_dimensions':[5696,1344],'source_bytes_match_manifest':True,'historical_candidate_crop_pixels_match_native':True},'evidence':ev,'limits':['Only the specified target boundary is a punctuation judgment; no global normalization or whole-page proofreading.','Neighbor descriptions state the actual displayed wording; unseen continuations are not certified.','Unicode spaces distinguish separated marks; they do not reproduce measured physical spacing.','Expected candidate readings were available; this independent correspondence check is not blind.']}
  if uid=='U00710':
   rec['existing_intervention_dependency']='SCAN-CH1-LAYER-00710: retain existing main/annotation separation; restore only the terminal tsheg removed by its main replacement.'
   rec['annotation_scope']='The separate smaller note below the main line is visibly separate; its complete wording is not independently re-certified by this punctuation review.'
  records.append(rec)
inputs=['AGENTS.md','guidelines/tibetan_translation_standard_v2.md','glossary/expanded_tibetan_english_glossary.csv','diplomatic/reviews/chapter-01/opening-locator-audit-20260927.json','diplomatic/reviews/chapter-01/sign-adoption-audit-20260927.md','diplomatic/reviews/chapter-01/signs-recovery-anchor-audit-20260927.json','diplomatic/reviews/chapter-01/signs-recovery-review-20260927.json','diplomatic/collation/chapter-01/additional-interventions.json','translations/2026-09-26-full-draft/data/source-units.json']
d={'id':'independent-signs-late-20260927','date':'2026-09-27','scope':'Four withdrawn candidates U00594/U00710/U01757/U02080 only. Native full-page orientation, page opening and complete target wording with surrounding anchors checked before sign allocation. No English translation QC or canonical edits.','status':'four supported proposals saved for coordinator checkpoint and adoption review','repository_head_at_save':subprocess.check_output(['git','rev-parse','HEAD'],cwd=r,text=True).strip(),'source_pdf':'editions/adzom-2000/sgra-thal-gyur.pdf','source_pdf_sha256':sha(r/'editions/adzom-2000/sgra-thal-gyur.pdf'),'method':['Display each complete archived native page for physical orientation; inspect unscaled opening and target-row segments.','Identify target lexical sequence and neighboring anchors before viewing historical terminal crop for sign judgment.','Inspect complete historical crop and an extra unscaled terminal crop for U00710; verify historical crop pixels against archived member.','Preserve all original bytes, no OCR, denoising, sharpening, resynthesis or lexical reconstruction.','The reviewer knew the proposals and source transcript; target correspondence and mark allocation were checked against the actual image.'],'input_sha256':{p:sha(r/p) for p in inputs},'records':records,'summary':{'targets_reidentified':4,'supported_punctuation_proposals':4,'canonical_edits':0,'full_page_proofreading':False,'chapter_completion_gate_passed':False}}
p=r/'diplomatic/reviews/chapter-01/independent-signs-late-20260927.json';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
md='''# Independent sign review — four later candidates

**Four targets verified; four local proposals supported.** Full native page context, opening wording and neighboring anchors were established before terminal marks were counted. [Exact provenance and readings](independent-signs-late-20260927.json).

| Anchor | Confirmed locator | Local finding |
|---|---|---|
| U00594 | PDF25 / image27 / row6 | Two detached shads after འབྱིན before སྟོན. |
| U00710 | PDF30 / image32 / row3 | Discrete tsheg after གང before two shads; retain the existing annotation separation. |
| U01757 | PDF69 / image71 / row2 | Two detached shads after འགྱུར before རང་ངོ. |
| U02080 | PDF81 / image83 / row4 | Two detached shads after ནི before གསལ. |

The complete target main wording matches each claimed anchor. All four archived native source hashes match their manifest; historical candidate crops reproduce the declared native pixels. New full-page, opening and row-context evidence is preserved.

These are independent visual rechecks of known proposals, not blind reviews. Only the specified punctuation boundaries are certified. The U00710 note’s complete wording, other page text and whole-chapter readiness are outside this judgment. Canonical files remain unchanged pending coordinator adoption.
'''
p.with_suffix('.md').write_text(md)
print('Saved four records and',len(list(e.iterdir())),'evidence images;',sum(x.stat().st_size for x in e.iterdir()),'bytes;',len(md.splitlines()),'MD lines')
