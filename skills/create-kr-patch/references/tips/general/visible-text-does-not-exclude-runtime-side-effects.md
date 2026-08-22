# Evidence-backed case

## Visible text does not exclude runtime side effects

- **Search terms:** first font load, CD read, background music stops, runtime asset side effect, Hangul visible
- **Observed scope:** The first runtime CD load of Hangul font data and concurrent background-music state on PlayStation.
- **Failure context:** Hangul became visible after replacing the BIOS provider, but music stopped during the first font read. Visible glyphs were mistaken for completion of the whole font path.
- **Evidence:** Music still stopped in a build that added CD-command completion and mode restoration around the first font load.
- **Established result:** Glyph display and preservation of audio during the first CD load were separate claims. The former was proven; an audio-safe load path was not.
- **Transfer limit:** For every new runtime load, verify concurrent audio, input, and display state in addition to the asset's visible result.
- **Related criteria:** `references/strategy/reinsertion.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4·§5, `references/platforms/ps1.md` §5.
