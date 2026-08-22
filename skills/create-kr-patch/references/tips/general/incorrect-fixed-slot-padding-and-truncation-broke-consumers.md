# Evidence-backed case

## Incorrect fixed-slot padding and truncation broke consumers

- **Search terms:** fixed slot, padding before terminator, trailing controls, zero is not space, token-safe truncation, blank page
- **Observed scope:** Fixed-slot strings, trailing control sequences, and strings concatenated with later text on Saturn and PlayStation.
- **Failure context:** Padding after a terminator or inside a trailing control group became an argument and stopped execution. Padding every short string inserted unwanted gaps, and zero bytes were error glyphs on some paths rather than spaces.
- **Evidence:** Valid space tokens, trailing control groups, terminators, and concatenation behavior were established per string path. Padding position varied accordingly, and overlength input preserved character and control-token boundaries.
- **Established result:** Slot size alone did not determine tail handling; behavior depended on how the consumer read trailing controls and bytes after termination.
- **Transfer limit:** Re-establish valid space, control extent, odd-byte behavior, and post-terminator reads for every path. Truncation is allowed only for a separately approved wording reduction.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1·§4.4, `references/strategy/reinsertion.md` §1.1·§6, `references/conventions/data-formats.md` §5.
