# Visible text does not exclude runtime side effects

- **Search terms:** first font load, CD read, background music stops, runtime asset side effect, Hangul visible
- **Observed scope:** The first runtime CD load of Hangul font data and concurrent background-music state on PlayStation.
- **Failure context:** Hangul became visible after replacing the BIOS provider, but music stopped during the first font read. Visible glyphs were mistaken for completion of the whole font path.
- **Discriminating evidence:** Command completion and mode restoration alone still left music stopped. Compare drive state, consumed sector, callbacks, audio-buffer supply and complete font bytes across the load. A later SDK-based loader restored music-region reads and nonzero audio samples after the first font load and a native video-to-font reload.
- **Established result:** The later artifact preserved the observed font bytes, callbacks, menu input and audio supply on those natural paths. A forced cache invalidation combined with menu transition still lost audio supply; it remained a diagnostic with different entry conditions, not a reproduced failure of the successful natural route.
- **Transfer limit:** Within a changed load's impact range, distinguish visible glyphs, audio supply and actual listening quality. Nonzero samples do not prove uninterrupted or noise-free music. Ending reloads, mixed streams and CD-error recovery were not established by these samples; separate state intervention from native load conditions before assigning a shared cause.
- **Related criteria:** `references/strategy/reinsertion.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4·§5, `references/platforms/ps1.md` §5.
