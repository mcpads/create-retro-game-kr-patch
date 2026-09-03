# Debugging and issue resolution

Distinguish the target state, routes to it, and what each route can establish. Close a QA defect only after reproduction, causal diagnosis, correction, and regression verification. Choose tools and observation order from current hypotheses and the environment. When `SKILL.md` principle 2 applies, search `references/tips/README.md` by raw symptom and affected transition before adding another local exception; a case suggests an explanation but does not establish the cause. Record work under `references/conventions/project-records.md` and judge release readiness through `references/strategy/build-and-verify.md`.

## 1. Completion conditions

A defect fix is complete only when all of these hold:

- the baseline input, product artifact, runtime state, symptom, and pass/fail observation are repeatable;
- direct observations, cause hypotheses, and rejected conclusions remain distinct;
- discriminating evidence narrows the defect boundary;
- the first incorrect state and its propagation to the symptom are explained;
- the same reproduction passes after correcting the established cause within its necessary impact range; and
- affected adjacent paths and representative previously working paths pass regression checks.

Disappearance of a symptom does not establish a cause unless the change's effect on the causal chain is explained.

A reproduction must identify enough input, state, route, and observation to distinguish the same issue in another run. If results vary, include the distinguishable outcome range in the reproduction conditions. Preserve record semantics from `references/conventions/project-records.md`; the project chooses concrete fields.

## 2. Decision experiments

Define which decisions an experiment can change and which observations distinguish its outcomes. Its scope need not match one code edit: combine changes or instrumentation when one run remains interpretable, and split them when the combined outcome cannot guide the next action.

Static inspection and runtime observation are evidence modes, not pipeline stages or competing quotas. Classify the resulting work by the claim it establishes under `references/conventions/project-conventions.md` §5.3. Static inspection can enumerate structures, possible paths, affected populations, and invariants. Runtime observation can establish actual selection, state transitions, timing, and visible consumption. At each decision boundary, identify the remaining uncertainty and live explanations, then choose, alternate, or combine the modes according to which evidence can distinguish them at the lowest total cost. Stop extending one mode when another result would neither distinguish those explanations nor strengthen the applicable claim.

Treat the exact product artifact as an experimental baseline, not as a disposable response to each observation. A newly observed defect still requires issue closure, but does not by itself end the current observation. Keep the artifact fixed while remaining affected routes can still produce independent, interpretable evidence. Change it when the experiment's question is answered, or when the defect blocks or contaminates later observations or threatens artifact or data integrity. Before changing the baseline, account for the affected route population and unresolved observations.

### 2.1 Reaching a target state and intervening in state

First define the question, target state, and prerequisites that the evidence must preserve. When controls, progression, branches, or acquisition conditions are unknown, consult manuals, guides, walkthroughs, gameplay videos, or cheat references to narrow candidate routes. Check the region, revision, and prerequisites described by each source, then reverify them on the target product artifact. Reuse an already verified route under the same baseline and conditions. External material proposes entry routes and input sequences; it does not prove target state or code path.

Choose among qualifying routes using the equivalent-evidence cost rule in `SKILL.md` principle 1. Candidates include normal play, compatible saved states or input recordings, in-game entry points, verified cheats or state edits, and verified calls to state-transition routines. Normal play is not automatically stronger, and a faster intervention is not equivalent when it bypasses a prerequisite covered by the claim.

Before editing state or forcing a routine call, use static and dynamic evidence to establish the target or routine's entry conditions, arguments, call context, side effects, and return state. A plausible address or one desired result does not establish a valid intervention.

A state reached through intervention proves only the prerequisites preserved after intervention and the consumption that follows the target state. If caller selection, acquisition conditions, branch or event state, saves, loads, or other transitions are part of the claim, use normal play or a verified caller path. Record investigative interventions but keep them out of patch content and reproducible product build inputs.

### 2.2 Isolating a changed factor

Use removal or addition as causal evidence only when the suspected change can be toggled independently.

