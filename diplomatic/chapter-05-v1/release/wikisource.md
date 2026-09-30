# Chapter 5 — related Wikisource reference comparison

**Release candidate — final gate pending**

W is the stored related Wylie transcription, not an independent printing. All 40 non-equal alignment blocks have explicit decisions. Exact original W lines and source Wylie remain quoted; stripped signs and collapsed spaces were used for alignment only.

[Stored provenance](../../../editions/adzom-wikisource/PROVENANCE.json) · [Reading](reading.md) · [Apparatus](apparatus.md)

Attribution: Wikisource revision 439571 and its contributor history, retained in the provenance file. The related text retains its applicable attribution/share-alike terms; this edition grants no additional rights.

<a id="w-c05-001"></a>
## W-C05-001 — U04782

**Original A Tibetan:**
```json
[
  "མ་གོལ་གནས་པའི་བསྒོམ་པ་གང༌། །"
]
```

**Original A Wylie:**
```json
[
  "ma gol gnas pa'i bsgom pa gang*/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4828,
    "raw": "mgo la gnas pa'i bsgom pa gang\n",
    "page_marker": 180,
    "start": 151487,
    "end": 151518
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ma gol",
    "W": "mgo la"
  }
]
```

**Decision:** Retain ma gol in the question; W mgo la is a differently segmented lexical reading, not a reason to turn non-straying into a head-location instruction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-002"></a>
## W-C05-002 — U04793

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་དང་པོ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan dang po/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan dang po",
    "W": ""
  }
]
```

**Decision:** Retain the first reply heading as a separate source heading. Its absence in the related website is not absence from Adzom; the native first-heading check supports its source role.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-003"></a>
## W-C05-003 — U04796

**Original A Tibetan:**
```json
[
  "གཏོང་བར་ནུས་ཤིང་བླ་མ་གུས། །"
]
```

**Original A Wylie:**
```json
[
  "gtong bar nus shing bla ma gus/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4842,
    "raw": "gtong bar nus shing bla mar gus\n",
    "page_marker": 181,
    "start": 151913,
    "end": 151945
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ma",
    "W": "mar"
  }
]
```

**Decision:** Keep bla ma gus; do not silently supply W final r merely to make a preferred grammatical attachment.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-004"></a>
## W-C05-004 — U04802

**Original A Tibetan:**
```json
[
  "ལུས་ངག་བྱ་བ་བྲལ་བ་དང་། །"
]
```

**Original A Wylie:**
```json
[
  "lus ngag bya ba bral ba dang /_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4848,
    "raw": "lus dag bya ba bral ba dang\n",
    "page_marker": 181,
    "start": 152109,
    "end": 152137
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ngag",
    "W": "dag"
  }
]
```

**Decision:** Retain ngag in lus ngag bya ba. W dag remains a quoted reference difference, not a certified print correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-005"></a>
## W-C05-005 — U04804

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་གཉིས་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan gnyis pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan gnyis pa",
    "W": ""
  }
]
```

**Decision:** Preserve the second reply heading, omitted in the website representation. No main-verse omission is inferred.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-006"></a>
## W-C05-006 — U04824

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་གསུམ་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan gsum pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan gsum pa",
    "W": ""
  }
]
```

**Decision:** Preserve the third reply label before its main paragraph; W omits that heading rather than supplying a replacement verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-007"></a>
## W-C05-007 — U04844

**Original A Tibetan:**
```json
[
  "ཆོས་ཉིད་སྟོང་པ་རིས་མེད་པས། །"
]
```

**Original A Wylie:**
```json
[
  "chos nyid stong pa ris med pas/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4889,
    "raw": "chos nyid stong pa'i ris med pas\n",
    "page_marker": 182,
    "start": 153385,
    "end": 153418
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "pa",
    "W": "pa'i"
  }
]
```

**Decision:** Retain stong pa ris med as supplied. W pai changes the particle and is not adopted without source evidence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-008"></a>
## W-C05-008 — U04850

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བཞི་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan bzhi pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bzhi pa",
    "W": ""
  }
]
```

**Decision:** Keep the fourth reply heading in its declared source-heading layer; its website absence does not delete it from the edition.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-009"></a>
## W-C05-009 — U04857

**Original A Tibetan:**
```json
[
  "ལུ་གུ་རྒྱུད་ལ་མངོན་དུ་སྤྱོད། །"
]
```

