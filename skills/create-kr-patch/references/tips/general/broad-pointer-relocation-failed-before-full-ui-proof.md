# Evidence-backed case

## Broad pointer relocation failed before full UI proof

- **Search terms:** pointer relocation overreach, partial runtime proof, UI not initialized, string consumed but not displayed, interaction QA
- **Observed scope:** A Saturn path that consumed a relocated string before UI initialization and a selection screen where display and interaction were fully observable.
- **Failure context:** Relocating every pointer-shaped value in range stopped progress despite passing restoration and load-size checks. Even a safe direct pointer proved neither window capacity nor display and interaction.
- **Evidence:** The pre-UI path preserved source structure and moved one confirmed direct pointer, proving entry and 16-bit character reads only. The real selection screen combined pointer, load size, window position, and width and verified full display, cursor movement, cancel, selection, and progress.
- **Established result:** Broad range-based relocation was rejected. One path proved complete UI behavior; the earlier path proved only string reachability and consumption.
- **Transfer limit:** Do not transfer one screen's success to another file or event. Recheck direct references, added-region boundary, alignment, terminator, load size, display, interaction, and progress per path.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.
