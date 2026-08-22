# MPR state resolved HuC6280 bank identity

- **Search terms:** HuC6280, MPR mapping, System Card BIOS, immediate X value, logical address, bank misidentification
- **Observed scope:** A PC Engine CD text handler that passed an address and an immediate X value into a BIOS call.
- **Failure context:** Similar X constants in several handlers looked like lower-bank selectors. A HuC6280 logical address alone could not identify the actual callee without the current MPR mapping.
- **Evidence:** Tracing the output routine together with MPR state showed no internal MPR change and resolved the callee to the System Card BIOS area currently mapped there. The X value was overwritten immediately after the call and did not propagate into later bank selection.
- **Established result:** The X constant was a BIOS task-scheduler argument, not a lower-bank or subscript identifier.
- **Transfer limit:** Trace MPR state and the actual consumer separately for every other entry point and indirect path.
- **Related criteria:** `references/strategy/initial-survey.md` §2.2·§3, `references/strategy/debugging.md` §2.2·§4, `references/platforms/pce.md` §1.
