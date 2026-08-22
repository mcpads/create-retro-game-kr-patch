# Reused slots retain unwritten data

- **Search terms:** ring buffer residue, fixed-width slot, blank trailing slot, partial write, scrolling banner
- **Observed scope:** A horizontally scrolling ending banner that reused fixed-width slots.
- **Failure context:** Overlong text clipped or overlapped the next slot, while short or empty trailing slots left previous content in unwritten cells.
- **Decisive test:** Slot width and count were derived from the consumer, every slot containing text and every blank slot was written to the exact width, and the final slots were observed through reuse.
- **Established result:** The reused buffer did not clear unwritten cells; blank slots and unused cells required explicit space data.
- **Transfer limit:** Re-derive slot width, count, reuse order, and clearing behavior for each consumer. Do not transfer the numeric limits.
- **Related criteria:** `references/strategy/translation-workflow.md` §4, `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.
