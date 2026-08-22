# Evidence-backed case

## Cleanup behavior may be caller-specific

- **Search terms:** stale tiles, missing clear, caller-specific cleanup, bottom-aligned text, battle message residue
- **Observed scope:** A Game Gear battle window shared by a bottom-aligned critical-hit message and the preceding spell name.
- **Failure context:** After Korean alignment moved the standard message row, one critical-message caller failed to clear the window and left part of the previous spell name. Clearing all dialogue or changing the shared clear routine did not match the caller-local omission.
- **Decisive test:** Stale tiles were observed at the failure point and compared with normal messages drawn after a clear. Callers lacking a clear were enumerated, and only the failing caller was redirected through an existing clear-capable path.
- **Established result:** The residue came from caller-specific cleanup responsibility, not a defect in the shared clearing logic.
- **Transfer limit:** Before redirecting a path, verify each caller's prior clear, coordinates, alignment, and semantic role, then regress the unaffected callers too.
- **Related criteria:** `references/strategy/debugging.md` §3·§5, `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2.
