# Rare paths may depend on table-tail entries

- **Search terms:** one branch corrupt, missing sentinel pointer, table tail, off-by-one address, pointer coverage
- **Observed scope:** A branch-specific SNES text failure.
- **Failure context:** The build omitted a special pointer at the end of a table and started the first text byte one byte early, overwriting that pointer.
- **Decisive test:** The failing branch's actual load path was disassembled and compared with the source constants, pointer count, and first text address.
- **Established result:** Restoring the complete fixed table and correcting the first text address repaired the branch.
- **Transfer limit:** Do not assume that story branch count equals consumer-path count.
- **Related criteria:** `references/strategy/build-and-verify.md` §4, `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §3, `references/strategy/initial-survey.md` §3.1, `references/conventions/data-formats.md` §4.
