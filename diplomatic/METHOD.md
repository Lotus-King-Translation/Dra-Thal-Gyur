# Editorial method

## Scope and authority

The target is one readable Tibetan diplomatic edition of the selected Adzom printing, with a comprehensive apparatus for the acquired comparison material. “Golden” describes the intended maintained edition, not a claim of an infallible or reconstructed original. The existing Adzom selection remains in force. A different edition's better grammar, a majority among transcriptions, or a preferred doctrinal interpretation does not by itself justify changing this witness.

The source register distinguishes a printing or manuscript from its modern transcript, duplicate files, reprints, containers with unresolved root mapping, and catalogue-only leads. No independence or stemma is inferred from filenames. The full acquired scan-only comparison work is still required; electronic collation is one stage of that work.

## Sigla

| Siglum | Meaning |
| --- | --- |
| A-scan | Adzom 2000 W1KG11703 facsimile, the governing base |
| A | Supplied Adzom Unicode e-text extracted from W1KG11703_7.docx |
| B | Supplied Tharpaling Unicode e-text extracted from W27491_7.docx |
| S | Supplied Sichuan Unicode e-text extracted from W3CN7084_7.docx |
| W | Stored Wikisource Adzom-block Wylie transcription, revision 439571 |

A, B, S, and W label these electronic sources, not automatically certified readings of their alleged exemplars. Other scan witnesses are named in full in scan reports until their chapter concordances and sigla are established. W is a related reference transcript, not an independent printing. Its editorial quotations are not new firsthand witnesses.

## Transcription and uncertainty

Preserve observable spelling, punctuation, repetition, headings, and source annotations. Separate main verse from smaller glosses or reported variants when the scan establishes the distinction. Do not silently repair arithmetic, Sanskrit, defective syntax, unusual orthography, or doctrinal difficulty. Transcription corrections record both the replaced e-text and the scan reading. A conjecture, if ever proposed, must be labelled and kept distinct from an observed reading.

Unresolved glyphs remain visibly unresolved with exact image evidence. A missing scan leaf, unreadable passage, supplied-transcript omission, uncollated passage, and a genuine witness omission are different states. None is converted into agreement or supplied silently from another witness.

Existing translation unit identifiers U00001 etc. are stable electronic anchors. They are not manuscript lines. Adzom PDF page N maps to BDRC image N+2. Scan-only insertions get additional identifiers; they do not renumber the existing anchors. The displayed Markdown uses editorial paragraph breaks at electronic unit boundaries and trims boundary whitespace for display; exact source strings, punctuation, offsets, and spaces remain in the collation ledger. The display is not a facsimile of physical lineation.

The machine-readable reading uses **both** `collation/chapter-01/reading-units.json` (the 2,635 original U anchors and their corrected main readings) and `collation/chapter-01/ch1-scan-insertions.json` (restorations and paratext, ordered by `after_unit` and `anchor_sequence`). Reading only the former would omit the restored lines. `tools/build_chapter1.py` combines both into the Markdown chapter.

## Apparatus and reasons

Each electronic locus gives exact A/B/S strings, source-unit anchors, zero-based half-open Unicode-character offsets, the underlying exact-difference identifiers, and a disposition with rationale. Full-unit quotations make Tibetan syllables readable; the raw patch layer can also identify differences inside a combining-character sequence. A null-length reading is an insertion/absence in a supplied transcript, not proof that its exemplar omits text.

When a scan-verified correction affects a locus, the corrected reading in the reading text and its intervention note govern; A remains quoted unchanged in the comparative apparatus. Other loci retain the selected Adzom reading under the base policy. The coverage ledger and per-unit statuses distinguish completed lexical comparison from outstanding title, annotation, punctuation and comparison-print verification. This explicitly explains the working choice without pretending to settle a printed-witness conflict from transcription alone.

W is collated in EWTS. Its lexical alignment strips specified EWTS punctuation signs and collapses spacing for alignment only. The exact website lines and exact A units remain quoted. This is a lexical comparison with a separate punctuation/sign inventory; it is not an exhaustive character-level equivalence claim across scripts. Website editorial notes remain separate from root text. Attribution: [stored provenance](../editions/adzom-wikisource/PROVENANCE.json), [revision 439571](https://wikisource.org/w/index.php?oldid=439571), [contributor history](https://wikisource.org/w/index.php?title=Sgra%20thal%20%E2%80%99gyur%20%28A-%27dzom%20blocks%29&action=history). Preserve the source's attribution and applicable share-alike terms; this dossier grants no additional rights over other editions.

## Verification and completion

The electronic comparison uses exact unique anchors and monotonic alignment, with no Unicode normalization. Every non-equal span must be represented, and both B and S must reconstruct byte-for-byte from A plus the apparatus. Readable whole-unit loci and minimal patch loci must each independently reconstruct them. Large differences and moved headings still need philological review even when reconstruction succeeds.

Before completing a chapter, check: complete base scan coverage; exact chapter boundaries; main text versus source-annotation layers; every acquired comparison witness's coverage or specifically documented unavailable spans; alignment of additions, omissions and transpositions; apparatus-to-text links; complete source-span accounting; and a candid unresolved-reading list. Only after that gate passes is a completed-chapter commit appropriate, followed by work on the next chapter.

The method does not impose an English translation or change the project's established terminology. Editorial explanations describe evidence and decisions without proposing new glossary entries.

## Second-reading scope

The continuous Adzom pass compares lexical main text, with source annotations reviewed separately; it does not certify exact physical punctuation or every ornate title glyph. Interventions retain existing e-text terminal delimiters where applicable until that review is complete. Thus the current product is a provisional diplomatic reading, not a completed strict facsimile transcription. Source-heading display order can be semantic/editorial: a comparison against U ordering alone does not establish a difference in the physical Adzom layout.

Independent-agent image inspection is not independently credentialed human palaeography. The reports state when candidates were known before inspection and where reliable discrimination failed. Neither expected-text recognition nor an OCR locator constitutes evidence of agreement. The candidate findings and uncollated ranges remain explicit.
