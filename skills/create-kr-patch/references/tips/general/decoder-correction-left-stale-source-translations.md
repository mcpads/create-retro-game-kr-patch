# Decoder correction left stale-source translations

- **Search terms:** decoder correction, stale translation, raw 0x7F, Japanese full stop, impact audit
- **Observed scope:** Early Japanese decoding for the Game Gear release of Madou Monogatari 1 and Korean translations derived from it.
- **Failure context:** An old decoder rendered raw `0x7F` as an asterisk, but source and screen comparison established it as Japanese `。`. Fixing only the decoder and extracted source left many stale asterisks and misinterpretations in the Korean translation.
- **Decisive test:** ROM frequency and context, runtime samples, and another source version established the punctuation. Every Korean asterisk position was then audited, retranslated where affected, and cross-reviewed.
- **Established result:** Correcting an upstream decoder did not repair translations already authored from its wrong output; the affected translation set required its own source comparison.
- **Transfer limit:** Do not infer the impact from a character search alone. Compare stable source identities with the changed decoding rule and audit the full affected range.
- **Related criteria:** `references/conventions/translation-artifacts.md` §1·§5, `references/strategy/translation-workflow.md` §3.1, `references/conventions/data-formats.md` §2.
