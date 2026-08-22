# Coupled geometry parameters disambiguated graphics assets

- **Search terms:** unknown bpp, width, height, offset, stride, padding, plausible partial image, asset boundary
- **Observed scope:** Saturn and PlayStation graphics with several bit-depth, width, height, and start-offset candidates of equal stored length.
- **Decision context:** Some candidates produced plausible letters or icons, while different regions used different stride or padding and adjacent effects or buttons could be misclassified as one image.
- **Evidence:** Row byte count, full-image continuity, repeated block structure, palette distribution, and neighboring asset boundaries were compared, and only established regions were re-encoded.
- **Established result:** Stored length and a plausible partial rendering did not establish bit depth, dimensions, or boundaries.
- **Transfer limit:** Select discriminating evidence again for each asset and do not apply one region's interpretation to the whole file.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§2·§3, `references/strategy/initial-survey.md` §2.2, `references/strategy/runtime-assets.md` §2.
