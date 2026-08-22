# Evidence-backed case

## Token width follows the consumer read unit

- **Search terms:** consumer read width, two-byte tokens, odd alignment, one-byte control, 65816
- **Observed scope:** An SNES text path whose consumer always read and advanced by two bytes.
- **Failure context:** An early Korean encoder emitted one-byte spaces and controls, shifting every following tile pair onto an odd boundary.
- **Decisive test:** The consumer's two-byte read and advance were confirmed. Serializing every token as a word and rejecting controls at odd positions removed the alignment failure.
- **Established result:** Token width followed the consumer's read unit, not the visible character format.
- **Transfer limit:** The use of a 65816 CPU does not by itself establish a two-byte text unit.
- **Related criteria:** `references/strategy/text-extraction.md` §2, `references/strategy/initial-survey.md` §2.2, `references/platforms/snes.md` §5.
