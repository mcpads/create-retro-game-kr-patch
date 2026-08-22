# Generated layouts invalidate stale fixed writes

- **Search terms:** overlapping writes, stale fixed offset, literal pool corruption, generated layout, write ownership
- **Observed scope:** Generated code and its literal pool in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** After layout became generator-controlled, a leftover fixed-address write still overwrote the literal pool at its new location.
- **Evidence:** The generated ranges and manual writes were compared in the final binary and shown to modify the same bytes.
- **Established result:** Removing the obsolete direct write and leaving one generator responsible for the range eliminated the literal-pool corruption.
- **Transfer limit:** Recompute final write ranges and overlap for every new layout.
- **Related criteria:** `references/strategy/build-and-verify.md` §1, `references/conventions/project-conventions.md` §5.2.
