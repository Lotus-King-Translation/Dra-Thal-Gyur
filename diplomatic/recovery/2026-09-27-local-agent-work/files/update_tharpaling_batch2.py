import json,hashlib,zipfile,io,subprocess
from pathlib import Path
from PIL import Image
r=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
f=r/'diplomatic/reviews/chapter-01/tharpaling-continuation-review-20260927.json'
d=json.loads(f.read_text())
for p in d['pages']:
 p.pop('approximate_anchor_neighborhood',None)
 p.pop('anchor_bounds_are_full_transcriptions',None)
 p['navigation_note']='No whole-page U-anchor bounds certified. Use only the separately recorded local observations for textual alignment.'
d['provenance_correction']='Batch2 withdraws the estimated whole-page U-anchor neighborhoods in batch1: they were navigation guesses, not independently established endpoints. The two separately evidenced local observations remain unchanged.'
def region(n,side,rows,box,issue):
 return {'rows':rows,'box_xyxy':box,'issue':issue,'coordinates_reference':f'diplomatic/evidence/chapter-01/recovered-tharpaling/p{n:03}-{side}.png','coordinate_convention':'zero-based half-open pixels in the existing enlarged crop, not native full-page coordinates','scope_qualification':'Examples of unresolved regions, not a claim that every remaining glyph is certified.'}
regions={
62:[('L',[1,2,3,4,5,6],[100,60,1450,610],'Intermittent fused ink masses and missing small strokes across left and medial groups; not all root/prefix/suffix distinctions resolved.'),('R',[4,5,6],[250,325,1630,620],'Extensive pale broken syllable groups in the lower three rows; exact wording is not independently read.')],
63:[('L',[1],[680,30,1510,135],'First restored verse has broken portions; the intervening small heading is present but its exact initial words and number are not certified.'),('L',[3,4,5,6],[680,210,1580,585],'Dense merged medial clusters, particularly rows3–4; expected wording cannot replace missing component discrimination.'),('R',[2,3,4,5,6],[500,130,1640,590],'Intermittent touching or pale stacks through the right-hand phrase groups; some complete phrases readable, no full-row certification.')],
64:[('L',[2,3,4,5,6],[300,165,1480,590],'Severe broken-stroke loss throughout left/medial parts of rows2–6 remains after polarity inversion.'),('R',[2,3,4,5,6],[960,170,1660,600],'Faded right phrase groups and endings; rows4–6 have further broad medial loss.'),('R',[4,5,6],[300,335,1150,600],'Substantial syllable strokes absent in this image; no reconstruction attempted.')],
65:[('L',[2,3,4,5,6],[100,135,1380,600],'Mixed overinking and granular fade in left and medial phrase groups; row6 has further fragmented endings.'),('R',[1,2,3,4,5,6],[180,50,1550,610],'Intermittent merged consonants and dotted losses across the six rows; this reviewer cannot certify every distinct syllable.')],
66:[('L',[1],[400,60,1560,160],'Pale fragmented upper-row syllables; small heading wording remains unresolved.'),('L',[2,4,6],[450,170,1700,610],'Dense blot at row2 toward right; broken medial stacks in row4 and a heavy ink mass in row6 obscure exact components.'),('R',[1,2],[0,60,1640,260],'Thin/broken strokes across upper two rows, including endings; several prefixes and suffixes not independently discriminated.'),('R',[3,4,5,6],[1050,250,1650,610],'Intermittent losses toward right endings; no full lexical or punctuation certification.')]
}
manifest=json.loads((r/'editions/tharpaling-1983/image-manifest.json').read_text())
with zipfile.ZipFile(r/'editions/tharpaling-1983/original-images.zip') as z:
 for n in range(62,67):
  m=next(x for x in manifest['images'] if x['pdf_page']==n)
  files={s:f'diplomatic/evidence/chapter-01/recovered-tharpaling/p{n:03}{s}.png' for s in ('','-L','-R')}
  src=Image.open(io.BytesIO(z.read(m['file']))).convert('RGB');ev=Image.open(r/files['']).convert('RGB')
  assert src.size==ev.size and src.tobytes()==ev.tobytes()
  p={'pdf_page':n,'bdrc_image':n+4,'main_rows_visually_inspected':[1,2,3,4,5,6],'visually_inspected':True,'fully_collated':False,'all_variants_enumerated':False,'navigation_note':'No whole-page U-anchor bounds certified. Use only separately recorded local observations for textual alignment.','unresolved_glyph_regions':[region(n,*x) for x in regions[n]],'source_quality':'Visible fade, broken strokes and/or overinking as specified; this report does not label the entire page illegible.','reader_capability':'The reviewer could follow some phrases but could not independently discriminate every glyph. Recognition of expected wording is not agreement evidence.','evidence_files':files,'evidence_sha256':{s:hashlib.sha256((r/pth).read_bytes()).hexdigest() for s,pth in files.items()},'archive_member':m['file'],'original_png_sha256':m['sha256'],'native_dimensions':list(ev.size),'original_pixels_match_archived_png':True}
  d['pages'].append(p)
