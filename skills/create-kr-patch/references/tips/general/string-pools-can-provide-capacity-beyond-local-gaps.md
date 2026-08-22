# Evidence-backed case

## String pools can provide capacity beyond local gaps

- **Search terms:** pooled string region, long credits, NUL gaps, pointer table, relocation capacity, empty-entry sentinel
- **Observed scope:** Ending credits and a word pointer table containing empty-entry values in PC-98 titles.
- **Failure context:** Treating every NUL gap as an independent fixed slot could not fit longer Korean credits, while the consumer actually entered each string through the pointer table.
- **Evidence:** Every valid pointer target and update site was linked. Strings were repacked inside the established region, pointers were updated, overlay size and following code were preserved, and display plus next-entry progress were verified.
- **Established result:** The whole region, rather than each original gap, could provide capacity because its complete reference model preserved independent entry points.
- **Transfer limit:** Use pooled capacity only after establishing every entry pointer, empty sentinel, pointer width, and following structure boundary.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3·§5, `references/strategy/build-and-verify.md` §3·§4.