- If the symptom disappears only when the change is removed, promote that change to a candidate cause.
- If the symptom remains, reject only the single-cause hypothesis; assess interaction separately.
- Success of a reference implementation proves feasibility, not correctness of the current implementation. Compare outputs under the same input and conditions.

Divide a candidate set only when reproduction is stable on the same input and failure changes monotonically as the set is partitioned. If only combinations fail or intermediate states are undecidable, hold one factor constant or isolate semantic units.

When comparing working and failing runs, eliminate unrelated baseline differences first. Treat the earliest incorrect state causally linked to the symptom, not the first difference in a log, as the candidate cause.

An isolated result applies only to that layer. Success in compression, placement, loading, or rendering does not prove another layer. Reassess old experiments when the source or product artifact baseline changes.

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
- Working and failing runs begin from the same semantic state. Establish compatibility before reusing saved state from another product artifact.
- Do not generalize tolerance or defects of one environment to every distribution target.

Use `references/strategy/build-and-verify.md` §4 to set the verification scope for console, medium, loader, and execution-environment claims.

Use a HITL observation under `references/conventions/project-records.md` §6 when the remaining evidence depends on human perception, or when the required target environment is available only to the human. Difficulty or an unavailable observation method does not turn a technical conclusion into a human decision: establish another observation path or report the check as not run. Require that possible answers distinguish hypotheses and next actions, and keep the returned observation separate from technical interpretation and approval. If the response has no discriminating power, do not confirm a conclusion; narrow the requested observation and return it to the original causal chain. Automate a human-observed pattern only when the same input permits an objective result.

## 5. Fix and regression

Choose what to correct together from established causal and ownership boundaries, not discovery order. When several established defects share a causal chain, state lifetime, or violated contract and their combined effect remains attributable, correct them together within the necessary impact range. Separate unrelated cleanup, optimization, symptom masking, and any combination whose result would be ambiguous.

Recording another observation does not require a tooling build, product build, test run, or new runtime pass when no corresponding input or implementation changed. After a correction changes the product artifact, rerun the original reproductions and the affected route set on the new artifact; earlier runtime observations remain evidence about the old baseline and do not transfer automatically.

Retain regression checks proportional to impact and recurrence risk:

- Make calculable length, range, and mapping invariants product build checks.
- Preserve state or lifetime defects that are visible only at runtime as repeatable scenarios. Use human review only where the pass condition itself is not mechanically decidable.
- Bind preserved saved states and input recordings to compatible product artifacts and environments.
- Recheck paths sharing state resources, branches touched by the fix, and representative previously working paths.

Do not expand one issue's regression scope to every game feature.

## 6. Issue closure

Close an issue as fixed only through §1. To close it as original behavior, reproduce the same scene and input on a supported source image when possible. If that is impossible, record the comparison scope and remaining uncertainty. Similar appearance in another environment does not establish identical behavior.

Accepted limitation and out-of-scope closure are human product decisions. Before requesting one, establish the observed effect, affected population and consumer paths, feasible options, cost, risk, and claim impact, then record it under `references/conventions/project-records.md` §1.1. Preserve the earlier result against its original criterion: a later decision can change future scope, tolerance, or claims but cannot relabel that result as pass. Reassess the checks affected by the decision. Protected-information and technical gates still required by the selected scope and claims remain in force; without closure evidence or a covering human decision, the issue remains open.

Retain these safeguards against repeated misdiagnosis:

- Do not turn a hypothesis label into a fact label.
- Prefer evidence that distinguishes competing hypotheses over more observations consistent with one hypothesis.
- Treat local passes followed by failures in another consumer, or the need for a new separately maintained interpretation or exception for the same fact, as evidence that the current defect boundary may be wrong. Compare the causal chains and reconsider their shared premises and ownership. A shared contract is one possible repair only when the chains actually converge there.
- Claims that code is unreachable, space is unused, or one path is the actual state writer require complete coverage of the declared denominator.
- Reuse an earlier implementation only within its verified input, output, and state range.
- Preserve failed experiments and rejection evidence.
