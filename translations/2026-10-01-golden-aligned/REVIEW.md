<a id="phase-d-review"></a>
# Post-translation review — current working text

**Task:** POST_TRANSLATION_REVIEW · **Mode:** review-and-revise · **Active continuation:** DTG-PD-20261005-Astra-02 · **Original review session:** DTG-PD-20261005-Astra-01 · **Reviewer:** GPT-6 Astra Pro, this review session, distinct from the September 26 authoring run and October 1 source-reconciliation coordinator. Review of the input is independent of those runs; checks of this session's repairs are self-checks, not a second independent review or human certification.

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
| chapter-01 | 1199 | DTG-000001 → DTG-001192 | 750 (ordinals 1–750; through DTG-000747) | In progress |
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

<a id="phase-d-batch-02"></a>
### Batch 02 — source ordinals 101–200 (DTG-000099 → DTG-000197)

All 100 pairs and 30 newly encountered attached notes were read in source order under Q1–Q9, I §8.1 and III, including necessary cross-pair context. Complete applicable glossary rows and whole-expression boundaries were checked. **Evidence was recorded before application. All 25 scoped repairs across 23 additional pairs and one source-annotation note repair are applied and self-checked.**

Repeated findings PD-T01/02/06/07 extend only to the individually checked locations below. PD-T01 at DTG-000023 is now resolved from the complete literary construction together with the text's own explanation of its two introductory settings and six-chapter body (DTG-000183–000196), not title proximity alone. DTG-000195 is followed by an explicit distinction of the tantra's title and textual exposition. The P1 correction of the source annotation at U00272 remains in its note layer, with its earlier English explicitly historical.

| Finding | Severity / confidence | Rationale |
|---|---|---|
| PD-T08 | Terminology/coverage / high for missing practice label; moderate-high for local syntax | The current question omits the established ru shan category, secret preliminary, and leaves only the separate phyed separating predicate. Restore the practice reference as the setting of that separation, retaining both members of the identified 'khor 'das compound, the interrogative instrument, and the actual predicate. N-T11's unapproved literal-only proposal cannot override the complete glossary entry. This does not declare all literal separating verbs a named practice; the later reply remains part of the cross-context self-check. |
| PD-T09 | Terminology / high | All four gnad occurrences are the explicit bodily/contemplative key-point family. P2 requires key point(s), including the direct-perception and cultivation modifiers. |
| PD-T10 | Terminology / high | P2 bem po is matter, contrasted here with rig bcas, the aware. The question still explicitly asks about that contrast. Matter denotes the non-knowing side in this construction; it does not assert immobility, death, or that karmic beings cannot have material bodies. No generic body/entity term is replaced. |
| PD-T11 | Terminology / moderate-high | The question asks about the enlightened intent of grub mtha' as the organized doctrinal system, not a list of individual propositions. Use tenet system; no numerical assertion or philosophical modifier is added. Compare the later detailed reply before closing this local classification. |
| PD-T12 | Terminology / high | Preserve both words of P2 sacred pledge and the distinct sdom pa/vow member. The latter's standalone shared assignment is not approved by this repair. |
| PD-T13 | Terminology / high for bcud; whole-construction confidence remains provisional | In the nourishment-taking question bcud is the extract/concentration family, not receptacle inhabitants. P2 quintessence replaces the unapproved vital-essence label. Keep the existing whole construction and N-T16's open instrumental/nourishment interpretation; this is not approval of that complete practice expression or a reconstruction from a falsely assumed whole entry. |
| PD-T14 | Terminology / moderate-high | Conviction is the epistemic result of the Great Perfection teaching and of its common introductory setting, distinct from the explicit faith at DTG-000146. No personal trusting relationship or confidences set is asserted here. Preserve the future context, recipient, compiler possession and purpose. |
| PD-T15 | Terminology / high | The exact snying po occurrences require core, not quintessence; both core-teaching relations and the purpose of increasing it are preserved. Bare snying in the surrounding heart/pith-instruction epithets is not automatically this complete headword. |
| PD-T16 | Terminology / high | P2 lung in the teaching epithet is transmission. Remove the old proposal's non-source adjective authoritative without changing eye-of-transmission or equating lung with wind/stagnant neutrality. |
| PD-T17 | Terminology / high | The actual coordinated extraction contrast, gathering dwangs ma and separating snyigs ma in the body, supports pure extract and residue. Preserve their distinct actions/order and attested spelling; the physical part exception is not specifically required here. This does not turn dngos ma into an extract or identify a modern substance. |


<!-- phase-d-batch-02 -->
```json
[
  {
    "pair": "DTG-000023",
    "golden": [
      "U00048",
      "U00049"
    ],
    "tibetan": "རྒྱུད་འབྱུང་གླེང་གཞི་དང་པོ་ལ། །\nལྔ་པོ་རྣམས་ཀྱི་ས་བོན་འཛིན། །",
    "before": "In the initial setting for the arising of the continuum,",
    "after": "In the initial setting for the arising of the tantra,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000107",
    "golden": [
      "U00224"
    ],
    "tibetan": "གནད་ཀྱི་འབྱུང་བ་གང་དང་གང༌། །",
    "before": "Which elements belong to the crucial points?",
    "after": "Which elements belong to the key points?",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000111",
    "golden": [
      "U00228"
    ],
    "tibetan": "རིག་བཅས་བེམ་པོའི་བྱེ་བྲག་གང༌། །",
    "before": "What distinguishes the aware from the insentient?",
    "after": "What distinguishes the aware from matter?",
    "finding": "PD-T10"
  },
  {
    "pair": "DTG-000112",
    "golden": [
      "U00229"
    ],
    "tibetan": "གནད་རྣམས་རང་བཟློག་ཐབས་གང་ལགས། །",
    "before": "What method reverses the crucial points themselves?",
    "after": "What method reverses the key points themselves?",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000113",
    "golden": [
      "U00230"
    ],
    "tibetan": "གྲུབ་མཐའ་དགོངས་པ་གང་གིས་འགྲུབ། །",
    "before": "By what is the enlightened intent of the tenets established?",
    "after": "By what is the enlightened intent of the tenet system established?",
    "finding": "PD-T11"
  },
  {
    "pair": "DTG-000123",
    "golden": [
      "U00240"
    ],
    "tibetan": "དམ་ཚིག་སྡོམ་པ་ཅི་ལྟ་བུ། །",
    "before": "What are the pledges and vows like?",
    "after": "What are the sacred pledges and vows like?",
    "finding": "PD-T12"
  },
  {
    "pair": "DTG-000126",
    "golden": [
      "U00243"
    ],
    "tibetan": "མངོན་སུམ་གནད་ལ་ཅི་ལྟར་བསྒྲེ། །",
    "before": "How is this applied to the crucial point of direct perception?",
    "after": "How is this applied to the key point of direct perception?",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000127",
    "golden": [
      "U00244"
    ],
    "tibetan": "འཁོར་འདས་རུ་ཤན་གང་གིས་ཕྱེད། །",
    "before": "By what are samsara and nirvana separated?",
    "after": "By what are cyclic existence and transcendence of sorrow separated in the secret preliminary?",
    "finding": "PD-T08 / PD-T02"
  },
  {
    "pair": "DTG-000135",
    "golden": [
      "U00252"
    ],
    "tibetan": "འཁོར་བའི་ཆུ་རྒྱུན་ཅི་ཡིས་གཅོད། །",
    "before": "By what is samsara's flowing stream cut?",
    "after": "By what is the flowing stream of cyclic existence cut?",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000136",
    "golden": [
      "U00253"
    ],
    "tibetan": "བཅུད་ཀྱིས་ལེན་པ་ཇི་ལྟ་བུ། །",
    "before": "What is the taking of nourishment from vital essences?",
    "after": "What is the taking of nourishment from quintessence?",
    "finding": "PD-T13"
  },
  {
    "pair": "DTG-000146",
    "golden": [
      "U00263",
      "U00264",
      "U00265",
      "U00266"
    ],
    "tibetan": "བདག་ལ་རིམ་པ་གསལ་ཕྱེ་བས། །\nམ་འོངས་པ་ཡི་དུས་རྣམས་སུ། །\nའདི་ལ་དད་ཅིང་འདུན་པ་ཀུན། །\nརྫོགས་ཆེན་འདི་ལ་ཡིད་ཆེས་ནས། །",
    "before": "will come to trust this Great Perfection.",
    "after": "will come to have conviction in this Great Perfection.",
    "finding": "PD-T14"
  },
  {
    "pair": "DTG-000148",
    "golden": [
      "U00268",
      "U00269"
    ],
    "tibetan": "འཁོར་བའི་ཐ་མ་ཟད་ནས་ནི། །\nམྱ་ངན་འདས་པའི་ལམ་སྣ་ཟིན། །",
    "before": "When samsara is exhausted to its very end,",
    "after": "When cyclic existence is exhausted to its very end,",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000148",
    "golden": [
      "U00268",
      "U00269"
    ],
    "tibetan": "འཁོར་བའི་ཐ་མ་ཟད་ནས་ནི། །\nམྱ་ངན་འདས་པའི་ལམ་སྣ་ཟིན། །",
    "before": "they will find the entrance to the path beyond sorrow.",
    "after": "they will find the entrance to the path of transcendence of sorrow.",
    "finding": "PD-T02"
  },
  {
    "pair": "DTG-000156",
    "golden": [
      "U00287",
      "U00288"
    ],
    "tibetan": "སངས་རྒྱས་རྣམས་ཀྱིས་མ་གསུངས་པ། །\nརྒྱུད་གཞན་ལས་ནི་ཁྱད་འཕགས་འདི། །",
    "before": "surpasses other continua.",
    "after": "surpasses other tantras.",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000157",
    "golden": [
      "U00289",
      "U00290",
      "U00291",
      "U00292"
    ],
    "tibetan": "ཁམས་གསུམ་གནས་སུ་མི་ལྡོག་ཕྱིར། །\nརབ་ཏུ་གསང་ཆེན་ངེས་པའི་བཀའ། །\nབསྟན་པའི་སྙིང་པོ་འཕེལ་དོན་དུ། །\nཐེག་པའི་ཡང་རབ་རྩེ་མོ་སྟེ། །",
    "before": "for increasing the quintessence of the teaching,",
    "after": "for increasing the core of the teaching,",
    "finding": "PD-T15"
  },
  {
    "pair": "DTG-000158",
    "golden": [
      "U00293",
      "U00294",
      "U00295",
      "U00296",
      "U00297",
      "U00298",
      "U00299"
    ],
    "tibetan": "ཆོས་ཀྱི་མེ་ལོང་དོན་གྱིས་སྡུད། །\nབཀའ་ཡི་འགྲེལ་པ་མན་ངག་སྙིང་། །\nརང་བཞིན་གསང་བ་རྫོགས་པ་ཆེ། །\nསྙིང་གི་ཏི་ཀ་ལུང་གི་མིག །\nཡང་གསང་ལྡེ་མིག་བལྟ་བའི་ཕུགས། །\nསྤྱོད་པའི་སྦྱང་ས་བསྒོམ་པའི་གནད། །\nམངལ་གྱི་རྒྱུན་གཅོད་ངན་སོང་ཕྱག །",
    "before": "the heart-commentary, the eye of authoritative transmission,",
    "after": "the heart-commentary, the eye of transmission,",
    "finding": "PD-T16"
  },
  {
    "pair": "DTG-000158",
    "golden": [
      "U00293",
      "U00294",
      "U00295",
      "U00296",
      "U00297",
      "U00298",
      "U00299"
    ],
    "tibetan": "ཆོས་ཀྱི་མེ་ལོང་དོན་གྱིས་སྡུད། །\nབཀའ་ཡི་འགྲེལ་པ་མན་ངག་སྙིང་། །\nརང་བཞིན་གསང་བ་རྫོགས་པ་ཆེ། །\nསྙིང་གི་ཏི་ཀ་ལུང་གི་མིག །\nཡང་གསང་ལྡེ་མིག་བལྟ་བའི་ཕུགས། །\nསྤྱོད་པའི་སྦྱང་ས་བསྒོམ་པའི་གནད། །\nམངལ་གྱི་རྒྱུན་གཅོད་ངན་སོང་ཕྱག །",
    "before": "the training ground of activity, the crucial point of cultivation,",
    "after": "the training ground of activity, the key point of cultivation,",
    "finding": "PD-T09"
  },
  {
    "pair": "DTG-000159",
    "golden": [
      "U00300",
      "U00301"
    ],
    "tibetan": "གསང་བ་མཆོག་གི་རྒྱུད་བཤད་ཀྱིས། །\nརྡོ་རྗེ་ཡང་འཛིན་འཁོར་རྣམས་ཉོན། །",
    "before": "I will explain the supreme secret continuum;",
    "after": "I will explain the supreme secret tantra;",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000162",
    "golden": [
      "U00307"
    ],
    "tibetan": "དེས་ན་བསྟན་པའི་སྙིང་པོ་བསྟན། །",
    "before": "Therefore I teach the quintessence of the teaching.",
    "after": "Therefore I teach the core of the teaching.",
    "finding": "PD-T15"
  },
  {
    "pair": "DTG-000163",
    "golden": [
      "U00308"
    ],
    "tibetan": "ཀྱེ་ཀྱེ་དགའ་བར་བྱེད་པས་ཟུང་། །",
    "before": "Listen, listen, Joy-Maker—take hold of this!",
    "after": "O, O, Joy-Maker—take hold of this!",
    "finding": "PD-T07"
  },
  {
    "pair": "DTG-000167",
    "golden": [
      "U00319",
      "U00320",
      "U00321",
      "U00322"
    ],
    "tibetan": " འབྱུང་བའི་དགོས་པ་འདི་ལྟ་སྟེ། །\nཆུ་ནི་དྭངས་མ་སྡུད་པ་དང་། །\nསྙིགས་མ་རྣམས་ནི་འབྱེད་པའི་ལས། །\nསོ་སོའི་ལུས་ལ་བྱེད་པས་ན། །",
    "before": "Water gathers the refined part\nand performs the activity of separating the dregs",
    "after": "Water gathers the pure extract\nand performs the activity of separating the residue",
    "finding": "PD-T17"
  },
  {
    "pair": "DTG-000178",
    "golden": [
      "U00336",
      "U00337"
    ],
    "tibetan": "འབྱུང་བཞི་དག་གི་དཀྱིལ་འཁོར་ཆེ། །\nལུས་སོགས་ གྲུབ་པའི་རྒྱུ་བྱས་ཏེ། །",
    "before": "The great maṇḍala of these four elements",
    "after": "The great mandala of these four elements",
    "finding": "PD-T06"
  },
  {
    "pair": "DTG-000187",
    "golden": [
      "U00357",
      "U00358",
      "U00359",
      "U00360"
    ],
    "tibetan": "ཐེག་གཞན་རྣམས་དང་སྒོ་བསྟུན་ཕྱིར། །\nཐུན་མོང་དག་གི་གླེང་གཞི་ཡིས། །\nསྡུད་པ་རང་གི་འཁོར་རྣམས་ལ། །\nཡིད་ཆེས་བྱ་ཕྱིར་བསྟན་པ་སྟེ། །",
    "before": "is taught to inspire trust",
    "after": "is taught to inspire conviction",
    "finding": "PD-T14"
  },
  {
    "pair": "DTG-000195",
    "golden": [
      "U00374",
      "U00375"
    ],
    "tibetan": "ཨེ་མ་རྒྱུད་དག་ངེས་འབྱུང་བ། །\nདགོངས་པ་རྣམ་པ་གཉིས་ཡིན་ཏེ། །",
    "before": "Ema! In the definite arising of the continua,",
    "after": "Ema! In the definite arising of the tantras,",
    "finding": "PD-T01"
  },
  {
    "pair": "DTG-000196",
    "golden": [
      "U00376",
      "U00377"
    ],
    "tibetan": "རིག་པ་རང་སྣང་བློ་ཅན་ལ། །\nརྒྱུད་ཀྱི་མཚན་དོན་རྣམ་ཕྱེ་སྟེ། །",
    "before": "the meaning of the continuum's title is distinguished.",
    "after": "the meaning of the tantra's title is distinguished.",
    "finding": "PD-T01"
  },
  {
    "note": "G-U00272",
    "golden": [
      "U00272"
    ],
    "source_role": "separate source annotation SCAN-CH1-LAYER-00272",
    "tibetan": "རྒྱུད་ཀྱི་ཆེ་བ་རྣམ་པར་བཀོད་པའི་བཀོད་པ",
    "before": "English: The array setting out the greatness of the continuum. This is a separate structural note, not words inside the main subject phrase.",
    "after": "English at the October 1 checkpoint (historical): The array setting out the greatness of the continuum. This is a separate structural note, not words inside the main subject phrase.\n\n    **Current source-annotation English (Phase D):** The array setting out the greatness of the tantra. This remains a separate structural note, not part of the main subject phrase. [Review evidence](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-batch-02).",
    "finding": "PD-T01 / PD-N02"
  }
]
```
<!-- /phase-d-batch-02 -->

<a id="phase-d-batch-02-dispositions"></a>
**No-change checks:** DTG-000115's generic bsgrub accomplishment is not dngos grub/spiritual accomplishment. DTG-000118/000125/000160/000193's spros constructions are not automatically the listed spros bral whole expression; their exposition/elaboration functions are retained. Viewing at DTG-000131 remains a grammatical view-family realization, not a newly introduced gaze entry. DTG-000151's mdangs/luster remains distinct from gdangs/radiance and from unreviewed gzi mdangs cases. Crucially, DTG-000176's whole 'gul 'phrig/vibrating and fluttering is already canonical; it must not be changed to 'gyu/movement by a fuzzy-form comparison. The body/limbs and solid/hollow-organ metaphor in DTG-000184–000190 remains a metaphor for this text, not a new source edition or a list of seven chapters. DTG-000192's mdo means briefly here, not the longer discourse-collection label. DTG-000159's generic vajra-holding retinue is not silently named Vajradhara. Earth supporting a foundation and wind sustaining the body are actual finite holding constructions, not the nominal apprehending-subject entry. The seventy/sixty-six source annotation and the singly displayed first-reply heading remain in their proper layers. The current sel/increases variant separation at DTG-000172 is already correct and remains qualified; no source substitution occurs.

**Inherited questions retained:** N-T43's standalone lama/guru proposal; N-T51's vow; N-T16's complete bcud kyis len pa construction (now using P2 quintessence); N-T17's rgyun/flow and separate womb-succession epithet; N-019's glen pa/simple force; N-020's sixty-limbed melody and unwritten manifestation attachment; N-021's rab gtser/disciplined; N-022's heart-commentary and sweeper epithets; N-023/G-U00316's ngang gzhi bab/settling-of-basic-condition; N-T18's compressed gradual/simultaneous audience; and N-026's audience relation remain exact, linked local treatments. Neither proposed meditative stability nor superficial replaces bsam gtan or kun rdzob globally. Ema at DTG-000155/000195 belongs with the earlier exact e ma question, not automatic e ma ho expansion.

**Additional bounded construction questions:** DTG-000174/U00331 `དགོས་པ་དྲོད་རྣམས་ཤེས་པར་བྱེད། །` is presently It makes one know its purpose in the forms of warmth. The neighboring purpose instructions favor an instructional reading, while byed permits a causative analysis; do not silently add an element as knowing-agent. DTG-000175/U00332 `རླུང་གིས་སྟོངས་དང་འདེགས་པ་དང༌། །` is presently Wind supports and lifts: the exact stongs lexical force needs a construction/lexicon parallel, not emendation to another spelling. DTG-000180/U00340 `འབྱུང་བ་ཆེན་པོ་རྒྱུ་གཅིག་པས། །` retains having a single cause, but being a single cause versus common causal origin needs comparison with the complete causal account. DTG-000181/U00342–343 `དེས་ན་དགོས་པ་རང་དང་གཞན། ། བྱ་བ་རྫོགས་པའི་དོན་ལ་མཁས། །` currently makes purposes the skilled subject; elements as the implicit subject and purposes as its complement is an alternative, but the exact attachment remains open alongside the existing golden qualification. DTG-000188/U00361 `འདུལ་གཞི་ལས་ནི་འདུལ་བྱེད་དུ། །` (Ground of training) requires a supported compound-level basis/trainee versus technical-Ground reading; capitalization alone does not resolve it. Explicit source commentary, an attested constructional parallel, or a later unambiguous internal explanation would settle these. They are retained as questions, not new shared mappings.

**Active-note reconciliation queued in this same package:** N-T11's literal-only ru shan proposal is not adopted; N-T16's vital-essence label is superseded by P2 only within its approved scope; N-T23's authoritative-transmission label is superseded by transmission; N-T50's pledge proposal by sacred pledge; and the dwangs ma/extract part of N-T65 by P2. N-T65's mdangs/gzi mdangs question remains separate. Subsequent whole-work usage integration will append current dispositions without editing original approval history. No new shared label is activated by these notes. Source-ordered review continues at ordinal 201, DTG-000198.



<a id="phase-d-resumption-02"></a>
### Resumption 02 — recovery and input verification

