# Shorter dialogue can change voice timing

- **Search terms:** voice desync, dialogue timing, wait frames, shorter translation, early audio cutoff, padding
- **Observed scope:** Voice-synchronized dialogue windows and wait or transition controls in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** Shorter Korean text caused later voice lines to be cut off progressively earlier. Padding the unused scene bytes back to the original size was proposed as a timing fix.
- **Evidence:** Disassembly showed that bytes after the transition control were not consumed. Controlled wait-value changes altered both visible pacing and voice cutoff in scene-level runtime tests.
- **Established result:** Timing on this path depended on wait frames and per-line glyph display time, not serialized byte length. Unconsumed tail padding was removed and only missing display time was restored.
- **Transfer limit:** Measure wait structure, line layout, and the actual voice boundary separately for every scene.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1·§3.2, `references/strategy/translation-workflow.md` §4, `references/strategy/build-and-verify.md` §5.
