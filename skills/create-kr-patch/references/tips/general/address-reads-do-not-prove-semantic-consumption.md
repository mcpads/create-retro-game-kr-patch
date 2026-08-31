# Address reads do not prove semantic consumption

- **Search terms:** read breakpoint false positive, RAM reuse, decompressor back-reference, semantic consumption, wrong execution phase
- **Observed scope:** A read breakpoint on an added string address in a Saturn title.
- **Failure context:** The read was attributed to a choice renderer, but a later compressed asset reused the same physical RAM and its decompressor back-reference read that address.
- **Discriminating evidence:** The hit's instruction, call path, source, destination, and current buffer role were connected. It was a post-choice decompression copy and separate from the choice consumer.
- **Established result:** An address read did not prove that the bytes were read as text; RAM reuse produced a false semantic signal.
- **Transfer limit:** Treat a read breakpoint as consumption evidence only when execution phase, call path, buffer role, and decoded result are connected.
- **Related criteria:** `references/strategy/debugging.md` §2.2·§3·§4, `references/strategy/compression.md` §2·§3, `references/strategy/runtime-assets.md` §2.
