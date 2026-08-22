# Evidence-backed case

## Repeated glyph blocks may encode pre-shifted variants

- **Search terms:** pre-shifted glyph copies, variable-width font, four repeated blocks, X-coordinate alignment, clipped glyph
- **Observed scope:** 16x16 variable-width glyph data and its selector in the Mega Drive release of Madou Monogatari.
- **Failure context:** Four similar blocks per glyph looked duplicated or unused. Generating only one copy made glyphs disappear or clip at some horizontal alignments.
- **Evidence:** Consumer disassembly showed that the low two bits of the X coordinate selected one of four copies. The generator therefore produced glyphs shifted by 0, 1, 2, and 3 pixels.
- **Established result:** The repeated blocks were pre-shifted copies for variable-width alignment states.
- **Transfer limit:** Trace the copy-selection expression, composition method, and coordinate unit again to derive the required shifts for another renderer.
- **Related criteria:** `references/strategy/font-strategy.md` §4·§5, `references/strategy/runtime-assets.md` §2.
