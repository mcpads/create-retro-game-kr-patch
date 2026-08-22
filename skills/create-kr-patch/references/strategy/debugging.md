# Debugging and issue resolution

Before runtime verification, distinguish the target state, routes to that state, and what each route can establish. A QA defect may be closed only after reproduction, causal diagnosis, correction, and regression verification. Choose debuggers, emulators, and observation order from the current hypotheses and environment. When the reassessment conditions in `SKILL.md` apply, search `references/tips/README.md` from the raw symptom and affected transition before adding another local exception. A case may suggest another explanation; it does not establish the cause. Record evidence, decisions, and next actions under `references/conventions/project-records.md`; judge release readiness through `references/strategy/build-and-verify.md`.

## 1. Completion conditions

A defect fix is complete only when all of these hold:

- the baseline input, build, runtime state, symptom, and pass/fail observation are repeatable;
- direct observations, cause hypotheses, and rejected conclusions remain distinct;
- discriminating evidence narrows the defect boundary;
- the first incorrect state and its propagation to the symptom are explained;
- the same reproduction passes after changing only the established defect; and
- affected adjacent paths and representative previously working paths pass regression checks.

Disappearance of a symptom does not establish a cause unless the change's effect on the causal chain is explained.

A reproduction must identify enough input, state, route, and observation to distinguish the same issue in another run. If results vary, include the distinguishable outcome range in the reproduction conditions. Preserve record semantics from `references/conventions/project-records.md`; the project chooses concrete fields.

## 2. Decision experiments

Before an experiment, state which outcomes promote or reject each hypothesis. Narrow the question if no possible result would reduce the current choices.

### 2.1 Reaching a target state and intervening in state

First define the question, target state, and prerequisites that the evidence must preserve. When controls, progression, branches, or acquisition conditions are unknown, consult manuals, guides, walkthroughs, gameplay videos, or cheat references to narrow candidate routes. Check the region, revision, and prerequisites described by each source, then reverify them on the target build. Reuse an already verified route under the same baseline and conditions. External material proposes entry routes and input sequences; it does not prove target state or code path.

Choose a route that preserves the prerequisites relevant to the claim and supplies the needed evidence at an acceptable reproduction cost. Candidates include normal play, compatible saved states or input recordings, in-game entry points, verified cheats or state edits, and verified calls to state-transition routines. Normal play is not automatically stronger, and a faster intervention is not equivalent when it bypasses a prerequisite under test.

Before editing state or forcing a routine call, use static and dynamic evidence to establish the target or routine's entry conditions, arguments, call context, side effects, and return state. A plausible address or one desired result does not establish a valid intervention.

A state reached through intervention proves only the prerequisites preserved after intervention and the consumption that follows the target state. If caller selection, acquisition conditions, branch or event state, saves, loads, or other transitions are under test, use normal play or a verified caller path. Record investigative interventions but keep them out of patch content and reproducible build inputs.

### 2.2 Isolating a changed factor

Use removal or addition as causal evidence only when the suspected change can be toggled independently.

- If the symptom disappears only when the change is removed, promote that change to a cause candidate.
- If the symptom remains, reject only the single-cause hypothesis; assess interaction separately.
- Success of a reference implementation proves feasibility, not correctness of the current implementation. Compare outputs under the same input and conditions.

Divide a candidate set only when reproduction is stable on the same input and failure changes monotonically as the set is partitioned. If only combinations fail or intermediate states are undecidable, hold one factor constant or isolate semantic units.

When comparing working and failing runs, eliminate unrelated baseline differences first. Treat the earliest incorrect state causally linked to the symptom, not the first difference in a log, as the cause candidate.

An isolated result applies only to that layer. Success in compression, placement, loading, or rendering does not prove another layer. Reassess old experiments when the source or build baseline changes.

## 3. Causal chain

Cause confirmation must connect:

```
faulty input, instruction, or rule -> first incorrect state -> propagation and lifetime -> observed failure
```

A screen, log line, crash location, or last writer may be only the end of the chain. Find the first divergence along the storage → lookup → load or transform → residency → consumption chain from `references/strategy/runtime-assets.md`, then explain why the fix breaks that causal path.

Symptom names do not determine cause identity: identical names may have distinct causes, while different names may emerge from one shared faulty state or lifetime. Rank candidates by how well they explain current observations and the chain, then choose an experiment that distinguishes the relevant hypotheses given the available evidence and reproduction cost.

## 4. Observation evidence

Collect only values and events that distinguish current hypotheses. The observation method and environment must also satisfy these conditions:

- Address translation, bank or overlay state, event timing, and input meaning match the real consumer path.
- Absence of an event is negative evidence only after proving that the method records that event on the path.
- Working and failing runs begin from the same semantic state. Establish compatibility before reusing saved state from another build.
- Do not generalize tolerance or defects of one environment to every distribution target.

Use `references/strategy/build-and-verify.md` §4 to set the verification scope for console, medium, loader, and execution-environment claims.

When mechanical evidence cannot decide, request a HITL observation under `references/conventions/project-records.md` §6, and require that its possible answers distinguish hypotheses and next actions. If the response has no discriminating power, do not confirm a conclusion; narrow the requested observation and return it to the original causal chain. Automate a human-observed pattern only when the same input permits an objective result.

## 5. Fix and regression

Limit a fix to the established defect and necessary impact range. Do not mix unrelated cleanup, optimization, or symptom-masking changes into the same decision experiment.

After the fix, rerun the original reproduction and retain regression checks proportional to impact and recurrence risk:

- Make calculable length, range, and mapping invariants build checks.
- Preserve state or lifetime defects that are visible only at runtime as repeatable scenarios. Use human review only where the pass condition itself is not mechanically decidable.
- Bind preserved saved states and input recordings to compatible builds and environments.
- Recheck paths sharing state resources, branches touched by the fix, and representative previously working paths.

Do not expand one issue's regression scope to every game feature.

## 6. Issue closure

Close an issue as fixed only through §1. To close it as original behavior, reproduce the same scene and input on a supported source build when possible. If that is impossible, record the comparison scope and remaining uncertainty. Similar appearance in another environment does not establish identical behavior.

Accepted limitation and out-of-scope closure are human product, quality, support, or scope decisions. Before requesting one, the agent establishes the observed effect, affected population and consumer paths, feasible technical options, cost and risk, and impact on product claims. Record the decision under `references/conventions/project-records.md` §1.1 and link it from the issue record. Preserve the observed result against the criterion used when it was obtained; a later decision does not relabel that result as pass. The decision may prospectively change a relevant quality tolerance, supported scope, or product claim. Record that change, retain its effect on earlier claims, and rerun the checks required by the new decision. Protected-information, build, artifact-integrity, and runtime conditions still required by the selected scope and claims cannot be waived; change the implementation or design, exclude the affected scope, or narrow the claim. Without fixed or original-behavior evidence or a recorded human decision that covers the issue, the issue remains open.

Retain these safeguards against repeated misdiagnosis:

- Do not turn a hypothesis label into a fact label.
- Prefer evidence that distinguishes competing hypotheses over more observations consistent with one hypothesis.
- Treat local passes followed by failures in another consumer, or the need for a new separately maintained interpretation or exception for the same fact, as evidence that the current defect boundary may be wrong. Compare the causal chains and reconsider their shared premises and ownership. A shared contract is one possible repair only when the chains actually converge there.
- Claims that code is unreachable, space is unused, or one path is the actual state writer require complete coverage of the declared denominator.
- Reuse an earlier implementation only within its verified input, output, and state range.
- Preserve failed experiments and rejection evidence.
