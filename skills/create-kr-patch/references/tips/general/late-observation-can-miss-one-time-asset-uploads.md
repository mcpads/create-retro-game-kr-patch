# Late observation can miss one-time asset uploads

- **Search terms:** late breakpoint, save state, one-time VRAM upload, missed producer, cached asset
- **Observed scope:** A VRAM upload performed during scene initialization on Game Gear and a scrolling banner written once at scene start on SNES.
- **Failure context:** A save state retaining old VRAM or a breakpoint armed after the screen appeared was used to reject the real source candidate and write path. In both cases the load or write had already finished.
- **Discriminating evidence:** Observation started before boot or scene entry, and the modified stored source was followed through loading and transfer to its consumer.
- **Established result:** A save state or late breakpoint did not prove the absence of a one-time load or write that had already occurred.
- **Transfer limit:** Start before the relevant load or write when a screen reuses cache or VRAM. Use save states only to reproduce later consumer behavior.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §2.1·§4.