Active continuation identity: **DTG-PD-20261005-Astra-02**, GPT-6 Astra Pro; original Phase D reviewer/session: **DTG-PD-20261005-Astra-01**. Both are distinct from the authoring/source-reconciliation runs. The earlier 200-pair review and self-check statements are retained as that session's records, not redescribed as a fresh semantic review by this continuation.

At resumption the review branch was at `673ee0e57a93057934c9caf88fcc012794f4f71a` with four unfinished modified files. They were preserved before synchronization on `recovery/phase-d-interrupted-20261005-0728`, commit **`ced6486c83555d236e7e41ac1e854044f79ab738`**, pushed and independently matched to the remote branch ref. The review branch was then fast-forwarded to that preservation commit. No other branch/worktree, stash or tag was rewritten. Remote main remains the frozen input `fc3a443ba5987efb0b132990bf131a236fa57320`.

Resumed English input: `ced6486c83555d236e7e41ac1e854044f79ab738`; `paired/translation.md` SHA-256 `f2f2295a543a85e1e62ae438c684c531e9d82990c1fd85282507a71876e3c18b`. The full active standard and glossary were read again; AGENTS, status, handoff, decisions, local format and source provenance were reread. Recomputed source, golden JSON, policy, format/lineage hashes match the freeze table. CSV parsing confirms 283 data rows and eight columns. Exact replay of the existing 42 recorded pair operations reproduces all 2,667 current English pair payloads, with 38 changed pairs. This is a reproducibility check, not a second semantic certification. Read-only `paired/validate.py` again fails at the same pre-existing protected-glossary contract before any new English repair.

<a id="phase-d-batch-03"></a>
### Batch 03 — source ordinals 201–300

**Read coverage:** all 100 pairs DTG-000198–DTG-000297, in actual source order, with continued clauses and the 17 newly encountered legacy/reconciliation notes. Related N-026 and the five queued legacy terminology notes were reread. Current source-correction notes at U00534, U00542, U00578, U00594 and U00596 were checked before considering old criticisms. **Evidence was saved before application. All 20 scoped English operations in 19 pairs and 11 source-linked review-note insertions are now applied and self-checked.**

Repeated finding families retain their previous rationale and severity/confidence: PD-T01 literary tantra, T02 cyclic existence, T06 mandala, T09 key point, T10 matter and T16 transmission. T10 here includes the attested shortened བེམ in its explicit contrast with རིག་བཅས; this is a locally supported short form, not a new shared row.

| Finding | Evidence / minimal repair | Severity | Confidence |
|---|---|---|---|
| PD-S03 | DTG-000200 has gnad in both lines. Keep both occurrences visible while applying key point; preserve the existing passive and the following realization condition. | Medium | High |
| PD-S04 | DTG-000220 marks mkhas pa with -s, not a beneficiary marker. Represent the skilled as the agent of completing the rite, consistent with the clear mkhas pas agent at DTG-000293; add no named person. | Medium | High for the case relationship; ordinary agent/instrument nuance does not name a new referent |
| PD-S05 | DTG-000267 explicitly has drug 'das, as does the parallel distance construction at DTG-000263. Restore beyond rather than assert exactly six worlds away; retain below and do not infer an unexpressed seventh world. | Medium | High |
| PD-E02 | DTG-000296 mixes an imperative with one's/oneself. Use your/yourself for the same generic addressee; preserve both reflexive/possessive occurrences and the instruction. | Low | High |
| PD-T18 | MTshan nyid receives characteristic(s); DTG-000235/000293 do not themselves supply a definition justifying the extra defining. DTG-000198 does give the no-return/exhaustion criterion and is retained. | Low | Moderate-high; scope is these constructions, not a blanket deletion |
| PD-T19 | Standalone zhing khams in the eightfold list and thirteen-realm introduction receives realms, not buddha-fields. No materially active field metaphor or separately written qualification appears in these two expressions. | Medium | High for the default; descriptive realm-name interpretations remain provisional |
| PD-T20 | DTG-000271's by-rgyan construction receives the transparent adorn-family verb. This does not force the same technical identity on the distinct ordinary spras decorations nearby. | Low | High |
| PD-N02 | Link exact unresolved constructions and the matter/knowing qualification to this report in the commentary layer, without inserting an interpretation into root prose. | Documentation | High for link scope, no claim of resolved syntax |

<!-- phase-d-batch-03 -->
```json
[
  {
    "pair": "DTG-000198",
    "golden": [
      "U00380",
      "U00381",
      "U00382"
    ],
    "tibetan": "ཁམས་གསུམ་འཁོར་བའི་རྒྱུན་བཅད་ནས། །\nཕྱི་ཕྱིར་ལྡོག་པ་མེད་པ་ཡིས། །\nཟད་པའི་མཚན་ཉིད་ཤེས་པའོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "finding": "PD-T02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000199",
    "golden": [
      "U00383",
      "U00384"
    ],
    "tibetan": "དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །\nརྒྱུད་ཀྱི་གཞུང་རྣམས་རྣམ་ཕྱེ་སྟེ། །",
    "before": "texts of the continua",
    "after": "texts of the tantras",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000200",
    "golden": [
      "U00385",
      "U00386"
    ],
    "tibetan": "གང་ལ་གང་མོས་ངེས་པའི་གནད། །\nརེ་རེ་དག་ལ་གནད་བཙུགས་ནས། །",
    "before": "The definitive crucial point corresponding to each inclination\nis applied to each one individually.",
    "after": "The definitive key point corresponding to each inclination\nis applied as a key point to each one individually.",
    "finding": "PD-T09/PD-S03",
    "kind": "translation"
  },
  {
    "pair": "DTG-000201",
    "golden": [
      "U00387",
      "U00388"
    ],
    "tibetan": "འབྲལ་བ་མེད་པར་ཡོངས་རྟོགས་ན། །\nའཁོར་བ་དག་ལ་གནས་པ་མིན། །",
    "before": "samsara",
    "after": "cyclic existence",
    "finding": "PD-T02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000203",
    "golden": [
      "U00392",
      "U00393"
    ],
    "tibetan": "དགོངས་པའི་གནད་དོན་མན་ངག་ནི། །\nསོ་སོའི་སྐབས་དང་ཤེས་པར་བྱའོ། །",
    "before": "crucial points",
    "after": "key points",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000205",
    "golden": [
      "U00395",
      "U00396",
      "U00397",
      "U00398"
    ],
    "tibetan": "རྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ཉིད་ཀྱིས།།\nངེས་པའི་མཚན་གྱི་རྣམ་གྲངས་ལ། །\nབསྟན་ནས་རྫོགས་དོན་མན་ངག་ནི། །\nཚིག་ཙམ་ངེས་པར་བརྟགས་ཕྱེ་སྟེ། །",
    "before": "king of continua",
    "after": "king of tantras",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000206",
    "golden": [
      "U00399",
      "U00400",
      "U00401",
      "U00402"
    ],
    "tibetan": "འབྲུ་རྣམས་དོན་དང་མཐུན་པར་ཡང༌། །\nདོན་གྱི་ངོ་ལ་འདི་ལྟར་སྐྱེལ། །\nསྒྲ་ཡི་བརྗོད་པ་འདི་ལྟ་བུ། །\nརྒྱུད་རྣམས་གཞན་དུ་མ་བཤད་པས། །",
    "before": "other continua",
    "after": "other tantras",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000220",
    "golden": [
      "U00439"
    ],
    "tibetan": "མཁས་པས་ཆོ་ག་རྫོགས་པའོ། །",
    "before": "For the skilled, the rite is complete.",
    "after": "The rite is completed by the skilled.",
    "finding": "PD-S04",
    "kind": "translation"
  },
  {
    "pair": "DTG-000225",
    "golden": [
      "U00455",
      "U00456",
      "U00457",
      "U00458",
      "U00459",
      "U00460",
      "U00461"
    ],
    "tibetan": "འདས་དང་མ་འོངས་ད་ལྟར་གྱི། །\nསྟོན་པ་སངས་རྒྱས་བཅོམ་ལྡན་འདས། །\nདབྱངས་གཅིག་གིས་ནི་དཀྱིལ་འཁོར་དུ། །\nསྐལ་བ་ཅན་གྱི་སྣང་བ་ལ། །\nདབང་པོ་དྲུག་གི་རྣམ་དག་པས། །\nབཅུ་བཅུ་ཡི་ནི་སྐུ་གསུམ་ལས། །\nཁྱད་པར་སྤྲུལ་པའི་སྐུ་ལས་འཕྲོས། །",
    "before": "maṇḍala",
    "after": "mandala",
    "finding": "PD-T06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000234",
    "golden": [
      "U00481",
      "U00482",
      "U00483",
      "U00484"
    ],
    "tibetan": "འབྱུང་བ་ལྔ་ལ་སྤྱོད་ནུས་དང༌། །\nམཚོན་དང་དུག་ལས་རྒྱལ་བ་དང༌། །\nབེམ་དང་རིག་བཅས་སྒྲ་རྣམས་དང༌། །\nབརྡའ་དང་ཐ་སྙད་ལ་མཁས་འགྱུར། །",
    "before": "the sounds of the insentient and the aware",
    "after": "the sounds of matter and the aware",
    "finding": "PD-T10",
    "kind": "translation"
  },
  {
    "pair": "DTG-000235",
    "golden": [
      "U00485",
      "U00486"
    ],
    "tibetan": "མདོར་ན་དགོས་པའི་བསྟན་བཅོས་དང༌། །\nབཀའ་ཡི་མཚན་ཉིད་ཤེས་པར་འགྱུར། །",
    "before": "defining characteristics",
    "after": "characteristics",
    "finding": "PD-T18",
    "kind": "translation"
  },
  {
    "pair": "DTG-000240",
    "golden": [
      "U00493",
      "U00494",
      "U00495",
      "U00496",
      "U00497"
    ],
    "tibetan": "ཐལ་བའི་གནས་ནི་རྣམ་པ་བརྒྱད། །\nའཇིག་རྟེན་ཁམས་དང་ཞིང་ཁམས་དང་། །\nདམ་བཅའ་སྐྱོན་དང་སྐྱོན་གནས་དང་། །\nའཕེན་པའི་ལས་དང་སྦྱོར་བ་དང་། །\nགྲགས་དང་སོང་བའི་གནད་དང་བརྒྱད། །",
    "before": "buddha-fields",
    "after": "realms",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000240",
    "golden": [
      "U00493",
      "U00494",
      "U00495",
      "U00496",
      "U00497"
    ],
    "tibetan": "ཐལ་བའི་གནས་ནི་རྣམ་པ་བརྒྱད། །\nའཇིག་རྟེན་ཁམས་དང་ཞིང་ཁམས་དང་། །\nདམ་བཅའ་སྐྱོན་དང་སྐྱོན་གནས་དང་། །\nའཕེན་པའི་ལས་དང་སྦྱོར་བ་དང་། །\nགྲགས་དང་སོང་བའི་གནད་དང་བརྒྱད། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000243",
    "golden": [
      "U00503",
      "U00504",
      "U00505",
      "U00506"
    ],
    "tibetan": "ཞིང་ཁམས་རྣམ་པ་བཅུ་གསུམ་ལ། །\nའདི་ནས་འཇིག་རྟེན་འོག་ན་ནི། །\nཐལ་བའི་དབྱངས་ཞེས་བྱ་བའི་ཡུལ། །\nརྒྱ་ཁྱོན་དཔག་དཀའ་རབ་ཏུ་མཛེས། །",
    "before": "buddha-fields",
    "after": "realms",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000267",
    "golden": [
      "U00560",
      "U00561"
    ],
    "tibetan": "འདི་ནས་འཇིག་རྟེན་ལྷོ་ནུབ་གཡས། །\nདྲུག་འདས་འོག་ན་ཐལ་བའི་རླུང་། །",
    "before": "six worlds away and below",
    "after": "beyond six worlds and below",
    "finding": "PD-S05",
    "kind": "translation"
  },
  {
    "pair": "DTG-000271",
    "golden": [
      "U00567",
      "U00568",
      "U00569",
      "U00570",
      "U00571"
    ],
    "tibetan": "དེ་སྟེང་བཅུ་གསུམ་བརྩེགས་པ་ན། །\nརིན་ཆེན་ཐལ་བ་ཞེས་བྱ་ན། །\nབཀྲ་ཤིས་ཉི་མ་རྣམས་ཀྱིས་སྤྲས། །\nའདོད་པའི་ཡོན་ཏན་རྣམས་ཀྱིས་བརྒྱན། །\nའཕྲུལ་གྱི་རི་མོ་ཡི་གེ་མཛེས། །",
    "before": "ornamented with",
    "after": "adorned with",
    "finding": "PD-T20",
    "kind": "translation"
  },
  {
    "pair": "DTG-000281",
    "golden": [
      "U00595"
    ],
    "tibetan": "སྟོན་པའི་བསྟན་པ་ལུང་གིས་བསྐོར། །",
    "before": "authoritative transmissions",
    "after": "transmissions",
    "finding": "PD-T16",
    "kind": "translation"
  },
  {
    "pair": "DTG-000285",
    "golden": [
      "U00601",
      "U00602",
      "U00603"
    ],
    "tibetan": "རང་འདོད་ངེས་པར་སྐྱོལ་བ་ནི། །\nལུང་དང་རིགས་པ་མན་ངག་གིས། །\nསྐྱོན་བསལ་བསྒྲུབ་དང་འགལ་བ་སྤང་། །",
    "before": "authoritative transmission",
    "after": "transmission",
    "finding": "PD-T16",
    "kind": "translation"
  },
  {
    "pair": "DTG-000293",
    "golden": [
      "U00612"
    ],
    "tibetan": "མཁས་པས་མཚན་ཉིད་རྫོགས་ཀྱིས་སྦྱར། །",
    "before": "defining characteristics",
    "after": "characteristics",
    "finding": "PD-T18",
    "kind": "translation"
  },
  {
    "pair": "DTG-000296",
    "golden": [
      "U00615"
    ],
    "tibetan": "རང་སྐྱོན་རང་གིས་ཤེས་བྱས་ལ། །",
    "before": "Know one's own faults oneself.",
    "after": "Know your own faults yourself.",
    "finding": "PD-E02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000199",
    "golden": [
      "U00383",
      "U00384"
    ],
    "tibetan": "དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །\nརྒྱུད་ཀྱི་གཞུང་རྣམས་རྣམ་ཕྱེ་སྟེ། །",
    "before": "For conceptual minds that focus on objects,\nthe texts of the tantras are distinguished.\n\nEarlier notes: [N-026](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-026).",
    "after": "For conceptual minds that focus on objects,\nthe texts of the tantras are distinguished.\n\nEarlier notes: [N-026](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-026).\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-01).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000227",
    "golden": [
      "U00464",
      "U00465"
    ],
    "tibetan": "གནས་དང་འབྱེད་དང་གནས་བཅུད་ཡུལ། །\nཐོབ་ཅིང་མཐོང་རྟོགས་ངེས་འཇུག་པའོ། །",
    "before": "The sites, distinctions, and domains of their vital cores [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029)\nare attained, and one assuredly enters seeing and realization.\n\nEarlier notes: [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029).",
    "after": "The sites, distinctions, and domains of their vital cores [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029)\nare attained, and one assuredly enters seeing and realization.\n\nEarlier notes: [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029).\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-02).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000238",
    "golden": [
      "U00491"
    ],
    "tibetan": "རྒྱུད་ལ་ངེས་པའི་འཕྲུལ་འབྱེད་ཕྱེ། །",
    "before": "The distinguishing magic definitive for the continuum is set apart.",
    "after": "The distinguishing magic definitive for the continuum is set apart.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-03).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000248",
    "golden": [
      "U00519",
      "U00520",
      "U00521"
    ],
    "tibetan": "འོད་དང་ཁ་དོག་ངེས་གསལ་ཞིང་། །\nསྟོན་པའི་བསྟན་པ་འདུལ་བའི་ཞིང་། །\nསོ་སོའི་ལས་དང་མཚན་བཅས་པའོ། །",
    "before": "Its light and colors are definitely clear;\nit is a field where the teacher's teaching trains beings,\neach with their own karma and characteristics.",
    "after": "Its light and colors are definitely clear;\nit is a field where the teacher's teaching trains beings,\neach with their own karma and characteristics.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-04).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000252",
    "golden": [
      "U00529",
      "U00530"
    ],
    "tibetan": "སྟོན་པའི་བསྟན་པ་འདུ་མཆེད་རྒྱས། །\nབསྐལ་པ་རྫོགས་པས་ཐལ་ཞེས་བྱའོ། །",
    "before": "The sources of the teacher's teaching expand;\nwith the age complete, it is called Penetration.",
    "after": "The sources of the teacher's teaching expand;\nwith the age complete, it is called Penetration.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-05).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000258",
    "golden": [
      "U00543"
    ],
    "tibetan": "སྒྲ་དབྱངས་སྣ་ཚོགས་འབྱུང་བའི་གཞི། །",
    "before": "It is the Ground from which diverse sounds and melodies arise.",
    "after": "It is the Ground from which diverse sounds and melodies arise.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-06).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000244",
    "golden": [
      "U00507",
      "U00508",
      "U00509",
      "U00510"
    ],
    "tibetan": "རྒྱུ་དང་རྐྱེན་དང་རང་བཞིན་དང༌། །\nསྟོན་པའི་བསྟན་པ་དེ་ཡི་འཁོར། །\nསྟེང་དང་འོག་དང་ཕྱོགས་མཚམས་སུ། །\nཆུ་ཞེང་ཉམས་དགའ་བཀོད་ལེགས་སྤྲས། །",
    "before": "Its causes, conditions, and intrinsic nature,\nthe teacher's teaching and its retinue,\nabove, below, and in the directions and intermediate directions—\nits length and breadth are pleasing, well-arrayed and adorned.\n\nEarlier notes: [N-032](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-032).",
    "after": "Its causes, conditions, and intrinsic nature,\nthe teacher's teaching and its retinue,\nabove, below, and in the directions and intermediate directions—\nits length and breadth are pleasing, well-arrayed and adorned.\n\nEarlier notes: [N-032](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-032).\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-07).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000276",
    "golden": [
      "U00587",
      "U00588"
    ],
    "tibetan": "སྟོན་པ་ཉིད་དང་བསྟན་པ་དང་། །\nདེ་ཡི་འཁོར་དང་ལོངས་སྤྱོད་རྫོགས། །",
    "before": "The teacher and the teaching,\nits retinue and enjoyments, are complete.",
    "after": "The teacher and the teaching,\nits retinue and enjoyments, are complete.\n\nReview note: [Construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q03-07).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000207",
    "golden": [
      "U00403"
    ],
    "tibetan": "ཨེ་མ་ངོ་མཚར་ཆེ་བ་ཉིད། །",
    "before": "Ema! How greatly wonderful!",
    "after": "Ema! How greatly wonderful!\n\nReview note: [Short exclamation remains provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-batch-03-dispositions).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000111",
    "golden": [
      "U00228"
    ],
    "tibetan": "རིག་བཅས་བེམ་པོའི་བྱེ་བྲག་གང༌། །",
    "before": "What distinguishes the aware from matter?",
    "after": "What distinguishes the aware from matter?\n\nReview note: [Matter and awareness](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-matter-note).",
    "finding": "PD-N02",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000234",
    "golden": [
      "U00481",
      "U00482",
      "U00483",
      "U00484"
    ],
    "tibetan": "འབྱུང་བ་ལྔ་ལ་སྤྱོད་ནུས་དང༌། །\nམཚོན་དང་དུག་ལས་རྒྱལ་བ་དང༌། །\nབེམ་དང་རིག་བཅས་སྒྲ་རྣམས་དང༌། །\nབརྡའ་དང་ཐ་སྙད་ལ་མཁས་འགྱུར། །",
    "before": "One can act upon the five elements,\nprevails over weapons and poison,\nand becomes skilled in the sounds of matter and the aware,\nin signs and conventions.\n\nEarlier notes: [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).",
    "after": "One can act upon the five elements,\nprevails over weapons and poison,\nand becomes skilled in the sounds of matter and the aware,\nin signs and conventions.\n\nEarlier notes: [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).\n\nReview note: [Matter and awareness](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-matter-note).",
    "finding": "PD-N02",
    "kind": "review-link"
  }
]
```
<!-- /phase-d-batch-03 -->

<a id="phase-d-batch-03-dispositions"></a>
**Important no-change cases:** DTG-000214's personal continuum is not a tantra title. DTG-000221/000237 preserve the established word-and-meaning compound despite neighboring acoustic sound passages; the five acoustic occasions and water sounds support sound in their own constructions. DTG-000202's accomplishment is bsgrub, not dngos grub. DTG-000216's rnam shes is a finite knowing construction, not mechanically the consciousness noun. DTG-000230's body of Vajradhara preserves lus, not an invented embodiment; its proper name is the approved rdo rje 'chang. DTG-000261 already retains object of focus and intrinsic nature. The complete sources do not authorize turning all ordinary moving/decorating verbs into technical glossary nouns. The numerical schemes and logical imagery remain literal and ordered: no four reasons are changed to three; DTG-000292 and DTG-000297 deliberately preserve their different source orders for assertion/proof/reason. The already separated pleasant-region and naga-face variant notes are not current source-layer defects. No empty graphic or missing passage is fabricated.

