# Gcn late Chapter1: bounded attempted reading

**Continuous lexical collation was not achieved.** This report records attempted ranges, two secure repeated-image pairs, and a local Chapter1 boundary observation. It provides no whole-page or whole-range lexical agreement certificate.

Source: `Dra-Thal-Gyur/editions/gcn-manuscript/bdrc-W1ER128.pdf`; SHA256 `0e32b67b69e6bc57059993c511981154c15f5eeacad2217003f03bae124f0501`. Assigned PDF449–484, ending at row4 of484. No Chapter2 readings were collated.

## Method and limitation

Rendered the complete PDF page with PyMuPDF Matrix(1,1), alpha=False, producing the full MRC composite at 3000×811. The first embedded 999×270 background image alone is unsuitable for collation.
Compared opening and later local phrases against the corrected Chapter1 reading units and corrected-ch1-wylie.txt. Full-page images and overlapping 2× halves were inspected for PDF449–451, with narrower 2×/3× row and opening targets.
Compared PDF452/453 with450/451 visually to identify repeated exposures. PDF454 received only a full-page readability inspection. PDF484 upper four rows received full-page and narrower local inspection.
The cursive letter forms and faded/compressed strokes could not be discriminated reliably enough to certify consecutive complete readings. Isolated phrase alignment is explicitly not counted as lexical agreement. No inference of agreement, omission, or transposition is drawn from the uncollated ranges.
Image display, rendering, and a locator attempt are separately identified; rendering alone is not inspection. No Chapter2 readings were collated.

Full MRC composites are3000×811; native coordinates are used below. Overlapping half crops were [80,100,1610,690] and [1440,90,2870,690], displayed2×. Source first embedded backgrounds were not used alone. PDF-to-BDRC image mapping remains unestablished.

## Attempted coverage

| PDF page | Actual work | Anchor / limit |
|---|---|---|
| 449 | all seven rows viewed in overlapping halves; attempted phrase alignment, no consecutive exact comparison achieved | U01427 (disputed, unverified candidate); end not established |
| 450 | all seven rows viewed in overlapping halves; attempted phrase alignment, no consecutive exact comparison achieved | No secure start anchor; end not established |
| 451 | full page and overlapping halves viewed; concentrated locator attempt on row1, without consecutive exact comparison | U01511 (unverified candidate only); end not established |
| 452 | full-page structural comparison only; observed repeated exposure of450 | No secure start anchor; end not established |
| 453 | full-page structural comparison only; observed repeated exposure of451 | No secure start anchor; end not established |
| 454 | full-page readability assessment only; no reading-unit comparison | No secure start anchor; end not established |
| 484 | local boundary inspection and limited reading attempts; no continuous upper-four-row collation | U02617 (unverified candidate only); end U02635 |

PDF455–483 inclusive were not inspected. Rendering455/456 while preparing images does not count as inspection. All attempted pages retain unresolved main-text readings; annotations and exact punctuation are uncollated.

## Findings

### GCN-L-001: observed_structural_repeat

PDF 450, 452. The same manuscript side appears twice: matching seven-row text layout, left-edge smear, row7 pen strokes, and physical border damage. Tonal/background treatment differs.
Do not count the second exposure as an additional text passage or advance reading-unit numbering through it. This is a repeated image exposure, not an inferred scribal repetition.
Evidence bounds `[0, 0, 3000, 811]`; `p450.png`, `p452.png`.

### GCN-L-002: observed_structural_repeat

PDF 451, 453. The same manuscript side appears twice: matching opening ornament, small annotations, row7 left smear, seven-row text layout, and border contours. Tonal/background treatment differs.
Do not count the second exposure as an additional text passage.
Evidence bounds `[0, 0, 3000, 811]`; `p451.png`, `p453.png`.

### GCN-L-003: unresolved_reading

PDF 484, row2. The final particle at the end of the cho phrul phrase is not securely discriminated as du/gyis in this pass. Do not count agreement with the base or the Ts variant.

Evidence bounds `[1450, 225, 2800, 335]`; `p484-r2-right.png`, `p484-r2-left.png`.

### GCN-L-004: unresolved_reading

PDF 484, row4. The faint internal wording after sna tshogs bkod pa is not securely read; particularly rang byung presence/absence cannot be decided here. Do not import the Ts colophon omission into this witness.

Evidence bounds `[1150, 365, 2070, 433]`; `p484-colophon-center-3x.png`, `p484-colophon-left.png`.

### GCN-L-005: observed_local_boundary

PDF 484, row4. The separated final dang po'o is locally legible at the end of the Chapter1 colophon. This supports the row4 Chapter1 boundary already mapped by the parent. It does not certify the entire colophon or its exact punctuation.

Evidence bounds `[1880, 340, 2760, 434]`; `p484-colophon-end-3x.png`.

## Consequences

PDF450/452 and451/453 must be handled as repeated exposures rather than independent consecutive text. The proposed U1427 locator for449 is disputed and unverified against the sequential middle-reader PDF442 U951–988 endpoint; do not use it as alignment authority. The proposed U1511 locator for451/453 is also an unverified candidate and may share the same expected-text error. No new lexical variant is established here. The final dang po'o at484row4 supports the existing boundary but does not establish the full colophon wording.

A reader able to discriminate this cursive hand must collate the attempted ranges and PDF455–483. Retain this report as an attempted-coverage record, not a completed witness pass.

No repository files were changed.
