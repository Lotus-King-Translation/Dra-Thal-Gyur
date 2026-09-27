# Chapter 1 supplied e-text collation

Scope: opening through the first chapter colophon, including witness-specific material before the identical next-chapter incipit. No text from the next chapter was collated or prepared.

This is a lossless comparison of supplied e-text extractions. It does **not** certify what the printed witnesses read. No source file was changed, normalized, harmonized, or corrected.

## Files and stable schema

- `collate_chapter1.py`: standard-library-only portable producer. Run `python collate_chapter1.py --repo /path/to/repository --out /path/to/output`.
- `chapter1-summary.json`: file/chapter checksums, ranges, method, counts and reconstruction result.
- `chapter1-conflicts.json`: 359 exact minimal Unicode difference groups. Each record includes `id`, `source_units`, `offsets`, `readings`, classification, context, review flags and status.
- `chapter1-loci.json`: 183 readable loci enclosing the same differences in complete Adzom source units. Each record includes `id`, `source_units`, `exact_conflicts`, `offsets`, `readings`, and status. Use this layer in a human apparatus: it avoids isolated combining marks and reunites adjacent split differences, including identically omitted verses in B/S aligned on different shads.
- `chapter1-pairwise.json`: full exact equality/difference opcode streams for A:B and A:S.
- `chapter1-A.txt`, `chapter1-B.txt`, `chapter1-S.txt` (reproducible producer outputs, not duplicated in this tracked dossier): exact UTF-8 chapter slices.

All offsets are zero-based, half-open Unicode code-point offsets in the full supplied e-text extraction. Ranges: A `[0,76376)`, B `[0,76794)`, S `[0,76999)`. A corresponds exactly to source units U00001–U02635. A/B/S represent the Adzom W1KG11703, Tharpaling W27491 and Sichuan W3CN7084 supplied e-texts, respectively.

## Validation and limits

The producer checks exact concatenation of the Adzom source units, exact partition of both pairwise input streams, equality of all unchanged intervals, and independent reconstruction of B and S from A with either the minimal conflict records or the readable loci. All checks passed. These tests establish no dropped characters; they do not establish print authenticity or an optimal philological alignment.

The 359 raw groups comprise 99 groups containing Tibetan textual differences, 49 punctuation/spacing groups, and 211 editorial-bracket/spacing groups. These are computational groups, not a count of independent historical variants. They touch 289 Adzom source units. Pairwise counts are 142 non-equal A:B operations and 286 non-equal A:S operations.

Alignment uses unique exact 32-code-point anchors selected in monotonic order by longest increasing subsequence, followed by exact `SequenceMatcher(autojunk=False)` comparisons of the gaps. The human loci reunite changes at the level of complete source units. Displaced headings and marginal material may appear as separate insertion/deletion loci: do not infer independent additions and omissions without viewing the page layout.

## Highest-priority review loci

