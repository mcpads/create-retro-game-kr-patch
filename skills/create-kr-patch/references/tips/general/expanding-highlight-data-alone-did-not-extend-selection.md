# Expanding highlight data alone did not extend selection

- **Search terms:** selection highlight too short, source-length read, highlight asset, static proof only, selected state
- **Observed scope:** A translated SNES selection row longer than the source-language highlight range.
- **Failure context:** The Korean row grew, but selection highlighting still covered only the original prefix. Expanding highlight data alone did not change the consumer's source-length read.
- **Evidence:** Data-only expansion had no effect, and static analysis tied the read range to the original length. Both ranges were adjusted, but selected and unselected runtime transitions were not yet observed.
- **Established result:** The highlight asset was not the only limit. Static evidence tied the highlighted extent to the consumer's source-length read, so both had to cover the translated row. The screen itself remains unproven because no runtime state transition was observed.
- **Transfer limit:** Re-derive both the highlight asset extent and the consumer's read range for every other row and screen. Static agreement between them does not establish the runtime selected-state transition.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.
