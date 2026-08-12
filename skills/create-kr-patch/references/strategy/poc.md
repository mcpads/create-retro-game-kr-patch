# Proof of concept

Use a PoC to resolve uncertainty that can change distribution feasibility before dependent implementation. Prioritize a condition whose failure would block completion or force redesign. Reuse equivalent evidence from the same revision and conditions. Compare cost only among tests that preserve the same condition, prerequisites, and proof scope.

## 1. Role and entry conditions

Run a PoC when the unresolved condition is completion-critical and postponing it would cause substantial rework. Before execution, state:

- the assumption and risk;
- pass, fail, and unresolved outcomes; and
- the implementation choices available after each outcome.

If no outcome reduces those choices, split out a narrower diagnostic. Do not shrink the original proof scope merely to obtain an easy success.

## 2. Choosing the proof scope

| Scope | Trigger | Question |
|---|---|---|
| Visibility | No equivalent runtime proof exists for the target revision and renderer | Can intended glyph pixels reach the screen through the actual path? |
| Representative end to end | No evidence connects extraction, transformation, reinsertion, and consumption for a representative unit, and scaling first would create large rework | Does one representative unit survive the complete path? |
| Conditional | A specific unresolved risk can change the design and has no static pass or rejection | Does the target condition hold under its real constraints? |

These scopes are independent. Visibility proves pixels through a declared data path. Representative end to end proves one declared unit. Encoding budgets, relocation, compression, and other consumers need separate criteria when they can still change the design.

Reuse evidence only when revision, renderer, consumer, preconditions, and proof scope match, and the current change does not alter identity, links, or consumption. Otherwise prove equivalence or rerun the relevant test.

## 3. Visibility verification

Choose a representative primary renderer, not merely the earliest reachable screen. Test separate consumers when their equivalence is unresolved. A composited screenshot, external subtitle, or overlay does not prove in-game consumption.

Visibility passes only when:

- the intended glyph appears at the intended position and shape;
- target storage, load, selection, and display are connected;
- nearby UI and entry or exit behavior remain intact; and
- the record distinguishes what the test proved from what it did not prove.

Begin with an established font unless letterform design is the uncertainty under test. Create or edit glyphs only for local missing symbols or verified UX requirements. A temporary glyph proves the path, not release-font completion. Apply `references/strategy/font-strategy.md` §4 to the release-font decision.

## 4. Representative text end to end

Choose a unit that connects the complete extraction-to-consumption boundary and includes the hardest applicable established constraint: length, control tokens, pointers, compression, padding, or another design-critical boundary. A short string that bypasses the hard condition is not representative. Identify the hardest constraint as the one nearest its established limit or without a workaround, not the one easiest to sample. If that is unresolved, establish it before choosing the unit.

Use separate units for consumers or risks that do not share the same path. Verify:

- unchanged round trip or the declared semantic-equivalence rule;
- character and control-token preservation or recalculation policies, and glyph mapping;
- reinsertion length, boundaries, references, and container structure;
- actual load and consumption; and
- displayed result plus affected regression paths.

Promote reproducible rules, evidence, and checks into the primary path, not the temporary artifact.

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
| Presentation or interaction | Windows, states, pages, input, audio, or event synchronization can change implementation | The representative path passes the applicable criteria in `references/strategy/build-and-verify.md` §5 within its declared proof scope |
| User strings | Player-created text is stored and consumed again | Input repertoire, storage representation, redisplay, and length conditions work together in distribution scope |

Do not turn every final-QA item into a PoC. Select only a representative condition that can change implementation.

When a runtime asset change triggers `references/strategy/runtime-assets.md` §1, include unresolved links from `references/strategy/runtime-assets.md` §2 in the pass criteria.

Do not run a separate conditional test when the risk is absent or equivalent static evidence already decides it.

## 6. Outcomes and integration

- **Pass** applies only to the declared scope.
- **Fail** blocks dependent implementation until the assumption or design changes.
- **Unresolved** is not pass. Split the first unproved boundary, then return to the original condition.

Record risk, representativeness, prior criteria, evidence, proved and unproved claims, rejected choices, and next action under `references/conventions/project-records.md` §4. If a test is skipped, record the equivalent evidence.

Adopt a successful PoC into the primary build from immutable source and combine it with every accepted change. Partial translation inputs follow `references/conventions/translation-artifacts.md` §5, but components must not remain isolated. Component success becomes project success only after the primary build passes `references/strategy/build-and-verify.md` §1.
