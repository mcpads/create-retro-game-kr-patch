# Evidence-backed case

## Pointer tables may not be reread between states

- **Search terms:** second pointer ignored, sequential block, pointer lifetime, table not reread, contiguous placement
- **Observed scope:** Consecutive menu and rule-editor text blocks in an SNES title.
- **Failure context:** Both blocks had table entries, suggesting that changing the second entry would redirect the second screen. The consumer instead advanced and reused the current text-object pointer after the first block.
- **Decisive test:** Pointer initialization, increment, and reuse were traced across the transition. Placing both new blocks contiguously and updating both references preserved menu entry, value changes, and return.
- **Established result:** A table entry's existence did not prove that the consumer reread it during the transition.
- **Transfer limit:** Re-derive table rereads and object-pointer lifetime for every other entry path. Require contiguous placement only for the proven path.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §2·§6, `references/strategy/runtime-assets.md` §2.
