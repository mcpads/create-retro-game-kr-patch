# Input glyphs and result glyphs may use different assets

- **Search terms:** name-entry candidates, result glyph mismatch, BNCG, MES font, NFTR no effect, multiple render paths
- **Observed scope:** Name-entry candidates and post-selection name rendering in revision 0 of the Japanese Nintendo DS release of Dragon Quest IX.
- **Failure context:** Replacing an `い` glyph in the apparent NFTR did not change the screen. It was easy to assume that the candidate grid and selected-name display shared one font because they belonged to the same UI.
- **Evidence:** A BNCG-only build changed only the candidate grid. Changing both BNCG and the matching MES slot made the grid, editing and confirmation displays, and later name displays agree.
- **Established result:** The candidate grid came from pre-rendered BNCG graphics, while the selected name came from MES glyphs. Both consumers had to change for one logical character slot.
- **Transfer limit:** Trace candidate and result supply paths separately for every screen. An NFTR that has no effect on one path remains a candidate elsewhere.
- **Related criteria:** `references/strategy/font-strategy.md` §5, `references/strategy/runtime-assets.md` §2.
