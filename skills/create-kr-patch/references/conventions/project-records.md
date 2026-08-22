# Project record conventions

Record human strategic decisions, initial surveys, PoCs, graphics-text catalogs, HITL observations, and QA issues while keeping evidence, decisions, and next actions distinct. Retain an equivalent existing record system. Field and state names below are optional examples; paths, serialization, and tools are not fixed.

Preserve source and translated text, control codes, and review states under `references/conventions/translation-artifacts.md`. Follow `references/conventions/project-conventions.md` for repository layout and source or derived assets.

## Contents

1. Common record rules
   - Human strategic decisions
2. Record placement
3. Initial survey records
4. PoC decision records
5. Graphics-text catalog
6. HITL observation requests
7. QA rounds and issues
8. Record validation

## 1. Common record rules

Regardless of format, distinguish:

- **Scope and baseline**: Identify the source, build, screen, asset, and code path represented.
- **Evidence binding**: Bind runtime and observation evidence to the exact input, artifact, and environment that produced it. A mutable path or state name does not establish content identity.
- **Observation and interpretation**: Separate direct observation, unverified hypothesis, and conclusion established through isolation.
- **Evidence location**: Link hashes, dumps, screenshots, traces, disassembly, and reproduction steps needed to reassess a decision.
- **Decision**: Distinguish pass, fail, and unresolved; retain both criteria and observed result.
- **Decision authority**: Distinguish an evidence-grounded technical conclusion, an ordinary implementation choice that preserves approved intent, and a human choice about product direction, scope, quality, support, acceptable loss, or investment. Do not use one class to stand in for another.
- **Claim relation**: Credit a result only to the larger decision or completion condition it directly strengthens. Keep visible whether the current cumulative build incorporates it and which relevant obligations remain unresolved. A difficult, useful, or locally successful result does not establish a broader claim merely because it was achieved. Projects may express this in their existing status vocabulary.
- **Adoption and reassessment**: When an established conclusion becomes part of the current specification, identify the source and consumer scope to which it applies and the changes, mismatches, or contrary evidence that would reopen the analysis. Repeated consumption alone does not invalidate it.
- **Human approval**: Where a decision requires it, identify the approving human, the exact scope and baseline approved, and the change that invalidates it.
- **Next action**: On failure identify the rejected assumption; when unresolved identify the observation that distinguishes the current possibilities; on pass identify promoted knowledge or the next step.
- **State intervention**: For a target state created by a cheat, state edit, or forced routine call, identify the exact baseline, pre-intervention state, edited target and value or call conditions and arguments, bypassed play and code path, post-intervention state, and the claims the intervention does and does not support. Do not mix intervention with patch changes or evidence of normal-play reachability.

Collection entries need stable IDs that survive reordering and file moves. Do not use an address, offset, or filename alone as identity; separate the logical ID from the current physical location. Refer to one authoritative record by ID or project-relative path instead of copying the same fact.

### 1.1 Human strategic decisions

Record a human decision when alternatives materially differ in product or localization scope, quality target, supported targets, accepted semantic or visual loss, accepted limitation, or technical investment and redesign. Do not create an approval step for a routine, reversible implementation choice with limited scope that preserves an already approved intent.

The agent first investigates far enough to frame a useful decision rather than transferring technical diagnosis to the human. Record the following information in an existing equivalent decision system or a current strategic-decision register:

| Example field | Meaning |
|---|---|
| `decision_id` | Stable identity used by dependent designs, records, and claims |
| `question` | The material choice and why current evidence requires it |
| `scope` | Product, population, consumer paths, revisions, and support claims to which the decision applies |
| `values` | Quality target, semantic or visual priorities, accepted loss, acceptable cost or time investment, and other human criteria that distinguish options |
| `options` | Feasible choices, including continued investigation when useful, with technical evidence, cost, risk, affected scope, and claim limits |
| `recommendation` | Agent recommendation and the evidence-sensitive reason for it |
| `human_decision` | Selected, deferred, or rejected choice, deciding human, rationale, and decision baseline |
| `effects` | Adopted design constraints, affected work, accepted limitations, and permitted claims; this is not proof that technical gates pass |
| `reassessment` | New evidence, changed intent, failed assumption, cost change, or scope change that requires the choice to be reviewed |
| `state` | Proposed, adopted, review required, or superseded, with stable links between replaced decisions |

