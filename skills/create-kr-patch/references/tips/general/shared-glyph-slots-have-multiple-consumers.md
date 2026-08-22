# Shared glyph slots have multiple consumers

- **Search terms:** shared glyph slot, tile alias, font collision, name-entry digits, reused graphics
- **Observed scope:** Shared glyph and tile slots across Dreamcast, SNES, Game Gear, Saturn, and PlayStation displays.
- **Failure context:** Changing a slot for one screen broke other labels, decoration, or numeric displays that consumed the same physical slot. On PlayStation, replacing name-entry digit codes also damaged month and day rendering.
- **Evidence:** All known consumers of each slot were enumerated. The fixes either allocated a new slot and updated its references, preserved shared pixels, or kept the date digit codes while changing only the remaining name-entry candidates.
- **Established result:** A physical slot was not owned by the first screen where it was found. Reassigning it without tracing shared consumers damaged other displays.
- **Transfer limit:** Enumerate text and non-text consumers again for every asset, then choose new allocation, shared-pixel preservation, or reference updates from the proven sharing relation.
- **Related criteria:** `references/strategy/font-strategy.md` §2·§5, `references/strategy/graphics-text.md` §2·§3, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4.
