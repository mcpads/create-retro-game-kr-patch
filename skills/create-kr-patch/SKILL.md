---
name: create-kr-patch
description: >-
  Use for Korean (Hangul) fan translations of retro console or PC games,
  including ROM or disc analysis, text-engine reverse engineering, Hangul fonts
  and custom encodings, script extraction and reinsertion, code hooks, patch
  builds, and emulator verification. Apply it to both new investigations and
  follow-up work in existing Korean-patch projects.
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
| Build and verification | `references/strategy/build-and-verify.md` | Reproducible artifacts, distribution boundaries, layered verification, and completion |
| Debugging and issue handling | `references/strategy/debugging.md` | Gameplay routes, target-state access, proof scope of state intervention, causes, fixes, and regression evidence |
| Graphics text, cross-cutting | `references/strategy/graphics-text.md` | Pixel-text population, protected visual assets, and consumer-path verification |
| Compression, cross-cutting | `references/strategy/compression.md` | Actual transform boundaries, consumer compatibility, and repacking verification |
| Runtime asset reachability, cross-cutting | `references/strategy/runtime-assets.md` | Storage, lookup, load or transform, residency, and consumption as one connected claim |

Apply the relevant conventions when designing or validating artifacts, interchange data, or records. Preserve an existing repository's equivalent structure when it already carries the same meanings.

| Scope | Document | Use it for |
|---|---|---|
| Project implementation, cross-cutting | `references/conventions/project-conventions.md` | Build boundaries, machine-code verification, round-trip equivalence and denominator, final-write verification, external-component reproduction, and source assets |
| Translation artifacts | `references/conventions/translation-artifacts.md` | Source preservation, control tokens, review states, and build-input eligibility |
| Project records | `references/conventions/project-records.md` | Survey, PoC, graphics catalog, HITL, QA evidence, and decision records |
| Analysis and build data | `references/conventions/data-formats.md` | Character maps, controls, pointers, translation links, reinsertion policies, and font configuration meanings |

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
- Investigate independent boundaries in parallel. When new evidence overturns a decision, return only the affected claims to their causal boundary.
- A representative PoC may run alongside population survey. Before scaling translation to the full distribution scope, determine population and volume through `references/strategy/text-extraction.md` §1.5, then determine glyph demand and supply through `references/strategy/translation-workflow.md` §5.4 and `references/strategy/font-strategy.md` §3.
- Do not grow a finite file or asset population one runtime observation at a time. Enumerate and partition it by consumer path through `references/strategy/initial-survey.md` §2.5, then limit runtime claims through `references/strategy/runtime-assets.md` §2.
- For finite display areas, distinguish observed source usage, confirmed consumer capacity, and the adopted display range through `references/strategy/translation-workflow.md` §4. Expand supply before reducing meaning; require human approval for any meaning or voice loss.
- Verify changed artifacts through the real build and consumer path. Fix a defect at the first boundary where the value diverges.

## Core invariants

### Blocking invariants

A violation here produces no artifact: the build fails, or the result does not qualify as a release candidate. Resolve it before continuing any dependent work.

- **Principle zero: a player usually plays once.** A release requires zero known critical defects. Crashes and progression blocks qualify, but so do broken glyphs, misleading hints or item names, and collapsed terminology or character voice. A mistranslation can cause progression failure, wrong choices, or false character interpretation.
- **Never commit source ROM or disc images, or unauthorized third-party assets.** Follow `references/conventions/project-conventions.md` §6 for permitted assets and source identification.
- **Make every final change verifiable before applying it.** Starting from an immutable source, identify the producer and allowed range of each change. Fail the build on overlapping writers, protected-range writes, or unexplained final differences. Follow `references/conventions/project-conventions.md` §5.2.
- **Require human approval before any batch edit of translated prose.** Do not apply detection results until a human has reviewed the baseline, transformation rule, scope, and expected impact. Let `references/strategy/translation-workflow.md` §5.2 determine exceptions.
- **Fail the build on any unmapped translated character.** Never skip a character whose glyph or encoding is missing.

### Judgment invariants

These determine how every other decision is made. Apply them in every judgment area.

- **Verify a transform boundary before modifying it.** Establish the byte-level reversibility required by that boundary, or equivalence in consumer meaning and protected information. Use the denominator and equivalence rules in `references/conventions/project-conventions.md` §5.1.
- **Verify the complete declared range of any generated or relocated machine-code profile.** Verifying only the instructions needed by one patch does not establish complete generation, relocation, or control flow. Follow `references/conventions/project-conventions.md` §2.3 for the full rule and its narrow exceptions.
- **Assign the first draft of free prose to the current agent or to subagents that share its evidence baseline and context.** Use another model or agent only for a scope that a human has approved after evaluating representative samples from the real target. Volume, speed, or cost does not justify an unverified translator. See `references/strategy/translation-workflow.md` §3.1.
- **Reserve final judgment of free prose for humans.** Automated checks and language heuristics may identify candidates and impact, but they do not replace translation review. Automation may reject only violations with human-approved scope and thresholds, or violations with a determinate truth value such as protected information and proven consumer constraints. Human review of the declared translation scope is a release-candidate requirement; leave unfinished units in the source language and continue development. See `references/strategy/translation-workflow.md` §5.1 and §5.4.
- **Preserve completion conditions in every work unit.** A representative unit includes all boundaries that must hold together and the hardest confirmed constraint. If diagnosis uses smaller units, return the result to the original completion condition before accepting it.
- **Require evidence for one complete path.** Do not add component-level successes and call the sum complete. Verify every declared change together in one build produced from the immutable source and approved inputs through the primary build path. Mark only populations, boundaries, and consumer rules with established coverage as complete. Partial success that leaves a completion-critical condition unresolved is not evidence for that condition.
- **Treat prior structures and numbers as hypotheses.** Do not transfer script formats, pointer rules, control codes, free-space amounts, or capacity figures before the target revision and consumer prove them, even across the same platform, developer, or series.
- **Supply the main character set from an established, verifiable font.** Do not draw the body font merely for PoC convenience. Limit custom glyph work to local omissions or established UX needs. See `references/strategy/font-strategy.md` §4.
