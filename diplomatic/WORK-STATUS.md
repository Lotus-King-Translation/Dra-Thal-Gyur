# Diplomatic edition — current work status

Updated 2026-09-28. **Chapter 1 is unfinished; Chapters 2–6 and the final colophon have not started.** Start at [HANDOFF.md](HANDOFF.md) for operational instructions and [WORK-QUEUE.json](WORK-QUEUE.json) for the next bounded task. This ledger records supported scholarly coverage and explicitly retained uncertainty; a saved inspection is not a whole-page collation.

Preserved pre-continuation edition baseline: `afb5c5133357942267dc55fc60a1d22704d5ef08`. Current [Chapter 1](chapter-01.md) SHA-256: `ead8cf12c9d51b988be465baccede0503670c2c5a719bd90abb506957c762f7f`. See [C1-SIGNS-01](reviews/chapter-01/continuation/C1-SIGNS-01.md) and the [C1-SIGNS-02 review](reviews/chapter-01/continuation/C1-SIGNS-02.md); these local punctuation changes do not complete the edition.

## What is already saved and integrated

- **2,635 base anchors**, **359 exact supplied-transcript differences in 183 loci**, and **273 Wikisource lexical comparison blocks**.
- **82 scan correction/source-layer records**, plus **13 restored main verses and one reply heading**.
- **123 comparison records**, including candidates and uncertainty: Dzongsar 49, Tingkye 30, Tsamdrak 22, Tharpaling 16, Gadkar 6. These are observations, not 123 confirmed variants or a coverage percentage.
- Adzom's continuous **main lexical** pass, its targeted annotation audit, and Dzongsar's continuous **main lexical** comparison survive. They should not be discarded or repeated wholesale.

Sources: [status](STATUS.json), [interventions](chapter-01.md#scan-interventions), [comparison records](collation/chapter-01/scan-comparison-loci.json), [base coverage](collation/chapter-01/scan-coverage.json).

## Saved coverage and unfinished work

PDF numbers refer to the named witness; provider-container numbers apply to Adzom1973 and Gcn. An inspected page is not automatically a collated page.

| Witness | Saved, reviewable coverage | Still required |
|---|---|---|
| Adzom base | Main sequence U00007–U02635: [opening/boundary](collation/chapter-01/opening-boundary-review.json), [PDF5–50](collation/chapter-01/continuous-early.json), [PDF51–101](collation/chapter-01/continuous-late.json); [41 annotation records](collation/chapter-01/annotation-audit.json); [five first-batch main-terminal dispositions](reviews/chapter-01/continuation/C1-SIGNS-01.md); [five further sign corrections](reviews/chapter-01/continuation/C1-SIGNS-02.md). | Whole PDF1–102 physical signs/source layers; 2 blocked candidates (U01239/U01557); U02489 small-heading terminal on PDF97 row1; insertion signs S02–S07/U01286; title/portrait. Keep U01522/U02615/U02620/S09 unresolved unless evidence resolves them. |
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

The [earlier sign audit](reviews/chapter-01/sign-adoption-audit-20260927.md) records ten independently reverified targets: nine added interventions and one revised intervention. The new [C1-SIGNS-01 report](reviews/chapter-01/continuation/C1-SIGNS-01.md) disposes five more main-terminal candidates: U02090 retained; U02172/U02183/U02484 corrected by three new records; U02489 corrected in its existing layer record. The independent review and its explicit boundary-inventory clarification preserve every detached mark without confusing terminal/opening ownership. **Two queued candidates (U01239/U01557) and systematic proofreading remain.** The small U02489 heading terminal is separately unresolved, with exact bounds and a next step in C1-BASE-PHYSICAL. The [readiness audit](reviews/chapter-01/readiness-audit-20260927.json) retains its historical candidate identities; current dispositions are in [WORK-QUEUE.json](WORK-QUEUE.json), not inferred from old counts.

C1-SIGNS-02 adds five two-shad corrections at U00995/U01094/U01270/U01416/U01534. U00995's initial 2-versus-3 disagreement is preserved with the same-reader structural adjudication: the extra counted stroke belongs to final pa. **Next is the preserved U01239 follow-up in C1-SIGNS-04, then U01557 in C1-SIGNS-05.** Continue bounded candidate reviews, resolve or precisely bound remaining base uncertainties, then fill witness gaps using retained ledgers first. Commit and verify every substantive batch remotely. Complete Chapter1's declared coverage and apparatus before starting Chapter2.

### Current continuation wave

C1-SIGNS-03 through C1-SIGNS-06 contribute eighteen supported boundary corrections. All twenty candidate identities and raw independent reports are retained. **U01239** has unresolved final-heading glyph/stroke segmentation; **U01557** has a faint heading opening. Its recovered follow-up establishes boundary correspondence while keeping the opening letters unresolved. Neither blocked candidate has been changed. Their exact source evidence and next steps are in [C1-SIGNS-04](reviews/chapter-01/continuation/C1-SIGNS-04.md) and [C1-SIGNS-05](reviews/chapter-01/continuation/C1-SIGNS-05.md). No new page is declared fully collated.

The [interruption audit](reviews/chapter-01/continuation/INTERRUPTION-20260928/README.md) preserves the two previously unpublished follow-ups, their raw logs and selected surviving coordinator drafts. Completed C1-SIGNS-03/C1-SIGNS-06 receipt labels are reconciled to their verified integration commit; these are not new readings.
