# Witness and coverage audit for a diplomatic edition

Audit date: 2026-09-27. Repository: `Lotus-King-Translation/Dra-Thal-Gyur`.

This is an inventory and evidentiary audit, not a collation. It reports the acquired files and the limitations documented by their provenance. No witness has been declared textually independent on the basis of a folder name, publication date, or divergent transcript alone. No chapter after chapter 1 was worked on for this audit.

## Governing evidence

`README.md` and `source/README.md` establish **Adzom W1KG11703, volume 1** as the selected base, with the **facsimile governing readings**. Its cleaned Unicode e-text is expressly an aid awaiting project proofreading. `editions/research/README.md` says that a previous report recommending Sichuan does not supersede the owner's Adzom selection. `AGENTS.md` requires the active translation standard and relevant eight-column glossary when translating or doing translation QC; this inventory does not introduce translations or terminology decisions.

For a genuinely diplomatic output, preserve Adzom's observable readings and document departures from its e-text as transcription corrections. If the edition adopts readings from another witness, identify those explicitly as editorial substitutions or emendations: the resulting text is a critically edited text based on Adzom, not a wholly diplomatic transcription of that witness. The user may use “golden diplomatic” broadly, but the methodology should define the actual treatment precisely.

## Witness inventory

All paths below are repository-relative. “Mapped facsimile” means a stored root-text image range with a page-to-provider-image manifest; it does not certify internal textual completeness, legibility, or chapter-by-chapter proofreading.

| Proposed inventory label | Folder | Direct evidence available | Locator and extent | Collation status / limitations |
| --- | --- | --- | --- | --- |
| Adzom base | `editions/adzom-2000/` | Mapped facsimile, 205 pages; one supplied Unicode transcript family | W1KG11703; volume 1; I1KG11710, images 3–207 | Selected base. No skipped indices. Title/closing boundaries checked previously; full project line-by-line proofreading remains undone. Image-only PDF. |
| Adzom 1973–1977 manifestation | `editions/adzom-1973-1977/` | Provider volume PDF | W1KG892; bibliographic root extent printed pp. 1–205 | Root-only extraction and PDF-to-printed-page mapping unresolved. Related Adzom manifestation, not presumed an independent witness. |
| Degé | `editions/dege-W1ER7/` | Mapped facsimile, 111 pages; no e-text | W1ER7; volume 3; I1ER175, images 647–757 | Scan-only comparison candidate. Boundary page may contain neighboring work; no skipped manifest indices. |
| Tharpaling | `editions/tharpaling-1983/` | Mapped facsimile, 147 pages; provider container; one supplied Unicode transcript family | W27491; volume 2; I4448, images 5–151 | Print is partly faint and uneven. Transcript expressly not yet proofread line by line. No skipped indices. |
| Tingkye | `editions/tingkye-1973/` | Mapped facsimile, 145 pages; extra provider container | W21518; volume 10; I1765, images 394–538, printed pp. 386–530 | Scan-only candidate. Title starts on image 394, before catalogue text start 395. The extra container `bdrc-W21518-9.pdf` failed prior visual matches at printed pp. 386/530 and is not an established second copy of this root extract. |
| Tsamdrak | `editions/tsamdrak-1982/` | Mapped facsimile, 172 pages; no e-text | W21521; volume 12; I0615, images 4–175, printed pp. 2–173 | Scan-only candidate. Closing page begins next text. No skipped indices. |
| Dzongsar | `editions/dzongsar-manuscript/` | Mapped facsimile, 248 pages; no e-text | W3PD988; volume 147; I3PD1345, images 5–252 | Inspected images described as illustrated gold-lettered manuscript, despite worksheet's old-print designation. Blank/title and closing blank retained. No skipped indices. |
| Gadkar | `editions/gadkar-manuscript/` | Mapped facsimile, 177 pages; no e-text | W1ER156 reproduction of MW1BL6; volume 32; virtual I1ER907, images 441–617 | Backing filenames and virtual image numbers differ; use manifest mapping. Title precedes catalogue text start. No skipped indices. Do not identify this with the Rig’dzin Tshewang Norbu lead. |
| Zhichen | `editions/khams-zhichen-manuscript/` | Mapped facsimile, 201 pages; no e-text | W2PD17382; volume 36; I1KG81308, images 31–231 | Title precedes catalogue text start. No skipped indices. |
| Langtang | `editions/langtang-manuscript/` | Mapped facsimile, 212 exposed pages from a 220-index range; no e-text | W1ER124; volume 3; I1ER800, image range 2–221 | Indices **4, 5, 38, 39, 40, 41, 172, 173** absent from manifest. Foliation and textual effect unestablished; must not call these eight lost text pages merely from numbering. |
| W1ER119, provenance unresolved | `editions/seventeen-tantras-W1ER119/` | Mapped facsimile, 168 exposed pages from a 200-index range; no e-text | W1ER119; volume 5; I1ER794, image range 2–201 | 32 skipped indices, listed below. Title, opening, and ending checked previously; internal textual completeness unestablished. |
| Gcn collection | `editions/gcn-manuscript/` | Provider container PDF | W1ER128; digital root location unresolved | rKTs reports 19 volumes and root in Ga; reproduction exposes three digital groups. Digital group 3 cannot be assumed to contain root. Not currently a verified root facsimile. |
| Sichuan 2016 | `editions/sichuan-2016/` | One supplied Unicode transcript family; no full facsimile | W3CN7084; volume 2; I3CN8462 | Provider PDFs private; manifest had only 41 preview canvases. Transcript can be compared **as a transcript**. Underlying print readings cannot all be certified from acquired material. |
| Paltség 2009 | `editions/paltseg-2009/` | Catalogue and acquisition lead only | W1KG14783; reported volume 5; anomalous volume 0 in location | No acquired root facsimile/e-text. Provider PDF private; collection manifest HTTP 500 at acquisition. |
| CTRC 49-volume compilation | `editions/ctrc-49-volume/` | Catalogue and preview manifest only | W3CN3207; volume 3; catalogue images 740–861 | No full acquired root facsimile/e-text. Full scan restricted. Worksheet's X4LQ9T is not the root identifier; correct preserved root record is MW3CN3207_O3CN3207_NAKR4R. |
| Gangteng EAP lead | `editions/gangteng-EAP/` | Collection-level catalogue lead only | EAP039/1/4/259 | Root extent unresolved; no acquired scan; collection endpoint HTTP 401 at acquisition. |
| Adzom-block Wikisource transcription | `editions/adzom-wikisource/` | Wylie text, revision 439571, timestamp 2015-09-09T14:02:11Z | Exact revision and contributor-history links in PROVENANCE.json | A reference transcription from a website, not an additional print. Exact correspondence to Adzom print not collated. Preserve attribution and applicable share-alike terms for reused text. |

