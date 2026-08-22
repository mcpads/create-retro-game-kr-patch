# Evidence-backed case

## Residual correction turned composition into exact glyph compression

- **Search terms:** compositional Hangul compression, residual rows, XOR correction, exact glyph reconstruction, finished-font bank budget
- **Observed scope:** Runtime reconstruction of name glyphs for a finite Hangul repertoire in the Japanese Game Boy Color release of Arle no Bouken.
- **Decision context:** Storing every finished glyph exceeded the chosen bank budget, while exposing a rough component-only result would have reduced the approved visual target.
- **Evidence:** Common initial-medial and final components were combined, and only differing rows received sparse XOR corrections. An independent decoder and the generated target implementation reproduced every declared finished glyph exactly and rejected undeclared combinations.
- **Established result:** Composition served as a compression basis rather than the visible font style; bounded residual data restored the tracked finished glyphs exactly within the measured bank.
- **Transfer limit:** Recompute component classes, residual population, serialized indexes, code size, and output equivalence for the target font and cell. The measured savings and source-font choice do not transfer to another repertoire or renderer.
- **Related criteria:** `references/strategy/font-strategy.md` §2.2·§4, `references/strategy/name-entry.md` §5, `references/strategy/build-and-verify.md` §1.
