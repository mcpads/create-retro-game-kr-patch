# Evidence-backed case

## Isolated removal rejected the suspected root cause

- **Search terms:** wrong root cause, suspected hook removed, symptom persists, WRAM overlap, DMA source
- **Observed scope:** Corrupted SNES tiles initially attributed to a VRAM hook.
- **Failure context:** Several observations fit the hook hypothesis, but they did not distinguish it from another writer corrupting the DMA source.
- **Decisive test:** A build with only the suspected hook removed still failed. Following the DMA source then showed that the Korean font occupied WRAM used by the game.
- **Established result:** The actual cause was a WRAM collision, not the suspected hook.
- **Transfer limit:** Removing a suspect is a valid rejection test only when the removal does not change other relevant paths.
- **Related criteria:** `references/strategy/debugging.md` §2.2.
