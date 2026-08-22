# Project conventions

Use these rules to translate patch-strategy invariants and decision criteria into project structure, interfaces, and verification. Inspect the existing repository and toolchain first and retain an equivalent mechanism when present. Choose directories, commands, languages, libraries, and output formats for the current project and environment. Read the applicable `references/platforms/` document for platform constraints.

## Contents

1. Ownership and authoritative sources
2. Primary build path and code boundary
3. Interfaces and exchange data
4. Reproducibility requirements for external components
5. Test policy
6. Source-asset handling

## 1. Ownership and authoritative sources

Before creating or extending a repository, inspect its current build, tests, documents, and asset flow. Do not create a parallel structure when that responsibility already has a defined owner and validation. Separate these roles without giving one fact several update paths:

- source inputs to the reproducible build;
- intermediate and output artifacts regenerable from source;
- current reverse-engineering conclusions and their evidence;
- current human strategic decisions and their applicability;
- translation assets and review state;
- runtime and QA evidence plus issue records; and
- externally injected source images and local caches.

Maintain one authoritative source for each current fact or state. When both a human summary and machine input are needed, derive one from the other or identify explicitly which one is authoritative. Project guidance should route to current structure, build and verification entry points, core documents, and known traps. Keep detailed analysis and current status in the applicable records.

During the initial survey or before adding a persistent location, identify the repository's existing vocabulary and authoritative locations for only the responsibilities the work actually uses. Reuse the established terms and locations across later sessions. When work spans several persistent responsibilities or may outlive the current context, make their ownership discoverable from the project's existing guidance or primary entry point; do not create another guide only to satisfy this convention. Before adding a directory, record class, or synonymous label, establish a distinct responsibility or a durable retention, access, or rights boundary that the current owner cannot represent. A change in confidence, maturity, phase, or file format is not enough. When ownership changes, make the new authority explicit and demote the old location from editable authority in the same change. A generated or read-only compatibility view may remain while needed when its source, status, consumers, and retirement condition are explicit.

Different components may need different representations of one fact. They have a single update path only when one representation is authoritative and the others are generated from it or checked through an explicit conversion or conformance boundary. Compilation and independent local checks do not establish agreement between separately maintained copies. If current representations conflict, one identifier carries different meanings, or preserving another consumer requires a new local interpretation or exception, treat the shared boundary as unresolved and do not promote those local results as cumulative until ownership and agreement are restored.

Investigation experiments, heuristic discovery, and one-off transforms stay outside the primary build. When a conclusion is adopted, record its evidence scope, applicability, and reassessment conditions alongside the current reverse-engineering specification. Repeated builds verify applicability and consume the specification; reproducibility does not require rerunning the investigation that established it.

Choose separately whether to adopt a result as a specification or make its producing procedure a build component. Put the procedure in the primary build only when its stable contract produces a deterministic result from declared inputs or enforces a gate required on every build. Then pin its version, make inputs and outputs explicit, propagate failures, and test the contract under §5.3. Dependence on an adopted conclusion is not by itself a reason to rerun its discovery procedure. A procedure that still produces candidate evidence rather than a required deterministic output or gate remains outside the primary build; rerun it when an applicability check, reassessment condition, or counterexample reopens the analysis. Handle source-derived inputs under §6.2.

When an investigative implementation becomes required by the primary build, adopt it explicitly under a stable production role and contract or keep it outside that path. Isolate or retire competing investigative entry points and candidate interpretations. A historical probe name neither defines nor excuses its current responsibility.

Apply `references/conventions/translation-artifacts.md` to translation meaning and review state, and `references/conventions/project-records.md` to human strategic decisions, investigation, PoC, and QA records.

## 2. Primary build path and code boundary

### 2.1 One primary path

Extraction, transformation, reinsertion, and patch generation must rerun from source through one documented primary path. That path starts from the adopted inputs and specifications under §1; it reconstructs the product, not the investigation history that established them. A primary build is one run of that path producing artifacts. External components may participate, but the path must fix their adopted version, input, output, options, failure conditions, and output verification. A secondary path must not modify the same artifact independently or inherit an untracked manual result.

The primary path must:

