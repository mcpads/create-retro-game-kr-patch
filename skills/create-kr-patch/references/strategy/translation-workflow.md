# Translation workflow

Judge translation and distribution eligibility by separating established context and approved decisions, protected information and consumer constraints, and semantic issues that require human judgment. Advance a unit to the next state only when the corresponding evidence requirements are satisfied.

## 1. States and eligibility

Translation eligibility and distribution eligibility are separate.

- **Translation-eligible** means the scene, speaker, and functional context needed to determine meaning is established, and the applicable approved terminology and voice decisions are identified. Do not fill unresolved context by guesswork.
- **Distribution-eligible** additionally means checks on protected information and actual consumer constraints pass, and every high-impact semantic decision is resolved and approved.

Define eligibility at the unit the product build actually selects. Do not expand one unresolved item to an unrelated scope or silently include it in a selected range. A defect found in review or runtime QA revokes eligibility for affected units and returns them to the relevant decision.

Human review of the declared localization scope is a release-candidate condition, not a blocker for technical development. Preserve source text for incomplete units or mark them as development inputs under `references/conventions/translation-artifacts.md` §5. Any input selected under the development/PoC input policy must still preserve protected information and established structural and consumer constraints.

Declare the completion denominator from confirmed translation targets and exclusions supported by evidence. A count difference between new extraction and existing assets is a candidate change, not a missing-translation count until additions, removals, duplicates, and non-text are distinguished.

Before scaling translation to the full distribution scope, complete the volume survey in `references/strategy/text-extraction.md` §1.5. Do not generalize earlier local results into total workload, completion, or complete-corpus demand.

Apply `references/conventions/translation-artifacts.md` to asset states and protected information, and `references/strategy/build-and-verify.md` §1 to inputs for the primary product build.

## 2. Establishing context

Context links extracted text to actual scenes, screens, and functions and narrows interpretations. Work may begin within a scope with an established denominator before complete extraction of the entire distribution, but the translated unit's denominator and consumer context must be known.

### 2.1 Context decision

Context is established when no unresolved factor can change the unit's translation, or remaining uncertainty is shown to be irrelevant to the result. Required evidence depends on the game and string role; do not impose one document set or checklist on every project.

If uncertainty can change meaning, return to scene inspection, further extraction, or consumer-path analysis. Do not replace it with general knowledge or a plausible guess.

When narrative, route, or relationship information outside the local unit can change meaning, establish that dependency first. For narrative-heavy dialogue, obtain enough of the complete plot, branches, and major relationship changes to assess outside influence. Reconstruct the applicable route structure before translating units affected by late reveals, branch order, or relationship changes. Conversely, do not require complete story reconstruction for independent UI or scenes already shown not to depend on it.

### 2.2 Evidence scope

Use source extraction and the scenes in which the game actually consumes the text as the baseline. Consult external sources when they can decide unresolved meaning, order, speaker, or terminology scope. Do not search every source category ceremonially after the question is already decided.

- Primary sources such as official manuals, sites, and guides may establish setting, names, and functions. Official Korean or other localizations may supply source-backed wording candidates; verify title, revision, region, and series continuity before approval for this project.
- Guides and walkthroughs may reconstruct scene order, branches, characters, and system functions. They are not source text for exact wording or speaker intent.
- Prior localizations, fan patches, and reverse-engineering records provide interpretation candidates and technical clues. Compare them with source text and scenes in the target game because they may add, omit, or change viewpoint.

If external sources do not resolve the question, return to corpus reading, route execution, extraction, or reverse engineering. Finding a source does not approve an interpretation whose applicability is unknown.

When new evidence invalidates the established context, correct the current decision and reassess affected eligibility. Do not preserve a rejected interpretation alongside current facts as if both remained valid.

### 2.3 Logical order and storage order

Storage order need not equal play or scene order. Create a translator-facing logical view around scene, screen, and speaker relations when required for meaning, but do not turn that reordering into a changed extraction baseline or physical layout. Identical source text need not receive identical translation when the consumer scene or speaker differs.

