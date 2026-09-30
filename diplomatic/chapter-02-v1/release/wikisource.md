# Chapter 2 - Wikisource reference comparison

**Release candidate - final gate pending**

105 blocks compare stored Adzom EWTS with the exact related Wylie reference. This is not a further independent printing. Normalization is for alignment only; the raw lines and all source positions remain preserved.

Source attribution and revision: [preserved provenance](../../../editions/adzom-wikisource/PROVENANCE.json). The source revision is 439571. Existing attribution and reuse terms remain those recorded in the repository method and source documentation.

[Reading](reading.md) - [Apparatus](apparatus.md) - [Structured comparison](apparatus.json)

<a id="w-c02-001"></a>
## W-C02-001 - U02714, U02715

**Original Adzom Tibetan:**
```json
["འདུ་བ་བརྒྱ་ལ་བརྒྱད་ཀྱང་བྱེད་པ་གཅིག །", "ལས་ཀུན་རྫོགས་པས་མཐའ་ཡས་འབྱུང༌། །"]
```

**Original source Wylie:**
```json
["'du ba brgya la brgyad kyang byed pa gcig_/", "las kun rdzogs pas mtha' yas 'byung*/_/"]
```

**Exact W lines:**
```json
[{"line": 2747, "raw": "'du ba brgyal byed pa gcig\n", "page_marker": 105, "start": 86362, "end": 86389}, {"line": 2748, "raw": "las kun rdzogs pas mtha' yas 'gyur\n", "page_marker": 105, "start": 86389, "end": 86424}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "brgya la brgyad kyang", "W": "brgyal"}, {"op": "replace", "A": "'byung", "W": "'gyur"}]
```

**Decision:** Retain main brgya la and the separate brgyad kyang note established by PDF105; do not fuse them to W brgyal. Retain U02715 byung rather than W gyur. The website is related transcript evidence, not an independent scan reading.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-002"></a>
## W-C02-002 - U02721

**Original Adzom Tibetan:**
```json
["དེ་ཡང་མིང་གཟུགས་འཁྲུལ་པའི་ཆ། །"]
```

**Original source Wylie:**
```json
["de yang ming gzugs 'khrul pa'i cha/_/"]
```

**Exact W lines:**
```json
[{"line": 2754, "raw": "de yang ming gzugs 'khrul ba'i cha\n", "page_marker": 105, "start": 86591, "end": 86626}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa'i", "W": "ba'i"}]
```

**Decision:** Retain U02721 pa'i rather than W ba'i; preserve the exact pa/ba spelling difference without normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-003"></a>
## W-C02-003 - U02726

**Original Adzom Tibetan:**
```json
["ལས་ཀུན་འགྱུར་བྱེད་བཞི་ས་བརྩིའོ། །"]
```

**Original source Wylie:**
```json
["las kun 'gyur byed bzhi sa brtsi'o/_/"]
```

**Exact W lines:**
```json
[{"line": 2759, "raw": "las kun 'gyur byed bzhi chas brtsi'o\n", "page_marker": 105, "start": 86762, "end": 86799}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "sa", "W": "chas"}]
```

**Decision:** Retain U02726 sa rather than W chas, also recorded in S. Agreement of digital versions does not license a new Adzom correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-004"></a>
## W-C02-004 - U02730

**Original Adzom Tibetan:**
```json
["ལས་ཡུལ་བརྩི་བ་དེ་ཙམ་མོ། །"]
```

**Original source Wylie:**
```json
["las yul brtsi ba de tsam mo/_/"]
```

**Exact W lines:**
```json
[{"line": 2763, "raw": "las yul brtsi bde tsam mo\n", "page_marker": 105, "start": 86900, "end": 86926}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "ba de", "W": "bde"}]
```

**Decision:** Retain U02730 ba de as separate syllables rather than W bde. Do not collapse the sequence into a different word.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-005"></a>
## W-C02-005 - U02733

**Original Adzom Tibetan:**
```json
["ལས་དང་བྱེད་པ་རེག་ཤེས་ལྔ། །"]
```

**Original source Wylie:**
```json
["las dang byed pa reg shes lnga/_/"]
```

**Exact W lines:**
```json
[{"line": 2766, "raw": "las dang byed pa rig shes lnga\n", "page_marker": 105, "start": 86995, "end": 87026}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "reg", "W": "rig"}]
```

**Decision:** Retain U02733 reg against W rig. The vowel difference remains explicit and is not settled by interpretation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-006"></a>
## W-C02-006 - U02740

**Original Adzom Tibetan:**
```json
["བྱས་ཚོགས་ཀྱང་ཚེ་གྲངས་ནི་དྲུག་ཅུ་སྟེ། །"]
```

**Original source Wylie:**
```json
["byas tshogs kyang tshe grangs ni drug cu ste/_/"]
```

**Exact W lines:**
```json
[{"line": 2774, "raw": "byas tshe grangs ni drug cu ste\n", "page_marker": 106, "start": 87234, "end": 87266}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "tshogs kyang", "W": ""}]
```

