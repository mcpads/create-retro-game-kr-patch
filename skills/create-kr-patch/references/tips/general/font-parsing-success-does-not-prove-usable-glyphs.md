# Font parsing success does not prove usable glyphs

- **Search terms:** empty glyph, font parses, zero-size raster, bitmap-only font, rasterizer compatibility
- **Observed scope:** A bitmap-embedded font whose outline path returned empty Hangul rasters.
- **Failure context:** File parsing succeeded, but representative Hangul glyphs rasterized to `0×0`, allowing the build to emit empty font pages.
- **Evidence:** Bitmap tables, effectively empty outlines, representative glyph dimensions, and the total empty-glyph count were inspected. An outline-based font through the same path returned pixels.
- **Established result:** Successful font parsing did not prove usable glyph output; representative dimensions and empty-glyph counts caused the bad asset to be rejected.
- **Transfer limit:** Repeat the representative-glyph check when font structure, code points, rasterizer, or raster path changes.
- **Related criteria:** `references/strategy/font-strategy.md` §3.2·§4·§6, `references/conventions/project-conventions.md` §4·§5.3.
