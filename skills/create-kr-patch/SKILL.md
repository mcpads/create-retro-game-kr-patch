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

Update decisions from evidence in the target game. Connect initial survey, fonts and encoding, PoC, extraction, translation, reinsertion, builds, distributable patches, and runtime verification into one completion path.

Choose tools, languages, libraries, and fonts from the target project's existing structure and the current environment. Regardless of those choices, preserve the required capabilities and verification criteria. Look up basic specifications from current primary sources when one straightforward search can recover them.

This methodology began with Japanese-source, text-heavy games. Treat observed frequencies and prior structures as hypotheses until the target revision confirms them.

## Routing

For an existing repository, reconstruct the current code, documents, artifacts, and verification state before choosing the active judgment area. Start with initial survey when the game or its structure is not yet understood.

| Judgment area | Document | Use it to determine |
|---|---|---|
| Initial survey | `references/strategy/initial-survey.md` | Completion-critical conditions, real dependency boundaries, initial volume, unresolved populations, and revision-specific facts |
| Fonts and encoding | `references/strategy/font-strategy.md` | Code-to-glyph mapping, total repertoire, active working set, representation, and runtime reachability |
| Text extraction | `references/strategy/text-extraction.md` | Population and volume, consumer-defined boundaries and tokens, reversible artifacts, and round trips |
| PoC | `references/strategy/poc.md` | Whether a PoC is needed and what visibility, representative end to end, or conditional proof must establish |
| Reinsertion and hooks | `references/strategy/reinsertion.md` | Boundary policies, reference completeness, hooks, space, and consumer invariants |
| Translation | `references/strategy/translation-workflow.md` | Translation work and agent assignment, context, approved terminology and voice, protected constraints, and high-risk meaning |
| Build and verification | `references/strategy/build-and-verify.md` | Reproducible artifacts, distribution boundaries, integrity and runtime verification, text and interaction QA, and release readiness |
| Debugging and issue handling | `references/strategy/debugging.md` | Gameplay routes, target-state access, proof scope of state intervention, causes, fixes, and regression evidence |
| Graphics text, cross-cutting | `references/strategy/graphics-text.md` | Pixel-text population, protected visual assets, and consumer-path verification |
| Compression, cross-cutting | `references/strategy/compression.md` | Actual transform boundaries, consumer compatibility, and repacking verification |
| Runtime asset reachability, cross-cutting | `references/strategy/runtime-assets.md` | Storage, lookup, load or transform, residency, and consumption as one connected claim |

Apply the relevant conventions when designing or validating artifacts, interchange data, or records. Preserve an existing repository's equivalent structure when it already carries the same meanings.

| Scope | Document | Use it for |
|---|---|---|
| Project implementation, cross-cutting | `references/conventions/project-conventions.md` | Build boundaries, machine-code verification, round-trip equivalence and denominator, final-write verification, test policy, external-component reproduction, and source assets |
| Translation artifacts | `references/conventions/translation-artifacts.md` | Source preservation, control tokens, review states, and build-input eligibility |
| Project records | `references/conventions/project-records.md` | Survey, PoC decisions, graphics-text catalog, HITL observations, QA evidence, and issue states |
| Analysis and build data | `references/conventions/data-formats.md` | Character maps, controls, pointers, translation links, reinsertion policies, and font render profile meanings |

Read a platform document only when a hardware, medium, address-space, or rendering constraint can change the current decision.

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
| Nintendo DS | `references/platforms/nds.md` |

For an unlisted platform, establish only the constraints that can change the current decision.

Whenever the judgment area or observed symptom changes, compare it with `Read when` in `references/tips/README.md`. Re-establish the selected case's `Transfer limit` in the current target. Determine completion from its `Related criteria`, never from resemblance to the case.

## Decision flow