| Locus | Source unit(s) | Evidence and required review |
| --- | --- | --- |
| L1-0001 | U00001–U00006 | Opening title and Sanskrit material differ substantially; A has prefatory material absent in B/S. B also begins with LF. Title-page versus body-text layout should govern interpretation. |
| L1-0002 / L1-0003 | U00010–U00012 / U00017 | A/S place the uncommon introduction heading before the opening formula. B places a different version inside the wind-mind line. A `ཐོས་པའི` contrasts with B/S `བསྟན་པའི`. This is an actual lexical difference in the supplied strings, not merely punctuation. |
| L1-0004 | U00022 | A/S `ཤེས་རབ` versus B `ཤེས་རང`; possible letter/transcription error, not established until print check. |
| L1-0005 / L1-0006 | U00029 / U00035 | Common-introduction heading appears in a different position in B, inside a line. Likely a layout-order issue worth checking; not certified as such. |
| L1-0007 | U00039 | A `སྟོད` versus B/S `སྟོང`; lexical distinction requiring facsimile verification. |
| L1-0012 | U00164–U00166 | B reverses the order of two lines relative to A/S and has local spellings `ཡོད་ཏན` / `བསམ་པས`. The full-locus readings make the transposition visible. |
| L1-0013 / L1-0014 | U00180 / U00187 | S braces bracket material incorporated without markers in A; B omits some of that material. Treat as evidence for an apparatus/body-text distinction to inspect, not permission to silently remove A text. |
| L1-0019 / L1-0020 | U00272 / U00278–U00279 | Another heading-like passage is integrated into different positions in A/S versus B. The B insertion differs verbally and interrupts `དབང་པོ`. |
| L1-0056 | U00940 | A/S `སངས་རྒྱས་སྐུར་ཐིམ…ནས` versus B `སངས་རྒྱས་ཀུན་དུ་གནས`. A substantive phrase difference; it should not be dismissed as a minor spelling issue. |
| L1-0061 / L1-0062 | U01063 / U01067–U01068 | Numeral variant / bracketed annotation material. B has ten extra tshegs before an inserted phrase, an obvious transcription/layout anomaly candidate but still preserved exactly. |
| L1-0074 | U01246 | B inserts a long title/volume-label phrase within the 360-day numeral, between `དྲུག` and `ཅུར`. Probable running-header leakage is a hypothesis to verify against page layout, not an edition-level variant to accept automatically. |
| L1-0078 | U01274 | Three complete lines present in B/S but absent from the supplied A text. The readable locus shows B=S; raw groups C1-0153/C1-0154 align the addition on different shads. |
| L1-0112 | U01724 | A/S `ཡང་ན་སེམས་ཀྱི་བྱ་བའི་ལས` versus B `ཡང་མདོ་སྔགས་རིག་མཛོད་ལས`; substantive phrase difference with a possible marginal citation involved. No provenance conclusion is established by e-text alone. |
| L1-0121 / L1-0122 | U01804 / U01806–U01807 | Annotation-like `ལྟེབ་དང་…ཀྱང་བྱུང` appears at different positions; the first syllable of the second item also differs (`བཏུགས` / `གཏུགས`). |
| L1-0123 | U01811–U01812 | B repeats the same line twice; A/S differ in note placement and numeral-bearing material. Inspect line order and marginal additions before selecting a reading. |
| L1-0128 | U01882 | Three complete lines present in B/S but absent from the supplied A text. |
| L1-0134 | U02005 | Three complete lines present in B/S but absent from the supplied A text. Raw groups C1-0268/C1-0269 split these on a shad; readable locus correctly shows B=S. |
| L1-0145 | U02187 | Two complete lines present in B/S but absent from supplied A. Raw groups C1-0286/C1-0287 split these on a shad; readable locus shows B=S. |
| L1-0155 | U02308 | Two lines and the answer-57 heading are present in B/S but absent from supplied A. B/S differ in heading punctuation/braces. |
| L1-0169 | U02489–U02490 | A joins a genitive ending to the answer-67 heading; B/S close the sentence with `པའོ`, and B lacks the heading at this position. Check print and marginal layout. |
| L1-0181 | U02615–U02616 | A lacks `དང` present in B/S; S brackets the preceding annotation-like expression. |
| L1-0183 | U02635 | A has doubled tsheg in `རྩ་་བ`; B/S single. B adds `བྷྲམྱ་ཏྲ་ཧྲ་ཏྱ། །ཉྲཿ །` after the colophon; S adds two spaces and double shad. Preserve these witness-specific closing strings. |

S contains 116 opening braces and 117 closing braces in this chapter. The unmatched closing brace at S offset 76203 (after the answer-76 heading, corresponding to U02611) is preserved; no balance repair was applied. Braces are supplied-text structural markers, not automatically evidence of printed punctuation. A and B contain no ASCII braces in this span.

No editorial reading has been adopted by this collation task. Apparatus decisions must distinguish (1) preservation of the selected base, (2) facsimile-confirmed transcription repair, and (3) conjectural or eclectic replacement. Agreement of B and S alone does not prove independence or authorize a silent repair.
