# Asset reachability does not prove readable text

- **Search terms:** false Hangul PoC, bytes reach VRAM, wrong tile, legibility, reachability versus visibility
- **Observed scope:** An early graphics-tile PoC and a later dialogue-font PoC in the same SNES project.
- **Failure context:** Patched bytes matched VRAM, but the changed tile was decoration or blank space and did not form legible Hangul.
- **Evidence:** Magnified runtime captures disproved the first interpretation. A later dialogue path connected storage, load, transformation, and display and rendered legible Hangul in the dialogue box.
- **Established result:** The first experiment proved asset reachability only; the later experiment proved both reachability and visible Hangul.
- **Transfer limit:** Storage and VRAM byte agreement does not prove the intended glyph or its legibility.
- **Related criteria:** `references/strategy/poc.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/font-strategy.md` §6.
