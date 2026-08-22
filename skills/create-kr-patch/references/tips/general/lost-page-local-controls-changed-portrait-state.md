# Evidence-backed case

## Lost page-local controls changed portrait state

- **Search terms:** portrait control, page prefix, control-code count, expression order, missing token
- **Observed scope:** All translated entries and portrait-selection controls in the Game Gear release of Madou Monogatari 2.
- **Failure context:** Portrait controls disappeared during translation. Matching only the total control count could move the same value to another page or after visible text, changing expression timing.
- **Evidence:** Every source and translation page was checked for the same wait and output boundaries, and every original portrait control was confirmed before visible text. Value, order, duplication, and reset were restored per page, then compared against a control-free build and the actual handler state.
- **Established result:** Portrait changes were restored by matching control values and order in each page prefix, not by matching a whole-string count.
- **Transfer limit:** Use this correspondence only when page boundaries match and exhaustive evidence shows the controls live in page prefixes. Do not infer it across mid-page controls or changed page structure.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1·§3.3, `references/strategy/translation-workflow.md` §4, `references/conventions/translation-artifacts.md` §3.
