# Chapter 6 — comparative apparatus and closing record

**Released bounded v1**

A/B/S quote exact supplied transcripts. All 21 exact differences are represented in 13 readable loci. W is a related reference transcript, not an independent printing.

[Reading](reading.md) · [W reference](wikisource.md) · [Coverage](COVERAGE.md) · [Structured apparatus](apparatus.json)

## Source-supported uncertainties

<a id="c6-u05248-uncertain"></a>
### C6-U05248-UNCERTAIN

**Original:**
```json
{
  "U05248": "རང་བྱུང་ཉིད་དང་རྩ་ལ་རྫོགས་དང་། །"
}
```

**Reason:** Supplied rtsa la retained; compact segmentation versus rtsal remains unresolved.

**Limits:** Supplied rtsa la retained; compact segmentation versus rtsal remains unresolved.

**Evidence:** [p197-native.png](../evidence/E01/p197-native.png), [U05248-rtsa-la-context.png](../evidence/focused/U05248-rtsa-la-context.png)

<a id="c6-u05309-uncertain"></a>
### C6-U05309-UNCERTAIN

**Original:**
```json
{
  "U05309": "ཕྱེད་པའི་ལས་དང་ལྡང་ཚད་དོ། །"
}
```

**Reason:** Supplied phyed retained rather than conjecturally replacing it with B/S byed.

**Limits:** Supplied phyed retained rather than conjecturally replacing it with B/S byed.

**Evidence:** [p199-native.png](../evidence/E01/p199-native.png), [p199-x3696.png](../evidence/E01/p199-x3696.png)

<a id="c6-u05398-uncertain"></a>
### C6-U05398-UNCERTAIN

**Original:**
```json
{
  "U05398": "ལོངས་སྐུ་དག་གིས་རྣམ་པར་ཐོབ། །"
}
```

**Reason:** Supplied dag gis retained with dag/ngag uncertainty; W is not silently adopted.

**Limits:** Supplied dag gis retained with dag/ngag uncertainty; W is not silently adopted.

**Evidence:** [p202-native.png](../evidence/E02/p202-native.png), [U05398-full-height.png](../evidence/focused/U05398-full-height.png)

<a id="c6-u05411-uncertain"></a>
### C6-U05411-UNCERTAIN

**Original:**
```json
{
  "U05411": "དང་ཤེས་པས་ནི་མི་རྟོག་སྐྱེ། །"
}
```

**Reason:** The retained dang and its function remain uncertain; no grammatical or doctrinal substitute is supplied.

**Limits:** The retained dang and its function remain uncertain; no grammatical or doctrinal substitute is supplied.

**Evidence:** [p203-native.png](../evidence/E02/p203-native.png), [U05411-dang-context.png](../evidence/focused/U05411-dang-context.png)

<a id="c6-u05448-uncertain"></a>
### C6-U05448-UNCERTAIN

**Original:**
```json
{
  "U05448": " ལེའུ་དྲུག་པའོ།། །།"
}
```

**Reason:** Supplied chapter-colophon signs are retained, not certified as exact physical punctuation.

**Limits:** Supplied chapter-colophon signs are retained, not certified as exact physical punctuation.

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png)

<a id="c6-u05459-uncertain"></a>
### C6-U05459-UNCERTAIN

**Original:**
```json
{
  "U05459": " སོ་ཕག །"
}
```

**Reason:** Ritual so phag retained without an asserted Sanskrit reconstruction.

**Limits:** Ritual so phag retained without an asserted Sanskrit reconstruction.

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="c6-u05460-uncertain"></a>
### C6-U05460-UNCERTAIN

**Original:**
```json
{
  "U05460": "ཨག་ཐམ།"
}
```

**Reason:** Ritual ag tham retained; W a ga tha ma and compact source graphic do not authorize silent respelling.

**Limits:** Ritual ag tham retained; W a ga tha ma and compact source graphic do not authorize silent respelling.

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

## Restored main text