**Decision:** W omits tshogs kyang, matching the corrected main-layer sequence. Preserve the smaller source note separately under the PDF106 intervention; absence from W alone would not authorize deletion.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-007"></a>
## W-C02-007 - U02767

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་གཉིས་པ།"]
```

**Original source Wylie:**
```json
["dris lan gnyis pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan gnyis pa", "W": ""}]
```

**Decision:** Retain the second-reply heading U02767 separately. Its absence from W is not a missing root verse or a reason to remove the Adzom heading.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-008"></a>
## W-C02-008 - U02780, U02781

**Original Adzom Tibetan:**
```json
["འཇུག་པའི་ལས་ནི་ཐད་ཀའོ། །", "དྲིས་ལན་གསུམ་པ།"]
```

**Original source Wylie:**
```json
["'jug pa'i las ni thad ka'o/_/", "dris lan gsum pa/"]
```

**Exact W lines:**
```json
[{"line": 2814, "raw": "'jug pa'i las ni tha dka'o\n", "page_marker": 107, "start": 88531, "end": 88558}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "thad ka'o dris lan gsum pa", "W": "tha dka'o"}]
```

**Decision:** Retain U02780 thad ka'o rather than W tha dka'o, and retain the third-reply heading U02781 which W lacks. Segmentation and heading omission are distinct observations.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-009"></a>
## W-C02-009 - U02787

**Original Adzom Tibetan:**
```json
["འགྱུ་བ་རང་ཐག་ཆོད་པའོ། །"]
```

**Original source Wylie:**
```json
["'gyu ba rang thag chod pa'o/_/"]
```

**Exact W lines:**
```json
[{"line": 2820, "raw": "'gyu ba rang thog chod pa'o\n", "page_marker": 107, "start": 88731, "end": 88759}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "thag", "W": "thog"}]
```

**Decision:** Retain U02787 thag rather than W thog; no vowel correction is adopted from the website.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-010"></a>
## W-C02-010 - U02801, U02802

**Original Adzom Tibetan:**
```json
["ཡང་ནི་འཁྲུལ་པ་མིན་པའི་གནད། །", "གཅིག་ཤེས་པ་ཡིས་ཐམས་ཅད་གྲོལ། །"]
```

**Original source Wylie:**
```json
["yang ni 'khrul pa min pa'i gnad/_/", "gcig shes pa yis thams cad grol/_/"]
```

**Exact W lines:**
```json
[{"line": 2835, "raw": "yang ni 'khrul pa man pa'i gnang\n", "page_marker": 108, "start": 89173, "end": 89206}, {"line": 2836, "raw": "gcig shes pa yis thams cad gol\n", "page_marker": 108, "start": 89206, "end": 89237}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "min", "W": "man"}, {"op": "replace", "A": "gnad", "W": "gnang"}, {"op": "replace", "A": "grol", "W": "gol"}]
```

**Decision:** Retain U02801 min and gnad and U02802 grol against W man, gnang and gol. The three differences are kept together in their exact two-line context, not repaired in either quotation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-011"></a>
## W-C02-011 - U02805

**Original Adzom Tibetan:**
```json
["འབྱུང་རིག་གནས་ཀྱི་རྟོག་པ་ཟད། །"]
```

**Original source Wylie:**
```json
["'byung rig gnas kyi rtog pa zad/_/"]
```

**Exact W lines:**
```json
[{"line": 2839, "raw": "'byung rig gnas kyi tog pa zad\n", "page_marker": 108, "start": 89297, "end": 89328}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rtog", "W": "tog"}]
```

**Decision:** Retain U02805 rtog against W tog. The missing romanized subjoined element is not silently normalized.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-012"></a>
## W-C02-012 - U02813

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཞི་པ།"]
```

**Original source Wylie:**
```json
["dris lan bzhi pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bzhi pa", "W": ""}]
```

**Decision:** Retain the fourth-reply heading U02813 outside the main verse; W omission is a heading-scope difference.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-013"></a>
## W-C02-013 - U02815

**Original Adzom Tibetan:**
```json
["རྩ་བའི་རྟེན་འབྲེལ་ལ་འཁྱལ་པས། །"]
```

**Original source Wylie:**
```json
["rtsa ba'i rten 'brel la 'khyal pas/_/"]
```

**Exact W lines:**
```json
[{"line": 2848, "raw": "rtsa ba'i rten 'brel la 'khyal bas\n", "page_marker": 108, "start": 89581, "end": 89616}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pas", "W": "bas"}]
```

**Decision:** Retain U02815 pas rather than W bas. The separately recorded B/S khril reading is not conflated with this website pa/ba difference.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-014"></a>
## W-C02-014 - U02829

**Original Adzom Tibetan:**
```json
["འགྲོ་བའི་འབྱུང་རིགས་བཅུ་གཉིས་འགྱུར། །"]
```

**Original source Wylie:**
```json
["'gro ba'i 'byung rigs bcu gnyis 'gyur/_/"]
```

**Exact W lines:**
```json
[{"line": 2863, "raw": "'go ba'i 'byung rigs bcu gnyis 'gyur\n", "page_marker": 109, "start": 90049, "end": 90086}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'gro", "W": "'go"}]
```

**Decision:** Retain U02829 gro rather than W go; no consonant-stack correction follows from the related transcription.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-015"></a>
## W-C02-015 - U02847

**Original Adzom Tibetan:**
```json
["འགྲོ་བའི་ལས་དང་བསོད་ནམས་དང་། །"]
```

**Original source Wylie:**
```json
["'gro ba'i las dang bsod nams dang /_/"]
```

**Exact W lines:**
```json
[{"line": 2882, "raw": "'gro ba'i las dang bsang nams dang\n", "page_marker": 110, "start": 90659, "end": 90694}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "bsod", "W": "bsang"}]
```

**Decision:** Retain U02847 bsod against W bsang. Preserve the unexpected W form without replacing it with a familiar compound in the source quotation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-016"></a>
## W-C02-016 - U02849, U02850

**Original Adzom Tibetan:**
```json
["བྱེ་བྲག་སོ་སོར་སྣང་བར་བྱེད། །", "གཞན་ཡང་སྣོད་དང་བཅུད་དག་གི། །"]
```

**Original source Wylie:**
```json
["bye brag so sor snang bar byed/_/", "gzhan yang snod dang bcud dag gi/_/"]
```

**Exact W lines:**
```json
[{"line": 2884, "raw": "bye brag so so snang ba byed\n", "page_marker": 110, "start": 90726, "end": 90755}, {"line": 2885, "raw": "gzhan yang snod dang bcu dag gi\n", "page_marker": 110, "start": 90755, "end": 90787}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "sor", "W": "so"}, {"op": "replace", "A": "bar", "W": "ba"}, {"op": "replace", "A": "bcud", "W": "bcu"}]
```

**Decision:** Retain U02849 sor and bar and U02850 bcud against W so, ba and bcu. These suffix differences remain exact, not a claim that the print omits letters.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-017"></a>
## W-C02-017 - U02857

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ལྔ་པ།"]
```

**Original source Wylie:**
```json
["dris lan lnga pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan lnga pa", "W": ""}]
```

**Decision:** Retain the fifth-reply heading U02857 which W does not transcribe; no root verse is supplied or deleted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-018"></a>
## W-C02-018 - U02872

**Original Adzom Tibetan:**
```json
["ཙིཏྟ་རིན་ཆེན་གཞལ་ཡས་སུ། །"]
```

**Original source Wylie:**
```json
["tsit+ta rin chen gzhal yas su/_/"]
```

**Exact W lines:**
```json
[{"line": 2907, "raw": "tsit ta rin chen gzhal yas su\n", "page_marker": 111, "start": 91447, "end": 91477}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "tsit+ta", "W": "tsit ta"}]
```

**Decision:** Retain Tibetan citta and preserve W tsit ta versus stored EWTS tsit+ta. This is a romanization/segmentation distinction, not established proof of a different Sanskrit spelling in print.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-019"></a>
## W-C02-019 - U02879

**Original Adzom Tibetan:**
```json
["ཐིག་ལེ་བསྐྱིལ་ཞིང་དཀྲུགས་པས་འགྲུབ། །"]
```

**Original source Wylie:**
```json
["thig le bskyil zhing dkrugs pas 'grub/_/"]
```

**Exact W lines:**
```json
[{"line": 2914, "raw": "thig le bskyal zhing dkrugs pas 'grub\n", "page_marker": 111, "start": 91674, "end": 91712}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "bskyil", "W": "bskyal"}]
```

**Decision:** Retain U02879 bskyil rather than W bskyal. No vowel emendation is adopted from this related website.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-020"></a>
## W-C02-020 - U02885

**Original Adzom Tibetan:**
```json
["རྡོ་རྗེ་ལུ་གུ་རྒྱུད་གནས་ཙིཏྟ་ནས་སྒོ་མིག་ནས་ཡུལ་ནམ་མཁའ་ལ་ཡེ་ཤེས་དངོས་སུ་འཆར་རོ །"]
```

**Original source Wylie:**
```json
["rdo rje lu gu rgyud gnas tsit+ta nas sgo mig nas yul nam mkha' la ye shes dngos su 'char ro_/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "rdo rje lu gu rgyud gnas tsit+ta nas sgo mig nas yul nam mkha' la ye shes dngos su 'char ro", "W": ""}]
```

**Decision:** W lacks the long U02885 gloss. The PDF111 smaller-note evidence governs its separation from root text, while the complete original gloss remains in the apparatus.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-021"></a>
## W-C02-021 - U02887, U02888, U02889

**Original Adzom Tibetan:**
```json
["བསྐྱིལ་འདིའི་དུས་ན་རླུང་འདྲེན་པ།", "ཞིང་མཁའ་རིག་པ་ལ་གཏད་པའོ། །", "གནད་ཡིན་ནོ། །"]
```

**Original source Wylie:**
```json
["bskyil 'di'i dus na rlung 'dren pa/", "zhing mkha' rig pa la gtad pa'o/_/", "gnad yin no/_/"]
```

**Exact W lines:**
```json
[{"line": 2921, "raw": "bskyil zhing mkha' la gtad pa'o\n", "page_marker": 111, "start": 91904, "end": 91936}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "'di'i dus na rlung 'dren pa", "W": ""}, {"op": "delete", "A": "rig pa", "W": ""}, {"op": "delete", "A": "gnad yin no", "W": ""}]
```

**Decision:** W has bskyil zhing mkha' la gtad pa'o, corresponding to the larger main row on PDF111. Preserve all smaller wind-note and rig pa components separately. W agreement does not resolve the uncertain function of small rig pa or erase its source presence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-022"></a>
## W-C02-022 - U02892

**Original Adzom Tibetan:**
```json
["སྣང་བའི་གནད་ནི་འཕེལ་དང་ཟད། །"]
```

**Original source Wylie:**
```json
["snang ba'i gnad ni 'phel dang zad/_/"]
```

**Exact W lines:**
```json
[{"line": 2924, "raw": "snang ba'i gnad ni 'phel dang zang\n", "page_marker": 111, "start": 92004, "end": 92039}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "zad", "W": "zang"}]
```

**Decision:** Retain U02892 zad rather than W zang; preserve the written distinction without grammatical or doctrinal repair.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-023"></a>
## W-C02-023 - U02894

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་དྲུག་པ།"]
```

**Original source Wylie:**
```json
["dris lan drug pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan drug pa", "W": ""}]
```

**Decision:** Retain the sixth-reply heading U02894, absent from W, as a source heading rather than an additional main verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-024"></a>
## W-C02-024 - U02907

**Original Adzom Tibetan:**
```json
["རོ་ནི་རྩ་ལ་བརྟེན་པ་ཡིས། །"]
```

**Original source Wylie:**
```json
["ro ni rtsa la brten pa yis/_/"]
```

**Exact W lines:**
```json
[{"line": 2939, "raw": "ro ni rtsal brten pa yis\n", "page_marker": 112, "start": 92446, "end": 92471}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rtsa la", "W": "rtsal"}]
```

**Decision:** Retain U02907 rtsa la against W rtsal. The syllable boundary and resulting wording remain source-specific.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-025"></a>
## W-C02-025 - U02909

**Original Adzom Tibetan:**
```json
["མས་ནི་དྭངས་མ་སྡུད་པ་དང༌། །"]
```

**Original source Wylie:**
```json
["mas ni dwangs ma sdud pa dang*/_/"]
```

**Exact W lines:**
```json
[{"line": 2941, "raw": "mas ni dangs ma sdud pa dang\n", "page_marker": 112, "start": 92503, "end": 92532}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "dwangs", "W": "dangs"}]
```

**Decision:** Retain U02909 dwangs against W dangs. Do not infer exact Tibetan glyph equivalence by normalizing the Wylie spelling.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-026"></a>
## W-C02-026 - U02912

