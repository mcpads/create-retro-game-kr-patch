# Whole-canvas rendering preserved cross-tile effects

- **Search terms:** composite canvas, tile seams, outline, gradient, shine, render then split
- **Observed scope:** Multi-tile SNES labels whose outline, background, gradient, or highlight crossed physical tile boundaries.
- **Decision context:** Rendering each tile independently broke continuous visual effects at tile seams.
- **Evidence:** The complete label was composed as one canvas, then split according to the verified tile, subtile, palette, storage, and transfer order. Tests on multiple entry screens confirmed that the seams and effects remained intact.
- **Established result:** Rendering the full label before splitting it produced continuous cross-tile effects.
- **Transfer limit:** Re-derive canvas coordinates, protected regions, and storage order for each asset.
- **Related criteria:** `references/strategy/graphics-text.md` §2·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.
