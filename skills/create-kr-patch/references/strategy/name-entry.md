# Name entry and player-created text

Apply this strategy when the patch supports a player name or other user-created text. Treat input, editing, storage, redisplay, and persistence as one feature. If the human-selected product scope does not support Hangul input, declare and record that boundary explicitly rather than leaving source input partly functional.

## 1. Product contract and scope

Establish the supported input repertoire, maximum logical length, editing commands, completion behavior, and every in-scope consumer of the committed value. The agent establishes feasible repertoire, length, interface, redisplay, and persistence options with their cost and support effect; a human selects among alternatives that materially change supported names, product scope, or UX and records the choice under `references/conventions/project-records.md` §1.1. Distinguish the intended repertoire from the language's full character population; a finite supported set is valid only when it is declared, mechanically enforced, and adequate for that selected product scope.

Treat the complete path as the design boundary. Establish the links that can change the current encoding or glyph decision, and keep unresolved links visible while investigation and design iterate:

```text
candidate selection -> partial edit state -> committed record -> display providers -> save representation -> reload consumers
```

An input-screen PoC proves only the front of this path. A confirmed name in one dialogue proves neither persistence nor every later consumer.

## 2. Separate identities and surfaces

Do not assume that a keyboard cell, the editing field, the committed record, and later name displays share one code or glyph asset. For each surface, establish:

- the logical character or composition key selected by each active cell;
- the representation used by unfinished editing state;
- the canonical identity stored after confirmation;
- the glyph provider, cache, or composition path used by each redisplay consumer; and
- the representation written to and restored from persistent storage.

One logical character may require coordinated updates to several providers. Conversely, visually identical cells may be commands, inactive positions, or aliases rather than input characters. Disable unused input in both selection data and presentation; blank graphics alone do not remove an active selector.

Apply `references/strategy/runtime-assets.md` §2 separately to candidate graphics, editing-field glyphs, and post-confirmation consumers unless their supply and lifetime equivalence is established.

## 3. Composition and editing state

When input composes Hangul from jamo, define an explicit state machine for initial, medial, final, no-final completion, confirmation, and deletion. The target project chooses the user interface, but mechanically verify these conditions when applicable:

- Only a complete supported syllable can enter a committed slot.
- An unsupported combination remains rejected without silent approximation or loss of unrelated committed text.
- Confirmation rejects an unfinished syllable or other partial state.
- Deletion cancels unfinished stages in declared order before removing a committed character.
- Every active selector maps to one declared action, and every supported composition has an accepted path.
- Inactive cells, out-of-order inputs, excess length, and invalid commands fail without corrupting the record.

Unsupported combinations are part of the contract only within a declared input domain. Define the input alphabet, reachable editing states, and actions whose rejection behavior is covered before claiming exhaustive rejection coverage. Do not claim full modern Hangul input from successful samples within a smaller set.

## 4. Committed records and persistence

Derive record width, termination, slot identity, packing, validation, and legacy discrimination from actual readers and save consumers. Preserving an original fixed width can reduce downstream change, but it is not a requirement and does not justify ambiguous packing.

A new record format must validate every structural field before any consumer treats it as committed text. Check applicable markers, ordering, terminator position, padding, occupied and empty values, rank or index bounds, and unused bits. Reject malformed or ambiguous records rather than interpreting them as another format by accident.

Use one canonical character identity across serialization, editing-field redisplay, dialogue insertion, menus, status, battle, ending, and save or load paths. If a consumer requires another representation, define and verify the conversion boundary. Determine whether existing saves remain supported, require migration, or are deliberately incompatible; do not infer compatibility from equal record size.

## 5. Glyph supply and exact composition

Apply `references/strategy/font-strategy.md` §2.2 and §3 to the complete allowed input repertoire, not only names present in the translated corpus. A runtime compositor may reduce stored glyph data, but it adds membership, mapping, reconstruction, cache, clearing, and lifetime conditions.

Composition need not expose a visibly compositional font. When it represents a selected finished font asset, define output equivalence against that asset and adopt the representation only when the complete supported set meets the declared pixel or visual equivalence and fits the measured code, data, and runtime budgets.

Verify a serialized composition pack with a decoder that reads the emitted representation rather than reusing the builder's internal objects. When generated machine code performs selection, serialization, or composition, execute it over the complete supported set and applicable invalid set under `references/conventions/project-conventions.md` §2.3. Builder agreement, a host-language model, or one visible name does not prove the emitted program.

## 6. Static, runtime, and human evidence

Use product build or artifact verification checks for finite, mechanically decidable populations:

- active selector and command coverage;
- accepted composition paths and rejected combinations;
- length boundaries and partial-state behavior;
- record round trips for every slot position and packed-field boundary;
- malformed-record rejection;
- glyph reconstruction and mapping for the complete supported set; and
- generated-code execution, bounds, and no-write behavior for rejected input.

Runtime evidence connects the exact integrated product artifact through representative interaction and persistence. Exercise candidate selection, applicable editing commands, confirmation, immediate redisplay, at least one dynamic insertion, and each distinct consumer class. When persistence is supported, distinguish:

- redisplay in the same uninterrupted session;
- explicit save followed by the target's native reset or power-cycle behavior; and
- reload in a fresh process, device session, or equivalent environment that reopens persistent storage.

Evidence from one level does not establish the next. Record launcher behavior, save-directory replacement, state injection, menu unlocks, or other interventions through `references/conventions/project-records.md` §1. An intervention can prove downstream record consumption without proving natural reachability.

Mechanical coverage does not approve candidate arrangement, editing labels, glyph readability, or visual quality. Preserve human presentation approval separately from runtime and serialization results.

## 7. Completion

Name entry is complete for the declared distribution scope only when:

1. Every supported input has an accepted editing and serialization path, and unsupported or malformed input fails as declared.
2. Candidate, editing, committed-record, and redisplay identities agree across every distinct product consumer.
3. Glyph supply and cache lifetime remain valid through the state transitions in which the value stays visible.
4. Save and reload behavior passes at the strongest persistence boundary claimed by the release.
5. The exact integrated product artifact passes representative interaction, transition, and unchanged-path regressions.
6. Required human approval of arrangement, labels, readability, and presentation is complete.

Keep narrower results explicit, such as mechanical-coverage-complete, representative-runtime-verified, persistence-pending, consumer-population-pending, or human-review-pending. Do not collapse them into name-entry support.
