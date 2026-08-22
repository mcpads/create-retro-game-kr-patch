# Retained display slots define glyph co-residency across transitions

- **Search terms:** stale line buffer, glyph codebook transition, retained glyph set, retained tile code, dynamic font page
- **Observed scope:** Dynamic dialogue pages and dialogue-to-menu transitions in the Japanese NES release of Fire Emblem.
- **Failure context:** Individual pages and a static integrated image fit their glyph budgets, but the next record left prior line slots visible while selecting a new codebook, so retained tile codes changed meaning.
- **Evidence:** Writer and clear paths showed that record initialization retained prior line buffers. Requiring every glyph in the record to coexist was unnecessarily large; requiring only glyphs still present in retained slots fit. Runtime then exposed a separate loss of the completed page during the following menu state.
- **Established result:** The required working set and code assignment were defined by observed transitions, retained physical slots, dynamic insertions, and release timing, not by isolated page demand or an unconditional union of all records.
- **Transfer limit:** Enumerate writers, clears, visible transitions, inserted values, and codebook changes for the target. Re-derive which slots persist and require one compatible mapping only for their proven shared lifetime.
- **Related criteria:** `references/strategy/font-strategy.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.
