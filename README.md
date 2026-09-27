# Dra Thal Gyur

Working repository for a Tibetan–English translation of the **Dra Thal Gyur root tantra**, supported by Vimalamitra's commentary in [The-Great-Commentary](https://github.com/Lotus-King-Translation/The-Great-Commentary).

**Active source: Adzom, BDRC W1KG11703, volume 1.** The scan governs readings; the cleaned Adzom e-text is an aid awaiting project proofreading. The working translation and its current coverage are recorded in [translations/](translations/README.md).

## Layout

| Location | Contents |
| --- | --- |
| [diplomatic/](diplomatic/README.md) | Chapter 1 reading and apparatus; provisional, with recovery records and explicit remaining collation gaps |
| [source/](source/README.md) | Only the selected Adzom root-tantra facsimile and its e-text |
| [editions/](editions/README.md) | Acquired reference editions, image archives, e-texts, metadata, and unresolved acquisition leads |
| [AGENTS.md](AGENTS.md) | Copied project instructions plus user-required remote preservation directives; revision recorded in GUIDANCE-PROVENANCE.json |
| [guidelines/](guidelines/tibetan_translation_standard_v2.md) | The three original guideline files, unchanged |
| [glossary/](glossary/expanded_tibetan_english_glossary.csv) | The original eight-column glossary, unchanged |
| [GUIDANCE-PROVENANCE.json](GUIDANCE-PROVENANCE.json) | Source commit and checksums for the copied instructions, guidelines, and glossary |

**Diplomatic Chapter 1 remains in progress.** [Current status](diplomatic/STATUS.json) and [continuation](diplomatic/HANDOFF.md) distinguish recovered evidence, verified local corrections and uncollated witnesses.

## Reading the source

Open [source/Dra-Thal-Gyur-Adzom-2000.pdf](source/Dra-Thal-Gyur-Adzom-2000.pdf). It contains 205 full-resolution scan pages (BDRC images 3–207), including the title and closing material. The same PDF is archived in the Adzom edition folder; Git LFS stores the identical bytes as one content object.

PDFs and ZIPs are stored through Git LFS. After cloning, run `git lfs pull`. From the repository root, verify the acquisition inventory with `shasum -a 256 -c editions/SHA256SUMS`; verify the active files with `cd source && shasum -a 256 -c SHA256SUMS`.

The [edition catalogue](editions/CATALOGUE.md) distinguishes actual files from catalogue-only records, partial scan sets, and unverified leads. Multiple manifestations or e-texts do not automatically constitute independent witnesses. Preserve each source's attribution and restrictions; this repository grants no additional redistribution rights.

Current full asset verification, including the documented local guidance revision: `python3 diplomatic/tools/verify_recovered_assets.py` (requires pikepdf). The original acquisition validator and asset bytes remain preserved.