The following are record transitions, not a required order for investigation or discussion. Evidence may return a decision to an earlier state:

1. **Frame**: Connect the unresolved boundary to a material human value choice. If one ordinary technical option clearly preserves the current decision, implement it instead of asking again.
2. **Prepare**: Establish feasible options and enough evidence to compare their effect, cost, risk, scope, and claim limits. State remaining uncertainty and a recommendation.
3. **Decide**: Let the human select, defer, or reject the material tradeoff. Record the exact scope and reasoning; do not infer approval from silence or prior investment.
4. **Apply**: Let an adopted decision guide later investigation and implementation within its scope. It narrows which outcomes are valuable, but it neither proves target facts nor waives protected-information, build, or runtime gates.
5. **Reassess**: Reopen only when a recorded trigger occurs or new evidence materially changes the comparison. Mark the current decision as requiring review, present the delta and affected downstream choices, and preserve superseded lineage rather than silently rewriting the old rationale.

When a material decision is made in a conversation, review, or issue, preserve it in the authoritative decision record before dependent work relies on it. Later agents treat applicable adopted decisions as part of the current baseline, cite them when they shape work, and update their state in the same change that reopens or supersedes them. Communication channels may link to the record but do not become competing authorities.

An adopted decision has authority only within its recorded product scope; it is not a universal strategy. A downstream agent must cite the relevant decision when it changes prioritization, design, accepted limitation, or a release claim, and must keep contrary technical evidence visible.

## 2. Record placement

Prefer existing repository locations and links with the same responsibility. Any new arrangement must retain these properties:

- Each kind of current record has one authoritative location, with guidance pointing to it.
- Current conclusions and active decisions remain distinct from completed or abandoned plans.
- Stable IDs and relationships survive splitting or merging records.
- When large, copyrighted, or environment-specific evidence remains outside the repository, committed records retain its identity and regeneration or reproduction conditions.

When work may outlive the current agent context, the authoritative current records must make the active work reconstructible without a conversation transcript. Keep visible the exact baseline and cumulative artifact, the completion condition or decisive unresolved boundary, the last established result, live and rejected explanations, the next observation or action that can distinguish them, the applicable adopted human decisions, and any pending human decision together with work that can continue without it. These facts may remain in existing records when one current entry links them.

The project chooses serialization and placement from its structure, review method, and machine-readability needs. Do not migrate equivalent existing records only to change format.

Apply the vocabulary and ownership boundary in `references/conventions/project-conventions.md` §1. Record confidence and workflow state inside the authoritative record or its stable links rather than expressing them through alternate locations or synonymous record classes. Establishing or rejecting a conclusion does not by itself justify moving or copying its record. When a conclusion becomes adopted build input, update the existing specification owner or create an explicitly linked build-owned projection; retain the investigation evidence as its source rather than turning either representation into a second editable authority. Preserve logical identity and lineage across these changes. Any other separate physical location requires a distinct record responsibility or a durable retention, access, rights, environment, or size boundary, and the authoritative record must retain the identity and relationship.

If records that claim to be current disagree about the baseline, artifact, entry point, adopted conclusion, or issue state, do not choose one by recency or convenience. Treat the current state as unresolved, identify the authoritative record, and change or demote the other current claims in the same update. Preserve superseded observations as history without leaving them as competing current instructions.

On resumption, verify the recorded baseline and applicable adopted decisions, then reconstruct the active claim and rejection evidence before another attempt. Do not repeat discovery merely because the prior agent context is unavailable. Keep chronological attempts in evidence or journal records rather than accumulating competing summaries that claim to be current.

## 3. Initial survey records

### 3.1 Architecture record

Keep only currently verified structure in the main record and separate it from a chronological experiment log. This table shows required information and optional field names:

| Example field | Meaning |
|---|---|
| `scope` | Target source revision and investigated media, files, and code paths |
| `confirmed` | Structure established by measurement or runtime tracing, with evidence references |
| `hypotheses` | Remaining hypotheses, distinguishing observations, and priority |
| `memory_map` | Established address-space, bank, and file-offset conversions |
| `control_flow` | Calls, dispatch, and data flow needed for the declared investigation scope |
| `unknowns` | Unknowns blocking completion or design and the next evidence that distinguishes them |

A project that needs one render path does not need a complete call graph. When a graph is needed, record node and edge meaning, hypothesis or confirmed state, and evidence location.

### 3.2 Text map

Record samples and volume findings needed for initial decisions in machine-readable form. A complete-extraction claim expands the record to the full declared denominator. Distinguish:

| Example field | Meaning |
|---|---|
| `asset_id` | Stable ID for a text region or table |
| `source` | Container, file, offset, size, and source hash |
| `boundaries` | Entry extent, alignment, terminator, and padding |
| `pointers` | Pointer-table location, width, base, duplicates, and null meaning |
| `encoding` | Character mapping and evidence |
| `controls` | Control codes, argument widths, state effects, and hypothesis or confirmed status |
| `population` | Enumeration by target kind and consumer, resolved/excluded/unresolved counts, remaining range, and stopping condition |
| `volume` | Measurement unit, value, basis, exact/lower-bound/estimate status, and handling of shared or duplicate members |
| `sample` | Raw bytes and reversible decoded sample |
| `roundtrip` | Reassembly result and byte-identity decision |

### 3.3 Feasibility assessment

For each risk, retain a `risk_id`, scope, observation evidence, impact, possible workaround, current decision, and next check. When glyph, encoding, storage, active memory, hook, compression, or runtime-asset boundaries can be quantified, retain measurements and limits. Conclude technical feasibility, recommend whether to proceed, proceed conditionally, or redesign, and identify remaining uncertainty that can overturn the recommendation. A material product, quality, support, scope, or investment choice follows §1.1.

## 4. PoC decision records

Keep each PoC decision independently identifiable. Bind the completion-critical risk and hypothesis to its representative target, baseline, intervention, predefined outcomes, observation, and evidence. Preserve separately what the result proved, what it did not prove, how it affects the cumulative build or larger decision, which assumptions and temporary artifacts were discarded, and what remains.

Manual hex edits, temporary offsets, and one-shot scripts may remain as evidence of the result but must not be labeled repeated-build inputs.

## 5. Graphics-text catalog

Catalog text blocks rather than texture files. When one texture contains several labels, record each label separately.

| Example field | Meaning |
|---|---|
| `block_id` | Stable text-block ID |
| `source` | Container path or index and, when needed, byte start, size, and source hash |
| `bounds` | Measured pixel `x`, `y`, `w`, and `h` |
| `format` | Only values needed for actual interpretation: pixel encoding, address calculation, palette, interval, cell, or tile structure |
| `text` | Source transcription and approved translation |
| `style` | Stroke, color, outline, shadow, cell, and row metrics |
| `catalog_state` | Current stage such as uninvestigated, no text, unresolved, found, restored, laid out, or verified |
| `evidence` | Crop, screenshot, mask, clean-plate hash, and in-game verification references |

Projects may rename states, but must distinguish uninvestigated, investigated with no text, and unresolved. Maintain bounding boxes in one field because they drive restoration and layout and also form the out-of-bounds pixel mask. Store percentage coordinates with source image dimensions or normalize them to pixels.

## 6. HITL observation requests

Keep each request small enough for one human observation session. Bind it to the exact source, build, environment, configuration, starting state, reproduction input, and observation point. State what to capture and how each possible answer changes the decision or next action; retain the actual response and whether it confirmed or rejected a hypothesis, showed the question to be irrelevant, or left it unresolved.

A human response supplies an observation, not technical interpretation or product approval. The agent remains responsible for the technical interpretation and next hypothesis; incomplete evidence remains unresolved. A product-value choice follows §1.1, while semantic or presentation judgment follows the applicable workflow and §7.2. Do not hide either inside an observation request.