**Original Adzom Tibetan:**
```json
["འདི་ཡི་ཡན་ལག་དྲུག་པོ་ལ། །"]
```

**Original source Wylie:**
```json
["'di yi yan lag drug po la/_/"]
```

**Exact W lines:**
```json
[{"line": 2944, "raw": "'di yi yan lag drug pho la\n", "page_marker": 112, "start": 92597, "end": 92624}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "po", "W": "pho"}]
```

**Decision:** Retain U02912 po rather than W pho; aspiration is not silently regularized.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-027"></a>
## W-C02-027 - U02914

**Original Adzom Tibetan:**
```json
["དྲོད་ཐོབ་འདོད་ན་མཉེ་བ་གནད། །"]
```

**Original source Wylie:**
```json
["drod thob 'dod na mnye ba gnad/_/"]
```

**Exact W lines:**
```json
[{"line": 2946, "raw": "drod thob 'dod nam nye ba gnad\n", "page_marker": 112, "start": 92658, "end": 92689}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "na mnye", "W": "nam nye"}]
```

**Decision:** Retain U02914 na mnye rather than W nam nye. Keep syllable segmentation separate from any interpretation of the bodily instruction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-028"></a>
## W-C02-028 - U02919

**Original Adzom Tibetan:**
```json
["ཉག་གཅིག་དགོངས་པ་སྟོན་པར་བྱེད། །"]
```

**Original source Wylie:**
```json
["nyag gcig dgongs pa ston par byed/_/"]
```

**Exact W lines:**
```json
[{"line": 2951, "raw": "nyag gcig dgongs pa ston pa byed\n", "page_marker": 112, "start": 92822, "end": 92855}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "par", "W": "pa"}]
```

**Decision:** Retain U02919 par against W pa. This is a suffix difference in the related transcript, not accepted scan correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-029"></a>
## W-C02-029 - U02922

**Original Adzom Tibetan:**
```json
["འདི་ལས་གསེང་ཞིང་མཉེ་བ་གནད། །"]
```

**Original source Wylie:**
```json
["'di las gseng zhing mnye ba gnad/_/"]
```

**Exact W lines:**
```json
[{"line": 2954, "raw": "'di las gseng zhing ma nye ba gnad\n", "page_marker": 112, "start": 92916, "end": 92951}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "mnye", "W": "ma nye"}]
```

**Decision:** Retain U02922 mnye against W ma nye; do not insert a syllable or interpret the separated W form as an instruction change.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-030"></a>
## W-C02-030 - U02927

**Original Adzom Tibetan:**
```json
[" ཆུ་ཡང་དམ་ཚིག་གིས་ནི་རབ་བརྟག་གོ། །"]
```

**Original source Wylie:**
```json
["_chu yang dam tshig gis ni rab brtag go/_/"]
```

**Exact W lines:**
```json
[{"line": 2960, "raw": "dam tshig gis ni rab brtag go\n", "page_marker": 113, "start": 93077, "end": 93107}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "chu yang", "W": ""}]
```

**Decision:** W omits chu yang from U02927, consistent with the native smaller-note separation on PDF113. Preserve the note and its uncertain semantic target; do not treat W omission as loss of a root clause.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-031"></a>
## W-C02-031 - U02934

**Original Adzom Tibetan:**
```json
["འདི་ཡི་ཡན་ལག་བཅུ་གཉིས་ལ། །"]
```

**Original source Wylie:**
```json
["'di yi yan lag bcu gnyis la/_/"]
```

**Exact W lines:**
```json
[{"line": 2967, "raw": "'di yis yan lag bcu gnyis la\n", "page_marker": 113, "start": 93298, "end": 93327}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "yi", "W": "yis"}]
```

**Decision:** Retain U02934 yi rather than W yis; no new grammatical suffix is adopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-032"></a>
## W-C02-032 - U02936

**Original Adzom Tibetan:**
```json
["ཚེ་ཉིད་སྤེལ་ན་བྱུགས་པ་བསྟན། །"]
```

**Original source Wylie:**
```json
["tshe nyid spel na byugs pa bstan/_/"]
```

**Exact W lines:**
```json
[{"line": 2969, "raw": "tshe nyid spel na byugs pa bston\n", "page_marker": 113, "start": 93360, "end": 93393}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "bstan", "W": "bston"}]
```