### 2.4 Speaker and voice context

Include speaker, addressee, relationship, and scene evidence when they can change translation. Do not give inferred tone the same confidence as established control signals, screens, or dialogue order. If an inference can change the result, leave it for human judgment and do not promote the unit before resolution.

A single rule for a speaker need not apply across every relationship or scene. When differences change translation, define each approval's scope by the speaker-to-addressee relationship and narrative point. The project chooses the representation; §3 defines the approved scope and exceptions.

## 3. Approved terminology and voice

Maintain one authoritative record for approved names, system terms, recurring expressions, and speaker voice. Distinguish each decision, its applicability, evidence, and review state under `references/conventions/translation-artifacts.md` §1.1.

- Writers and reviewers use the same approved decisions and must not adopt silent local variants.
- Define separate scopes when one source term refers to different targets, speakers, or scenes; do not create unexplained variants for the same target.
- A new term, source conflict, or voice exception that can change output blocks the affected units from eligibility until approval.
- Series and prior-localization choices remain candidates until approved for this title and context.
- Before approving names, places, items, or system terms, check applicable official Korean wording or wording explicitly inherited from another edition or title. Adopt it only where source meaning and continuity match.
- Do not impose one source ranking or style priority on every project. State which sources govern the target and translation goal.

Automation may flag candidates against approved decisions but cannot approve a new wording or resolve a conflict. It may decide a violation only when applicability and allowed output are unambiguous. Word presence, inflection, omission, and adaptation in free prose require semantic review.

### 3.1 Translation work and agent assignment

Translation drafting permits creative judgment, but advancement to an eligible state is deliberately constrained because semantic errors can repeat across a finite corpus without violating mechanical checks. The controls below govern reliance, merge, review, and distribution eligibility; they do not prescribe one writing style or one way to discover a good expression.

Split work only at boundaries that preserve context. Free-prose drafting by another model or agent follows the evaluation, scope, and review conditions below. Do not outsource the full first draft to an unevaluated model or agent.

Before assigning substantial drafting to another model or agent, have that model or agent translate representative target samples and high-impact sentences under the same context, terminology, and voice conditions as production. A human evaluates accuracy, preservation of context and voice, and correction burden, then approves the assigned scope. Include dialogue, UI, sentences with names, context-sensitive sentences, and items with protected tokens or display constraints. Do not generate the full corpus under the label of evaluation, and do not replace human evaluation with an average score or agreement among models.

An evaluation applies only to the sampled text and conditions. Reevaluate the affected scope when the model or agent, supplied context, approved terminology, or voice guidance changes. A human-evaluated sample may remain as a working draft under the same baseline, but evaluation does not complete review or grant distribution eligibility. A model or agent that fails evaluation may still organize batches, serialize data, and inspect protected information; it must not draft or choose free prose.

Parallel drafting or review requires established decision context and independent review per unit. Split the corpus if it cannot satisfy those requirements as one unit; do not split it merely to create batches when it can satisfy them as one unit. Do not cut scene, speaker, or functional context, or make batches so large that a reviewer loses the relationships needed for judgment.

Draft free prose from context. Rule-based automation has the same limits: it may generate or choose prose only for fixed phrases whose applicability and output are already approved.

Provide writers and reviewers with a common input package containing:

- stable ID, source text, and protected raw bytes;
- reversible control tokens and forbidden raw tokens with established boundaries and argument widths;
- meaning established from the target consumer and the policy from `references/strategy/text-extraction.md` §4.4 for established tokens;
- scene, speaker, adjacent context, source consumption order, and any global narrative or route dependency that changes meaning;
- approved terms and voice guidance, including their applicability; and
- identified consumer conditions affecting length, layout, encoding, and other behavior, clearly distinguishing limits verified on the target from adopted design choices and current implementation state under §4.1.

