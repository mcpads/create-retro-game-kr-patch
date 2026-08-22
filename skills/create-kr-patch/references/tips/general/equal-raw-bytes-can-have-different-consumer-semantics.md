# Equal raw bytes can have different consumer semantics

- **Search terms:** token semantic mismatch, same raw byte, prior patch, position control, punctuation code
- **Observed scope:** A Game Gear engine derived from an English-language release and a consumer in a Japanese NES release that assigned different meanings to the same raw values.
- **Failure context:** Variable and punctuation tokens from prior material were preserved numerically, but the target consumers interpreted them as literal string content or position controls.
- **Decisive test:** Each target token handler, pointer mapping, glyph mapping, and runtime value was compared with its source. Only confirmed static values became localized text, while position-control codes remained reserved from glyph allocation.
- **Established result:** Matching numeric tokens or glyph shapes in a prior patch did not establish matching semantics in the target engine.
- **Transfer limit:** Before preserving or replacing a token, re-establish its meaning and runtime variability in the target consumer.
- **Related criteria:** `references/strategy/translation-workflow.md` §3.1·§4, `references/strategy/text-extraction.md` §3.3·§4.4, `references/conventions/translation-artifacts.md` §3, `references/strategy/initial-survey.md` §4.
