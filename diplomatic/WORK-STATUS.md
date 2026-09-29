# Diplomatic edition — current work status

Updated 2026-09-29. **Chapter 1 is unfinished; Chapters 2–6 and the final colophon have not started.** Start at [HANDOFF.md](HANDOFF.md) for operational instructions and [WORK-QUEUE.json](WORK-QUEUE.json) for the next bounded task. This ledger records supported scholarly coverage and explicitly retained uncertainty; a saved inspection is not a whole-page collation.

Preserved pre-continuation edition baseline: `afb5c5133357942267dc55fc60a1d22704d5ef08`. Current [Chapter 1](chapter-01.md) SHA-256: `7579a1b5cdbfd4cf242db3ab50c351e556f29570d09f93a5d8f2c58f99f09356`. See [C1-SIGNS-01](reviews/chapter-01/continuation/C1-SIGNS-01.md) and the [C1-SIGNS-02 review](reviews/chapter-01/continuation/C1-SIGNS-02.md); these local punctuation changes do not complete the edition.

## What is already saved and integrated

- **2,635 base anchors**, **359 exact supplied-transcript differences in 183 loci**, and **273 Wikisource lexical comparison blocks**.
- **88 scan correction/source-layer/uncertainty records**, plus **13 restored main verses and one reply heading**.
- **493 comparison records**, including qualified observations and uncertainty: Degé 56, Dzongsar 49, Gadkar 6, Langtang 2, Tharpaling 4, Tharpaling 1983 W27491 12, Tingkye 215, Tsamdrak 149. These are not a count of confirmed variants or a coverage percentage.
- Adzom's continuous **main lexical** pass, its targeted annotation audit, and Dzongsar's continuous **main lexical** comparison survive. They should not be discarded or repeated wholesale.

