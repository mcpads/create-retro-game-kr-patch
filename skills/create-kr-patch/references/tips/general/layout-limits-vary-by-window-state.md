# Layout limits vary by window state

- **Search terms:** dialogue width, window tag, page break, narrow window, line reflow, portrait state
- **Observed scope:** A narrow dialogue state and a page-transition control in the Game Gear release of Madou Monogatari 2.
- **Failure context:** Assuming one wide window for a script region missed a narrower state in the same region, while a width-only checker also rejected text that could be reflowed or moved to the next page.
- **Evidence:** Source pages were compared with the active window geometry and the overflow was reproduced. Width and row usage were checked after reflow, and continuous play confirmed that the control cleared the window, opened the next page, and preserved the first character.
- **Established result:** The active window tag, not the containing script region, determined capacity. Width and row count had to be evaluated together, with confirmed page transitions available for text that could not fit.
- **Transfer limit:** Before adding a page, verify that the control preserves portrait, window, input, and event state on that path.
- **Related criteria:** `references/strategy/text-extraction.md` §4.4, `references/strategy/translation-workflow.md` §4, `references/strategy/build-and-verify.md` §5, `references/strategy/reinsertion.md` §6.
