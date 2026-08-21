---
name: create-kr-patch
description: >-
  Use for Korean (Hangul) fan translations of retro console or PC games,
  including ROM or disc analysis, text-engine reverse engineering, Hangul fonts
  and custom encodings, script extraction and reinsertion, code hooks, patch
  builds, and emulator verification. Apply it to both new investigations and
  follow-up work in existing Korean-patch projects. 레트로 게임 한글화·한글패치·한글
  패치·ROM 번역의 신규 조사와 기존 프로젝트 후속 작업에 사용한다.
---

# Create a Korean patch for a retro game

## Purpose

Base decisions on evidence from the target game. Keep the evidence and adopted results from the initial survey, fonts and encoding, PoC, extraction, translation, reinsertion, builds, distributable patches, and runtime verification traceable through completion.

Choose tools, languages, libraries, and fonts based on the target project's existing structure and the current environment. Regardless of those choices, preserve the required capabilities and verification criteria. Look up basic specifications from current primary sources when one straightforward search can recover them.

This methodology began with text-heavy games whose source language was Japanese. Treat observed frequencies and prior structures as hypotheses until the target revision confirms them.

## Routing

For an existing repository, reconstruct the current code, documents, artifacts, and verification state before choosing the active judgment area. Start with the initial survey when the game or its structure is not yet understood.

| Judgment area | Document | Use it to determine |
|---|---|---|
| Initial survey | `references/strategy/initial-survey.md` | Completion-critical conditions, real dependency boundaries, initial volume, unresolved populations, and revision-specific facts |
| Fonts and encoding | `references/strategy/font-strategy.md` | Code-to-glyph mapping, total repertoire, active working set, representation, and runtime reachability |
| Name entry and user strings | `references/strategy/name-entry.md` | Input repertoire, editing state, committed records, glyph supply, redisplay consumers, and persistence |
| Text extraction | `references/strategy/text-extraction.md` | Population and volume, consumer-defined boundaries and tokens, reversible artifacts, and round trips |
| PoC | `references/strategy/poc.md` | Whether a PoC is needed and what a visibility proof, representative end-to-end path, or conditional proof must establish |
| Reinsertion and hooks | `references/strategy/reinsertion.md` | Boundary policies, reference completeness, hooks, space, and consumer invariants |
| Translation | `references/strategy/translation-workflow.md` | Translation work and agent assignment, context, approved terminology and voice, protected information and consumer constraints, and high-risk meaning |
| Build and verification | `references/strategy/build-and-verify.md` | Reproducible artifacts, build-owned gates, distribution boundaries, integrity and runtime verification, text and interaction QA, and release readiness |
| Debugging and issue handling | `references/strategy/debugging.md` | Gameplay routes, target-state access, proof scope of state intervention, causes, fixes, and regression evidence |
| Graphics text, cross-cutting | `references/strategy/graphics-text.md` | Pixel-text population, protected visual assets, and consumer-path verification |
| Compression, cross-cutting | `references/strategy/compression.md` | Actual transform boundaries, consumer compatibility, and repacking verification |
| Runtime asset reachability, cross-cutting | `references/strategy/runtime-assets.md` | Storage, lookup, load or transform, residency, and consumption as one connected claim |

Apply the relevant conventions when designing or validating artifacts, interchange data, or records. Preserve an existing repository's equivalent structure when it already carries the same meanings.

| Scope | Document | Use it for |
|---|---|---|
| Project implementation, cross-cutting | `references/conventions/project-conventions.md` | Build and test ownership, machine-code verification, round-trip equivalence and denominator, final-write verification, external-component reproduction, and source assets |
| Translation artifacts | `references/conventions/translation-artifacts.md` | Source preservation, control tokens, review states, and build-input eligibility |
| Project records | `references/conventions/project-records.md` | Human strategic decisions, survey and PoC decisions, graphics-text catalog, HITL observations, QA evidence, and issue states |
| Analysis and build data | `references/conventions/data-formats.md` | Character maps, controls, pointers, translation links, reinsertion policies, and font render profile meanings |

Read a platform document only when a constraint involving hardware, the medium, address space, or rendering can change the current decision.

| Platform | Document |
|---|---|
| SNES | `references/platforms/snes.md` |
| Mega Drive | `references/platforms/megadrive.md` |
| Sega Saturn | `references/platforms/saturn.md` |
| PlayStation | `references/platforms/ps1.md` |
| Dreamcast | `references/platforms/dreamcast.md` |
| PC Engine and CD-ROM² | `references/platforms/pce.md` |
| PC-98 | `references/platforms/pc98.md` |
| Game Gear | `references/platforms/gg.md` |
| Game Boy and Game Boy Color | `references/platforms/gb.md` |
| NES and Famicom | `references/platforms/nes.md` |
| Nintendo DS | `references/platforms/nds.md` |

For an unlisted platform, establish only the constraints that can change the current decision.

When a reproduced symptom or judgment area may match prior evidence, search `references/tips/README.md` by symptom, structure, or technical term and read only the relevant cases. Re-establish a selected case's `Transfer limit` in the current target. Determine completion from its `Related criteria`, never from resemblance to the case. Absence of a matching case does not delay evidence available from the target itself.

## Choosing the next boundary