<a id="a2000-c06-s01"></a>
### A2000-C06-S01

After U05382; before U05383.

```text
ཏོག་དང་སིང་བས་སྣ་ཚོགས་ལས།
འུར་ཞིང་སིང་བས་མཆོག་ཐོབ་པའོ།
```

**Reason:** Native PDF202 row1 contains both main verses between the exact surviving flanks. B/S/W also record the material; adoption rests on the governing scan.

**Punctuation:** Editorial single shad per restored verse and editorial reading line breaks.

**Limits:** Sound-word meanings and physical punctuation are not normalized.

**Evidence:** [p202-native.png](../evidence/E02/p202-native.png), [p202-x1848.png](../evidence/E02/p202-x1848.png), [p202-x3696.png](../evidence/E02/p202-x3696.png), [S01-two-verses.png](../evidence/focused/S01-two-verses.png)

## The 13 A/B/S release choices

<a id="l6-0001"></a>
### L6-0001

Anchors: U05225, U05226.
Exact differences: C6-0001, C6-0002.

**Disposition:** retain_base

**Reason:** Retain the first-reply heading separately from the main kye kye clause. S braces are editorial annotation markup, not Tibetan words.

**Selected anchor strings:**
```json
{
  "U05225": "ཞུས་ལན་དང་པོ།",
  "U05226": "ཀྱེ་ཀྱེ་ལྷ་ཡི་དབང་ཕྱུག་ཉོན། །"
}
```

**A [150388, 150430]:**
```text
ཞུས་ལན་དང་པོ།ཀྱེ་ཀྱེ་ལྷ་ཡི་དབང་ཕྱུག་ཉོན། །
```

**B [151094, 151136]:**
```text
ཞུས་ལན་དང་པོ།ཀྱེ་ཀྱེ་ལྷ་ཡི་དབང་ཕྱུག་ཉོན། །
```

**S [151465, 151509]:**
```text
{ཞུས་ལན་དང་པོ།}ཀྱེ་ཀྱེ་ལྷ་ཡི་དབང་ཕྱུག་ཉོན། །
```

**Evidence:** [collation.json](../collation.json), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="l6-0002"></a>
### L6-0002

Anchors: U05245, U05246.
Exact differences: C6-0003, C6-0004.

**Disposition:** retain_base

**Reason:** Retain the second-reply heading separately from the following main clause. S braces are presentation markup and do not change the Tibetan heading or root wording.

**Selected anchor strings:**
```json
{
  "U05245": "ཞུས་ལན་གཉིས་པ།",
  "U05246": "འོད་ཀྱི་ཡང་ཞུན་བཅུ་བདུན་བཤད། །"
}
```

**A [150955, 150999]:**
```text
ཞུས་ལན་གཉིས་པ།འོད་ཀྱི་ཡང་ཞུན་བཅུ་བདུན་བཤད། །
```

**B [151661, 151705]:**
```text
ཞུས་ལན་གཉིས་པ།འོད་ཀྱི་ཡང་ཞུན་བཅུ་བདུན་བཤད། །
```

