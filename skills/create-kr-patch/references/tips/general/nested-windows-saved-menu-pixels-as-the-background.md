# Nested windows saved menu pixels as the background

- **Search terms:** persistent menu residue, background backup, nested window, field spell, restore contamination
- **Observed scope:** A Game Gear field-spell path that rechecked a location event and opened a dialogue while the spell menu remained visible.
- **Failure context:** The event saved the visible menu over the outer window's background backup. Later restoration repeatedly reproduced the contaminated copy; the underlying background tiles were intact.
- **Discriminating evidence:** Fresh-process reproduction from an in-game save and observations at the background-save routine located the backup change before the visible residue. The shared spell-to-event call exposed the nested overwrite.
- **Established result:** Restoring the outer background before the shared event recheck prevented the observed overwrite. The same spell/event route, map return and a second field-spell path preserved the expected backup and normal interaction. Hook entry/return observations verified preserved registers.
- **Transfer limit:** Establish backup ownership and nested save/restore timing on the target. The observation left the defect's origin unresolved, and the correction affected future backups; old emulator states could retain contaminated copies.
- **Related criteria:** `references/strategy/debugging.md` §3·§5, `references/strategy/reinsertion.md` §5·§6, `references/strategy/runtime-assets.md` §2.
