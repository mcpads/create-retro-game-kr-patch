# Static overlays overwrote runtime-updated cells

- **Search terms:** dynamic tile overwritten, static overlay, state-dependent cells, broad post-DMA hook, save UI
- **Observed scope:** Save-slot, delete, and copy tilemaps in an SNES title containing both static and runtime-updated cells.
- **Failure context:** Reapplying a complete static Korean tilemap after every related transfer replaced dynamic slot and confirmation text. A temporary-buffer trigger also ran on neighboring screens.
- **Evidence:** Activation was narrowed by the final decompressed asset identity, dynamic cells were excluded, and only state-required static additions were applied. Occupied and empty slots, confirm and cancel, re-entry, and neighboring screens were checked.
- **Established result:** Excluding runtime-updated cells preserved dynamic state while allowing the fixed labels to remain translated.
- **Transfer limit:** Reconnect dynamic cells, stable state signal, asset identity, and write order for each target screen.
- **Related criteria:** `references/strategy/graphics-text.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §4·§6.
