# Shared glyph slots have multiple consumers

- **Search terms:** shared glyph slot, tile alias, font collision, name-entry digits, reused graphics, sampled texels, stretched panel, speech-bubble color
- **Observed scope:** Shared glyph and tile slots across Dreamcast, SNES, Game Gear, Saturn, and PlayStation displays, plus a shared text texture in a Nintendo 3DS game.
- **Failure context:** Changing a slot for one screen broke other labels, decoration, or numeric displays that consumed the same physical slot. On PlayStation, replacing name-entry digit codes also damaged month and day rendering.
- **Discriminating evidence:** All known consumers of each slot were enumerated. The fixes either allocated a new slot and updated its references, preserved shared pixels, or kept the date digit codes while changing only the remaining name-entry candidates. In the 3DS case, a speech-bubble panel sampled a few white texels inside the original lettering; relettering changed them to green. The correction reserved those texels. A wider crop audit produced candidates requiring texture-to-consumer confirmation.
- **Established result:** A physical slot was not owned by the first screen where it was found. Reassigning it without tracing shared consumers damaged other displays.
- **Transfer limit:** Establish text and non-text sharing at the slot or sampled-subregion level. Choose allocation, pixel preservation, or reference updates from that relation; candidate crop matches alone do not prove consumption.
- **Related criteria:** `references/strategy/font-strategy.md` §2·§5, `references/strategy/graphics-text.md` §2·§3, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4.