1. declare offsets, sizes, integer widths, and endianness to reproduce byte-level output;
2. produce artifacts with equivalent semantics that pass the same checks from the same declared inputs;
3. fail on missing encodings, lossy transforms, overflow, unknown states, and failed verification;
4. identify required versions and inputs and make the same entry point usable in another environment.

An existing project may retain several components or languages when they already form an equivalent reproducible path. They need not become one executable if responsibility and failure remain traceable in one build graph.

### 2.2 Reuse boundary

A reusable unit must describe inputs, outputs, and invariants without target-game facts. Keep target-specific revision, encoding table, pointer addresses, hook locations, and similar facts in the target implementation rather than embedding them in reusable CPU, container, address, or graphics components.

Preserve the same test vectors and consumer-visible behavior when extracting a reusable component. Reuse potential or component count alone does not justify a shared layer or a changed boundary.

### 2.3 Verifying machine-code generation and decoding

When a patch generates or moves more than a fixed short instruction sequence, or claims completeness of control flow or references, it must declare a target ISA profile and assemble and disassemble under the same semantic model. The profile distinguishes CPU variant, instruction width and interpretation mode, extensions, and state-dependent interpretation. No specific product or library is required. If the project implements generation and interpretation itself, it must support every valid instruction and addressing mode in the declared profile, not only the subset currently needed by one patch.

- Verify every valid instruction and mode in the declared profile for semantic equivalence in both assemble → disassemble and disassemble → assemble directions.
- Reject out-of-profile opcodes and modes, reserved values, and truncated instructions rather than treating them as data or success.
- After final placement, disassemble generated ranges again and verify instruction boundaries, operands, branch targets, delay slots, literal pools, and return paths.
- When moving source instructions, compare original effects and live-state invariants at the new location.
- A completeness claim for references or calls must report the declared entry points, the scope of banks, overlays, and modes, and any uninterpreted regions.

The denominator for ISA support is every valid instruction and mode in the declared profile. The denominator for code-analysis completeness is the declared code region. Do not merge them. Report literals, embedded data, and canonical aliases separately. Do not absorb out-of-profile values as instructions or equivalent opcodes. Excluding an optional extension requires evidence that it does not appear in generated, moved, or analyzed scope; encountering it must fail and require a revised profile and verification range.

A fixed short instruction sequence on a verified revision may remain an explicit byte specification without a local ISA implementation only when expected bytes and an independent check of instruction boundaries and effects are present. This exception ends when final placement changes branches, addresses, or literals, or when source instructions move; use the complete ISA path and final placement instead.

## 3. Interfaces and exchange data

### 3.1 Execution interface

Follow the existing project's command and interface conventions. The primary entry point must expose declared inputs and outputs without hidden host state, return machine-detectable failures that identify the affected scope, and reach final artifacts without bypassing verification. Analysis output consumed by automation needs a stable machine-readable interface. Do not add a wrapper over an equivalent existing call path.

### 3.2 Machine-readable input and output

Exchange data between stages must use a machine-readable representation with validated schema and allowed values. The project chooses serialization and field names, but must preserve:

- provenance identifying source and region, plus stable identity surviving re-extraction;
- separation of extractor-protected source information from human-edited information;
- explicit integer width, endianness, address basis, boundaries, and control information;
- rejection of unknown fields, states, tokens, and type mismatches; and
- explicit conversion for schema changes rather than silent absorption.

Extraction output and translation input must share one protected-information baseline. Apply `references/conventions/translation-artifacts.md` to translation assets and `references/conventions/data-formats.md` to mappings, control codes, pointers, reinsertion policy, and font profiles. Retain an established project format if it preserves the same information and validation.

Keep frequently adjusted presentation parameters separate from reverse-engineered structural values. Update each value in one place.

## 4. Reproducibility requirements for external components

When an external program, library, or service affects primary-build output, bind its source and version to declared inputs, options, outputs, failure propagation, and applicability. Retain target-specific round-trip or cross-validation evidence, independent output verification in the primary build, and the license basis for bundling or redistribution. Preserve an existing mechanism that already satisfies these requirements.

## 5. Test policy

### 5.1 Round trip first

First verify round-trip invariants for containers, encodings, compression, address conversion, and render data. For an unchanged transform such as parse -> serialize, require source-byte identity when the format has one canonical representation. When several serializations are valid, require equivalent game consumption and protected metadata. Declare the applicable equivalence before editing. Other documents that require unchanged round trip use this same criterion.

