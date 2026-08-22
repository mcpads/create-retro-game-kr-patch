# Evidence-backed case

## Small-label contrast changed across UI states

- **Search terms:** small UI label, outline contrast, selected background, limited palette, pixel typography, clipping
- **Observed scope:** Small confirmation labels and their real selected-state background in a PlayStation UI.
- **Decision context:** The label needed separate background, outline, and body roles within a limited palette and without antialiasing.
- **Evidence:** Output was restricted to the three declared palette indices and displayed as `예` and `아니오` on the real confirmation screen. Outline and body remained distinguishable without clipping or adjacent-UI damage.
- **Established result:** Pixel typography constrained to three semantic palette roles preserved contrast and legibility on the actual selected background.
- **Transfer limit:** Recheck contrast, clipping, and surrounding UI under the real palette and state background of every other surface.
- **Related criteria:** `references/strategy/graphics-text.md` §2·§4, `references/strategy/font-strategy.md` §4, `references/strategy/build-and-verify.md` §5.