**Decision:** Retain U02936 bstan rather than W bston; preserve the vowel difference without normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-033"></a>
## W-C02-033 - U02943, U02944, U02945, U02946

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བདུན་པ།", " ཡེ་ཤེས་འཆར་བའི་སྒོ་ཉིད་ནི། །", "ལུས་བཅུད་དྭངས་མ་ཀུན་འདུས་པའི། །", "ཙཀྵུ་ཞེས་པའི་སྒོ་ལས་འཐོན། །"]
```

**Original source Wylie:**
```json
["dris lan bdun pa/", "_ye shes 'char ba'i sgo nyid ni/_/", "lus bcud dwangs ma kun 'dus pa'i/_/", "tsak+Shu zhes pa'i sgo las 'thon/_/"]
```

**Exact W lines:**
```json
[{"line": 2976, "raw": "ye shes 'char ba'i sgo nyid ne\n", "page_marker": 113, "start": 93579, "end": 93610}, {"line": 2977, "raw": "lus bcud dangs ma kun 'dus pa'i\n", "page_marker": 113, "start": 93610, "end": 93642}, {"line": 2978, "raw": "tsak shu zhes pa'i sgo las 'thon\n", "page_marker": 113, "start": 93642, "end": 93675}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bdun pa", "W": ""}, {"op": "replace", "A": "ni", "W": "ne"}, {"op": "replace", "A": "dwangs", "W": "dangs"}, {"op": "replace", "A": "tsak+Shu", "W": "tsak shu"}]
```

**Decision:** Retain the seventh-reply heading and main ni, dwangs, and stored Tibetan cakshu form. W omits the heading and has ne, dangs and tsak shu. Romanization spacing/capitalization is not automatic evidence for Tibetan letter changes.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-034"></a>
## W-C02-034 - U02950

**Original Adzom Tibetan:**
```json
["དབང་པོ་ཡུལ་ལ་འཆར་བྱེད་པའི། །"]
```

**Original source Wylie:**
```json
["dbang po yul la 'char byed pa'i/_/"]
```

**Exact W lines:**
```json
[{"line": 2982, "raw": "dbang po yul la 'char byed pa'o\n", "page_marker": 113, "start": 93774, "end": 93806}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa'i", "W": "pa'o"}]
```

**Decision:** Retain U02950 pa'i rather than W pa'o. The ending remains quoted exactly rather than rewritten to fit syntax.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-035"></a>
## W-C02-035 - U02954, U02955

**Original Adzom Tibetan:**
```json
["བ་མིན་རྭ་འདྲའི་འཁྱིལ་པ་ལས། །", "ཨ་འབྲས་ཞེས་པ་དཀར་ནག་ཕྱེད། །"]
```

**Original source Wylie:**
```json
["ba min rwa 'dra'i 'khyil pa las/_/", "a 'bras zhes pa dkar nag phyed/_/"]
```

**Exact W lines:**
```json
[{"line": 2987, "raw": "ba min rwa 'dra'i khyil pa las\n", "page_marker": 114, "start": 93903, "end": 93934}, {"line": 2988, "raw": "a 'bras zhes pa dkar nag gyed\n", "page_marker": 114, "start": 93934, "end": 93964}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'khyil", "W": "khyil"}, {"op": "replace", "A": "phyed", "W": "gyed"}]
```

**Decision:** Retain U02954 prefixed khyil and U02955 phyed against W khyil and gyed. The website spelling and segmentation do not replace the selected base or resolve the separate B/S phrase difference.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-036"></a>
## W-C02-036 - U02957

**Original Adzom Tibetan:**
```json
["ཤེས་པའི་རང་རྩལ་རྫོགས་པར་སྟོན། །"]
```

**Original source Wylie:**
```json
["shes pa'i rang rtsal rdzogs par ston/_/"]
```

**Exact W lines:**
```json
[{"line": 2990, "raw": "shes pa'i rang gsal rdzogs par ston\n", "page_marker": 114, "start": 93999, "end": 94035}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rtsal", "W": "gsal"}]
```

**Decision:** Retain U02957 rtsal rather than W gsal. A familiar alternative is not authority for replacing the source-specific word.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-037"></a>
## W-C02-037 - U02959

**Original Adzom Tibetan:**
```json
["མངོན་སུམ་པ་དང་རང་གནད་ཀྱིས། །"]
```

**Original source Wylie:**
```json
["mngon sum pa dang rang gnad kyis/_/"]
```

**Exact W lines:**
```json
[{"line": 2992, "raw": "mngon sum ba dang rang gnad kyis\n", "page_marker": 114, "start": 94067, "end": 94100}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa", "W": "ba"}]
```

**Decision:** Retain U02959 pa rather than W ba; record the exact graph difference.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-038"></a>
## W-C02-038 - U02979

**Original Adzom Tibetan:**
```json
["དབྱིངས་ཀྱི་དྭངས་མ་སྡུད་པ་དང༌། །"]
```

**Original source Wylie:**
```json
["dbyings kyi dwangs ma sdud pa dang*/_/"]
```

**Exact W lines:**
```json
[{"line": 3012, "raw": "dbyings kyi dangs ma sdud pa dang\n", "page_marker": 114, "start": 94730, "end": 94764}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "dwangs", "W": "dangs"}]
```

**Decision:** Retain U02979 dwangs against W dangs; romanization variation is not used to normalize the Tibetan source.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-039"></a>
## W-C02-039 - U02986

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བརྒྱད་པ།"]
```

**Original source Wylie:**
```json
["dris lan brgyad pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan brgyad pa", "W": ""}]
```

**Decision:** Retain the eighth-reply heading U02986, which W lacks. It remains a heading, not a newly restored root verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-040"></a>
## W-C02-040 - U02993

**Original Adzom Tibetan:**
```json
["རྒྱང་ཞགས་འགུལ་པ་མེད་པ་གནད། །"]
```

**Original source Wylie:**
```json
["rgyang zhags 'gul pa med pa gnad/_/"]
```

**Exact W lines:**
```json
[{"line": 3026, "raw": "rgyang zhags 'gul ba med pa gnad\n", "page_marker": 115, "start": 95161, "end": 95194}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa", "W": "ba"}]
```

**Decision:** Retain U02993 pa rather than W ba. No grammatical correction or print-level claim is adopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-041"></a>
## W-C02-041 - U03002

**Original Adzom Tibetan:**
```json
["ཉི་མའི་བསླབ་ཐབས་རྣལ་འབྱོར་པས། །"]
```

**Original source Wylie:**
```json
["nyi ma'i bslab thabs rnal 'byor pas/_/"]
```

**Exact W lines:**
```json
[{"line": 3035, "raw": "nyi ma'i bslab thabs rnal 'byor bas\n", "page_marker": 115, "start": 95461, "end": 95497}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pas", "W": "bas"}]
```

**Decision:** Retain U03002 pas rather than W bas, preserving the aspiration-independent pa/ba distinction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-042"></a>
## W-C02-042 - U03010

**Original Adzom Tibetan:**
```json
["ཁྲིད་ལ་མཁས་པས་སྣང་བར་འགྱུར། །"]
```

**Original source Wylie:**
```json
["khrid la mkhas pas snang bar 'gyur/_/"]
```

**Exact W lines:**
```json
[{"line": 3044, "raw": "khrid la mkhas pas nang bar 'gyur\n", "page_marker": 116, "start": 95721, "end": 95755}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "snang", "W": "nang"}]
```

**Decision:** Retain U03010 snang rather than W nang. Do not remove the source prefix from the root based on a website transcription.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-043"></a>
## W-C02-043 - U03012

**Original Adzom Tibetan:**
```json
["རྫོགས་པའི་ཆོས་ཉིད་ཐོབ་པའོ། །"]
```

**Original source Wylie:**
```json
["rdzogs pa'i chos nyid thob pa'o/_/"]
```

**Exact W lines:**
```json
[{"line": 3046, "raw": "rdzogs pa'i chos nyid theb pa'o\n", "page_marker": 116, "start": 95787, "end": 95819}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "thob", "W": "theb"}]
```

**Decision:** Retain U03012 thob rather than W theb. The o/e contrast remains explicit and unadopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-044"></a>
## W-C02-044 - U03018

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་དགུ་པ།"]
```

**Original source Wylie:**
```json
["dris lan dgu pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan dgu pa", "W": ""}]
```

**Decision:** Retain the ninth-reply heading U03018, absent from W; compare the independent S dris/dri issue separately.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-045"></a>
## W-C02-045 - U03025

**Original Adzom Tibetan:**
```json
["རྟོག་བཅས་ཡུལ་གྱི་སྣང་བ་ལ། །"]
```

**Original source Wylie:**
```json
["rtog bcas yul gyi snang ba la/_/"]
```

**Exact W lines:**
```json
[{"line": 3058, "raw": "rtag bcas yul gyi snang ba la\n", "page_marker": 116, "start": 96177, "end": 96207}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rtog", "W": "rtag"}]
```

**Decision:** Retain U03025 rtog rather than W rtag. No vowel choice is made from expected philosophical meaning.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-046"></a>
## W-C02-046 - U03050

**Original Adzom Tibetan:**
```json
["སྐུ་དང་ཐིག་ལེ་འདུན་པའོ། །"]
```

**Original source Wylie:**
```json
["sku dang thig le 'dun pa'o/_/"]
```

**Exact W lines:**
```json
[{"line": 3084, "raw": "sku dang thig le bdun pa'o\n", "page_marker": 117, "start": 97047, "end": 97074}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'dun", "W": "bdun"}]
```

**Decision:** Retain U03050 dun rather than W bdun, preserving the actual apostrophe/prefix difference in the exact strings. The numerical-looking alternative is not inserted as a repaired enumeration.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-047"></a>
## W-C02-047 - U03056, U03057

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་པ།", "འདི་ཉིད་ཡུལ་གནད་འདི་ལྟ་སྟེ། །"]
```

**Original source Wylie:**
```json
["dris lan bcu pa/", "'di nyid yul gnad 'di lta ste/_/"]
```

**Exact W lines:**
```json
[{"line": 3090, "raw": "'di nyid yul gnas 'di lta ste\n", "page_marker": 117, "start": 97243, "end": 97273}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu pa", "W": ""}, {"op": "replace", "A": "gnad", "W": "gnas"}]
```

**Decision:** Retain the tenth-reply heading U03056 and U03057 gnad rather than W gnas. Heading omission and main-word difference remain separately explained.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-048"></a>
## W-C02-048 - U03062

**Original Adzom Tibetan:**
```json
["ཡུལ་ནི་ཐ་དད་གཅིག་རྫོགས་གནང་། །"]
```

**Original source Wylie:**
```json
["yul ni tha dad gcig rdzogs gnang /_/"]
```

**Exact W lines:**
```json
[{"line": 3096, "raw": "yul ni tha dad gcig rdzogs gnad\n", "page_marker": 118, "start": 97407, "end": 97439}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "gnang", "W": "gnad"}]
```

**Decision:** Retain U03062 gnang rather than W gnad. Do not silently replace it with snang or the website form; earlier translation difficulty is not source evidence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-049"></a>
## W-C02-049 - U03067

**Original Adzom Tibetan:**
```json
["རྟོག་མཐའ་ཟད་ཕྱིར་འཁོར་ལས་གྲོལ། །"]
```

**Original source Wylie:**
```json
["rtog mtha' zad phyir 'khor las grol/_/"]
```

**Exact W lines:**
```json
[{"line": 3101, "raw": "rtog mtha' zang phyir 'khor las grol\n", "page_marker": 118, "start": 97575, "end": 97612}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "zad", "W": "zang"}]
```

**Decision:** Retain U03067 zad against W zang; no unobserved source correction is adopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-050"></a>
## W-C02-050 - U03089

**Original Adzom Tibetan:**
```json
["བག་རྡུལ་དྭངས་པའི་ནམ་མཁའ་ལ། །"]
```

**Original source Wylie:**
```json
["bag rdul dwangs pa'i nam mkha' la/_/"]
```

**Exact W lines:**
```json
[{"line": 3124, "raw": "bag rdul dangs pa'i nam mkha' la\n", "page_marker": 119, "start": 98321, "end": 98354}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "dwangs", "W": "dangs"}]
```

**Decision:** Retain U03089 dwangs against W dangs, preserving the distinct romanization without assuming identical glyphs.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-051"></a>
## W-C02-051 - U03093

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་གཅིག་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu gcig pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu gcig pa", "W": ""}]
```

**Decision:** Retain the eleventh-reply heading U03093, absent from W, as a heading rather than a missing main verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-052"></a>
## W-C02-052 - U03106

**Original Adzom Tibetan:**
```json
["རྣམ་ཤེས་ཉིད་དང་བར་སྣང་དང་། །"]
```

**Original source Wylie:**
```json
["rnam shes nyid dang bar snang dang /_/"]
```

**Exact W lines:**
```json
[{"line": 3140, "raw": "rnam shes nyid dang par snang dang\n", "page_marker": 119, "start": 98829, "end": 98864}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "bar", "W": "par"}]
```

**Decision:** Retain U03106 bar snang against W par snang. The initial consonant difference is preserved without grammatical normalization.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-053"></a>
## W-C02-053 - U03114

**Original Adzom Tibetan:**
```json
["གསུམ་གྱིས་བྱེད་འདུས་ཁྱད་པར་བརྟེན། །"]
```

**Original source Wylie:**
```json
["gsum gyis byed 'dus khyad par brten/_/"]
```

**Exact W lines:**
```json
[{"line": 3148, "raw": "gsum kyis byed 'dus khyad par brten\n", "page_marker": 119, "start": 99085, "end": 99121}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "gyis", "W": "kyis"}]
```

**Decision:** Retain U03114 gyis against W kyis. Record both particles without selecting by grammatical expectation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-054"></a>
## W-C02-054 - U03130

**Original Adzom Tibetan:**
```json
["དབྱིངས་ལ་གོམས་པར་གྱུར་པའི་མིས། །"]
```

**Original source Wylie:**
```json
["dbyings la goms par gyur pa'i mis/_/"]
```

**Exact W lines:**
```json
[{"line": 3165, "raw": "dbyings la goms par gyur ba'i mis\n", "page_marker": 120, "start": 99618, "end": 99652}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa'i", "W": "ba'i"}]
```

**Decision:** Retain U03130 pa'i against W ba'i; no source correction is adopted from this related transcription.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-055"></a>
## W-C02-055 - U03134

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་གཉིས་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu gnyis pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu gnyis pa", "W": ""}]
```

**Decision:** Retain the twelfth-reply heading U03134, which W omits. Its absence does not erase the Adzom structural label.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-056"></a>
## W-C02-056 - U03142

**Original Adzom Tibetan:**
```json
["ཐོག་མ་མཆེད་པར་ནུས་པ་ལ། །"]
```

**Original source Wylie:**
```json
["thog ma mched par nus pa la/_/"]
```

**Exact W lines:**
```json
[{"line": 3177, "raw": "thog ma mchod par nus pa la\n", "page_marker": 121, "start": 99977, "end": 100005}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "mched", "W": "mchod"}]
```

**Decision:** Retain U03142 mched rather than W mchod. A more familiar verb is not an independent basis for emendation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-057"></a>
## W-C02-057 - U03144

**Original Adzom Tibetan:**
```json
["ཆུ་ཡི་མེས་ནི་ཟིན་སྐྱེན་བརྗེད། །"]
```

**Original source Wylie:**
```json
["chu yi mes ni zin skyen brjed/_/"]
```

**Exact W lines:**
```json
[{"line": 3179, "raw": "chu yi mes ni zin skyin brjod\n", "page_marker": 121, "start": 100035, "end": 100065}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "skyen brjed", "W": "skyin brjod"}]
```

**Decision:** Retain U03144 skyen brjed against W skyin brjod. Both vowel differences are quoted in their water-fire context, without turning the passage into practical advice or imposing a meaning.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-058"></a>
## W-C02-058 - U03147, U03148

**Original Adzom Tibetan:**
```json
["ཆུའི་རླུང་ལན་གཉིས་བྱུང་བ་དཔྱད།", "ཆུ་ཡི་རླུང་གིས་ཡངས་པ་དང༌། །"]
```

**Original source Wylie:**
```json
["chu'i rlung lan gnyis byung ba dpyad/", "chu yi rlung gis yangs pa dang*/_/"]
```

**Exact W lines:**
```json
[{"line": 3182, "raw": "chu yi rlung gis yas pa dang\n", "page_marker": 121, "start": 100126, "end": 100155}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "chu'i rlung lan gnyis byung ba dpyad", "W": ""}, {"op": "replace", "A": "yangs", "W": "yas"}]
```

**Decision:** Separate U03147 as the printed repetition comment, which W omits. Retain main U03148 yangs rather than W yas; removing a source comment does not authorize a second lexical alteration.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-059"></a>
## W-C02-059 - U03159, U03160

**Original Adzom Tibetan:**
```json
["ས་ཡིས་ས་ནི་ཚིགས་དང་ཡན་ལག་རྒྱས་པར་འཛིན། །", "མེ་ཡིས་ས་ནི་དབང་པོ་རྒྱས། །"]
```

**Original source Wylie:**
```json
["sa yis sa ni tshigs dang yan lag rgyas par 'dzin/_/", "me yis sa ni dbang po rgyas/_/"]
```

**Exact W lines:**
```json
[{"line": 3193, "raw": "sa yis sas ni tshigs dang yan lag rgyas par 'dzin\n", "page_marker": 121, "start": 100470, "end": 100520}, {"line": 3194, "raw": "me yis sas ni dbang po rgyas\n", "page_marker": 121, "start": 100520, "end": 100549}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "sa", "W": "sas"}, {"op": "replace", "A": "sa", "W": "sas"}]
```

**Decision:** Retain sa in U03159 and U03160 against W sas at both positions. Preserve the repeated case-pattern difference without rewriting the elemental enumeration.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-060"></a>
## W-C02-060 - U03167

**Original Adzom Tibetan:**
```json
["རླུང་གི་རླུང་གིས་རྟོག་དཔྱོད་འཛིན། །"]
```

**Original source Wylie:**
```json
["rlung gi rlung gis rtog dpyod 'dzin/_/"]
```

**Exact W lines:**
```json
[{"line": 3201, "raw": "rlung gi rlung gis rtog spyod 'dzin\n", "page_marker": 121, "start": 100736, "end": 100772}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "dpyod", "W": "spyod"}]
```

**Decision:** Retain U03167 dpyod rather than W spyod; no contextual reinterpretation is used to change the consonant.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-061"></a>
## W-C02-061 - U03186

**Original Adzom Tibetan:**
```json
["སྡིག་སྤང་དགེ་བ་སྤྱོད་པར་སྨིན། །"]
```

**Original source Wylie:**
```json
["sdig spang dge ba spyod par smin/_/"]
```

**Exact W lines:**
```json
[{"line": 3221, "raw": "sdig spang dge bskyod par smin\n", "page_marker": 122, "start": 101352, "end": 101383}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "ba spyod", "W": "bskyod"}]
```

**Decision:** Retain U03186 dge ba spyod against W dge bskyod. The fused/different W form is retained literally, not silently divided or repaired in the quotation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-062"></a>
## W-C02-062 - U03192

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་གསུམ་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu gsum pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu gsum pa", "W": ""}]
```

**Decision:** Retain the thirteenth-reply heading U03192 which W lacks, explicitly separate from the following main text.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-063"></a>
## W-C02-063 - U03200

**Original Adzom Tibetan:**
```json
["སྒྲ་ནི་པི་ཝང་བུམ་ལྡིར་དང་། །"]
```

**Original source Wylie:**
```json
["sgra ni pi wang bum ldir dang /_/"]
```

**Exact W lines:**
```json
[{"line": 3235, "raw": "sgra ni pi wang bum lngir dang\n", "page_marker": 123, "start": 101783, "end": 101814}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "ldir", "W": "lngir"}]
```

**Decision:** Retain U03200 ldir against W lngir. The difference in the sound-description spelling remains unadopted and exact.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-064"></a>
## W-C02-064 - U03203

**Original Adzom Tibetan:**
```json
["དྲི་ནི་ངད་ལྡན་སྦྱར་བ་དང༌། །"]
```

**Original source Wylie:**
```json
["dri ni ngad ldan sbyar ba dang*/_/"]
```

**Exact W lines:**
```json
[{"line": 3238, "raw": "dri ni dad ldan sbyar ba dang\n", "page_marker": 123, "start": 101877, "end": 101907}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "ngad", "W": "dad"}]
```

**Decision:** Retain U03203 ngad rather than W dad. The choice is base retention, not proof that the more familiar semantic reading is original.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-065"></a>
## W-C02-065 - U03217

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་བཞི་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu bzhi pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu bzhi pa", "W": ""}]
```

**Decision:** Retain the fourteenth-reply heading U03217, absent from W, without counting it as a newly restored verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-066"></a>
## W-C02-066 - U03225, U03226, U03227

**Original Adzom Tibetan:**
```json
["ལུས་ཀྱི་དབང་པོ་ཀུན་ཟད་སྟེ། །", "རང་བཞིན་མེད་པས་ནུས་པ་ཟད། །", "དྲིས་ལན་བཅོ་ལྔ་པ།"]
```

**Original source Wylie:**
```json
["lus kyi dbang po kun zad ste/_/", "rang bzhin med pas nus pa zad/_/", "dris lan bco lnga pa/"]
```

**Exact W lines:**
```json
[{"line": 3260, "raw": "lus kyi dbang po kun brang ste\n", "page_marker": 124, "start": 102539, "end": 102570}, {"line": 3261, "raw": "rang bzhin med pas nus pa zang\n", "page_marker": 124, "start": 102570, "end": 102601}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "zad", "W": "brang"}, {"op": "replace", "A": "zad dris lan bco lnga pa", "W": "zang"}]
```

**Decision:** Retain U03225 zad and U03226 zad against W brang and zang, and retain the fifteenth-reply heading U03227. Different endings and heading omission are not combined into a fabricated missing verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-067"></a>
## W-C02-067 - U03239

**Original Adzom Tibetan:**
```json
["བདེན་སྣང་རྫུན་པ་ཡིད་ཀྱི་ལུས། །"]
```

**Original source Wylie:**
```json
["bden snang rdzun pa yid kyi lus/_/"]
```

**Exact W lines:**
```json
[{"line": 3273, "raw": "bden snang rdzun pa yid kyis las\n", "page_marker": 124, "start": 102955, "end": 102988}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "kyi lus", "W": "kyis las"}]
```

**Decision:** Retain U03239 yid kyi lus rather than W yid kyis las. Both the particle and final word remain source-specific; neither W nor doctrinal expectation changes the base.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-068"></a>
## W-C02-068 - U03242

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་དྲུག་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu drug pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu drug pa", "W": ""}]
```

**Decision:** Retain the sixteenth-reply heading U03242 which W omits. The nearby uncertain U03240 form remains separately flagged, not solved by the heading count.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-069"></a>
## W-C02-069 - U03253, U03254, U03255

**Original Adzom Tibetan:**
```json
["གདེང་གིས་གྲོལ་བས་འབད་རྩོལ་མེད། །", "དེ་ལ་གདེང་གིས་གྲོལ་བར་བཤད། །", "ཡེ་ནས་གྲོལ་བས་བསྐྱར་གཞི་མེད། །"]
```

**Original source Wylie:**
```json
["gdeng gis grol bas 'bad rtsol med/_/", "de la gdeng gis grol bar bshad/_/", "ye nas grol bas bskyar gzhi med/_/"]
```

**Exact W lines:**
```json
[{"line": 3287, "raw": "gding gis grol bas 'bad rtsol med\n", "page_marker": 125, "start": 103378, "end": 103412}, {"line": 3288, "raw": "de la gding gis grol bar bshad\n", "page_marker": 125, "start": 103412, "end": 103443}, {"line": 3289, "raw": "ye nas grol bas bskyal gzhi med\n", "page_marker": 125, "start": 103443, "end": 103475}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "gdeng", "W": "gding"}, {"op": "replace", "A": "gdeng", "W": "gding"}, {"op": "replace", "A": "bskyar", "W": "bskyal"}]
```

**Decision:** Retain gdeng at U03253/U03254 and bskyar at U03255 against W gding and bskyal. Repeated spelling variation is recorded at each occurrence and not normalized globally.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-070"></a>
## W-C02-070 - U03259

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་བདུན་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu bdun pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu bdun pa", "W": ""}]
```

**Decision:** Retain the seventeenth-reply heading U03259 absent from W, preserving the root/heading distinction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-071"></a>
## W-C02-071 - U03263

**Original Adzom Tibetan:**
```json
["རང་བཞིན་ཤུགས་ཀྱིས་འཆང་གཞི་བྱེད། །"]
```

**Original source Wylie:**
```json
["rang bzhin shugs kyis 'chang gzhi byed/_/"]
```

**Exact W lines:**
```json
[{"line": 3296, "raw": "rang bzhin shugs kyis 'char gzhi byed\n", "page_marker": 125, "start": 103660, "end": 103698}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'chang", "W": "'char"}]
```

**Decision:** Retain U03263 chang against W char, keeping the exact prefixed spellings in their quotations; no new source-letter reading is claimed.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-072"></a>
## W-C02-072 - U03270

**Original Adzom Tibetan:**
```json
["ཀ་ནས་དག་པའི་དྲི་མ་ཟད། །"]
```

**Original source Wylie:**
```json
["ka nas dag pa'i dri ma zad/_/"]
```

**Exact W lines:**
```json
[{"line": 3303, "raw": "ka nas dag pas dri ma zad\n", "page_marker": 125, "start": 103893, "end": 103919}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa'i", "W": "pas"}]
```

**Decision:** Retain U03270 pa'i against W pas. The particle difference is recorded without grammatical emendation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-073"></a>
## W-C02-073 - U03287

**Original Adzom Tibetan:**
```json
["བསམ་པ་ཅི་ལྟར་གནས་པ་ཤེས། །"]
```

**Original source Wylie:**
```json
["bsam pa ci ltar gnas pa shes/_/"]
```

**Exact W lines:**
```json
[{"line": 3321, "raw": "bsam pa ci ltar gnas la shes\n", "page_marker": 126, "start": 104427, "end": 104456}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa", "W": "la"}]
```

**Decision:** Retain U03287 pa against W la. No alternative instruction is adopted merely because it makes sense in context.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-074"></a>
## W-C02-074 - U03290, U03291

**Original Adzom Tibetan:**
```json
["འདུལ་བྱེད་སྐུ་ཡང་དེ་ཙམ་མོ། །", "དྲིས་ལན་བཅོ་བརྒྱད་པ།"]
```

**Original source Wylie:**
```json
["'dul byed sku yang de tsam mo/_/", "dris lan bco brgyad pa/"]
```

**Exact W lines:**
```json
[{"line": 3324, "raw": "'du la byed sku yang de tsam mo\n", "page_marker": 126, "start": 104522, "end": 104554}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'dul", "W": "'du la"}, {"op": "delete", "A": "dris lan bco brgyad pa", "W": ""}]
```

**Decision:** Retain U03290 dul as one written syllable rather than W du la, and keep the eighteenth-reply heading U03291. The W segmentation is not silently converted into a new root word.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-075"></a>
## W-C02-075 - U03298

**Original Adzom Tibetan:**
```json
["ཙིཏྟ་རིན་ཆེན་གཞལ་ཡས་ན། །"]
```

**Original source Wylie:**
```json
["tsit+ta rin chen gzhal yas na/_/"]
```

**Exact W lines:**
```json
[{"line": 3331, "raw": "tsit ta rin chen gzhal yas na\n", "page_marker": 126, "start": 104732, "end": 104762}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "tsit+ta", "W": "tsit ta"}]
```

**Decision:** Retain Tibetan citta at U03298 and quote stored tsit+ta versus W tsit ta exactly. Romanization formatting is not a certified Tibetan spelling variant.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-076"></a>
## W-C02-076 - U03305

**Original Adzom Tibetan:**
```json
["ཀ་ཏི་ཤེལ་གྱི་སྦུ་གུ་ཅན། །"]
```

**Original source Wylie:**
```json
["ka ti shel gyi sbu gu can/_/"]
```

**Exact W lines:**
```json
[{"line": 3338, "raw": "ka te shel gyi spu gu can\n", "page_marker": 126, "start": 104949, "end": 104975}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "ti", "W": "te"}, {"op": "replace", "A": "sbu", "W": "spu"}]
```

**Decision:** Retain U03305 ka ti and sbu gu against W ka te and spu gu. Vowel and initial-consonant differences stay in the apparatus; no anatomical interpretation determines the spelling.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-077"></a>
## W-C02-077 - U03309, U03310

**Original Adzom Tibetan:**
```json
["རང་རྩ་ལ་རྫོགས་པའི་རྟེན་དུ་གནས། །", "དྭངས་མ་འདུས་པའི་མིག་གཉིས་ནས། །"]
```

**Original source Wylie:**
```json
["rang rtsa la rdzogs pa'i rten du gnas/_/", "dwangs ma 'dus pa'i mig gnyis nas/_/"]
```

**Exact W lines:**
```json
[{"line": 3343, "raw": "rang rtsal rdzogs pa'i rten du gnas\n", "page_marker": 127, "start": 105075, "end": 105111}, {"line": 3344, "raw": "dangs ma 'dus pa'i mig gnyis nas\n", "page_marker": 127, "start": 105111, "end": 105144}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rtsa la", "W": "rtsal"}, {"op": "replace", "A": "dwangs", "W": "dangs"}]
```

**Decision:** Retain U03309 rtsa la and U03310 dwangs against W rtsal and dangs. Word-boundary variation and romanization are distinct and neither is silently normalized.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-078"></a>
## W-C02-078 - U03313

**Original Adzom Tibetan:**
```json
["དག་པ་དབྱིངས་ཀྱི་སྒྲོན་མར་སྨིན། །"]
```

**Original source Wylie:**
```json
["dag pa dbyings kyi sgron mar smin/_/"]
```

**Exact W lines:**
```json
[{"line": 3347, "raw": "dag pa dbyings kyi sgron ma smin\n", "page_marker": 127, "start": 105211, "end": 105244}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "mar", "W": "ma"}]
```

**Decision:** Retain U03313 mar against W ma; no final-ra deletion is adopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-079"></a>
## W-C02-079 - U03319

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་བཅུ་དགུ་པ།"]
```

**Original source Wylie:**
```json
["dris lan bcu dgu pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan bcu dgu pa", "W": ""}]
```

**Decision:** Retain the nineteenth-reply heading U03319 which W does not transcribe; no source verse is lost.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-080"></a>
## W-C02-080 - U03335

**Original Adzom Tibetan:**
```json
["འདི་འདྲ་གཅིག་ཏུ་ངེས་མེད་པས། །"]
```

**Original source Wylie:**
```json
["'di 'dra gcig tu nges med pas/_/"]
```

**Exact W lines:**
```json
[{"line": 3369, "raw": "'di dra gcig tu nges med pas\n", "page_marker": 128, "start": 105890, "end": 105919}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'dra", "W": "dra"}]
```

**Decision:** Retain the prefixed dra spelling at U03335 against W dra without its initial apostrophe. The exact strings remain available; no claim of print equivalence is made.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-081"></a>
## W-C02-081 - U03339, U03340

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉི་ཤུ་པ།", " དགོངས་པ་གཅིག་ལས་གཡོས་པ་མེད། །"]
```

**Original source Wylie:**
```json
["dris lan nyi shu pa/", "_dgongs pa gcig las g.yos pa med/_/"]
```

**Exact W lines:**
```json
[{"line": 3373, "raw": "dgongs pa gcig las g.yos ba med\n", "page_marker": 128, "start": 106025, "end": 106057}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyi shu pa", "W": ""}, {"op": "replace", "A": "pa", "W": "ba"}]
```

**Decision:** Retain the twentieth-reply heading and U03340 pa rather than W ba. The W heading omission does not license any change to the main sentence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-082"></a>
## W-C02-082 - U03353

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་གཅིག་པ།"]
```

**Original source Wylie:**
```json
["dris lan nyer gcig pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer gcig pa", "W": ""}]
```

**Decision:** Retain the twenty-first-reply heading U03353 absent from W as a structural heading, not an interpolated main verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-083"></a>
## W-C02-083 - U03361

**Original Adzom Tibetan:**
```json
["ངེས་ཚིག་ཀུན་ནི་འདུས་པ་ལ། །"]
```

**Original source Wylie:**
```json
["nges tshig kun ni 'dus pa la/_/"]
```

**Exact W lines:**
```json
[{"line": 3393, "raw": "nges tshig kun ni 'dus pa las\n", "page_marker": 128, "start": 106659, "end": 106689}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "la", "W": "las"}]
```

**Decision:** Retain U03361 la against W las; the website suffix is not adopted without source evidence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-084"></a>
## W-C02-084 - U03372, U03373

**Original Adzom Tibetan:**
```json
["ཕྱེད་པའི་ཚད་ཀྱིས་འབྲས་བུའོ། །", "དྲིས་ལན་ཉེར་གཉིས་པ།"]
```

**Original source Wylie:**
```json
["phyed pa'i tshad kyis 'bras bu'o/_/", "dris lan nyer gnyis pa/"]
```

**Exact W lines:**
```json
[{"line": 3405, "raw": "phyed pa'i tshid kyis 'bras bu'o\n", "page_marker": 129, "start": 107007, "end": 107040}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "tshad", "W": "tshid"}, {"op": "delete", "A": "dris lan nyer gnyis pa", "W": ""}]
```

**Decision:** Retain U03372 tshad against W tshid and retain the twenty-second-reply heading U03373. The vowel difference and omitted heading are recorded separately.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-085"></a>
## W-C02-085 - U03377

**Original Adzom Tibetan:**
```json
["དྲན་བསམ་རྣམས་ཀྱི་གཞི་པའོ། །"]
```

**Original source Wylie:**
```json
["dran bsam rnams kyi gzhi pa'o/_/"]
```

**Exact W lines:**
```json
[{"line": 3409, "raw": "dran bsam rnams kyi gzhi ma'o\n", "page_marker": 129, "start": 107132, "end": 107162}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa'o", "W": "ma'o"}]
```

**Decision:** Retain U03377 pa'o against W ma'o; the main clause is not reinterpreted by changing the terminal consonant.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-086"></a>
## W-C02-086 - U03395, U03396

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་གསུམ་པ།", "འབྱུང་བ་དྭངས་སྙིགས་འབྱེད་འདོད་པས། །"]
```

**Original source Wylie:**
```json
["dris lan nyer gsum pa/", "'byung ba dwangs snyigs 'byed 'dod pas/_/"]
```

**Exact W lines:**
```json
[{"line": 3428, "raw": "'byung ba dwangs snyigs byed 'dod pas\n", "page_marker": 130, "start": 107719, "end": 107757}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer gsum pa", "W": ""}, {"op": "replace", "A": "'byed", "W": "byed"}]
```

**Decision:** Retain the twenty-third-reply heading U03395 and prefixed byed in U03396 against W byed without the apostrophe. Keep the exact source spellings rather than normalizing them to each other.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-087"></a>
## W-C02-087 - U03402, U03403

**Original Adzom Tibetan:**
```json
["བྱེད་ལས་ཤ་དང་དེ་ཡི་ནད། །", "དྭངས་མས་ལུས་ཟུངས་རྫོགས་པ་དང་། །"]
```

**Original source Wylie:**
```json
["byed las sha dang de yi nad/_/", "dwangs mas lus zungs rdzogs pa dang /_/"]
```

**Exact W lines:**
```json
[{"line": 3434, "raw": "byed las sha dang de yi nang\n", "page_marker": 130, "start": 107909, "end": 107938}, {"line": 3435, "raw": "dangs mas lus zungs rdzogs pa dang\n", "page_marker": 130, "start": 107938, "end": 107973}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "nad dwangs", "W": "nang dangs"}]
```

**Decision:** Retain U03402 nad and U03403 dwangs against W nang and dangs. The fact that the token diff crosses a line does not merge the two clauses or create a new medical claim.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-088"></a>
## W-C02-088 - U03408

**Original Adzom Tibetan:**
```json
["བྱེད་ལས་ཁྲག་དང་དེ་ཡི་ནད། །"]
```

**Original source Wylie:**
```json
["byed las khrag dang de yi nad/_/"]
```

**Exact W lines:**
```json
[{"line": 3440, "raw": "byed las khrag dang de yi nang\n", "page_marker": 130, "start": 108107, "end": 108138}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "nad", "W": "nang"}]
```

**Decision:** Retain U03408 nad rather than W nang. The written health-related noun is recorded as text, not endorsed as medical advice or altered by interpretation.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-089"></a>
## W-C02-089 - U03413

**Original Adzom Tibetan:**
```json
["གནད་ཀྱིས་ཟས་ཀྱི་རྣལ་འབྱོར་འགྲུབ། །"]
```

**Original source Wylie:**
```json
["gnad kyis zas kyi rnal 'byor 'grub/_/"]
```

**Exact W lines:**
```json
[{"line": 3445, "raw": "gnad gyis zas kyi rnal 'byor 'grub\n", "page_marker": 130, "start": 108269, "end": 108304}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "kyis", "W": "gyis"}]
```

**Decision:** Retain U03413 kyis rather than W gyis; no grammatical normalization is adopted.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-090"></a>
## W-C02-090 - U03415, U03416, U03417

**Original Adzom Tibetan:**
```json
["སྨིན་པས་ལུག་དང་གླང་རྡུལ་ལོ། །", "བྱེད་ལས་དྲོད་དང་དེ་ཡི་ནད། །", "དྭངས་མས་ངག་ལུས་རྫོགས་པ་དང་། །"]
```

**Original source Wylie:**
```json
["smin pas lug dang glang rdul lo/_/", "byed las drod dang de yi nad/_/", "dwangs mas ngag lus rdzogs pa dang /_/"]
```

**Exact W lines:**
```json
[{"line": 3447, "raw": "smin pas lug dang glang rngul lo\n", "page_marker": 130, "start": 108338, "end": 108371}, {"line": 3448, "raw": "byed las drod dang de yi nang\n", "page_marker": 130, "start": 108371, "end": 108401}, {"line": 3450, "raw": "dangs mas ngag lus rdzogs pa dang\n", "page_marker": 131, "start": 108405, "end": 108439}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rdul", "W": "rngul"}, {"op": "replace", "A": "nad dwangs", "W": "nang dangs"}]
```

**Decision:** Retain U03415 rdul, U03416 nad and U03417 dwangs against W rngul, nang and dangs. Preserve the unusual source formulations, with no attempt to repair physiology or historical theory.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-091"></a>
## W-C02-091 - U03422, U03423

**Original Adzom Tibetan:**
```json
["སྨིན་པས་ཉི་རྡུལ་རྫོགས་པ་དང༌། །", "བྱེད་ལས་དབུགས་དང་དེ་ཡི་ནད། །"]
```

**Original source Wylie:**
```json
["smin pas nyi rdul rdzogs pa dang*/_/", "byed las dbugs dang de yi nad/_/"]
```

**Exact W lines:**
```json
[{"line": 3455, "raw": "smin pas nyi rngul rdzogs pa dang\n", "page_marker": 131, "start": 108579, "end": 108613}, {"line": 3456, "raw": "byed las dbugs dang de yi nang\n", "page_marker": 131, "start": 108613, "end": 108644}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rdul", "W": "rngul"}, {"op": "replace", "A": "nad", "W": "nang"}]
```

**Decision:** Retain U03422 rdul and U03423 nad against W rngul and nang. These repeated differences are documented, not converted into a universal substitution rule.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-092"></a>
## W-C02-092 - U03432

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་བཞི་པ།"]
```

**Original source Wylie:**
```json
["dris lan nyer bzhi pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer bzhi pa", "W": ""}]
```

**Decision:** Retain the twenty-fourth-reply heading U03432 absent from W; it remains separate from the following main verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-093"></a>
## W-C02-093 - U03436

**Original Adzom Tibetan:**
```json
["འཁོར་བའི་འབྲེལ་པ་ཀུན་སྤངས་ཏེ། །"]
```

**Original source Wylie:**
```json
["'khor ba'i 'brel pa kun spangs te/_/"]
```

**Exact W lines:**
```json
[{"line": 3468, "raw": "'khor ba'i 'bral pa kun spangs te\n", "page_marker": 131, "start": 109003, "end": 109037}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "'brel", "W": "'bral"}]
```

**Decision:** Retain U03436 brel rather than W bral, with the exact prefixed forms quoted. No semantic preference decides the vowel.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-094"></a>
## W-C02-094 - U03454

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་ལྔ་པ།"]
```

