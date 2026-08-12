# Initial survey

Reduce uncertainty enough to decide feasibility and the next implementation boundary. Prioritize conditions whose failure would block completion or force redesign. Compare experiment cost only among methods that preserve the same condition, prerequisites, and proof scope.

## 1. Questions to answer before completion

1. **Input boundary**: Which revision, representation, and modification unit does the project support?
2. **Text kind**: Which target text is runtime text, baked graphics, or another representation?
3. **Storage and consumer**: Where is it stored, how is it selected, and which consumer gives it meaning?
4. **Glyph path**: How does a code reach glyph data and pixels?
5. **Intervention boundary**: Is the change data replacement, relocation or new assets, code modification, or a combination?
6. **Evidence**: Which uncertainty needs a PoC, and what equivalent evidence already exists?
7. **Initial volume**: Is the target population exact, a lower bound, an estimate, or unresolved?
8. **Display budget**: Which values describe observed source usage, and which are confirmed consumer capacity?

Treat risks such as encoding space, glyph capacity, name entry, relocation, compression, and distinct consumer paths as conditional when they remain independent of basic visibility. Apply `references/strategy/poc.md` to their proof scope and outcomes, and `references/strategy/graphics-text.md` when distribution text is stored as graphics pixels. Do not add unrelated battle, sound, or general graphics investigation unless it is a direct prerequisite for localization.

## 2. Follow dependency boundaries instead of a fixed sequence

Media, logical files or blocks, code consumers, fonts, and text structure are possible investigation categories, not a required sequence. Begin from storage or consumption according to available evidence. Work on the unresolved completion-critical condition, not merely the easiest local success.

For each result, ask whether it changes:

- feasibility or the required workaround;
- the representative or conditional PoC target;
- replacement versus code intervention;
- extraction, reinsertion, compression, or runtime verification;
- supported revision or distribution form; or
- the priority of remaining risks.

Defer investigation that changes none of these. Establish another category's boundary first only when it is a real prerequisite.

### 2.1 Input and rebuild boundary

- Identify each supported revision with a hash and the structural fingerprints the build requires.
- For containers or filesystems, establish an unchanged rebuild round trip under `references/conventions/project-conventions.md` §5.1 before editing.
- For direct patching, establish expected source bytes and the complete post-change range.
- Investigate filesystem, track, and sector details only when the build reads or rewrites them.
- Do not make a release claim while the supported input remains unresolved.

### 2.2 Storage structure and consumer meaning

Byte patterns, search results, statistics, and prior-patch diffs produce candidates. Establish encoding, pointers, terminators, compression, and graphics interpretation through the actual consumer or independent equivalent runtime evidence.

Determine pointer width, byte order, base, and coordinate system from the consumer. CPU identity alone does not establish them. An unresolved control token may remain a reversible raw token when its boundary and argument width are known; do not invent semantics.

A candidate address that merely falls within a plausible range does not establish a pointer structure.

### 2.3 Glyph and render path

- Connect the glyph source to a screen consumer.
- When replacing an existing glyph in the same format changes the target screen as predicted, it proves that the replacement path can reuse that consumer.
- A new encoding, hook, dynamic supplier, or relocation must state the solved constraint and the new consumption conditions it introduces.
- Derive cell and glyph demand from the target corpus and actual budgets.
- When source text for a finite display area can be enumerated without added assumptions, measure applicable visible width, rows, pages, and start/end behavior at the consumer or window path, including control tokens and variable insertions. A stored source width or height is evidence of capacity only after establishing that the consumer uses it. Use `references/strategy/translation-workflow.md` §4 to distinguish observed source usage from confirmed consumer capacity.

### 2.4 Capacity and runtime assets

Compare capacity with the actual required repertoire, text growth, buffers, and transfers. Do not begin with relocation or dynamic mapping merely because capacity might be insufficient; first establish the limiting resource.

When a change triggers `references/strategy/runtime-assets.md` §1, assess the links in `references/strategy/runtime-assets.md` §2.

