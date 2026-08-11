# Project conventions

Use these rules to implement patch-strategy invariants and decision criteria as project structure, interfaces, and verification. Inspect the existing repository and toolchain first and retain an equivalent mechanism when present. Choose directories, commands, languages, libraries, and products for the current project and environment. Read the applicable `references/platforms/` document for platform constraints.

## Contents

1. Responsibility boundaries and a single basis
2. Primary build path and code boundary
3. Interfaces and exchange data
4. Reproduction conditions for external components
5. Test policy
6. Source-asset handling

## 1. Responsibility boundaries and a single basis

Before creating or extending a repository, inspect its current build, tests, documents, and asset flow. Do not create a parallel structure when one location and check already carry the responsibility. Separate these roles without giving one fact several update paths:

- source inputs to the reproducible build;
- intermediate and output artifacts regenerable from source;
- current reverse-engineering conclusions and their evidence;
- translation assets and review state;
- runtime and QA evidence plus issue records; and
- externally injected source images and local caches.

Maintain each current fact or state in one place. When both a human summary and machine input are needed, derive one from the other or point explicitly to the basis. Project guidance should route to current structure, build and verification entry points, core documents, and known traps. Keep detailed analysis and current status in the applicable records.

Investigation experiments and one-off transforms may remain outside the primary build. When repeated builds depend on one, promote it into a maintained component with fixed version, explicit inputs and outputs, propagated failures, and tests. An unpromoted temporary artifact or manual edit must not become the build's only input.

Apply `references/conventions/translation-artifacts.md` to translation meaning and review state, and `references/conventions/project-records.md` to investigation, PoC, and QA records.

## 2. Primary build path and code boundary

### 2.1 One primary pipeline

Extraction, transformation, reinsertion, and patch generation must rerun from source through one documented primary path. External components may participate, but the path must fix their adopted version, input, output, options, failure conditions, and output verification. A secondary path must not modify the same artifact independently or inherit an untracked manual result.

The primary path must:

1. declare offsets, sizes, integer widths, and endianness to reproduce byte-level output;
2. produce artifacts with the same meaning and verification result from the same declared inputs;
3. fail on missing encodings, lossy transforms, overflow, unknown states, and failed verification;
4. identify required versions and inputs and provide the same entry point in another environment.

An existing project may retain several components or languages when they already form an equivalent reproducible path. They need not become one executable if responsibility and failure remain traceable in one build graph.

### 2.2 Reuse boundary

A reusable unit must describe inputs, outputs, and invariants without target-game facts. Keep target-specific revision, encoding table, pointer addresses, hook locations, and similar facts in the target implementation rather than embedding them in reusable CPU, container, address, or graphics components.

The same test vectors and consumed result must survive extraction into a reusable component. Reuse potential or component count alone does not justify a shared layer or a changed boundary.

### 2.3 Machine-code generation and interpretation verification

When a patch generates or moves more than a fixed short instruction sequence, or claims completeness of control flow or references, it must declare a target ISA profile and assemble and disassemble under the same semantic model. The profile distinguishes CPU variant, instruction width and interpretation mode, extensions, and state-dependent interpretation. No product or library is required. If the project implements generation and interpretation itself, it must support every valid instruction and addressing mode in the declared profile, not only the subset currently needed by one patch.

- Verify every valid instruction and mode in the declared profile for semantic equivalence in both assemble -> disassemble and disassemble -> assemble directions.
- Reject out-of-profile opcodes and modes, reserved values, and truncated instructions rather than treating them as data or success.
- After final placement, disassemble generated ranges again and verify instruction boundaries, operands, branch targets, delay slots, literal pools, and return paths.
- When moving source instructions, compare original effects and live-state invariants at the new location.
- A completeness claim for references or calls must report declared entry points, bank, overlay, and mode scope plus uninterpreted regions.

The denominator for ISA support is every valid instruction and mode in the declared profile. The denominator for code-analysis completeness is the declared code region. Do not merge them. Report literals, embedded data, and canonical aliases separately. Do not absorb out-of-profile values as instructions or equivalent opcodes. Excluding an optional extension requires evidence that it does not appear in generated, moved, or analyzed scope; encountering it must fail and require a revised profile and verification range.

A fixed short instruction sequence on a verified revision may remain an explicit byte specification without a local ISA implementation only when expected bytes and an independent check of instruction boundaries and effects are present. This exception ends when final placement changes branches, addresses, or literals, or when source instructions move; use the complete ISA path and final placement instead.

## 3. Interfaces and exchange data

### 3.1 Execution interface

Follow the existing project's command and interface conventions. A new interface needs only these properties:

- source input, configuration, translation assets, and output location are explicit;
- no host-specific absolute path or hidden global state is embedded in code;
- automation can decide success and failure, and failures identify affected scope and cause;
- analysis output is stable machine input for later stages rather than parsed human prose; and
- the primary build entry point reaches final artifacts without bypassing required verification.

The project decides whether analysis and build share one interface. Do not add a naming scheme or wrapper over an equivalent existing call path.

### 3.2 Machine-readable input and output

Exchange data between stages must use a machine-readable representation with validated schema and allowed values. The project chooses serialization and field names, but must preserve:

