<a id="phase-d-review"></a>
# Post-translation review — current working text

**Task:** POST_TRANSLATION_REVIEW · **Mode:** review-and-revise · **Session:** DTG-PD-20261005-Astra-01 · **Reviewer:** GPT-6 Astra Pro, this review session, distinct from the September 26 authoring run and October 1 source-reconciliation coordinator. Review of the input is independent of those runs; checks of this session's repairs are self-checks, not a second independent review or human certification.

**Authority:** the owner's explicit October 5, 2026 assignment authorizes the smallest supported English and translation-note repairs in this repository only. No fresh translation, stylistic rewrite, Tibetan emendation, segmentation change, new shared glossary assignment, release or tag movement is authorized.

## Frozen inputs and adopted policy

English input commit: `fc3a443ba5987efb0b132990bf131a236fa57320` (current remote main at freeze). Canonical authored working English: `paired/translation.md`; fixed paired source: `paired/source.md`. Inherited translation edition: `translation-golden-aligned-v1.0.0` (`e24e97ddad9cefa339b5583a38389179dba7a365`). Paired identity/format edition: `dra-thal-gyur-paired-v2.0.0` (`d2285b8fe09e2a27be7aab5bcfb7a87806e949c5`). Golden Tibetan: `root-tantra-v1.0.0` (`b83051912977268b97615bd382d82e51c3406d61`). These are inherited edition identifiers, not a new release or a certification of revised text.