### 2.5 Population and initial volume

Work backward from declared screen and function consumers, selection branches, and indexes to enumerate files and entries. Do not grow the target list one runtime discovery at a time.

- Statically enumerate a finite population when possible.
- Partition it by shared format, selection, load or transform, consumer, and state lifetime.
- A shared extension, directory, or one successful run does not prove a shared consumer path.
- Establish membership from references, dispatchers, read code, or validated structure.
- If static scope remains unresolved, report a lower bound and the unresolved region; narrow exceptions rather than claiming completeness.
- Use `references/strategy/runtime-assets.md` §2 to distinguish one common runtime link from exceptions.
- Survey early text volume through `references/strategy/text-extraction.md` §1.5. A representative PoC may precede expensive enumeration when the lower bound and unresolved region are explicit.
- Candidate byte or string count does not equal translation workload.

## 3. Promoting hypotheses to facts

Keep confirmed facts, candidates, and rejected candidates distinct.

- Establish stored meaning from a consumer, dispatcher, reference structure, or independent equivalent evidence.
- Connect render input, intermediate representation, and screen output.
- A self round trip proves implementation agreement, not game compatibility.
- A completeness claim requires both a denominator and coverage of its consumer paths.
- Conflicting evidence keeps a claim provisional.
- One successful title or item does not establish a platform rule.

### 3.1 Fixed revision and unresolved population

For a fixed revision and a proven consumer, treat hook sites, original instructions, table entries, and pointer storage as revision specification. Use explicit constants and expected source bytes instead of runtime heuristics.

Derive values that depend on build output, such as end addresses, branch displacements, file sizes, and checksums. A fixed specification does not mean hard-coding derived outputs.

A finite list becomes complete only after establishing its denominator. When population detection remains necessary, fail the build if the parser or detector cannot establish scope. Do not silently repair disagreement between heuristics and specification; reassess revision, denominator, and false positives.

Store pointer findings under `references/conventions/data-formats.md` §4.

## 4. Prior patches and lineage

Use prior patches as candidate maps and risk evidence, not authority. Choose references by matching bottleneck and representation rather than language label alone. A Chinese or other CJK patch may expose non-Latin code-space, glyph, and budget constraints more directly than a Latin-variable-width patch, but remeasure the Korean corpus, cells, and spacing.

Use a prior patch by:

- diffing it against its identified source to generate candidates;
- cross-checking public results or independently reproduced behavior;
- recording checksum, application order, license, and incompatibilities when it enters the build lineage; and
- remeasuring every width, repertoire, slot, and representation constraint for the current target.

Once the target's own storage -> consumer -> screen path supplies sufficient evidence, use that path as the implementation basis. Do not require a fixed count of prior examples before transitioning. Retain prior patches only as coverage or failure candidates within their verified range.

## 5. Completion

The initial survey is complete when all of these hold:

1. Supported input and modification or rebuild boundaries are identified.
2. A representative target has a reversible storage and consumer interpretation.
3. Initial volume is labeled exact, lower bound, estimate, or unresolved.
4. Required PoCs are distinguished from conditional PoCs, and skipped tests cite equivalent evidence.
5. Every unresolved risk has a next diagnostic, workaround, or viable design branch.

Produce:

- the current architecture and established conclusions;
- a text and asset map including volume status; and
- a proceed/risk table mapping unresolved conditions to next evidence.

Record these conclusions with the survey semantics in `references/conventions/project-records.md` §3. A chronological journal does not replace current conclusions. Return work to the next unresolved condition or to approved implementation. Do not repeat a PoC without a new trigger or loss of evidence equivalence. When a test fails, revise the failed boundary rather than reopening unrelated parts of the survey. Reopen the declared completion scope only when the boundary's own options are exhausted or its established cause recurred; record which options were rejected and the evidence that closed them. Content left outside a narrowed scope requires an approved exception under `references/conventions/translation-artifacts.md` §5. Apply platform constraints only from the applicable platform document and target evidence.