Declare the denominator covered by the round trip. Rebuilding one asset requires the population sharing its consumer rule. Putting a transform into the primary build or claiming general format support requires the full corpus processed by that path. Do not generalize representative samples to the declared denominator; include applicable boundary-risk samples.

For inverse pairs such as encode/decode, compress/decompress, and logical/physical address conversion, generate or systematically enumerate boundary, empty, maximum, truncated, and invalid inputs. Invalid input must not emit partial output as success.

### 5.2 Expected Write rules

Every change from source to target image must be planned as a verifiable Expected Write before application. This includes code and data writes, generated regions, rebuilt containers, pointer, checksum, and header postprocessing, growth, and truncation. No separate path may mutate final output. A component may build a candidate file or byte stream, but before merging it into the final image it must register and verify the resulting differences as Expected Writes.

Calculate the complete write plan first, verify every write against immutable source, then apply it to one output. Do not treat a buffer changed by an earlier write as expected source. If writes intentionally depend on one another, declare the predecessor output and composition rule and establish the final bytes and a single writer before application. The project chooses concrete APIs and types, but each write needs at least: writer identity and purpose, source coordinate system and allowed range, expected source bytes or an equally strong source condition, and final bytes or a derivation rule. A fixed range on a fixed supported revision requires exact expected bytes or a strong hash identifying the range; existence somewhere in the file is not sufficient.

The build must fail when:

- expected source does not match;
- an unregistered path modifies final output;
- different writers overlap without a declared composition;
- a protected, non-target, or out-of-range region changes;
- the union of registered writes does not explain the final diff; or
- pointer, checksum, or metadata postprocessing bypasses write tracking.

Verify all writes belonging to one logical change together. If one fails, apply none and leave no partially modified artifact. The project chooses the application mechanism.

Resolve intentional overlap as one composed write or explicit dependency before application, not by execution order. Every changed output byte must have one decidable writer and reason. An existing tracked image, change manifest, or before/after diff mechanism is equivalent only if it satisfies prior planning, immutable-source verification, single writer, and complete-diff conditions.

When one stage rebuilds a large file, bank, or sector, distinguish writable subranges and protected consumers. Do not broaden the allowed range merely because the stage handles padding or the outer container.

Final-diff audit must include length changes, appended tails, and truncated ranges as well as the common source-output extent. Fail unless registered writes and derivation rules explain expected final size and every changed region.

### 5.3 Investigation, build, test, and runtime responsibilities

Classify work by the claim it establishes and the inputs that can change that claim, not by the command that happens to run it or whether it is automated. One executable may support several roles, but each invocation needs one declared responsibility:

| Responsibility | Use it when | It establishes | Boundary |
|---|---|---|---|
| Investigation | The structure, explanation, applicability, or method is still uncertain. | Candidate evidence and, when adopted, a scoped specification with reassessment conditions. | Keep heuristic search, probes, and candidate selection outside recurring builds and tests. A test may protect a deterministic contract adopted from the investigation; it does not rediscover the contract or treat the current candidate as an expected result. |
| Build | The result depends on current declared source, translation, assets, configuration, or adopted specifications. | Derived product values, rejection of invalid current inputs, and the exact artifact to verify. | Do not pin mutable product results in tests. Calling an investigative procedure from the build does not make it a build component unless it has been adopted under §1 with a stable deterministic output or recurring gate. |
| Test | A result follows from a stable invariant, data format, fixed source profile, minimal fixture, or reproduced failure under controlled inputs. | Continued conformance of an implementation or boundary to that contract. | A passing test neither selects the current product inputs nor proves that the built artifact reaches a live consumer. |
| Runtime verification | The claim depends on the game, loader, renderer, state transition, persistence path, or target environment consuming an exact artifact. | Observed behavior on the declared route and state, bound to that artifact and environment. | Automation does not turn runtime evidence into a build gate or ordinary test. Runtime samples do not establish static population coverage unless the remaining members are tied to the same proven consumer path. |

