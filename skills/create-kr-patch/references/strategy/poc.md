# Proof of concept

Use a PoC to resolve uncertainty that can change distribution feasibility before dependent implementation. Its timing and scope follow the current evidence and dependencies rather than a universal order. Reuse evidence from the same revision and conditions only when it tests the same condition under the same prerequisites and supports the same claim.

## 1. Role and entry conditions

Run a PoC when the unresolved condition is completion-critical and postponing it would cause substantial rework. Before execution, state:

- the assumption and risk;
- pass, fail, and unresolved outcomes; and
- the implementation choices available after each outcome.

If no outcome reduces those choices, split out a narrower diagnostic. Do not narrow the original claim merely to obtain an easy success.

## 2. Choosing what the PoC must establish

| Scope | Trigger | Question |
|---|---|---|
| Visibility | No equivalent runtime evidence exists for the target revision and renderer | Can intended glyph pixels reach the screen through the actual path? |
| Representative end-to-end path | No evidence connects extraction, transformation, reinsertion, and consumption for a representative unit, and scaling first would create large rework | Does one representative unit survive the complete path? |
| Conditional | A specific unresolved risk can change the design and cannot be passed or rejected using static evidence | Does the target condition hold under its real constraints? |

These scopes are independent. A visibility PoC establishes that the intended pixels reach the screen through a declared data path. A representative end-to-end PoC establishes the complete path for one declared unit. Encoding budgets, relocation, compression, and other consumers need separate criteria when they can still change the design.

Reuse evidence only when revision, renderer, consumer, preconditions, and supported claim match, and the current change does not alter identity, links, or consumption. Otherwise establish equivalence or rerun the relevant test.

## 3. Visibility verification

Choose a representative primary renderer, not merely the earliest reachable screen. Test separate consumers when their equivalence is unresolved. A composited screenshot, external subtitle, or overlay does not prove in-game consumption.

Visibility passes only when all of these hold:

- the intended glyph appears at the intended position and shape;
- target storage, load, selection, and display are connected;
- nearby UI and entry or exit behavior remain intact; and
- the record distinguishes what the test proved from what it did not prove.

Choose a glyph source that preserves the visibility question without adding unrelated letterform uncertainty. Apply the source, authoring, and transform boundaries in `references/strategy/font-strategy.md` §4. A temporary or candidate glyph proves the declared path, not release-font completion.

## 4. Representative end-to-end text path

Choose a unit that connects the complete extraction-to-consumption boundary and exercises the applicable constraint that is hardest to satisfy: length, control tokens, pointers, compression, padding, or another boundary whose failure would invalidate scale-up. A short string that bypasses that condition is not representative. If the decisive constraint is still unresolved, establish it before claiming a representative unit, or state the narrower claim supported by the result. This governs representativeness; it does not impose a universal investigation order outside the PoC claim.

Use separate units for consumers or risks that do not share the same path. Verify:

- unchanged round trip or the declared semantic-equivalence rule;
- character and control-token preservation or recalculation policies, and glyph mapping;
- reinsertion length, boundaries, references, and container structure;
- actual load and consumption; and
- displayed result and affected regression paths.

When adopting a successful PoC result, encode any adopted product rules and required checks in the primary path, and keep the supporting evidence linked through `references/conventions/project-records.md` §4. Decide separately under `references/conventions/project-conventions.md` §1 whether the producing procedure belongs in the build; adopting the result does not make the temporary artifact a build input. A temporary code mapping supports only the representative claim, not collision freedom across the distribution. Apply `references/strategy/font-strategy.md` §2.1 to the distribution mapping decision.

One representative unit does not prove total volume. An unresolved population does not invalidate the unit; use `references/strategy/text-extraction.md` §1.5 to decide when enumeration must precede scaling.

## 5. Conditional verification

Run a conditional PoC only for a design-changing risk without equivalent static evidence.

| Risk | Trigger | Pass criteria |
|---|---|---|
| Separate consumers | Target screens may use different glyph, texture, or render paths | Every distribution screen is assigned to an established consumer path and its constraints |
| Encoding or control collision | New code space or width may collide with parser or control behavior | The target corpus decodes without ambiguity and does not invade non-text or control paths |
| Stored or active capacity | Stored glyph, texture, RAM, or VRAM supply is near required demand | Declared distribution demand fits supply and remains valid for the required asset lifetime |
| Growth or relocation | Translation can move boundaries, references, alignment, or following data | The representative change preserves every applicable reference and boundary through load and consumption |
| Compression or container | Edited data is packed and may change size or representation | Unchanged equivalence and modified container validity both hold, and the target consumer accepts the result |
| Graphics text | Distribution text is stored as graphics pixels | The representative path passes `references/strategy/graphics-text.md` §4 |
| Presentation or interaction | Windows, states, pages, input, audio, or event synchronization can change implementation | The representative path passes the applicable criteria in `references/strategy/build-and-verify.md` §5 within the declared scope of the PoC |
| User strings | Player-created text is stored and consumed again | Input repertoire, storage representation, redisplay, and length conditions work together within the distribution scope |

Do not turn every final-QA item into a PoC. Select only a representative condition that can change implementation.

When a runtime asset change triggers `references/strategy/runtime-assets.md` §1, include unresolved links from `references/strategy/runtime-assets.md` §2 in the pass criteria.

## 6. Outcomes and integration

- **Pass** applies only to the claim defined for the PoC.
- **Fail** blocks dependent implementation until the assumption or design changes.
- **Unresolved** is not a pass. Isolate the first unsupported boundary, then return to the original condition.

Record risk, representativeness, predefined criteria, evidence, supported and unsupported claims, rejected choices, and the next action under `references/conventions/project-records.md` §4. If a test is skipped, record the equivalent evidence.

The project may name intermediate states differently, but preserve the distinction among a local result, its adoption into the cumulative build, and the completion claim it supports. A local pass may justify another investigation before integration when that evidence is more useful; record that it has not yet been integrated and keep the remaining conditions explicit rather than treating it as project success.

When a successful PoC is adopted, reproduce its rules through the primary build from immutable source and combine them with every accepted change. Partial translation inputs follow `references/conventions/translation-artifacts.md` §5. Component success becomes project success only after the primary build passes `references/strategy/build-and-verify.md` §1.