Agent output may change translated text, rationale, questions, and proposal status. It must not recreate or normalize source identity, raw bytes, or protected tokens. A batch is a logical translation unit; it does not redefine source entry boundaries, order, or physical placement.

When a term, voice decision, or source interpretation changes across batches, revalidate earlier affected batches against the current approved decisions. Merge parallel results only when stable IDs and baselines match. Never resolve conflicts in entries, terminology, or protected information by last-writer-wins. Apply the state and protected-field semantics in `references/conventions/translation-artifacts.md`.

## 4. Protected information and consumer constraints

Separate translatable content from structure that must remain. Translation must not change source-controlled values such as raw bytes, identifiers, pointer evidence, and boundary information.

Assign each control token a policy based on how the target consumer uses it. For a token that changes meaning or execution, such as termination, event, or variable insertion, its preservation rule must cover order and arguments. Represent a token with unresolved meaning as forbidden raw data only when its boundary and argument width are established. Otherwise block the unit from translation and distribution eligibility. Apply `references/conventions/translation-artifacts.md` §3 to representation and `references/strategy/text-extraction.md` §4.4 to reversibility and policy.

Line, page, and wait tokens may move for Korean readability, page rhythm, and display constraints only after their consumer meaning and valid positions are established. Require equivalent state transitions under the token policy. Judge window, portrait, selection, input, voice, and event tokens by their own policies and verify changes through `references/strategy/build-and-verify.md` §5.

Derive length, width, rows, slots, encoding, and variable-insertion combinations from the real consumer, not language-wide defaults. A template that inserts a variable before a Korean particle makes the particle form depend on the inserted value's final consonant. Establish whether the consumer can select the form, whether per-value strings can be precomputed, or whether phrasing must avoid the dependency; one fixed form fails for part of the value population. Do not disguise a technical constraint violation as poor translation or resolve it automatically through semantic shortening. Choose among phrasing adjustment, established line or page controls, progression changes, and capacity changes according to the cause and effect.

For a finite display area, distinguish:

- **Observed source usage**: maximum visible width, row and page counts, and placement observed in the source.
- **Confirmed consumer capacity**: limits established by connecting stored width, height, or coordinates to consumer calculations.
- **Adopted display range**: the range selected for the Korean patch.

An observed maximum does not prove that the game permits no more. Do not merge limits from different renderers or window types.

When translated output exceeds observed source usage, do not shorten it automatically or fail it for that fact alone. Establish capacity through consumer code, display area, and runtime results, or change the adopted display range and verify it on the same consumer path. Human preference cannot waive protected information or established consumer constraints. If capacity remains unresolved and output exceeds source usage, return to consumer analysis and withhold distribution eligibility.

### 4.1 Product intent and constraint authority

Keep these roles distinct:

- **Product intent**: Within the declared scope, established source meaning and approved terminology, voice, and wording decisions define what the localized product should preserve. Candidate wording may still inform design through its intended meaning and resource requirements.
- **Established target constraint**: A limit supported by evidence from the applicable consumer, hardware, medium, or required product behavior, with its scope recorded. A limit observed only in the current implementation is not a target constraint.
- **Adopted design**: A selected display range, layout, encoding, font supply, reinsertion policy, renderer change, or other means of satisfying product intent under target constraints. Adoption makes the choice available for implementation and verification, not immutable.
- **Current implementation**: The code and artifact that currently realize an adopted design. It supplies evidence of behavior, feasibility, and change cost, but prior investment gives it no authority over product priorities.

Target constraints and protected-information rules may mechanically reject an option only within their established scope. Approved wording decisions govern semantic acceptability within their recorded applicability; changing one requires a wording decision, not an implementation-side substitution. A failure observed in the current implementation establishes only failure under that implementation and design; it does not by itself establish a translation defect. If the conflict belongs to the adopted design rather than a code defect, reopen the affected design choice. Prior work may materially affect cost and completion scope, but its existence alone must not narrow translation review options.

