# Post-decompression patches reused downstream transfers

- **Search terms:** post-decompression patch, reuse DMA, no recompressor, compressed UI, WRAM overwrite
- **Observed scope:** Several compressed UI assets in an SNES title.
- **Decision context:** Only part of each decompressed asset needed replacement, and preserving the game's existing transfer path avoided introducing a new compressor or DMA path.
- **Evidence:** Each decompression call was connected to its input identity, bounded WRAM output, and downstream DMA destination. Full replacements used verified decompressed results; partial replacements changed only the required WRAM region after original decompression. Entry and re-entry were tested on multiple screens.
- **Established result:** Replacing the required region immediately after the original decompression allowed the existing DMA path to carry the modified asset.
- **Transfer limit:** Intervene only where input identity, output bound, call state, downstream consumer, and last writer are all connected.
- **Related criteria:** `references/strategy/compression.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §4.