**Retained linked questions:** N-027's All-Pervader numbers/side-locks/grouping; N-028's hero/hero-goer, neutral member and counts; N-029's six/tens/three and compact final list; N-030's technical-science/archery/thal-yig treatment; N-031's eightfold parsing; N-032's thirteen ordered names, relative directions and opaque counts; N-034's lda-ldi, mer mer po and awnings; and N-036's proof/fortress/wheel relation remain open. The thirteen introduced names were read in order from Melody of Penetration through Star Penetration; descriptive English names, including Sound of Penetration, are not newly approved proper-name defaults. N-T19 higher knowing and N-T21 logical consequence remain shared-label proposals; the logical construction at DTG-000291 is locally supported by assertions, reasons and debate, not a global replacement of penetration. Exact short ཨེ་མ at DTG-000207 continues the existing short-exclamation question (DTG-000069/000155/000195); it is not silently expanded to ཨེ་མ་ཧོ or assigned that whole-expression default.

<a id="phase-d-matter-note"></a>
**Matter and awareness:** At DTG-000111 and DTG-000234 the approved matter label denotes the material/non-knowing side of the stated contrast with the aware. It does not mean immobile/dead, does not assert that karmic beings lack material bodies, and does not replace every body, entity or being expression. Elemental sounds in the surrounding account make the sound-of-matter construction intelligible without adding insentient to the technical label.

<a id="pd-q03-01"></a>
#### PD-Q03-01 — The dmigs pas / yul gyi blo audience construction

Retain the linked N-026 working construction rather than force object of focus into an unparsed clause. The instrumental/relational function of དམིགས་པས and its connection to ཡུལ་གྱི་བློ require resolution. Nominal object-of-focus versus a finite focusing construction remains open; the clear literary tantra repair does not settle it. A constructional parallel or an explicit explanation of the two contrasted audiences would settle the attachment.

**DTG-000199 / U00383 U00384**

Tibetan: `དམིགས་པས་ཡུལ་གྱི་བློ་རྣམས་ལ། །` / `རྒྱུད་ཀྱི་གཞུང་རྣམས་རྣམ་ཕྱེ་སྟེ། །`

English before this batch (provisional):

> For conceptual minds that focus on objects,
> the texts of the continua are distinguished.

<a id="pd-q03-02"></a>
#### PD-Q03-02 — gnas bcud yul and the scope of bcud

N-029's vital cores is not a newly approved label. Quintessence is approved only in its recorded scope; contents/inhabitants is a different authorized construction. The compact གནས་བཅུད་ཡུལ does not yet establish which relation/sense applies. Retain the existing linked provisional list, not a reconstruction from components. A referent-identifying explanation of the sites, distinctions and domains would settle this.

**DTG-000227 / U00464 U00465**

Tibetan: `གནས་དང་འབྱེད་དང་གནས་བཅུད་ཡུལ། །` / `ཐོབ་ཅིང་མཐོང་རྟོགས་ངེས་འཇུག་པའོ། །`

English before this batch (provisional):

> The sites, distinctions, and domains of their vital cores [N-029](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-029)
> are attained, and one assuredly enters seeing and realization.

<a id="pd-q03-03"></a>
#### PD-Q03-03 — rgyud in the concluding magic clause

Retain continuum provisionally. Unlike the explicit texts/titles at DTG-000199/000205/000206, this clause can concern either an individual's continuum or this tantra's distinctive efficacy. Proximity to a title is insufficient under P1. An unambiguous referent or internal parallel would settle it.

**DTG-000238 / U00491**

Tibetan: `རྒྱུད་ལ་ངེས་པའི་འཕྲུལ་འབྱེད་ཕྱེ། །`

English before this batch (provisional):

> The distinguishing magic definitive for the continuum is set apart.

<a id="pd-q03-04"></a>
#### PD-Q03-04 — Training field, implied beings and possession

The working English makes the teaching train beings and assigns individual karma/characteristics to them. The source instead compactly juxtaposes the teacher's teaching, a training field, and individual las/mtshan. Beings are not overtly named. A nominal training-field description and attachment of las/mtshan to the field/teaching are alternatives. Retain only as a visibly linked provisional construction; do not silently invent a new agent or substitute discipline as a textual-category label. An explicit constructional parallel for the repeated realm descriptions would settle the subject and modifiers.

**DTG-000248 / U00519 U00520 U00521**

Tibetan: `འོད་དང་ཁ་དོག་ངེས་གསལ་ཞིང་། །` / `སྟོན་པའི་བསྟན་པ་འདུལ་བའི་ཞིང་། །` / `སོ་སོའི་ལས་དང་མཚན་བཅས་པའོ། །`

English before this batch (provisional):

> Its light and colors are definitely clear;
> it is a field where the teacher's teaching trains beings,
> each with their own karma and characteristics.

<a id="pd-q03-05"></a>
#### PD-Q03-05 — The exact expanded form du mched

The English sources treats འདུ་མཆེད as a nominal source-expression. Gathering/proliferation or another complete construction is not excluded by the present clause. No spelling change to another headword, component-built glossary equivalent, or independently approved source-family default is justified. A lexical/constructional parallel or later explicit explanation would settle this; retain the working treatment as provisional.

**DTG-000252 / U00529 U00530**

Tibetan: `སྟོན་པའི་བསྟན་པ་འདུ་མཆེད་རྒྱས། །` / `བསྐལ་པ་རྫོགས་པས་ཐལ་ཞེས་བྱའོ། །`

English before this batch (provisional):

> The sources of the teacher's teaching expand;
> with the age complete, it is called Penetration.

<a id="pd-q03-06"></a>
#### PD-Q03-06 — Technical Ground versus a support/origin

The described realm is the གཞི from which sounds and melodies arise. P1 approves capitalization only for an identified technical Ground; it does not decide this support/origin construction. Retain the current capitalized wording provisionally, not as proof of that identification. An explicit identification with the technical Ground or a clear ordinary-support parallel would settle the case.

**DTG-000258 / U00543**

Tibetan: `སྒྲ་དབྱངས་སྣ་ཚོགས་འབྱུང་བའི་གཞི། །`

English before this batch (provisional):

> It is the Ground from which diverse sounds and melodies arise.

<a id="pd-q03-07"></a>
#### PD-Q03-07 — The possessor in de yi khor

The repeated དེ་ཡི་འཁོར follows teacher/teaching descriptions. Its can refer to the realm or teaching in English, while his/the teacher's is another possible construal. Tibetan de yi alone does not resolve the antecedent. Do not silently impose a personal possessor merely because it is more conventional. Retain with N-032 and this question until a clear antecedent or parallel settles it.

**DTG-000244 / U00507 U00508 U00509 U00510**

Tibetan: `རྒྱུ་དང་རྐྱེན་དང་རང་བཞིན་དང༌། །` / `སྟོན་པའི་བསྟན་པ་དེ་ཡི་འཁོར། །` / `སྟེང་དང་འོག་དང་ཕྱོགས་མཚམས་སུ། །` / `ཆུ་ཞེང་ཉམས་དགའ་བཀོད་ལེགས་སྤྲས། །`

English before this batch (provisional):

> Its causes, conditions, and intrinsic nature,
> the teacher's teaching and its retinue,
> above, below, and in the directions and intermediate directions—
> its length and breadth are pleasing, well-arrayed and adorned.

**DTG-000276 / U00587 U00588**

Tibetan: `སྟོན་པ་ཉིད་དང་བསྟན་པ་དང་། །` / `དེ་ཡི་འཁོར་དང་ལོངས་སྤྱོད་རྫོགས། །`

English before this batch (provisional):

> The teacher and the teaching,
> its retinue and enjoyments, are complete.

<a id="phase-d-notes-02"></a>
**Queued note-status reconciliation:** append, without rewriting historical proposals, the current dispositions for N-T11 (retain secret preliminary and the separate phyed predicate at DTG-000127; later reply still to be checked), N-T16 (P2 quintessence in the nourishment context, whole bcud kyis len pa construction still provisional), N-T23 (P2 transmission without unsupported authoritative), N-T50 (P2 sacred pledge, distinct from sdom pa), and N-T65 (P2 pure extract/residue in the reviewed elemental contrast, without settling mdangs/gzi mdangs). These are policy applications in recorded occurrences, not local new shared assignments. The five current dispositions are now appended in LEGACY-NOTES.md and USAGES.json; the historical source notes/proposals remain unchanged.


<a id="phase-d-batch-04"></a>
### Batch 04 — source ordinals 301–450; bounded return to DTG-000188

**Read coverage:** all 150 pairs DTG-000298–DTG-000447, in source order, with the full current source/English, continued sentences, and all 21 newly encountered notes. N-T20 and N-T22 were also read in full. DTG-000187–000189 were reread on returning to the earlier training-basis question. **Evidence checkpoint: the following 20 English operations in 20 pairs and six review-link insertions are recorded before application; application and self-check are pending.**

Repeated terminology families retain their established batch rationale: T01 literary tantra (the text is explicitly read), T02 cyclic existence, T04 full spiritual accomplishment in a transparent descriptive name, T09 key point, T12 sacred pledge (distinct from vows), T18 characteristic without an unprovided definition, and T19 realm. Proper-name repairs preserve the descriptive construction and all modifiers; they do not assert a historical identification or a new canonical whole-name entry. E02 continues the narrowly grammatical imperative-addressee repair without changing the source's position or its possessor.

| Finding | Evidence and scope | Severity | Confidence |
|---|---|---|---|
| PD-S06 | The bodily/training basis at DTG-000322/000351 is explicitly the changing elemental body/five aggregates; DTG-000352 refers back to that basis. DTG-000354 explains the introductory setting's five aspects, not a new assertion that the technical Ground has five constituents. Use ordinary basis, retaining the source wordplay in a linked note. Apply the supported training-basis reading retrospectively to DTG-000188; its broader arising-as-trainer relationship remains provisional. | Medium, sense/attachment control | Moderate-high for these basis referents; not certification of the whole earlier clause |
| PD-T21 | Restore the meaningful ordinary component in the cognitive sems phrases at DTG-000398 and DTG-000426. Neither is the established wind-mind compound or the approved karmic-being entry. Keep the explicit loving/virtuous modifiers. | Medium, lexical component | High |
| PD-T22 | P2 now assigns nominal dngos po to entity, not the older contextual proposal actual presence. DTG-000441 explicitly counts three and does not separately say actual. Apply entities while retaining embodiment, speech, awakened mind, the recipient and effortless result. The precise represented referents remain N-048's question. | Medium, adopted terminology | High for the scoped label; ritual referents remain provisional |
| PD-N03 | Link the precise tenets/construction question and ordinary-basis interpretation in the commentary layer. No source role, metadata or root segmentation changes. | Documentation | High for location/link scope |

<!-- phase-d-batch-04 -->
```json
[
  {
    "pair": "DTG-000299",
    "golden": [
      "U00621",
      "U00622",
      "U00623"
    ],
    "tibetan": "སྒྲ་དོན་བརྗོད་བྱའི་ཚིག་ཙམ་ལས། །\nའབྲེལ་དང་འབྲེལ་མེད་མཚན་ཉིད་ཀྱིས། །\nཁྱབ་བྱའི་དོན་རྣམས་ཐལ་འགྱུར་བརྩིའོ། །",
    "before": "defining characteristics",
    "after": "characteristics",
    "finding": "PD-T18",
    "kind": "translation"
  },
  {
    "pair": "DTG-000307",
    "golden": [
      "U00633"
    ],
    "tibetan": "སྦྱོར་བའི་དམིགས་ཀྱིས་རང་འདོད་བསྐྱང༌། །",
    "before": "maintain one's own position",
    "after": "maintain your own position",
    "finding": "PD-E02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000322",
    "golden": [
      "U00664",
      "U00665"
    ],
    "tibetan": "རླུང་ས་མེ་ཆུ་ཆ་ལྔ་ལས། །\nའགྱུར་ཞིང་བྱེད་པ་ལུས་ཀྱི་གཞི། །",
    "before": "body's Ground",
    "after": "body's basis",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000329",
    "golden": [
      "U00681",
      "U00682",
      "U00683"
    ],
    "tibetan": "གླེང་གཞིར་བཅས་པས་གཞི་བཟུང་སྟེ། །\nགནད་འདུས་བཀོད་པ་སེམས་ཀྱི་རྟེན། །\nརང་ཐོག་འབེབས་པ་གཉིས་པ་ཡིན། །",
    "before": "Crucial Points",
    "after": "Key Points",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000333",
    "golden": [
      "U00689",
      "U00690"
    ],
    "tibetan": "ལྔ་པ་བལྟ་བསྒོམ་བཀོད་པ་སྟེ། །\nབྱ་བྲལ་རྫོགས་པ་དབྱིངས་ཀྱི་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000337",
    "golden": [
      "U00696",
      "U00697",
      "U00698",
      "U00699",
      "U00700"
    ],
    "tibetan": "དཔལ་གྱི་དགོངས་པ་འབྱུང་བའི་གཏེར། །\nབདེ་བ་ཐབས་ཀྱི་སྐུ་ཉིད་ཀྱང༌། །\nལུང་བསྟན་རྗེས་འཛིན་སེམས་ཀྱི་གནད། །\nའགྲོ་བ་བདག་སྐྱོབ་རླུང་གི་ལྷ། །\nལྷག་མ་ཉིད་ཀྱང་དེ་ཙམ་མོ། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000348",
    "golden": [
      "U00719"
    ],
    "tibetan": "དབང་དང་དམ་ཚིག་སྡོམ་པ་རྫོགས། །",
    "before": "pledges",
    "after": "sacred pledges",
    "finding": "PD-T12",
    "kind": "translation"
  },
  {
    "pair": "DTG-000188",
    "golden": [
      "U00361",
      "U00362"
    ],
    "tibetan": "འདུལ་གཞི་ལས་ནི་འདུལ་བྱེད་དུ། །\nབྱུང་བས་བསྟན་པ་གནས་པར་བྱེད། །",
    "before": "Ground of training",
    "after": "basis of training",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000351",
    "golden": [
      "U00722",
      "U00723",
      "U00724"
    ],
    "tibetan": "གླེང་གཞི་དག་ལ་ཡང་དག་ཚིག །\nགདུལ་བྱ་གང་ཟག་སོ་སོ་ལ། །\nགདུལ་གཞི་ཕུང་པོ་རྣམ་པ་ལྔ། །",
    "before": "Ground of training",
    "after": "basis of training",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000352",
    "golden": [
      "U00725"
    ],
    "tibetan": "དེ་ཡི་འདུལ་བྱེད་གླེང་གཞི་སྟེ། །",
    "before": "that Ground",
    "after": "that basis",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000354",
    "golden": [
      "U00727"
    ],
    "tibetan": "གཞི་ནི་རྣམ་པ་ལྔ་ཡིན་ཏེ། །",
    "before": "‘Ground’",
    "after": "‘Basis’",
    "finding": "PD-S06",
    "kind": "translation"
  },
  {
    "pair": "DTG-000373",
    "golden": [
      "U00783",
      "U00784",
      "U00785",
      "U00786"
    ],
    "tibetan": "དེ་ཡི་ཡོན་བདག་ཁྱིམ་བདག་རིགས། །\nདགེ་བའི་དངོས་གྲུབ་ཅེས་བྱ་བས། །\nབསྟན་པ་དམ་པ་འདི་ཉིད་ནི། །\nལོ་བརྒྱའི་བར་ལ་གནས་པར་བྱེད། །",
    "before": "Accomplishment of Virtue",
    "after": "Spiritual Accomplishment of Virtue",
    "finding": "PD-T04",
    "kind": "translation"
  },
  {
    "pair": "DTG-000398",
    "golden": [
      "U00838",
      "U00839",
      "U00840",
      "U00841",
      "U00842",
      "U00843"
    ],
    "tibetan": "སྟོང་དང་སུམ་བརྒྱ་འདས་འོག་ཏུ། །\nཡང་ནི་འཛམ་གླིང་བྱང་གི་ངོས། །\nགཟི་བརྗིད་ལྡན་པའི་རི་ཡི་རྩེར། །\nདགེ་སློང་གཟུགས་ལ་བྱམས་སེམས་བྲལ། །\nགཡས་པ་ལ་ནི་རྣ་བ་གཉིས། །\nམིག་ནི་ཟུར་གསུམ་མས་ཡར་འགེབ། །",
    "before": "loving mind",
    "after": "loving ordinary mind",
    "finding": "PD-T21",
    "kind": "translation"
  },
  {
    "pair": "DTG-000421",
    "golden": [
      "U00906",
      "U00907"
    ],
    "tibetan": "དེ་ནས་མཛེས་ལྡན་བཀོད་པ་ཡི། །\nཞིང་ཁམས་དག་ཏུ་ངེས་འཕར་ནས། །",
    "before": "field of Beautiful Array",
    "after": "realm of Beautiful Array",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000426",
    "golden": [
      "U00919",
      "U00920",
      "U00921"
    ],
    "tibetan": "ཐམས་ཅད་བྱང་ཆུབ་སེམས་ཆེན་པོ། །\nམི་སྐྱེའི་ཆོས་ལ་བཟོད་ཐོབ་སྟེ། །\nདགེ་བའི་སེམས་ལྡན་འབའ་ཞིག་འབྱུང་། །",
    "before": "virtuous minds",
    "after": "virtuous ordinary minds",
    "finding": "PD-T21",
    "kind": "translation"
  },
  {
    "pair": "DTG-000430",
    "golden": [
      "U00929",
      "U00930",
      "U00931"
    ],
    "tibetan": "དེ་འོག་གཙུག་ཕུད་དབྱངས་ལྡན་པའི། །\nའཇིག་རྟེན་ཁམས་ནི་ཡངས་པར་ནི། །\nསྟོན་པ་མཐའ་ཡས་འཁོར་བ་འཇིག །",
    "before": "Samsara",
    "after": "Cyclic Existence",
    "finding": "PD-T02",
    "kind": "translation"
  },
  {
    "pair": "DTG-000441",
    "golden": [
      "U00955",
      "U00956",
      "U00957"
    ],
    "tibetan": "སྐུ་གསུང་ཐུགས་ཀྱི་དངོས་པོ་གསུམ། །\nསུ་ལ་བབ་པ་འབད་མེད་པར། །\nགདོན་མི་ཟ་བའི་སངས་རྒྱས་ཐོབ། །",
    "before": "actual presences",
    "after": "entities",
    "finding": "PD-T22",
    "kind": "translation"
  },
  {
    "pair": "DTG-000442",
    "golden": [
      "U00958",
      "U00959",
      "U00960",
      "U00961"
    ],
    "tibetan": "དེ་ཕྱིར་བྱིན་གྱིས་རླབས་ཀྱི་གནད། །\nགསུང་གི་སྤྲུལ་པ་ཉིད་ལས་ཀྱང༌། །\nསྟོན་པའི་ཁ་དོག་ལེགས་བྲིས་ནས། །\nམཆན་ཁུང་གཡོན་དུ་བཏགས་བྱས་ཏེ། །",
    "before": "crucial point",
    "after": "key point",
    "finding": "PD-T09",
    "kind": "translation"
  },
  {
    "pair": "DTG-000444",
    "golden": [
      "U00964",
      "U00965"
    ],
    "tibetan": "རྒྱུད་འདི་སུས་ནི་རྟག་བཀླགས་ན། །\nདེས་ཀྱང་གོང་མ་བཞིན་དུ་འགྱུར། །",
    "before": "this continuum",
    "after": "this tantra",
    "finding": "PD-T01",
    "kind": "translation"
  },
  {
    "pair": "DTG-000445",
    "golden": [
      "U00966",
      "U00967",
      "U00968",
      "U00969",
      "U00970"
    ],
    "tibetan": "བཀའ་གསང་ངེས་པ་བཅུ་བདུན་དང་། །\nབསྟན་པའི་གཟེར་དང་འཕྲུལ་ཡིག་བཅས། །\nསྤྲུལ་སྐུའི་ཞིང་ཁམས་ཐོག་མ་ལ། །\nསྟོན་པ་ཀུན་ཏུ་བཟང་པོ་ཡིས། །\nསྟུག་པོ་བཀོད་པའི་གནས་སུ་གསུངས། །",
    "before": "earliest field",
    "after": "earliest realm",
    "finding": "PD-T19",
    "kind": "translation"
  },
  {
    "pair": "DTG-000313",
    "golden": [
      "U00640",
      "U00641"
    ],
    "tibetan": "གྲུབ་མཐའ་བློ་ལ་བརྟེན་པ་ཡིས། །\nརང་གཞན་ཤེས་པའི་རྩལ་གྱིས་སོ། །",
    "before": "through the expressiveness of knowing in oneself and others.",
    "after": "through the expressiveness of knowing in oneself and others.\n\nReview note: [Tenets and construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q04-01).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000188",
    "golden": [
      "U00361",
      "U00362"
    ],
    "tibetan": "འདུལ་གཞི་ལས་ནི་འདུལ་བྱེད་དུ། །\nབྱུང་བས་བསྟན་པ་གནས་པར་བྱེད། །",
    "before": "Earlier notes: [N-T09](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t09).",
    "after": "Earlier notes: [N-T09](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t09).\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000322",
    "golden": [
      "U00664",
      "U00665"
    ],
    "tibetan": "རླུང་ས་མེ་ཆུ་ཆ་ལྔ་ལས། །\nའགྱུར་ཞིང་བྱེད་པ་ལུས་ཀྱི་གཞི། །",
    "before": "Earlier notes: [N-040](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-040).",
    "after": "Earlier notes: [N-040](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-040).\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000351",
    "golden": [
      "U00722",
      "U00723",
      "U00724"
    ],
    "tibetan": "གླེང་གཞི་དག་ལ་ཡང་དག་ཚིག །\nགདུལ་བྱ་གང་ཟག་སོ་སོ་ལ། །\nགདུལ་གཞི་ཕུང་པོ་རྣམ་པ་ལྔ། །",
    "before": "the basis of training is the five aggregates.",
    "after": "the basis of training is the five aggregates.\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000352",
    "golden": [
      "U00725"
    ],
    "tibetan": "དེ་ཡི་འདུལ་བྱེད་གླེང་གཞི་སྟེ། །",
    "before": "The introductory setting is what trains that basis.",
    "after": "The introductory setting is what trains that basis.\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  },
  {
    "pair": "DTG-000354",
    "golden": [
      "U00727"
    ],
    "tibetan": "གཞི་ནི་རྣམ་པ་ལྔ་ཡིན་ཏེ། །",
    "before": "Earlier notes: [N-043](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-043).",
    "after": "Earlier notes: [N-043](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-043).\n\nReview note: [Basis, wordplay, and scope](../translations/2026-10-01-golden-aligned/REVIEW.md#phase-d-basis-04).",
    "finding": "PD-N03",
    "kind": "review-link"
  }
]
```
<!-- /phase-d-batch-04 -->

