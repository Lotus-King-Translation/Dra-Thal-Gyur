# Dra Thal Gyur

Working repository for a Tibetan–English translation of the **Dra Thal Gyur root tantra**, supported by Vimalamitra's commentary in [The-Great-Commentary](https://github.com/Lotus-King-Translation/The-Great-Commentary).

**Active source: Adzom, BDRC W1KG11703, volume 1.** The scan governs readings; the cleaned Adzom e-text is an aid awaiting project proofreading. The working translation and its current coverage are recorded in [translations/](translations/README.md).

## Paired reading edition

[Read Tibetan](paired/source.md) · [Read English](paired/translation.md) ·
[Format and validation](paired/README.md) · [Continuation](paired/HANDOFF.md)

The paired-text/2 edition preserves the fixed `root-tantra-v1.0.0` Tibetan and
`translation-golden-aligned-v1.0.0` English. Its 2,667 shared pairs declare source
presentation explicitly: 48 prose, 2,448 verse, 2 h1 and 169 h3; no paired h2 is
invented. Six chapter wrappers and the distinct closing material are preserved.
Five v1 pair memberships changed with [complete lineage](paired/v2/PAIR-AUDIT.json).
The exact two-file corpus, notes and source coverage are checked mechanically;
this is not a new semantic review of inherited English.

## Layout

| Location | Contents |
| --- | --- |
| [diplomatic/](diplomatic/README.md) | Released six-chapter golden edition: corrected Adzom reading, restorations, apparatus and explicit coverage limits |
| [source/](source/README.md) | Only the selected Adzom root-tantra facsimile and its e-text |
| [editions/](editions/README.md) | Acquired reference editions, image archives, e-texts, metadata, and unresolved acquisition leads |
| [AGENTS.md](AGENTS.md) | Copied project instructions plus user-required remote preservation directives; revision recorded in GUIDANCE-PROVENANCE.json |
| [guidelines/](guidelines/tibetan_translation_standard_v2.md) | The three original guideline files, unchanged |
| [glossary/](glossary/expanded_tibetan_english_glossary.csv) | The original eight-column glossary, unchanged |
| [GUIDANCE-PROVENANCE.json](GUIDANCE-PROVENANCE.json) | Source commit and checksums for the copied instructions, guidelines, and glossary |

**The whole root tantra bounded v1 is released.** Read [the fixed edition](diplomatic/root-tantra-v1/release/README.md), tagged `root-tantra-v1.0.0`. Exhaustive witness collation remains unfinished. Preservation and later work begin at [diplomatic/HANDOFF.md](diplomatic/HANDOFF.md) on `main`. It provides restart checks, an exact work queue and remote checkpoint instructions. The edition and all preserved recovery archives are together on this branch.

## Reading the source

Open [source/Dra-Thal-Gyur-Adzom-2000.pdf](source/Dra-Thal-Gyur-Adzom-2000.pdf). It contains 205 full-resolution scan pages (BDRC images 3–207), including the title and closing material. The same PDF is archived in the Adzom edition folder; Git LFS stores the identical bytes as one content object.

PDFs and ZIPs are stored through Git LFS. After cloning, run `git lfs pull`. From the repository root, verify the acquisition inventory with `shasum -a 256 -c editions/SHA256SUMS`; verify the active files with `cd source && shasum -a 256 -c SHA256SUMS`.

The [edition catalogue](editions/CATALOGUE.md) distinguishes actual files from catalogue-only records, partial scan sets, and unverified leads. Multiple manifestations or e-texts do not automatically constitute independent witnesses. Preserve each source's attribution and restrictions; this repository grants no additional redistribution rights.

Full asset verification after materializing all required Git LFS files: `python3 diplomatic/tools/verify_recovered_assets.py` (requires pikepdf). It checks documented local guidance revisions and writes the current `diplomatic/ASSET-VALIDATION.json`; it does not overwrite historical reports. The original acquisition validator and asset bytes remain preserved.
