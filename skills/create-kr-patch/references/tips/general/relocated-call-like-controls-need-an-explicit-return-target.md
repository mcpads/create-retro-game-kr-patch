# Relocated call-like controls need an explicit return target

- **Search terms:** call-like text control, return address, relocated continuation, physical successor, resume target
- **Observed scope:** Text continuations using call and return controls in the Japanese Sega Saturn release of Waku Waku Puyo Puyo Dungeon.
- **Failure context:** Relocating a continuation preserved its terminal control bytes but changed the physical byte immediately after the call-like control, so return resumed at the wrong content.
- **Decisive test:** Consumer analysis showed that the control saved the address following the token before jumping to a shared block. The relocated path reconstructed that return target explicitly, and a source entry from the game verified the return path rather than only terminal-byte equality.
- **Established result:** Control-token preservation was insufficient because physical placement participated in control flow; relocation had to preserve or explicitly reconstruct the original return target.
- **Transfer limit:** Re-derive call depth, pushed address, target base, return operation, physical adjacency, and nested continuation behavior. Do not treat every branch-like token as a call or reuse the observed control values.
- **Related criteria:** `references/strategy/text-extraction.md` §4.4, `references/strategy/reinsertion.md` §1.2·§3, `references/strategy/build-and-verify.md` §5.
