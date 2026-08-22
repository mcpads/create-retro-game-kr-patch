# Original-coordinate planning prevented multi-insertion drift

- **Search terms:** multiple growing regions, original-coordinate plan, reverse-order insertion, pointer-site shift, pointer-target shift
- **Observed scope:** Multiple expanded data ranges followed by pointers, directories, and structure addresses in PC-98 game files.
- **Failure context:** Changes safe in isolation could miss or duplicate corrections when later edits used already-shifted positions, or when pointer storage sites and pointer targets received the same accumulated delta.
- **Evidence:** Every change was planned in original coordinates and growing ranges were applied in descending original-offset order. Storage-site and target deltas were calculated separately, and following structures were assigned their final positions once. Static and runtime checks then covered the combined artifact.
- **Established result:** Original-coordinate planning, reverse application, and separate site-versus-target shifts moved each position-dependent structure exactly once.
- **Transfer limit:** Use reverse application only for an established set of original-coordinate variable ranges and following structures. Re-enumerate references, interior entry points, structure addresses, fixed constants, and load capacity on new input.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3, `references/strategy/build-and-verify.md` §3·§4, `references/conventions/project-conventions.md` §5.2.
