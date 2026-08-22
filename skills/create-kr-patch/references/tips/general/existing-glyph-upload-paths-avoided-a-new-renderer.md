# Existing glyph upload paths avoided a new renderer

- **Search terms:** system font hook, glyph provider, 1bpp to 4bpp, reuse upload path, VRAM cache
- **Observed scope:** System glyph-provider calls followed by bitmap conversion and VRAM upload on PC Engine CD and PlayStation.
- **Decision context:** A complete replacement renderer appeared necessary for Hangul, but the original path already handled conversion, cache, and upload after obtaining a glyph.
- **Evidence:** Only the provider boundary was replaced with a compatible source while the original downstream path remained. Hangul and existing characters were displayed together.
- **Established result:** Both consumers could reuse the original conversion and upload path by replacing only the glyph-provider interface.
- **Transfer limit:** Recheck provider ABI, bit layout, buffer lifetime, cache identity, and downstream conversion for every caller.
- **Related criteria:** `references/strategy/font-strategy.md` §5, `references/strategy/reinsertion.md` §4, `references/strategy/runtime-assets.md` §2, `references/strategy/poc.md` §3·§5.