Investigative analysis may produce code, tables, addresses, or other machine-readable results. Their form does not make them build inputs or test expectations. Adopt the conclusion separately from its discovery procedure under §1, and make the primary build consume the adopted specification. Reopen the investigation only when its recorded applicability check, reassessment condition, or counterevidence requires it. A deterministic verifier may belong to the build after adoption when it checks the current artifact against that specification; its analysis-shaped implementation does not reopen or repeat discovery.

Automate a test only when its expected result follows from an established invariant, data format, or reproduced failure. Assert observable boundary behavior, not incidental line counts, current list sizes, prose wording, or internal call order. A harmless implementation or documentation edit must not require a test change unless the tested contract itself changed.

A test of a checker or validator provides evidence only about that component's contract. It is meaningful when controlled valid input is accepted and a relevant defect that the check claims to detect is rejected. It does not independently strengthen a product claim when it merely confirms that another check exists, was invoked, produced a report, or agreed with logic derived from the same implementation. Test count, assertion count, validation layers, and command success are not quality or completion evidence by themselves. Consolidate or remove tests that cannot distinguish conformance from a relevant contract defect.

A value expected to change under valid edits to declared translation, assets, or configuration is a build result, not a stable test expectation. Let the build derive and report current counts, addresses, displacements, sizes, and checksums. Test the invariant relating those values to source identity, capacity, layout, or artifact consistency. Pin an exact derived value only when it belongs to a declared fixed source profile, data format, frozen release artifact, or minimal regression fixture, and state both the contract that fixes it and the condition that permits it to change.

When producers, analyzers, generators, verifiers, or reports encode the same adopted fact in different representations, an integration check must derive them from the authoritative source or verify their explicit conversion or conformance contract. Testing each component against its own literals does not establish their mutual agreement.

An integration test runs the primary build from declared source, translation, and configuration inputs through final artifacts. It covers at least:

- build completion and the validity and mutual consistency of the output extent, header, checksum fields, and container;
- translation protected information, glyph coverage, length and layout, and pointer ranges;
- identity between the built target and the result of applying the distribution artifact to source; and
- the link between static checks and separate runtime verification required by changed paths.

The primary build owns every criterion that `references/strategy/build-and-verify.md` §1 requires it to fail on. Tests may exercise the build's acceptance and rejection behavior with controlled inputs, but the build remains the enforcement path for current product inputs.

When source media is unavailable, report source-dependent checks as explicitly not run and continue schema, translation, and unit checks that do not require it. Never report a partial run as complete success. Use `references/strategy/build-and-verify.md` for runtime criteria and `references/conventions/project-records.md` for evidence semantics.

## 6. Source-asset handling

### 6.1 Do not commit copyrighted source assets

Do not commit source ROMs or disc images, fully patched output images, or whole graphics, font, audio, and memory dumps extracted from copyrighted source. Ignore rules must cover every actual project input and output location and extension.

Repository-tracked material may include project-authored code, documentation, translation data, selected font and other authored assets, distributable artifacts that do not reproduce source, regeneration procedures, and hashes. Establish the intended distribution basis for every tracked asset. Track third-party fonts, tools, and reference assets only after confirming exact license and source and only as permitted. Apply `references/strategy/font-strategy.md` §4 to selected generatively authored glyph assets. Absence of embedded source content or use of a generative tool does not by itself establish distribution rights; assess applicable rights and terms.

### 6.2 Source injection and identification

Inject source-image location at runtime or through documented local configuration; do not hard-code it. A local default may exist if another environment can override it. Host-specific absolute paths and personal filenames must not become repository assumptions.

Before interpreting or modifying content as a supported build input, determine its revision and region, compute its size and a strong content hash, and match them to a declared source profile. An unknown source may be examined under an explicit survey-only baseline to establish its identity and structure, but a supported build must reject it until the applicable profile and coordinates are established. Do not promote survey findings from that input into another profile silently. Maintain expected identity in one code location or validated manifest. When supporting several sources, separate coordinate and format profiles and record the selected profile in output.

Regenerate source-derived build inputs such as palettes, tile bases, glyph originals, and baked graphics from declared source when possible. Prior-patch extracts and manual working files may provide comparison or bootstrap evidence but must not enter the build without independent verification against declared source. When an irreproducible local derivative is unavoidable, document its limit, identity hash, necessary rights, and verification procedure, and fail the build when it is absent.
