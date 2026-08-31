# Zero-length entries may point to runtime text

- **Search terms:** zero-length entry, external string pointer, runtime-composed text, WRAM string, null pointer
- **Observed scope:** A Game Gear string table and dynamic money or status text assembled for the field screen.
- **Failure context:** A zero-length entry was treated as an empty string and its pointer was cleared, causing the game to parse boot code as text.
- **Discriminating evidence:** An exhaustive comparison of the original table showed that only the failing entries pointed outside the file bank into runtime-composed WRAM strings. Preserving the original pointers restored the display.
- **Established result:** Length zero represented an external runtime string reference in this range, not null or empty data.
- **Transfer limit:** Classify each empty-looking entry as null, empty text, an external range, or runtime-composed text before choosing how to preserve it.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§6, `references/strategy/runtime-assets.md` §2, `references/conventions/data-formats.md` §4.
