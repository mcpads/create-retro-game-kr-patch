# Compression strategy

Apply these trigger conditions and verification criteria when modifying compressed assets. Establish the byte-level format and implementation from the target platform and project.

## 1. Trigger and denominator

Use this strategy when the target loader or consumer transforms stored input into another byte stream and that output is linked to actual consumption. Do not establish a separate compression path when the transform boundary is unresolved or compression does not affect the current decision.

When this strategy applies, declare the supported denominator under `references/conventions/project-conventions.md` §5.1. Preserve unsupported variants unchanged or reject them explicitly.

## 2. Consumer format interpretation

Establish the adopted format interpretation from the target consumer's read semantics or independent equivalent evidence. An algorithm name or a sibling game's implementation may narrow candidates, but verify at least these boundaries on target input:

- input extent and termination;
- literal and match interpretation, including byte and bit order;
- valid output references and overlapping-copy semantics;
- output size, alignment, buffer, and destination limits; and
- the consumer and protected range of each container field.

Do not invent values for fields whose consumption is unresolved. Preserve the source value or generate it from a public specification. Exclude the variant from supported scope if neither choice is justified.

## 3. Decompression verification

A decompressor must:

- process every source stream in the declared denominator without out-of-bounds access;
- match output produced by the target consumer or an independent oracle;
- retain the same meaning for supported rare modes and boundary conditions; and
- reject unsupported variants, truncated input, and impossible references.

One plausible screen or the existence of an external implementation does not establish the interpretation. Reverify an adopted external implementation against the same variant and target samples.

## 4. Recompression verification

Keep these three criteria distinct:

| Criterion | Meaning | Requirement |
|---|---|---|
| A. Self round trip | The project's decompressor restores the compressor input | Required for the declared compressed population |
| B. Source-byte reproduction | Recompressing source-decompressed data reproduces the source stream | Required only when the format demands one canonical representation |
| C. Target-consumer compatibility | The target consumer decompresses and uses the new stream as intended | Required for distribution |

A proves agreement between the project's own implementations only; it does not prove C. Before using recompression in distribution:

- verify A across the declared denominator;
- enforce the target consumer's reference range, output limit, and termination invariants on compressor output;
- compare the expected decompressed bytes with output from the target consumer or the independent evidence established in §2; and
- treat post-decompression load or display as supporting evidence for consumption, not as a replacement for output correctness.

### 4.1 Unchanged control for observed defects

When a recompressed asset fails and codec behavior must be separated from content changes, recompress unchanged source-decompressed bytes with the same compressor and feed them through the same consumer path. This applies the change isolation in `references/strategy/debugging.md` §2.2 and must satisfy its isolation conditions.

- Failure of the unchanged recompression keeps a semantic mismatch between compressor and target decompressor as a cause candidate.
- Success of the unchanged recompression with failure only after editing moves attention to edited boundaries, output limits, placement, and downstream consumption.

Self round-trip success does not remove the codec layer from consideration. Do not require this control when codec and content are already distinguished.

## 5. Size, repacking, and alternatives

If recompressed output exceeds its allocation, compare options against actual output and consumer boundaries rather than estimated compression ratio:

- Can the same format interpretation produce a smaller valid stream?
- Can a smaller edit still meet the localization requirement?
- Can every address, metadata field, loader, and buffer represent and consume a relocated extent?
- Can container reserialization preserve untouched data and protected metadata?
- Does the target consumer provide a verified uncompressed or alternate path?

Bypassing compression introduces new code, storage, load, residency, and consumption conditions. Verify them; do not select a bypass merely because it appears simpler. If the asset change triggers `references/strategy/runtime-assets.md` §1, verify the links in `references/strategy/runtime-assets.md` §2 as well.

## 6. Completion

Compression work is complete only when all applicable conditions hold:

- The target consumer established the format variant and boundaries.
- Every source stream in the declared denominator decompresses correctly.
- Every recompressed item passes A.
- A canonical format, if required, passes B.
- Recompressed output satisfies target invariants and output limits and passes C.
- If codec and content competed as explanations for a defect, an unchanged control distinguished them.
- A runtime-asset change triggered under `references/strategy/runtime-assets.md` §1 passes the link assessment in `references/strategy/runtime-assets.md` §2.
- Unsupported variants and unresolved fields are preserved or explicitly rejected.

Self round trip, successful boot, or one displayed screen alone does not prove completion.
