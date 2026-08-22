# Evidence-backed case

## Runtime screen evidence corrected extraction labels

- **Search terms:** wrong extraction label, metadata mismatch, tile indices, mislabeled segment, screen evidence
- **Observed scope:** Option and pause labels in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** A human-authored Japanese metadata label was translated even though it disagreed with the phrase assembled by the screen's tile indices. Removing the presumed display path did not remove the bad label.
- **Decisive test:** The segment's tile indices were decoded directly from the binary and their assembly order was retraced.
- **Established result:** A label attached during extraction was not source-text evidence. The tile data actually consumed by the screen corrected the mislabeled entry.
- **Transfer limit:** A removal test cannot isolate a labeling error if it also changes the input data or assembly order.
- **Related criteria:** `references/strategy/debugging.md` §2.2·§6, `references/strategy/text-extraction.md` §1.2·§4.2.