**Original source Wylie:**
```json
["dris lan nyer lnga pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer lnga pa", "W": ""}]
```

**Decision:** Retain the twenty-fifth-reply heading U03454 which W omits; no root clause is supplied or removed.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-095"></a>
## W-C02-095 - U03469

**Original Adzom Tibetan:**
```json
["རེ་ལྡེ་ཙམ་ལས་གྲུ་ཆད་སྣང་། །"]
```

**Original source Wylie:**
```json
["re lde tsam las gru chad snang /_/"]
```

**Exact W lines:**
```json
[{"line": 3501, "raw": "re lnge tsam las gru chad snang\n", "page_marker": 132, "start": 110030, "end": 110062}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "lde", "W": "lnge"}]
```

**Decision:** Retain U03469 lde against W lnge. The uncommon written group remains unchanged rather than being guessed from context.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-096"></a>
## W-C02-096 - U03487

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་དྲུག་པ།"]
```

**Original source Wylie:**
```json
["dris lan nyer drug pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer drug pa", "W": ""}]
```

**Decision:** Retain the twenty-sixth-reply heading U03487 absent from W, including its source-specific numbering.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-097"></a>
## W-C02-097 - U03494

**Original Adzom Tibetan:**
```json
["གཞི་ཡིས་བཞི་ཡང་བྱུང་འགྲོ་བའི་སྣང་བ་སྟོན། །"]
```

**Original source Wylie:**
```json
["gzhi yis bzhi yang byung 'gro ba'i snang ba ston/_/"]
```

**Exact W lines:**
```json
[{"line": 3526, "raw": "gzhi yis 'gro ba'i snang ba ston\n", "page_marker": 133, "start": 110800, "end": 110833}]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "bzhi yang byung", "W": ""}]
```

**Decision:** W omits bzhi yang byung from U03494 and agrees with the separated main reading. Native PDF133, not website omission, governs preservation of that phrase as a smaller variant note.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="w-c02-098"></a>
## W-C02-098 - U03505, U03506

**Original Adzom Tibetan:**
```json
["མཁས་པས་ཤེས་པར་བྱས་ཏེ་བཟུང༌། །", "བྱེད་ལས་རླུང་གི་གྲངས་ཚད་ཀྱིས། །"]
```

**Original source Wylie:**
```json
["mkhas pas shes par byas te bzung*/_/", "byed las rlung gi grangs tshad kyis/_/"]
```

**Exact W lines:**
```json
[{"line": 3538, "raw": "mkhas pas shes pa byas te bzung\n", "page_marker": 134, "start": 111155, "end": 111187}, {"line": 3539, "raw": "byed las lung gi grangs tshad kyis\n", "page_marker": 134, "start": 111187, "end": 111222}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "par", "W": "pa"}, {"op": "replace", "A": "rlung", "W": "lung"}]
```

**Decision:** Retain U03505 par and U03506 rlung against W pa and lung. The suffix and subscribed-letter differences remain separate unadopted observations.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-099"></a>
## W-C02-099 - U03511

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་བདུན་པ།"]
```

