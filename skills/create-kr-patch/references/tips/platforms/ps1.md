# PlayStation-specific cases

## Reloaded hooks mixed instruction-cache line states

- **Search terms:** R3000A I-cache, cache-line split, KSEG1 alias, self-modifying code, reloaded hook, mixed instructions
- **Observed scope:** A PlayStation hook executed after boot-time decompression reloaded its RAM, with the trampoline crossing an instruction-cache line boundary.
- **Failure context:** Reloading the RAM left adjacent cache lines in different states, so an original call instruction executed with a patched delay slot and corrupted a preserved register.
- **Evidence:** RAM contents, executed instructions, and register outcomes were compared for both cache lines. The trampoline was reduced to one line, the next original instruction remained in the delay slot, and the hook body ran through the uncached KSEG1 alias.
- **Established result:** Keeping the reloaded trampoline inside one cache line and executing the hook body uncached removed the mixture of pre-update and post-update instructions.
- **Transfer limit:** For another hook, inspect the reload range, cache-line boundaries, aliases, and execution order before choosing cache invalidation or an uncached path.
- **Related criteria:** `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §3, `references/platforms/ps1.md` §1, `references/conventions/project-conventions.md` §2.3.