**S [152034, 152080]:**
```text
{ཞུས་ལན་གཉིས་པ།}འོད་ཀྱི་ཡང་ཞུན་བཅུ་བདུན་བཤད། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0003"></a>
### L6-0003

Anchors: U05248.
Exact differences: C6-0005.

**Disposition:** retain_with_explicit_uncertainty

**Reason:** Retain the supplied rtsa la division with the source-reading uncertainty explicitly visible; S rtsal is preserved in the apparatus.

**Selected anchor strings:**
```json
{
  "U05248": "རང་བྱུང་ཉིད་དང་རྩ་ལ་རྫོགས་དང་། །"
}
```

**A [151024, 151056]:**
```text
རང་བྱུང་ཉིད་དང་རྩ་ལ་རྫོགས་དང་། །
```

**B [151730, 151762]:**
```text
རང་བྱུང་ཉིད་དང་རྩ་ལ་རྫོགས་དང་། །
```

**S [152105, 152136]:**
```text
རང་བྱུང་ཉིད་དང་རྩལ་རྫོགས་དང་། །
```

**Evidence:** [collation.json](../collation.json), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="l6-0004"></a>
### L6-0004

Anchors: U05275, U05276.
Exact differences: C6-0006, C6-0007.

**Disposition:** retain_base

**Reason:** Retain the fourth-reply heading and following phrase exactly from Adzom; S brace presentation does not authorize normalization.

**Selected anchor strings:**
```json
{
  "U05275": "ཞུས་ལན་བཞི་པ།",
  "U05276": "ལོངས་སྤྱོད་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །"
}
```

**A [151819, 151866]:**
```text
ཞུས་ལན་བཞི་པ།ལོངས་སྤྱོད་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །
```

**B [152525, 152572]:**
```text
ཞུས་ལན་བཞི་པ།ལོངས་སྤྱོད་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །
```

**S [152899, 152948]:**
```text
{ཞུས་ལན་བཞི་པ།}ལོངས་སྤྱོད་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0005"></a>
### L6-0005

Anchors: U05292, U05293.
Exact differences: C6-0008, C6-0009.

**Disposition:** retain_base

**Reason:** Retain the fifth-reply heading and the complete-enjoyment clause. S braces mark editorial presentation only.

**Selected anchor strings:**
```json
{
  "U05292": "ཞུས་ལན་ལྔ་པ།",
  "U05293": "སྤྲུལ་པའི་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །"
}
```

**A [152310, 152355]:**
```text
ཞུས་ལན་ལྔ་པ།སྤྲུལ་པའི་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །
```

**B [153016, 153061]:**
```text
ཞུས་ལན་ལྔ་པ།སྤྲུལ་པའི་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །
```

**S [153392, 153439]:**
```text
{ཞུས་ལན་ལྔ་པ།}སྤྲུལ་པའི་སྐུ་ཡང་སྐུ་གསུང་ཐུགས། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0006"></a>
### L6-0006

Anchors: U05303.
Exact differences: C6-0010.

**Disposition:** retain_base

**Reason:** Retain Adzom ma lus in mdzad pa ma lus rdzogs pa dang. S agrees with A; B omission of ma is recorded but does not justify changing the governing witness.

**Selected anchor strings:**
```json
{
  "U05303": "མཛད་པ་མ་ལུས་རྫོགས་པ་དང་། །"
}
```

**A [152611, 152637]:**
```text
མཛད་པ་མ་ལུས་རྫོགས་པ་དང་། །
```

**B [153317, 153341]:**
```text
མཛད་པ་ལུས་རྫོགས་པ་དང་། །
```

**S [153695, 153721]:**
```text
མཛད་པ་མ་ལུས་རྫོགས་པ་དང་། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0007"></a>
### L6-0007

Anchors: U05305, U05306.
Exact differences: C6-0011, C6-0012.

**Disposition:** retain_base

**Reason:** Retain the sixth-reply heading and sku yi mtshan nyid ngo bo dang. The S brace convention is presentation, not source wording.

**Selected anchor strings:**
```json
{
  "U05305": " ཞུས་ལན་དྲུག་པ།",
  "U05306": "སྐུ་ཡི་མཚན་ཉིད་ངོ་བོ་དང་། །"
}
```

**A [152666, 152708]:**
```text
 ཞུས་ལན་དྲུག་པ།སྐུ་ཡི་མཚན་ཉིད་ངོ་བོ་དང་། །
```

**B [153370, 153412]:**
```text
 ཞུས་ལན་དྲུག་པ།སྐུ་ཡི་མཚན་ཉིད་ངོ་བོ་དང་། །
```

