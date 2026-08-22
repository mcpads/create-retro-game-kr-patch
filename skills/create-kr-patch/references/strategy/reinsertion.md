# Reinsertion strategy

Reinsertion is not merely writing translated bytes. It must preserve the consumer boundaries and state conditions affected by changed length, address, or code. Length preservation, in-place growth, full relocation, and code hooks are candidates, not defaults.

## 1. Reinsertion policy

| Established condition | Available choice | Pass criteria |
|---|---|---|
| Slot width is the consumer boundary and the translation fits | Preserve length | Terminator, padding, tokens, and over-read |
| Every moved reference and following position-dependent structure can be updated | Grow in place | Reference completeness, alignment, size, and load |
| Every consumer can represent and reach a new location | Full relocation | Address representation, loader, buffer, and lifetime |
| A code hook is a feasible or preferred design after comparison with applicable data and lookup paths | Consider a code hook | Hook ABI, source effects, return, and installation prerequisites |
| No condition is established | Policy unresolved | Return to a question that can change the completion decision and seek evidence that distinguishes the viable policies |

Policies may differ by entry or region in one file. When entries share a bank, extent, buffer, or slot pool, size every entry in that pool before adopting the first policy; entries that individually fit can exhaust the pool together. Bind each policy to an established boundary model and stable key. Fail on overflow or unresolved entries. Apply the representation rules in `references/conventions/data-formats.md` §5.

### 1.1 Fixed slots

A fixed-slot policy must satisfy all of these conditions:

- Translation bytes and required tokens fit within the consumer's read extent.
- Actual boundary signals such as terminator, length field, next pointer, or fixed record width are preserved or recomputed.
- Padding value and position are not consumed as characters, control arguments, or another field.
- No multibyte character or control token is truncated automatically.

Overflow must fail the build and identify the established boundary and selected policy. Resolve it through an applicable reinsertion or presentation policy, or through a wording decision under `references/strategy/translation-workflow.md` §4.1 and §5; the current implementation does not make shortening the default. Do not set a global padding byte or a universal rule based on position before or after a terminator.

### 1.2 Growth and relocation

Before growing or moving text, establish all relevant structures, not just direct pointers:

- pointer storage, target address, base, width, endianness, and bank representation;
- references into strings, shared tails, and duplicate references;
- position-dependent values in following code, metadata, and assets;
- file, container, filesystem, and game-level location and size metadata; and
- load buffers, decompressed size, active memory, and consumption lifetime.

Growth or relocation fails for a scope if any required condition cannot be updated or preserved. If a representative risk can overturn the implementation and no equivalent evidence exists, verify length or relocation first through `references/strategy/poc.md`.

## 2. Reference completeness and coordinates

Use `references/strategy/text-extraction.md` §1.3 to decide when an approved catalog or structural parser becomes repeated-build specification and when heuristic search remains only an audit.

Each reference must distinguish at least:

- **Storage coordinate**: where the reference bytes reside.
- **Target coordinate**: the source structure identified by the value.
- **Representation**: width, endianness, base, bank or segment, and valid range.
- **Consumer**: the path that reads and interprets the value.

After relocation, calculate storage-coordinate and target-coordinate movement independently. Derive displacement, relative distance, and final address from placement output rather than copying source constants.

Do not relocate an interior-string reference by applying its source byte distance to translated text. Update it only when an explicit structural anchor survives translation. Otherwise preserve the containing structure or change policy; do not proceed unresolved.

When a move crosses a bank, segment, or pointer-width boundary, update every higher-level selector and consumer transition required to represent the new target. Updating a low offset alone is insufficient.

## 3. Relocation verification

Relocated output must be checked mechanically for all of these conditions:

- Every reference in the approved catalog resolves, with no unexpected reference form.
- Every new value fits its representation width, alignment, and valid address range.
- Every reference targets a declared structure boundary consumable by its reader.
- Unmoved values and protected regions do not change without justification.
- Re-extraction reproduces the intended translation and token structure.
- The actual loader and runtime consumer reach every grown or moved asset.

Do not auto-correct a failed check by selecting another pointer candidate or padding policy. Correct the structure model or leave the scope incomplete.