- Define the intended completion scope and every condition that must hold within it.
- Investigate unresolved conditions that would make completion impossible or force a major redesign before optimizing lower-risk work. Compare cost only between evidence that resolves the same condition while preserving the same prerequisite state and proof scope.
- Investigate independent boundaries in parallel. When new evidence overturns a decision, return the affected claims to their causal boundary and reassess what depended on them.
- A representative PoC may run alongside population survey. Before scaling translation to the full distribution scope, determine population and volume through `references/strategy/text-extraction.md` §1.5. Determine glyph demand and supply from the first-draft corpus through `references/strategy/translation-workflow.md` §5.4 and `references/strategy/font-strategy.md` §3.
- Do not grow a finite file or asset population one runtime observation at a time. Enumerate and partition it by consumer path through `references/strategy/initial-survey.md` §2.5, then limit runtime claims through `references/strategy/runtime-assets.md` §2. When the same change then repeats across that population, size it against the whole population before adopting the first instance; `references/strategy/reinsertion.md` §1 owns shared banks, extents, buffers, and slot pools.
- For finite display areas, distinguish observed source usage, confirmed consumer capacity, and the adopted display range through `references/strategy/translation-workflow.md` §4. Expand supply before reducing meaning; require human approval for any meaning or voice loss.
- Verify changed artifacts through the real build and consumer path. Fix a defect at the first boundary where the value diverges. Return to the declared completion scope when every policy its owning document offers has been rejected with evidence, or when the same boundary fails again after its established cause was addressed. There, narrow it through `references/strategy/initial-survey.md` §5 or change the design rather than continuing local attempts.

## Core invariants

### Blocking invariants

A violation here stops the release path, and stops the build unless the invariant names a development exception. Every such exception is declared and recorded; none is taken silently. Resolve it before continuing any dependent work.

- **Principle zero: a player usually plays once.** A release requires zero known critical defects; a pre-release test build under `references/conventions/translation-artifacts.md` §5 discloses them instead. Crashes and progression blocks qualify, but so do broken glyphs, misleading hints or item names, and collapsed terminology or character voice. A mistranslation can cause progression failure, wrong choices, or false character interpretation.
- **Never commit source ROM or disc images, or unauthorized third-party assets.** Follow `references/conventions/project-conventions.md` §6 for permitted assets and source identification.
- **Make every final change verifiable before applying it.** Starting from an immutable source, identify the producer and allowed range of each change. Fail the build on overlapping writers, protected-range writes, or unexplained final differences. Follow `references/conventions/project-conventions.md` §5.2.
- **Require human approval before any rule-based bulk transformation of translated prose.** Do not apply detection results until a human has reviewed the transformation rule, the pre-transformation text, scope, and expected impact. Let `references/strategy/translation-workflow.md` §5.2 determine exceptions.
- **Never silently skip or substitute a character whose glyph or encoding is missing.** An unmapped character fails the build. A development build proceeds only with the unmapped set declared under `references/conventions/translation-artifacts.md` §5, and never becomes a release candidate.

### Judgment invariants

These determine how every other decision is made. Apply them in every judgment area.

- **Verify a transform boundary before modifying it.** Establish the byte-level reversibility or consumer-meaning equivalence that the boundary requires, with the denominator and equivalence rules in `references/conventions/project-conventions.md` §5.1.
- **Verify the complete declared range of any generated or relocated ISA profile.** Verifying only the instructions needed by one patch does not establish complete generation, relocation, or control flow. Follow `references/conventions/project-conventions.md` §2.3 for the full rule and its narrow exceptions.
- **Assign the first draft of free prose to the current agent or to subagents that share its evidence baseline and context.** Use another model or agent only for a scope that a human has approved after evaluating representative samples from the real target. Volume, speed, or cost does not justify an unverified translator. See `references/strategy/translation-workflow.md` §3.1.
- **Reserve final judgment of free prose for humans.** Automated checks and language heuristics may identify candidates and impact, but they do not replace translation review. Automation may reject only violations with human-approved scope and thresholds, or violations with a determinate truth value such as protected information and proven consumer constraints. Human review of the declared localization scope is a release-candidate requirement; development continues under `references/conventions/translation-artifacts.md` §5. See `references/strategy/translation-workflow.md` §5.1 and §5.4.
- **Preserve completion conditions in every unit that must prove one.** Such a unit includes all boundaries that must hold together and the hardest established constraint. If diagnosis uses smaller units, return the result to the original completion condition before accepting it. See `references/strategy/poc.md` §4.
- **Require evidence for one complete path.** Do not add component-level successes and call the sum complete. Verify every declared change together in one build produced from the immutable source and approved inputs through the primary build path. Mark only populations, boundaries, and consumer rules with established coverage as complete. Partial success that leaves a completion-critical condition unresolved is not evidence for that condition.
- **Treat prior structures and numbers as hypotheses.** Do not transfer script formats, pointer rules, control codes, free-space amounts, or capacity figures before the target revision and consumer prove them, even across the same platform, developer, or series.
- **Supply the main character set from an established, verifiable font.** Do not draw the body font merely for PoC convenience. Limit custom glyph work to local omissions or established UX needs. See `references/strategy/font-strategy.md` §4.
