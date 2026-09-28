# Diplomatic edition — current work status

Updated 2026-09-28. **Chapter 1 is unfinished; Chapters 2–6 and the final colophon have not started.** This is the entry point for deciding what remains. It records saved evidence, not new manuscript readings.

Edition baseline: `afb5c5133357942267dc55fc60a1d22704d5ef08`. [Chapter 1](chapter-01.md) SHA-256: `927d6b36c7d105efa2857ef5f2392fcf5f2f6b54f287f6c8139d43663fe51c40`. Later recovery commits preserve records without completing the edition.

## What is already saved and integrated

- **2,635 base anchors**, **359 exact supplied-transcript differences in 183 loci**, and **273 Wikisource lexical comparison blocks**.
- **56 scan correction/source-layer records**, plus **13 restored main verses and one reply heading**.
- **123 comparison records**, including candidates and uncertainty: Dzongsar 49, Tingkye 30, Tsamdrak 22, Tharpaling 16, Gadkar 6. These are observations, not 123 confirmed variants or a coverage percentage.
- Adzom's continuous **main lexical** pass, its targeted annotation audit, and Dzongsar's continuous **main lexical** comparison survive. They should not be discarded or repeated wholesale.

Sources: [status](STATUS.json), [interventions](chapter-01.md#scan-interventions), [comparison records](collation/chapter-01/scan-comparison-loci.json), [base coverage](collation/chapter-01/scan-coverage.json).

## Saved coverage and unfinished work

PDF numbers refer to the named witness; provider-container numbers apply to Adzom1973 and Gcn. An inspected page is not automatically a collated page.

| Witness | Saved, reviewable coverage | Still required |
|---|---|---|
| Adzom base | Main sequence U00007–U02635: [opening/boundary](collation/chapter-01/opening-boundary-review.json), [PDF5–50](collation/chapter-01/continuous-early.json), [PDF51–101](collation/chapter-01/continuous-late.json); [41 annotation records](collation/chapter-01/annotation-audit.json). | Whole PDF1–102 physical signs/source layers; 30 remaining candidates; insertion signs S02–S07/U01286; title/portrait. Keep U01522/U02615/U02620/S09 unresolved unless evidence resolves them. |
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

The [54-file recovery matrix](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/blob/recovery/task-records-2026-09-27/diplomatic/recovery/2026-09-27-task-records/missing-report-recovery-matrix.md) tracks missing historical report files, often JSON/Markdown pairs—not 54 independent research passes. **Four complete report bodies were replayed from retained transcript sources; 50 remain incomplete.** Partial bodies, failed-save commands, summaries and withdrawals remain useful evidence, but are not completed witness coverage. Historical 1,016/1,024-observation claims must not replace the saved 123-record apparatus.

Usable sources remain: ten mapped facsimile assemblies, acquisition manifests/archives, three supplied transcript families, provider containers and retained evidence crops; see [source inventory](SOURCES.md). Some large files require Git LFS materialization. Sichuan full scans and catalogue-only Paltség/CTRC/Gangteng leads remain unavailable in the acquired holdings. Missing reports do not mean these other source scans vanished.

## Completion gate and next bounded work

The saved [validation record](VALIDATION.json) reports passing reconstruction, source accounting, links and listed-hash checks. It explicitly says `chapter_complete: false`; it cannot detect unseen manuscript variants.

The [sign audit](reviews/chapter-01/sign-adoption-audit-20260927.md) records ten independently reverified targets: nine added interventions and one revised intervention. **Thirty candidates and systematic proofreading remain.** The exact candidate list and acceptance criteria are in the [readiness audit](reviews/chapter-01/readiness-audit-20260927.json); its older snapshot counts/tasks are superseded by its post-recovery updates and current STATUS.json.

Next scholarly work, when resumed: review those candidates, resolve or precisely bound remaining base uncertainties, then fill witness gaps above using retained ledgers first. Commit and verify each substantive batch remotely. Complete Chapter1's declared coverage and apparatus before starting Chapter2. This status audit changes no canonical text.
