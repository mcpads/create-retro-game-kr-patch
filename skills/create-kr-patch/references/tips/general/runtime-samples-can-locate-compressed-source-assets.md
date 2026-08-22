# Runtime samples can locate compressed source assets

- **Search terms:** runtime sample reverse search, compressed font source, LZ scan, missed breakpoint, glyph cache
- **Observed scope:** Locating an unknown compressed font source from live glyph bytes.
- **Failure context:** WRAM and VRAM breakpoints repeatedly missed the initial load because the game used an accumulated glyph cache and DMA, while several live glyph samples and a verified decompressor were available.
- **Evidence:** Candidate ROM positions were decompressed with the verified format and bounded output. Results containing multiple live glyph tiles were rendered and compared byte-for-byte with WRAM samples.
- **Established result:** Reverse-searching verified decompression outputs with several runtime glyph samples located the compressed source and internal glyph layout.
- **Transfer limit:** Confirm a candidate only when the compression format and output bound are known and multiple live samples plus final display agree.
- **Related criteria:** `references/strategy/compression.md` §2·§3, `references/strategy/initial-survey.md` §2.2·§2.5, `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §4.
