# Translation workflow

Judge translation and distribution eligibility by separating established context and approved decisions, protected information and consumer constraints, and semantic issues that require human judgment. Promote each state only when its evidence is satisfied.

## 1. States and eligibility

Translation eligibility and distribution eligibility are separate.

- **Translation-eligible** means the scene, speaker, and functional context needed to determine meaning is established, and the applicable approved terminology and voice decisions are identified. Do not fill unresolved context by guesswork.
- **Distribution-eligible** additionally means protected information and actual consumer constraints pass, and every high-impact semantic decision is resolved and approved.

Define the eligibility unit at the real build-selection boundary. Do not expand one unresolved item to an unrelated scope or silently include it in a selected range. A defect found in review or runtime QA revokes eligibility for affected units and returns them to the relevant decision.

Human review of the declared translation scope is a release-candidate condition, not a blocker for technical development. Preserve source text for incomplete units or mark them as development inputs under `references/conventions/translation-artifacts.md` §5. Any input selected by a development build must still preserve protected information and established structural and consumer constraints.

Declare the completion denominator from confirmed translation targets and evidenced exclusions. A count difference between new extraction and existing assets is a candidate change, not a missing-translation count until additions, removals, duplicates, and non-text are distinguished.

Before scaling translation to the full distribution scope, pass the volume survey in `references/strategy/text-extraction.md` §1.5. Do not generalize earlier local results into total workload, completion, or complete-corpus demand.

Apply `references/conventions/translation-artifacts.md` to asset states and protected information, and `references/strategy/build-and-verify.md` §1 to common build inputs.

## 2. Establishing context

Context links extracted text to actual scenes, screens, and functions and narrows interpretations. Work may begin on a scope with an established denominator before complete extraction of the entire distribution, but the translated unit's denominator and consumer context must be known.

### 2.1 Context decision

Context is established when no unresolved factor can change the unit's translation, or remaining uncertainty is shown irrelevant to the result. Required evidence depends on the game and string role; do not impose one document set or checklist on every project.

If uncertainty can change meaning, return to scene inspection, further extraction, or consumer-path analysis. Do not replace it with general knowledge or a plausible guess.

When narrative, route, or relationship information outside the local unit can change meaning, establish that dependency first. For narrative-heavy dialogue, obtain enough of the complete plot, branches, and major relationship changes to assess outside influence. Reconstruct the applicable route structure before translating units affected by late reveals, branch order, or relationship changes. Conversely, do not require complete story reconstruction for independent UI or scenes already shown not to depend on it.

### 2.2 Evidence scope

Use source extraction and actual consumed scenes as the baseline. Consult external sources when they can decide unresolved meaning, order, speaker, or terminology scope. Do not search every source category ceremonially after the question is already decided.

- Primary sources such as official manuals, sites, and guides may establish setting, names, and functions. Official Korean or other localizations are candidates for established wording; verify title, revision, region, and series continuity.
- Guides and walkthroughs may reconstruct scene order, branches, characters, and system functions. They are not source text for exact wording or speaker intent.
- Prior localizations, fan patches, and reverse-engineering records provide interpretation candidates and technical clues. Compare them with source text and real scenes because they may add, omit, or change viewpoint.

If external sources do not resolve the question, return to corpus reading, route execution, extraction, or reverse engineering. Finding a source does not approve an interpretation whose applicability is unknown.

When new evidence overturns context, correct the current decision and reassess affected eligibility. Do not preserve a rejected interpretation beside current fact as if both remained valid.

### 2.3 Logical order and storage order

Storage order need not equal play or scene order. Build a translator-facing logical view around scene, screen, and speaker relations when required for meaning, but do not turn that reordering into a changed extraction baseline or physical layout. Identical source text need not receive identical translation when consumer scene or speaker differs.

### 2.4 Speaker and voice context

Include speaker, addressee, relationship, and scene evidence when they can change translation. Do not give inferred tone the same confidence as established control signals, screens, or dialogue order. If an inference can change the result, leave it for human judgment and do not promote the unit before resolution.

One speaker rule need not apply across every relationship or scene. When differences change translation, scope approval by speaker-to-addressee relationship and narrative point. The project chooses the representation; §3 owns the approved scope and exceptions.

## 3. Approved terminology and voice

Manage reusable decisions such as names, system terms, recurring expressions, and speaker voice in one approved basis. Distinguish decision, applicability, evidence, and review state, following `references/conventions/translation-artifacts.md`.

- Writers and reviewers use the same approved basis and must not adopt silent local variants.
- Split applicability when one source term refers to different targets, speakers, or scenes; do not create unexplained variants for the same target.
- A new term, source conflict, or voice exception that can change output blocks affected eligibility until approval.
- Series and prior-localization choices remain candidates until approved for this title and context.
- Before approving names, places, items, or system terms, check applicable official Korean wording or formally inherited wording from another edition or title. Adopt it only where source meaning and continuity match.
- Do not impose one source ranking or style priority on every project. Declare authority for the target and translation goal.