W1ER119 absent manifest indices: **48, 49, 52, 53, 56, 57, 60, 61, 64, 65, 68, 69, 72, 73, 96, 97, 102, 103, 122, 123, 170, 171, 174, 175, 180, 181, 184, 185, 190, 191, 196, 197**.

Additional bibliographic leads only, without acquired root facsimiles or e-texts: Spiti/Orgyen Dorje, Sumra 1977 (volume 1); A. W. Barber, Taipei 1991 (volume 56; reproduction not presumed independent of exemplar); Rig’dzin Tshewang Norbu manuscript (volume Tha, ff. 1b–71b; shelfmark/acquisition unresolved). Translation records in `editions/translations/` are not Tibetan witnesses and contain no acquired commercial translation texts.

## Actual transcript families and duplicates

There are **three**, not nine, supplied Unicode transcript families:

| Family | Original DOCX | Extracted TXT | Separate supplied TXT | Evidence |
| --- | --- | --- | --- | --- |
| Adzom | `adzom-2000/W1KG11703_7.docx` | `adzom-2000/W1KG11703_7.txt` | `adzom-2000/a.txt` | DOCX extraction and short TXT match after decoding UTF-8 signature and stripping outer whitespace. Source-folder TXT is byte-identical to edition-folder extraction. |
| Tharpaling | `tharpaling-1983/W27491_7.docx` | `tharpaling-1983/W27491_7.txt` | `tharpaling-1983/b.txt` | Same decoded-and-trimmed text. |
| Sichuan | `sichuan-2016/W3CN7084_7.docx` | `sichuan-2016/W3CN7084_7.txt` | `sichuan-2016/s.txt` | Same decoded-and-trimmed text. |

These equalities were independently checked in this audit, agreeing with `editions/research/original-text-files.json`. The DOCX and its extraction are one representation chain, not independent readings. The original supplied TXT is not an additional witness merely because it has a separate Drive link. The two Wikisource files (`source.wikitext` and `sgra-thal-gyur.wikitext`) were also independently verified byte-identical. No transcript genealogy or stemma follows from these file-level results.