**S [153750, 153794]:**
```text
 {ཞུས་ལན་དྲུག་པ།}སྐུ་ཡི་མཚན་ཉིད་ངོ་བོ་དང་། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0008"></a>
### L6-0008

Anchors: U05309.
Exact differences: C6-0013.

**Disposition:** retain_with_explicit_uncertainty

**Reason:** Retain phyed with explicit uncertainty after inspecting the row-end group; B/S byed alone does not authorize replacement.

**Selected anchor strings:**
```json
{
  "U05309": "ཕྱེད་པའི་ལས་དང་ལྡང་ཚད་དོ། །"
}
```

**A [152766, 152793]:**
```text
ཕྱེད་པའི་ལས་དང་ལྡང་ཚད་དོ། །
```

**B [153470, 153497]:**
```text
བྱེད་པའི་ལས་དང་ལྡང་ཚད་དོ། །
```

**S [153852, 153879]:**
```text
བྱེད་པའི་ལས་དང་ལྡང་ཚད་དོ། །
```

**Evidence:** [collation.json](../collation.json), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="l6-0009"></a>
### L6-0009

Anchors: U05317, U05318.
Exact differences: C6-0014, C6-0015.

**Disposition:** retain_base

**Reason:** Retain the seventh-reply heading and the three-modes clause. The transcript difference is heading presentation only.

**Selected anchor strings:**
```json
{
  "U05317": " ཞུས་ལན་བདུན་པ།",
  "U05318": "སྐུ་ཡི་བཞུགས་ཚུལ་རྣམ་པ་གསུམ། །"
}
```

**A [152990, 153035]:**
```text
 ཞུས་ལན་བདུན་པ།སྐུ་ཡི་བཞུགས་ཚུལ་རྣམ་པ་གསུམ། །
```

**B [153694, 153739]:**
```text
 ཞུས་ལན་བདུན་པ།སྐུ་ཡི་བཞུགས་ཚུལ་རྣམ་པ་གསུམ། །
```

**S [154076, 154123]:**
```text
 {ཞུས་ལན་བདུན་པ།}སྐུ་ཡི་བཞུགས་ཚུལ་རྣམ་པ་གསུམ། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0010"></a>
### L6-0010

Anchors: U05328, U05329.
Exact differences: C6-0016, C6-0017.

**Disposition:** retain_base

**Reason:** Retain the eighth-reply heading and sku yi rang bzhin chos nyid ni. Leading-space and brace differences are presentation only.

**Selected anchor strings:**
```json
{
  "U05328": " ཞུས་ལན་བརྒྱད་པ།",
  "U05329": "སྐུ་ཡི་རང་བཞིན་ཆོས་ཉིད་ནི། །"
}
```

**A [153308, 153352]:**
```text
 ཞུས་ལན་བརྒྱད་པ།སྐུ་ཡི་རང་བཞིན་ཆོས་ཉིད་ནི། །
```

**B [154012, 154055]:**
```text
ཞུས་ལན་བརྒྱད་པ།སྐུ་ཡི་རང་བཞིན་ཆོས་ཉིད་ནི། །
```

