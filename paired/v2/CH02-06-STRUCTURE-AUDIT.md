# Chapter 2–6 and closing structure audit

Provisional structural recommendation for issue #4; no source, translation,
terminology or canonical-pair edits. Input authorities are the exact commits
pinned in `paired/core.py`: golden `b83051912977268b97615bd382d82e51c3406d61`,
English `e24e97ddad9cefa339b5583a38389179dba7a365`; v1 membership is unchanged.

## Coverage and method

All 2,838 golden objects from U02636 through U05466, including the four restored
objects and three transition graphics, were inspected in released order using
an EWTS rendering of the pinned Tibetan as a reading aid. The Tibetan strings
were inspected directly for all non-main roles and every non-seven-token main
line; the complete native PDF205 image was inspected for closing structure.
The released English was consulted for existing pair membership and empty-layer
presentation, not as the authority for source form. This is structural review,
not new translation QC or full scan proofreading.

| Part | Golden objects | Existing v1 pairs | Pair range |
| --- | ---: | ---: | --- |
| Chapter 2 | 987 | 543 | DTG-001193–DTG-001735 |
| Chapter 3 | 685 | 354 | DTG-001736–DTG-002089 |
| Chapter 4 | 460 | 237 | DTG-002090–DTG-002326 |
| Chapter 5 | 436 | 211 | DTG-002327–DTG-002537 |
| Chapter 6 | 252 | 108 | DTG-002538–DTG-002645 |
| Closing | 18 | 15 | DTG-002646–DTG-002660 |

The 91 `source_heading` objects are passed to the separate heading-hierarchy
audit. The remaining recommendation is 2,711 verse objects in 1,349 v1 pairs
and 36 prose/display-body objects in 28 v1 pairs. No existing v1 pair in this
scope crosses a proposed format boundary; no split is required here.

## Verse determination

All 2,707 `main_text` objects and A2000-C03-S01, A2000-C04-S01,
A2000-C05-S01 and A2000-C06-S01 are verse. These continue the source's
line-by-line metrical instruction, question/reply and narrative sequences.
No non-metrical Sanskrit formula or prose narrative interruption occurs within
these main-text sequences. In particular, narrative openings and speech
introductions are verse, and ritual sounds embedded in lines remain verse.
The four restored objects preserve respectively 3, 3, 2 and 2 verse lines.

The mechanical token inventory located 187 main lines outside seven written
tsheg-delimited tokens; it did not determine form. Most shorter results reflect
contracted finals such as `pa'o` or Sanskrit compounds such as `tsit+ta` and
`pad+ma`. Longer lines remain within verse sequences: U02974, U03155,
U03159, U03309, U03380, U03399, U04526, U04970–U04973,
U04976–U04983, U05109–U05110, U05114–U05115, U05205,
U05248, U05269, U05272 and U05280. U04312 is a short source line,
not a prose interruption. None of these observations licenses metrical repair.

## Prose and body-display exceptions

| Objects | v1 pair(s) | Proposed form and source reason |
| --- | --- | --- |
| U03621–U03622 | DTG-001735 | prose: chapter-title and chapter-number colophon syntax |
| U04304–U04305 | DTG-002088 | prose: chapter-title and chapter-number colophon syntax |
| U04762–U04763 | DTG-002325 | prose: chapter-title and chapter-number colophon syntax |
| U05196–U05197 | DTG-002536 | prose: chapter-title and chapter-number colophon syntax |
| U05447–U05448 | DTG-002645 | prose: sixth-chapter title/number completion formula |
| U02680 | DTG-001225 | prose display: empty source-annotation anchor; seventeen-subdivision note remains in its endnote |
| U02885 | DTG-001331 | prose display: empty anchor; the long gloss remains separate from the root verse |
| U02888 | DTG-001333 | prose display: empty joined anchor; the main clause is already at U02887 |
| U02889 | DTG-001334 | prose display: empty source-note anchor; no second verse is supplied |
| U03147 | DTG-001465 | prose display: empty source-query anchor, not a root instruction |
| C3-TRANSITION, C4-TRANSITION, C5-TRANSITION | DTG-002089, DTG-002326, DTG-002537 | prose display: unresolved graphic markers, with empty Tibetan payloads |

`prose` on an empty layer is a reader-facing body style, not a claim that an
untranscribed graphic is linguistically prose. Preserve the empty strings,
roles, source-note links and disclosed English markers. Source annotation
wording must not be reinserted into the canonical root reading.

## Closing material: explicit determination

Recommend `prose` for each U05449–U05466 (DTG-002646–DTG-002660):
U05449–U05451 form one work-title/completion sentence; U05452–U05454 and
U05464 are repeated seals; U05455–U05456 form a recipient-restriction clause;
U05457, U05461 and U05462 are invocatory/entrustment and warning clauses;
U05458–U05460 and U05463 are ritual formulas; U05465 is a text-family notice;
U05466 is the triple auspicious formula. Preserve all 18 anchors and their roles.

U05461, `དཔལ་ལྡན་མགོན་པོ་ནག་པོ་ཁྱོད་ལ་གཏད།`, has nine syllables;
U05465, `ཐལ་འགྱུར་རྒྱུད་ལ་མ་བུ་བདུན།།`, has seven. These counts alone
are insufficient to promote either isolated clause into a verse passage.
The native closing runs through unequal-length restriction, invocation,
warning, seal and bibliographic clauses without a recovered stanza structure.
In particular, the neighboring invocations U05457 and U05462 have different
lengths and syntactic functions. This prose choice is editorial and moderately
confident; a future source-supported identification of a verse invocation could
justify revising the structural decision in a later paired edition. It does not
alter the wording or assert that all protector invocations are generally prose.

## Evidence and limits

Consulted `paired/v2/PLAN.md`, the fixed template FORMAT/AGENTS copies,
`paired/README.md`, `paired/MIGRATION.md`, the pinned `reading.json` and
English `edition.json`; Chapter 2 layer decisions and the corresponding
SOURCE-ANNOTATIONS records; Chapter 6 DECISIONS (`C6-END`,
`C6-CLOSING-TITLE`, `C6-CLOSING-SEALS`, `C6-CLOSING-INVOCATION`,
`C6-CLOSING-TAIL`, all 18 `closing_units`) and FINAL-REVIEW.
Direct image evidence: `diplomatic/chapter-06-v1/evidence/E02/p205-native.png`.
The inherited exact-sign, ritual-reading and annotation-attachment uncertainties
remain; none is silently resolved by a display format. No glossary mapping is
introduced, and no independent semantic clearance is claimed.
