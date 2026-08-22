# One-time OBJ uploads ignored later WRAM patches

- **Search terms:** OBJ VRAM, OAM, one-time DMA, preloaded sprite text, WRAM no effect, last writer, decompression hook
- **Observed scope:** Equipment and shop text rendered as OBJ tiles in the SNES release of Madou Monogatari: Hanamaru Daiyouchienji.
- **Failure context:** The original OBJ CHR was transferred from WRAM to VRAM only during screen initialization. Editing the WRAM buffer afterward had no visible effect, while a broad hook also overwrote field NPC tiles.
- **Evidence:** The OBJ VRAM load order and last writer were traced. A final transfer ran during screen initialization, and the replacement was narrowed to the target asset and placed after its last decompression while excluding the field-NPC path.
- **Established result:** Replacing only the text's pixel tiles in OBJ VRAM after the final relevant load changed the preloaded text while preserving the original OAM layout and attributes.
- **Transfer limit:** Validate OBJ tile transfer separately from OAM layout. Recheck display-off timing, DMA restoration, destination, palette, last writer, and trigger conditions for every other screen.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/graphics-text.md` §3, `references/strategy/reinsertion.md` §4, `references/platforms/snes.md` §3·§4.