An index contains only ID, target hypothesis, current decision, and response location. Do not duplicate request bodies in the index.

## 7. QA rounds and issues

### 7.1 QA rounds

A QA round binds the baseline build, verification scope, issues, coverage, and closure. Distinguish build identity, target environments and scope, automated results, required-path coverage, linked issues, closure decision, and remaining distribution blockers.

For each text display region, record region ID, renderer and box scope, width calculation, line and page limits, state effects of line and page controls, and violation severity. Keep observed source usage, confirmed consumer capacity, and adopted display range distinct under `references/strategy/translation-workflow.md` §4. Apply `references/strategy/build-and-verify.md` §5 to presentation and interaction. For the applicable states, record the state matrix, starting state and input sequence, reference points and tolerances for progression, voice, and events, and the visual baseline and comparison conditions. Measure concrete values on the target game.

### 7.2 Translation, layout, and presentation review

When a project reviews translated presentation, keep wording, layout, mechanical checks, presentation judgment, runtime evidence, and build eligibility as separate facts under `references/strategy/translation-workflow.md` §5.6. Preserve an equivalent existing record system; it may record:

| Example field | Meaning |
|---|---|
| `unit_id` | Stable translation or display unit |
| `wording_decision` | Selected text identity, approval scope, approver, and the baseline that would invalidate it |
| `layout_specification` | Selected-text hash, source-text and control-topology identities, geometry identity, and explicit window, page, and line assignment in display order |
| `mechanical_result` | Protected-information, terminology, glyph, encoding, control, and geometry results from the authoritative checks |
| `evidence_class` | Static reproduction, runtime after intervention, or normal-play runtime |
| `evidence_identity` | Exact build, layout, environment, intervention when applicable, capture or trace identity, and content hash |
| `presentation_decision` | Approved, revision required, or evidence insufficient, with human rationale when judgment is required |
| `runtime_result` | Consumer path, reached state, observed output, and the claims the evidence does and does not support |
| `eligibility` | Derived build-input decision and the failed upstream condition when ineligible |

A browser selection, screenshot, local cache, or mutable preview path is not the approval record. Store the decision in the project's versioned source of truth and retain derivative evidence outside the repository when required by rights, size, or environment constraints, while keeping its identity and reproduction conditions in the record.

Do not label static reproduction as in-game or runtime evidence. Do not create a static reproduction from inferred line or page assignment when the target requires unresolved human layout. When automatic layout follows a complete deterministic consumer model, record that model and its mechanical result rather than fabricating a human layout decision.

### 7.3 Individual issues

Keep an issue stable across QA rounds and title it by the symptom rather than an evidence filename. Preserve the reproduced baseline, prior state and input, expected and observed results, evidence, live and rejected hypotheses, and decision experiments. A fixed issue additionally connects the established faulty input to the first incorrect state and observed failure, the corrective change and its impact range, and pre-fix failure to post-fix regression evidence. Original-behavior closure cites the source comparison and remaining uncertainty; accepted limitations and out-of-scope closure cite the recorded human decision that covers the issue, affected scope, rationale, and claim impact. Link reusable start state only when it materially reduces reproduction cost.

## 8. Record validation

Builds or dedicated checks verify machine-readable records:

- Required IDs are present and unique.
- Referenced project-relative paths and item IDs exist.
- Hypotheses and confirmed conclusions do not share one field.
- Pass, fail, and unresolved decisions include evidence and next action.
- Closed issues include a reproduction baseline, closure evidence or a recorded human decision that covers the issue, affected scope, and claim impact.
- Adopted human strategic decisions have scope, options, rationale, effects, and reassessment conditions; at most one decision is current for the same identity and applicability.
- Resolved plus excluded graphics-text catalog members match the declared denominator without hidden unresolved members.
- Volume records distinguish exact, lower bound, and estimate and state how unresolved scope affects workload and completion.

A Markdown-only project may capture this information through tables and links. JSON, YAML, or a database may add schema validation, but serialization itself is not a strategy decision.
