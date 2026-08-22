# Evidence-backed case

## Self round-trips do not prove compressor compatibility

- **Search terms:** incompatible recompressor, self round-trip passes, original data recompressed, invalid back-reference, CNX v2
- **Observed scope:** CNX v2-compressed battle assets in a Saturn title.
- **Failure context:** Battle animation broke even though the changed file was isolated and the custom compressor-decompressor round-trip passed.
- **Decisive test:** Unmodified decompressed Japanese data was recompressed and reproduced the defect in the game while still passing the custom round-trip, isolating a semantic difference from the game decompressor.
- **Established result:** The compressor created matches against zero-filled output positions that had not yet been produced, while the game safely referenced only completed output. Restricting distance to produced bytes restored compatibility.
- **Transfer limit:** A self round-trip does not prove target-consumer compatibility. Test an unmodified recompressed asset in the real consumer.
- **Related criteria:** `references/strategy/compression.md` §4.1, `references/strategy/initial-survey.md` §3, `references/strategy/debugging.md` §2.2.
