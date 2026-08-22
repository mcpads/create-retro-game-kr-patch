# Evidence-backed case

## Translated screens may have multiple visual layers

- **Search terms:** duplicate title layer, sprite overlay, background edit, multiple entry paths, palette cycle, Japanese residue
- **Observed scope:** A PC Engine CD title subtitle duplicated in the background and a high-priority sprite, reached through two entry paths.
- **Failure context:** Editing only the background left the Japanese subtitle sprite over the Korean graphic. Fixing one entry path did not establish the other path.
- **Decisive test:** Background and sprite consumers were traced separately, the sprite was rebuilt from the final Korean background, and both entry paths were checked while the palette cycled.
- **Established result:** Every overlapping graphics layer and entry path had to be updated to remove the original presentation.
- **Transfer limit:** Enumerate actual graphics layers and entry paths rather than inferring them from file count.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.