**S [154396, 154442]:**
```text
 {ཞུས་ལན་བརྒྱད་པ།}སྐུ་ཡི་རང་བཞིན་ཆོས་ཉིད་ནི། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0011"></a>
### L6-0011

Anchors: U05382.
Exact differences: C6-0018, C6-0019.

**Disposition:** adopt_evidenced_correction

**Reason:** Restore both scan-attested main verses after U05382 and before U05383. B/S retain their own exact punctuation in the apparatus.

**Selected anchor strings:**
```json
{
  "U05382": "སྒྲ་ནི་ཤག་དང་སྡིག་པ་དང༌། །"
}
```

**Also include:** A2000-C06-S01.

**A [154835, 154861]:**
```text
སྒྲ་ནི་ཤག་དང་སྡིག་པ་དང༌། །
```

**B [155538, 155621]:**
```text
སྒྲ་ནི་ཤག་དང་སྡིག་པ་དང༌། །ཏོག་དང་སིང་བས་སྣ་ཚོགས་ལས། །འུར་ཞིང་སིང་བས་མཆོག་ཐོབ་པའོ། །
```

**S [155925, 156008]:**
```text
སྒྲ་ནི་ཤག་དང་སྡིག་པ་དང༌། །ཏོག་དང་སིང་བས་སྣ་ཚོགས་ལས། །འུར་ཞིང་སིང་བས་མཆོག་ཐོབ་པའོ། །
```

**Evidence:** [collation.json](../collation.json), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

<a id="l6-0012"></a>
### L6-0012

Anchors: U05436.
Exact differences: C6-0020.

**Disposition:** retain_base

**Reason:** Retain Adzom rang dag in nam mkha rang dag gsal ba dang. S agrees with A; B nga dag is preserved as a transcript difference without replacing the base.

**Selected anchor strings:**
```json
{
  "U05436": "ནམ་མཁའ་རང་དག་གསལ་བ་དང་། །"
}
```

**A [156379, 156404]:**
```text
ནམ་མཁའ་རང་དག་གསལ་བ་དང་། །
```

**B [157139, 157163]:**
```text
ནམ་མཁའ་ང་དག་གསལ་བ་དང་། །
```

**S [157526, 157551]:**
```text
ནམ་མཁའ་རང་དག་གསལ་བ་དང་། །
```

**Evidence:** [collation.json](../collation.json)

<a id="l6-0013"></a>
### L6-0013

Anchors: U05466.
Exact differences: C6-0021.

**Disposition:** retain_base

**Reason:** Retain all three Adzom virtue formulas. They are visible in PDF205 rows2–3; B/S give only closing signs here, not an authoritative deletion.

**Selected anchor strings:**
```json
{
  "U05466": " དགེའོ་དགེའོ་དགེའོ།།"
}
```

**A [157268, 157288]:**
```text
 དགེའོ་དགེའོ་དགེའོ།།
```

**B [158027, 158030]:**
```text
 །།
```

**S [158415, 158418]:**
```text
 །།
```

**Evidence:** [collation.json](../collation.json), [SOURCE-REVIEW.json](../SOURCE-REVIEW.json)

## Full-work closing material

<a id="u05449"></a>
### U05449 — work_colophon

Retain rin po che opening as part of the work colophon, not a seventh chapter.

**Exact selected text:**
```text
རིན་པོ་ཆེ་འབྱུང་བར་བྱེད་པ།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x0000.png](../evidence/E02/p204-x0000.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png)

<a id="u05450"></a>
### U05450 — work_colophon

Retain the complete closing work title, including rtsa bar bstan pa.

**Exact selected text:**
```text
 སྒྲ་ཐལ་འགྱུར་ཆེན་པོ་ཆོས་རྣམས་ཀུན་གྱི་རྩ་བར་བསྟན་པའི་རྒྱུད་ཅེས་བྱ་བ།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x0000.png](../evidence/E02/p204-x0000.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png)

<a id="u05451"></a>
### U05451 — work_colophon

Retain all words of the concluding count statement and rdzogs so; do not turn the count into a modern catalogue assertion.

**Exact selected text:**
```text
 རང་བཞིན་རྫོགས་པ་ཆེན་པོ་ཤོ་ལོ་ཀ་འབུམ་ཕྲག་དྲུག་ཅུ་རྩ་བཞི་ལས་ཁྱད་པར་དུ་བཀོད་པ་རྫོགས་སོ།། །།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x0000.png](../evidence/E02/p204-x0000.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png)

<a id="u05452"></a>
### U05452 — seal

Retain the first triple rgya seal group.

**Exact selected text:**
```text
རྒྱ་རྒྱ་རྒྱ།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png), [p205-x0000.png](../evidence/E02/p205-x0000.png)

<a id="u05453"></a>
### U05453 — seal

Retain the second triple rgya seal group without deduplication.

**Exact selected text:**
```text
 རྒྱ་རྒྱ་རྒྱ།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png), [p205-x0000.png](../evidence/E02/p205-x0000.png)

