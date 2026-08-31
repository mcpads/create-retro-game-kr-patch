# Shared boundary logic let generator errors pass validation

- **Search terms:** shared generator bug, shared validator formula, JIS boundary, Shift_JIS 0x7F, exhaustive glyph display
- **Observed scope:** JIS-to-Shift_JIS conversion at an extension-row boundary in PC-98 titles.
- **Failure context:** An odd-row boundary formula mapped cell `0x5F` to forbidden trail byte `0x7F`. The glyph generator and validator shared the same error, so agreement between them did not expose it.
- **Evidence:** Independent enumeration of both row parities and runtime markers at the boundary established the required skip from `0x7E` to `0x80` and added a separate forbidden-value check.
- **Established result:** Independent boundary enumeration and real consumer display found a defect hidden by two components sharing one formula.
- **Transfer limit:** Do not establish an encoding boundary from generator-validator agreement when they share logic. Exercise forbidden and boundary values independently and compare them with the real consumer.
- **Related criteria:** `references/strategy/font-strategy.md` §2·§4, `references/strategy/build-and-verify.md` §4·§5, `references/conventions/project-conventions.md` §5.1·§5.3.
