# Active translation source: Adzom

**Selected witness:** Adzom Chögar printing, catalogued as 2000, BDRC **W1KG11703**, volume 1, root-text record **MW1KG11703_0001_001**. No other edition is an active source in this folder.

| File | Role |
| --- | --- |
| [Dra-Thal-Gyur-Adzom-2000.pdf](Dra-Thal-Gyur-Adzom-2000.pdf) | Primary facsimile: 205 pages, from BDRC image group I1KG11710, images 3–207 inclusive |
| [W1KG11703_7.docx](W1KG11703_7.docx) | Original cleaned Adzom e-text supplied through the WeBuddhist/OpenPecha shared Drive |
| [W1KG11703_7.txt](W1KG11703_7.txt) | UTF-8 extraction of that DOCX; no Tibetan spelling or punctuation corrections |
| [SOURCE.json](SOURCE.json) | Provenance, scope, and verification metadata |
| [SHA256SUMS](SHA256SUMS) | Checksums of the three source files |

## Authority and scope

The **printed scan governs readings**. The cleaned e-text is a working aid, not a project-proofread diplomatic transcription. Its provider's completion flag does not certify line-by-line accuracy. Do not silently combine it with another edition or correct the scan's readings from it.

PDF page 1 is the printed title leaf (BDRC image 3). The text begins on PDF page 2 (image 4) and its closing material ends on PDF page 205 (image 207). The whole root tantra is represented, including the opening material and final colophon; translation progress is recorded separately in [translations/](../translations/README.md).

The PDF is an image-only assembly of the full-resolution IIIF responses, not a provider-exported original PDF. The images are not cropped, resized, enhanced, or subjected to new OCR. The corresponding archive and per-image checksums are preserved in [editions/adzom-2000/](../editions/adzom-2000/README.md). PDF page N corresponds to BDRC image N + 2 throughout this source.

## Retrieve

From the repository root, run `git lfs pull`, then `cd source && shasum -a 256 -c SHA256SUMS`.

Follow [AGENTS.md](../AGENTS.md), the copied translation standard, and the glossary. Comparison witnesses remain in [editions/](../editions/README.md). Vimalamitra's commentary remains in the separate [The-Great-Commentary repository](https://github.com/Lotus-King-Translation/The-Great-Commentary).

[PAGE-MAP.csv](PAGE-MAP.csv) maps every source PDF page to its original image URL and checksum. Internal chapter boundaries have not yet been indexed for this root edition; do not reuse the Palyul commentary index.