When one logical change writes several payloads, pointers, or hook sites, verify the complete write set atomically under `references/conventions/project-conventions.md` §5.2.

## 4. Code hooks

Before choosing code intervention, establish what applicable data, table, and lookup paths can meet and compare their impact, cost, and risk with a hook. A font or encoding change alone neither requires nor forbids a hook. A hook may be preferable when it preserves a human-approved product or design choice, but a material tradeoff in quality, scope, support, or technical investment follows the decision record in `references/conventions/project-records.md` §1.1.

A hook must specify and verify:

- entry live-ins, return live-outs, and intended new output;
- the effects of overwritten source instructions and every return path;
- instruction mode, branch range and delay behavior, stack, and calling convention;
- preservation or intentional modification of bank, segment, interrupt, and other entry state; and
- code paths that initialize, update, and release shared state.

Determine the required saved CPU state and interrupt handling from the effects of the overwritten instructions and the state that callers read after the hook returns.

When generating, replacing, or relocating executable machine code, or claiming reference completeness, apply the assemble-then-disassemble verification in `references/conventions/project-conventions.md` §2.3. Do not pass an unsupported instruction as arbitrary bytes or data.

Write a hook only after identifying the target revision and checking expected bytes plus instruction boundaries at the installation site. Derive branch displacement, literal addresses, and code or data ends from final placement.

Repeated fill or apparently unreachable space is not evidence of free space. Do not use it until direct and indirect entry points, reads, writes, copy-source use, and runtime generation have been excluded for the declared denominator.

## 5. Space and runtime reachability

An empty region, relocation gap, expanded medium, new file, or source-text storage no longer used after complete translation is only a candidate. Adoption requires proof that:

- no prior references or consumers remain, or all have moved;
- address decoding, mapper, filesystem, container, and game metadata represent the range;
- storage, decompression, load buffers, and transfers accept the grown asset;
- protected fields and intentional irregular structures remain intact where required; and
- the real runtime path reads the new location and retains it through consumption.

Translating one entry does not free all bytes in its range. Shared tails, duplicate pointers, interior entries, and inline literals can keep the range live. Reclaim only a range with established reference completeness. Do not reclaim a scope with unresolved population under `references/strategy/text-extraction.md` §1.4 or source text retained as an approved exception under `references/conventions/translation-artifacts.md` §5.

Growth of file or image size does not prove expansion of address space, buffers, or consumer paths. If a reinserted asset triggers `references/strategy/runtime-assets.md` §1, completion requires the link assessment in `references/strategy/runtime-assets.md` §2.

## 6. Consumer invariants

Apply only invariants present on the target path:

- **Character boundaries**: Look-ahead and branch consumers interpret new multibyte characters and control tokens consistently.
- **Entry boundaries**: Preserve whichever of terminator, length, fixed width, next pointer, or delimiter actually defines the consumer boundary.
- **Padding and alignment**: Write only established consumable positions and values; do not invade trailing tokens or following fields.
- **Layout and clearing**: Drawing and clearing extents match every expanded or reduced state without covering adjacent UI or graphics. No stale pixels or tiles remain after page or window transitions, exit, or re-entry.
- **Shared state**: Identify every writer and transition, and assign initialization, update, and release responsibility.
- **Encoding coverage**: An unmapped character fails the build; never omit or replace it silently. A development build follows `references/conventions/translation-artifacts.md` §5.
- **User strings**: If Hangul input is supported, apply `references/strategy/name-entry.md` to editing state, the committed record, every redisplay consumer, and persistence. An out-of-scope boundary must follow the human product-scope decision in `references/strategy/name-entry.md` §1.

If the presence of an invariant is unresolved, return to consumer investigation rather than treating it as passed.

## 7. Completion

Reinsertion is complete only when all of these hold:

- Every entry has an established policy under §1, with no overflow and no unresolved entry.
- Every changed reference passes §2, and relocated output passes every check in §3.
- A chosen code hook passes §4.
- Adopted space passes §5, and a change that triggers `references/strategy/runtime-assets.md` §1 passes the link assessment in `references/strategy/runtime-assets.md` §2.
- Every invariant present on the target path passes §6.
