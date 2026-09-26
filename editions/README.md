# Reference editions and acquisition status

All acquired versions and research records belong here. Only Adzom W1KG11703 is active in [source/](../source/README.md). Files below are distinct manifestations, not a claim of independent recensions.

## Root-tantra facsimiles acquired from BDRC IIIF

| Edition / witness | PDF pages | Coverage |
| --- | ---: | --- |
| [Adzom 2000](adzom-2000/README.md) | 205 | Images 3–207; active base; no missing image indices |
| [Degé W1ER7](dege-W1ER7/README.md) | 111 | Images 647–757; no missing image indices |
| [Tsamdrak](tsamdrak-1982/README.md) | 172 | Images 4–175; no missing image indices |
| [Tharpaling](tharpaling-1983/README.md) | 147 | Images 5–151, including title; no missing image indices |
| [Tingkye](tingkye-1973/README.md) | 145 | Images 394–538; boundary pages also contain neighbouring text |
| [Dzongsar](dzongsar-manuscript/README.md) | 248 | Catalogued images 5–252; very dark source images require caution |
| [Langtang](langtang-manuscript/README.md) | 212 | Available images 2–221; **8 missing indices** in the supplied manifest |
| [W1ER119 manuscript](seventeen-tantras-W1ER119/README.md) | 168 | Available images 2–201; **32 missing indices** in the supplied manifest |
| [Khams / Zhichen](khams-zhichen-manuscript/README.md) | 201 | Images 31–231, including title; no missing image indices |
| [Gadkar](gadkar-manuscript/README.md) | 177 | Virtual-volume images 441–617, including title; no missing image indices |

Each folder contains `sgra-thal-gyur.pdf`, `original-images.zip`, `image-manifest.json`, and provider metadata. The ZIP preserves the unaltered full-resolution **IIIF response bytes** (JPEG or lossless PNG), not a claim to possess original master TIFFs. The PDF is an image-only assembly with no added OCR, cropping, enhancement, or downsampling. Shared boundary pages remain uncropped. See each image manifest for source URLs, PDF-to-image mapping, dimensions, hashes, and gaps.

## Other acquired material

Original provider container-volume PDFs are retained for [Adzom 1973–1977](adzom-1973-1977/README.md), Tharpaling, Tingkye, and [W1ER128 / Gcn](gcn-manuscript/README.md). The latter's root-text location has not been securely mapped to the current three-volume digital packaging.

Original cleaned DOCX e-texts and uncorrected UTF-8 extractions are retained for Adzom 2000, Tharpaling, and [Sichuan 2016](sichuan-2016/README.md). Their provider's completion flags are recorded, not treated as project proofreading. Further shared plaintext files and the original worksheet export are under [research/](research/README.md).

See [CATALOGUE.md](CATALOGUE.md) for the remaining bibliographic records and acquisition leads, and [ACQUISITION.json](ACQUISITION.json) for the file inventory. To verify all stored acquisition files, run `shasum -a 256 -c editions/SHA256SUMS` from the repository root. Reproduction scripts do not grant access to restricted material.

The [Wikisource Wylie transcription](adzom-wikisource/README.md) is also retained as an attributed Adzom reference, not a separate independent witness. The verification script is [verify_assets.py](verify_assets.py).