**Original A Wylie:**
```json
[
  "lu gu rgyud la mngon du spyod/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4902,
    "raw": "lu gu rgyud lam mngon du spyod\n",
    "page_marker": 183,
    "start": 153771,
    "end": 153802
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "la",
    "W": "lam"
  }
]
```

**Decision:** Keep la in lu gu rgyud la mngon du spyod. Do not fuse it with an m from W lam or change the source clause to an inferred path term.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-010"></a>
## W-C05-010 — U04860

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་ལྔ་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan lnga pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan lnga pa",
    "W": ""
  }
]
```

**Decision:** Preserve the fifth reply heading and exact original outer space; W heading omission does not alter source content.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-011"></a>
## W-C05-011 — U04865

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་དྲུག་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan drug pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan drug pa",
    "W": ""
  }
]
```

**Decision:** Keep the sixth reply label separate from root text; no witness-omission claim follows from W omission.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-012"></a>
## W-C05-012 — U04873

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་བདུན་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan bdun pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bdun pa",
    "W": ""
  }
]
```

**Decision:** Keep the seventh reply heading, including its exact original string in machine data. W has no equivalent heading line.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-013"></a>
## W-C05-013 — U04885

**Original A Tibetan:**
```json
[
  "ཞུས་ལན་བརྒྱད་པ།"
]
```

**Original A Wylie:**
```json
[
  "zhus lan brgyad pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan brgyad pa",
    "W": ""
  }
]
```

**Decision:** Preserve the eighth heading before the meditation paragraph, not as a newly supplied verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-014"></a>
## W-C05-014 — U04900

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་དགུ་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan dgu pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan dgu pa",
    "W": ""
  }
]
```

