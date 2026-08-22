# A glyph mapping may be range-local

- **Search terms:** false global glyph map, range-local mapping, first-occurrence order, later text corrupt, unknown mapping switch
- **Observed scope:** Message text and a built-in glyph pool in a Saturn title.
- **Failure context:** Early samples suggested first-occurrence glyph order, so each new code across the file was assigned the next global glyph slot. Later kanji messages decoded incorrectly.
- **Evidence:** The glyph pool exceeded the number of globally found codes, the same code selected different glyphs by range, the global map rendered broken messages, and runtime consumers read different contiguous glyph regions.
- **Established result:** A single file-wide map was rejected. No global extraction or reinsertion map was adopted while the range-switch rule remained unknown.
- **Transfer limit:** Map and transform only ranges whose switch rule and consumer index calculation are established.
- **Related criteria:** `references/strategy/text-extraction.md` §2, `references/strategy/font-strategy.md` §2, `references/strategy/debugging.md` §2.2.