These are decision heuristics, not stages. Start from the current product scope and intended claims; when they are not defined enough to choose work, survey feasible options and prepare the material differences for human decision. Choose the next investigation or implementation by expected decision value, dependencies, cost, and reversibility. A completion-blocking or redesign risk often deserves early evidence, but no fixed ordering replaces the current evidence. Call one experiment a cheaper equivalent only when it preserves the same condition, prerequisites, and proof scope.

- Keep independent evidence baselines distinct and investigate them in parallel when useful. When new evidence overturns a decision, reassess only the claims and adopted work that depend on it.
- Enumerate a finite population by consumer path instead of growing it one runtime observation at a time. Size repeated changes against shared banks, extents, buffers, or slot pools before general adoption. A representative PoC may run alongside that survey, but its local result retains its declared proof scope.
- For display and representation conflicts, establish target-proven limits and survey feasible supply, design, wording or adaptation, and scope alternatives far enough to expose their semantic effect, cost, risk, and affected population. Do not force a supply-first sequence or claim that reduction is necessary before that comparison.
- Verify adopted changes together through the primary build and real consumer paths. Do not repeat an equivalent failed attempt. Return to the premise or declared scope when further work presents a materially different product, quality, cost, risk, or support choice.

## Core invariants

### Claim and build gates

A violation stops the affected release claim. A mechanically invalid product input or artifact also stops the build unless a declared development-input policy explicitly permits that condition. Record every exception and its claim limit.

- **Represent player impact honestly.** Humans set the quality target, supported scope, and accepted limitations. Crashes, progression blocks, broken glyphs, misleading text, semantic loss, and presentation defects are evidence against claims such as playable, complete, or release-ready; do not assign universal product severity from the category alone. A human decision may change the quality criterion, scope, or claim that applies to later judgment, but it does not rewrite an earlier observation against its original criterion. A development or pre-release build may disclose known limitations under `references/conventions/translation-artifacts.md` §5. A release candidate must meet the current human-approved quality target and make no claim broader than its evidence, while still passing every mechanical gate required by that scope and claim. Apply issue closure and release reassessment through `references/strategy/debugging.md` §6 and `references/strategy/build-and-verify.md` §6.
- **Never commit source ROM or disc images, or unauthorized third-party assets.** Follow `references/conventions/project-conventions.md` §6 for permitted assets and source identification.
- **Make every final change verifiable before applying it.** Starting from an immutable source, identify the producer and allowed range of each change. Fail the build on overlapping writers, protected-range writes, or unexplained final differences. Follow `references/conventions/project-conventions.md` §5.2.
- **Never silently skip or substitute a character whose glyph or encoding is missing.** An unmapped character fails the build. A development build proceeds only with the unmapped set declared under `references/conventions/translation-artifacts.md` §5, and never becomes a release candidate.

### Judgment invariants

These determine how every other decision is made. Apply them in every judgment area.

- **Verify a transform boundary before modifying it.** Establish the byte-level reversibility or consumer-meaning equivalence that the boundary requires, with the denominator and equivalence rules in `references/conventions/project-conventions.md` §5.1.
- **Keep investigation observations, adopted specifications, build gates, tests, and artifact evidence distinct.** A path to completion connects these roles; it does not replay discovery or design work in every build. Reopen an adopted specification only when its applicability fails or new evidence challenges it. Derive values that legitimately vary with product inputs in the build instead of freezing them as tests. Builds reject invalid artifacts; tests exercise stable behavior, formats, and reproduced failures. See `references/strategy/build-and-verify.md` §1 and `references/conventions/project-conventions.md` §1 and §5.3.
- **Keep product intent, established constraints, adopted design, and current implementation distinct.** Approved meaning, terminology, voice, wording, presentation, and scope define product value; target-proven limits constrain it; design choices remain revisable; current code and prior investment establish behavior and change cost, not authority over value. See `references/strategy/translation-workflow.md` §4.1.
- **Keep decision authority with its subject.** The agent independently searches, surveys, reproduces, measures, and establishes feasible options, technical limits, cost, risk, affected scope, and claim limits. Humans choose product and localization scope, quality targets, supported targets, acceptable semantic or visual loss, accepted limitations, and whether a material technical investment or redesign is worthwhile. Do not ask a human to perform missing technical diagnosis. Proceed when one bounded, reversible in-scope implementation choice clearly preserves approved intent and differs only in ordinary technical detail. Record material human choices with applicability and reassessment conditions under `references/conventions/project-records.md` §1.1, and use an applicable current decision as a heuristic basis rather than reopening it without a trigger. Human preference cannot waive protected information or mechanical artifact constraints; change the implementation, design, declared scope, or claim instead.
- **Reserve semantic and presentation judgment for humans.** Automation may enforce determinate rules and human-approved thresholds or present review candidates; it does not decide naturalness, voice, adaptation, presentation taste, or acceptable loss. Human review of the declared localization scope is required for release-candidate judgment, while declared development inputs may continue under `references/conventions/translation-artifacts.md` §5. See `references/strategy/translation-workflow.md` §5.
- **Relate local evidence to one cumulative product claim.** Use small units when they discriminate well, but state what they prove, what remains unresolved, and whether the primary build incorporates the adopted result. Do not add component successes and call the sum complete. Verify every declared change together from immutable source and approved inputs through the primary build and applicable consumer paths. See `references/strategy/poc.md` §4 and §6.
- **Treat prior structures and numbers as hypotheses.** Do not transfer script formats, pointer rules, control codes, free-space amounts, or capacity figures before they are verified on the target revision through the actual consumer, even across the same platform, developer, or series.
