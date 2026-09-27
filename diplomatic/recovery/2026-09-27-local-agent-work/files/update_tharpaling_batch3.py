import json,hashlib,zipfile,io,subprocess
from pathlib import Path
from PIL import Image
r=Path('/Users/mikkokotila/dev/Dra-Thal-Gyur')
f=r/'diplomatic/reviews/chapter-01/tharpaling-continuation-review-20260927.json'
d=json.loads(f.read_text())
assert d['reviewed_pdf_pages']==list(range(57,67))
def region(n,side,rows,box,issue):
 return {'rows':rows,'box_xyxy':box,'issue':issue,'coordinates_reference':f'diplomatic/evidence/chapter-01/recovered-tharpaling/p{n:03}-{side}.png','coordinate_convention':'zero-based half-open pixels in the existing enlarged crop, not native full-page coordinates','scope_qualification':'Examples of unresolved regions, not a claim that every remaining glyph is certified.'}
regions={
67:[('L',[1,2,3,4,5,6],[300,50,1930,575],'Frequent merged ink masses in medial phrase groups; several roots, prefixes and suffixes not independently discriminated.'),('L',[6],[200,475,550,575],'Small heading at lower left remains incomplete for this reader.'),('R',[1,2,3,4,5,6],[150,45,1400,570],'Granular losses and heavy touching stacks recur across right-side groups; no continuous exact transcription obtained.')],
68:[('L',[1,2,3,4,5,6],[150,75,1850,590],'Touching stacks mixed with fine-component dropout; especially dense at row1 middle and row4 right-middle.'),('R',[1,2,3,4,5,6],[520,40,1380,575],'Broken small strokes and overinked groups across upper and lower right portions; all syllable components not secure.')],
69:[('L',[1,2,3,4,5],[700,40,1900,465],'Pale broken medial strokes across several phrase groups; particularly fragmented row1 middle and row4 toward right.'),('R',[5],[530,345,710,455],'Solid dark blot occludes a local glyph cluster in row5; letters underneath are not reconstructed.'),('R',[1,2,3,4,5,6],[150,20,1370,555],'Other intermittent losses and touching strokes through right-side groups; complete rows remain unresolved.')],
70:[('L',[1,2,3,4,5,6],[0,65,1150,590],'Broken small strokes and merged letters recur in left/medial groups; row5 middle strongly speckled.'),('R',[1,2,3,4,5,6],[400,60,1360,620],'Upper right endings, small headings and medial groups remain partly fragmentary. Lower rows contain clearer sequences but not complete certified readings.')],
71:[('L',[1,2],[1350,75,1950,260],'Broad dropout toward upper-row middle/right removes much of several syllable groups; no reconstruction from reference text.'),('R',[1,2],[250,70,1290,260],'Thin and partly missing strokes across upper right phrases and a small note/heading at row2 end; exact wording unresolved.'),('L',[3,4],[700,275,1400,430],'Some touching letter groups in lower-left/medial text remain beyond this reviewer; no all-character agreement.'),('R',[3,4],[500,260,1300,435],'Remaining broken strokes toward row3/4 right; exact ending letters not fully discriminated.')]
}
manifest=json.loads((r/'editions/tharpaling-1983/image-manifest.json').read_text())
with zipfile.ZipFile(r/'editions/tharpaling-1983/original-images.zip') as z:
 for n in range(67,72):
  m=next(x for x in manifest['images'] if x['pdf_page']==n)
  files={s:f'diplomatic/evidence/chapter-01/recovered-tharpaling/p{n:03}{s}.png' for s in ('','-L','-R')}
  src=Image.open(io.BytesIO(z.read(m['file']))).convert('RGB');ev=Image.open(r/files['']).convert('RGB')
  assert src.size==ev.size and src.tobytes()==ev.tobytes()
  p={'pdf_page':n,'bdrc_image':n+4,'main_rows_visually_inspected':[1,2,3,4,5,6],'visually_inspected':True,'fully_collated':False,'all_variants_enumerated':False,'navigation_note':'No whole-page U-anchor bounds certified. Use only separately recorded local observations for textual alignment.','unresolved_glyph_regions':[region(n,*x) for x in regions[n]],'source_quality':'Visible fade, broken strokes and/or overinking as specified; this report does not label the entire page illegible.','reader_capability':'The reviewer could follow some phrases but could not independently discriminate every glyph. Recognition of expected wording is not agreement evidence.','evidence_files':files,'evidence_sha256':{s:hashlib.sha256((r/pth).read_bytes()).hexdigest() for s,pth in files.items()},'archive_member':m['file'],'original_png_sha256':m['sha256'],'native_dimensions':list(ev.size),'original_pixels_match_archived_png':True}
  if n==71:
   p['chapter_01_scope']='Rows1–4 and row5 through its colophon. Row5 right continuation and row6 were displayed and visually traversed for boundary context only; they are Chapter2, not a completed Chapter2 review.'
   p['confirmed_chapter_end_anchor']='U02635'
   p['confirmed_chapter_end_locator']='PDF71 / BDRC I4448 image75 / row5; closing colophon native crop [490,277,1205,329]'
  d['pages'].append(p)