When current choices cannot preserve meaning or voice, compare plausible alternatives in design, wording or adaptation, and scope using current evidence. The agent establishes technical feasibility, cost, and affected scope; a human decides preference and semantic loss. Record a material choice and its reassessment conditions under `references/conventions/project-records.md` §1.1 so later work can use it within its recorded scope. Do not require every category of alternative, impose a fixed order between translation and engineering, or repeat an option already rejected with equivalent evidence.

## 5. Separate generation, review, and approval

Do not merge mechanically decidable violations with semantic judgment. Semantic or human approval cannot replace protected-information, state, encoding, or consumer checks, and passing mechanical checks cannot replace semantic review.

### 5.1 What automation may decide

| Class | Subject | Role of automation |
|---|---|---|
| Mechanically decidable rule | Protected fields and tokens; encoding and glyph mapping; confirmed width, height, row, page, and slot limits; approved wording whose applicability and required output are both unambiguous | Withhold distribution eligibility and block product builds under the release-candidate input policy on violation |
| Language heuristic | Dictionary presence, frequency, spelling and spacing, repeated phrases, LLM scores | Produce candidates with evidence and affected scope for human review; do not edit prose or decide fitness |
| Semantic judgment | Contextual meaning, naturalness, voice and relationship, adaptation, names, and wordplay | Produce options and evidence in independent review; a human decides |

Observed source maxima are not established consumer constraints by themselves. Dictionary presence does not prove correctness or error. Unresolved heuristic findings may remain review candidates; detection alone is not a confirmed defect and must not decide fitness automatically.

### 5.2 Rule-based bulk transformation of translated prose

An automated check may identify translation-defect candidates and affected scope. A batch transformation based on such a rule may edit translations only after a human explicitly approves the rule, the pre-transformation text, scope, and expected impact. Any change to them requires renewed approval. Approval of the transformation does not grant distribution eligibility; results must pass current source, context, terminology, voice, protected-information, and consumer checks. Route exceptions and high-impact semantic decisions to unit-level translation and review. Serialization, protected-information checks, and states derived from pass criteria do not require this approval when they do not change translation meaning.

### 5.3 High-impact semantic judgment

Judge semantic impact by whether an error would materially change player understanding, choice, progression, relationships, or authorial intent, not by a fixed ranking of quality categories. Record options and evidence for conflicts in source interpretation, new wording, adapted wordplay or cultural elements, and uncertain speaker identity or relationships. Human approval is required. One unresolved high-impact judgment blocks the affected unit from distribution eligibility.

### 5.4 Timing and invalidation of full-scope human review

The complete first draft is an input for measuring representation demand. Human review of the complete distribution scope must finish before release-candidate judgment. Before investing in review whose result depends on final glyph supply, render reachability, or layout, determine whether unresolved technical work can invalidate it. Delay only the affected review scope; independent wording, terminology, voice, or source-interpretation decisions may proceed when their evidence is stable.

For review that depends on those technical conditions, establish that:

- unique glyphs from the corpus and runtime insertions fit and can be supplied under the total-repertoire and active-working-set budgets in `references/strategy/font-strategy.md` §3;
- that supply reaches target render paths through `references/strategy/runtime-assets.md` §2 or equivalent evidence; and
- every finite display area can accept the first draft's maximum demand, or has a verified path to change the adopted display range under §4.

Check mapping and coverage mechanically across the complete corpus and runtime insertions. Judge distinct consumer paths with representative runtime evidence or existing equivalent evidence. One-glyph PoC or partial sample does not prove complete-corpus capacity. When a design fails, return to §4.1: establish plausible design, wording, and scope alternatives far enough to compare technical feasibility, semantic effect, cost, and affected paths. Follow the current recorded human decision if it covers the case; otherwise present the material tradeoff for human selection and record the result. Then verify the resulting resource demand and consumer paths again. A routine repair with limited scope that preserves the approved choice remains an implementation decision.

