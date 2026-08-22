# Image header mismatch hid required runtime memory

- **Search terms:** PRG-RAM header mismatch, prior patch, unmapped execution, analysis copy, iNES declaration
- **Observed scope:** An analysis copy of a prior English patch for the NES release of Parodius Da!.
- **Failure context:** The prior patch stored and read expanded data in PRG-RAM while its image header declared no PRG-RAM. After normal progress, execution jumped to an unmapped value and departed from valid control flow.
- **Decisive test:** After tracing the first control-flow departure, only the PRG-RAM declaration in the analysis copy was corrected. The same play path then continued.
- **Established result:** The header correction was necessary for studying that prior-patch copy, not evidence that a patch built from the Japanese original should change its header.
- **Transfer limit:** Correcting the declaration isolates this cause only; it does not validate the prior patch as a whole or authorize changing the production patch input.
- **Related criteria:** `references/strategy/initial-survey.md` §2.1·§3·§4, `references/strategy/build-and-verify.md` §1·§2, `references/strategy/debugging.md` §2.2.
