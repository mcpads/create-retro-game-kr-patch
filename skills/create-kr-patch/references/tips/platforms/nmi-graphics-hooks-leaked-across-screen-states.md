# NMI graphics hooks leaked across screen states

- **Search terms:** NMI hook, CHR overwrite, screen discriminator, BG1 tilemap base, re-entry, adjacent screen
- **Observed scope:** An SNES puzzle screen whose conditional-message CHR and tilemap were overwritten during NMI.
- **Failure context:** Passing new state from puzzle processing into NMI did not reliably distinguish initial entry, re-entry, and adjacent screens.
- **Decisive test:** The new signal was removed. The NMI consumer instead checked the current screen mode, BG1 tilemap base, and original tilemap pattern together. A counterexample screen that matched only the global state was excluded, and the overwrite then ran only on the intended screen.
- **Established result:** State already consumed by NMI was sufficient to identify this screen without introducing a separate cross-phase flag.
- **Transfer limit:** Revalidate that the chosen screen mode, tilemap base, and original pattern uniquely identify every other target screen at consumption time.
- **Related criteria:** `references/strategy/reinsertion.md` §4, `references/strategy/debugging.md` §2.2, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4, `references/platforms/snes.md` §1.