<a id="phase-d-basis-04"></a>
**Basis and wordplay — local construction decision, not a shared glossary replacement.** DTG-000322 says `ལུས་ཀྱི་གཞི`, the body's basis, in the sequence of changing elements. DTG-000351 explicitly identifies `གདུལ་གཞི` with five aggregates; DTG-000352's `དེ་ཡི` refers back to what is trained. This provides the internal comparison lacking at the earlier DTG-000188 `འདུལ་གཞི`. The basis reading is locally supported; the precise relationship of arising as what trains at DTG-000188 is still not independently resolved. It must not be counted as a fully settled clause merely because Ground was corrected.

At DTG-000353–000354 the text explains gleng ba and gzhi separately within the introductory-setting account. Basis renders the latter component in that explanation; introductory setting remains the complete expression gleng gzhi. The subsequent place, teacher, retinue, teaching and time are the five aspects being described. This is interpretive source wordplay, not historical etymology. The Tibetan component labels Phun/Gsum/Tshogs, their differing explanations and every stated numeral remain unchanged. Technical Ground at DTG-000344, in the explicit unchanging Ground/path/result sequence, is retained. The chapter-outline Ground uses at DTG-000328/000329/000334 are less decisive: their support-of-a-chapter versus technical referents remain within N-041 for comparison with the chapter endings; they are not changed by this local basis decision.

<a id="pd-q04-01"></a>
#### PD-Q04-01 — Tenets, system and instrumental continuation

**DTG-000313 / U00640–U00641.** Tibetan: `གྲུབ་མཐའ་བློ་ལ་བརྟེན་པ་ཡིས། །` / `རང་གཞན་ཤེས་པའི་རྩལ་གྱིས་སོ། །`

Current English: “Tenets depend on the conceptual mind, / through the expressiveness of knowing in oneself and others.” This is retained provisionally. The immediately preceding assertions/reasons/examples make constituent tenets possible under the P2 row, but a whole tenet system is also possible. The two instrumental constructions do not unambiguously state the finite dependence clause chosen by the English. Compare the full establishment account and DTG-000891 before deciding between a system depending on conceptual mind and establishment through reliance on conceptual mind/knowing. An explicit internal parallel supplying that relationship would settle it. Do not add philosophical or force the noun into a new shared default while this is open.

<a id="phase-d-batch-04-dispositions"></a>
**Other justified retentions and bounded questions:** The logical chos can occurrences DTG-000304/000308/000309 meet P2's subject exception; the paired chos nyid/property at DTG-000304 remains the explicitly linked N-T20 proposal, not an approved extension of that exception. N-037's wind/argument imagery and N-038's impure-wind/primordial-knowing clause remain provisional, preserving the printed negation. Current G-U00626/G-U00632/G-U00651/G-U00710/G-U00800 already separate the variants; the old nus pa/capacity speculation does not supersede the selected bus pa annotation. The additional heading delimiters at G-U00910/G-U00948 do not warrant English edits.

N-039's dngos grouping and the doing/doer-versus-two-operations relationship in DTG-000315 remain provisional: both source members and every listed contrast survive, but no hidden grammatical table is reconstructed. N-040's exact elemental order, the single water after doubled wind/earth/fire, and lung sdeb remain; lung is not silently emended to rlung or certified as the teaching/transmission sense merely from spelling. The clear support construction at DTG-000322 is resolved without pretending to solve that numerical matrix.

At DTG-000332, N-T22's nature of ordinary mind is retained provisionally because this clause identifies the object of the fourth chapter's transmission in a parallel account of the nature of phenomena and completed qualities. That supports a lexicalized nature-reading but does not exclude the owner's preferred intensive ordinary mind itself. The full scope must be compared with DTG-001115; neither book preference nor repeated usage settles it. Ordinary mind remains visible in either alternative. The source's six chapter arrays and compressed remainder (N-041) retain their order and terms; the chapter-title gnad repairs do not add or rename a chapter. Nye bar at DTG-000345 and rigs byed at DTG-000341 retain N-042's exact local questions rather than a new metaphysical interpretation.

The later prophecy's unusual body descriptions are not diagnoses or historical identifications. Preserve the source's front/blue tooth, right elbow, scorpion-shaped mole, triangular-eye covering, westward/Vajra-Seat question, two-tipped tongue and emerald arm projection. The causal connection across DTG-000394–000395 is supported by the preceding yis; the nominal fragment should not be judged in isolation. At DTG-000426 the retinue of five thousand, plural all, attained acceptance, and persons possessing virtuous ordinary minds support the person-reading great bodhisattvas for the shortened byang chub sems chen po; this is a local attested construction, not permission to reconstruct every byang chub sems expression from components.

The names in N-045 remain source-based/provisional, including Sūtrade, Jaya Ākar and Bharabhati Sāli. Glorious Protector and Glory-Holder, Glory of Joy and Deity of Bliss, and the two prophetic sequences' other differing names are deliberately not conflated. DTG-000430's cyclic-existence label is repaired without resolving whether mtha' yas qualifies the destroyer or the cyclic existence; N-045's name-boundary qualification remains operative. Sanskrit transliterations such as Jinamitra and Kamalaśīla are not replaced by familiar identities. N-047's anticipatory half yields seven and a half hundreds, while sa ya drug 'bum remains the expressly unresolved literal count; these are different constructions.

<a id="phase-d-prophecy-comparison"></a>
**Source-linked comparison of the two prophetic sequences (N-044/N-045):** This is a comparison, not a reconciliation. The first account introduces seven named ages (DTG-000364), sixty ages of darkness between them (000365), and then: north/Glorious Protector/Jinamitra, 1,300 years (000366–000369); sixty [years] of darkness (000370); south/Glory of Joy/Spiritual Accomplishment of Virtue, 100 years (000371–000373); 120 years of darkness (000374); east/Sūtrade/Jaya Ākar, 1,400 years (000375–000377); 5,000 years of darkness (000378); west/Protector of Bliss/Holder of Heroes, 1,000 years (000379–000381); 5,000 years of darkness (000382); Vajra Seat/Excellent Intelligence/Pure Cool-Maker, 550 years (000383–000386), then elemental destruction (000387–000389).

The second account instead alternates particular destructive figures with: first Glory-Holder after sixty years (000393–000397), then a 1,300-period statement (000398); Deity of Bliss/100 years following sixty years of darkness (000399–000401); a king suppressing practitioners and sixty years' disappearance (000402–000404); a solitary-buddha form/120 years (000405–000406); a Golden-City elder and sixty years of darkness (000407–000409); Glorious Lion/1,400 years (000410); the king's son and sixty years of darkness (000411–000412); Kamalaśīla's master Protector of Youth/1,000 years (000413); the lion-headed commoner, three months after birth and sixty [years] (000414–000415); Beautifying Youth/550 years (000416); the bird-bodied figure, ten years after birth and sixty [years] (000417–000418); Śākya Dzīka/ten years (000419). The text itself calls this seven stages at 000420. The differing names, duration units and number of narrative notices remain as written. No modern date conversion, arithmetic harmonization, silent eighth-stage correction or identity merger is warranted.

<a id="phase-d-notes-04"></a>
**Active note/usage dispositions to append after this evidence checkpoint:** N-T20: subject now approved only for the three actually read logical occurrences; property, assertion, logical reason and reasoning retain their separate historical proposal statuses. N-T22: apply the U07 construction control and retain the qualified nature-reading for 000332 pending 001115. N-048: actual-presences wording is superseded by P2 entities at 000441, while the sun referent, colored speech-emanation, object worn and ritual relationships remain unresolved. N-043: ordinary basis/setting-component reading and all wordplay preserved, without settling the four gathered in time or scriptural-collection scope. N-T50: sacred pledge also applies at 000348, retaining vows. N-T23: transmission already conforms at 000332/000362; this does not settle opaque lung sdeb at 000325 or the complete lung bstan/prophecy expression at 000337. Historical notes and approval records will not be rewritten.

<a id="phase-d-resumption-03"></a>
### Resumption 03 — preserved interrupted work and current-input verification

Active reviewer/session: **DTG-PD-20261005-Astra-03**, GPT-6 Astra Pro, independent of the authoring and October 1 source-reconciliation runs. Earlier Phase D semantic-review statements remain attributed to sessions 01/02; verification of this review's repairs is a self-check, not another independent certification. The current assignment authorizes minimal English and translation-note repairs only in this repository, with no source, segmentation, glossary-assignment or release-tag changes.

The checkout initially contained unpublished Batch 04 edits in `paired/translation.md`, this report, `LEGACY-NOTES.md` and `USAGES.json`, on `review/post-translation-20261005` at `70ad217392aea5fa0774b5f02a6de9300ab74517`. All four files were preserved unchanged at **`cbb308f20db0dbd00ec261c4bd017ffbfd7ad53c`**, pushed to `recovery/phase-d-interrupted-20261005-cont03`, and matched to that remote ref. The review branch was then fast-forwarded to the preservation commit. Other checkouts/worktrees, stash state and all historical tag objects were left untouched. Remote main remains **`fc3a443ba5987efb0b132990bf131a236fa57320`**. No review pull request existed at this checkpoint; adoption PR #5 is verified merged.

**Resumed English input:** `cbb308f20db0dbd00ec261c4bd017ffbfd7ad53c`; canonical English SHA-256 **`cf32cc7eb0c12173b13b204d86115f31338c9ab821c16e09b2c36419844baa2f`**. The complete active standard (including I §8.1 and III), all 283 glossary rows/all eight columns, AGENTS, status, handoff, decisions, retained format, source provenance and existing review/usage records were read. Root `FORMAT.md` remains absent; the already recorded adopted paired-format documentation governs. The policy, golden/source, format and lineage hashes reproduce the original freeze table. Standard, glossary and DECISIONS reproduce the adopted `10fe4e8c1ea0be37a205753dbb4a7e6e4c84a126` blobs exactly. The file history contains no later local terminology override; the earlier scoped rendering decisions remain structural decisions, not new shared terminology authority.

The finite scope is unchanged: **2,667 pairs / 5,484 golden objects**, including the opening, all six chapters, all 15 closing pairs, source annotations and linked unresolved spans. At this checkpoint, sessions 01/02 have a verified saved semantic-coverage record through ordinal 300. The preserved Batch 04 claims reading through ordinal 450, but its repair verification and status integration are pending. Continuation 03 has additionally reread current ordinals **1–100**, with all **50** first-encountered attached notes, from the actual canonical files; this is not 100 additional distinct pairs. Existing qualifications and supported repairs are retained. Fresh source-order rereading continues at ordinal 101, while the next range absent from the saved earlier read record is 451–2667. No complete-work readiness is claimed.

**Actual current-input checks, before new repairs by continuation 03:** exact replay of all **99** recorded pair operations (**82** English repairs and **17** review-link insertions) reproduces all current pair payloads. There are **77** distinct English-repair pairs and **86** changed pairs including note-only changes. Fixed Tibetan/golden bytes, all 2,667 IDs/order, policy/format/lineage, inherited note associations, original usage history and **696** English local-link targets pass the read-only integrity check. `git diff --check` passes. Replay establishes reproducibility, not semantic correctness of the preserved Batch 04.

The eight existing validators/build checks were actually rerun on this preserved input. `paired/validate.py` (ordinary and `--require-final`), `paired/migrate.py --check`, `paired/project.py --check`, and the golden-review translation validator/build check all fail at the historical protected-glossary contract, as before. The golden-review corruption suite passes its positive case and all **36** deliberately corrupted fixtures. **`paired/test_paired.py` now runs 64 tests: 53 pass, nine fail and two error.** Both positive-case errors are the exact released-English comparison at DTG-000002. That same early comparison preempts the intended rejection in nine negative fixtures: closing-as-seventh-chapter, closing-role change, restored-verse deletion, extraneous source text, missing final signoff, hidden source heading, Tibetan join-newline change, whitespace trimming and Tibetan-word mutation. These are present on the resumed input after earlier authorized English repairs; they are not all the original pre-edit baseline failures, and they do not demonstrate a new Tibetan alteration. The earlier 63-pass/one-error result remains historical, not the current test result. No historical validation contract, signed receipt or release is changed to conceal this mismatch. The standard's 63 semantic regression specifications have **not** been executed as a test suite.

<a id="phase-d-reread-03"></a>
### Continuation 03: current-text reread through ordinal 300

Current ordinals **1–300** have now been reread in source order, with all **97** first-encountered note records (50 + 30 + 17), under Q1–Q9, I §8.1 and III. This is a reread of existing coverage, not 300 additional distinct reviewed pairs. The current source corrections, separated annotations, title/continuum and word/sound distinctions, matter/awareness contrast, sacred pledges/vows, retained descriptive names and exact numerical constructions were checked before proposing changes.

The following three findings were recorded **before application**. S07 clarifies the scope of the five further sites; S08 preserves an explicit ordinal rather than distance phrasing; E02 extends the confirmed imperative-pronoun repair. These are not new terminology assignments. N-019/020/021/022/023/026–036 and the exact-linked earlier Phase D construction questions retain their narrower unresolved scopes. In particular, no source variant is promoted to main text, no thal-yig/lda-ldi decipherment is invented, and no full phrase is reconstructed from component matches.

<!-- phase-d-reread-03-operations -->
```json
[
  {
    "pair": "DTG-000212",
    "ordinal": 215,
    "golden": [
      "U00413",
      "U00414",
      "U00415"
    ],
    "family": "S07",
    "kind": "english",
    "tibetan": "སྟོང་དང་གནས་གཞན་ལྔ་ཡིན་པས། །\nའདི་ཉིད་ཤེས་པ་ཙམ་གྱིས་ནི། །\nབཅོམ་ལྡན་འདས་ལ་རེག་པར་སྦྱོར། །",
    "before": "Since there are a thousand and five further sites,",
    "after": "Since there are a thousand sites and five further ones,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "U00410–U00413 explicitly gives five sites with two hundred each and one additional site each. In སྟོང་དང་གནས་གཞན་ལྔ་ the further/other sites are the five, not the entire thousand-and-five. Make the modifier scope unambiguous without changing either number or the following mere-knowing condition.",
    "context_pairs": [
      "DTG-000211",
      "DTG-000212",
      "DTG-000213"
    ]
  },
  {
    "pair": "DTG-000275",
    "ordinal": 278,
    "golden": [
      "U00582",
      "U00583",
      "U00584",
      "U00585",
      "U00586"
    ],
    "family": "S08",
    "kind": "english",
    "tibetan": "དེ་འོག་འཇིག་རྟེན་དགུ་པ་ན། །\nདུང་ལྡན་ཐལ་བའི་ལྷ་ཞེས་པ། །\nདད་ཅིང་བསུང་བའི་དྲི་ཡིས་མྱོས། །\nའཁྱུག་ཅིང་རབ་ཏུ་འབར་བའི་འོད། །\nརབ་ཏུ་མེར་མེར་པོ་ཡིས་འཁྲིགས། །",
    "before": "Nine worlds below it,",
    "after": "In the ninth world below it,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "དེ་འོག་འཇིག་རྟེན་དགུ་པ་ན། explicitly locates this in the ninth world below the preceding realm. Preserve the ordinal construction, as in the nearby sixth-world expressions, rather than assimilating it to the cardinal-distance and beyond-six constructions. N-032 and N-034 do not settle a different reading of this line. No location or cosmological map is inferred.",
    "context_pairs": [
      "DTG-000273",
      "DTG-000274",
      "DTG-000275",
      "DTG-000276",
      "DTG-000277"
    ]
  },
  {
    "pair": "DTG-000285",
    "ordinal": 288,
    "golden": [
      "U00601",
      "U00602",
      "U00603"
    ],
    "family": "E02",
    "kind": "english",
    "tibetan": "རང་འདོད་ངེས་པར་སྐྱོལ་བ་ནི། །\nལུང་དང་རིགས་པ་མན་ངག་གིས། །\nསྐྱོན་བསལ་བསྒྲུབ་དང་འགལ་བ་སྤང་། །",
    "before": "To bring one's own position to a definite conclusion,",
    "after": "To bring your own position to a definite conclusion,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "རང་འདོད་ is governed here by the explicit second-person instructions remove, establish and abandon in U00603. Retain the same addressee across the purpose clause and its imperatives, extending the already confirmed E02 pattern. The descriptive own/others constructions in DTG-000284 and DTG-000295 are not changed. N-036 preserves the remaining argumentation imagery and unenumerated counts.",
    "context_pairs": [
      "DTG-000284",
      "DTG-000285",
      "DTG-000286"
    ]
  }
]
```

**Application/self-check:** All three recorded repairs were applied and reread with the eleven listed context pairs. The 1,000 plus five further sites, the explicit ninth-world relation, and the imperative addressee are retained without changing a number, agent, negation or technical component. The full integrity replay passes 2,667 pairs and 696 local-link targets: 85 English operations in 79 pairs, 17 review links and 88 changed pairs including note-only changes, plus the separately recorded source-annotation repair. The final paired validator and projector check were rerun; both still report the historical protected-glossary mismatch, so the projector produced no new reader output. `git diff --check` passes. This is repair self-verification, not another independent review.

<a id="phase-d-recovered-04-check"></a>
### Continuation 03: recovered Batch 04 verified

All current ordinals **301–450** (DTG-000298–000447), their **21** first-encountered notes and all necessary preceding context were read in source order. Together with the prior reread this is **450 distinct current pairs and 118 first-encountered attached notes**, not additive coverage across reviewers. The full eight-column rows governing Ground/basis, ordinary mind and whole compounds, key point, sacred pledge, entity, realm, spiritual accomplishment and literary tantra were rechecked. N-T20 was also reread in full, including the limited logical-subject disposition and the still-provisional adjacent expressions.

The recovered **20 English repairs in 20 pairs**, including the earlier DTG-000188 training-basis return, and six note-link insertions were self-checked against their recorded exact source and immediate clauses. The ordinary-basis repairs do not alter technical Ground, the five aggregates or the source's component wordplay. Ordinary mind retains the loving/virtuous qualifiers; entities retains all three embodiment/speech/awakened-mind members and the effortless result. The descriptive-name corrections retain spiritual and cyclic-existence components without certifying names or changing modifier attachment. Key point, realm, sacred pledge and literary tantra preserve number and scope. The imperative pronoun does not introduce a different agent. All six recovered note/usage dispositions accurately retain their stated unresolved boundaries and historical records. This is verification within the review, not a second independent certification.

The source corrections at G-U00626, G-U00632, G-U00651, G-U00710 and G-U00800 already separate annotations; in particular, the selected bus pa alternative is not an unresolved nus pa correction to main text. The impure reading's negation remains. The numerical and name differences in the two prophecy accounts, bodily signs, anticipatory-half construction, large unresolved numerical phrase and unexpanded ritual references remain as documented in Batch 04. No additional main-English repair is justified solely by their unfamiliarity. N-041's six chapter descriptions and N-T22's sems nyid family remain for comparison with the ensuing chapter endings and DTG-001115.

One further narrow construction question is identified below. It is linked without changing the provisional English or treating it as a confirmed mistranslation.