**Original source Wylie:**
```json
["dris lan nyer bdun pa/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer bdun pa", "W": ""}]
```

**Decision:** Retain the twenty-seventh-reply heading U03511 absent from W as a heading, not a lost main verse.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-100"></a>
## W-C02-100 - U03519

**Original Adzom Tibetan:**
```json
["ལུས་ནི་མིང་དང་ཕྲ་རབ་རྡུལ། །"]
```

**Original source Wylie:**
```json
["lus ni ming dang phra rab rdul/_/"]
```

**Exact W lines:**
```json
[{"line": 3551, "raw": "lus ni ming dang phra rab rngul\n", "page_marker": 134, "start": 111564, "end": 111596}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rdul", "W": "rngul"}]
```

**Decision:** Retain U03519 rdul rather than W rngul, without imposing the repeated W spelling on the root.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-101"></a>
## W-C02-101 - U03521

**Original Adzom Tibetan:**
```json
["ལུས་སེམས་བསྡོམ་པའི་བར་དུ་བརྟགས། །"]
```

**Original source Wylie:**
```json
["lus sems bsdom pa'i bar du brtags/_/"]
```

**Exact W lines:**
```json
[{"line": 3553, "raw": "lus sems bsdom pas bar tu brtags\n", "page_marker": 134, "start": 111627, "end": 111660}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "pa'i", "W": "pas"}, {"op": "replace", "A": "du", "W": "tu"}]
```

