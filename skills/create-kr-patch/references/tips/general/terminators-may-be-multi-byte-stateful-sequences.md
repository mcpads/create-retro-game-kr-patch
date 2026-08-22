# Terminators may be multi-byte stateful sequences

- **Search terms:** multi-byte terminator, single `FF`, `00 00`, `00 FF`, scanner misparse
- **Observed scope:** Multi-byte controls in an SNES text path.
- **Failure context:** A scanner treated a lone `FF` as a terminator even though the game rendered it as the character `今`.
- **Decisive test:** Following the consumer separated `00 00` termination, `00 FF` button wait, and lone `FF` character data. The affected range was then re-extracted.
- **Established result:** Testing only the first byte of a control sequence caused the extraction error.
- **Transfer limit:** Derive the complete terminator sequence and parser state for every other consumer.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1.