<a id="pd-q04-02"></a>
#### PD-Q04-02 — Maturation and the five families

**DTG-000446 / U00971–U00973.** Tibetan: `དེ་ནས་ལྕང་ལོ་ཅན་གྱི་གནས། །` / `ཀུན་གཟིགས་རྣམ་པར་སྣང་མཛད་ཀྱིས། །` / `འདི་ཉིད་བཟུང་བས་རིགས་ལྔར་སྨིན། །`

Current English: “Then, in the abode of Those with Long Locks, / the All-Seeing Vairocana / held this, bringing the five families to maturity.” Retain provisionally. The teacher is the explicit holder, and the holding has an instrumental connection to maturation. But `རིགས་ལྔར་སྨིན` does not by itself settle whether the five families are the recipients brought to maturity, the forms/aspect in which maturation occurs, or the category into which an unexpressed recipient matures. An internal parallel making the maturation subject and this terminative relationship explicit, or authorized commentary on this clause, would settle it. N-049's existing name/count qualifications remain; no new family designation, agent or historical identity is supplied. **Severity:** medium potential relationship ambiguity. **Confidence:** moderate that the English remains interpretive; no confidence claim that the alternative is superior.

<!-- phase-d-q04-02-link -->
```json
[
  {
    "pair": "DTG-000446",
    "ordinal": 449,
    "golden": [
      "U00971",
      "U00972",
      "U00973"
    ],
    "family": "PD-Q04-02",
    "kind": "review-link",
    "tibetan": "དེ་ནས་ལྕང་ལོ་ཅན་གྱི་གནས། །\nཀུན་གཟིགས་རྣམ་པར་སྣང་མཛད་ཀྱིས། །\nའདི་ཉིད་བཟུང་བས་རིགས་ལྔར་སྨིན། །",
    "before": "Then, in the abode of Those with Long Locks,\nthe All-Seeing Vairocana\nheld this, bringing the five families to maturity.\n\nEarlier notes: [N-049](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-049).",
    "after": "Then, in the abode of Those with Long Locks,\nthe All-Seeing Vairocana\nheld this, bringing the five families to maturity.\n\nEarlier notes: [N-049](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-049).\n\nReview note: [Maturation construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q04-02).",
    "rationale": "Link the exact unresolved maturation construction; no main-English change.",
    "severity": "documentation",
    "confidence": "high for link and source scope"
  }
]
```

**Link application/integrity:** The exact question link was applied without changing the main English. Full recorded-operation replay passes: 2,667 pairs, 103 operations (85 English repairs and 18 review links), 79 distinct English-repair pairs, 89 changed pairs including note-only changes, and 697 local-link targets. Fixed Tibetan/golden/policy/format/lineage, IDs/order and inherited note/history checks pass. English SHA-256: `5ceabb13015b9891ea4103cdca4e7f9d57ac51cc31f2c1ec20f47cde00cbe3b9`. No new generated view was produced; the existing release-bound build failures remain as actually rerun above. `git diff --check` passes. Saved semantic coverage is now 450/2,667; continuation is ordinal 451, DTG-000448. Text readiness remains provisional and the complete-work pass remains in progress.

<a id="phase-d-batch-05"></a>
### Batch 05 — source ordinals 451–600

All **150** current pairs DTG-000448–000597 were read in source order, with all **38** first-encountered active/historical note records, their current source updates and complete proposal fields. Current ordinals 601–615 were also read as connected context for N-064, without adding them to this batch's coverage. For the historical note view only duplicated unit-by-unit Tibetan quotations were omitted; the current fixed Tibetan was read in full in the pair view, and all source-annotation text, alternatives, scope and qualifications were retained.

**Evidence before application:** 25 English operations in 22 pairs and one question-link insertion are specified below. The full eight-column glossary rows and the complete expressions govern; no finding follows solely from an English substring or a historical example. Repeated T03, T02, T19, T01, T09 and T13 findings retain their earlier scoped rationale. New T23 covers the actual category sequence, preserving discipline, discourse collection and higher doctrine rather than conflating their complete labels. T24 applies the process form familiarization without settling N-057's shifting construction. E03 repairs a dangling filial relation; S10 distinguishes physical limbs from the literary branch metaphor; S09 restores a stated wish-condition while leaving the compressed result clause qualified.

<!-- phase-d-batch-05-operations -->
```json
[
  {
    "pair": "DTG-000448",
    "ordinal": 451,
    "golden": [
      "U00978",
      "U00979",
      "U00980"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "བརྫུས་དང་སྒོ་ང་ལས་སྐྱེས་དང་། །\nདྲོད་དང་མངལ་ནས་སྐྱེས་པ་ཡི། །\nསེམས་ཅན་རྣམས་ནི་སྨིན་པར་བྱེད། །",
    "before": "Sentient beings",
    "after": "Karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000450",
    "ordinal": 453,
    "golden": [
      "U00983",
      "U00984",
      "U00985"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "འདི་ཡི་མཛད་པ་སུམ་ཅུ་དྲུག །\nསྐུ་གསུང་ཐུགས་ལ་བརྟེན་ནས་ནི། །\nགདུལ་ཡུལ་སེམས་ཅན་རྣམས་ལ་སྣང༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000485",
    "ordinal": 488,
    "golden": [
      "U01068",
      "U01069",
      "U01070"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "འདི་དུས་འཁོར་བ་དོང་སྤྲུགས་ཏེ། །\nསེམས་ཅན་རྣམས་ཀྱིས་སངས་རྒྱས་འཐོབ། །\nའགྲོ་བ་དྲུག་ཅེས་སྣང་མི་སྲིད། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000486",
    "ordinal": 489,
    "golden": [
      "U01071",
      "U01072",
      "U01073"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "བསྐལ་པ་སྟོང་ཕྲག་ཉི་ཤུར་ནི། །\nསེམས་ཅན་འཁོར་བ་རྒྱུན་ཆད་ནས། །\nལུས་ཅན་རྣམ་པར་མི་སྣང་ངོ༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000487",
    "ordinal": 490,
    "golden": [
      "U01074",
      "U01075",
      "U01076",
      "U01077"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "དེ་ནས་ལས་ཀྱི་བྱེ་བྲག་ལས། །\nསེམས་ཅན་ཉོན་མོངས་མངོན་མེད་ཀྱང༌། །\nབག་ལ་ཉལ་བ་ལངས་པའི་དབང་། །\nཤིན་ཏུ་ཕྲ་བ་བླངས་པའི་གཟུགས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000488",
    "ordinal": 491,
    "golden": [
      "U01078",
      "U01079"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "གྲངས་མང་རབ་ཏུ་ཕྲ་བ་ལས། །\nགཟུགས་ཅན་སེམས་ཅན་ལུས་འཕེལ་འགྱུར། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000510",
    "ordinal": 513,
    "golden": [
      "U01124",
      "U01125",
      "U01126"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སྤྱི་མཐུན་ལས་ཀྱི་བྱེ་བྲག་ལས། །\nསེམས་ཅན་ལས་ཀྱི་བརྟེན་སོ་ཡིས། །\nཕྱི་ཡི་འབྱུང་བ་ལ་བརྟེན་ནས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000522",
    "ordinal": 525,
    "golden": [
      "U01145",
      "U01146"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "རྩི་ནི་སེམས་ཅན་གཞན་དོན་དང་། །\nརང་གི་དོན་ཡང་རྫོགས་པའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000524",
    "ordinal": 527,
    "golden": [
      "U01148",
      "U01149",
      "U01150",
      "U01151"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་དུས་ནི་རྣམ་པ་བརྒྱད། །\nནད་དང་རླུང་དང་ཚ་བ་ནི། །\nཤེས་པ་ཉོན་མོངས་བྱང་སེམས་དང་། །\nཡེ་ཤེས་ཉིད་དང་འབྱུང་བའོ། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000526",
    "ordinal": 529,
    "golden": [
      "U01155"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་རླུང་སེམས་འཕོ་བའི་དུས། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000534",
    "ordinal": 537,
    "golden": [
      "U01168"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་གཅིག་གི་དུས་ཡིན་ནོ། །",
    "before": "sentient being",
    "after": "karmic being",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000535",
    "ordinal": 538,
    "golden": [
      "U01169",
      "U01170",
      "U01171",
      "U01172"
    ],
    "family": "T03",
    "kind": "translation",
    "tibetan": "སེམས་ཅན་སྤྱི་ཡི་དུས་དག་ནི། །\nདང་པོ་དཔག་ཏུ་མེད་པ་ནས། །\nཐ་མ་ཚེ་ལོ་བཅུ་པའི་བར། །\nདུས་ཀྱི་རིམ་པ་དྲུག་ཅུ་འབྱུང༌། །",
    "before": "sentient beings",
    "after": "karmic beings",
    "severity": "medium",
    "confidence": "high",
    "rationale": "P2 assigns the complete sems can expression to karmic being. Preserve the actual number, possessive and attached source qualifications; do not extend the label to neighboring gro ba, lus can, bodhisattva or the separate wind-mind compound."
  },
  {
    "pair": "DTG-000485",
    "ordinal": 488,
    "golden": [
      "U01068",
      "U01069",
      "U01070"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འདི་དུས་འཁོར་བ་དོང་སྤྲུགས་ཏེ། །\nསེམས་ཅན་རྣམས་ཀྱིས་སངས་རྒྱས་འཐོབ། །\nའགྲོ་བ་དྲུག་ཅེས་སྣང་མི་སྲིད། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the adopted cyclic-existence label for khor ba, preserving its negation, possessors, temporal scope and the distinct rgyun/flow construction."
  },
  {
    "pair": "DTG-000486",
    "ordinal": 489,
    "golden": [
      "U01071",
      "U01072",
      "U01073"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "བསྐལ་པ་སྟོང་ཕྲག་ཉི་ཤུར་ནི། །\nསེམས་ཅན་འཁོར་བ་རྒྱུན་ཆད་ནས། །\nལུས་ཅན་རྣམ་པར་མི་སྣང་ངོ༌། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Use the adopted cyclic-existence label for khor ba, preserving its negation, possessors, temporal scope and the distinct rgyun/flow construction."
  },
  {
    "pair": "DTG-000451",
    "ordinal": 454,
    "golden": [
      "U00986",
      "U00987",
      "U00988",
      "U00989",
      "U00990"
    ],
    "family": "E03",
    "kind": "translation",
    "tibetan": "ང་ནི་མྱ་ངན་འདས་འོག་ཏུ། །\nནུབ་ཕྱོགས་ཨུ་རྒྱན་དག་གི་ཡུལ། །\nདྷ་ན་ཀོ་ཤའི་ལྷ་ལྕམ་ལ། །\nཕ་མེད་བུ་ནི་བཛྲ་ཧེ། །\nའདིས་ནི་དམ་པའི་བསྟན་པ་འཛིན། །",
    "before": "to the divine lady of Dhanakośa,\na fatherless son, Vajrahe,",
    "after": "a fatherless son of the divine lady of Dhanakośa,\nVajrahe,",
    "severity": "minor",
    "confidence": "high",
    "rationale": "U00988–U00990 gives the divine lady, a fatherless son, and this son as the explicit upholder. The dangling English to-phrase currently appears attached to will uphold. Express the already stated filial relation without inserting a birth verb, another upholder, a historical identification or a reconstructed name."
  },
  {
    "pair": "DTG-000469",
    "ordinal": 472,
    "golden": [
      "U01024",
      "U01025",
      "U01026",
      "U01027",
      "U01028",
      "U01029",
      "U01030",
      "U01031"
    ],
    "family": "T19",
    "kind": "translation",
    "tibetan": "བསྟན་པའི་སྙིང་ཐིག་གསང་བ་འདི།།\nདེ་ལྟར་བསྟན་པ་བདུན་འདས་ནས། །\nཞིང་ཁམས་གཉིས་ལ་ངེས་སྤྱད་ནས། །\nདེ་ལྟར་བདུན་པོ་ཐལ་ནས་ཀྱང༌། །\nརྡོ་རྗེ་གདན་གྱི་སྤོ་ལ་ནི། །\nབསྟན་པ་ཀུན་གྱི་གསུང་གི་བཙས། །\nརང་བྱུང་ཆེན་པོའི་ཡི་གེ་ཉིད། །\nསྒྲ་དང་བཅས་ཏེ་བབས་པ་ནི། །",
    "before": "two fields",
    "after": "two realms",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The two zhing khams are the realms in the transmission-course account, not an operative field metaphor. Preserve the repeated seven and the unestablished course, heart-sphere and speech-token constructions."
  },
  {
    "pair": "DTG-000478",
    "ordinal": 481,
    "golden": [
      "U01055",
      "U01056"
    ],
    "family": "T23",
    "kind": "translation",
    "tibetan": "མདོ་སྡེའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nདྲང་ངེས་ལས་ཀྱི་མཐའ་ལ་དགོད། །",
    "before": "Through the sūtra teaching for eight ages,",
    "after": "Through the teaching of the discourse collection for eight ages,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The mdo sde category occurs between the discipline and higher-doctrine teaching categories in U01050–U01066. Apply the complete approved discourse collection label, preserving teaching and eight ages; the drang nges las kyi mtha construction remains N-052."
  },
  {
    "pair": "DTG-000484",
    "ordinal": 487,
    "golden": [
      "U01066",
      "U01067"
    ],
    "family": "T23",
    "kind": "translation",
    "tibetan": "མངོན་པའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nཐམས་ཅད་ཚེ་གཅིག་འབྲས་བུ་ཐོབ། །",
    "before": "Through the higher teaching for eight ages,",
    "after": "Through the teaching of higher doctrine for eight ages,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Mngon pa here names the doctrinal category in the three-category teaching sequence, not a generic higher adjective. Preserve the separate bstan pa/teaching and all eight ages; do not promote the separately reported hundred variant into main text."
  },
  {
    "pair": "DTG-000491",
    "ordinal": 494,
    "golden": [
      "U01084",
      "U01085",
      "U01086"
    ],
    "family": "T01",
    "kind": "translation",
    "tibetan": "རྒྱུད་ཀྱི་ལུས་དང་ཡན་ལག་ནི། །\nལུས་ལ་བཀོད་པ་བརྒྱ་ཕྲག་ནི། །\nགཉིས་དང་ལྔ་བཅུ་ཐམ་པའོ། །",
    "before": "body and branches of the continuum",
    "after": "body and branches of the tantra",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The following explicit questions, six chapter arrays and counted textual body/branches establish the literary sense of rgyud. Apply P1 tantra, without altering the metaphor or any count."
  },
  {
    "pair": "DTG-000497",
    "ordinal": 500,
    "golden": [
      "U01095",
      "U01096",
      "U01097",
      "U01098"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཉིས་པའི་ལུས་ནི་ཉེར་བསྟན་པ། །\nགནད་རྣམས་འདུས་པའི་བཀོད་པ་ལ། །\nཞུས་པ་ཉི་ཤུ་རྩ་བརྒྱད་ལས། །\nགནད་དུས་བཀོད་པ་སུམ་ཅུ་གཅིག །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the complete gnad label in the chapter-array description; preserve the twenty-eight questions and thirty-one arrays."
  },
  {
    "pair": "DTG-000497",
    "ordinal": 500,
    "golden": [
      "U01095",
      "U01096",
      "U01097",
      "U01098"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཉིས་པའི་ལུས་ནི་ཉེར་བསྟན་པ། །\nགནད་རྣམས་འདུས་པའི་བཀོད་པ་ལ། །\nཞུས་པ་ཉི་ཤུ་རྩ་བརྒྱད་ལས། །\nགནད་དུས་བཀོད་པ་སུམ་ཅུ་གཅིག །",
    "before": "crucial-point times",
    "after": "key-point times",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply gnad/key point within the explicitly provisional literal gnad dus rendering while retaining times, its Tibetan identity and N-054. This does not emend dus to dus with an a-chung or approve the entire compound."
  },
  {
    "pair": "DTG-000519",
    "ordinal": 522,
    "golden": [
      "U01142"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "དྲིས་ནི་བཅུད་ཀྱིས་ལེན་པ་འགྲུབ། །",
    "before": "taking nourishment from vital essences",
    "after": "taking nourishment from quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The same bcud kyis len pa nourishment construction as the earlier scoped T13 finding occurs with smell. P2 quintessence applies in this nourishment/concentration sense; the whole expression is still a linked local construction, not a new canonical assignment."
  },
  {
    "pair": "DTG-000538",
    "ordinal": 541,
    "golden": [
      "U01181",
      "U01182"
    ],
    "family": "T24",
    "kind": "translation",
    "tibetan": "གོམས་པའི་འཕོ་དུས་བརྒྱད་རིམ་གྱིས། །\nསྤྱོད་པ་ཕྱི་ནས་ངན་པར་འགྱུར། །",
    "before": "habituation",
    "after": "familiarization",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved process form for goms pa, distinct from sgom/cultivation. The eight stages, shifting relation and subsequent worsening remain unchanged and qualified by N-057."
  },
  {
    "pair": "DTG-000579",
    "ordinal": 582,
    "golden": [
      "U01275",
      "U01276",
      "U01277"
    ],
    "family": "S10",
    "kind": "translation",
    "tibetan": "ས་ཡི་ཟུག་པས་རྡུལ་རྣམས་འབྱིན། །\nབྱེར་བ་ཡིས་ནི་ཡན་ལག་འབྱིན། །\nསྙོམས་པས་ལུས་འབྱུང་རྫོགས་པའོ། །",
    "before": "its dispersal produces branches;",
    "after": "its dispersal produces limbs;",
    "severity": "medium",
    "confidence": "moderate-high",
    "rationale": "The verse concerns earth producing particles and completing the elements of the body. Yan lag here denotes the bodily limbs in that physical sequence, unlike the explicitly textual branches at DTG-000491–000507. No change is made to those textual metaphors or to the elemental functions."
  },
  {
    "pair": "DTG-000594",
    "ordinal": 597,
    "golden": [
      "U01309",
      "U01310"
    ],
    "family": "S09/T02",
    "kind": "translation",
    "tibetan": "འཁོར་བའི་ལས་རྒྱུད་གཅད་འདོད་ན། །\nབྱ་བ་བྲལ་བར་རྫོགས་པས་རྫོགས། །",
    "before": "To cut the karmic continuum of samsara:",
    "after": "If one wishes to cut the karmic continuum of cyclic existence,",
    "severity": "medium",
    "confidence": "high for conditional and label; remainder provisional",
    "rationale": "Preserve the explicit wish-condition gcad dod na rather than recasting it as a bare purpose. Rgyud remains karmic continuum, not literary tantra; khor ba takes cyclic existence. The unexpressed subject and compressed completion clause remain within N-064; no new doctrinal subject is supplied."
  },
  {
    "pair": "DTG-000492",
    "ordinal": 495,
    "golden": [
      "U01087",
      "U01088",
      "U01089",
      "U01090"
    ],
    "family": "PD-Q05-01",
    "kind": "review-link",
    "tibetan": "དང་པོ་ངེས་པ་གསལ་བ་ཡིས། །\nསྣ་ཚོགས་བཀོད་པ་ཡན་ལག་ལ། །\nཞུས་པ་བདུན་ཅུ་ཐམ་པ་ལ། །\nཡན་ལག་བཀོད་པ་བརྒྱ་གཅིག་གོ། །",
    "before": "First, through clarity of ascertainment,\nin the branches of the manifold array,\nthere are exactly seventy questions;\nthe arrays of the branches number one hundred and one. [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054)\n\n[^G-U01090]\n\nEarlier notes: [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054).",
    "after": "First, through clarity of ascertainment,\nin the branches of the manifold array,\nthere are exactly seventy questions;\nthe arrays of the branches number one hundred and one. [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054)\n\n[^G-U01090]\n\nEarlier notes: [N-054](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-054).\n\nReview note: [Numerical construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q05-01).",
    "severity": "documentation",
    "confidence": "high for exact span and linkage",
    "rationale": "Link the precise main-count question without changing the selected source or asserting that either competing numerical analysis is settled."
  }
]
```

<a id="pd-q05-01"></a>
#### PD-Q05-01 — Main count and separately reported numerical variant

**DTG-000492 / U01087–U01090**, particularly `ཡན་ལག་བཀོད་པ་བརྒྱ་གཅིག་གོ། །`. Current English says “the arrays of the branches number one hundred and one.” Retain this **provisionally**, not as an independently certified count. The scope of `བརྒྱ་གཅིག` needs to distinguish the reading one hundred from an elliptical hundred-and-one count; the separately printed “eleven also occurs” does not by itself establish either the main arithmetic or a full replacement yielding 111. The older N-054 rationale is an inherited interpretation, not an owner-approved numerical rule. A decisive internal count construction or authorized commentary on this enumeration would settle it; no new witness reading, change to the golden text or adjustment to actual chapter totals is made. **Severity:** medium possible numerical difference. **Confidence:** moderate that this requires qualification; neither alternative is certified here.

