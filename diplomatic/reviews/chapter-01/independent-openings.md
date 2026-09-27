# Degé and Tingkye opening: limited visual sample

**Second-reading update (2026-09-27):** The [targeted rereading](second-dege-tingkye.md) resolves Tingkye U00018 terminal *khang* and U00026 terminal *r* as present, supports Tingkye U00019 *rig pa* against Degé/Adzom *rig pas*, and preserves the remaining Tingkye verb and Degé compact-text uncertainties. That report supersedes the corresponding tentative statements below.

Prepared 2026-09-27 for the diplomatic-edition work. This is a **sample of the opening**, not a complete chapter collation, not an edition, and not evidence that all conflicts in chapter 1 have been identified. The comparison baseline here is the supplied Adzom e-text and its `source-units.json` identifiers, not an independently established Adzom scan reading. Any final Adzom reading must be checked against its facsimile.

## Material actually inspected

- `editions/dege-W1ER7/sgra-thal-gyur.pdf`, PDF page 1, image group **I1ER175**, image **647**. Main text has seven lines. The main-line opening corresponding to U00012–U00028 is on lines 2–4. The physical Tibetan folio number is not reliably read in this inspection, so none is supplied or inferred.
- `editions/tingkye-1973/sgra-thal-gyur.pdf`, PDF pages 1–2, image group **I1765**, images **394–395**, visibly printed pages **386–387**. The root begins on the last two of seven main lines of printed page 386. U00012–U00014 are on page 386 line 7; U00015 spans the page turn; U00016–U00028 continue on printed page 387 lines 1–3.
- The first three pages of both PDFs were rendered and the relevant opening areas inspected at enlarged crop scale. Most of page 2 and page 3 were outside the checked unit range. They must not be represented as collated.
- Tingkye `bdrc-W21518-9.pdf` was **not** used. Its mapping is unresolved according to the repository README.

Rendering used PyMuPDF after bundled Poppler failed to load `libpoppler.so.160`. Repository source files were not modified. Temporary crops, and temporary green-channel contrast views of the red Degé print, served only as viewing aids. None is a replacement source. The observed variants below are visible in the unenhanced images as well.

## Image evidence and identifiers

| Witness | PDF page | BDRC image | Printed page | Source image URL | Source image SHA-256 |
| --- | --- | --- | --- | --- | --- |
| Degé | 1 | I1ER175 / 647 | Tibetan folio not confidently read | https://iiif.bdrc.io/bdr:I1ER175::I1ER1750647.jpg/full/max/0/default.jpg | `50a914969454ee35facff1492ad236e62cf90746f3dd8efd5cdccaba4674405f` |
| Tingkye | 1 | I1765 / 394 | 386 | https://iiif.bdrc.io/bdr:I1765::17650394.TIF/full/max/0/default.png | `420996df86f86cb4d341e81f83e664f982f05ce9a85288da6ec1c72c52095a0c` |
| Tingkye | 2 | I1765 / 395 | 387 | https://iiif.bdrc.io/bdr:I1765::17650395.TIF/full/max/0/default.png | `25e7b0d12ba5a43f964476883fd7e7133cdb3362cda947aa1b835dc509ae9077` |

URLs and hashes are copied from each repository image manifest. They were not fetched anew. PDF page and visible printed-page relationships were checked visually.

## Conflicts that can be reported conservatively

These are lexical/orthographic snippets only. No assertion of character-for-character punctuation equivalence is intended: Tingkye uses a repeated multi-dot terminal mark, unlike the Degé print's shad. Whitespace in these snippets is editorial word separation. A complete diplomatic punctuation apparatus still requires separate treatment.

| Adzom working unit | Adzom e-text reading | Tingkye scan reading | Tingkye locator | Degé scan comparison | Reason to retain the Adzom reading in a *diplomatic Adzom base* (subject to scan verification) |
| --- | --- | --- | --- | --- | --- |
| U00013 | འཁོར་དང་འདས་པའི་ཐོག་མར་ནི | འཁོར་དང་འདས་པའི་ཐོག་མར | PDF 1 / image 394 / printed 386, line 7 | Degé PDF 1 / image 647, line 2 visibly includes terminal ནི | Tingkye lacks ནི. A diplomatic base retains the base witness's attested text; agreement with Degé supplies comparative support but is not a license to reconstruct a majority reading. |
| U00014 | རང་བྱུང་བྱས་པ་མེད་པ་ལས | རང་བྱུང་བྱས་པ་མེད་པ་ལ | PDF 1 / image 394 / printed 386, line 7 | Degé PDF 1 / image 647, line 2 has terminal ལས | Tingkye has ལ in place of ལས. Retain the base particle if its scan confirms it, rather than harmonizing its grammar with another witness. |
| U00022 | སྐུ་དང་ཡེ་ཤེས་ཤེས་རབ་རླུང | སྐུ་དང་ཡེ་ཤེས་རབ་རླུང | PDF 2 / image 395 / printed 387, line 2 | Degé PDF 1 / image 647, line 3 has ཡེ་ཤེས་ཤེས་རབ | Tingkye has one ཤེས at this juncture; the base has two. Retain the base's repetition if its scan confirms it. Possible haplography is a hypothesis, not an established history of the variant. |
| U00023 | མི་ཕྱེད་སྣ་ཚོགས་དམིགས་མེད་པས | མི་ཕྱེད་སྣ་ཚོགས་དམིགས་མེད་པ | PDF 2 / image 395 / printed 387, line 2 | Degé PDF 1 / image 647, line 3 visibly has terminal པས | Tingkye lacks final ས. A diplomatic text retains the base's form; do not silently choose the variant that seems smoother. |
| U00027, terminal phrase only | ཡོངས་སུ་མེད | ཡོངས་མེད | PDF 2 / image 395 / printed 387, line 3 | Degé PDF 1 / image 647, line 4 has ཡོངས་སུ་མེད | Tingkye lacks སུ at this point. Retain the base phrase once the base scan is verified. No full-line exact transcription is offered here because the handwriting earlier in Tingkye's line is less certain. |

