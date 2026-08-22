# Logical tile indices are not physical coordinates

- **Search terms:** logical tile number, physical tile coordinate, tile base, CHR index, round-trip graphics
- **Observed scope:** Background tilemap encoders for PC Engine CD and SNES assets.
- **Failure context:** One encoder used logical tile numbers as physical coordinates; another assumed a nonzero original tile base was zero. Both damaged the screen or protected background.
- **Decisive test:** Original screen data was encoded without edits and compared with the actual upload destination and physical tiles. Applying the source's number transform restored both round-trip equality and protected regions.
- **Established result:** Tilemap numbering and physical storage coordinates had to be derived from the consumer, not chosen as encoder defaults.
- **Transfer limit:** Re-derive the logical-to-upload transform for every screen and background layer.
- **Related criteria:** `references/platforms/pce.md` §2, `references/strategy/graphics-text.md` §2·§4.