**Decision:** Retain the ninth heading and its base spelling. Website omission is a presentation difference in this comparison.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-015"></a>
## W-C05-015 — U04909

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་བཅུ་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan bcu pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu pa",
    "W": ""
  }
]
```

**Decision:** Retain the tenth reply heading before ma gol gnas pai bsgom pa ni; W does not govern heading removal.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-016"></a>
## W-C05-016 — U04923

**Original A Tibetan:**
```json
[
  "ཁ་དོག་ཡིག་འབྲུ་སྐྱུར་བྱེད་རྣམས། །"
]
```

**Original A Wylie:**
```json
[
  "kha dog yig 'bru skyur byed rnams/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4964,
    "raw": "kha dog yig 'bru sgyur byed rnams\n",
    "page_marker": 185,
    "start": 155675,
    "end": 155709
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "skyur",
    "W": "sgyur"
  }
]
```

**Decision:** Retain A skyur with the explicit unresolved reading recorded at L5-0015. W agrees with S sgyur but is related transcript evidence, not an additional independent scan vote.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-017"></a>
## W-C05-017 — U04925, U04926

**Original A Tibetan:**
```json
[
  "མ་གོལ་གནས་པའི་བསྒོམ་པའོ། །",
  "ཞུས་ལན་བཅུ་གཅིག་པ།"
]
```

**Original A Wylie:**
```json
[
  "ma gol gnas pa'i bsgom pa'o/_/",
  "zhus lan bcu gcig pa/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4966,
    "raw": "mgo la gnas pa'i bsgom pa'o\n",
    "page_marker": 185,
    "start": 155740,
    "end": 155768
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "ma gol",
    "W": "mgo la"
  },
  {
    "op": "delete",
    "A": "zhus lan bcu gcig pa",
    "W": ""
  }
]
```

**Decision:** Retain ma gol rather than the W segmentation mgo la, and preserve the eleventh heading omitted by W. Keep those two observations distinct.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-018"></a>
## W-C05-018 — U04939

**Original A Tibetan:**
```json
[
  " ཞུས་ལན་བཅུ་གཉིས་པ།"
]
```

**Original A Wylie:**
```json
[
  "_zhus lan bcu gnyis pa/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "zhus lan bcu gnyis pa",
    "W": ""
  }
]
```

**Decision:** Preserve the twelfth reply heading, which the website leaves out; no wording is inferred from the absence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-019"></a>
## W-C05-019 — U04951

**Original A Tibetan:**
```json
[
  "འདི་མན་ཆད་བསྡུས་དོན་བཤད།"
]
```

**Original A Wylie:**
```json
[
  "'di man chad bsdus don bshad/"
]
```

**Exact W lines and locations:**
```json
[]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "'di man chad bsdus don bshad",
    "W": ""
  }
]
```

**Decision:** Keep the physically distinct summary notice at U04951 as a source-section heading. Native PDF186 supports that role; W omission is not permission to lose the notice.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-020"></a>
## W-C05-020 — U04953

**Original A Tibetan:**
```json
[
  "གནས་པའི་ལྟ་བས་ཆོས་ཀུན་རྟོགས། །"
]
```

**Original A Wylie:**
```json
[
  "gnas pa'i lta bas chos kun rtogs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 4992,
    "raw": "gnas pa'i ltabs chos kun rtogs\n",
    "page_marker": 186,
    "start": 156582,
    "end": 156613
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "lta bas",
    "W": "ltabs"
  }
]
```

**Decision:** Keep the explicit lta bas sequence. W ltabs fuses characters into a different segmentation; record it rather than alter the main clause.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-021"></a>
## W-C05-021 — U04975

**Original A Tibetan:**
```json
[
  "དངོས་མེད་རང་བཞིན་རྫོགས་པ་ཆེ། །"
]
```

**Original A Wylie:**
```json
[
  "dngos med rang bzhin rdzogs pa che/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5015,
    "raw": "dngos med rang bzhin rdzogs pa chen\n",
    "page_marker": 187,
    "start": 157340,
    "end": 157376
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "che",
    "W": "chen"
  }
]
```

**Decision:** Retain che at the end of dngos med rang bzhin rdzogs pa che, rather than adding final n from W chen. No new source correction is established.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-022"></a>
## W-C05-022 — U04979

**Original A Tibetan:**
```json
[
  "རྣམ་རྟོག་ལས་ཀྱི་སྤྱོད་པ་རྟོགས་པའི་གདེང༌། །"
]
```

**Original A Wylie:**
```json
[
  "rnam rtog las kyi spyod pa rtogs pa'i gdeng*/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5019,
    "raw": "rnam rtog las kyi spyod pa rtogs pa'i gding\n",
    "page_marker": 187,
    "start": 157504,
    "end": 157548
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "gdeng",
    "W": "gding"
  }
]
```

**Decision:** Keep gdeng as supplied at U04979; W gding is preserved as a related spelling difference, not normalized across the chapter.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-023"></a>
## W-C05-023 — U04981

**Original A Tibetan:**
```json
[
  "ལུས་དང་ངག་ཡིད་དྭངས་པས་སྐུ་གསུམ་རྫོགས། །"
]
```

**Original A Wylie:**
```json
[
  "lus dang ngag yid dwangs pas sku gsum rdzogs/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5021,
    "raw": "lus dang ngag yid dangs bas sku gsum rdzogs\n",
    "page_marker": 187,
    "start": 157591,
    "end": 157635
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "dwangs pas",
    "W": "dangs bas"
  }
]
```

**Decision:** Retain dwangs pas in the body/speech/mind clause. Record both W dangs and bas; their conjunction does not authorize silently respelling the source.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-024"></a>
## W-C05-024 — U04989

**Original A Tibetan:**
```json
[
  "རྒྱུད་ལ་མ་བརྟེན་མན་ངག་གིས། །"
]
```

**Original A Wylie:**
```json
[
  "rgyud la ma brten man ngag gis/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5029,
    "raw": "rgyud lam brten man ngag gis\n",
    "page_marker": 187,
    "start": 157883,
    "end": 157912
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "la ma",
    "W": "lam"
  }
]
```

**Decision:** Keep rgyud la ma brten, including explicit ma. W lam brten alters both segmentation and the negative; do not erase the base negation from the reading.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-025"></a>
## W-C05-025 — U05004

**Original A Tibetan:**
```json
[
  "སྡིག་སྤྱད་པས་ནི་དགེ་ཐོབ་པོ། །"
]
```

**Original A Wylie:**
```json
[
  "sdig spyad pas ni dge thob po/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5045,
    "raw": "sdig spyad pas ni dge thob bo\n",
    "page_marker": 188,
    "start": 158360,
    "end": 158390
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "po",
    "W": "bo"
  }
]
```

**Decision:** Retain the final po at U05004 instead of a grammar-based switch to W bo. The source wording remains visible even when unusual.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-026"></a>
## W-C05-026 — U05007

**Original A Tibetan:**
```json
[
  "སྤྱོད་པ་སྤྱད་པས་གོལ་སྒྲིབ་ལ། །"
]
```

**Original A Wylie:**
```json
[
  "spyod pa spyad pas gol sgrib la/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5048,
    "raw": "spyod pa spyad pas go la sgrib la\n",
    "page_marker": 188,
    "start": 158461,
    "end": 158495
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "gol",
    "W": "go la"
  }
]
```

**Decision:** Keep gol in the supplied clause; W go la is an alternate segmentation and is not adopted as a correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-027"></a>
## W-C05-027 — U05035

**Original A Tibetan:**
```json
[
  "མི་བརྒྱ་ལྕགས་སྒྲོག་གཅིག་མ་ཐར། །"
]
```

**Original A Wylie:**
```json
[
  "mi brgya lcags sgrog gcig ma thar/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5077,
    "raw": "mi brgya lcags srog gcig ma thar\n",
    "page_marker": 189,
    "start": 159392,
    "end": 159425
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "sgrog",
    "W": "srog"
  }
]
```

**Decision:** Retain lcags sgrog in the hundred-people chain simile; W srog lacks the same initial group. This is a reference difference, not a new scan claim.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-028"></a>
## W-C05-028 — U05037

**Original A Tibetan:**
```json
[
  "ཐར་པས་གོང་དུ་གྲོལ་ལམ་ཟད། །"
]
```

**Original A Wylie:**
```json
[
  "thar pas gong du grol lam zad/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5079,
    "raw": "thar bas gong du grol lam zad\n",
    "page_marker": 189,
    "start": 159458,
    "end": 159488
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "pas",
    "W": "bas"
  }
]
```

**Decision:** Keep thar pas rather than W thar bas; the related website is not a basis for particle normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-029"></a>
## W-C05-029 — U05065

**Original A Tibetan:**
```json
[
  "ངག་ནི་རབ་ཏུ་གཅད་པར་བྱའོ། །"
]
```

**Original A Wylie:**
```json
[
  "ngag ni rab tu gcad par bya'o/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5108,
    "raw": "ngag ni rab tu bcad par bya'o\n",
    "page_marker": 190,
    "start": 160374,
    "end": 160404
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "gcad",
    "W": "bcad"
  }
]
```

**Decision:** Retain gcad par at U05065. W bcad is recorded without rewriting the supplied verbal form or construing this as a practical instruction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-030"></a>
## W-C05-030 — U05071

**Original A Tibetan:**
```json
[
  "ཕྲེང་བ་དོ་ཤལ་ཕྱེད་པ་ཡང་། །"
]
```

**Original A Wylie:**
```json
[
  "phreng ba do shal phyed pa yang /_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5114,
    "raw": "phring ba do shal phyed pa yang\n",
    "page_marker": 190,
    "start": 160572,
    "end": 160604
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "phreng",
    "W": "phring"
  }
]
```

**Decision:** Keep phreng ba rather than W phring ba; no source-backed vowel correction has been established.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-031"></a>
## W-C05-031 — U05080

**Original A Tibetan:**
```json
[
  "སྤྱོད་པ་བསྟེན་པས་ལུས་སྦྱོང་འགྱུར། །"
]
```

**Original A Wylie:**
```json
[
  "spyod pa bsten pas lus sbyong 'gyur/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5124,
    "raw": "blta ba bsten pas khams gsum chad\n",
    "page_marker": 191,
    "start": 160887,
    "end": 160921
  },
  {
    "line": 5125,
    "raw": "bsgom pa bsten pas 'khrul rgyun 'gags\n",
    "page_marker": 191,
    "start": 160921,
    "end": 160959
  },
  {
    "line": 5126,
    "raw": "spyod pa brten pas lus spyod 'gyur\n",
    "page_marker": 191,
    "start": 160959,
    "end": 160994
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "spyod",
    "W": "blta ba bsten pas khams gsum chad bsgom"
  },
  {
    "op": "insert",
    "A": "",
    "W": "'khrul rgyun 'gags spyod pa brten pas"
  },
  {
    "op": "replace",
    "A": "sbyong",
    "W": "spyod"
  }
]
```

**Decision:** Include A2000-C05-S01 after U05079: its two verses are established by actual Adzom PDF191. The alignment block also includes U05080, where W brten and lus spyod differ from supplied bsten and lus sbyong; retain the base there rather than treating the whole W block as an insertion to copy.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-032"></a>
## W-C05-032 — U05091

**Original A Tibetan:**
```json
[
  "སྦྱངས་པས་སེམས་ཀྱི་གནས་པར་འགྱུར། །"
]
```

**Original A Wylie:**
```json
[
  "sbyangs pas sems kyi gnas par 'gyur/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5137,
    "raw": "spyangs pas sems kyi gnas par 'gyur\n",
    "page_marker": 191,
    "start": 161314,
    "end": 161350
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "sbyangs",
    "W": "spyangs"
  }
]
```

**Decision:** Retain sbyangs rather than W spyangs. This reference distinction does not authorize changing the base spelling.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-033"></a>
## W-C05-033 — U05094

**Original A Tibetan:**
```json
[
  "མཚན་མ་མཚན་མ་བཟོ་ཡི་ཡང་བྱུང་ཐབས་བཟོའི་སྦྱོར་བ་ཡི། །"
]
```

**Original A Wylie:**
```json
[
  "mtshan ma mtshan ma bzo yi yang byung thabs bzo'i sbyor ba yi/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5140,
    "raw": "mtshan ma thabs bzo'i sbyor ba yi\n",
    "page_marker": 191,
    "start": 161419,
    "end": 161453
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "mtshan ma bzo yi yang byung",
    "W": ""
  }
]
```

**Decision:** Adopt only the main/note separation supported by PDF191. W omits the compact alternate, but the edition preserves that alternate in its own annotation layer with explicit lettering uncertainty.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-034"></a>
## W-C05-034 — U05106

**Original A Tibetan:**
```json
[
  "ཆོས་ཀྱི་འཁྲུལ་པས་ ཡེ་གཞི་ཡང་ཡས་གཞི་བྱས། །"
]
```

**Original A Wylie:**
```json
[
  "chos kyi 'khrul pas _ye gzhi yang yas gzhi byas/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5153,
    "raw": "chos kyi 'khrul pas yas gzhi byas\n",
    "page_marker": 192,
    "start": 161838,
    "end": 161872
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "ye gzhi yang",
    "W": ""
  }
]
```

**Decision:** Use the large-letter main yas gzhi and retain smaller ye gzhi yang separately, on native PDF192 evidence. W omission of the smaller words does not mean those source words are lost.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-035"></a>
## W-C05-035 — U05132

**Original A Tibetan:**
```json
[
  "འཁོར་དང་འདྲེས་པའི་གཞི་མ་བརྟེན་པའི་གཞི་མ་དང་ཡང་བྱུང་དག །"
]
```

**Original A Wylie:**
```json
[
  "'khor dang 'dres pa'i gzhi ma brten pa'i gzhi ma dang yang byung dag_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5180,
    "raw": "'khor dang 'dres pa'i gzhi ma dag\n",
    "page_marker": 193,
    "start": 162717,
    "end": 162751
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "delete",
    "A": "brten pa'i gzhi ma dang yang byung",
    "W": ""
  }
]
```

**Decision:** Keep the main gzhi ma dag and preserve the longer brten pai gzhi ma dang yang byung as a qualified source note. Native PDF193, not website agreement alone, supports the separation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c05-036"></a>
## W-C05-036 — U05144

**Original A Tibetan:**
```json
[
  "གཞན་ཡང་དག་པའི་སྣང་བ་བཤད། །"
]
```

**Original A Wylie:**
```json
[
  "gzhan yang dag pa'i snang ba bshad/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5192,
    "raw": "gzhan yang dad pa'i snang ba bshad\n",
    "page_marker": 193,
    "start": 163110,
    "end": 163145
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "dag",
    "W": "dad"
  }
]
```

**Decision:** Retain dag pai snang ba at U05144; W dad pai is an exact reference reading but not a source-supported replacement.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-037"></a>
## W-C05-037 — U05148

**Original A Tibetan:**
```json
[
  "ཉམས་ཀྱི་སྣང་བ་གོང་འཕེལ་ནི། །"
]
```

**Original A Wylie:**
```json
[
  "nyams kyi snang ba gong 'phel ni/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5196,
    "raw": "nyams gyi snang ba gong 'phel ni\n",
    "page_marker": 193,
    "start": 163239,
    "end": 163272
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "kyi",
    "W": "gyi"
  }
]
```

**Decision:** Keep nyams kyi as supplied rather than normalizing to W gyi. The difference remains independently visible in the reference apparatus.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-038"></a>
## W-C05-038 — U05171, U05172, U05173, U05174

**Original A Tibetan:**
```json
[
  "དུམ་བུ་རང་གི་ངོས་སུ་ཆད། །",
  "བར་ཆོད་ཉིད་ནི་འབྱུང་བའོ། །",
  "དཀར་གསལ་པདྨ་ལྟ་བུ་དང༌། །",
  "རྣོ་ཞིང་ཁ་དོག་སྣ་ཚོགས་ལ། །"
]
```

**Original A Wylie:**
```json
[
  "dum bu rang gi ngos su chad/_/",
  "bar chod nyid ni 'byung ba'o/_/",
  "dkar gsal pad+ma lta bu dang*/_/",
  "rno zhing kha dog sna tshogs la/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5220,
    "raw": "du ma bu rang gi ngos su chad\n",
    "page_marker": 194,
    "start": 163993,
    "end": 164023
  },
  {
    "line": 5221,
    "raw": "bar chad nyid ni 'byung ba'o\n",
    "page_marker": 194,
    "start": 164023,
    "end": 164052
  },
  {
    "line": 5222,
    "raw": "dkar gsal pad ma lta bu dang\n",
    "page_marker": 194,
    "start": 164052,
    "end": 164081
  },
  {
    "line": 5223,
    "raw": "rno zhin kha don sna tshogs la\n",
    "page_marker": 194,
    "start": 164081,
    "end": 164112
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "dum",
    "W": "du ma"
  },
  {
    "op": "replace",
    "A": "chod",
    "W": "chad"
  },
  {
    "op": "replace",
    "A": "pad+ma",
    "W": "pad ma"
  },
  {
    "op": "replace",
    "A": "zhing",
    "W": "zhin"
  },
  {
    "op": "replace",
    "A": "dog",
    "W": "don"
  }
]
```

**Decision:** Retain the four original anchor strings: dum bu, bar chod, pad+ma in source EWTS, and rno zhing kha dog. Record W du ma bu, bar chad, pad ma, zhin and kha don separately; transliteration spacing and lexical substitutions are not a single accepted normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-039"></a>
## W-C05-039 — U05176

**Original A Tibetan:**
```json
[
  " དམར་གསལ་དྭངས་པའི་ཟེར་འཕྲོ་ལ། །"
]
```

**Original A Wylie:**
```json
[
  "_dmar gsal dwangs pa'i zer 'phro la/_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5225,
    "raw": "dmar gsal dangs pa'i zer 'phrol\n",
    "page_marker": 194,
    "start": 164149,
    "end": 164181
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "dwangs",
    "W": "dangs"
  },
  {
    "op": "replace",
    "A": "'phro la",
    "W": "'phrol"
  }
]
```

**Decision:** Retain dwangs pai zer phro la; W dangs and phrol combine spelling and segmentation changes. No silent fusion of the terminal particle is made.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c05-040"></a>
## W-C05-040 — U05187, U05188, U05189

**Original A Tibetan:**
```json
[
  "ས་ནི་ལྡེག་དང་སིང་བ་དང༌། །",
  "ཟུར་ལ་འཕར་ཞིང་འདྲིལ་བས་འགྲུབ། །",
  "རླུང་ནི་སྦིར་ཞིང་གཟིར་བ་དང་། །"
]
```

**Original A Wylie:**
```json
[
  "sa ni ldeg dang sing ba dang*/_/",
  "zur la 'phar zhing 'dril bas 'grub/_/",
  "rlung ni sbir zhing gzir ba dang /_/"
]
```

**Exact W lines and locations:**
```json
[
  {
    "line": 5237,
    "raw": "sa ni ldeg dang sid pa dang\n",
    "page_marker": 195,
    "start": 164503,
    "end": 164531
  },
  {
    "line": 5238,
    "raw": "zur la 'bar zhing 'dril bas 'grub\n",
    "page_marker": 195,
    "start": 164531,
    "end": 164565
  },
  {
    "line": 5239,
    "raw": "rlung ni sdir zhing gzir ba dang\n",
    "page_marker": 195,
    "start": 164565,
    "end": 164598
  }
]
```

**Alignment differences:**
```json
[
  {
    "op": "replace",
    "A": "sing ba",
    "W": "sid pa"
  },
  {
    "op": "replace",
    "A": "'phar",
    "W": "'bar"
  },
  {
    "op": "replace",
    "A": "sbir",
    "W": "sdir"
  }
]
```

**Decision:** Keep supplied sing ba, phar and sbir in the sound-description sequence. W sid pa, bar and sdir remain exact recorded alternatives. The unusual sound terms are not replaced by expectations or interpreted as known technical sounds.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)
