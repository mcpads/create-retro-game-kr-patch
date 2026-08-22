# Visible layout and screen bounds determined dialogue-window size

- **Search terms:** dialogue box width, dialogue box height, visible glyph count, control tokens, line count, screen boundary
- **Observed scope:** Dynamic battle-dialogue window sizing for Korean text.
- **Failure context:** Longer or multiline Korean text overflowed a fixed-size window designed for Japanese text, while serialized byte or token counts also overestimated visible width by counting controls and line changes.
- **Evidence:** Korean text was tokenized like the consumer. Controls were excluded from width, line changes determined row count, and the resulting window was independently clamped to the actual screen boundary. Tests in runtime battle scenes confirmed both the window size and text layout.
- **Established result:** Maximum visible width and line count determined content size, while the screen edge remained a separate placement limit.
- **Transfer limit:** Re-measure token semantics, coordinate system, and visible boundary for every other window consumer.
- **Related criteria:** `references/strategy/translation-workflow.md` §4, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.
