# Font loads left overwritten motion caches marked valid

- **Search terms:** character reselect, attack freeze, motion cache, loaded flag, reused font arena
- **Observed scope:** A PlayStation Training mode whose character selectors temporarily reused memory occupied by common combat motions.
- **Failure context:** Selection and initial battle worked, but returning to selection and attacking afterward caused an address exception. Font loading had overwritten resident motion data while the native loaded flag still caused battle entry to skip reloading it.
- **Discriminating evidence:** Unchanged on-disc motion bytes contrasted with font data in the corrupted resident range, while the native loaded flag skipped restoration. The predecessor and failing artwork candidate shared selector code, so their artwork difference did not establish the cause.
- **Established result:** The shared selector font loader invalidated the native motion cache before overwriting it. Native battle entry then restored the complete source motion resource. Fresh execution verified its full resident bytes, repeated reselection, attacks, pause and representative registered-name display.
- **Transfer limit:** Establish resource lifetime and the validity state that authorizes reuse. Invalidation applies where the native owner reloads before consumption and the temporary asset remains valid until exit.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/name-entry.md` §5·§6, `references/strategy/debugging.md` §3·§5.
