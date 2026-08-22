# Evidence-backed case

## Selection highlighting depended on data and consumer range

- **Search terms:** selection highlight too short, source-length read, highlight asset, static proof only, selected state
- **Observed scope:** A translated selection row longer than the source-language highlight range.
- **Failure context:** The Korean row grew, but selection highlighting still covered only the original prefix. Expanding highlight data alone did not change the consumer's source-length read.
- **Evidence:** Data-only expansion had no effect, and static analysis tied the read range to the original length. Both ranges were adjusted, but selected and unselected runtime transitions were not yet observed.
- **Established result:** Static evidence established that both highlight data and its read range had to cover the full translated row.
- **Transfer limit:** Do not mark the screen complete until runtime evidence shows every row changing state through its final cell.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.