These are **five observed loci**, not a claim that the selected seventeen units contain only five variants.

## Other observations and uncertainties

1. Tingkye U00019 appears to have རིག་པ where the Adzom e-text has རིག་པས. The local shapes are readable but the joining strokes merit a second independent paleographic check before this becomes a resolved apparatus entry. Do not treat it as established from this note alone.
2. Tingkye U00018's final གཞལ་མེད་ཁང is tightly written. **Do not report an omission of ཁང**: an initial low-scale impression of absence was not secure under enlargement. This locus remains unreported here.
3. Tingkye U00026's ད་ལྟ(ར) needs a second reading; do not claim omission of final ར from this inspection.
4. Tingkye U00012's verb in the standard opening formula needs a second reading. Familiarity with the formula is not adequate evidence to supply it.
5. The two Adzom e-text section labels at U00011 and U00029 must be distinguished from root main text and any interlinear or marginal material. This sample does not establish their complete presence/absence or textual status in the two comparison witnesses.
6. Sanskrit title spellings, ornate initial marks, terminal punctuation, and line-break punctuation have not been transcribed exhaustively here.
7. U00015, U00016, U00017, U00020, U00021, U00024, U00025 and U00028 were used as alignment anchors. They are not certified as exact all-character agreements by this limited note.

## Practical collation rule established by this sample

Use the Adzom scan as the controlling witness if the project remains diplomatic. Record each comparison witness's exact confidently read form and physical locator; mark illegibility or uncertainty without filling it from a familiar formula. Distinguish an e-text correction (e-text versus its own scan) from an actual witness variant (one scan versus another). A chapter is not complete until its entire base text and every witness included in its declared scope have been collated, with limitations stated explicitly. These opening observations cannot meet that completion gate by themselves.

## Follow-up: continuous Degé collation capability test

The requested chapter-1 boundary was checked against the actual source-unit data. It is **U02635**, offsets **76303–76376**, ending:

> སྣ་ཚོགས་བཀོད་པ་རང་བྱུང་མན་ངག་གི་རྩ་་བ་ངེས་པར་འབྱུང་བའི་ལེའུ་སྟེ་དང་པོའོ།།

The doubled tsheg in རྩ་་བ is reproduced from the e-text here; it is not a scan-certified reading. The unit identifier and exact offsets above govern the electronic chapter boundary.

For a practical readability test, the PDF's underlying embedded images for **Degé PDF pages 1–2** were extracted directly (without rasterizing or rescaling) and viewed in three horizontal crops each. This is a read-only extraction of the stored source image. Page 1's original image is 3484×569 pixels for seven main text lines. I attempted to continue alignment through the remainder of page 1 and examine page 2 at that native image level.

**Result:** many main-line phrases are legible, and the five comparative loci above remain usable, but I cannot responsibly certify a continuous character-level transcription/collation from this test. In particular:

- On image 647, small interlinear material around main line 3 is significantly smaller than the main script; its precise wording, insertion point and textual status are unresolved in this inspection.
- On image 647, the glyph joining/suffix at the U00019 alignment remains less secure than the clear comparative loci above. It must not be supplied from the expected Adzom phrase.
- On image 648 / PDF page 2, the rightmost ends of multiple main lines are markedly faint. Enlarging them does not restore absent contrast/detail. No exact readings of these faint areas are certified here.
- The attempted continuation beyond U00028 has not produced a trustworthy all-unit transcript or a list of every difference. Therefore **the certified comparison scope has not been expanded beyond the five loci listed above**. Viewing a page is not equivalent to collating it.

This is an assessment of the reliability of this particular visual reading, **not** a claim that the facsimile is wholly illegible or that a qualified reader with independent verification could never collate it. A completion claim for chapter 1 across Degé would require a continuous checked transcript, explicit treatment of the small annotations, and an independent resolution or marked uncertainty at the faint loci. This note does not provide that result and must not be cited as if it does.
