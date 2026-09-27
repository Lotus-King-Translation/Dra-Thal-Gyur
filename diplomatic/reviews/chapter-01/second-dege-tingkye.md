# Second visual reading: Degé and Tingkye, Chapter 1 opening

Date: 2026-09-27. Task: an independent second inspection of specifically uncertain opening loci. This report **does not certify a complete chapter or a continuous transcription of either witness**. It records only the evidence below. No repository file was changed by this reader.

## Procedure and evidence

The initial native Degé crops and Tingkye opening crops were inspected before reading the earlier `independent-openings.md` report or the Adzom unit strings. The earlier report and unit strings were then used to identify the requested locations; the decisions below were checked again in independently extracted native PDF images. Consequently this is a second visual reading, with an initial independent phase, not a claim that every later comparison was blind.

Native images were extracted with PyMuPDF from `editions/dege-W1ER7/sgra-thal-gyur.pdf` pages 1–2 and `editions/tingkye-1973/sgra-thal-gyur.pdf` pages 1–2. Originals were preserved. Cropping, enlargement, and green-channel autocontrast were inspection aids only. No letter restoration, interpolation claimed as new detail, or transcription from an expected formula was used.

Degé native page 1 is 3484 × 569; its extracted JPEG SHA-256 is `50a914969454ee35facff1492ad236e62cf90746f3dd8efd5cdccaba4674405f`, exactly matching the repository manifest for I1ER175 image 647. Page 2 is 3475 × 604; its extracted JPEG SHA-256 is `dfddf7198212ce836b28e5a849c9cf5dd24ee71907e3d2c18229e0d332075b1b`, exactly matching image 648.

Tingkye native embedded images are 4350 × 1100 pixels, 1-bit grayscale. They are PDF-extracted PNG serializations, not byte-identical copies of the manifest PNGs. Page 1 / I1765 image 394 visibly bears printed page 386; page 2 / image 395 bears printed page 387. The extracted PNG hashes are respectively `a30cd34e41334939480fd87f21e842236b62395eb55d224ec02ce56364973ba8` and `5fbfa53df39a1aff493e7d8eb329106055287fa1e1c4ec297fc191bb28ce3eb3`. An attempted comparison against `original-images.zip` could not run because that local file is not a materialized ZIP. No new pixel-equivalence claim is made.

All crop coordinates below are zero-based half-open `(left, top, right, bottom)` pixel boxes in these native images. The cited crops are preserved in [second-reading evidence](../../evidence/chapter-01/second-reading/). The [structured ledger](../../collation/chapter-01/second-dege-tingkye.json) provides exact locators.

## Results at requested loci

The Tibetan in the reading column is a lexical transcription of the cited span. It does **not** certify source tsheg spacing or an exact Unicode representation of Tingkye's multi-dot terminal mark. Certainty labels apply to the stated span, not the whole unit or page.

| Witness / anchor | Physical locator and crop | Second reading | Confidence and disposition |
| --- | --- | --- | --- |
| Tingkye U00018, final phrase | PDF 2 / I1765 image 395 / printed p. 387 / line 1. [ting-u18-terminal.png](../../evidence/chapter-01/second-reading/ting-u18-terminal.png), box `(2610,260,2870,385)`; surrounding [ting-387-line1.png](../../evidence/chapter-01/second-reading/ting-387-line1.png) | གཞལ་མེད་ཁང | High for retention of terminal ཁང. The close crop contains the terminal shape after མེད; it must not be registered as an omission of ཁང. The reading should be treated as a resolution of the previous *uncertainty*, not as a new variant. |
| Tingkye U00019 | PDF 2 / image 395 / p. 387 / line 1. [ting-u19.png](../../evidence/chapter-01/second-reading/ting-u19.png), box `(2820,275,3410,385)` | རང་བྱུང་རིག་པ་བཅོས་པ་མེད | High for རིག་པ without suffix ས. The pa is followed directly by the ba of བཅོས; the intervening sa visible in the Adzom transcript and Degé is absent here. Register the Tingkye lexical variant against Adzom's རིག་པས. |
| Tingkye U00026, temporal phrase | PDF 2 / image 395 / p. 387 / line 3. [ting-u26.png](../../evidence/chapter-01/second-reading/ting-u26.png), box `(570,425,1160,550)`; this crop begins in the preceding text and includes the requested phrase | མ་འོངས་ད་ལྟར་མེད | High for ད་ལྟར, including terminal ར. No omission of ར is supported. This resolves the previously open suffix reading in this span only. |
| Tingkye U00012, verb | PDF 1 / image 394 / p. 386 / line 7. [ting-u12-verb-full.png](../../evidence/chapter-01/second-reading/ting-u12-verb-full.png), box `(1880,744,2130,880)`; context [ting-386-line7.png](../../evidence/chapter-01/second-reading/ting-386-line7.png) | འདི་སྐད་བདག་གིས་⟦uncertain verb⟧་པའི་དུས་གཅིག་ན | Unresolved. Initial བ is visible; the following stack and lower hook cannot be assigned securely in this reading. A separate reader given only the crop suggested བསྟུན (moderate confidence), with བསྟན still possible, and explicitly declined to certify either. This candidate is a reading proposal, not an adopted witness text. Do not supply the familiar ཐོས from the base formula. |
| Degé U00019 | PDF 1 / I1ER175 image 647 / main line 3. [dege-u19-target.png](../../evidence/chapter-01/second-reading/dege-u19-target.png), box `(1140,197,1450,270)`, and its `-green.png` inspection variant | རང་བྱུང་རིག་པས་བཅོས་པ་མེད | High to moderate for the contested suffix: པས, not པ. A separate sa-shaped component follows pa before the ba of བཅོས in both the color image and contrast view. This supports the base transcript locally and does not justify filling adjacent small material. |

