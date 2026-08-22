# Evidence-backed case

## Record regrouping broke interior pointers

- **Search terms:** sub-string pointer, grouped translation entry, interior entry point, per-item padding, delimiter boundary
- **Observed scope:** A grouped translation entry whose component strings were independently referenced by a Saturn game.
- **Failure context:** Applying one total length delta to several names made earlier growth clip later names or move an interior pointer into another name.
- **Evidence:** Source and translation were split at the same delimiters and component counts were compared. Fixed slots were padded per component and direct pointers were recalculated from each component's original start and individual movement.
- **Established result:** Length and pointer correction had to use the sub-strings consumed by the game, not the enclosing translation record.
- **Transfer limit:** Apply this correspondence only when delimiter, component count, and consumption structure are preserved. Reject the grouped record or handle it separately when they cannot be matched.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3·§4.1·§4.2, `references/strategy/reinsertion.md` §1.1·§1.2·§2, `references/conventions/data-formats.md` §4.