Automation may flag candidates against approved decisions but cannot approve a new wording or resolve a conflict. It may decide a violation only when applicability and allowed output are unambiguous. Word presence, inflection, omission, and adaptation in free prose require semantic review.

### 3.1 Translation work and agent assignment

Split work at boundaries that preserve context. The current translation agent must either draft free prose directly or divide it among subagents within the same workflow. Give each subagent the complete baseline and context below and independently review its result. Do not outsource the full first draft to an unverified model or agent solely for volume, speed, or cost.

Before assigning substantial drafting to another model or agent, translate representative target samples and high-impact sentences under the same context, terminology, and voice conditions as production. A human evaluates accuracy, retained context and voice, and correction burden, then approves the assigned scope. Include dialogue, UI, sentences with names, context-sensitive sentences, and items with protected tokens or display constraints. Do not generate the full corpus under the label of evaluation, and do not replace human evaluation with an average score or agreement among models.

An evaluation applies only to the sampled text and conditions. Reevaluate affected scope when the model or agent, supplied context, terminology, or voice basis changes. A human-evaluated sample may remain as a working draft under the same baseline, but evaluation does not complete review or grant distribution eligibility. A failed model or agent may still organize batches, serialize data, and inspect protected information; it must not draft or choose free prose.

Parallel drafting or review requires established decision context and independent review per unit. Split the corpus if it cannot satisfy those requirements as one unit; do not split it merely to create batches when it can. Do not cut scene, speaker, or functional context, or make batches so large that a reviewer loses the relationships needed for judgment.

Draft free prose from context. Rule-based automation may organize batches, serialize data, and run checks. It must not generate or choose translated prose except for fixed phrases whose applicability and output are already approved.

Provide writers and reviewers with one baseline containing:

- stable ID, source text, and protected raw bytes;
- reversible control tokens and forbidden raw tokens with established boundaries and argument widths;
- target-consumer meaning and the policy from `references/strategy/text-extraction.md` §4.4 for established tokens;
- scene, speaker, adjacent context, source consumption order, and any global narrative or route dependency that changes meaning;
- approved terminology and voice with applicability; and
- actual length, layout, encoding, and other consumer constraints.

Agent output may change translated text, rationale, questions, and proposal state. It must not recreate or normalize source identity, raw bytes, or protected tokens. A batch is a logical translation unit; it does not redefine source entry boundaries, order, or physical placement.

When a term, voice decision, or source interpretation changes across batches, revalidate earlier affected batches against the same approved basis. Merge parallel results only when stable IDs and baselines match. Never resolve conflicts in entries, terminology, or protected information by last-writer-wins. Apply the state and protected-field semantics in `references/conventions/translation-artifacts.md`.

## 4. Protected information and consumer constraints

Separate translatable content from structure that must remain. Translation must not change source-baseline values such as raw bytes, identifiers, pointer evidence, and boundary information.

Assign control-token policies from actual consumption: preserve, move within layout, recompute, translate to target meaning, or forbid editing. A token that changes meaning or execution, such as termination, event, or variable insertion, includes order and arguments in its preservation rule. Preserve an unresolved-meaning token in forbidden raw form only when boundary and argument width are established. Otherwise block the unit from translation and distribution eligibility. Apply `references/conventions/translation-artifacts.md` §3 to representation and `references/strategy/text-extraction.md` §4.4 to reversibility and policy.

Line, page, and wait tokens may move for Korean readability, page rhythm, and display constraints only after their consumer meaning and valid positions are established. Require equivalent state transitions under the token policy. Judge window, portrait, selection, input, voice, and event tokens by their own policies and verify changes through `references/strategy/build-and-verify.md` §5.

Derive length, width, rows, slots, encoding, and insertion combinations from the real consumer, not language-wide defaults. Do not disguise a technical constraint violation as poor translation or resolve it automatically through semantic shortening. Choose among phrasing adjustment, established line or page controls, progression changes, and capacity changes according to the cause and effect.

For a finite display area, distinguish:

- **Observed source usage**: maxima observed across source visible width, rows, pages, and placement.
- **Confirmed consumer capacity**: limits established by connecting stored width, height, or coordinates to consumer calculations.
- **Adopted display range**: the range selected for the Korean patch.

An observed maximum does not prove that the game permits no more. Do not merge limits from different renderers or window types.

When translated output exceeds observed source usage, do not shorten it automatically or fail it for that fact alone. Establish capacity through consumer code, display area, and runtime results, or change the adopted display range and verify it on the same consumer path. Human preference cannot waive protected information or established consumer constraints. If capacity remains unresolved and output exceeds source usage, return to consumer analysis and withhold distribution eligibility.

