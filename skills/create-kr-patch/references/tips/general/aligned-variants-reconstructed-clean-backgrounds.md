# Evidence-backed case

## Aligned variants reconstructed clean backgrounds

- **Search terms:** reconstruct clean background, 4bpp label variants, nibble comparison, palette semantics, no text-free source
- **Observed scope:** Several 4bpp label variants sharing one background in a Saturn title.
- **Decision context:** No text-free original existed. Byte-wise maximum and OR operations either ignored the two separate pixels in each byte or mixed color bits.
- **Evidence:** Variants with matching coordinates and palettes were compared per 4-bit pixel to choose the value where text disappeared. New text overwrote only non-background pixels.
- **Established result:** A text-free background could be recovered by comparing individual pixels across variants that truly shared background, coordinates, and palette.
- **Transfer limit:** Pixels covered by text in every variant remain unknown. If palette index order does not match brightness, derive background selection from color meaning instead of numeric extrema.
- **Related criteria:** `references/strategy/graphics-text.md` §2·§4.
