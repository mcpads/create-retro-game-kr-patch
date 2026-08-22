# Evidence-backed case

## Zero-filled space is not proven free

- **Search terms:** false free space, zero-filled region, no static references, indirect call, first boot crash
- **Observed scope:** Candidate insertion regions in a Dreamcast label table and Saturn executable code.
- **Failure context:** A zero-filled Dreamcast range with no patch overlap and a Saturn function with no direct calls or value references were treated as unused. The first failed on a clean boot; the second was called indirectly during dungeon entry.
- **Decisive test:** The first invalid instruction exposed overwritten conversion code and constants. After they were restored and the connected tables were relocated with all references fixed, the title booted cleanly and gameplay proceeded. Saturn candidates were tested with isolated trap builds along the same play path; non-execution was recorded only for the observed path.
- **Established result:** Zero-filled data and lack of static references did not prove free space. Observed execution proved use, while non-execution in a limited run did not prove global non-use.
- **Transfer limit:** Any unobserved mode, path, or later section limits the corresponding code- or data-space claim.
- **Related criteria:** `references/strategy/reinsertion.md` §4·§5, `references/strategy/initial-survey.md` §2.5·§3, `references/strategy/debugging.md` §6, `references/conventions/project-conventions.md` §5.2.