Human decisions about terminology, voice, or high-impact source interpretation may proceed whenever their evidence is stable. If glyph reduction changes meaning or voice, obtain approval at that point. If later review introduces new glyph or state-specific demand, reassess glyph budgets and consumer paths only for the affected scope.

### 5.5 Second review of a first draft

When a first draft made under §3.1 is considered for distribution eligibility, apply this decision chain:

```text
First draft → independent second review → options and evidence → human decision
                         └─ mechanical violations return to the relevant verification step
```

The second review must not assume the first draft's conclusion. In a separate review context, compare the source, approved decisions, speaker and scene evidence, and protected and consumer constraints again. When meaning, wording, or voice has alternatives, present options, evidence, impact, and a recommendation instead of silently overwriting the draft. Agreement between two outputs does not constitute quality approval. Human approval remains final, and affected units remain ineligible until then.

Apply §4.1 when candidate or approved wording conflicts with the selected design; the current implementation is not the baseline for semantic fitness.

Independence means a review that does not take the first draft's reasoning or conclusion as the answer. It does not require a specific model, service, or execution mechanism.

### 5.6 Separate wording, layout, presentation, and runtime decisions

Do not use one approval state for decisions with different evidence and invalidation rules. When layout or presentation requires human judgment, distinguish at least:

- **Wording selection**: the human-approved translated expression.
- **Explicit layout**: the selected text assigned to established windows, pages, lines, and control positions.
- **Mechanical validation**: protected information, terminology, glyph, encoding, control, and established geometry checks.
- **Presentation approval**: a human judgment of the exact text and layout shown by identified evidence.
- **Runtime verification**: the exact product artifact was consumed through the target renderer under recorded execution conditions.
- **Eligibility as a product build input**: all required upstream decisions and checks for the selected input remain valid.

A correct screen does not approve meaning, and approved wording does not establish layout or runtime consumption. Automatic layout is acceptable only when established consumer behavior and adopted layout rules determine the result. If geometry or page assignment remains unresolved, do not generate an inferred preview and present it for approval.

An explicit layout places the selected wording; it does not authorize rewriting it. If a presentation alternative uses a different expression, return the affected unit to wording selection, retain the prior decision and identity, and record the new scope-specific wording decision's relationship, applicability, rationale, semantic impact, and approval. Development may compare candidate wording and layouts under an explicit non-distribution input policy, but dependent approvals and release-candidate eligibility remain invalid until the selected wording decision is approved.

Bind each approval to its wording, layout, and evidence identities. Reassess only downstream decisions affected by an upstream change; unchanged independent decisions remain valid.

Label evidence by what produced it. Static reproduction uses identified assets, established geometry, and explicit layout but does not prove emulator execution or runtime residency. Runtime evidence obtained after a recorded state or call intervention uses the game's consumer but does not prove the bypassed route. Normal-play runtime evidence reaches the target through the declared play path on the exact product artifact but does not prove unobserved branches.

Record these decisions and evidence bindings through `references/conventions/project-records.md` §7.2. Human approval remains required only where meaning or presentation depends on judgment; mechanically derived layout and runtime facts remain technical checks.

## 6. Distribution eligibility

Promote only a scope satisfying all of these conditions:

1. No context uncertainty remains that can change translation.
2. Applicable terminology and voice match the approved decisions.
3. Protected tokens and actual consumer constraints pass.
4. High-impact semantic judgments are resolved with required human approval.
5. The first draft received an independent second review, with options and evidence presented for human review.
6. The entry passes the checks for use as a product build input in `references/conventions/translation-artifacts.md` §5.

An ineligible translation may be used only as an explicitly non-distributable input for development, technical verification, or a PoC. Output from a model or agent that failed §3.1 evaluation is not eligible for this exception. Such use neither grants distribution eligibility nor bypasses the conditions above; follow `references/conventions/translation-artifacts.md` §5 for identification and protection.

Return failed units to context research, terminology and voice approval, protected or consumer-constraint resolution, or semantic judgment according to the failed condition. Do not collapse these states into one generic "translation complete" label.