## 5. Separate generation, review, and approval

Do not merge mechanically decidable violations with semantic judgment. Semantic or human approval cannot replace protected-information, state, encoding, or consumer checks, and passing mechanical checks cannot replace semantic review.

| Class | Subject | Role of automation |
|---|---|---|
| Established constraint | Protected fields and tokens; encoding and glyph mapping; confirmed width, height, row, page, and slot limits; approved wording with one unambiguous applicability and output | Withhold distribution eligibility and block release-candidate builds on violation |
| Language heuristic | Dictionary presence, frequency, spelling and spacing, repeated phrases, LLM scores | Produce candidates with evidence and affected scope for human review; do not edit prose or decide fitness |
| Semantic judgment | Contextual meaning, naturalness, voice and relationship, adaptation, names, and wordplay | Produce options and evidence in independent review; a human decides |

Observed source maxima are not established consumer constraints by themselves. Dictionary presence does not prove correctness or error. Unresolved heuristic findings may remain review candidates; detection alone is not a confirmed defect and must not decide fitness automatically.

An automated check may identify translation-defect candidates and affected scope. A batch transformation based on such a rule may edit translations only after a human explicitly approves the rule, baseline, scope, and expected impact. Any change to them requires renewed approval. Approval of the transformation does not grant distribution eligibility; results must pass current source, context, terminology, voice, protected-information, and consumer checks. Send exceptions and high-impact semantics to unit-level translation and review. Serialization, protected-information checks, and states derived from pass criteria do not require this approval when they do not change translation meaning.

Judge semantic impact by whether an error would materially change player understanding, choice, progression, relationships, or authorial intent, not by a fixed ranking of quality categories. Record options and evidence for conflicts in source interpretation, new wording, adapted wordplay or cultural elements, and uncertain speaker or relationship. Human approval is required. One unresolved high-impact judgment blocks the affected unit from distribution eligibility.

### Timing of human review for the complete distribution scope

The first-draft corpus is an input for measuring representation demand. Complete-scope human review must finish before release-candidate judgment, but should begin only after the integrated development build establishes that:

- unique glyphs from the corpus and runtime insertions fit and can be supplied under the total-repertoire and active-working-set budgets in `references/strategy/font-strategy.md` §3;
- that supply reaches target render paths through `references/strategy/runtime-assets.md` §2 or equivalent evidence; and
- every finite display area can accept the first draft's maximum demand, or has a verified path to change the adopted display range under §4.

Check mapping and coverage mechanically across the complete corpus and runtime insertions. Judge distinct consumer paths with representative runtime evidence or existing equivalent evidence. One-glyph PoC or partial sample does not prove complete-corpus capacity. When a design fails, change supply, loading, or mapping and reverify the same demand and paths.

Human decisions needed earlier for terminology, voice, or high-impact source interpretation may proceed. If glyph reduction changes meaning or voice, obtain approval at that point. Limit early review to necessary decisions. If later review introduces new glyph or state-specific demand, return the affected scope to glyph-budget and consumer-path assessment.

### Conditional flow for an LLM first draft

When an LLM first draft made under §3.1 is considered for distribution eligibility, apply this decision chain:

```text
LLM first draft -> independent second LLM review -> options and evidence to a human -> human approval
                         \-> mechanical violations return to the applicable verification step
```

The second review must not assume the first draft's conclusion. In a separate review context, compare source, approved basis, speaker and scene evidence, and protected and consumer constraints again. When meaning, wording, or voice has alternatives, present options, evidence, impact, and a recommendation instead of silently overwriting the draft. Agreement between two generations does not approve quality. Human approval remains final, and affected units remain ineligible until then.

Independence means a review that does not take the first draft's reasoning or conclusion as the answer. It does not require a specific model, service, or execution mechanism. This flow triggers only when a project chooses an LLM first draft.

## 6. Distribution eligibility

Promote only a scope satisfying all of these conditions:

1. No context uncertainty remains that can change translation.
2. Applicable terminology and voice match the approved basis.
3. Protected tokens and actual consumer constraints pass.
4. High-impact semantic judgments are resolved with required human approval.
5. If an LLM produced the first draft, it received independent second LLM review and human-facing options and evidence.

An ineligible translation may be used only as an explicitly non-distribution development, technical, or PoC input. Output from a model or agent that failed §3.1 evaluation is not eligible for this exception. Such use neither grants distribution eligibility nor bypasses the conditions above; follow `references/conventions/translation-artifacts.md` §5 for identification and protection.

Return failed units to context research, terminology and voice approval, protected or consumer-constraint resolution, or semantic judgment according to the failed condition. Do not collapse these states into one generic "translation complete" label.