<a id="phase-d-notes-05"></a>
**Active note/usage dispositions recorded before appending:** The following exact-scope records are to be appended to the existing usage file and linked in the active legacy-note index. The ten original usage records, all seventeen earlier dispositions and original historical notes remain unchanged. These are status/scope updates, not new canonical glossary assignments.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-051",
    "pairs": [
      "DTG-000469"
    ],
    "ids": [
      "U01024",
      "U01025",
      "U01026",
      "U01027",
      "U01028",
      "U01029",
      "U01030",
      "U01031"
    ],
    "source": {
      "DTG-000469": "བསྟན་པའི་སྙིང་ཐིག་གསང་བ་འདི།།\nདེ་ལྟར་བསྟན་པ་བདུན་འདས་ནས། །\nཞིང་ཁམས་གཉིས་ལ་ངེས་སྤྱད་ནས། །\nདེ་ལྟར་བདུན་པོ་ཐལ་ནས་ཀྱང༌། །\nརྡོ་རྗེ་གདན་གྱི་སྤོ་ལ་ནི། །\nབསྟན་པ་ཀུན་གྱི་གསུང་གི་བཙས། །\nརང་བྱུང་ཆེན་པོའི་ཡི་གེ་ཉིད། །\nསྒྲ་དང་བཅས་ཏེ་བབས་པ་ནི། །"
    },
    "realization": "two realms",
    "status": "Approved P2 realm label; remaining constructions provisional",
    "reason": "The realm label is adopted without approving heart-sphere, speech-token, Great Naturally Arisen as a name, or the definite-course construction. Seven/two and the embodiment/speech/awakened-mind sequence remain distinct.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-052",
    "pairs": [
      "DTG-000475",
      "DTG-000478",
      "DTG-000484"
    ],
    "ids": [
      "U01048",
      "U01049",
      "U01050",
      "U01051",
      "U01055",
      "U01056",
      "U01066",
      "U01067"
    ],
    "source": {
      "DTG-000475": "དེ་ལ་སོགས་ཏེ་སྟོན་པའི་འཁོར། །\nའཕགས་པ་ཉན་ཐོས་ཁྲི་ཕྲག་གཉིས། །\nའདུལ་བའི་བསྟན་པ་བསྐལ་པ་གཅིག །\nདགྲ་བཅོམ་འབྲས་བུ་ཉིད་ལ་བཀོད། །",
      "DTG-000478": "མདོ་སྡེའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nདྲང་ངེས་ལས་ཀྱི་མཐའ་ལ་དགོད། །",
      "DTG-000484": "མངོན་པའི་བསྟན་པ་བསྐལ་པ་བརྒྱད། །\nཐམས་ཅད་ཚེ་གཅིག་འབྲས་བུ་ཐོབ། །"
    },
    "realization": "discipline; discourse collection; higher doctrine",
    "status": "Approved P2 category labels in this sequence",
    "reason": "Discipline already conforms and does not require an added collection. Discourse collection and higher doctrine retain the explicit teaching nouns and durations. The participants, perfection attachment and provisional/definitive activity construction remain unresolved; no efficacy or cosmological reconciliation is implied.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-054",
    "pairs": [
      "DTG-000491",
      "DTG-000492",
      "DTG-000497"
    ],
    "ids": [
      "U01084",
      "U01085",
      "U01086",
      "U01087",
      "U01088",
      "U01089",
      "U01090",
      "U01095",
      "U01096",
      "U01097",
      "U01098"
    ],
    "source": {
      "DTG-000491": "རྒྱུད་ཀྱི་ལུས་དང་ཡན་ལག་ནི། །\nལུས་ལ་བཀོད་པ་བརྒྱ་ཕྲག་ནི། །\nགཉིས་དང་ལྔ་བཅུ་ཐམ་པའོ། །",
      "DTG-000492": "དང་པོ་ངེས་པ་གསལ་བ་ཡིས། །\nསྣ་ཚོགས་བཀོད་པ་ཡན་ལག་ལ། །\nཞུས་པ་བདུན་ཅུ་ཐམ་པ་ལ། །\nཡན་ལག་བཀོད་པ་བརྒྱ་གཅིག་གོ། །",
      "DTG-000497": "གཉིས་པའི་ལུས་ནི་ཉེར་བསྟན་པ། །\nགནད་རྣམས་འདུས་པའི་བཀོད་པ་ལ། །\nཞུས་པ་ཉི་ཤུ་རྩ་བརྒྱད་ལས། །\nགནད་དུས་བཀོད་པ་སུམ་ཅུ་གཅིག །"
    },
    "realization": "tantra; key point; key-point times (provisional)",
    "status": "P1/P2 labels applied; counts and complete gnad dus construction provisional",
    "reason": "The body/branches account is explicitly textual. Only gnad terminology is repaired inside the visibly provisional gnad dus wording. The brgya gcig main-count question is now precisely linked; the reported eleven remains a separate variant, and no count is changed to match a chapter inventory.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T16",
    "pairs": [
      "DTG-000519"
    ],
    "ids": [
      "U01142"
    ],
    "source": {
      "DTG-000519": "དྲིས་ནི་བཅུད་ཀྱིས་ལེན་པ་འགྲུབ། །"
    },
    "realization": "taking nourishment from quintessence",
    "status": "Approved P2 component in the same reviewed nourishment construction; complete construction provisional",
    "reason": "Extend the earlier scoped quintessence disposition to this actual smell/nourishment occurrence. Do not turn the older whole-expression proposal into a shared assignment or settle the distinct gnas bcud yul question.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T25",
    "pairs": [
      "DTG-000524",
      "DTG-000531"
    ],
    "ids": [
      "U01148",
      "U01149",
      "U01150",
      "U01151",
      "U01164",
      "U01165"
    ],
    "source": {
      "DTG-000524": "སེམས་ཅན་དུས་ནི་རྣམ་པ་བརྒྱད། །\nནད་དང་རླུང་དང་ཚ་བ་ནི། །\nཤེས་པ་ཉོན་མོངས་བྱང་སེམས་དང་། །\nཡེ་ཤེས་ཉིད་དང་འབྱུང་བའོ། །",
      "DTG-000531": "བྱང་ཆུབ་སེམས་ནི་འཇིལ་བ་དང་། །\nརབ་ཏུ་འཕྲིགས་ཤིང་ཕྲ་བར་འགྱུར། །"
    },
    "realization": "awakening ordinary mind (retained provisionally)",
    "status": "Unresolved whole-expression treatment; not an approved component-built default",
    "reason": "The adjacent short/full forms are internally linked, but the bodily sequence does not settle aspiration, bodily substance or another technical referent. The old component-preservation rationale alone cannot establish this whole expression. Retain its exact-linked provisional treatment pending a decisive internal construction or authorized commentary; do not apply it to bodhisattva occurrences.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-057",
    "pairs": [
      "DTG-000538"
    ],
    "ids": [
      "U01181",
      "U01182"
    ],
    "source": {
      "DTG-000538": "གོམས་པའི་འཕོ་དུས་བརྒྱད་རིམ་གྱིས། །\nསྤྱོད་པ་ཕྱི་ནས་ངན་པར་འགྱུར། །"
    },
    "realization": "familiarization",
    "status": "Approved P2 process label; shifting construction provisional",
    "reason": "Goms pa takes the process form familiarization here, not cultivation. The eight shifting stages, individual/collective times, physiological verbs and lifespan counts remain qualified; the label repair is not approval of their entire scheme.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T30",
    "pairs": [
      "DTG-000512"
    ],
    "ids": [
      "U01129",
      "U01130",
      "U01131"
    ],
    "source": {
      "DTG-000512": "ནང་འབྱུང་ལས་ཀྱི་རིམ་པ་ནི། །\nསས་ནི་ལུས་ཀྱི་གཞི་བྱས་ཏེ། །\nབསྐྱེད་པས་ཤ་ནི་སྨིན་པར་འདོད། །"
    },
    "realization": "foundation",
    "status": "Locally supported physical construction under P1; no shared reassignment",
    "reason": "Earth explicitly provides the bodily foundation. Retain foundation rather than impose technical Ground or replace it with basis merely for uniformity. This disposition does not yet cover U01339 or settle the other Ground-of-words and chapter-outline uses.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-063",
    "pairs": [
      "DTG-000578",
      "DTG-000579",
      "DTG-000584"
    ],
    "ids": [
      "A2000-C01-S01",
      "U01275",
      "U01276",
      "U01277",
      "U01286"
    ],
    "source": {
      "DTG-000578": "ཆུ་ཡི་ཟུག་པས་དབང་པོ་སྡུད།\nབྱེར་བ་ཡིས་ནི་འཁྲུགས་པར་བྱེད།\nསྙོམས་པ་ཡིས་ནི་འབྲས་བུ་འབྱིན།",
      "DTG-000579": "ས་ཡི་ཟུག་པས་རྡུལ་རྣམས་འབྱིན། །\nབྱེར་བ་ཡིས་ནི་ཡན་ལག་འབྱིན། །\nསྙོམས་པས་ལུས་འབྱུང་རྫོགས་པའོ། །",
      "DTG-000584": ""
    },
    "realization": "water triad present; bodily limbs",
    "status": "Current source restoration recognized; specific bodily sense repaired; other constructions provisional",
    "reason": "The three water verses are present at A2000-C01-S01. U01286 remains the qualified inherited omission query, not evidence of a current missing water triad. Retain all source annotations, twelve announced functions and repeated operations. The unnamed pair, entering another and ritual classifications remain unresolved; the bodily limbs repair is not a new universal yan lag assignment.",
    "review": "REVIEW.md#phase-d-notes-05"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T68",
    "pairs": [
      "DTG-000487"
    ],
    "ids": [
      "U01074",
      "U01075",
      "U01076",
      "U01077"
    ],
    "source": {
      "DTG-000487": "དེ་ནས་ལས་ཀྱི་བྱེ་བྲག་ལས། །\nསེམས་ཅན་ཉོན་མོངས་མངོན་མེད་ཀྱང༌། །\nབག་ལ་ཉལ་བ་ལངས་པའི་དབང་། །\nཤིན་ཏུ་ཕྲ་བ་བླངས་པའི་གཟུགས། །"
    },
    "realization": "dormant tendencies (retained provisionally)",
    "status": "Existing whole-expression proposal remains provisional; related approved label clarified",
    "reason": "Keep bag la nyal ba distinct from bag chags, now assigned imprints by P2 rather than the historical note's habitual tendencies comparator. No unconscious mechanism is inferred, and later occurrences require their own reading before the family scope can be reconciled.",
    "review": "REVIEW.md#phase-d-notes-05"
  }
]
```

**Important justified retentions and rejected false positives:** The explicit four birth modes retain warmth rather than an unprinted substitute. Ordinary beings (`འགྲོ་བ`), embodied beings (`ལུས་ཅན`), bodhisattvas and the whole wind-mind compound are not changed merely because nearby sems can becomes karmic being. DTG-000462's Word-Specialist/Glorious/holder boundary remains N-050: an English or Tibetan substring does not settle whether dzin is part of a name or the upholding predicate. The source-based lineage names and non-abiding terminal predicate remain qualified without historical identification.

DTG-000520's **substances** is retained under the dngos po row's material-context exception: the clause explicitly concerns taste transforming its objects into nectar in the bodily/sensory sequence. This is not a free synonym for entity, a claim that all entities are matter, or certification of the described practice's efficacy. DTG-000512's bodily foundation is likewise not silently promoted to technical Ground or rewritten to basis for stylistic consistency. The question/array/branch numbers remain as written, with the newly linked main-count question distinguished from the still-qualified gnad dus phrase.

The source's actions/clothing/faculties list is not emended to food or body. The omission notice at U01144 does not license an invented touch instruction or decide the nectar fragment's referent. The eightfold physiological list retains its order and the printed negative “primordial knowing is not clear”; no bodily-fluid interpretation of byang chub sems is silently adopted. Seasonal orders differ between passages and remain different. The sixty/thirty/thirty, seven fire/seven water/fourteen, 180-period, 720 mornings/evenings and 360-day counts are not forced into an external chronology. The twelve-animal sequence keeps snake before dragon. U01233's single displaced formation/destruction/emptiness note is not treated as multiple independent annotations.

The restored water triad is present at DTG-000578; the historical missing-water finding is therefore rejected as a current omission defect. U01286's annotation remains separately qualified, and the unnamed penetration-pair, entering-another clause and ritual categories remain open. Summon/stir and other printed variants remain separated from root prose. The elemental operations are not collapsed, rationalized or expanded into practical instructions. The long N-064 sequence preserves explicit negations, one/many, repeated completion language, intrinsic nature, self-appearance and primordial knowing; changing the first condition does not settle its unstated subject or Ground-of-words construction.

**Pre-commit self-check rejection of a proposed note update:** The ninth provisional disposition above, N-T68, is **rejected and is being withdrawn**, not adopted. Its claim that P2 assigned bag chags to imprints is unsupported. The actual eight-column row is `བག་ཆགས་` / `Habitual tendencies`, with blank scope/forms/exceptions/related fields, source `G, line 74`, status `Established`. The full-row recheck therefore requires removing the newly appended N-T68 usage record and active-index paragraph below, leaving the existing historical and active N-T68 text unchanged. The older dormant-tendencies proposal remains provisional and distinct from habitual tendencies. This records a correction to this review's own proposed note, not a change to owner approval history or a new shared label. No English pair repair in this batch depends on the rejected claim.

```json
{
  "file": "translations/2026-10-01-golden-aligned/LEGACY-NOTES.md",
  "anchor": "n-t68",
  "before": "**Phase D disposition, 2026-10-05 (continuation 03):** Existing whole-expression proposal remains provisional; related approved label clarified. Keep bag la nyal ba distinct from bag chags, now assigned imprints by P2 rather than the historical note's habitual tendencies comparator. No unconscious mechanism is inferred, and later occurrences require their own reading before the family scope can be reconciled. [Current review and scope](REVIEW.md#phase-d-notes-05).\n\n",
  "after": "",
  "usage_action": "Remove only the just-appended session-03 N-T68 disposition; preserve all seventeen inherited records and the eight other supported session-03 dispositions.",
  "reason": "Actual full glossary row retains Habitual tendencies; imprints was an unsupported proposed-policy claim.",
  "severity": "medium",
  "confidence": "high"
}
```

**Application, changed-clause self-check and validation:** All 25 English repairs in 22 pairs and the numerical-question link were applied and checked against the current Tibetan in a 57-pair changed-clause/context view. The wish-condition, filial relation, physical-limbs sense, complete category labels, number, possessors, modifiers and remaining qualified constructions were rechecked. No source, negation, agent, temporal relation, chapter count or technical component changed beyond the recorded corrections. The unsupported N-T68 note proposal was withdrawn as documented above; eight supported append-only note/usage dispositions remain.

The final paired validator and projector check were actually rerun: both exit 1 at the historical protected-glossary check. The full operation-replay/integrity check exits 0, reproducing 129 pair operations: 110 English repairs in 101 distinct pairs and 19 review links, affecting 112 pair payloads including note-only changes. All 2,667 pair identities/order, fixed source/golden/policy/format/lineage, inherited note associations, historical usage/index records and 698 local-link targets pass. The earlier annotation repair remains unchanged. English SHA-256: `3e3a8e68ead43189ecc244276bb60f4932c1ec7c4516c15915cb3232641bb944`. `git diff --check` passes. No new reader output was produced. This is a repair self-check, not another independent review.

**Saved semantic coverage:** 600/2,667 pairs, ordinals 1–600 through DTG-000597, with 156 first-encountered note records read. Continue at ordinal 601 / DTG-000598. The connected N-064 context through ordinal 615 was read but is not separately counted as completed coverage. The whole-work pass remains in progress; text readiness remains provisional.

<a id="phase-d-batch-06"></a>
### Batch 06 — source ordinals 601–750

All 150 current pairs DTG-000598–000747 and all 39 first-encountered note records were read in source order. The connected N-064 argument was completed, as were the U01493–U01513 dream sequence and the bodily/channel sequences; ordinals 751–760 were additionally read as continuation context, not added to completed coverage. The note-view method is the same as Batch 05: current fixed Tibetan and all note prose/qualifications are read; only duplicate historical unit quotations are elided in the convenience view. Q1–Q9, I §8.1 and III govern. The complete relevant rows, including bare dngos versus dngos po, goms process/state, bcud scope, wind-mind, rtog med, the complete lamp expression, realm and spiritual accomplishment, were rechecked; I §8.1 was reread directly.

**Evidence before application:** The following 21 English operations in 20 pairs extend the confirmed labels and repair three local attachment/syntax issues. S13 puts nyid with direct perception rather than key point; E04 fixes the combining-clause syntax without recreating the historically corrected object/time transposition; S12 distinguishes the practitioner condition from its appearing object. Two further constructions are linked provisionally rather than forcibly corrected.

<!-- phase-d-batch-06-operations -->
```json
[
  {
    "pair": "DTG-000603",
    "ordinal": 606,
    "golden": [
      "U01319"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འདི་ཤེས་འཁོར་བའི་ལམ་འགག་གོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved khor ba label without changing the blocking predicate, this/knowing antecedent or its place in the connected view sequence."
  },
  {
    "pair": "DTG-000615",
    "ordinal": 618,
    "golden": [
      "U01334"
    ],
    "family": "T02",
    "kind": "translation",
    "tibetan": "འདིས་ཀྱང་འཁོར་བའི་སྒོ་འགག་གོ། །",
    "before": "samsara",
    "after": "cyclic existence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Apply the approved khor ba label without changing the blocking predicate, this/knowing antecedent or its place in the connected view sequence."
  },
  {
    "pair": "DTG-000604",
    "ordinal": 607,
    "golden": [
      "U01320",
      "U01321"
    ],
    "family": "S13/T09",
    "kind": "translation",
    "tibetan": "གནད་ལས་བྱུང་བའི་མངོན་སུམ་ཉིད། །\nགོམས་པའི་སྟོབས་ཀྱིས་འཁྲུལ་པ་འཇིག །",
    "before": "Direct perception arising from the crucial point itself—",
    "after": "Direct perception itself, arising from the key point—",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Nyid follows mngon sum and emphasizes direct perception, not the preceding gnad. Restore its modifier attachment and apply key point. Familiarity remains the approved state form; the following delusion-destruction clause and its implicit topic relation are not expanded."
  },
  {
    "pair": "DTG-000678",
    "ordinal": 681,
    "golden": [
      "U01481"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྩ་རྣམས་ཁུངས་སུ་བཟུང་བ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000680",
    "ordinal": 683,
    "golden": [
      "U01484"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "བརྗོད་པའི་རྒྱུན་རྣམས་གཅད་པ་གནད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000682",
    "ordinal": 685,
    "golden": [
      "U01487"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "གཉིད་ལ་གོམས་པ་གནད་ཡིན་ནོ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000685",
    "ordinal": 688,
    "golden": [
      "U01493",
      "U01494"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "རྨི་ལམ་གནད་ཀྱི་ལམ་ཁྱེར་ནི། །\nསྔོན་དུ་བྱ་དང་གནད་ལ་དབབ། །",
    "before": "crucial points of dreams onto the path\nconsists of preparation and applying the crucial points",
    "after": "key points of dreams onto the path\nconsists of preparation and applying the key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000687",
    "ordinal": 690,
    "golden": [
      "U01499",
      "U01500",
      "U01501",
      "U01502",
      "U01503",
      "U01504"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ནས་གནད་ལ་འབེབས་དུས་སུ། །\nསྦྱང་དང་བསྒྱུར་དང་བཅད་པ་དང༌། །\nདཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །\nབསྐྱིལ་བཟློག་ལས་ཀྱི་གནད་བྱས་པས། །\nལས་ཀྱི་རྨི་ལམ་མཐའ་ཟད་དེ། །\nབག་ཆགས་འཁྲུལ་པ་དྲུང་ནས་ཐོན། །",
    "before": "crucial points:\ntraining, transformation, cutting off, and\nstirring, concentrating the vitality, and releasing at the crucial point;\nby applying the crucial points",
    "after": "key points:\ntraining, transformation, cutting off, and\nstirring, concentrating the vitality, and releasing at the key point;\nby applying the key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000700",
    "ordinal": 703,
    "golden": [
      "U01533",
      "U01534",
      "U01535"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དངོས་གཞི་རང་གི་རྒྱུད་བརྟེན་ནི། །\nལུས་ཀྱི་གནད་དང་ངག་དང་ཡང་། །\nསེམས་ཀྱི་གནད་ལ་བརྟེན་པ་ཡིས། །",
    "before": "crucial points of body and speech\nand the crucial point",
    "after": "key points of body and speech\nand the key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000710",
    "ordinal": 713,
    "golden": [
      "U01558",
      "U01559",
      "U01560",
      "U01561",
      "U01562",
      "U01563",
      "U01564",
      "U01565",
      "U01566"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ལུས་ཀྱི་གནད་ནི་རྩ་ཡིན་ཏེ། །\nགནས་དང་བཀོད་པ་འགྱུ་བ་དང་། །\nའཁོར་ལོའི་རྟེན་དང་ལུས་ཀྱི་སྲོག །\nམིང་དང་བྱེ་བྲག་རྒྱུ་དང་རྐྱེན། །\nབྱེད་པའི་ལས་དང་མཚན་ཉིད་དང༌། །\nཉོན་མོངས་ལས་དང་ཡེ་ཤེས་ལས། །\nལམ་ལ་བརྟེན་ནས་མངོན་སྣང་བ། །\nནད་དང་འབྱུང་བའི་བྱེ་བྲག་དང༌། །\nའཁྲུག་མར་གནས་པའི་མཐའ་ཡིས་དབྱེ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000715",
    "ordinal": 718,
    "golden": [
      "U01571",
      "U01572"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ལྟར་རྩ་ཡིས་གནད་ཀྱིས་ཀྱང༌། །\nསངས་རྒྱས་གནས་ནི་མཚོན་པའོ། །",
    "before": "crucial points",
    "after": "key points",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000719",
    "ordinal": 722,
    "golden": [
      "U01579",
      "U01580",
      "U01581",
      "U01582",
      "U01583"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "ཡང་ན་མཁས་པས་གནད་ཉིད་བཙལ། །\nརྩ་ནས་ངེས་པར་འགྱུ་བ་ནི། །\nའབུམ་ཕྲག་གཅིག་དང་ཁྲི་ཕྲག་གཉིས། །\nསྟོང་ཕྲག་དྲུག་དང་བརྒྱ་ཕྲག་དྲུག །\nརྩ་ནས་ངེས་པར་འབྱུང་བ་སྟེ། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000722",
    "ordinal": 725,
    "golden": [
      "U01587"
    ],
    "family": "T09",
    "kind": "translation",
    "tibetan": "དེ་ཡི་གནད་ཀྱིས་སྦྱོར་ཐབས་འབད། །",
    "before": "crucial point",
    "after": "key point",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Every changed occurrence corresponds to gnad in this exact clause. Preserve singular/plural and the complete channel, dream, body/speech/ordinary-mind or timing construction. This does not approve the unresolved operations or their practical efficacy."
  },
  {
    "pair": "DTG-000660",
    "ordinal": 663,
    "golden": [
      "U01440",
      "U01441"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "རང་ལོའི་འབྱུང་བ་བཅུད་པ་ལ། །\nགནས་སུ་ཕྱིན་པས་ངེས་པར་འགྲུབ། །",
    "before": "vitality",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Bcud occurs in the extraction/concentration sense, not the receptacle-and-inhabitants construction. Apply the approved label while keeping the already qualified taking/concentrating construction and its actual own-year or dream-practice scope."
  },
  {
    "pair": "DTG-000687",
    "ordinal": 690,
    "golden": [
      "U01499",
      "U01500",
      "U01501",
      "U01502",
      "U01503",
      "U01504"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "དེ་ནས་གནད་ལ་འབེབས་དུས་སུ། །\nསྦྱང་དང་བསྒྱུར་དང་བཅད་པ་དང༌། །\nདཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །\nབསྐྱིལ་བཟློག་ལས་ཀྱི་གནད་བྱས་པས། །\nལས་ཀྱི་རྨི་ལམ་མཐའ་ཟད་དེ། །\nབག་ཆགས་འཁྲུལ་པ་དྲུང་ནས་ཐོན། །",
    "before": "vitality",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Bcud occurs in the extraction/concentration sense, not the receptacle-and-inhabitants construction. Apply the approved label while keeping the already qualified taking/concentrating construction and its actual own-year or dream-practice scope."
  },
  {
    "pair": "DTG-000661",
    "ordinal": 664,
    "golden": [
      "U01442",
      "U01443",
      "U01444",
      "U01445",
      "U01446"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "བཅུད་ཀྱིས་ལེན་པར་འདོད་པས་ནི། །\nབདུད་རྩི་རྣམ་ལྔ་སྦྱར་བའི་ཐབས། །\nགཞན་དུ་འབྱུང་བ་སྙོམས་པ་ལ། །\nམཁས་པས་ཆ་སྙོམས་ལེགས་སྦྱར་ནས། །\nརིན་པོ་ཆེ་ཡི་སྣོད་དུ་བླུགས། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the confirmed bcud kyis len pa label repair to this actual nourishment construction. Retain the qualified whole phrase, skilled person, explicit materials, sequence and conspicuous editorial warning; no recipe or safety claim is added."
  },
  {
    "pair": "DTG-000663",
    "ordinal": 666,
    "golden": [
      "U01449",
      "U01450",
      "U01451",
      "U01452",
      "U01453"
    ],
    "family": "T13",
    "kind": "translation",
    "tibetan": "དངུལ་ཆུའི་ཐིགས་པ་རེ་བླངས་ནས། །\nནང་བཞིན་སྲན་མའི་རྡོག་མ་ཙམ། །\nམཁས་པ་དག་གིས་ཟ་སྤྱོད་ན། །\nབཅུད་ཀྱིས་ལེན་པ་ཆེན་པོར་ཡང་། །\nའགྱུར་བ་ཐེ་ཚོམ་མི་ཟའོ། །",
    "before": "vital essences",
    "after": "quintessence",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Extend the confirmed bcud kyis len pa label repair to this actual nourishment construction. Retain the qualified whole phrase, skilled person, explicit materials, sequence and conspicuous editorial warning; no recipe or safety claim is added."
  },
  {
    "pair": "DTG-000723",
    "ordinal": 726,
    "golden": [
      "U01588",
      "U01589"
    ],
    "family": "T04",
    "kind": "translation",
    "tibetan": "ཆེན་པོ་ལ་ནི་དུས་བརྩི་སྟེ། །\nམཆོག་དང་ཐུན་མོང་དངོས་གྲུབ་བརྟག །",
    "before": "supreme and common accomplishments",
    "after": "supreme and common spiritual accomplishments",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Preserve both supreme and common modifiers and the spiritual component of the complete dngos grub label. Do not apply the label to generic grub/sgrub or thob elsewhere in this range."
  },
  {
    "pair": "DTG-000740",
    "ordinal": 743,
    "golden": [
      "U01628",
      "U01629",
      "U01630",
      "U01631",
      "U01632",
      "U01633"
    ],
    "family": "T19",
    "kind": "translation",
    "tibetan": "དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །\nགཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ། །\nརེག་གི་ཁམས་ལ་བརྟགས་པ་ཡིས། །\nའཇིག་རྟེན་ཐུན་མོང་ལས་མཐའ་དང༌། །\nམངོན་པར་ཤེས་པ་རྫོགས་པ་དང་། །\nཞིང་ཁམས་རྣམས་ལ་ལོངས་སྤྱོད་དོ། །",
    "before": "the fields",
    "after": "the realms",
    "severity": "medium",
    "confidence": "high",
    "rationale": "Zhing khams names realms enjoyed after the listed accomplishments; there is no operative material-field metaphor. Retain number and the distinct mngon par shes pa expression; this is not higher doctrine."
  },
  {
    "pair": "DTG-000654",
    "ordinal": 657,
    "golden": [
      "U01420",
      "U01421",
      "U01422",
      "U01423",
      "U01424"
    ],
    "family": "E04",
    "kind": "translation",
    "tibetan": "མཁའ་འགྲོ་དབང་དུ་སྡུད་པའི་མིས། །\nམ་མོ་འདུ་བའི་སར་ཕྱིན་ནས། །\nརིན་པོ་ཆེ་ཡི་སྦྱོར་བ་དག །\nའབྱུང་བའི་མགོ་ཉིད་འཚོགས་དུས་སུ། །\nལེགས་པར་སྦྱར་ཏེ་རི་ལུ་ཉིད། །",
    "before": "A person gathering ḍākinīs under his power,\nhaving gone to a place where mamos assemble,\na preparation of precious substances— [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\nat the time when the heads of the elements meet, [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\nproperly combines [them] into the pill itself. [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)",
    "after": "A person gathering ḍākinīs under his power,\nhaving gone to a place where mamos assemble,\nproperly combines a preparation of precious substances— [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\nat the time when the heads of the elements meet— [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)\ninto the pill itself. [N-068](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-068)",
    "severity": "minor",
    "confidence": "high",
    "rationale": "Move the existing English verb before its object so the named person, not the preparation, is the grammatical actor. Keep the preparation-before-time order already corrected historically at U01422–U01423; do not recreate that transposition. Remove only the now-unneeded bracketed object pronoun, retaining the pill/result, every source component and all three note links. No ingredient or new operation is supplied."
  },
  {
    "pair": "DTG-000735",
    "ordinal": 738,
    "golden": [
      "U01617",
      "U01618"
    ],
    "family": "S12/T24",
    "kind": "translation",
    "tibetan": "ཉིན་མཚན་མེད་པར་གོམས་སྤྱོད་ན། །\nའདི་ཉིད་རྩོལ་བྲལ་མངོན་དུ་སྣང་། །",
    "before": "Engaging in familiarity without [distinguishing] day and night,",
    "after": "When one engages in familiarization without [distinguishing] day and night,",
    "severity": "medium",
    "confidence": "high",
    "rationale": "The source goms spyod na is the practitioner condition, whereas di nyid is the thing appearing in the following clause. Remove the dangling English participle that attaches engaging to that demonstrative; use the approved process form familiarization. Preserve the qualified day/night phrase, direct appearance and freedom from effort."
  },
  {
    "pair": "DTG-000706",
    "ordinal": 709,
    "golden": [
      "U01545",
      "U01546",
      "U01547"
    ],
    "family": "PD-Q06-01",
    "kind": "review-link",
    "tibetan": "བསོད་ནམས་ལས་ཀྱི་བྱེད་པའོ། །\nའགྲོ་བའི་བཀྲག་དང་གཟི་མདངས་བསྐྱེད། །\nམཆེད་ཅིང་སྡུད་པའི་ལས་ཀུན་བྱེད། །",
    "before": "It performs the activities of merit and karma;\nit generates beings' luster and splendor;\nit performs every activity of spreading and gathering.\n\nEarlier notes: [N-074](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-074).",
    "after": "It performs the activities of merit and karma;\nit generates beings' luster and splendor;\nit performs every activity of spreading and gathering.\n\nEarlier notes: [N-074](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-074).\n\nReview note: [Merit/karma construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q06-01).",
    "severity": "documentation",
    "confidence": "high for source scope and linkage",
    "rationale": "Link the exact unresolved construction and competing analyses without changing the main English or treating a component/substring match as proof of an error."
  },
  {
    "pair": "DTG-000740",
    "ordinal": 743,
    "golden": [
      "U01628",
      "U01629",
      "U01630",
      "U01631",
      "U01632",
      "U01633"
    ],
    "family": "PD-Q06-02",
    "kind": "review-link",
    "tibetan": "དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །\nགཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ། །\nརེག་གི་ཁམས་ལ་བརྟགས་པ་ཡིས། །\nའཇིག་རྟེན་ཐུན་མོང་ལས་མཐའ་དང༌། །\nམངོན་པར་ཤེས་པ་རྫོགས་པ་དང་། །\nཞིང་ཁམས་རྣམས་ལ་ལོངས་སྤྱོད་དོ། །",
    "before": "Through the culmination of activities examined in actuality,\nand through examining the domains of form, sound, smell, taste,\nand touch, [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03)\nthe culmination of common worldly activities\nand higher knowing are perfected,\nand one enjoys the realms.\n\nEarlier notes: [N-077](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-077), [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).",
    "after": "Through the culmination of activities examined in actuality,\nand through examining the domains of form, sound, smell, taste,\nand touch, [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03)\nthe culmination of common worldly activities\nand higher knowing are perfected,\nand one enjoys the realms.\n\nEarlier notes: [N-077](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-077), [N-T03](../translations/2026-10-01-golden-aligned/LEGACY-NOTES.md#n-t03).\n\nReview note: [Bare dngos construction provisional](../translations/2026-10-01-golden-aligned/REVIEW.md#pd-q06-02).",
    "severity": "documentation",
    "confidence": "high for source scope and linkage",
    "rationale": "Link the exact unresolved construction and competing analyses without changing the main English or treating a component/substring match as proof of an error."
  }
]
```

<a id="pd-q06-01"></a>
#### PD-Q06-01 — Merit and karma, or meritorious karma?

**DTG-000706 / U01545:** `བསོད་ནམས་ལས་ཀྱི་བྱེད་པའོ། །`. Current English: “It performs the activities of merit and karma.” Retain provisionally. The worldly-wind list supplies the acting wind, but bsod nams las may be a modifier-plus-karma expression (candidate “meritorious karma”) rather than two coordinate objects. Conversely, the absence of dang alone does not prove coordination impossible in a compressed list. No new conjunction or modifier analysis is imposed solely from a component lookup. An internal parallel with an explicit relationship, or authorized commentary on this nominal phrase, would settle it. **Severity:** medium possible modifier/coordination difference. **Confidence:** moderate that the construction needs qualification; no alternative is certified.

<a id="pd-q06-02"></a>
#### PD-Q06-02 — Nominal objects versus actuality

**DTG-000740 / U01628–U01633**, beginning `དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །`. Current English begins “Through the culmination of activities examined in actuality”. The following explicit examination of form/sound/smell/taste/touch domains supports testing the alternative “activities of examining entities”; the present wording instead takes dngos la as an actuality construction. The bare-form row expressly requires this analysis and permits actuality when justified. Retain the clause provisionally rather than treat la or an English substring as conclusive. A decisive parallel distinguishing objects examined from activities tested in actuality, or authorized commentary, would settle the attachment. The separate, explicit actual/nonactual transference contrast at DTG-000743–000746 is not automatically an entity contrast. **Severity:** medium possible object/modifier difference. **Confidence:** moderate for the unresolved boundary, high that an automatic entity substitution is not licensed.

<a id="phase-d-notes-06"></a>
**Active note/usage additions recorded before application:** The following narrow dispositions extend the existing index/usage history without rewriting old proposals or adding a canonical assignment.

```json
[
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T30",
    "pairs": [
      "DTG-000618"
    ],
    "ids": [
      "U01338",
      "U01339"
    ],
    "source": {
      "DTG-000618": "ཕུན་སུམ་ཚོགས་པ་དྲུག་ཅུ་ཡིས། །\nབསྟན་པ་དམ་པའི་གཞི་མ་འཛིན། །"
    },
    "realization": "foundation",
    "status": "Locally supported ordinary teaching-support construction under P1",
    "reason": "U01339 has now been read in the complete qualities account: the teacher upholds the teaching through sixty excellences. Foundation is retained locally, not changed to technical Ground or replaced with basis merely for uniformity. This extends only the earlier physical-foundation disposition to the separately evidenced teaching-support construction; no shared glossary reassignment results.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-066",
    "pairs": [
      "DTG-000627",
      "DTG-000628",
      "DTG-000629",
      "DTG-000630",
      "DTG-000631",
      "DTG-000632",
      "DTG-000633",
      "DTG-000634",
      "DTG-000635",
      "DTG-000636",
      "DTG-000637"
    ],
    "ids": [
      "U01354",
      "U01355",
      "U01356",
      "U01357",
      "U01358",
      "U01359",
      "U01360",
      "U01361",
      "U01362",
      "U01363",
      "U01364",
      "U01365",
      "U01366",
      "U01367",
      "U01368",
      "U01369",
      "U01370",
      "U01371",
      "U01372",
      "U01373",
      "U01374",
      "U01375",
      "U01376",
      "U01377",
      "U01378",
      "U01379",
      "U01380"
    ],
    "source": {
      "DTG-000627": " སྐུ་གསུམ་བསླབ་པའི་རིམ་པ་ཉིད། །\nའབྱུང་བའི་འདོད་དོན་གཙོར་བྱས་ཏེ། །\nམཆོག་ཏུ་ས་ཆུ་མེ་རླུང་གི། །\nསྒྲ་ལ་བསླབས་པས་ངེས་པར་འགྲུབ། །",
      "DTG-000628": "ཆུ་ཡི་སྒྲ་ནི་གཤང་བ་ལ། །\nམཁའ་འགྲོ་མ་ཡི་སྒྲ་དབྱངས་འཛིན། །",
      "DTG-000629": "འདི་ལ་རྟག་ཏུ་གོམས་བྱས་ན། །\nསྤྲུལ་པའི་སྐུ་ཡང་ངེས་པར་འགྲུབ། །",
      "DTG-000630": "ས་ཡི་སྒྲ་ནི་བསིལ་ཞིང་ལྗི། །\nཚངས་པ་ཆེན་པོའི་སྒྲ་སྐད་ལྡན། །",
      "DTG-000631": "འདི་ལ་རྟག་ཏུ་བརྟན་སྤྱོད་ན། །\nལོངས་སྤྱོད་རྫོགས་སྐུ་ངེས་འགྲུབ་པའོ། །",
      "DTG-000632": "མེ་ཡི་སྒྲ་ནི་རིང་བྱེད་བསླབ། །\nཁྱབ་འཇུག་ཆེན་པོའི་གསུང་དབྱངས་སྟོན། །",
      "DTG-000633": "འདི་ལ་མཉན་པར་སུས་སྤྱོད་པ། །\nཆོས་སྐུའི་ཡོན་ཏན་ངེས་པར་འཐོབ། །",
      "DTG-000634": "རླུང་གི་སྒྲ་ནི་གཟིར་ཞིང་དྲག །\nམཁའ་ལྡིང་རྒྱལ་པོའི་སྦྱོར་བ་གསུང་། །",
      "DTG-000635": "འདི་ནི་རྟག་ཏུ་ཟློ་ཤེས་ན། །\nསྐུ་གསུམ་ཐུན་མོང་བསླབ་བྱའོ། །",
      "DTG-000636": "དེ་ལྟར་འབྱུང་བཞིའི་སྒྲ་དོན་ནི། །\nཕྱི་ཡི་དུས་ལ་ངེས་པར་སྦྱོར། །\nདགུན་དང་དཔྱིད་དང་དབྱར་དང་སྟོན། །\nཆུ་དང་ས་སྟེ་མེ་རླུང་གི། །",
      "DTG-000637": "རིམ་པ་དུས་དང་ངེས་སྦྱར་ཏེ། །\nརྣལ་འབྱོར་ལུས་དང་བསྟུན་བྱས་ན། །\nའགྲུབ་པར་ཐེ་ཚོམ་མི་ཟའོ། །"
    },
    "realization": "sound; word and meaning",
    "status": "P1 acoustic exception adopted within the actual acoustic clauses",
    "reason": "The voice/melody, listening and elemental-sound clauses support sound. The complete sgra don expression at U01374 keeps word and meaning. The old proposed-exception status is historical. Gshang, lengtheners, the All-Pervader and sky-soarer designation/application remain qualified; no mantra or seasonal scheme is imported.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-068",
    "pairs": [
      "DTG-000654",
      "DTG-000660"
    ],
    "ids": [
      "U01420",
      "U01421",
      "U01422",
      "U01423",
      "U01424",
      "U01440",
      "U01441"
    ],
    "source": {
      "DTG-000654": "མཁའ་འགྲོ་དབང་དུ་སྡུད་པའི་མིས། །\nམ་མོ་འདུ་བའི་སར་ཕྱིན་ནས། །\nརིན་པོ་ཆེ་ཡི་སྦྱོར་བ་དག །\nའབྱུང་བའི་མགོ་ཉིད་འཚོགས་དུས་སུ། །\nལེགས་པར་སྦྱར་ཏེ་རི་ལུ་ཉིད། །",
      "DTG-000660": "རང་ལོའི་འབྱུང་བ་བཅུད་པ་ལ། །\nགནས་སུ་ཕྱིན་པས་ངེས་པར་འགྲུབ། །"
    },
    "realization": "grammatical combining clause; quintessence",
    "status": "Minimal English repair and approved component; whole ritual constructions provisional",
    "reason": "The preparation still precedes the time clause in source order; only the existing English verb is placed before its object. No old alignment error is reintroduced. Quintessence repairs the bcud component at U01440 without resolving its full own-year construction. Ingredient identities, absorbed/combined and A/ali alternatives, quantities and application referents stay qualified.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T16",
    "pairs": [
      "DTG-000661",
      "DTG-000663"
    ],
    "ids": [
      "U01442",
      "U01443",
      "U01444",
      "U01445",
      "U01446",
      "U01449",
      "U01450",
      "U01451",
      "U01452",
      "U01453"
    ],
    "source": {
      "DTG-000661": "བཅུད་ཀྱིས་ལེན་པར་འདོད་པས་ནི། །\nབདུད་རྩི་རྣམ་ལྔ་སྦྱར་བའི་ཐབས། །\nགཞན་དུ་འབྱུང་བ་སྙོམས་པ་ལ། །\nམཁས་པས་ཆ་སྙོམས་ལེགས་སྦྱར་ནས། །\nརིན་པོ་ཆེ་ཡི་སྣོད་དུ་བླུགས། །",
      "DTG-000663": "དངུལ་ཆུའི་ཐིགས་པ་རེ་བླངས་ནས། །\nནང་བཞིན་སྲན་མའི་རྡོག་མ་ཙམ། །\nམཁས་པ་དག་གིས་ཟ་སྤྱོད་ན། །\nབཅུད་ཀྱིས་ལེན་པ་ཆེན་པོར་ཡང་། །\nའགྱུར་བ་ཐེ་ཚོམ་མི་ཟའོ། །"
    },
    "realization": "taking nourishment from quintessence",
    "status": "Approved P2 component in further occurrences; whole construction provisional",
    "reason": "Extend the already recorded local nourishment treatment to U01442 and U01452. The old vital-essences variant is superseded only in these current clauses. The historical prescription remains explicitly editorially cautioned, and unidentified ingredients, objects and sequence are not reconstructed.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-072",
    "pairs": [
      "DTG-000685",
      "DTG-000686",
      "DTG-000687",
      "DTG-000688",
      "DTG-000689",
      "DTG-000690",
      "DTG-000691"
    ],
    "ids": [
      "U01493",
      "U01494",
      "U01495",
      "U01496",
      "U01497",
      "U01498",
      "U01499",
      "U01500",
      "U01501",
      "U01502",
      "U01503",
      "U01504",
      "U01505",
      "U01506",
      "U01507",
      "U01508",
      "U01509",
      "U01510",
      "U01511",
      "U01512",
      "U01513"
    ],
    "source": {
      "DTG-000685": "རྨི་ལམ་གནད་ཀྱི་ལམ་ཁྱེར་ནི། །\nསྔོན་དུ་བྱ་དང་གནད་ལ་དབབ། །",
      "DTG-000686": "སྔོན་དུ་ལུས་ངག་སེམས་སྦྱངས་ཏེ། །\nའབྱོངས་པའི་རྟགས་ལ་བརྟེན་ནས་ནི། །\nབརྟག་དང་ཟིལ་གྱིས་གནོན་པ་དང༌། །\nབག་ཆགས་གསུམ་པོ་ངེས་གཟུང་བྱ། །",
      "DTG-000687": "དེ་ནས་གནད་ལ་འབེབས་དུས་སུ། །\nསྦྱང་དང་བསྒྱུར་དང་བཅད་པ་དང༌། །\nདཀྲུགས་དང་བཅུད་དང་གནད་ལ་འབོར། །\nབསྐྱིལ་བཟློག་ལས་ཀྱི་གནད་བྱས་པས། །\nལས་ཀྱི་རྨི་ལམ་མཐའ་ཟད་དེ། །\nབག་ཆགས་འཁྲུལ་པ་དྲུང་ནས་ཐོན། །",
      "DTG-000688": "འདི་དུས་རང་གི་བརྩོན་འགྲུས་ཀྱིས། །\nརབ་ལ་ཆད་དང་འབྲིང་ལ་ཤེས། །\nཐ་མ་འགྱུར་བར་ངེས་པ་སྟེ། །",
      "DTG-000689": "འདི་དག་རྨི་ལམ་ཐོག་མ་ཡང༌། །\nརབ་ལ་བརྗེད་དང་ཐ་མ་འགགས། །\nའབྲིང་ལ་ཤིན་ཏུ་གསལ་བ་ལ། །\nཐ་མ་ཡིན་པ་ཤེས་པའོ། །",
      "DTG-000690": "ཐ་མ་མི་གསལ་དེ་ནས་འགྱུར། །",
      "DTG-000691": "དེ་རྣམས་ཀྱིས་ནི་ཚད་ལ་ཕེབ། །"
    },
    "realization": "key point; quintessence; habitual tendencies",
    "status": "Complete continuation read; approved components applied; graded relationships still provisional",
    "reason": "The full U01493–U01513 sequence has now been read together, not stopped at an old authoring-batch boundary. All actions, examination/overpowering/habitual-tendency triad and repeated inferior-grade statements are preserved. The already qualified concentrating construction takes quintessence; no new procedural definition or hierarchy is inferred.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-T34",
    "pairs": [
      "DTG-000707"
    ],
    "ids": [
      "U01548",
      "U01549",
      "U01550",
      "U01551",
      "U01552",
      "U01553",
      "U01554",
      "U01555"
    ],
    "source": {
      "DTG-000707": "འདས་པའི་སྐུ་དང་ཡེ་ཤེས་དང༌། །\nཐིག་ལེ་ཉིད་ལ་གོམས་པ་དང༌། །\nཡང་ཞིང་སྟོང་དང་གསལ་བར་ཁྱབ། །\nལུས་ཀྱི་འབྱུང་བ་ཟད་པ་དང་། །\nསེམས་ཀྱི་རྟོག་པ་འགགས་པ་དང༌། །\nམི་རྟོག་ཡེ་ཤེས་སྐྱེ་བ་དང༌། །\nཕྱི་ཡི་སྣང་བ་ཟད་པ་དང༌། །\nརླུང་སེམས་གཉིས་སུ་འདྲེས་པ་སྟེ། །"
    },
    "realization": "wind and ordinary mind, the two",
    "status": "Supported local two-member analysis; not a replacement for canonical wind-mind",
    "reason": "The explicit gnyis and mixing construction support retaining both separately named members in this clause. Their precise gnyis su relation remains qualified; no merging into one or nondual result is supplied. This does not authorize splitting the established wind-mind expression in other constructions.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-071",
    "pairs": [
      "DTG-000676",
      "DTG-000677",
      "DTG-000678",
      "DTG-000679",
      "DTG-000680",
      "DTG-000681",
      "DTG-000682",
      "DTG-000683",
      "DTG-000684"
    ],
    "ids": [
      "U01477",
      "U01478",
      "U01479",
      "U01480",
      "U01481",
      "U01482",
      "U01483",
      "U01484",
      "U01485",
      "U01486",
      "U01487",
      "U01488",
      "U01489",
      "U01490",
      "U01491",
      "U01492"
    ],
    "source": {
      "DTG-000676": " གཉིད་ཀྱི་རྣལ་འབྱོར་སུས་བསྒོམ་པ། །\nའདིས་ནི་གཏི་མུག་ལམ་དུ་བྱེད། །",
      "DTG-000677": "ཕྱི་ཡི་དུས་ནི་གཞི་དག་ལས། །\nརྣལ་འབྱོར་ལུས་ཀྱི་རྩལ་སྦྱངས་ཏེ། །",
      "DTG-000678": "རྩ་རྣམས་ཁུངས་སུ་བཟུང་བ་གནད། །",
      "DTG-000679": "ནང་གི་དུས་ནི་བཞི་ཉིད་ཀྱིས། །\nརྣལ་འབྱོར་དག་གི་རྩལ་སྦྱངས་ཏེ། །",
      "DTG-000680": "བརྗོད་པའི་རྒྱུན་རྣམས་གཅད་པ་གནད། །",
      "DTG-000681": "གསང་བའི་དུས་ནི་བཞི་ཡིས་ཀྱང་། །\nརྣལ་འབྱོར་སེམས་ཀྱི་རྩལ་སྦྱངས་ཏེ། །",
      "DTG-000682": "གཉིད་ལ་གོམས་པ་གནད་ཡིན་ནོ། །",
      "DTG-000683": "ཁོ་ན་ཉིད་ཀྱི་དུས་བཞི་ཡིས། །\nལུས་དང་ངག་སེམས་ངེས་བསྡུས་ནས། །\nའོད་གསལ་ཆེན་པོ་གཉིད་དང་བསྲེ། །",
      "DTG-000684": "དེ་ལྟར་གོམས་ནས་སྐུ་གསུམ་ལ། །\nངེས་པར་སྦྱོར་རོ་རྣལ་འབྱོར་པས། །"
    },
    "realization": "key point; dull confusion and suchness retained provisionally",
    "status": "Approved gnad labels; shared-control family questions remain open",
    "reason": "The current fixed reading gzhi dag is not silently changed to bzhi/four. Technical Ground versus an ordinary basis and dag attachment remain provisional at U01479. Gti mug and kho na nyid remain unapproved whole labels; gti mug will be compared with rmongs/rmugs and the affliction lists, preserving ignorance, delusion and technical dullness. The separate body/yoga/ordinary-mind expressiveness and clear-light/sleep mixing remain visible.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-076",
    "pairs": [
      "DTG-000727",
      "DTG-000728",
      "DTG-000730",
      "DTG-000733",
      "DTG-000735"
    ],
    "ids": [
      "U01597",
      "U01598",
      "U01599",
      "U01600",
      "U01601",
      "U01602",
      "U01603",
      "U01604",
      "U01605",
      "U01608",
      "U01609",
      "U01610",
      "U01613",
      "U01614",
      "U01617",
      "U01618"
    ],
    "source": {
      "DTG-000727": "ཐིག་ལེའི་ཆོས་ཉིད་བརྟན་འདོད་པས། །\nདོན་དམ་དང་ནི་ཀུན་རྫོབ་ལས། །",
      "DTG-000728": "རེ་ཞིག་ཀུན་རྫོབ་ཐིག་ལེ་ལ། །\nབརྟེན་ནས་སངས་རྒྱས་འདོད་པ་ཡིས། །\nརིགས་མ་མཚན་ཉིད་རྫོགས་པ་ནི། །\nལྷ་དང་ལྷ་མིན་ཚངས་པ་དང༌། །\nགལ་ཏེ་རིགས་ངན་མུ་སྟེགས་སམ། །\n མཚན་ཉིད་རྫོགས་པ་དག་མཐོང་ན། །\nའགུགས་པའི་སྦྱོར་བ་ངེས་བརྩམས་ནས། །",
      "DTG-000730": "དེ་ནས་ཀུན་རྫོབ་ཐིག་ལེ་ཉིད། །\nདབབ་ཅིང་གཟུང་དང་བཟློག་པ་དང༌། །\nརྩ་ལ་གདབ་ཅིང་རླུང་དང་བསྲེ། །",
      "DTG-000733": "དོན་དམ་ཐིག་ལེ་བརྟན་པ་ཡིས། །\nཆོས་སྐུ་སྟོང་པའི་ཡུལ་རྣམས་རྙེད། །",
      "DTG-000735": "ཉིན་མཚན་མེད་པར་གོམས་སྤྱོད་ན། །\nའདི་ཉིད་རྩོལ་བྲལ་མངོན་དུ་སྣང་། །"
    },
    "realization": "relative/ultimate spheres retained provisionally; familiarization",
    "status": "P3 paired-label evaluation pending shared assignment; local condition repaired",
    "reason": "The owner-preferred superficial/superfactual pair was tested together against the sphere distinction: the former is linked to the woman/channels/wind sequence, the latter to empty dharma-embodiment domains and the canonical lamp of the empty sphere. This supports a paired proposal but does not settle the physical/visionary scope or authorize a new shared default. Retain current relative/ultimate provisionally; do not apply either proposal to mthar thug or generic English adjectives. The full characteristics repetition, family-woman qualification, caste wording as source language, and unspecified techniques remain intact. At U01617 only the practitioner condition/process is repaired, not its appearing object.",
    "review": "REVIEW.md#phase-d-notes-06"
  },
  {
    "session": "DTG-PD-20261005-Astra-03",
    "legacy_note": "N-077",
    "pairs": [
      "DTG-000740",
      "DTG-000742",
      "DTG-000743",
      "DTG-000744",
      "DTG-000745",
      "DTG-000746",
      "DTG-000747"
    ],
    "ids": [
      "U01628",
      "U01629",
      "U01630",
      "U01631",
      "U01632",
      "U01633",
      "U01635",
      "U01636",
      "U01637",
      "U01638",
      "U01639",
      "U01640",
      "U01641",
      "U01642",
      "U01643",
      "U01644",
      "U01645",
      "U01646",
      "U01647"
    ],
    "source": {
      "DTG-000740": "དངོས་ལ་བརྟགས་པའི་ལས་མཐའ་ཡིས། །\nགཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ། །\nརེག་གི་ཁམས་ལ་བརྟགས་པ་ཡིས། །\nའཇིག་རྟེན་ཐུན་མོང་ལས་མཐའ་དང༌། །\nམངོན་པར་ཤེས་པ་རྫོགས་པ་དང་། །\nཞིང་ཁམས་རྣམས་ལ་ལོངས་སྤྱོད་དོ། །",
      "DTG-000742": "འཕོ་བའི་བྱེ་བྲག་རྣམ་པ་གསུམ། །\nདབང་པོ་དག་གི་དབྱེ་བ་ཡིས། །\nའོད་གསལ་བ་དང་སྒྱུ་ལུས་དང༌། །\nཐ་མ་ལུས་ངག་ཡིད་ལའོ། །",
      "DTG-000743": "ལུས་ངག་འཕོ་བ་རྣམ་པ་གཉིས། །\nདངོས་སུ་འཕོ་དང་དངོས་མེད་དོ། །",
      "DTG-000744": "དངོས་ནི་རླུང་གིས་སྦྱང་བའི་ཐབས། །",
      "DTG-000745": "སྒྲ་དང་བཟོ་དང་སྒྱུ་རྩལ་དང་། །\nརྟེན་ཅིང་འབྲེལ་ལ་སྦྱངས་པས་ནི། །\nསོ་སོའི་འབྱུང་བ་ནང་མཐུན་པས། །\nལུས་ངག་ཡིད་ཀྱིས་གཏད་པས་འགྲུབ། །",
      "DTG-000746": "དངོས་མེད་སེམས་ཀྱི་གོམས་སྟོབས་བརྟན། །",
      "DTG-000747": "སྒྱུ་ལུས་རྨི་ལམ་དག་ལ་སྦྱངས། །"
    },
    "realization": "realms; actuality construction provisional; actual/nonactual transference",
    "status": "Approved realm label; separate bare-form and whole-expression questions retained",
    "reason": "Dngos la at U01628 is now linked as a nominal-objects versus actuality construction question. Do not force it to entity from the spelling alone. The explicit actual/nonactual transference contrast and method-versus-ordinary-mind-familiarity explanation support retaining those contextual adjective senses at U01639–U01646. Transference, word/craft/illusory-expressiveness and the dream/illusory-body scope remain provisional whole-expression treatments; the ensuing intermediate-state continuation is read as context, not yet added to this batch coverage.",
    "review": "REVIEW.md#phase-d-notes-06"
  }
]
```

**Justified retentions and rejected false positives:** The explicit acoustic passages retain sound while the complete word-and-meaning expression is preserved. The four season/element correspondences, cool/heavy and pressing/fierce descriptions, and unidentified designations are not made more familiar. General accomplishment/attainment verbs are not turned into spiritual accomplishment. All explicit speech/ordinary-mind/mental-faculty distinctions, the main-practice compound and nonliterary personal continuum remain intact. The force of methods is procedural in the local applications; it is not changed merely to conform to a book-wide preference for means.

The actual fixed gzhi dag reading in the sleep passage remains separate from the tempting four-reading. The complete preparatory and operative dream lists were read through their repeated inferior-grade results; none is deleted or reassigned to produce an elegant hierarchy. Habitual tendencies is the unchanged established label, not imprints. The distinct source wind/ordinary-mind two-member wording does not erase wind-mind elsewhere. The eight channel operations retain their individual verbs and qualified objects, and the two counts remain 21,600 and 126,600 without an added daily interval. The lamp of the empty sphere is an established complete expression, not a fresh assembly of components.

The visible N-069 editorial warning is retained as editorial, not attributed to the Tibetan. No ingredient identity, dose conversion, anatomical location, missing characteristic, procedure, medical efficacy or ritual efficacy is supplied. The current main/variant separation at U01414/01417/01422/01439/01567 is already correct; the historical transposition and merged-annotation criticisms are not reused as current defects. N-076's bracketed her refers to the already qualified woman; its compressed characteristics construction is not rewritten merely because a fuller paraphrase is easier to read. Its physical/visionary scope and proposed family-woman label remain open. The P3 superficial/superfactual test remains a paired, source-scoped shared-label proposal, not an activated default or a blanket replacement for English relative/ultimate.

**Application, changed-clause self-check and validation:** All 21 English operations in 20 pairs and both construction-question links were applied and rechecked in a 53-pair changed-clause/context view against the complete Tibetan clauses. The direct-perception emphasis, combining agent/object, source-order preparation/time relationship and practitioner condition were checked explicitly. Number, negation, possessors, qualifications, distinct technical components and the editorial safety warning remain intact. All nine scoped note/usage additions preserve the inherited records. This is repair self-verification, not another independent review.

The final paired validator and projector check were rerun; both still exit 1 at the historical protected-glossary contract. The full recorded-operation replay/integrity check passes all 2,667 pairs, fixed source/golden/policy/format/lineage, inherited note associations/history and 700 English local-link targets. Current totals are 152 operations: 131 English repairs in 121 distinct pairs and 21 review links, affecting 133 pair payloads including note-only changes, plus the previously recorded separate annotation repair. The usage file now has 34 Phase D dispositions, with all 25 inherited from the preceding commit unchanged. English SHA-256: `5f9bc5bf9897eecb087f6c35ba890bd549a28726e60b54e571205623712d08bf`. `git diff --check` passes. No dependent reader was produced by the blocked projector.

**Saved coverage:** 750/2,667 pairs, ordinals 1–750 through DTG-000747, with 195 first-encountered note records. Continue at ordinal 751 / DTG-000748. Ordinals 751–760 have additionally been read as connected context, not counted as completed coverage. Text remains provisional and the whole-work pass is still in progress.

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

**Batch 02 repair self-check (same reviewer):** all 23 newly changed pairs and the corrected source-annotation sentence were reread against their complete Tibetan strings. Both members of the cyclic-existence/sorrow and sacred-pledge/vow contrasts remain; the aware/matter question preserves the knowing contrast without asserting that bodies are immaterial. The literary title/exposition context supports the scoped tantra occurrences, including the earlier question at DTG-000023; this resolves that Batch 01 question without generalizing all rgyud. The incomplete short Ema and other linked construction limits remain. No new agent, causal clause, numeral, negation or possession was introduced by the label repairs. The secret-preliminary and tenet-system constructions remain subject to the recorded later-reply comparison rather than an unqualified whole-work approval. Actual integrity replay passes all 42 recorded pair operations across 38 distinct pairs, the single note operation, unchanged fixed source and 2,667 IDs/order, unchanged per-pair old note associations, and all 685 current local-link targets. Historical annotation English remains visible alongside the current correction. Deferred legacy-status integration is explicitly listed in the batch disposition, not reported as already done.

**Batch 03 actual verification (continuation 02; repair self-check, not another independent review):** all revised clauses were reread against the exact Tibetan and full glossary rows, including necessary surrounding pairs. The complete revised English span DTG-000197–DTG-000297 was read continuously from the canonical file after application. Both key-point occurrences, the skilled agent/instrument, the beyond-six/below relationship, and the generic reflexive addressee remain source-supported. No numeral, negation, named agent, causal relation, or embodiment/knowing component was added or lost by these repairs. The unresolved constructions remain linked, not silently certified.

The actual read-only integrity check passes: replay of all **73 pair operations** (62 English repairs plus 11 review links) exactly reproduces every current pair payload from frozen main; **57 English-repair pairs / 65 changed pairs including note-only changes**. Fixed Tibetan bytes and golden hash, all **2,667** shared IDs/order/envelopes, all inherited per-pair note associations, **694** current English local link targets, and adopted policy hashes pass. Original usage records and the first six Phase D dispositions are unchanged; exactly five dated dispositions were appended. Removing only the five dated additions reproduces the prior legacy index byte-for-byte. `git diff --check` passes. Canonical English SHA-256: `ef0aecded418e6ef1e2dfdb03a9f53bfe45444cb6c185608be431d3962087c5b`. One attempted custom display command was blocked before execution; the successful canonical-file read and subsequent integrity checks, not that blocked attempt, support these results. No semantic regression fixture is claimed executed by this check.

### Canonical and generated layers

`paired/translation.md` is the sole current authored English. The dated September draft and October 1 readers/JSON are historical release outputs, not separately edited current translations. `paired/MANIFEST.json` and `paired/v2/PAIR-AUDIT.json` describe the released paired import. Existing builders require exact released English and old policy inputs; rerunning them cannot silently become a post-review build. Their signed contracts, receipts and tags will not be rewritten to make revised working English appear historically signed off. Applicable builds will still be attempted and actual failures reported. Any bounded working-output integration left unsupported by the existing process will be distinguished from semantic coverage.

## Coverage versus text disposition

**Current coverage:** 300/2,667 semantic pairs reviewed (source ordinals 1–300); 2,367 remain unreviewed. **Text disposition:** in review, not ready for a whole-work acceptance claim. **Applied changed pairs:** 57 with English repairs (62 scoped operations); 65 including eight additional note-only pairs. The one source-annotation note repair, 11 new review links and legacy-status additions are counted separately. Batch 03 repairs are self-checked; full-work review remains incomplete. **Unresolved questions/shared proposals:** see batch records; whole-work totals not yet established. No human certification, new release, or harmonization of the other three works is claimed.

## Continuation

Continue at source-order ordinal 301, DTG-000298, after the applied and self-checked Batch 03 repairs. The exact next unreviewed ranges are Chapter 1 ordinals 301–1199 and all Chapters 2–6/closing (1200–2667). Keep the original Tibetan, all stable IDs/roles/formats, notes and historic releases intact. Save review progress and small explicit commits on `review/post-translation-20261005`.

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
