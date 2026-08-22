# Build and verification

Judge build inputs, distribution artifacts, static checks, and runtime checks by the criteria below. Read the applicable `references/platforms/` document for platform-specific checksums, sectors, and execution environments. Record evidence according to `references/conventions/project-records.md`. The target project chooses concrete files, commands, and serialization.

## 1. Reproducible build

The build and distribution path must satisfy all of these conditions:

- Do not commit or distribute copyrighted source ROMs, disc images, or patched images. Follow `references/conventions/project-conventions.md` §6.2 for source injection and handling.
- Rebuild from an immutable source and declared inputs. Never use a previously patched image as the input to the next build.
- Reproduce every final change from build inputs. A change discovered manually must enter the build with its source, applicability, expected original state, and output rule.
- When editing extracted assets, preserve stable entry identity, separate editable values from protected values, and retain undecoded data reversibly. Follow `references/conventions/project-conventions.md` §5.1 for unchanged reassembly equivalence.
- Where the build produces a distribution artifact, derive it and the patched image from the same verification graph. Applying it must reproduce the target image.

The primary build combines every adopted translation, glyph, mapping, reinsertion, code, and container change into one result made from the immutable source. Component checks and PoC artifacts do not prove integration. Judge applicable static and runtime claims on that cumulative result. A development build follows the input policy in `references/conventions/translation-artifacts.md` §5, but every adopted technical change still enters the same build. Keep it producible for runtime verification and diagnosis, and attribute post-integration evidence to that exact result.

The cumulative build consumes adopted results, not the investigation or design procedures that produced them. Apply `references/conventions/project-conventions.md` §1 when promoting either a result or a procedure.

For one supported revision, consume verified reverse-engineering conclusions only within their established applicability. A finite catalog enters the specification only after its population is established. Reopen analysis on a source or applicability mismatch, a reassessment condition, or contrary evidence. Derive addresses, sizes, and checksums that depend on current build inputs, and do not promote heuristic candidates during a build (`references/strategy/initial-survey.md` §3.1).

Turn every criterion that can be decided mechanically from current inputs or artifact structure into a build check; keep runtime behavior under §4. Do not produce a verified artifact when an applicable encoding, glyph or space budget, layout, length, pointer, compression, or container invariant fails. A change that triggers `references/strategy/runtime-assets.md` §1 must pass both static storage/reference/capacity checks and runtime load/residency/consumption checks.

The primary build owns these rejections. Tests may exercise them with fixed inputs, but the build must enforce them for its declared product inputs whenever it runs; apply the ownership rules in `references/conventions/project-conventions.md` §5.3.

Every write from the source to the target image must satisfy the final-write verification rules in `references/conventions/project-conventions.md` §5.2. A failed write check must prevent artifact production.

## 2. Distribution format and image changes

Adopt a distribution format only when the project can prove that it:

- distinguishes the supported source revision, size, and header, track, or sector representation before application;
- compares the applied result with the target image;
- represents file growth, final image size, and the required write set without loss;
- identifies each input and application order for multi-track or multi-artifact releases; and
- fixes a reproducible user application path and distribution conditions.

When file size or extent changes, choose in-place editing, partial relocation, full rebuild, or preservation of the original packing only if that path can verify every changed consumer condition. No option is safe by name alone. The chosen path must prove that:

- boot and game loaders read the new locations, sizes, and alignments;
- duplicate references and metadata at filesystem, container, and game layers identify the same targets;
- untouched tracks, sectors, files, and intentionally irregular source structures remain unchanged outside the declared write scope; and
- reparsed structures are valid and the real loader consumes the new assets.

Failure to establish every reference for a partial relocation does not justify a full rebuild. If no candidate path can produce this evidence, the image change remains incomplete; return to the declared completion scope.

## 3. Integrity verification

Make an integrity field a build responsibility only after establishing its consumer.

- If a header, container, or game routine reads a checksum or size field, update it after every relevant write and verify the exact consumed range.
- If the build emits raw sectors, update error-detection and correction fields for changed sectors according to their actual sector mode. An irregular field in an untouched source sector may participate in protection or media behavior; do not normalize it without evidence.
- If a file location, size, or entry layout changes, update every layer that duplicates those values and compare both reparsed structure and actual consumption.

Successful boot or tolerance in one execution environment does not prove structural or sector integrity.

Build and application entry points must enforce the same source-identification rules. A mismatch must prevent output. The applied result must also match the target image.

## 4. Runtime verification

Set runtime scope from the consumer paths touched by the change and from the distribution claims. Do not turn asset count into an equal number of runtime trials. Use `references/strategy/runtime-assets.md` §2 to determine which items share a verified link and which exceptions require separate execution.

If the route to a target state is unknown, or state intervention could reduce reproduction cost, establish the route and what the intervention can prove through `references/strategy/debugging.md` §2.1 first.