Sources: [status](STATUS.json), [interventions](chapter-01.md#scan-interventions), [comparison records](collation/chapter-01/scan-comparison-loci.json), [base coverage](collation/chapter-01/scan-coverage.json).

## Saved coverage and unfinished work

PDF numbers refer to the named witness; provider-container numbers apply to Adzom1973 and Gcn. An inspected page is not automatically a collated page.

| Witness | Saved, reviewable coverage | Still required |
|---|---|---|
| Adzom base | Main sequence U00007–U02635: [opening/boundary](collation/chapter-01/opening-boundary-review.json), [PDF5–50](collation/chapter-01/continuous-early.json), [PDF51–101](collation/chapter-01/continuous-late.json); [41 annotation records](collation/chapter-01/annotation-audit.json); [five first-batch main-terminal dispositions](reviews/chapter-01/continuation/C1-SIGNS-01.md); [five further sign corrections](reviews/chapter-01/continuation/C1-SIGNS-02.md). | Whole PDF1–102 physical signs/source layers; U01239 blocked; U01557 initial heading letters separately uncertain; U02489 small-heading terminal on PDF97 row1; U01286 exact note letters/signs (source-note separation integrated; S02–S07 terminal corrections integrated; qualified S02-L3 dot retained); title/portrait. Keep U01522/U02615/U02620/S09 unresolved unless evidence resolves them. |
| Dzongsar | Main lexical PDF2–121 through U02635: [opening](collation/chapter-01/dzongsar-collation.json), [middle](collation/chapter-01/dzongsar-middle.json), [late](collation/chapter-01/dzongsar-late.json). | Listed local uncertainties; exact signs, annotations, Sanskrit/foreign stacks. No full diplomatic certification. |
| Tingkye | [Opening PDF1–2](collation/chapter-01/tingkye-collation.json), [PDF35–39](collation/chapter-01/tingkye-root.json), [three junction checks at6/27/32](reviews/chapter-01/tingkye-recovery-review-20260927.md); endpoint69. | Continuous3–34/40–69 lacks complete integrated ledgers. Review archived61–69 fragments before rereading; opening/35–39 remain partial. |
| Tsamdrak | [Attempted PDF1–13 through U00349; endpoint83 row6](collation/chapter-01/tsamdrak-collation.json). | Resolve unreliable opening suffix/stack readings; PDF14–83 continuous collation. Later middle/late reports survive only as summaries. |
| Tharpaling | [Opening1–3](collation/chapter-01/tharpaling-collation.json); retained44–51 fragments and [partial52–56](collation/chapter-01/recovered-tharpaling.json); [57–71 traversal](reviews/chapter-01/tharpaling-continuation-review-20260927.md), zero pages fully collated. | Missing4–43 ledger; verify retained44–51; complete52–71 where readable. Three old omission claims are withdrawn. Latest boundary review places PDF56 end at U02100, superseding U02093. |
| Degé | [Opening1–2](collation/chapter-01/second-dege-tingkye.json); [endpoint54 row3](collation/chapter-01/dege-boundary.json). | Continuous3–54; exact opening/faint endings/interlinear readings. Later continuation/late/final bodies incomplete. |
| Gadkar | [PDF1–11 locator sequence and endpoint91 row4](collation/chapter-01/gadkar-ch1.json). | Reliable exact opening discrimination and continuous12–91; locator recognition is not agreement. |
| Zhichen | [Opening1–3 attempt and boundary searches](collation/chapter-01/zhichen-ch1.json). | Establish Chapter1 endpoint and reliable continuous reading. No certified lexical range. |
| W1ER119 | [17 inspections and16 numerical manifest discontinuities](collation/chapter-01/w1er119-ch1.json). | Establish endpoint, actual gap effects, continuous reading. Replayed import audit does not supply a missing collation. |
| Langtang | [Opening continuity across provider images3→6](reviews/chapter-01/langtang-opening-gap.md). | Recheck historical PDF104 endpoint; recover or rebuild continuous ledger and later gap effects. Summary counts do not certify coverage. |
| Adzom1973 | [Boundary mapping](reviews/chapter-01/container-mapping-recovery-20260927.md): root11–215; Chapter1 ends112. | Internal-exposure accounting and continuous11–112 comparison. |
| Gcn | [Boundary mapping](reviews/chapter-01/container-mapping-recovery-20260927.md): title407, incipit408, Chapter1 ends484 row4. | Continuous comparison and composite-exposure accounting; middle fragments/late failed-attempt replay are not complete collation. |
| Sichuan / Wikisource | [Exact transcript apparatus](collation/chapter-01/chapter1-conflicts.json) / [Wikisource comparison](reviews/chapter-01/wikisource.md). | Sichuan full print unavailable; Wikisource is a reference transcription. Neither comparison certifies unseen printed glyphs. |

## Recovery is separate from completion

All preserved archives are now on `main`, indexed in [recovery/README.md](recovery/README.md). Historical recovery branches remain available but are not continuation branches.

The [54-file recovery matrix](recovery/2026-09-27-task-records/missing-report-recovery-matrix.md) tracks missing historical report files, often JSON/Markdown pairs—not 54 independent research passes. **Four complete report bodies were replayed from retained transcript sources; 50 remain incomplete.** Partial bodies, failed-save commands, summaries and withdrawals remain useful evidence, but are not completed witness coverage. Historical 1,016/1,024-observation claims must not replace the saved 123-record apparatus.

Usable sources remain: ten mapped facsimile assemblies, acquisition manifests/archives, three supplied transcript families, provider containers and retained evidence crops; see [source inventory](SOURCES.md). Some large files require Git LFS materialization. Sichuan full scans and catalogue-only Paltség/CTRC/Gangteng leads remain unavailable in the acquired holdings. Missing reports do not mean these other source scans vanished.

## Completion gate and next bounded work

The saved [validation record](VALIDATION.json) reports passing reconstruction, source accounting, links and listed-hash checks. It explicitly says `chapter_complete: false`; it cannot detect unseen manuscript variants.

The [earlier sign audit](reviews/chapter-01/sign-adoption-audit-20260927.md) records ten independently reverified targets: nine added interventions and one revised intervention. The new [C1-SIGNS-01 report](reviews/chapter-01/continuation/C1-SIGNS-01.md) disposes five more main-terminal candidates: U02090 retained; U02172/U02183/U02484 corrected by three new records; U02489 corrected in its existing layer record. The independent review and its explicit boundary-inventory clarification preserve every detached mark without confusing terminal/opening ownership. **U01239 remains blocked. The U01557 terminal correction is remotely verified; systematic proofreading remains.** The small U02489 heading terminal is separately unresolved, with exact bounds and a next step in C1-BASE-PHYSICAL. The [readiness audit](reviews/chapter-01/readiness-audit-20260927.json) retains its historical candidate identities; current dispositions are in [WORK-QUEUE.json](WORK-QUEUE.json), not inferred from old counts.

C1-SIGNS-02 adds five two-shad corrections at U00995/U01094/U01270/U01416/U01534. U00995's initial 2-versus-3 disagreement is preserved with the same-reader structural adjudication: the extra counted stroke belongs to final pa. **Next base-uncertainty work is S09/PDF102, retaining the completed bounded PDF60/PDF101 reviews; U01286 remains precisely blocked for note letters/signs. U01239 remains precisely blocked after its restart review.** Continue bounded candidate reviews, resolve or precisely bound remaining base uncertainties, then fill witness gaps using retained ledgers first. Commit and verify every substantive batch remotely. Complete Chapter1's declared coverage and apparatus before starting Chapter2.

### Current continuation wave

C1-SIGNS-03 through C1-SIGNS-06 contribute eighteen supported boundary corrections. All twenty candidate identities and raw independent reports are retained. **U01239** has unresolved final-heading letter segmentation; its recovered and fresh follow-ups now establish two detached boundary marks and exact correspondence; **U01557** has a faint heading opening. Its recovered follow-up establishes boundary correspondence while keeping the opening letters unresolved. U01239 retains its source scaffold with a new visible uncertainty marker. U01557 now has its verified second terminal shad, while its faint initial letters remain visibly uncertain and explicitly assigned to C1-BASE-PHYSICAL. Their exact source evidence and next steps are in [C1-SIGNS-04](reviews/chapter-01/continuation/C1-SIGNS-04.md) and [C1-SIGNS-05](reviews/chapter-01/continuation/C1-SIGNS-05.md). No new page is declared fully collated.

The [interruption audit](reviews/chapter-01/continuation/INTERRUPTION-20260928/README.md) preserves the two previously unpublished follow-ups, their raw logs and selected surviving coordinator drafts. Completed C1-SIGNS-03/C1-SIGNS-06 receipt labels are reconciled to their verified integration commit; these are not new readings.

The current follow-up adds one terminal correction (U01557) and one uncertainty-only note (U01239). No lexical source string is changed; an uncertainty-only note must not be counted as an adopted glyph reading.

The [verified follow-up receipt](reviews/chapter-01/continuation/C1-SIGNS-05-restart-publication.json) records 29 completed terminal-sign candidates and one blocked candidate. Separately carried heading-letter uncertainty is not counted as a resolved lexical reading.

The [base-layer continuation](reviews/chapter-01/continuation/C1-BASE-LAYERS.md) integrates six second-shad restorations in S02/S03, without changing lexical readings or the 13 restored-verse count. PDF73/74/78 are local correspondence sources, not newly certified whole-page coverage.

The B02 continuation adds five further shads in S04–S07: inventories 1/2/2/2/2, without lexical, tsheg, insertion-order or verse-count changes. U01286 remains the last target in C1-BASE-LAYERS; no complete page or witness is certified by these local corrections.

U01286 is now removed from the main-verse sequence and preserved as a separate source annotation, with its exact supplied string quoted unchanged. Independent layout correspondence is strong, but complete printed note letters and terminal signs are unresolved; this is a source-layer correction, not a new lexical transcription or an omitted-verse restoration. See [B03](reviews/chapter-01/continuation/C1-BASE-LAYERS.md#batch-b03--u01286-source-note-layer).

### Bounded continuation readings — Wave001

Tingkye PDF3 rows1–7 and PDF4 rows1–3 now have a partial comparison ledger with explicit glyph/sign limits, plus a separate PDF6 U00180–U00184 check. Twenty-five localized or uncertain observations are integrated; the old no-nas withdrawal is rechecked without duplication. The next continuous span is PDF4 row4, U00106 continuation. PDF5/7 remain unread in that packet. [Report](reviews/chapter-01/continuation/C1-TINGKYE.md).

The Tsamdrak opening test resolves U00030’s verb locally as thos, retains U00012 bstan/bstun uncertainty, and records a qualified rtog-versus-rtogs observation at U00148. The old U00143 transposition is reaffirmed. These tests are not three fully collated pages. [Report](reviews/chapter-01/continuation/C1-TSAMDRAK.md).

U01522’s extra middle components and separate right segment are more precisely inventoried but remain unresolved; no Adzom word was changed. Adzom physical PDF1–5 has a partial row/region ledger with13 boundary assessments, not five completed pages. [Uncertainty review](reviews/chapter-01/continuation/C1-BASE-UNCERTAINTIES.md) and [physical review](reviews/chapter-01/continuation/C1-BASE-PHYSICAL.md).

### Continued single-page reviews — second session wave

Tingkye PDF4 rows4–7 now joins the preceding row ledger and continues through U00127 at the page turn. Its next full comparison starts PDF5 row1. Sixteen further local or uncertain records preserve the actual signs and lexical differences; earlier PDF6 observations still do not move the continuous frontier. Tsamdrak PDF14 has all seven rows transcribed with bounded doubts and fourteen new local/uncertain records; next is PDF15.

Adzom PDF3 now has a source-ordered four-row physical inventory, all twelve boundaries and marginal regions inspected. U00014 ends with a tiered graph plus a detached shad; exact encoding remains unresolved, and the unchanged transcript scaffold is visibly qualified. Marginal components are read in physical order as ka / sgra / gnyis / thal-gyur, not merged into main text. PDF101 all-row note search leaves U02615 wording and the dense U02620 candidate locus unverified; the same ink is not allocated twice. These reviews add no base lexical substitution and do not complete Chapter1.

### Reconnected integration — 29 September 2026

The saved S09 boundary review is integrated with its erroneous raw following-incipit identification rejected. S09 remains unread, and no Tibetan wording or source string changed. Continue its exact unresolved questions alongside title/portrait work. The earlier eight and later twenty-one saved page reports remain the integration priority; do not commission duplicate replacement readings.

Adzom PDF4–7 preserved physical reviews are integrated with their exact remaining questions. Page7 retains all existing shads: the rejected raw proposal would have removed22 detached components. Two new uncertainty-only records visibly qualify seven anchors; no Tibetan reading string changed. U00045 retains its no-added-dot spelling; an erroneous supplemental gcig label is not adopted. Earlier pending comparison reports at Tingkye5, Tsamdrak15 and Dege3 remain the next integration priority.

Tingkye PDF5/B03 is integrated: seven rows through the U00162 page exit, with18 new bounded/qualified observations. Incoming U00127 is updated in its existing entry as gNang; prior uncertainty remains in its history. U00143 follows U00147 in this source. Next is the already preserved PDF6 report, not a fresh repeat.

Tsamdrak PDF15/B03 is integrated through U00418 with13 local/source-layer/uncertain apparatus entries. The seven-row ledger retains Q01–Q09; local absence of heading U00394 is not a lost main verse. Next is the already preserved PDF16 report.

Degé PDF3/B01 is integrated as a seven-row source-ordered attempt with15 explicit bounded lexical uncertainties, not15 accepted variants. No base wording changed. All eight earlier saved reports are now integrated; the21 already preserved next-page outputs remain the priority.

Tingkye PDF6–10 are now integrated from their preserved seven-row reports:35 target rows,79 new scoped or uncertain observations, and three earlier junction records rechecked without duplication. U00199/U00200 source order has one shared record across the page turn; U00272 context is not double-counted. U00181 medial wording remains qualified with the earlier snang-bai proposal preserved alongside the later unresolved reading. U00308 kye repetition is unresolved, not an omission. Next new Tingkye page is PDF11, U00348 continuation.

Tsamdrak PDF16–20 reports are integrated:35 target rows and68 scoped or uncertain findings. The source has an additional main verse between U00432/U00433 across PDF16 rows3–4, recorded only as Tsamdrak evidence. Detached small graphics on the later pages retain unclassified values rather than reconstructed heading text. Next new Tsamdrak page is PDF21, U00581 continuation. Adzom reading strings, source annotations and13 restorations are unchanged.

Degé PDF4–8 reports are integrated:35 target rows and28 scoped source-layer/graphic/uncertainty observations, not28 definite lexical variants. Compact notes are kept at their actual physical positions; their unresolved words are not borrowed from Adzom. Next new Degé page is PDF9 at U00390 continuation. All base reading strings, prior interventions and13restored verses remain unchanged. Of the21recovered later reports,15comparison-page reports are integrated;6Adzom physical reports remain.

Tingkye PDF11–13 is now integrated: 21 target rows, 41 selected local observations and six additional bounded lexical questions. The interrupted claim at 5f274c9 was verified before resuming. Next continuous Tingkye comparison is PDF14/U00464; this does not settle the retained page-specific glyph and graphic questions.

Tsamdrak PDF21–23 is integrated through U00681: 21 source rows, 27 selected localized observations and three separately indexed lexical questions. All nine nested page23 findings are preserved, including the unchanged repetition. The original malformed JSON remains intact alongside its exact mechanical sidecar. Next is PDF24/U00682; no Adzom reading or insertion changed.

Degé PDF9–11 is integrated: 21 target rows from U00390 continuation through U00539 opening, with thirteen source-layer/graphic/uncertainty records and all eighteen bounded questions retained. The next continuous reading is PDF12/U00539 continuation. Reply-label ordinals and small-note wording are not supplied from Adzom; all base reading strings and restored material remain unchanged.

The three targeted Dzongsar reviews are integrated as extensions of existing U00440/U00534/U00710 records, with no duplicate apparatus entries. Exact abrasion, first small syllable and annotation-role uncertainties remain visible; the prior record text is retained in history. All four completed new-reading reports are now integrated. The six saved Adzom physical reports PDF8–13 are next.

The interrupted Adzom PDF8–10 disposition draft is preserved on main at d46ce1579d962c9af78b220534b59bf8942b02c2. The three associated physical reports are now integrated: eighteen target rows, all original sign and source-layer inventories, and all bounded unresolved components. No canonical Tibetan, punctuation or insertion string changed. U00156 terminal-count and U00179/U00184/U00197 lexical/layer proposals remain explicitly pending rather than silently adopted or treated as agreement. The remaining preserved-report integration is Adzom PDF11–13. See [continued integration](reviews/chapter-01/continuation/SESSION-20260929-INTEGRATION-CONTINUED/README.md).

Adzom PDF11–13 is now integrated: eighteen physical rows, seventy-five boundary intervals, the physically interleaved PDF13 note and all exact unresolved components. Every one of the six saved Adzom physical reports is integrated, so the prior report backlog is cleared. No source, reading, insertion, intervention or comparison string changed in these six integrations. Next new base physical page is PDF14/U00277; title/portrait and the per-page component questions remain unfinished.

Langtang Chapter1 endpoint is now freshly established at PDF104/provider111 row2, with its medial colophon Q01 unresolved. The three-triangle boundary graphic and following incipit crossing rows2–3 are recorded separately. This does not supply the missing continuous collation; subsequent-chapter content remains excluded. See [Langtang continuation](reviews/chapter-01/continuation/C1-LANGTANG.md).

Adzom PDF14–16: eighteen source-ordered physical rows, margins, fillers and interleaved notes integrated from the preserved report; fourteen bounded questions remain. O15-3/O16-3 remain pending sign-adoption candidates; no canonical text changed.