Three transcript differences can yield a useful **candidate apparatus**, but not an exhaustive collation of the stored witnesses and not confirmed print variants until scans have been read. Scan-only candidates cannot be coded as agreeing with the base because they lack e-text.

## Chapter 1: concrete evidence gaps before claiming readiness

1. **Base scan control.** The selected Adzom scan begins its text on PDF page 2 / BDRC image 4. A valid diplomatic chapter must check every retained base reading against that scan, including page boundaries, marginal/interlinear additions, damaged or uncertain letters, spelling and punctuation. Repository status does not certify that this has already happened.
2. **Eight other scan-only mapped witnesses.** Degé, Tingkye, Tsamdrak, Dzongsar, Gadkar, Zhichen, Langtang and W1ER119 have no searchable transcript in the repository. Their chapter-1 extent must be found visually and their actual text collated before saying that all acquired mapped witnesses were collated. The scans exist; the gap is transcription/collation, not universal lack of access.
3. **Langtang opening discontinuity.** Its first mapped images are 2, 3, 6, 7. Whether missing manifest indices 4–5 omit chapter-1 content requires examining foliation and the text crossing image 3 to 6. The repository correctly leaves that significance unresolved. The gap cannot be silently supplied from Adzom or interpreted as omission by the manuscript.
4. **Sichuan cannot be fully verified against print from current acquired files.** A claim concerning Sichuan must distinguish “Sichuan supplied transcript reads …” from “Sichuan print reads …”. Preview manifests alone do not establish chapter-1 coverage; establish any available preview coverage before using it to upgrade certainty.
5. **Unmapped containers.** Adzom 1973–1977 and Gcn cannot yet be counted among chapter-1 collated texts. Resolve their root mapping first, or explicitly identify them as uncollated acquired containers in the coverage statement.
6. **Wikisource omissions and representation.** It omits Sanskrit syllables in its displayed opening and has its own line/page markers. Treat omission of material from this reference transcription separately from an omission in its claimed printed exemplar. Romanization conversion is a normalization step that must not create or suppress an apparent variant silently.
7. **Chapter boundary.** `source/README.md` says internal chapter boundaries were not indexed at acquisition. A scan-supported chapter-1 ending and start of following chapter are needed; an old commentary index must not substitute for a root-text index.
8. **Every-conflict scope.** Orthographic, punctuation, segmentation, paratext and substantive variants require explicit coverage policy. An algorithm that normalizes spaces, shads, tshegs, or Unicode before comparison may suppress conflicts; it must retain an exact-text comparison layer or clearly document the excluded class. A reproducible diff detects transcript differences, not automatically manuscript readings or reasoning for the chosen reading.

## Minimum defensible coverage statement

A chapter file should say which witnesses were inspected in that chapter, give precise PDF/provider-image and preferably folio/line references, enumerate unreadable or unavailable spans, and distinguish confirmed scan readings, unverified transcript readings, and editorial interventions. “Not collated” and “not extant/omitted” are different states. “No differences detected among the collated witnesses in this span” must never imply coverage of the catalogued but inaccessible witnesses.

It is possible to produce and fully annotate an Adzom-based edition for all readable acquired material, with explicit unresolved/unavailable evidence. It is not possible to honestly guarantee an apparatus of **every conflict in every listed edition**, including inaccessible scans and unidentified containers, from the present inventory alone. Any chapter marked ready should have a narrowly accurate scope rather than an absolute completeness claim.

## Verification scope of earlier repository metadata

`editions/VALIDATION.json` (2026-09-26) states `text_proofread: false` and `complete_foliation_audit: false`. The recorded pixel validation covers 1,786 images across the ten mapped assemblies and reports no pixel mismatches. This establishes that assembled PDFs preserve the archived images, not that the Tibetan reading is correct, all textual leaves are present, or all witnesses agree.

At this audit's local check, all ten mapped `sgra-thal-gyur.pdf` files were actual PDFs. The four provider-container paths were still Git LFS pointer files in this checkout; that is a local materialization state, not evidence that the repository lacks those assets. The parent agent may materialize them later. No repository files were altered and no commits were made by this audit.

## Subsequent Chapter 1 scan checks

The [Langtang opening inspection](reviews/chapter-01/langtang-opening-gap.md) found apparent main-text continuity from image 3 to image 6 at the phrase corresponding to U00017. Missing indices 4–5 therefore do not justify a textual lacuna at this boundary. This local finding does not resolve later gaps or establish full collation. The [Chapter 1 dossier](chapter-01.md) records targeted Adzom corrections and restorations plus limited comparison-scan evidence; none upgrades the whole chapter to complete.