- The development environment must expose observations that distinguish the current failure layer. Do not use absence of an event as negative evidence until the observation method's address, event, and input interpretation are known to cover the real consumer path.
- When claiming support for a console, medium, loader, or execution environment, verify the final candidate on that target path. Add a second environment when tolerance or implementation-specific behavior in the first environment is a current risk. Implementations that are not independent do not count as independent evidence.
- Center execution on representative modified consumer paths. Add boot, exit, re-entry, shared state, and representative unchanged paths only when the change or support claim can affect them.
- Add separate renderers, branches, user input or saves, disc or overlay transitions, and long-lived residency as conditional regressions when they can change consumption of the modified asset or state. Do not impose features absent from the game or unrelated to the change as universal requirements.

Bind every runtime result and reusable state or input recording to the exact target image and environment that produced it. Transfer the result to another build only through byte identity or equivalent consumption at the relevant boundary. Intermediate builds that make no runtime claim do not require their own runtime pass.

Turn a repeated, objectively decidable regression into a reproducible runtime check. When the final semantic or visual judgment is not mechanically decidable, retain an explicit human review instead of reporting automated success. An unavailable observation is not that case: establish it through `references/strategy/debugging.md` §2.1, or report the check as not run.

## 5. Text, presentation, and interaction QA

Judge final text, presentation, and interaction changes on their actual consumer paths. For a finite text scope, evaluate every member against the encoding, width, row, page, and slot model established from that consumer. Activate only criteria present on the target path and plausibly affected by the change.

- Translation review and the build must use the same identities for established target constraints. Keep those constraints distinct from adopted design choices and measurements derived from current build inputs under `references/strategy/translation-workflow.md` §4.1; failure under the selected design does not by itself reject the wording.
- The build must consume the exact wording and layout identities selected by its input policy and recorded under `references/strategy/translation-workflow.md` §5.6. It must not silently shorten, substitute, or switch to an unrecorded scope-specific wording selection.
- Include automatic wrapping, control-token state transitions, and worst-case variable insertion when they affect the consumed result.
- Judge dialogue, menus, and name entry separately when they use different consumers. For player-created text, apply the interaction, redisplay, and persistence scopes in `references/strategy/name-entry.md` §6.
- A violation of an established fixed slot, encoding, or page limit must fail the build. Treat scrolling as valid only when it belongs to the adopted design, and leave genuinely judgment-dependent presentation criteria to human review.
- Judge glyphs and baked graphics text against the visual completion criteria in `references/strategy/font-strategy.md` §4 and `references/strategy/graphics-text.md` §4, using real backgrounds, palettes, and states.
- When a window or frame changes size or position, verify actual anchors, clipping, screen bounds, and overlap with portraits, cursors, and adjacent UI.
- When a change touches state-specific assets or placement, verify the distinctions and transitions among applicable default, focused, selected, and disabled states. Verify affected navigation, confirm and cancel events, repeat behavior, state transitions, and results against the target model.
- When a change touches text progression or synchronization, verify applicable page, wait, scroll, auto-advance, skip, voice, and event timing within the declared tolerance.
- For a changed display extent, verify the layout and clearing criteria in `references/strategy/reinsertion.md` §6 across transition, exit, and re-entry. Page or progression changes must not introduce empty pages or unintended early or duplicate advancement.

Judge the release result from Korean-encoded output and verified consumer conditions, distinguishing observed source usage from confirmed capacity through `references/strategy/translation-workflow.md` §4.

## 6. Issue closure and release readiness

Close a defect as fixed through the completion conditions in `references/strategy/debugging.md` §1. Close an issue as original behavior, an accepted limitation, or out of scope only through the evidence and human-decision boundaries in `references/strategy/debugging.md` §6. Apply the status, authority, and evidence distinctions in `references/conventions/project-records.md` §1.1 and §7.

Incomplete human review of the declared localization scope does not block development builds, technical verification, or a pre-release test build that collects it under `references/conventions/translation-artifacts.md` §5. A release candidate must satisfy all of these conditions:

- Every declared change is regenerated from immutable source and approved inputs through the primary build, and component checks plus runtime evidence pass together on that exact result.
- The declared localization scope matches the population findings in `references/strategy/text-extraction.md` §1.4, §1.5, which record zero unresolved members and evidence for every exclusion.
- Every declared automated build, application, and runtime check required by the current supported scope and release claims passes against its current recorded criterion. When a human decision changes a quality tolerance, scope, or claim, retain the earlier result against its original criterion and reassess the checks applicable to the new decision through `references/strategy/debugging.md` §6.
- The current human-approved quality target and release claims are satisfied, and every known issue and accepted limitation is recorded with its decision authority, scope, player effect, and claim impact.
- Human review of the complete localization scope is complete under `references/strategy/translation-workflow.md` §5.4.
- Applying the distribution artifact reproduces the verified target image.
- Player-facing release material states supported source revisions and representations, the verified application procedure and prerequisites, play-affecting limitations or exclusions, and save-data compatibility or required migration. It presents facts owned by the source profiles in `references/conventions/project-conventions.md` §6.2, the distribution path in `references/strategy/build-and-verify.md` §2, and current decision and QA records in `references/conventions/project-records.md` §1.1·§7; it does not redefine them.
