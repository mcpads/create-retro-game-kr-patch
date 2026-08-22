# Standard-decoder rejection does not prove free code space

- **Search terms:** CP932 decoder rejection, custom Shift_JIS, unused lead byte, code-space collision, 0xEB
- **Observed scope:** A game-specific Shift_JIS-like consumer in the PC-98 Madou Monogatari titles.
- **Failure context:** Statistics limited to byte pairs accepted by standard CP932 classified lead byte `0xEB` as unused, while the source contained game-specific pairs rejected by the standard decoder.
- **Decisive test:** Every parser-reachable two-byte pair in the source was counted, game-specific pairs were reserved, and the Hangul encoder was verified not to emit them.
- **Established result:** `0xEB` was not free code space because the game consumed non-CP932 pairs under that lead byte.
- **Transfer limit:** This result covers direct two-byte codes only. Evaluate the code-space budget for escape forms of other lengths separately.
- **Related criteria:** `references/strategy/font-strategy.md` §2.1, `references/strategy/text-extraction.md` §2, `references/platforms/pc98.md` §5.