locus={'id':'TH-CONT-20260927-S07','witness':'Tharpaling 1983 W27491','units':['U02308','U02309'],'insertion_ids':['A2000-C01-S05','A2000-C01-S06','A2000-C01-S07'],'base_snippet_at_review':'A2000-C01-S07: ཡང་ནི་ལྷ་དབང་དགའ་བྱེད་ཉོན།','comparison_reading':'ཡང་ནི་ལྷ་དབང་དགའ་བྱེད་ཉོན','comparison_context':'Page63 row1: two main phrase groups separated by a small heading. The latter main phrase is read here; the preceding verse and intervening heading are not fully transcribed.','status':'supported_partial_restoration_observation','confidence':'moderate for the latter main phrase; preceding main verse and small heading remain unresolved','locator':'PDF63 / BDRC image67 / row1; p063-restored-verses-heading.png latter main phrase, box [1110,0,1800,186] in that existing enlarged crop','rationale':'The enlarged strip visibly preserves yang ni lha dbang dga byed nyon as a connected main-text sequence after the small heading. The first restored verse has visible broken glyph components and the heading is small; neither receives all-character agreement from this review.','decision':'Record bounded corroboration of S07; preserve Adzom restoration and uncertainty for S05/S06. Do not infer continuous witness agreement.','evidence':['evidence/chapter-01/recovered-tharpaling/p063.png','evidence/chapter-01/recovered-tharpaling/p063-L.png','evidence/chapter-01/extension/tharpaling-continuation/p063-restored-verses-heading.png'],'review':'reviews/chapter-01/tharpaling-continuation-review-20260927.md'}
d['loci'].append(locus)
d['repository_head_at_save']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=r,text=True).strip()
d['method']='Direct inspection of all six main rows in native full-page images and existing enlarged L/R crops for PDF57–66. P57–60 and p64 also viewed with reversible RGB polarity inversion; p61 viewed in source polarity and inverse. Page63 restored-verse strip additionally inspected. No OCR, reconstructed letters, denoising, sharpening, or model-generated imagery. Original full-page pixels equal archived acquisition PNGs. Expected A readings were known; not a blind review.'
d['batch_state']='second_five_pages_saved_waiting_for_remote_checkpoint'
d['reviewed_pdf_pages']=list(range(57,67))
d['not_completed']=['Continuous exact collation and all-variant enumeration for pages57–66','Exact punctuation, small annotations and every root/suffix distinction','Pages67–71 not visually inspected in these two batches','No changes to Adzom base or canonical coverage files']
d['summary']={'visually_inspected_pages':10,'fully_collated_pages':0,'candidate_local_observations':3,'chapter_completion_gate_passed':False}
d['additional_evidence_sha256']={p:hashlib.sha256((r/'diplomatic'/p).read_bytes()).hexdigest() for p in locus['evidence']}
f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f.with_suffix('.loci.json').write_text(json.dumps(d['loci'],ensure_ascii=False,indent=2)+'\n')
md='''# Tharpaling continuation review — 27 September 2026

**PDF57–66 inspected; zero pages fully collated.** All six main rows visually traversed per page. [Structured scope](tharpaling-continuation-review-20260927.json); [local records](tharpaling-continuation-review-20260927.loci.json).

| PDF / BDRC image | Remaining glyph-reading limits |
|---|---|
| 57–61 / 61–65 | Faded and merged groups across all pages; exact unresolved boxes retained in JSON. |
| 62 / 66 | Merged left/medial ink; lower right rows4–6 particularly fragmented. |
| 63 / 67 | Restored first verse and small heading incomplete; medial ink masses across rows3–6. |
| 64 / 68 | Severe left/medial dropouts in rows2–6; broad lower/right loss despite inversion. |
| 65 / 69 | Recurring fused and broken groups; no complete row certified. |
| 66 / 70 | Pale upper rows, row2/6 ink masses and broken row4 medial stacks. |

Three bounded observations: U02100/U02101 at p56/57; p59 second restored verse; p63 latter restored verse ཡང་ནི་ལྷ་དབང་དགའ་བྱེད་ཉོན. Preceding verses and small headings retain the stated uncertainties.

Batch2 withdraws batch1 estimated whole-page U-anchor ranges: they were not established endpoints. The two supported local observations remain unchanged.

Native pixels match the acquisition archive. Full pages, L/R enlargements and specified polarity inversions inspected; no OCR or reconstructed letters. Familiar sequence recognition does not certify surrounding glyphs. Pages67–71 await the next checkpointed batch.
'''
f.with_suffix('.md').write_text(md)
print('saved', len(d['pages']), 'pages;',len(d['loci']),'local records;',len(md.splitlines()),'MD lines')