- provenance identifying source and region, plus stable identity surviving re-extraction;
- separation of extractor-protected source information from human-edited information;
- explicit integer width, endianness, address basis, boundaries, and control information;
- rejection of unknown fields, states, tokens, and type mismatches; and
- explicit conversion for schema changes rather than silent absorption.

Extraction output and translation input must share one protected-information baseline. Apply `references/conventions/translation-artifacts.md` to translation assets and `references/conventions/data-formats.md` to mappings, control codes, pointers, reinsertion policy, and font profiles. Retain an equivalent established project format after comparing meaning and validation.

Keep frequently adjusted presentation parameters separate from reverse-engineered structural values. Update each value in one place.

## 4. Reproduction conditions for external components

When an external program, library, or service affects primary-build output, record in the project:

- a source and version or commit sufficient to reproduce the result;
- declared inputs, options, outputs, and failure propagation;
- the capability and applicability assigned to the component;
- round-trip or cross-validation results on target source or a representative risk corpus;
- independent verification of its output in the primary build; and
- license conditions for bundling or redistribution.

Choose a component that satisfies these conditions in the current environment and implementation. Retain an existing equivalent reproduction and verification mechanism.

## 5. Test policy

### 5.1 Round trip first

First verify round-trip invariants for containers, encodings, compression, address conversion, and render data. For an unchanged transform such as parse -> serialize, require source-byte identity when the format has one canonical representation. When several serializations are valid, require equivalent game consumption and protected metadata. Declare the applicable equivalence before editing. Other documents that require unchanged round trip use this same criterion.

Declare the denominator covered by the round trip. Rebuilding one asset requires the population sharing its consumer rule. Putting a transform into the common build or claiming general format support requires the full corpus processed by that path. Do not generalize representative samples to the declared denominator; include applicable boundary-risk samples.

For inverse pairs such as encode/decode, compress/decompress, and logical/physical address conversion, generate or systematically enumerate boundary, empty, maximum, truncated, and invalid inputs. Invalid input must not emit partial output as success.

### 5.2 Expected Write rules

Every change from source to target image must be planned as a verifiable Expected Write before application. This includes code and data writes, generated regions, rebuilt containers, pointer, checksum, and header postprocessing, growth, and truncation. No separate path may mutate final output. A component may build a candidate file or byte stream, but before merging it into the final image it must register and verify the resulting differences as Expected Writes.

Calculate the complete write plan first, verify every write against immutable source, then apply it to one output. Do not treat a buffer changed by an earlier write as expected source. If writes intentionally depend on one another, declare the predecessor output and composition rule and establish final bytes plus one writer before application. The project chooses concrete APIs and types, but each write needs at least: writer and meaning, source coordinate system and allowed range, expected source bytes or an equally strong source condition, and final bytes or a derivation rule. A fixed range on a fixed supported revision requires exact expected bytes or a strong hash identifying the range; existence somewhere in the file is not sufficient.

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

### 5.3 Integration tests

Automate a test only when its expected result follows from an established invariant, data format, or reproduced failure. Assert observable boundary behavior, not incidental line counts, current list sizes, prose wording, or internal call order. A harmless implementation or documentation edit must not require a test change unless the tested contract itself changed.

An integration test runs the primary build from declared source, translation, and configuration inputs through final artifacts. It covers at least:

- build completion and output size, header, checksum, and container validity;
- translation protected information, glyph coverage, length and layout, and pointer ranges;
- identity between the built target and the result of applying the distribution artifact to source; and
- the link between static checks and separate runtime verification required by changed paths.

When source media is unavailable, report source-dependent checks as explicitly not run and continue schema, translation, and unit checks that do not require it. Never report a partial run as complete success. Use `references/strategy/build-and-verify.md` for runtime criteria and `references/conventions/project-records.md` for evidence semantics.

## 6. Source-asset handling

### 6.1 Do not commit copyrighted source assets

Do not commit source ROMs or disc images, fully patched output images, or whole graphics, font, audio, and memory dumps extracted from copyrighted source. Ignore rules must cover every actual project input and output location and extension.

Track only project-authored code, documentation, and translation data; distributable artifacts that do not reproduce source; regeneration procedures; hashes; and other material whose distribution rights have been established. Track third-party fonts, tools, and reference assets only after confirming exact license and source and only as permitted. Absence of embedded source content does not by itself establish distribution rights; assess applicable rights and terms.

### 6.2 Source injection and identification

Inject source-image location at runtime or through documented local configuration; do not hard-code it. A local default may exist if another environment can override it. Host-specific absolute paths and personal filenames must not become repository assumptions.

Before reading content, verify revision, region, size, and a strong identity hash. Fail clearly on an unknown source. Maintain expected identity in one code or validated-manifest location. When supporting several sources, separate coordinate and format profiles and record the selected profile in output.

Regenerate source-derived build inputs such as palettes, tile bases, glyph originals, and baked graphics from declared source when possible. Prior-patch extracts and manual working files may provide comparison or bootstrap evidence but must not enter the build without independent verification against declared source. When an irreproducible local derivative is unavoidable, document its limit, identity hash, necessary rights, and verification procedure, and fail the build when it is absent.
