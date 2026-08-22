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

Treat source-language frequencies and structures from other titles as hypotheses until the target revision confirms them.

## Foundational principle

**Treat each playthrough as the whole product.** For many players, one playthrough is their entire experience of the game. Do not describe a release as mostly working while a known in-scope defect can block progress, corrupt displayed text or intended meaning, mislead the player about a choice, break established terminology or voice, or impair interaction. Fix the defect, narrow the scope or claim through an explicit human decision, or withhold the release; successful paths do not offset it. See `references/strategy/build-and-verify.md` §6 and `references/strategy/translation-workflow.md` §6.

## Operating principles

1. **Credit progress only to the claim it actually strengthens.** Keep the hardest or most decisive unresolved condition for completion visible. Choose another task only when it supplies evidence or a prerequisite for that condition, advances another independently valuable claim, or implements a relevant recorded human decision. This preserves direction without imposing a fixed order. See `references/conventions/project-records.md` §1, `references/conventions/project-conventions.md` §1 and §5.3, and `references/strategy/build-and-verify.md` §1.
2. **Reassess the approach when an observation conflicts with the current explanation or work stops producing information.** Do so when repeated work yields equivalent evidence, local checks pass without strengthening the cumulative claim, or repairs add exceptions or conflicting accounts of the current state without explaining the mismatch. When resuming work, reconstruct the current baseline, the completion condition at issue, and evidence for live and rejected explanations from the authoritative project records before another attempt. Search `references/tips/README.md` using the observation or affected transition; a case can suggest another hypothesis and evidence that distinguishes it from alternatives, not a repair to copy. Preserve valid evidence and do not force an analogy. See `references/conventions/project-records.md` §2 and `references/strategy/debugging.md` §2·§3·§6.
3. **Keep product priorities and decision authority separate from implementation.** Current code and prior investment establish behavior and the cost of change; they do not decide what the product should value. The agent establishes technical facts and feasible options; humans make material choices about product direction, quality, scope, acceptable loss, support, and investment. Do not transfer an unresolved technical diagnosis to a human or request a new decision for a routine implementation choice with limited scope that preserves approved intent. Record material decisions under `references/conventions/project-records.md` §1.1; apply translation boundaries through `references/strategy/translation-workflow.md` §4.1 and §5.

## Task-specific guidance

For an existing repository, reconstruct the current code, documents, artifacts, and verification state before choosing the guidance relevant to the next decision. Start with the initial survey when the game or its structure is not yet understood.

| Decision area | Document | Use it to determine |
|---|---|---|
| Initial survey | `references/strategy/initial-survey.md` | Completion-critical conditions, actual dependencies, initial volume, unresolved populations, and revision-specific facts |
| Fonts and encoding | `references/strategy/font-strategy.md` | Code-to-glyph mapping, total repertoire, active working set, representation, and runtime reachability |
| Name entry and user strings | `references/strategy/name-entry.md` | Input repertoire, editing state, committed records, glyph supply, redisplay consumers, and persistence |
| Text extraction | `references/strategy/text-extraction.md` | Population and volume, consumer-defined boundaries and tokens, reversible artifacts, and round trips |
| PoC | `references/strategy/poc.md` | Whether a PoC is needed and what a visibility, representative end-to-end, or conditional PoC must establish |
| Reinsertion and hooks | `references/strategy/reinsertion.md` | Boundary policies, reference completeness, hooks, space, and consumer invariants |
| Translation | `references/strategy/translation-workflow.md` | Translation work and agent assignment, context, approved terminology and voice, protected information and consumer constraints, and high-impact semantic decisions |
| Build and verification | `references/strategy/build-and-verify.md` | Reproducible artifacts, checks enforced by the build, distribution boundaries, integrity and runtime verification, text and interaction QA, and release readiness |
| Debugging and issue handling | `references/strategy/debugging.md` | Gameplay routes, target-state access, what state intervention can establish, causes, fixes, and regression evidence |
| Graphics text | `references/strategy/graphics-text.md` | Pixel-text population, protected visual assets, and consumer-path verification |
| Compression | `references/strategy/compression.md` | Verified transformation boundaries, consumer compatibility, and repacking verification |
| Runtime asset reachability | `references/strategy/runtime-assets.md` | Storage, lookup, load or transform, residency, and consumption as one connected claim |

Apply the relevant conventions when designing or validating artifacts, exchange data, or records. Keep an existing repository structure when it already preserves the same responsibilities and constraints.

| Scope | Document | Use it for |
|---|---|---|
| Project-wide implementation | `references/conventions/project-conventions.md` | Investigation, build, test, and runtime-verification ownership; machine-code verification; round-trip equivalence and denominator; final-write verification; external-component reproducibility; and source assets |
| Translation artifacts | `references/conventions/translation-artifacts.md` | Source preservation, control tokens, review states, and build-input eligibility |
| Project records | `references/conventions/project-records.md` | Human strategic decisions, survey and PoC decisions, graphics-text catalog, HITL observations, QA evidence, and issue states |
| Analysis and build data | `references/conventions/data-formats.md` | Character maps, controls, pointers, translation links, reinsertion policies, and font-rendering profiles |

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

## Artifact requirements

Violating one of these requirements invalidates the affected release claim. A mechanically invalid input or artifact must also stop the build unless the declared development-input policy permits it. Record every exception and the resulting limit on the claim.

- Never commit source ROM or disc images, or unauthorized third-party assets. Follow `references/conventions/project-conventions.md` §6.
- Plan every final change from an immutable source and fail on overlapping writers, protected-range writes, or unexplained final differences. Follow `references/conventions/project-conventions.md` §5.2.
- Never silently skip or substitute a character whose glyph or encoding is missing. An unmapped character fails the build. A development build may proceed only under `references/conventions/translation-artifacts.md` §5 and cannot become a release candidate.
