# Adzom chapter-one focused facsimile review

Source: `source/Dra-Thal-Gyur-Adzom-2000.pdf`, hydrated image-only PDF. PDF N = BDRC image N+2. Review performed directly on embedded original 5696 × 1344-pixel PNGs and cropped details. Crop coordinates were used only for inspection; no OCR was generated. The main text is compared with `source/W1KG11703_7.txt` and its unchanged unit index in `translations/2026-09-26-full-draft/data/source-units.json`.

## Scope and limitation

Visually reviewed opening/title PDF pages 1–4, the chapter boundary at PDF102, and five specifically flagged possible omission sites at PDF51,74,78,85,90. This is NOT a full chapter-one scan proofread. The opening/title inspection does not settle the Sanskrit-letter transcription, non-Tibetan ornamental script, every punctuation mark, or every marginal label. No later chapter has been collated here.

## Main findings

All five flagged omission groups really are present in the Adzom-2000 facsimile, and absent from the cleaned Adzom e-text: **13 main-text verse lines**, plus a smaller reply heading on PDF90. They can be restored from the selected base scan rather than borrowed from another witness. See `ch1-scan-insertions.json` for exact Tibetan reading transcriptions and all locators/crops.

| After / before source unit | PDF / image | Main-text lines | Important detail |
| --- | --- | ---: | --- |
| U01274 / U01275 | 51 / 53 | 3 | Water verses precede earth verses; preserve printed order. |
| U01882 / U01883 | 74 / 76 | 3 | Second verse prints **སྐུ་**, against website **su**; scan is འགྲུབ་, retained as printed. |
| U02005 / U02006 | 78 / 80 | 3 | Includes distinction of worldly base and cause/result. |
| U02187 / U02188 | 85 / 87 | 2 | Physical row 4 last verse, then row 5 first verse. |
| U02308 / U02309 | 90 / 92 | 2 | Correct anchor is BEFORE U02309, not after it. Reply heading lies between the two restored verses. |

PDF90 source heading is **དྲིས་ལན་ང་བདུན་པ།** (`dris lan nga bdun pa/`); preserve it separately from main verse. It is visibly smaller type. The number is read from the image; reply 56/58 context is corroboration only.

## Opening findings

- PDF1/image3 has three graphic/text lines, including a non-Tibetan-looking ornamental script line, Tibetan-script Sanskrit title, and Tibetan title. The main Tibetan title agrees lexically with U00004, but no complete scholarly Sanskrit/ornamental transcription is certified here. The e-text must not be presented as already checked letter-for-letter at this title.
- PDF2/image4 opening contains the main title/homage and a smaller `thun mong ma yin pa'i gleng gzhi bkod pa/` label; PDF4/image6 contains the smaller `thun mong gi gleng gzhi bkod pa/` label. Their size/layout supports treating them as source structural annotations, rather than pretending the cleaned e-text's linear placement reproduces layout.
- PDF2/image4 has a portrait caption outside the main text frame, omitted from cleaned e-text. Provisional reading: **བརྒྱུད་པ་ཀུན་གྱི་ཐོག་མའི་གཞི། སྟོན་པ་ཀུན་ཏུ་བཟང་པོ་ལ་འདུད།།**. Its presence and distinct paratext status are clear; retain transcription as provisional with the crop. The prior report's Wylie is supported but not independently elevated to absolute certainty.
- **Confirmed correction at U00039:** e-text སྟོད་ (`stod`) should read scan སྟོང་ (`stong`). PDF4/image6 row3 right / row4 left. Full proposed reading: **སྟོང་དང་ལྡན་པ་དབུས་མའི་གནས། །**. Final ང is visible. See `ch1-opening-corrections.json`.

## Chapter-boundary inscription

PDF102/image104 has a compact scan-only inscription/ornamental-looking annotation after chapter-one colophon U02635 and before chapter-two opening U02636. Earlier project notes call it an unresolved small annotation. Direct inspection confirms presence; I cannot responsibly supply a complete word sequence. Some signs are unlike ordinary surrounding print, and enlarging the existing raster supplies no new information. Retain explicit unresolved status and the image; do not substitute a guessed chapter-two heading. This is an unresolved reading, not text reviewed and omitted as irrelevant.

## Editorial treatment

The restored main text is a lexical Tibetan reading with readable Unicode punctuation, not a facsimile of variable interletter spacing or line-fill dots. Preserve underlying e-text unchanged, and document insertions/correction in the diplomatic artifact. A Markdown edition can represent unresolved scan text honestly, but this sampling does not justify calling all base-witness characters or all edition conflicts verified.
