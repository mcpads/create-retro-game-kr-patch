# Stored glyph cells exceeded the visible render area

- **Search terms:** clipped final consonant, glyph cell height, sampled rows, baseline, bottom row, storage bounds
- **Observed scope:** Story-dialogue glyphs stored in 14-row cells in a PSP game.
- **Failure context:** Hangul fit the stored cell, but final consonants reaching its bottom row were clipped in the game.
- **Discriminating evidence:** Source glyphs used rows 0–11 or 0–12. Patched ink reaching row 13 was visibly cut off. A smaller glyph and raised baseline kept ink within rows 0–11; replay of the observed story path showed intact final consonants.
- **Established result:** The build gained an ink-row bound. Its conservative 12-row setting was distinct from the source's observed use of 13 rows; an earlier claim that the renderer drew only 12 rows was corrected.
- **Transfer limit:** Distinguish storage dimensions, observed sampling or clipping, and the chosen layout margin. Establish the visible area for the actual consumer before using cell capacity as a placement limit.
- **Related criteria:** `references/strategy/font-strategy.md` §4·§5, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.
