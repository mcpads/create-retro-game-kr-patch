# Evidence-backed case

## Incomplete-token truncation consumed terminators

- **Search terms:** token-boundary truncation, incomplete prefix, fixed slot, terminator consumed, `FB`, `FA`
- **Observed scope:** A two-byte prefix encoding in an SNES text path.
- **Failure context:** Truncating a translation to the source byte length left a lone `FB` or `FA` prefix. The game consumed the following `FF` terminator as the second character byte and lost the terminator.
- **Decisive test:** The truncated output was parsed again with the same tokenizer. Removing an incomplete final token and returning to the previous character boundary removed the failure.
- **Established result:** Fixed-byte truncation had to end at a complete game token, not merely at the target byte count.
- **Transfer limit:** An even byte count does not prove a valid boundary in every variable-length encoding. This case selects the cut point only after a shortening decision has been approved.
- **Related criteria:** `references/strategy/reinsertion.md` §1.1, `references/strategy/text-extraction.md` §2.