Common policy commit: `Lotus-King-Translation/tibetan-text-project-template@882454cb2576d0b2529296bd7a3a7c87371ab4cf`. Local adoption: `10fe4e8c1ea0be37a205753dbb4a7e6e4c84a126`, merged by PR [#5](https://github.com/Lotus-King-Translation/Dra-Thal-Gyur/pull/5) at the frozen main commit; merge verified through GitHub and the remote ref. Standard **2.1.0, Parts I–III**, including I §8.1 and III, and **283 data rows with all eight glossary columns** were read. Active policy hashes and row/column counts were recomputed and match the adopted records. P1/P2/P3 govern only their stated scopes. No later explicit owner-approved local terminology exception was found; the present assignment changes edit authority, not glossary policy.

Root `FORMAT.md` is absent (documentation gap). The operative local format is documented in `paired/README.md`, `paired/MIGRATION.md`, `paired/core.py` and the retained `paired/v2/reference/template-FORMAT.md`; the latter is a historical format reference, not a replacement terminology-policy version. The complete 2,660-entry lineage JSON was parsed and reproduced from the pinned baseline without discrepancy. Source structure and membership will not change.

| Frozen file | SHA-256 |
|---|---|
| `AGENTS.md` | `d12a92da3151ac74995a2f81b517a2329730aa09b441de99b3c81723be1edf71` |
| `PROJECT-STATUS.md` | `156351ff053b1faa1a2c2b58e76abb3fc6ab491d1f36af361eaa61ae2ad84baf` |
| `translations/HANDOFF.md` | `192599bde87085fb5e5b624e3c9ce11554e01917daf438508fa166d961e4da95` |
| `DECISIONS.md` | `138e4a35e028a9be6df7127e66cb58263b83c671dad47f6ea12d7aebe6070693` |
| `guidelines/tibetan_translation_standard_v2.md` | `dba2654f0790ffb3e3c59a71097588a11d18b0122d26a3e46beb82045d0cc32f` |
| `glossary/expanded_tibetan_english_glossary.csv` | `f767cd8af409bc16a6ed41bb086d23d1f204cb6db76c48189c168a9a95401da7` |
| `paired/source.md` | `f25ec78468cc5120426ad59e689d8708159a42fa16d5aa3869a990b53f31cc4c` |
| `paired/translation.md` | `06dfdd15d37c504f644a2d76583236eff15cc28bf19417c1b6ddedd89af8d1e8` |
| `paired/v2/STRUCTURE-DECISIONS.json` | `b5b2241b9214cfa0c468341f5b6e25bf08084cf021389595260d60266899fda0` |
| `paired/v2/PAIR-AUDIT.json` | `27285d659160afeced6022d4801f301e365404e8d7ad312d1117ec12787d1efc` |
| `paired/v2/reference/template-FORMAT.md` | `c4c6d00ff8cb09dea5743368087da735c7adb86fde0692c3a10594a5ccba7b98` |
| `diplomatic/root-tantra-v1/release/reading.json` | `d0f03b58e4e60ae8db730dfe2a498742d4e9d2e3f4d74fa5bdb13c9574c9b309` |
| `diplomatic/root-tantra-v1/release/reading.md` | `a49fc523d54a2705fe5a1b712a3703c0cc6539e9824364c23c4f47bb14dc910e` |
| `translations/2026-10-01-golden-aligned/REVIEW.md` | `e727eced469cd6e4e1b94801e9d3e2accb2b703cc039d716f7da520be4364c4a` |
| `translations/2026-10-01-golden-aligned/USAGES.json` | `3233afe2a8d1727d97b5b21a9d79e92b0f68e8f4b8c2e9894ef661fe745ac47c` |

### Preservation and release inventory

Initial local checkout was clean on `policy/adopt-template-882454cb` at `10fe4e8`; remote main was fetched and its tree matched that checkout. The review branch starts at frozen main. No stash existed. The detached recovery worktree at `4dd344ee4febca7cb117f03519c6ec85ede6e930` was clean and was not changed. The local-only recovery baseline `e17a496` is already an ancestor; all existing branches/worktrees were preserved. No reset, cleanup, force push or tag write was performed.

Remote annotated tag objects and peeled commits were read at freeze:

| Ref | Object/commit |
|---|---|
| `refs/tags/chapter-01-v1.0.0` | `7f74249c6378dd9f5b6733456bf4cec5a79af0b8` |
| `refs/tags/chapter-01-v1.0.0^{}` | `cf8430ce08240f179fa1cadefebedb3ec2cc6f4c` |
| `refs/tags/chapter-02-v1.0.0` | `303899657ec087447f3c679208ae43992f530f0d` |
| `refs/tags/chapter-02-v1.0.0^{}` | `6e9b4ed977103b6151bbd75784852a4a17865c90` |
| `refs/tags/chapter-03-v1.0.0` | `79d19d71df1369288ff11ebdfb9306cdea9f9edf` |
| `refs/tags/chapter-03-v1.0.0^{}` | `17abe1f0e68069406f782a77e93dab10841b81fb` |
| `refs/tags/chapter-04-v1.0.0` | `7ba6a17a9e688b7c9ef8f8bc80617839e3b72358` |
| `refs/tags/chapter-04-v1.0.0^{}` | `5abb397ab77a32b6e360d0a269ed92bf71b855e1` |
| `refs/tags/chapter-05-v1.0.0` | `8a9286c3e2053eceb1ff78223858510c07e0591e` |
| `refs/tags/chapter-05-v1.0.0^{}` | `c4e03593e52939c52f989c6611e2ea4df967afb2` |
| `refs/tags/chapter-06-v1.0.0` | `a7edeeabdec771aeefbacd94020d09ca79c00737` |
| `refs/tags/chapter-06-v1.0.0^{}` | `128dc0fedf0de737ca14e025ee4aa0028b145713` |
| `refs/tags/dra-thal-gyur-paired-v2.0.0` | `449483c4003479803f8ee19fd965cd8be1183953` |
| `refs/tags/dra-thal-gyur-paired-v2.0.0^{}` | `d2285b8fe09e2a27be7aab5bcfb7a87806e949c5` |
| `refs/tags/root-tantra-v1.0.0` | `97379615d268149eee768c9c1ec99b7be2f993b4` |
| `refs/tags/root-tantra-v1.0.0^{}` | `b83051912977268b97615bd382d82e51c3406d61` |
| `refs/tags/translation-golden-aligned-v1.0.0` | `ed0783c6a394d4ace736a09d812f0666c6743848` |
| `refs/tags/translation-golden-aligned-v1.0.0^{}` | `e24e97ddad9cefa339b5583a38389179dba7a365` |

The October 1 source-reconciliation report remains verbatim below as history. Its 173 endnotes, 340 earlier-note IDs (4,932 object/note associations), 65 separate source-annotation components, 23 restored verses and 18 closing anchors are inputs, not evidence of fresh semantic review. Existing `USAGES.json`, `LEGACY-NOTES.md`, golden `UNCERTAINTIES.md`, and source-reconciliation `DECISIONS.json` supply current dispositions before an older criticism is evaluated. No new source update after the fixed golden edition is adopted here.

<a id="phase-d-coverage"></a>
## Finite whole-work scope and actual coverage

File/source order, not numerical ID order, governs. Chapter 1 includes the title/opening and the twelve split children DTG-002661–DTG-002672; the five retired v1 IDs are not reintroduced. The complete ordered inventory remains the existing canonical source and `paired/v2/PAIR-AUDIT.json`, not a second segmentation ledger. Total scope: **2,667 pairs / 5,484 golden objects** (5,466 original anchors and 18 additions); formats: 48 prose, 2,448 verse, 2 h1, 0 h2, 169 h3.

<!-- phase-d-coverage-start -->
| Part | Expected pairs | Expected source-ordered range | Actually semantically reviewed | Status |
|---|---:|---|---:|---|
| chapter-01 | 1199 | DTG-000001 → DTG-001192 | 100 (ordinals 1–100; through DTG-000098) | In progress |
| chapter-02 | 543 | DTG-001193 → DTG-001735 | 0 | Not started |
| chapter-03 | 354 | DTG-001736 → DTG-002089 | 0 | Not started |
| chapter-04 | 237 | DTG-002090 → DTG-002326 | 0 | Not started |
| chapter-05 | 211 | DTG-002327 → DTG-002537 | 0 | Not started |
| chapter-06 | 108 | DTG-002538 → DTG-002645 | 0 | Not started |
| closing-material | 15 | DTG-002646 → DTG-002660 | 0 | Not started |
<!-- phase-d-coverage-end -->

The fixed golden has **72 uncertainty-bearing objects in 66 pairs**; this is a source-qualification inventory, not the final count of unresolved translation questions. Opening inscriptions, caption, empty annotation carriers, chapter-transition metadata and closing graphics remain in scope. Exact inherited pairs:

`DTG-000001`, `DTG-000002`, `DTG-000003`, `DTG-000004`, `DTG-000005`, `DTG-000008`, `DTG-002662`, `DTG-000016`, `DTG-000023`, `DTG-000034`, `DTG-000038`, `DTG-000048`, `DTG-000059`, `DTG-000068`, `DTG-000070`, `DTG-000080`, `DTG-002665`, `DTG-002666`, `DTG-000166`, `DTG-000167`, `DTG-000181`, `DTG-000182`, `DTG-000183`, `DTG-000563`, `DTG-000584`, `DTG-000696`, `DTG-000709`, `DTG-002667`, `DTG-002668`, `DTG-002671`, `DTG-001187`, `DTG-001191`, `DTG-001192`, `DTG-001331`, `DTG-001332`, `DTG-001333`, `DTG-001334`, `DTG-001354`, `DTG-001519`, `DTG-001735`, `DTG-001826`, `DTG-001904`, `DTG-001905`, `DTG-001906`, `DTG-002088`, `DTG-002089`, `DTG-002091`, `DTG-002195`, `DTG-002218`, `DTG-002284`, `DTG-002325`, `DTG-002326`, `DTG-002396`, `DTG-002480`, `DTG-002486`, `DTG-002495`, `DTG-002514`, `DTG-002536`, `DTG-002537`, `DTG-002559`, `DTG-002585`, `DTG-002624`, `DTG-002633`, `DTG-002645`, `DTG-002653`, `DTG-002654`.

Review protocol: read every source/English pair and associated notes in source order, apply Q1–Q9, I §8.1 and III, read continued sentences across pair boundaries, then perform bidirectional terminology and continuous-English checks. Pattern matches are candidates only. Findings are recorded below before repairs. No percentage of accuracy will be inferred from counts.

<a id="phase-d-findings"></a>
## Current findings and dispositions

The freeze checkpoint had no semantic findings. Batch records below distinguish read coverage, evidence recorded before repair, and actual application/self-check status. Coverage is not inferred from inventory or structural checks.

<a id="phase-d-batch-01"></a>
### Batch 01 — source ordinals 1–100 (DTG-000001 → DTG-000098)

All 100 pairs and all 50 first-encountered attached historical/reconciliation notes were read against the current golden strings, including the opening material and continued clauses. Q1–Q9, I §8.1 and III were applied. The full rows for the correction families below were re-read, including exceptions and allowed forms. **Evidence was recorded before application. All 17 scoped repairs across 15 pairs are now applied and self-checked.**

| Finding | Severity / confidence | Source-based rationale and bounded scope |
|---|---|---|
| PD-T01 | Terminology / high | P1 literary-use exception: explicit titles (including the foreign-title's provisional English rendering), the king of texts gathering all teachings, and the family of texts from which teaching is proclaimed denote tantric scriptures. Use tantra, not continuum. This does not license replacing path-continuum at DTG-000092 or every nearby rgyud. Foreign lettering and the proposed All-Penetrating Word title remain qualified. |
| PD-T02 | Terminology / high | P2 cyclic-existence terminology; the opening coordinated འཁོར་དང་འདས་པ is the recognizably paired technical contrast, not an unrelated isolated 'das. Retain both members, the temporal beginning, and the path's possession relation. |
| PD-T03 | Terminology / high | P2 complete sems can equivalent is karmic being; plural preserved. This does not change 'gro ba, las can, or bare sems. |
| PD-T04 | Terminology / high | P2 dngos grub requires spiritual accomplishment. Retain ultimate, supreme, plurality and the following negation of effort. |
| PD-T05 | Terminology / high | P2 actual spatial bar snang is open sky here, distinct from nam mkha' space in the same clause. No interval or accidental adverbial substring is involved. |
| PD-T06 | Presentation / high | P2 mandates mandala without diacritics in this technical use. No semantic change; thabs cig remains together, not methods. |
| PD-T07 | Rhetorical function / high | Repeated kye kye is the repeated vocative O, O. There is no nyon/listen imperative to translate at this location. Preserve both vocatives, the quotation, Blessed One, and separately written e ma (still locally provisional). |
| PD-E01 | Presentation / high | Lowercase from continues the same sentence after the comma. It does not introduce a second sentence or change source verse form. |
| PD-S01 | Syntax / high | U00116 བྱིན་གྱིས་རླབས་ཀྱིས is instrumental. English incorrectly made blessing the actor. Through blessing plus a passive predicate preserves the instrument without inventing a named agent; the preceding speech instrument and the provisional its-own-sound reference remain. |
| PD-S02 | Modifier attachment / high | U00119's genitive participle བཅུད་བསྡུས་པའི qualifies the following king of tantras, not the preceding kalaviṅka sound. Move the existing English relative clause immediately after its head within the same unchanged pair. Keep the teacher as speaker, 360 sounds, temporal relation, and quintessence. |

The following exact scoped repair records are also the application checklist. Tibetan is quoted byte-for-byte from the frozen pair; newlines are escaped in JSON. Two repairs in DTG-000047 are explicitly sequenced, not counted as two changed pairs.

<!-- phase-d-batch-01 -->
```json
[
  {
    "pair": "DTG-000002",
    "golden": [
      "U00002"
    ],
    "tibetan": "རཏྞཱཀཱརཤབྡམཧཱཔྲསཾགཏནྟྲནཱམབིཧརཏིསྨ།།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000004",
    "golden": [
      "U00004"
    ],
    "tibetan": " རིན་པོ་ཆེ་འབྱུང་བར་བྱེད་པ་སྒྲ་ཐལ་འགྱུར་ཆེན་པོའི་རྒྱུད་ཅེས་བྱ་བ་བཞུགས།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000005",
    "golden": [
      "U00005",
      "U00006"
    ],
    "tibetan": "གཾགརྦམཏགཱ རྒྱ་གར་སྐད་དུ།\n རཏྣ་ཀ་ར་ཤབྡ་མ་ཧཱ་པྲ་སཾ་ག་ཏནྟྲ་ནཱ་མ།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000006",
    "golden": [
      "U00007",
      "U00008"
    ],
    "tibetan": " བོད་སྐད་དུ།\n རིན་པོ་ཆེ་འབྱུང་བར་བྱེད་པ་སྒྲ་ཐལ་འགྱུར་ཆེན་པོའི་རྒྱུད་ཅེས་བྱ་བ།",
    "before": "Continuum",
    "after": "Tantra",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000047",
    "golden": [
      "U00117",
      "U00118",
      "U00119",
      "U00120",
      "U00121",
      "U00122",
      "U00123"
    ],
    "tibetan": "དེ་ནས་ཕྱོགས་བྲལ་ནམ་མཁའ་ལས། །\nཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་ལས། །\nབསྟན་པ་ཀུན་གྱི་བཅུད་བསྡུས་པའི། །\nརྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ཉིད་ནི། །\nཚིག་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང་། །\nབརྒྱ་ཕྲག་གསུམ་དང་དྲུག་ཅུ་ཡི། །\nསྒྲ་ལས་དྲངས་ཏེ་སྟོན་པས་གསུངས། །",
    "before": "this very king of continua,",
    "after": "this very king of tantras,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000060",
    "golden": [
      "U00158",
      "U00159",
      "U00160",
      "U00161"
    ],
    "tibetan": "དེ་ལྟར་གསུངས་པའི་ཆོ་འཕྲུལ་དུ། །\nརྒྱུད་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང་། །\nརྩ་བའི་སྒྲ་ཚིག་ཐལ་འགྱུར་ལས། །\nཐམས་ཅད་ངེས་འབྱུང་བསྟན་པར་འཕྲོས། །",
    "before": "even before all continua,",
    "after": "even before all tantras,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-002662",
    "golden": [
      "U00013",
      "U00014",
      "U00015",
      "U00016",
      "U00017"
    ],
    "tibetan": "འཁོར་དང་འདས་པའི་ཐོག་མར་ནི། །\nརང་བྱུང་བྱས་པ་མེད་པ་ལས། །\nའབྱུང་བ་འདུས་པའི་ཕུང་པོར་ཤར། །\n ས་ཆུ་མེ་རླུང་འབྱུང་བ་བཞི། །\nདབུས་སུ་རླུང་སེམས་རྒྱུ་དང་རྐྱེན། །",
    "before": "At the beginning of samsara and what is beyond it,",
    "after": "At the beginning of cyclic existence and transcendence of sorrow,",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000061",
    "golden": [
      "U00162",
      "U00163"
    ],
    "tibetan": "བསྟན་པ་དམ་པའི་འདུ་མཆེད་གྲུབ། །\nགསུངས་པས་འཁོར་བ་ནུབ་པར་བྱེད། །",
    "before": "by its being spoken, samsara is made to subside.",
    "after": "by its being spoken, cyclic existence is made to subside.",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000092",
    "golden": [
      "U00209"
    ],
    "tibetan": "འཁོར་བའི་ལམ་རྒྱུད་གང་གིས་བཅད། །",
    "before": "What cuts the continuum of samsara's path?",
    "after": "What cuts the continuum of the path of cyclic existence?",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000086",
    "golden": [
      "U00203"
    ],
    "tibetan": "སེམས་ཅན་དུས་ཀྱི་རིམ་པ་གང༌། །",
    "before": "What are the successive ages of sentient beings?",
    "after": "What are the successive ages of karmic beings?",
    "finding": "PD-T03"
  },
  {
    "pair": "DTG-000040",
    "golden": [
      "U00097",
      "U00098",
      "U00099"
    ],
    "tibetan": "དངོས་གྲུབ་མཆོག་རྣམས་མཐར་ཐུག་པའི། །\nའབད་ཅིང་རྩོལ་བ་མ་ཡིན་པས། །\nགང་སུ་འཕྲད་པ་གྲོལ་བར་ངེས། །",
    "before": "Since the ultimate supreme accomplishments",
    "after": "Since the ultimate supreme spiritual accomplishments",
    "finding": "PD-T04"
  },
  {
    "pair": "DTG-000045",
    "golden": [
      "U00107",
      "U00108",
      "U00109",
      "U00110",
      "U00111",
      "U00112",
      "U00113"
    ],
    "tibetan": "དེ་ལྟར་དངོས་ཀྱི་བསྟན་པ་ལས། །\nགཟུགས་བརྙན་ཆོ་འཕྲུལ་འདི་ལྟ་བུ། །\nསུས་ཀྱང་བརྗོད་དུ་མེད་པར་ནི། །\nནམ་མཁའ་མི་འབྱེད་བར་སྣང་ལས། །\nཚིག་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང༌། །\nདགུ་གཉིས་བཞི་ཡི་ཡང་སྟེང་ནས། །\nཚངས་པ་ཆེན་པོའི་དབྱངས་སུ་བསྒྲགས། །",
    "before": "[was proclaimed] from the sky, undivided from space:",
    "after": "[was proclaimed] from the open sky, undivided from space:",
    "finding": "PD-T05"
  },
  {
    "pair": "DTG-000067",
    "golden": [
      "U00176",
      "U00177",
      "U00178"
    ],
    "tibetan": "དབྱེར་མི་ཕྱེད་པས་སྙོམས་ཞུགས་ཏེ། །\nརང་བཞིན་རྫོགས་པ་ཆེན་པོ་ཡི། །\nདཀྱིལ་འཁོར་གཅིག་ཏུ་ཐབས་ཅིག་འཁོད། །",
    "before": "abided together in a single maṇḍala.",
    "after": "abided together in a single mandala.",
    "finding": "PD-T06"
  },
  {
    "pair": "DTG-000069",
    "golden": [
      "U00180",
      "U00181",
      "U00182",
      "U00183"
    ],
    "tibetan": "དེ་ནས་གཅིག་དང་ཐ་མི་དད། །\nརང་བཞིན་དག་པའི་འཁོར་རྣམས་ལས། །\nལྷ་དབང་གིས་ནི་འདི་སྐད་གསོལ། །\nཨེ་མ་ཀྱེ་ཀྱེ་བཅོམ་ལྡན་འདས། །",
    "before": "‘Ema! Listen, listen, Blessed One!",
    "after": "‘Ema! O, O, Blessed One!",
    "finding": "PD-T07"
  },
  {
    "pair": "DTG-000069",
    "golden": [
      "U00180",
      "U00181",
      "U00182",
      "U00183"
    ],
    "tibetan": "དེ་ནས་གཅིག་དང་ཐ་མི་དད། །\nརང་བཞིན་དག་པའི་འཁོར་རྣམས་ལས། །\nལྷ་དབང་གིས་ནི་འདི་སྐད་གསོལ། །\nཨེ་མ་ཀྱེ་ཀྱེ་བཅོམ་ལྡན་འདས། །",
    "before": "From among the retinue whose intrinsic nature was pure,",
    "after": "from among the retinue whose intrinsic nature was pure,",
    "finding": "PD-E01"
  },
  {
    "pair": "DTG-000046",
    "golden": [
      "U00114",
      "U00115",
      "U00116"
    ],
    "tibetan": "དེ་ནས་ཆོས་ཉིད་ནམ་མཁའ་ལས། །\nཁྱབ་འཇུག་ཆེན་པོའི་གསུང་གིས་ནི། །\nབྱིན་གྱིས་རླབས་ཀྱིས་རང་སྒྲར་སྟོན། །",
    "before": "blessing displayed it as its own sound.",
    "after": "through blessing, it was displayed as its own sound.",
    "finding": "PD-S01"
  },
  {
    "pair": "DTG-000047",
    "golden": [
      "U00117",
      "U00118",
      "U00119",
      "U00120",
      "U00121",
      "U00122",
      "U00123"
    ],
    "tibetan": "དེ་ནས་ཕྱོགས་བྲལ་ནམ་མཁའ་ལས། །\nཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་ལས། །\nབསྟན་པ་ཀུན་གྱི་བཅུད་བསྡུས་པའི། །\nརྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ཉིད་ནི། །\nཚིག་རྣམས་ཀུན་གྱི་ཐོག་མར་ཡང་། །\nབརྒྱ་ཕྲག་གསུམ་དང་དྲུག་ཅུ་ཡི། །\nསྒྲ་ལས་དྲངས་ཏེ་སྟོན་པས་གསུངས། །",
    "before": "which gathers the quintessence of all teachings,\nthis very king of tantras,",
    "after": "this very king of tantras,\nwhich gathers the quintessence of all teachings,",
    "finding": "PD-S02",
    "sequence_note": "Applied after PD-T01 in the same batch; frozen input has continua at this location."
  }
]
```
<!-- /phase-d-batch-01 -->

<a id="phase-d-batch-01-nochange"></a>
**Important retentions / rejected false positives.** DTG-000008's incomplete portrait caption and DTG-000070/U00187's separation of the reported purpose variant from enlightened intent already follow the current golden source; old criticisms are not current defects. DTG-000019/U00035 is only a source-delimiter change. DTG-000020/U00039 already reads a thousand [stamens], not the historical upper-part reading. The lotus construction remains provisionally linked to N-004/G-U00039; relocating its descriptive modifiers would require settling more of that compressed construction than this repair authorizes. DTG-000025's distinguishing marks retains the canonical noun marks and a contextual descriptive adjective; a glossary substring alone is not sufficient reason to delete it. The source headings' gleng gzhi remains introductory setting, not Ground. DTG-000057's gzhi ma foundation and DTG-000092's path-continuum are not the literary rgyud/title exception. DTG-000035's longer 'od zer khyim is not proven identical to the listed 'od khyim whole expression. DTG-000067's thabs cig means together; DTG-000044's las can is not sems can. The three embodiment names and complete enjoyment component remain intact, including recognizable short forms.

<a id="phase-d-batch-01-open"></a>
**Local unresolved constructions retained, not silently approved.** The existing notes continue to carry the opening palace/instrumental and retinue groupings (N-003), realm/lotus location and numerical supply (N-004/G-U00039), the unspecified five/two (N-005), khams dang gud bcas (N-006), seventeen yang zhun (N-007), nine–two–four (N-008), the three-intent punctuation (N-009), phonological labels/numerical sets (N-010), fourteen–two and dgod (N-011), one-with-this (N-012/G-U00180), and the byer zug snyoms triad (N-014). Opening foreign strings/caption retain their exact linked qualifications. These are inherited open questions, not newly discovered defects.

Additional exact review questions: DTG-000023/U00048 རྒྱུད་འབྱུང་གླེང་གཞི (arising of the continuum) may denote this scripture's emergence, but this occurrence's scope is retained pending comparison with its later explanation; title proximity alone does not apply P1. DTG-000030/U00069 བསམ་གཏན་དང་པོར (first meditative absorption) requires the shared bsam gtan/ting nge 'dzin family distinction; meditative stability is a proposal, not a silently adopted default. In the same pair, U00070 མངོན་དུ་བྱ་དང་བྱེད་པ་བྲལ (free of manifest doing and agency) permits action/agent versus two-action analysis; no agent is inserted from the glossary alone. DTG-000042/U00101 གཞན་འབད་པ (other exertion versus others' exertion), DTG-000043/U00104 ཆོས་ཀྱི་སྐུ་ལ་ངེས་བརྒྱུད (transmission's attachment/reference), and DTG-000069/U00183 ཨེ་མ (Ema, distinct from full e ma ho) remain construction-specific questions. The following explanations, an explicit parallel, or owner-approved commentary/terminology reconciliation would settle these; retained wording is not a new book-wide default. Whole-work family checking remains pending.

**Notes/usage disposition pending integration:** N-T03's acoustic sound treatment is now approved within P1's actual acoustic scope; N-T04's cognitive thugs/awakened mind is now P2 canonical. Their historical absent/proposed statements are not current policy. N-T01's keep-continuum title instruction is superseded only by P1's literary exception; All-Penetrating Word remains proposed. N-T09's Ground capitalization is approved presentation, not automatic approval of each technical-sense parse. N-T07's short embodiment forms are recognized in their explicit three-embodiment context; no shared entry is added. N-T15's finite hold/maintain constructions are not nominal apprehending subject. Original approval history remains untouched.

<a id="phase-d-notes-01"></a>
### PD-N01 — current note-status reconciliation (recorded before application)

Severity: note-status inconsistency; confidence: high. P1/P2 supersede the earlier proposed/absent terminology statuses only within their approved scopes. The original research notes and original ten usage records remain intact. The current index and existing usage file receive dated dispositions linked to this review rather than rewritten historical approvals. The paired footer needs one explanatory paragraph because its inherited Current English quotations refer to the October 1 checkpoint, not necessarily the corrected current pair.

**Before:** no Phase D notice after `## Golden-source footnotes and endnotes` in `paired/translation.md`; no Phase D disposition for the following legacy IDs in `LEGACY-NOTES.md`; no `phase_d_dispositions` property in existing `USAGES.json`.

**After, footer paragraph:**

> These source-reconciliation notes preserve the October 1 decision evidence. Each **Current English** quotation records the English selected at that historical checkpoint; it is not a second canonical translation of the revised pair. Current corrections and terminology dispositions are recorded in the [post-translation review](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-review). Original source evidence and approval history remain unchanged.

**After, current index/usage dispositions:** N-T01: P1 requires tantra in explicit textual titles; retain the unapproved whole-expression title and foreign-script qualifications. N-T03: acoustic sound is P1-approved only in actual acoustic contexts; word and whole expressions remain distinct. N-T04: cognitive/honorific standalone thugs as awakened mind is P2-approved, not still an absent entry. N-T09: P1 Ground capitalization is approved presentation, not approval of every contextual parse. N-T07: the observed three-embodiment short forms are locally supported realizations of established whole expressions, not new shared assignments. N-T15: the observed finite holding/maintaining uses are resolved as local transitive constructions, not an extension of the nominal apprehending-subject entry.

The affected initial usages are source-linked in the index and in `USAGES.json`. Their English need not change when it already meets the adopted rule. This note correction creates no new glossary assignment and does not certify occurrences outside the reviewed range.

<!-- phase-d-findings -->

<a id="phase-d-verification"></a>
## Actual validation and repair verification

Baseline execution in this session, before any English or report edit:

| Command | Actual result |
|---|---|
| `python3 -B paired/validate.py` | FAIL: protected glossary differs from the historical release contract. |
| `python3 -B paired/validate.py --require-final` | Same pre-existing protected-glossary failure. |
| `python3 -B paired/test_paired.py` | 64 run; 63 pass, 1 error (`positive_released_corpus`, protected glossary). All 57 corruption tests pass. |
| `python3 -B paired/migrate.py --check` | FAIL: protected glossary. |
| `python3 -B paired/project.py --check` | FAIL: protected glossary. |
| `python3 -B translations/2026-09-26-full-draft/golden-review/validate_translation.py --require-final` | FAIL: protected baseline glossary. |
| `python3 -B translations/2026-09-26-full-draft/golden-review/test_translation.py` | PASS: positive case and all 36 deliberately corrupted fixtures. |
| `python3 -B translations/2026-09-26-full-draft/golden-review/build_translation.py --check` | FAIL: protected glossary. |
| `git diff --check` | PASS before edits. |
| Full pinned lineage reproduction, CSV shape and active policy hashes | PASS: all 2,660 lineage records reproduce; 283 × 8 glossary; both adopted hashes match. |

A bundled command was blocked before execution; the individual commands above were subsequently actually executed. The tests listed here are repository engineering tests, **not** execution of the standard's semantic regression specifications. At the freeze checkpoint no repair self-check had yet occurred. Subsequent batch results follow below.

**Batch 01 repair self-check (not a second independent review):** every changed clause was reread in its full Tibetan pair and necessary neighboring context. The source instruments, modifier head, speaker, numeric values, negation and relationships remain represented. In PD-S01 the passive adds no named agent; PD-S02 keeps the teacher as speaker and attaches quintessence to the text. The title and acoustic exceptions do not replace nonliterary continuum/word uses. The actual read-only integrity check passes: fixed source bytes, all 2,667 stable pair IDs/order, all 173 old note bodies and per-pair note associations. Exact replay of the 17 recorded scoped repairs reproduces every current pair payload; no unrecorded pair change is present. Current local-link check passes (684 targets). The released structural validator also passes with the current unchanged source and frozen English (5,484 golden objects); that is not release validation of revised English. Original ten usage records and legacy-index history reproduce after removing only the recorded dated additions. PD-N01 is applied in the current footer/index/usage layers. An initially bundled check/write/commit command was blocked before execution; the separate read-only check actually ran successfully. Existing signed build failures remain as reported above.

### Canonical and generated layers

`paired/translation.md` is the sole current authored English. The dated September draft and October 1 readers/JSON are historical release outputs, not separately edited current translations. `paired/MANIFEST.json` and `paired/v2/PAIR-AUDIT.json` describe the released paired import. Existing builders require exact released English and old policy inputs; rerunning them cannot silently become a post-review build. Their signed contracts, receipts and tags will not be rewritten to make revised working English appear historically signed off. Applicable builds will still be attempted and actual failures reported. Any bounded working-output integration left unsupported by the existing process will be distinguished from semantic coverage.

## Coverage versus text disposition

**Current coverage:** 100/2,667 semantic pairs reviewed (source ordinals 1–100); 2,567 remain unreviewed. **Text disposition:** in review, not ready for a whole-work acceptance claim. **Applied changed pairs:** 15 (17 scoped repairs; note-status additions counted separately). **Unresolved questions/shared proposals:** see batch records; whole-work totals not yet established. No human certification, new release, or harmonization of the other three works is claimed.

## Continuation

Continue at source-order ordinal 101, DTG-000099, after the applied and self-checked Batch 01 repairs. Keep the original Tibetan, all stable IDs/roles/formats, notes and historic releases intact. Save review progress and small explicit commits on `review/post-translation-20261005`.

---

## Historical October 1 report — preserved, not current Phase D certification

# Golden-source reconciliation — review report

**Version:** translation-golden-aligned-v1.0.0. **Golden source:** root-tantra-v1.0.0.

**Mode:** complete comparison of all original anchors and golden additions; source-impact review of every difference with relevant English/context. Unchanged-source passages retain their earlier translation rather than being certified by a new whole-corpus semantic QC.

**Preservation:** the original English draft, its raw batches and decision logs, the Tibetan golden release, and the established glossary remain unchanged. This is a separate annotated revision.

## Completed source reconciliation

All 110 changed original strings, all 18 added golden objects (including 23 main verses), all 42 uncertainty-only passages, two adjacent sentence-continuity revisions, and the Chapter 2 graphic metadata are represented in 173 endnotes. All 65 source-annotation components are retained and rendered separately.

The changed-original-anchor dispositions are: 41 English retentions with notes, 10 meaning/assembly revisions, 43 source-note relocations, and 16 non-main/joined anchors preserved through notes. Two further adjacent English units change for continuity with restored text. These are not counts of confirmed lexical errors.

## Meaningful findings

U00187 no longer treats purpose and the annotation formula as additional root content. U01803 no longer expands ya bzhi to four million after the golden release rejected the required sa/ya split. U02887 follows the selected main clause toward space while preserving smaller rig pa as an unresolved gloss/addition. U03802–U03803 exclude the smaller alternative numbers from the root. U05106 follows main yas gzhi rather than selecting the note ye gzhi.

## Retained uncertainty and limits

The printed source and interpretation are distinct. For example, stong at U00039 is the selected source reading, while a thousand [stamens] is a contextual interpretation; yas gzhi at U05106 is selected main text, while upper basis is provisional. The uplift/praise construction at U04312 is not certified here. Newly restored compressed clauses and sound forms retain explicit provisional notes.

All 72 uncertainty-bearing golden objects retain their flags in the machine edition and linked endnotes. Original omission queries are kept as source annotations, not presented as proof that restored text remains missing. The first portrait-caption line and boundary graphics are represented without invented decipherments.

This review does not alter or certify the exhaustive manuscript-comparison project, perform new scan reading, approve new glossary entries, or claim independent human palaeographic review. Validation measures preservation, coverage and internal consistency rather than a translation-accuracy percentage.

Build and check with [build_translation.py](../2026-09-26-full-draft/golden-review/build_translation.py). Validation results are recorded in VALIDATION.json.
