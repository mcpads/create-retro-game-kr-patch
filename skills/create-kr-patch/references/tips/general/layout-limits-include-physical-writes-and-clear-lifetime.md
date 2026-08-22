# Layout limits include physical writes and clear lifetime

- **Search terms:** physical write footprint, stale tile, clear lifetime, logical width, adjacent HUD damage
- **Observed scope:** Dialogue, ending, and map-label regions on SNES, NES, and Mega Drive whose physical writes outlived their logical text.
- **Failure context:** Placement used visible blank space or cursor advance as the limit. Old tiles remained, physical cells reached adjacent UI, or later states did not clear the covered background.
- **Evidence:** Written cells and cells cleared or overwritten by later states were traced separately. Logical advance and physical footprint were measured independently, and reused regions were either fully cleared or kept within the original update area.
- **Established result:** The usable layout limit depended on both the physical write footprint and the lifetime over which later states cleared or overwrote it, not on visible space alone.
- **Transfer limit:** Confirm terminators, physical footprint, and following state transitions before removing padding, extending rows, or placing labels.
- **Related criteria:** `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/translation-workflow.md` §4, `references/strategy/build-and-verify.md` §5.
