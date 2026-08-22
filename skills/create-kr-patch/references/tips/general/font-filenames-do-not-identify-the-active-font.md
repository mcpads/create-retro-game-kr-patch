# Font filenames do not identify the active font

- **Search terms:** wrong active font, multiple font sizes, font filename, glyph sheet probe, code-to-glyph mismatch
- **Observed scope:** One story-dialogue screen and multiple font sizes in the Dreamcast release of Sakura Wars 2.
- **Failure context:** A prior small-font experiment and filenames were used to assume that story dialogue used the same font. Slot numbers derived from one size were also transferred to another.
- **Evidence:** Distinctive probes were inserted across each candidate sheet. Runtime display selected a different sheet from the earlier experiment, and independent decoding showed that the same character occupied different slots between sizes.
- **Established result:** The active dialogue font and its code-to-glyph mapping had to be established independently; mappings were not shared across font sizes.
- **Transfer limit:** Prove the active font and that sheet's code-to-glyph mapping separately for every other screen.
- **Related criteria:** `references/strategy/font-strategy.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/poc.md` §3·§5.
