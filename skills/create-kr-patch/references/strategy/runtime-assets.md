# Runtime asset reachability

Determine whether a font, script, graphic, mapping table, or compressed block is used by connecting **storage → lookup → load or transform → residency → consumption**.

Choose asset formats, placement, loader implementations, and verification tools for the target project. Apply only the internal-validity criteria in §4 that correspond to changed stages. This document determines whether each stage's output becomes the next stage's input.

## 1. Trigger conditions

Apply the link assessment below when any of these conditions holds:

- The build adds a runtime asset that did not exist in the source.
- An asset grows beyond its original slot, file extent, bank, or sector, or moves elsewhere.
- Compression, packing, or identity metadata changes the loader's input or output.
- Residency changes, or the implementation adds a buffer, cache, DMA, or overlay path.
- Location and size remain fixed but the consumer must interpret a different encoding, cell layout, index rule, or format.

A separate link assessment is unnecessary for a same-size replacement only when existing evidence covers the same revision and consumer path and establishes identical links before and after the change. Evidence from another revision, loader, residency model, or narrower scope does not qualify.

## 2. Link assessment

`Storage → lookup → load or transform → residency → consumption` is a dependency model, not a required implementation sequence. Directly mapped assets may combine stages, and some assets have no transform. Exclude an inapplicable stage only with evidence. Reuse prior evidence only when it covers the same supported revision, asset identity, consumer path, and state lifetime, and the current change does not alter that link. One trace may establish several links.

Do not make runtime sample count equal file or item count. For a population enumerated through `references/strategy/initial-survey.md` §2.5, assess together only items that have static evidence for the same selection rule and link. A representative runtime sample proves that the shared link operates; static coverage must still establish which other items use it. Produce separate runtime evidence when links differ or static analysis cannot distinguish them. Add boundary items when size, format, metadata, or state transition can change consumption even within one link class.

At every changed boundary, determine:

1. Do the built asset's identity, location, and size refer to the same object as the runtime lookup metadata?
2. Does the real read path select that object and pass the verified load or transform result to the next memory boundary?
3. Does the delivered asset have the required capacity and lifetime, including after relevant state transitions, until consumption?
4. Does every required consumer read the asset with the same format, encoding, and index rules, and can the result be connected through RAM, VRAM, or final output?

Boot success, matching bytes inside an image, or one apparently correct screen does not establish the complete changed link. Limit every claim to the changed boundaries, consumer paths, and state transitions that can alter asset lifetime.

When the claim concerns load, upload, initialization, or cache refresh, state created after that boundary does not prove that the boundary was crossed. Save states remain usable when they begin before the boundary in the same build; otherwise start a new run and cross the boundary again.

## 3. Outcomes and next action

- **Pass** — Evidence connects every changed link and the asset remains valid across relevant state transitions. Return this result to the strategy that requested the assessment.
- **Fail** — Return to the strategy that owns the first broken link. Preserve evidence for preceding links and do not redesign unaffected layers.
- **Unresolved** — Record the last established boundary and the first unestablished boundary. If implementation depends on the answer, use `references/strategy/poc.md` to design a diagnostic that distinguishes that first missing link, then return the result to this assessment.

## 4. Criteria by changed component

| Question | Apply |
|---|---|
| Storage space, pointers, and hooks | `references/strategy/reinsertion.md` |
| Compression identification, decompression or recompression round trip, and transform result | `references/strategy/compression.md` |
| Glyph demand, encoding, and residency model | `references/strategy/font-strategy.md` |
| Restoration, layout, and re-encoding of graphics text | `references/strategy/graphics-text.md` |
| Risk that must be resolved before implementation | `references/strategy/poc.md` |
| Isolation of a broken link's cause | `references/strategy/debugging.md` |
| Image integrity, patch artifacts, and regression | `references/strategy/build-and-verify.md` |

Let the target project's implementation and documentation define concrete asset lists, file paths, manifest fields, and evidence-record formats when they are needed.
