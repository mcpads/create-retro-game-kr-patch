# Project record conventions

Record initial surveys, PoCs, graphics-text catalogs, HITL observations, and QA issues while keeping evidence, decisions, and next actions distinct. Retain an equivalent existing record system. Field and state names below are optional examples; paths, serialization, and tools are not fixed.

Preserve source and translated text, control codes, and review states under `references/conventions/translation-artifacts.md`. Follow `references/conventions/project-conventions.md` for repository layout and source or derived assets.

## Contents

1. Common record rules
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
- **Human approval**: Where a decision requires it, identify the approving human, the exact scope and version approved, and the change that invalidates it.
- **Next action**: On failure identify the rejected assumption; when unresolved identify the observation that distinguishes the current possibilities; on pass identify promoted knowledge or the next step.
- **State intervention**: For a target state created by a cheat, state edit, or forced routine call, identify exact baseline, pre-intervention state, edited target and value or call conditions and arguments, bypassed play and code path, post-intervention state, and proved and unproved scope. Do not mix intervention with patch changes or evidence of normal-play reachability.

Collection entries need stable IDs that survive reorder and file moves. Do not use address, offset, or filename alone as identity; separate logical ID from current physical location. Refer to one owning record by ID or project-relative path instead of copying the same fact.

## 2. Record placement

Prefer existing repository locations and links with the same responsibility. Any new arrangement must retain these properties:

- One current record kind is maintained in one place, with guidance pointing to it.
- Current conclusions and active decisions remain distinct from completed or abandoned plans.
- Stable IDs and relationships survive splitting or merging records.
- When large, copyrighted, or environment-specific evidence remains outside the repository, committed records retain its identity and regeneration or reproduction conditions.

The project chooses serialization and placement from its structure, review method, and machine-readability needs. Do not migrate equivalent existing records only to change format.

## 3. Initial survey records

### 3.1 Architecture record

Keep only currently verified structure in the main record and separate it from a chronological experiment log. This table shows required meanings and optional field names:

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

For each risk, retain a `risk_id`, scope, observation evidence, impact, possible workaround, current decision, and next check. When glyph, encoding, storage, active memory, hook, compression, or runtime-asset boundaries can be quantified, retain measurements and limits. Conclude whether to proceed, proceed conditionally, or redesign, and identify remaining uncertainty that can overturn the choice.

## 4. PoC decision records

Keep each PoC decision as one record independent of other decisions. Existing record structure decides file boundaries. Optional fields include:

| Example field | Meaning |
|---|---|
| `poc_id` | Stable ID linked to the strategy PoC |
| `risk_trigger` | Completion-critical or design-changing risk and why the decision is early |
| `hypothesis` | Assumption distinguished by the experiment |
| `target` | Representative screen, text, glyph, or code path and selection basis |
| `criteria` | Pass, fail, and unresolved criteria plus next action for each |
| `procedure` | Minimal reproducible intervention and baseline build |
| `result` | Observation, evidence location, and decision |
| `proved` | Established result adopted into implementation after pass |
| `not_proved` | Scope that the experiment cannot generalize to |
| `discarded` | Rejected assumptions and temporary artifacts excluded from implementation |
| `next` | Follow-up or skipped verification with reason |

Manual hex edits, temporary offsets, and one-shot scripts may remain as result evidence but must not be labeled repeated-build inputs.

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
| `priority` | Work order based on exposure and importance |
| `catalog_state` | Current stage such as uninvestigated, no text, unresolved, found, restored, laid out, or verified |
| `evidence` | Crop, screenshot, mask, clean-plate hash, and in-game verification references |

Projects may rename states, but must distinguish uninvestigated, investigated with no text, and unresolved. Maintain bounding boxes in one field because they drive restoration and layout and also form the out-of-bounds pixel mask. Store percentage coordinates with source image dimensions or normalize them to pixels.

## 6. HITL observation requests

One request should fit one human observation session.

| Example field | Meaning |
|---|---|
| `request_id` | Stable ID |
| `reproduction_baseline` | Source, build artifact, execution environment, and configuration identity |
| `setup` | Starting state and short input or reproduction procedure |
| `observation_point` | Breakpoint, screen, frame, or other observation point |
| `capture` | Registers, memory, trace, or screenshot to read |
| `branches` | Decision and next action for each possible observation |
| `response` | Actual values, capture references, and observer notes |
| `outcome` | Confirmed, rejected, irrelevant, or unresolved |

An index contains only ID, target hypothesis, current decision, and response location. Do not duplicate request bodies in the index.

## 7. QA rounds and issues

### 7.1 QA rounds

A round binds baseline build, verification scope, issues, coverage, and closure. Distinguish build identity, target environments and scope, automated results, required-path coverage, linked issues, closure decision, and remaining distribution blockers.

For each text display region, record region ID, renderer and box scope, width calculation, line and page limits, state effects of line and page controls, and violation severity. Keep observed source usage, confirmed consumer capacity, and adopted display range distinct under `references/strategy/translation-workflow.md` §4. Apply `references/strategy/build-and-verify.md` §5 to presentation and interaction. For the applicable states, record the state matrix, starting state and input sequence, reference points and tolerances for progression, voice, and events, and the visual baseline and comparison conditions. Measure concrete values on the target game.

### 7.2 Individual issues

| Example field | Meaning |
|---|---|
| `issue_id` | Stable ID across rounds |
| `summary` | Short symptom-centered title |
| `baseline` | Reproduced build and environment |
| `reproduction` | Prior state, short input, expected result, and observed result |
| `evidence` | Screenshot, dump, and trace references |
| `hypotheses` | Unresolved causes and decision experiments |
| `rejected` | Rejected hypotheses and evidence |
| `mechanism` | Established faulty input -> first incorrect state -> propagation -> observed failure chain |
| `change` | Fix to the established defect and impact range |
| `regression` | Pre-fix failure, post-fix pass, and a reference to the added regression check |
| `issue_state` | Open, investigating, recheck needed, fixed, not a bug, or out of scope |

Do not use an evidence filename or location as issue title or state. An initial report distinguishes at least baseline, reproduction context, expected and observed results, and decision evidence. Link reusable start state only when it materially reduces reproduction cost.

## 8. Record validation

Builds or dedicated checks verify machine-readable records:

- Required IDs are present and unique.
- Referenced project-relative paths and item IDs exist.
- Hypotheses and confirmed conclusions do not share one field.
- Pass, fail, and unresolved decisions include evidence and next action.
- Closed issues include reproduction baseline and closure evidence.
- Resolved plus excluded graphics-text catalog members match the declared denominator without hidden unresolved members.
- Volume records distinguish exact, lower bound, and estimate and state how unresolved scope affects workload and completion.

A Markdown-only project may express these meanings through tables and links. JSON, YAML, or a database may add schema validation, but serialization itself is not a strategy decision.
