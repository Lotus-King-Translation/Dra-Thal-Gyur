# Reference editions

Start with [CATALOGUE.md](CATALOGUE.md) for every stored witness and acquisition lead. Only Adzom W1KG11703 is active in [source/](../source/README.md).

Full-resolution image responses are preserved in each `original-images.zip`, with an image-only PDF and per-image provenance. These archive names refer to the downloaded IIIF responses, not camera originals. Original provider volume PDFs are retained separately.

The [e-text inventory](etext-inventory.json) and [research records](research/README.md) distinguish original supplied files from reproducible extractions. No Tibetan reading has been corrected or harmonized.

Run `git lfs pull` after cloning. From the repository root: `shasum -a 256 -c editions/SHA256SUMS`. For full image/PDF verification: `uv run --with pikepdf --with pillow python editions/verify_assets.py`. See [VALIDATION.json](VALIDATION.json) for scope and results.

For decoded-pixel comparison of every assembled page: `uv run --with pikepdf --with pillow python editions/verify_image_pixels.py`. The recorded result is [PIXEL-VALIDATION.json](PIXEL-VALIDATION.json).
