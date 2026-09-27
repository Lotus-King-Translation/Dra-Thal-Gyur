import json,hashlib
from pathlib import Path
root=Path('/workspace/scratch/a117ee885aff')
source='Dra-Thal-Gyur/editions/gcn-manuscript/bdrc-W1ER128.pdf'
d={
 'witness':'Gcn',
 'source_pdf':source,
 'source_pdf_sha256':'0e32b67b69e6bc57059993c511981154c15f5eeacad2217003f03bae124f0501',
 'assigned_range':{'pdf_pages':[449,484],'end':'Chapter 1 colophon, PDF484 row4; rows5–7 excluded'},
 'status':'bounded_attempt_failed_for_continuous_lexical_collation_with_duplicate_and_boundary_observations',
 'method':[
  'Rendered the complete PDF page with PyMuPDF Matrix(1,1), alpha=False, producing the full MRC composite at 3000×811. The first embedded 999×270 background image alone is unsuitable for collation.',
  'Compared opening and later local phrases against the corrected Chapter1 reading units and corrected-ch1-wylie.txt. Full-page images and overlapping 2× halves were inspected for PDF449–451, with narrower 2×/3× row and opening targets.',
  'Compared PDF452/453 with450/451 visually to identify repeated exposures. PDF454 received only a full-page readability inspection. PDF484 upper four rows received full-page and narrower local inspection.',
  'The cursive letter forms and faded/compressed strokes could not be discriminated reliably enough to certify consecutive complete readings. Isolated phrase alignment is explicitly not counted as lexical agreement. No inference of agreement, omission, or transposition is drawn from the uncollated ranges.',
  'Image display, rendering, and a locator attempt are separately identified; rendering alone is not inspection. No Chapter2 readings were collated.'
 ],
 'exact_diplomatic_preservation':False,
 'continuous_lexical_collation_completed':False,
 'bdrc_image_mapping':'Not established for these pages. Do not infer PDF-to-BDRC numbering from the incomplete IIIF sample.',
 'main_crops':{'left': [80,100,1610,690],'right':[1440,90,2870,690],'scale':2,'coordinates':'native composite pixels; full bounds[0,0,3000,811]'},
 'attempts':[
  {'pdf_page':449,'rows':[1,7],'status':'all seven rows viewed in overlapping halves; attempted phrase alignment, no consecutive exact comparison achieved','first_unit_locator_candidate':'U01427','first_unit_locator_candidate_status':'disputed and unverified; do not use for alignment','first_unit_locator_candidate_basis':'Initial phrase impression, not a secure reading. The middle reader sequentially reached PDF442 at U00951–U00988, which disputes this much later opening unless an intervening jump is established. No such jump has been verified. Parent locator is not independent authority; the PDF448 ending remains pending.','last_unit_locator':None,'unresolved':'Full words and suffixes through the attempted main rows; the end unit is not established in this report. Do not use a presumed next-page anchor to fill it.','evidence':['p449.png','p449-left-2x.png','p449-right-2x.png','p449-opening-target.png','p449-row1-2x.png','p449-row7-2x.png']},
  {'pdf_page':450,'rows':[1,7],'status':'all seven rows viewed in overlapping halves; attempted phrase alignment, no consecutive exact comparison achieved','first_unit_locator':None,'last_unit_locator':None,'unresolved':'Opening and closing units are not securely established. An informal U01480 opening conjecture was not reliable enough to adopt.','evidence':['p450.png','p450-left-2x.png','p450-right-2x.png','p450-opening-target.png','p450-row1-2x.png','p450-row7-2x.png']},
  {'pdf_page':451,'rows':[1,7],'status':'full page and overlapping halves viewed; concentrated locator attempt on row1, without consecutive exact comparison','first_unit_locator_candidate':'U01511','first_unit_locator_candidate_basis':'Row1 resembles tha ma yin pa shes pa\'o, then U01512/1513; candidate only. Small heading above row2 left would fit U01514, but its letters are not certified.','last_unit_locator':None,'unresolved':'The row1 anchor is a candidate, and remaining main text and annotations are uncollated.','evidence':['p451.png','p451-left-2x.png','p451-right-2x.png','p451-opening-target.png','p451-row1-2x.png']},
  {'pdf_page':452,'rows':[1,7],'status':'full-page structural comparison only; observed repeated exposure of450','lexical_collation':False,'evidence':['p452.png']},
  {'pdf_page':453,'rows':[1,7],'status':'full-page structural comparison only; observed repeated exposure of451','lexical_collation':False,'evidence':['p453.png']},
  {'pdf_page':454,'rows':[1,7],'status':'full-page readability assessment only; no reading-unit comparison','lexical_collation':False,'evidence':['p454.png']},
  {'pdf_page':484,'rows':[1,4],'status':'local boundary inspection and limited reading attempts; no continuous upper-four-row collation','first_unit_locator_candidate':'U02617','last_unit_locator':'U02635','unresolved':'Main lexical comparison of rows1–3 is incomplete. Row4 colophon full wording, faint internal words, and punctuation are not certified.','evidence':['p484.png','p484-colophon-left.png','p484-colophon-right.png','p484-colophon-center-3x.png','p484-colophon-end-3x.png','p484-r2-left.png','p484-r2-right.png']}
 ],
 'uninspected_pages':[455,483],
 'uninspected_pages_note':'PDF455–483 inclusive were not visually inspected in this task. Images455/456 happened to be rendered while preparing crops, which is not inspection. No claim of coverage is made for these pages.',
 'findings':[
  {'id':'GCN-L-001','status':'observed_structural_repeat','pdf_pages':[450,452],'reading_units':None,'observation':'The same manuscript side appears twice: matching seven-row text layout, left-edge smear, row7 pen strokes, and physical border damage. Tonal/background treatment differs.','implication':'Do not count the second exposure as an additional text passage or advance reading-unit numbering through it. This is a repeated image exposure, not an inferred scribal repetition.','evidence_bounds':[0,0,3000,811],'evidence':['p450.png','p452.png']},
  {'id':'GCN-L-002','status':'observed_structural_repeat','pdf_pages':[451,453],'reading_units':None,'observation':'The same manuscript side appears twice: matching opening ornament, small annotations, row7 left smear, seven-row text layout, and border contours. Tonal/background treatment differs.','implication':'Do not count the second exposure as an additional text passage.','evidence_bounds':[0,0,3000,811],'evidence':['p451.png','p453.png']},
  {'id':'GCN-L-003','status':'unresolved_reading','pdf_pages':[484],'row':2,'reading_units':['U02625'],'base_lemma_wylie':'cho phrul du','observed_reading_wylie':None,'query':'The final particle at the end of the cho phrul phrase is not securely discriminated as du/gyis in this pass. Do not count agreement with the base or the Ts variant.','evidence_bounds':[1450,225,2800,335],'evidence':['p484-r2-right.png','p484-r2-left.png']},
  {'id':'GCN-L-004','status':'unresolved_reading','pdf_pages':[484],'row':4,'reading_units':['U02635'],'base_lemma_wylie':'sna tshogs bkod pa rang byung man ngag gi rtsa ba nges par byung bai leu ste dang poo','observed_reading_wylie':None,'query':'The faint internal wording after sna tshogs bkod pa is not securely read; particularly rang byung presence/absence cannot be decided here. Do not import the Ts colophon omission into this witness.','evidence_bounds':[1150,365,2070,433],'evidence':['p484-colophon-center-3x.png','p484-colophon-left.png']},
  {'id':'GCN-L-005','status':'observed_local_boundary','pdf_pages':[484],'row':4,'reading_units':['U02635'],'observed_reading_wylie':'dang poo','observation':'The separated final dang po\'o is locally legible at the end of the Chapter1 colophon. This supports the row4 Chapter1 boundary already mapped by the parent. It does not certify the entire colophon or its exact punctuation.','evidence_bounds':[1880,340,2760,434],'evidence':['p484-colophon-end-3x.png']}
 ],
 'evidence_directory':'/workspace/scratch/a117ee885aff/gcn-late',
 'repository_mutations':False,
 'next_required_work':'A reader able to discriminate this cursive hand must collate the attempted ranges and PDF455–483. Retain this report as an attempted-coverage record, not a completed witness pass.'
}
(root/'gcn-late.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
lines=['# Gcn late Chapter1: bounded attempted reading','',
 '**Continuous lexical collation was not achieved.** This report records attempted ranges, two secure repeated-image pairs, and a local Chapter1 boundary observation. It provides no whole-page or whole-range lexical agreement certificate.','',
 f'Source: `{source}`; SHA256 `{d["source_pdf_sha256"]}`. Assigned PDF449–484, ending at row4 of484. No Chapter2 readings were collated.','',
 '## Method and limitation','']+[x for x in d['method']]+['',
 'Full MRC composites are3000×811; native coordinates are used below. Overlapping half crops were [80,100,1610,690] and [1440,90,2870,690], displayed2×. Source first embedded backgrounds were not used alone. PDF-to-BDRC image mapping remains unestablished.','',
 '## Attempted coverage','', '| PDF page | Actual work | Anchor / limit |','|---|---|---|']
for a in d['attempts']:
 anchor=a.get('first_unit_locator') or a.get('first_unit_locator_candidate') or 'No secure start anchor'
 if a.get('first_unit_locator_candidate'): anchor+=' (disputed, unverified candidate)' if a.get('first_unit_locator_candidate_status') else ' (unverified candidate only)'
 lines.append(f'| {a["pdf_page"]} | {a["status"]} | {anchor}; end {a.get("last_unit_locator") or "not established"} |')
lines+=['','PDF455–483 inclusive were not inspected. Rendering455/456 while preparing images does not count as inspection. All attempted pages retain unresolved main-text readings; annotations and exact punctuation are uncollated.','',
 '## Findings','']
for f in d['findings']:
 lines +=[f'### {f["id"]}: {f["status"]}','',f'PDF {", ".join(map(str,f["pdf_pages"]))}'+(f', row{f["row"]}' if 'row'in f else '')+'. '+f.get('observation',f.get('query','')),f.get('implication',''),f'Evidence bounds `{f["evidence_bounds"]}`; '+', '.join('`'+s+'`'for s in f['evidence'])+'.','']
lines+=['## Consequences','',
 'PDF450/452 and451/453 must be handled as repeated exposures rather than independent consecutive text. The proposed U1427 locator for449 is disputed and unverified against the sequential middle-reader PDF442 U951–988 endpoint; do not use it as alignment authority. The proposed U1511 locator for451/453 is also an unverified candidate and may share the same expected-text error. No new lexical variant is established here. The final dang po\'o at484row4 supports the existing boundary but does not establish the full colophon wording.','',
 d['next_required_work'],'', 'No repository files were changed.']
(root/'gcn-late.md').write_text('\n'.join(lines)+'\n')
print('Saved gcn-late.json/md; attempts',len(d['attempts']),'findings',len(d['findings']))