**Decision:** Retain U03521 pa'i and du against W pas and tu. Preserve both exact particle differences without using grammar as authority to alter the base.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-102"></a>
## W-C02-102 - U03529

**Original Adzom Tibetan:**
```json
["དྲིས་ལན་ཉེར་བརྒྱད་པའོ།"]
```

**Original source Wylie:**
```json
["dris lan nyer brgyad pa'o/"]
```

**Exact W lines:**
```json
[]
```

**Alignment differences:**
```json
[{"op": "delete", "A": "dris lan nyer brgyad pa'o", "W": ""}]
```

**Decision:** Retain the twenty-eighth-reply heading U03529 absent from W. Its terminal spelling and punctuation are preserved, not inferred from ordinal sequence.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-103"></a>
## W-C02-103 - U03555

**Original Adzom Tibetan:**
```json
["རང་སྣང་ཡིན་པར་སུས་མ་མཐོང༌། །"]
```

**Original source Wylie:**
```json
["rang snang yin par sus ma mthong*/_/"]
```

**Exact W lines:**
```json
[{"line": 3588, "raw": "ngang snang yin par sus ma mthong\n", "page_marker": 136, "start": 112720, "end": 112754}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "rang", "W": "ngang"}]
```

**Decision:** Retain U03555 rang rather than W ngang. No contextual preference authorizes changing the initial consonant.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-104"></a>
## W-C02-104 - U03577