locus={'id':'TH-CONT-20260927-CHAPTER-END','witness':'Tharpaling 1983 W27491','units':['U02635','U02636'],'base_snippet_at_review':'U02635 closing colophon; U02636 next chapter incipit.','comparison_reading':None,'comparison_context':'Physical chapter closing colophon on row5, followed by a blank interval, intervening signs/text and the next incipit farther right.','status':'chapter_boundary_reconfirmed','confidence':'high for physical boundary; complete colophon spelling and exact punctuation not newly certified','locator':'PDF71 / BDRC I4448 image75 / main row5. Native colophon crop [490,277,1205,329]; see separate next-incipit crop.','rationale':'The separately inspected colophon strip has a clear closing leu ste dang poo ending; the next-incpit strip begins de nas lha dbang and continues beyond the boundary. This confirms the physical location reported in tharpaling-collation.md, not full-page agreement. No guessed page-start anchor or complete lexical colophon transcription is introduced.','decision':'Retain U02635 as Chapter1 endpoint, excluding Chapter2 continuation from Chapter1 coverage. Keep all unresolved preceding glyph groups explicit.','evidence':['evidence/chapter-01/recovered-tharpaling/p071.png','evidence/chapter-01/recovered-tharpaling/p071-L.png','evidence/chapter-01/recovered-tharpaling/p071-R.png','evidence/chapter-01/tharpaling/crops/p071-colophon-precise.png','evidence/chapter-01/tharpaling/crops/p071-next-incipit.png'],'review':'reviews/chapter-01/tharpaling-continuation-review-20260927.md','prior_observation':'reviews/chapter-01/tharpaling-collation.md physical chapter boundary'}
d['loci'].append(locus)
d['repository_head_at_save']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=r,text=True).strip()
d['method']='Direct inspection of all six main rows in native full-page images and existing enlarged L/R crops for PDF57–71; page71 rows after Chapter1 closure provide boundary context only. P57–60 and p64 also viewed with reversible RGB polarity inversion; p61 viewed in source polarity and inverse. Page63 restored-verse strip and page71 colophon/next-incipit strips additionally inspected. No OCR, reconstructed letters, denoising, sharpening, or model-generated imagery. Original full-page pixels equal archived acquisition PNGs. Expected A readings were known; not a blind review.'
d['batch_state']='final_five_pages_saved_waiting_for_remote_checkpoint'
d['reviewed_pdf_pages']=list(range(57,72))
d['not_completed']=['Continuous exact collation and all-variant enumeration for pages57–71 through Chapter1 endpoint','Exact punctuation, small annotations and every root/suffix distinction','No Chapter2 collation: page71 right row5 and row6 observed only as boundary context','No changes to Adzom base or canonical coverage files']
d['remaining_capacity_limits']=['This reviewer cannot independently discriminate every root, prefix, suffix, superscript and subscript in the existing low-resolution, partly fused or broken images. This is a reader limitation, not proof that another reader cannot resolve them.','Polarity inversion and existing enlargements change visibility but add no lost spatial information. Some local pixels visibly omit strokes or obscure them with solid ink; expected Tibetan must not be substituted.','No clean text or OCR alignment was used as glyph proof; no blanket equivalence or exhaustive variant enumeration is supported.','A second competent Tibetan scan reader, improved source imaging where available, and exact glyph-level comparison remain necessary for the unresolved regions and complete Chapter1 certification.']
d['summary']={'visually_inspected_pages':15,'fully_collated_pages':0,'candidate_local_observations':4,'chapter_completion_gate_passed':False}
for p in locus['evidence']:
 d['additional_evidence_sha256'][p]=hashlib.sha256((r/'diplomatic'/p).read_bytes()).hexdigest()
f.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
f.with_suffix('.loci.json').write_text(json.dumps(d['loci'],ensure_ascii=False,indent=2)+'\n')
md='''# Tharpaling continuation review — 27 September 2026

**PDF57–71 inspected; zero pages fully collated.** Six main rows traversed per page; page71 after its Chapter1 colophon is boundary context only. [Structured scope](tharpaling-continuation-review-20260927.json); [local records](tharpaling-continuation-review-20260927.loci.json).

| PDF / BDRC image | Remaining glyph-reading limits |
|---|---|
| 57–61 / 61–65 | Faded and merged groups throughout; exact unresolved boxes retained in JSON. |
| 62–66 / 66–70 | Broken upper/lower groups and ink masses; p64 severe loss despite inversion; p63 first restored verse and small heading incomplete. |
| 67 / 71 | Fused medial stacks across six rows; small lower-left heading incomplete. |
| 68 / 72 | Fine-component losses mixed with touching ink, including right endings. |
| 69 / 73 | Broad intermittent fade; a solid blot occludes a row5 right-hand cluster. |
| 70 / 74 | Broken left/medial groups and right endings; small headings not resolved. |
| 71 / 75 | Severe upper-row dropout; some lower groups incomplete. Physical Chapter1 endpoint confirmed on row5. |

Four bounded observations: U02100/U02101 at p56/57; p59 second restored verse; p63 latter restored verse ཡང་ནི་ལྷ་དབང་དགའ་བྱེད་ཉོན; p71 Chapter1 endpoint U02635. Other letters retain stated uncertainty.

Batch2 withdrew batch1 estimated whole-page U-anchor ranges. Only locally evidenced alignment survives. Native page pixels match the acquisition archive; no OCR or reconstructed glyphs were used.

The remaining limit is both damaged image information and this reader’s inability to discriminate every glyph. Another competent Tibetan reader may resolve more. Complete glyph-level collation remains necessary; chapter readiness is not established.
'''
f.with_suffix('.md').write_text(md)
print('saved',len(d['pages']),'pages;',len(d['loci']),'local records;',len(md.splitlines()),'MD lines')