<a id="u05454"></a>
### U05454 — seal

Retain the third triple rgya seal group without deduplication.

**Exact selected text:**
```text
 རྒྱ་རྒྱ་རྒྱ།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png), [p205-x0000.png](../evidence/E02/p205-x0000.png)

<a id="u05455"></a>
### U05455 — transmission_restriction

Retain the introductory phrase of the recipient restriction.

**Exact selected text:**
```text
 རྒྱུད་ཀྱི་རྒྱལ་པོ་འདི་ནི།
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png), [p205-x0000.png](../evidence/E02/p205-x0000.png)

<a id="u05456"></a>
### U05456 — transmission_restriction

Retain the full recipient restriction across the PDF204/205 page turn.

**Exact selected text:**
```text
 འགྲོ་བ་ཁྱད་པར་ཅན་ལ་མ་གཏོགས་པ་སུ་དགའ་དགའ་ལ་ཡོད་པ་མ་ཡིན་ནོ། །
```

**Evidence:** [p204-native.png](../evidence/E02/p204-native.png), [p204-x1848.png](../evidence/E02/p204-x1848.png), [p204-x3696.png](../evidence/E02/p204-x3696.png), [p205-x0000.png](../evidence/E02/p205-x0000.png)

<a id="u05457"></a>
### U05457 — protector_invocation

Retain the invocation and its printed epithets without importing deity names.

**Exact selected text:**
```text
དཔལ་སྔགས་སྲུང་གི་རྒྱལ་མོ་སྨུག་ནག་ཁྲོས་མའི་རྒྱལ་མོ་རག་གདོང་མས་སྲུངས་ཤིག །
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05458"></a>
### U05458 — ritual_formula

Retain the first sa ma ya formula as separate ritual text.

**Exact selected text:**
```text
ས་མ་ཡ།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05459"></a>
### U05459 — ritual_formula

Retain so phag with a visible reading/interpretation qualification.

**Exact selected text:**
```text
 སོ་ཕག །
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05460"></a>
### U05460 — ritual_formula

Retain ag tham with a visible segmentation qualification; W a ga tha ma is separately recorded.

**Exact selected text:**
```text
ཨག་ཐམ།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05461"></a>
### U05461 — protector_invocation

Retain the address to the black protector as source invocation text.

**Exact selected text:**
```text
 དཔལ་ལྡན་མགོན་པོ་ནག་པོ་ཁྱོད་ལ་གཏད།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05462"></a>
### U05462 — protector_invocation

Retain the recipient-warning clause as historical source text, not an editorial threat.

**Exact selected text:**
```text
 སྣོད་མེད་པ་ལ་བྱིན་ན་དམ་ཚིག་གི་ཆད་པ་ཆོད་ཅིག །
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05463"></a>
### U05463 — ritual_formula

Retain the second sa ma ya formula without merging it with U05458.

**Exact selected text:**
```text
ས་མ་ཡ།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05464"></a>
### U05464 — seal

Retain the final triple rgya seal group.

**Exact selected text:**
```text
 རྒྱ་རྒྱ་རྒྱ།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05465"></a>
### U05465 — concluding_note

Retain the seven mother-and-child notice without inventing the seven titles.

**Exact selected text:**
```text
 ཐལ་འགྱུར་རྒྱུད་ལ་མ་བུ་བདུན།།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)

<a id="u05466"></a>
### U05466 — closing_auspicious_formula

Retain all three dge-o formulas, visible across rows2–3 despite absence of their words in B/S.

**Exact selected text:**
```text
 དགེའོ་དགེའོ་དགེའོ།།
```

**Evidence:** [p205-native.png](../evidence/E02/p205-native.png), [p205-x0000.png](../evidence/E02/p205-x0000.png), [p205-x1848.png](../evidence/E02/p205-x1848.png), [p205-x3696.png](../evidence/E02/p205-x3696.png)
