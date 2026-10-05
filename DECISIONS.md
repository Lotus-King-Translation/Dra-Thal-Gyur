# Project decisions

## Preserved project history

This root entry point is added for shared-policy adoption; it does not replace or duplicate the existing locus ledgers. Source decisions remain in [the chapter 1 release ledger](diplomatic/release-v1-proposal/DECISIONS.json) and the chapter 2–6 `DECISIONS.json` files under `diplomatic/`. Their governing continuation is [diplomatic/HANDOFF.md](diplomatic/HANDOFF.md). English reconciliation decisions and provisional usages remain in [the existing reconciliation ledger](translations/2026-09-26-full-draft/golden-review/DECISIONS.json). Source-based pairing decisions and full membership lineage remain in [STRUCTURE-DECISIONS.json](paired/v2/STRUCTURE-DECISIONS.json) and [PAIR-AUDIT.json](paired/v2/PAIR-AUDIT.json). The explicit 2026-09-27 frequent remote-preservation instruction is retained in [AGENTS.md](AGENTS.md).

## Shared template decisions — preserved scope and provenance

The following P1, P2 and P3 records are copied verbatim from [`Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`](https://github.com/Lotus-King-Translation/tibetan-text-project-template/blob/882454cb2576d0b2529296bd7a3a7c87371ab4cf/DECISIONS.md). Their template-only scope, historical version/hash statements, validation claims and issue dispositions describe those original template changes, not tests or translation corrections in this book. The local adoption record below makes the pinned resulting policy operative here. P3's explicit issue-disposition supersession is retained; older assistant proposals and unapproved book usages are not new authority.

<a id="post-translation-review-2026-10-05"></a>

### 2026-10-05 — Capture issues #1/#2 and add completed-English review (P3)

**Authorization:** the owner directed that the lessons in issues #1 and #2 be incorporated into the template rather than left pending in tickets, and that the guideline and AGENTS.md cover review of completed English by another agent. The owner will propagate the files and assign one reviewer to each of the four works. This task does not perform those reviews.

**Implemented scope:** baseline `43b24b2781d9f278b413b5c833012e42758232d4`; standard **2.1.0**, Phase D in `AGENTS.md`, shared controls in Part I §8.1 and the executable review contract in Part III. Reuse Part II Q1–Q9, the existing finding/usage formats, status and handoff. No new workflow file, schema, validator, lexicon redesign or translation is introduced. The entire **283-row glossary is byte-for-byte unchanged**, including all original assignments and P1/P2 controls.

**What replaces the pending-ticket dependency:** approved vocabulary stays in the CSV. The remaining U01–U14 questions are captured as explicit, reusable construction/family review controls, including the owner's preferences and exclusions; they are no longer dependent on issue comments or chat. Reviewers must examine them when encountered, record evidence and a local disposition or visible unresolved treatment, and return genuinely new shared-label proposals without activating competing book glossaries. This instruction authorizes the review process, not unspecified new English defaults. Uncertainty is an explicit review outcome, not a silent omission or reason to leave the entire task unprocessed.

**Capture map (all 44 U groups and 21 G groups):**

| Groups | Operative home |
| --- | --- |
| U01–U03 | Approved honorific/name CSV rows; Part I §8.1 full/short forms, unresolved honorific/title and recurring-name controls |
| U04 / U09 / U11 / U14 / U15–U44 | P2 CSV assignments, conditions and source references; Part I §8.1 links and Part III §3 checks |
| U05–U08 / U10 / U12–U13 | Part I §8.1's family/meditation/compound/means/two-truth/phrase/luster controls, with actual alternatives and comparator IDs |
| G01–G10 | Existing protected terms plus Part III §3's lexical, component, whole-expression and omitted-relationship checks, with loci |
| G11 / G13 / G14 / G17 / G20 | P1 CSV rules; Part I §9 and Part III §3 scope/capitalization/adoption checks |
| G12 / G15 / G16 / G18 / G19 / G21 | Part III §3's source-dependent exception, qualifier, ordinary-sense and short-form checks under Part I §6 |

**Phase D boundary:** freeze source/English/policy inputs and reviewer identity; distinguish review-only from authorized revision; inspect every pair including closing material; recheck corrections and derived outputs; preserve historical records. Reuse one report with exact coverage, before/after evidence, no-change cases, unresolved questions and actual tests. A completed review is not clean text approval, a new release, or human certification. Four agents may finish independently under one pinned policy; the coordinator handles cross-work reconciliation. No additional review stage is required merely to check the reviewer's own edits.

**Issue disposition:** issues #1 and #2 may close as completed **template learning-capture** tasks once this commit is published and linked. Their audit bodies and comments remain historical evidence. This supersedes P1/P2's instruction to keep those template tickets open; it does not claim their example passages were corrected or their unresolved lexical interpretations approved. Work-specific findings now belong to the Phase D review package, not a new holding ticket.

**Propagation:** adopt `AGENTS.md`, `guidelines/tibetan_translation_standard_v2.md`, and `glossary/expanded_tibetan_english_glossary.csv` from the same template snapshot. Merge P1/P2/P3 into each book's `DECISIONS.md` and add Phase D fields from `translations/HANDOFF.md`; preserve local decisions, populated status and history. The three updated READMEs are optional navigation changes. Update local `PROJECT-STATUS.md` for adoption without copying its template placeholders. No source/English placeholder, script, tag or source register needs propagation.

**Validation:** all 44 U groups and 21 G groups are accounted for in the capture map and operative files. The full 283-row/eight-column glossary and 24 unrelated tracked files are unchanged; exactly eight existing documents changed, with no new tracked files. Relative links, section anchors, active version references and 72 distinct cited pair IDs were checked. Ten in-memory document-integrity corruption controls were rejected. The existing paired-template validator passed with zero placeholder pairs, and `git diff --check` passed. R58–R63 extend the existing section to 63 fixture specifications; R48 corrects a copied unresolved-source spelling, not a Tibetan edition; the other 56 prior fixture rows are unchanged. The new contract and controls were self-reviewed, not independently certified. No translation-model benchmark or new full-book semantic review was performed. No book/source/tag is changed by this patch.

**Content identities:** glossary SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`; standard SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`.

<a id="terminology-expansion-2026-10-05"></a>

### 2026-10-05 — Approved issue #1 additions and matter/karmic-being clarification (P2)

**Authorization:** the owner accepted the proposed U15–U44 treatments in chat and instructed implementation in the template, except that U35 should not use the proposed insentient-matter label. The owner explicitly confirmed **karmic being** for སེམས་ཅན and suggested **matter** for བེམ་པོ/བེམས་པོ, subject to comprehension. P2 implements matter with a source-sensitive scope note, rather than reintroducing sentience vocabulary. Earlier firm decisions in [the owner's issue comment](https://github.com/Lotus-King-Translation/tibetan-text-project-template/issues/1#issuecomment-5978887526) remain authoritative. Approval concerns these proposed defaults and their stated conditions, not unconditional application to disputed clauses.

**Finite scope:** template only; baseline `cd9d1c26ee70dc7d486b50c2d9df1244613215f5`. Append **61 records**, including separate attested forms, for **283 total glossary rows**. This covers all **30 groups U15–U44**, six earlier groups with specifically settled implementation (U01/U03/U04/U09/U11/U14), and the newly reconfirmed karmic-being convention. The original **222 Tibetan–English assignments remain unchanged and in order**. Correct only status/provenance fields in two existing rows that still called standalone ཐུགས absent. Update the existing combined standard to **2.0.2**, retaining its filename; update the decision/status/handoff records and issue #1. No translation or source publication is part of this patch.

**Approved defaults and controls:** exact forms, grammar, triggers, exclusions, related entries and pinned source evidence are in the existing CSV, not a competing synonym list. U15–U44 follow the accepted proposals. The linked cluster is **essence / core / pure extract / quintessence**; core never becomes essence, and no general core-to-quintessence exception is activated. Existing whole-expression assignments, including Mahamudra, retain precedence. Earlier firm entries added here are the full/short **Blessed One**, the proper name **Vajradhara**, **sacred pledge**, **transmission**, **key point**, and **core**.

**U35:** use **matter** as the mass noun and **material thing(s)** where the source requires count grammar. The relevant knowing/non-knowing distinction must remain intelligible, with a source-linked explanatory note where the concise label obscures it. Matter does not mean immobile, dead, lifeless or non-karmic being, and does not imply that karmic beings lack material bodies. It does not replace every occurrence of body, entity or substance. Selected checks: DTG-000111/000869, SMB-000047/000050 and MTP-000540/000550. The default is implemented; disputed comprehension or clause interpretation remains locally reviewable.

**U36/U40:** citta is an approved **retention policy**, not certification of a heart/anatomical identity. Awakened mind is approved for standalone ཐུགས in the cognitive/honorific scope. Heart/location passages and the unresolved Pearls clauses remain open to construction-level review. Lexical approval alone must not remove their uncertainty markers.

**Not silently approved:** U02's specific Joy-Maker/Delight-Maker/Maker-of-Joy choice; U05's affliction/mental-state defaults; U06's bsam gtan label; U07's every-occurrence itself treatment; U08's thabs rule; U10's superficial/superfactual pair; U12's phrase/word rule; U13's luster/lustre decision. The English equivalent for Tathāgata and the distinct rdo rje dzin title also still need explicit selection. Neither this patch nor a settled proper-name entry turns those open questions into approved defaults. The owner-approved U15–U44 label choices do not decide every disputed historical passage.

**Guidance and examples:** recognize scoped Approved P2 entries alongside the preserved original assignments; preserve complete karmic-being wording and avoid an invented inverse relation to matter; distinguish English honorifics from retained proper names and compositional epithets. Remove obsolete standalone-thugs absence claims in Parts I/II and R24. Add **R35–R57**, yielding **57 fixture specifications**, covering both conforming treatments and prohibited overextensions. These extend the existing section only.

**Adoption and remaining work:** template encoding is complete (**61/61 rows; 30/30 approved new groups**). Eight earlier groups still need specific choices, with the partial honorific/title questions noted above. All four books still require explicit glossary/standard adoption and source-sensitive English/note revisions. Do not overwrite historical release inputs, rewrite Tibetan, or treat issue #1 as closed. Issue #2's existing translation departures are not corrected by adding entries here.

**Validation:** Structural/source-reference checks passed: all 222 original assignments and their order preserved; the eight-column schema unchanged; 220 original raw records untouched, with only status/provenance fields changed in the two obsolete standalone-thugs documentation records. All 61 additions have explicit approval, scoped usage and verified pinned Tibetan occurrence references; no new duplicate headwords. 14 in-memory corruption controls were rejected. All 33 unchanged original fixtures and P1 expected results are preserved; R24 is updated and R35–R57 added. The existing paired-template validator passed with zero placeholder pairs, and git diff --check passed. New fixture specifications and selected matter/citta/related-term examples were self-reviewed, not independently certified; no translation-model benchmark, full book retranslation, scan proofreading or exhaustive new semantic audit was performed. 27 unrelated tracked files are unchanged; no new tracked file, tool, schema or review stage is introduced.

**Content identities:** glossary SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`; standard SHA-256 `c1b8e91dcfc858fa3b87bb0adba63f98b28ff273f350e34cf9d45e82951cfbbb`. This is a template maintenance commit, not a new fixed Tibetan or English release; no tag is created or moved.

<a id="terminology-clarification-2026-10-04"></a>

### 2026-10-04 — Bounded issue #2 terminology clarification (P1)

**Authorization:** after reviewing [issue #2](https://github.com/Lotus-King-Translation/tibetan-text-project-template/issues/2) and the proposed bounded patch, the owner instructed: “Do the changes/updates now in the template repo.” The approval concerns the specific five-row/three-amendment proposal, not every alternative interpretation listed in the issue.

**Scope and version:** template only; translation standard **2.0.1** and glossary clarification revision **2026-10-04 (P1)**. Retain the standard's existing filename. Baseline template commit: `f6431c25c7c9fa852c404b8cd3e0e3cdeae1178f`. All 222 Tibetan–English assignments, row order, eight columns and unrelated supplementary cells remain unchanged. No new headwords, files, tools, schemas or review stages are introduced.

**Approved glossary clarifications:** the operative conditions and exclusions are recorded in the five existing rows, with P1 provenance:

| Existing assignment, unchanged | Approved clarification | Issue group |
| --- | --- | --- |
| རྒྱུད་ → Continuum | Literary **tantra** only for unambiguous tantric scripture/text-genre uses; retain other senses and whole-expression precedence | G11 |
| སྒྲ་ → Word | Auditory **sound** where the sense is supported; retain linguistic whole expressions and review ambiguous extensions | G14 |
| འབྲས་བུ་ → Result | Botanical **fruit** and explicitly sustained tree/fruit metaphors, not blanket stylistic alternatives | G17 |
| གཞི་ → The Ground | Technical **Ground**, with ordinary article grammar; no adjudication of disputed support/other senses | G13 |
| གཞི་སྣང་ → Ground-appearance | Consistent technical capital G and existing hyphenation | G13 |

**Guidance:** Part I §3.3 now addresses overlapping source modifiers and established English components without automatic duplication or loss; §6 requires reuse of adopted shared approved usages rather than competing chapter/book defaults; §9 defers to approved glossary presentation rules. Part II extends R04/R11/R18 and adds R31–R34, retaining all existing IDs and the other expected distinctions. Normal grammatical variation still needs no new lexical approval.

**Not approved or performed:** no general logical-property, physical-movement, separating/secret-preliminary or nominal-apprehension exceptions (G12/G15/G16/G18); no final adjudication of the individual G19 vajra passages. Other pending proposals remain pending. G01–G10 remain translation-remediation tasks, not reasons to add synonyms. No sibling repository, Tibetan source, English translation or release tag is changed, and issue #2 remains open.

**Adoption:** consuming projects must explicitly adopt the new glossary/standard versions and recheck affected occurrences. Do not overwrite inputs bound to historical releases. This template update is not a claim that existing translations have been corrected or brought into compliance.

**Validation:** Structural checks passed: all 222 base assignments, their order and the eight columns are unchanged; exactly five glossary records changed, with the other 217 raw records unchanged. All 29 other tracked files are unchanged. The fixture table has 34 unique IDs, with 27 original fixture rows unchanged. Seven in-memory corruption controls covering assignment/headword changes, row order/count, schema, unrelated supplementary edits and duplicate/replaced rows were rejected. `git diff --check` and the existing paired-template validator passed (zero placeholder pairs). The seven affected fixture specifications were manually reviewed; no translation/QC model benchmark or independent philological certification was performed.

**Content identities:** glossary SHA-256 `07e1b3a567aa6abb72fac931b23830deba68de14477a9c3b147296d960995ce4`; standard SHA-256 `710abf09ac7b98f6cb092dec11493787425280cc52031b2c1b41d8fe477e89c2`.

<a id="policy-adoption-2026-10-05"></a>

## 2026-10-05 — Adopt the common pinned policy; do not review English

**Authority and scope:** the owner's current propagation instruction explicitly names this repository, the template commit `882454cb2576d0b2529296bd7a3a7c87371ab4cf`, the three operative files, and the required decision/status/handoff merges. It authorizes policy adoption, validation and publication only; it expressly prohibits English review, retranslation or correction, source/pair changes, archived-input changes, new terminology decisions, and template-repository edits.

**Operative baseline:** standard **2.1.0**, SHA-256 `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f`; glossary **283 data rows / eight columns**, SHA-256 `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7`. Both files are byte-identical to the pinned template. P1/P2/P3 are adopted with their original anchors and scoped approvals. No later explicit owner-approved local terminology exception was found in the inspected decision history; no exception is inferred from assistant proposals or local usage notes.

**Local history retained:** The existing Adzom source authority, diplomatic recovery/continuation instructions, paired-text/2 source-only formats, immutable membership and v1-to-v2 lineage are retained. Earlier source and English locus decisions stay in their existing ledgers; this root record does not replace them. Earlier 'glossary unchanged' statements and phase deferrals retain their original release/task scope; they do not override this newer explicit active-policy adoption. They are not rewritten to claim that earlier releases used the new baseline.

**Preservation and validation boundary:** existing source/English releases and tags remain fixed. Historical policy inputs remain available at their exact unchanged commits/tags, and archived copies are not overwritten. Legacy validators that bind active policy paths to earlier release hashes may reject this adoption checkout; those failures are reported, not hidden by editing old contracts, signatures, validators, or derived outputs. See [actual before/after checks](translations/HANDOFF.md#policy-adoption-validation). Publication is via `policy/adopt-template-882454cb` and a pull request to `main`; adoption on `main` is not claimed before merge.

**Review state:** reviewer/session unassigned; reviewed pairs **0/2667**; review completion **not started**; text disposition **not assessed**. One bounded policy adoption is recorded for this repository, with **0** English changes and **0** reviews performed.