**Original Adzom Tibetan:**
```json
["ལུས་ངག་ཡིད་ལས་མ་འདས་པས། །"]
```

**Original source Wylie:**
```json
["lus ngag yid las ma 'das pas/_/"]
```

**Exact W lines:**
```json
[{"line": 3610, "raw": "lus ngag yid la ma 'das pas\n", "page_marker": 136, "start": 113434, "end": 113462}]
```

**Alignment differences:**
```json
[{"op": "replace", "A": "las", "W": "la"}]
```

**Decision:** Retain U03577 las rather than W la; the source-specific case ending stays explicit.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md)

<a id="w-c02-105"></a>
## W-C02-105 - U03622

**Original Adzom Tibetan:**
```json
[" གནད་འདུས་བཀོད་པ་རིག་པའི་རྩ་བ་ངེས་པར་འབྱུང་བའི་ལེའུ་སྟེ་གཉིས་པའོ།།"]
```

**Original source Wylie:**
```json
["_gnad 'dus bkod pa rig pa'i rtsa ba nges par 'byung ba'i le'u ste gnyis pa'o//"]
```

**Exact W lines:**
```json
[{"line": 3657, "raw": "gnad 'dus bkod pa rig pa'i rtsa ba nges par 'byung ba'i le'u ste\n", "page_marker": 138, "start": 114924, "end": 114989}, {"line": 3658, "raw": "gnyis pa'o\n", "page_marker": 138, "start": 114989, "end": 115000}]
```

**Alignment differences:**
```json
[]
```

**Decision:** The colophon is split over two W lines but has no remaining normalized lexical-token difference. Record the physical website lineation and exact signs separately; retain U03622 and the source-boundary uncertainty without counting this as a lexical correction.

**Evidence:** [wikisource.json](../wikisource.json), [W-REVIEW.md](../W-REVIEW.md), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)
