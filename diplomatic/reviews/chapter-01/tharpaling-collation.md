# Tharpaling Chapter 1: collation attempt and capability obstacle

Date: 2026-09-27. **Continuous exact collation is not complete and cannot be certified by this reading.** This report records independently observed local readings, the physical chapter boundary, and a concrete obstruction encountered during the continuous attempt. No repository file or commit was changed.

## What was inspected

Native PDF images were extracted without changing originals. Tharpaling’s mapped facsimile has 147 pages, ordinarily 2198 × 454 pixels in 1-bit grayscale. Pages 1–3 were traversed row by row: the single title row, four rows on page 2, and six rows on page 3. Page 71 was separately inspected to establish the actual colophon boundary. Earlier exploratory page views used only to locate the boundary are not counted as collation.

OCR was used only as an approximate locator. Its output is visibly unreliable and is not treated as source evidence. Native originals, enlarged viewing crops, and provisional OCR locator output are separated in `tharpaling-ch1/`. Neither exact transcript reconstruction nor an OCR match is claimed to prove agreement with the print.

## Physical chapter boundary

Chapter 1’s closing colophon occurs on **mapped PDF page 71 / I4448 image 75 / main row 5**, corresponding to Adzom anchor U02635. Its lexical text reads:

> སྣ་ཚོགས་བཀོད་པ་རང་བྱུང་མན་ངག་གི་རྩ་བ་ངེས་པར་འབྱུང་བའི་ལེའུ་སྟེ་དང་པོའོ

The next chapter’s incipit, དེ་ནས་ལྷ་དབང་རྟོག་པ་མེད, starts farther right on that same row, after intervening material. Thus the boundary is observed in the physical witness rather than inferred only from the electronic transcript. This lexical quotation does not certify exact source shad or tsheg encoding. Evidence: [p071-colophon-precise.png](../../evidence/chapter-01/tharpaling/crops/p071-colophon-precise.png) and [p071-next-incipit.png](../../evidence/chapter-01/tharpaling/crops/p071-next-incipit.png); native colophon crop `(490,277,1205,329)`.

## Local findings

| Locator | Observed reading or layout | Consequence |
| --- | --- | --- |
| PDF1 / image5 / title row | Secure opening phrase རྫོགས་པ་ཆེན་པོ; title continuation remains partly unclear | The supplied B opening title does not reproduce this entire visible front title. Keep it as separate unresolved frontmatter; do not silently substitute B’s label. |
| PDF2 / image6 / row2 / U00012 | བསྟན | Supports B’s lexical variant against Adzom’s ཐོས. Retain Adzom under the diplomatic-base policy and record Tharpaling’s form. |
| PDF2 / image6 / row3 / U00017 neighborhood | Smaller writing occurs between the main-line དབུས་སུ and རླུང་སེམས | B linearizes a source annotation within the main verse. Separate its layer; its complete wording is not securely read here. |
| PDF2 / image6 / row4 / U00022 | ཤེས་རང | Confirms that B’s རང is locally supported by the print, rather than necessarily a transcription mistake for Adzom’s རབ. Record the witness variant and preserve the base reading. |

Native evidence crops and exact boxes for these findings are listed in [structured review](../../collation/chapter-01/tharpaling-collation.json).

## Concrete obstacle to continuous certification

On **PDF page 3 / image 7, left portions of rows 2–6**, heavy overinking, joined strokes, and broken letters prevent this reader from independently establishing full words continuously. The affected inspection region is native box **(175,150,850,375)**; [p003-obscuration.png](../../evidence/chapter-01/tharpaling/crops/p003-obscuration.png) preserves the evidence. Individual words and the broad sequence align with the supplied B transcript, but that is insufficient to certify all retained letters or enumerate all differences. Reading the expected B wording into these shapes would create a false agreement claim.

This is not an arbitrary stopping rule or a declaration that the complete witness is illegible. It is a concrete limit of this attempted reading. Another qualified Tibetan reader or better source evidence may resolve it. The adjacent small heading and damaged title also prevent a fully exact diplomatic account even before page3. **Pages4–70 remain not continuously collated**, and no uninspected span has been marked as agreement.

## Alternative source checked

To test whether the difficulty was caused by the assembled PDF, the public provider file at the exact repository-recorded URL was downloaded read-only to `provider-volume.pdf`. Its SHA-256 is `bb9637516e8018dde4cf0dfda51909ef15e359755179e55b0575c5cabd21804f`, matching the repository’s provider record.

Provider pages 5, 6, 7, and 75 visually match mapped root pages 1, 2, 3, and 71 respectively. The provider image dimensions are again 2198 × 454. Its rendering preserves the same obstructed shapes; it did not supply a clearer independent reading. Evidence is retained in [provider-p005.png](../../evidence/chapter-01/tharpaling/crops/provider-p005.png), [provider-p006.png](../../evidence/chapter-01/tharpaling/crops/provider-p006.png), [provider-p007.png](../../evidence/chapter-01/tharpaling/crops/provider-p007.png), and [provider-p075.png](../../evidence/chapter-01/tharpaling/crops/provider-p075.png). This verifies those four correspondences, not every page of the 666-page container.

The targeted readings and boundary may be integrated into a provisional dossier. They do not pass the chapter-completion gate or justify claiming every Tharpaling conflict has been annotated.

[Structured review and exact evidence paths](../../collation/chapter-01/tharpaling-collation.json). This is a review-time snapshot; the current Adzom main reading follows the separate scan interventions.
