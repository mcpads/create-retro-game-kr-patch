# Graphics text

Choose discovery and image-editing methods for the current format and project. Use the criteria below to determine the target population, preservation conditions, real consumption, and completion. Read byte-level texture-container facts from the relevant platform document. Verify the connection between stored assets and runtime consumers through `references/strategy/runtime-assets.md`.

## 1. Trigger and population

Apply this strategy when a string in the distribution scope is stored as pixels in a graphics asset rather than rendered through a font, and those pixels are connected to a real screen consumer. Do not establish a separate graphics-text path when storage is unresolved or pixel storage cannot change the current decision.

When this strategy applies, define the denominator of assets, states, and variants to review. Classify every item as **resolved / excluded / unresolved**, using the meanings in `references/strategy/text-extraction.md` §1.4. Here, resolved means confirmed as a translation target; excluded means judged out of scope with evidence. Count selected, unselected, disabled, or other separately consumed variants as separate items. Complete coverage requires a decision for every item in the denominator.

Absence of a new write at display time does not prove that the asset is absent. It may have been preloaded; connect storage, load result, and screen consumer. If static and runtime inventories disagree, do not finalize the denominator until the difference is explained.

Use `references/conventions/project-records.md` §5 for the meanings and states recorded in this population.

## 2. Protected pixels and palette invariants

When neither a header nor a confirmed consumer defines the asset structure, determine pixel encoding, start boundary, address calculation, and segment boundaries together for the editable region. For a linear bitmap, determine bit depth, pixel order, start offset, row stride, width, and height. For tiled, planar, or swizzled data, determine the corresponding address rule. File size and a partially plausible image create candidates only. The adopted interpretation must explain the entire editable region and protect all remaining bytes; it need not decode an excluded region that will remain unchanged.

Before editing each asset, declare:

- Editable and protected pixel regions.
- Permitted palette indices or attributes and every known shared consumer.
- Container invariants such as size, alignment, tile or cell order, metadata, and compression.

A text-free background must be an approved reference against which protected regions can be compared. If it cannot be regenerated deterministically, freeze the accepted result and verify identity against it. The asset is incomplete when the boundary between source text and background is unresolved, or when a clean environment cannot reproduce and verify the result.

Before modification, establish an unchanged round trip under the equivalence criteria in `references/conventions/project-conventions.md` §5.1. When a format permits multiple encodings, include decoded pixels in the protected comparison. The modified artifact must preserve pixels outside the allowed region, palette indices or attributes, and all declared container invariants under the same criteria.

## 3. Consumer path

For every state and variant that shares meaning, connect stored asset, load result, and screen consumer. Include sharing and change impact when one asset feeds several screens or one screen composes several assets. An identical display result does not justify omitting the storage-to-load-to-selection link.

When a graphics change meets a trigger in `references/strategy/runtime-assets.md` §1, verify the links in `references/strategy/runtime-assets.md` §2 independently of visual review.

## 4. Completion

Mark the graphics-text scope complete only when every condition below holds:

- Every item in the declared denominator is resolved or excluded, with zero unresolved items.
- For assets not directly defined by a header or consumer, pixel encoding, address calculation, and boundaries explain the editable region; all uninterpreted regions remain unchanged.
- The build reproduces protected-pixel, palette, container, and unchanged-round-trip checks.
- Translated regions follow approved layout and visual criteria, remain readable without clipping against the real background and palette, and preserve every required state distinction.
- Every target state and variant is assigned to a confirmed consumer path.
- Static population coverage and runtime evidence establish each changed asset's storage → load → selection → display path under `references/strategy/runtime-assets.md` §2.
- Representative unchanged consumer paths preserve baseline behavior.

The scope remains **incomplete** while any denominator item, background or protected region, shared-asset path, or real consumer remains unresolved. If text is visible only through an external substitute or appears outside the file population, locate the missing storage or composition layer. Exclude an incomplete item from release eligibility or resolve its cause.