The five clear comparative loci in the earlier report were not exhaustively re-collated here. Their survival as prior findings is not a certification of all intervening letters or punctuation by this second report.

## Degé small material: still unresolved

On PDF 1 / image 647 / line 3, the compact material located approximately in native box `(690,198,1135,260)` remains insufficiently secure for an exact transcription. Evidence: [dege-compact-color.png](../../evidence/chapter-01/second-reading/dege-compact-color.png) and [dege-compact-green.png](../../evidence/chapter-01/second-reading/dege-compact-green.png); contextual strips [dege-1-line3-left-color.png](../../evidence/chapter-01/second-reading/dege-1-line3-left-color.png) and [dege-1-line3-middle-color.png](../../evidence/chapter-01/second-reading/dege-1-line3-middle-color.png).

It sits in the neighborhood of the main-line U00018–U00019 transition and is smaller and more crowded than the surrounding letters. This second reader cannot securely establish all its words, its attachment point, or whether all the compact writing is one added annotation rather than a compressed continuation of the line. Therefore this report does **not** label it a heading, correction, gloss, or omission. An accurate working record is `⟦compact written material unresolved; image 647, line 3, box 690,198–1135,260⟧`, outside the adopted main text until its relation to that text is established.

This is a positive uncertainty record after reinspection, not evidence that the writing is absent or necessarily unrecoverable by another qualified reader.

## Degé page 2 right ends: narrower uncertainty record

The rightmost parts of all seven lines on PDF 2 / image 648 were inspected in color and in green-channel autocontrast. Some surviving letters are readable, but this pass did not produce a secure continuous transcription or complete mapping to U identifiers. There is uneven contrast, especially near the right boundary. Neither enlargement nor contrast adjustment establishes letters where detail remains indeterminate.

Evidence crops [dege2-r1-color.png](../../evidence/chapter-01/second-reading/dege2-r1-color.png) through [dege2-r7-color.png](../../evidence/chapter-01/second-reading/dege2-r7-color.png), with matching `-green.png` files, all use x = 2650–3070. The respective y intervals are 77–159, 146–211, 200–265, 251–318, 306–372, 359–426, 412–479. The boxes intentionally include some adjacent-line context and are **not** asserted to isolate every line perfectly; main lines are counted from the top of the page's text frame.

The appropriate status remains `not continuously transcribed; exact span readings unresolved` for these right-end regions. This should not be generalized to the entire page, and it is not an assertion that every character inside each box is illegible. No complete-witness or all-conflicts claim can be inferred from this check.

## Editorial consequences

1. Tingkye U00019 can be upgraded from a tentative to a supported variant in the targeted apparatus, retaining Adzom's attested reading under the diplomatic-base policy and recording Tingkye's རིག་པ exactly.
2. Tingkye U00018 and U00026 should explicitly be protected against false omission reports: terminal ཁང and ར are present in the inspected spans.
3. Degé U00019 supports རིག་པས locally. Its small adjacent material and page 2 right ends remain open, with exact evidence boxes.
4. Tingkye U00012 must keep its uncertain verb visible. The agreement of two readers that it is unresolved is not an exact reading.
5. These focused results cannot satisfy the repository's chapter-completion gate: this report does not cover the whole Adzom base or a continuous full chapter of either comparison witness.
