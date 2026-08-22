# Evidence-backed case

## Shared hooks corrupted caller-specific state

- **Search terms:** shared hook, caller-saved register, Z80 B register, loop counter corruption, graphics plane state
- **Observed scope:** A glyph-expansion hook shared by two Game Gear text loops.
- **Failure context:** The hook used `B` as a temporary prefix index. That worked for one caller, but another used `B` as its per-line character counter, so return changed the loop into a wraparound and prevented screen transfer.
- **Decisive test:** Entry and return register meanings were compared across every caller of the shared routine. Preserving `B` and normalizing each caller's graphics-plane state restored glyph expansion and transfer on dialogue and field paths.
- **Established result:** The shared hook worked only after preserving the second caller's character counter and the plane state expected by each path.
- **Transfer limit:** Adopt a shared hook only after accounting for every observed caller's inputs, outputs, and original behavior. Re-derive preserved registers per path.
- **Related criteria:** `references/strategy/reinsertion.md` §4, `references/strategy/debugging.md` §3·§5.
