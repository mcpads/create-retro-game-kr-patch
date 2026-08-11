# SNES-specific cases

## Composite glyph layout changed tilemap arithmetic

- **Search terms:** 16x16 glyph, 2x2 tiles, N times 2, tilemap index, WRAM font, code-to-tile transform
- **Observed scope:** A 16x16 glyph path and its tilemap writer in the SNES release of Madou Monogatari.
- **Failure context:** Hangul tiles reached the intended WRAM address, but the screen kept reading different tiles under several layout hypotheses.
- **Decisive test:** Tracing the tilemap writer showed that horizontal indexing converted character code `N` to `N×2` and `N×2+1`. One visible glyph was a 2x2 arrangement of that left-right pair; address-only experiments had omitted this transform.
- **Established result:** This path required both the `N→N×2, N×2+1` transform and the 2x2 tile arrangement, not only the glyph data address.
- **Transfer limit:** Derive the code-to-tile transform again for every other renderer.
- **Related criteria:** `references/strategy/font-strategy.md`, `references/strategy/runtime-assets.md` §2.

## NMI graphics hooks leaked across screen states

- **Search terms:** NMI hook, CHR overwrite, screen discriminator, BG1 tilemap base, re-entry, adjacent screen
- **Observed scope:** An SNES puzzle screen whose conditional-message CHR and tilemap were overwritten during NMI.
- **Failure context:** Passing new state from puzzle processing into NMI did not reliably distinguish initial entry, re-entry, and adjacent screens.
- **Decisive test:** The new signal was removed. The NMI consumer instead checked the current screen mode, BG1 tilemap base, and original tilemap pattern together. A counterexample screen that matched only the global state was excluded, and the overwrite then ran only on the intended screen.
- **Established result:** State already consumed by NMI was sufficient to identify this screen without introducing a separate cross-phase flag.
- **Transfer limit:** Revalidate that the chosen screen mode, tilemap base, and original pattern uniquely identify every other target screen at consumption time.
- **Related criteria:** `references/strategy/reinsertion.md` §4, `references/strategy/debugging.md` §2.

## One-time OBJ uploads ignored later WRAM patches

- **Search terms:** OBJ VRAM, OAM, one-time DMA, preloaded sprite text, WRAM no effect, last writer, LZ hook
- **Observed scope:** Equipment and shop text rendered as OBJ tiles in the SNES release of Madou Monogatari: Hanamaru Daiyouchienji.
- **Failure context:** The original OBJ CHR was transferred from WRAM to VRAM only during screen initialization. Editing the WRAM buffer afterward had no visible effect, while a broad hook also overwrote field NPC tiles.
- **Evidence:** The OBJ VRAM load order and last writer were traced. A ROM-to-OBJ-VRAM DMA ran while display output was stopped. The shop hook sampled its input state before the decompressor clobbered it and transferred only after the last relevant LZ call, excluding the NPC path.
- **Established result:** Preloaded text whose original OAM layout and attributes had to remain intact was changed by replacing only its pixel tiles in OBJ VRAM after the final relevant load.
- **Transfer limit:** Validate OBJ tile transfer separately from OAM layout. Recheck display-off timing, DMA restoration, destination, palette, last writer, and trigger conditions for every other screen.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/graphics-text.md` §3, `references/strategy/reinsertion.md` §4.
