# Manual layout decisions must precede faithful static previews

- **Search terms:** inferred dialogue layout, static preview approval, explicit page ranges, presentation evidence
- **Observed scope:** Dialogue translation review for the Japanese PlayStation release of Puyo Puyo Box.
- **Failure context:** Automatic wrapping and inferred line proportions produced plausible images before the window, page, line, and control placement had been established, risking approval of a layout that was not derived from the game.
- **Evidence:** The review path rejected inferred previews, kept wording selection separate, and required explicit text ranges in display order, tied to the chosen text, controls, and geometry, before static reproduction. Static previews, runtime evidence obtained through intervention, and evidence from normal play remained distinct.
- **Established result:** A static preview became faithful evidence only after layout was an explicit input; it did not itself decide layout, approve wording, or prove runtime consumption.
- **Transfer limit:** Use automatic layout when a complete deterministic consumer model establishes it. Otherwise require the target's actual geometry and the necessary human layout decision, and revalidate downstream evidence whenever text, controls, or geometry changes.
- **Related criteria:** `references/strategy/translation-workflow.md` §5.6, `references/strategy/build-and-verify.md` §5, `references/conventions/project-records.md` §7.2.
