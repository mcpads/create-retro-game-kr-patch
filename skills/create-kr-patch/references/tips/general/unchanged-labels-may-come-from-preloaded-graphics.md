# Unchanged labels may come from preloaded graphics

- **Search terms:** menu label unchanged, no VRAM write, preloaded sprite text, selected and unselected states, wrong main font
- **Observed scope:** Two-state battle-menu tabs in a Saturn title.
- **Failure context:** The Japanese tab survived main-font edits, and opening the menu produced no new VRAM write, rejecting a draw-time main-font hypothesis.
- **Discriminating evidence:** Selected and unselected label pairs were decoded directly from a decompressed sprite asset and matched to the screen. Replacing both states changed the complete tab.
- **Established result:** The edit target was a pair of preloaded sprite images, not the main font.
- **Transfer limit:** Absence of a draw-time write does not identify a stored file or offset. Connect decoded storage to the visible result.
- **Related criteria:** `references/strategy/graphics-text.md` §1, `references/strategy/runtime-assets.md` §2.
