# Evidence-backed case

## Composite glyph layout changed tilemap arithmetic

- **Search terms:** 16x16 glyph, 2x2 tiles, N times 2, tilemap index, WRAM font, code-to-tile transform
- **Observed scope:** A 16x16 glyph path and its tilemap writer in the SNES release of Madou Monogatari.
- **Failure context:** Hangul tiles reached the intended WRAM address, but the screen kept reading different tiles under several layout hypotheses.
- **Decisive test:** Tracing the tilemap writer showed that horizontal indexing converted character code `N` to `N×2` and `N×2+1`. One visible glyph was a 2x2 arrangement of that left-right pair; address-only experiments had omitted this transform.
- **Established result:** This path required both the `N→N×2, N×2+1` transform and the 2x2 tile arrangement, not only the glyph data address.
- **Transfer limit:** Derive the code-to-tile transform again for every other renderer.
- **Related criteria:** `references/strategy/font-strategy.md` §4·§5, `references/strategy/runtime-assets.md` §2, `references/platforms/snes.md` §3.
