# Duplicate text does not imply interchangeable pointers

- **Search terms:** merged duplicate strings, stable pointer slot ID, interior pointer, shared control block, translated offset
- **Observed scope:** A PlayStation story script where one pointer entered a complete control block inside another message and extraction merged the overlapping strings.
- **Failure context:** Renumbering deduplicated entries by list order translated the wrong pointer slot. Copying the interior tail as a separate source block left Japanese text when the interior pointer was used.
- **Evidence:** Extraction preserved original pointer-slot IDs and reinsertion prioritized them. Interior pointers were recalculated from corresponding complete control-block boundaries in source and translation, then checked with synthetic data for every entry path.
- **Established result:** Deduplication could not replace stable source pointer identities, and interior targets had to follow preserved structure rather than original byte distance.
- **Transfer limit:** This works only when the same structural boundary can be identified in both source and translation.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3·§4.1·§4.2, `references/strategy/reinsertion.md` §1.2·§2·§3, `references/conventions/data-formats.md` §4.
