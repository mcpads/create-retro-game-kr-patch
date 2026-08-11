# Text extraction strategy

Establish the consumable text population in distribution scope and preserve source codes, control tokens, boundaries, and references in a form that supports reinsertion. Choose discovery techniques and analysis tools for the target; judge completion by the criteria below.

## 1. Population and reference model

### 1.1 Supported input

Declare supported source revisions, discs, execution paths, and distribution text scope. Identify a fixed revision by hash and structural expectations. For multiple inputs or unresolved populations, reject unsupported structures explicitly rather than inferring them silently.

### 1.2 Evidence for text

A byte sequence that resembles characters is only a candidate. Include it in the text population only after independent evidence establishes actual consumption, such as:

- a declared table, record, or script structure identifies the string boundary;
- a runtime consumer reads the range as characters or tokens;
- source screen state corresponds to code-to-glyph output; or
- another independent extraction path reproduces the same boundary and meaning.

One statistic, standard decode, search hit, or visual resemblance does not establish text.

### 1.3 Reference population

For a fixed supported revision, an exhaustively reviewed catalog of pointers, indexes, and script references is explicit specification. Repeated builds must verify and consume its count, locations, and expected bytes. Parse inputs whose count and boundaries follow completely from established structure within the declared scope. Use heuristic searches to discover candidates and audit omissions, never to adopt results automatically.

Establish reference width, endianness, base, bank, and segment from the real consumer, not platform convention. Do not use file order, pointer sorting, or the next reference as a boundary unless the consumer guarantees it. Preserve duplicate pointers, shared tails, and interior-string entries.

### 1.4 Completion denominator

"Complete extraction" means every member of the declared population is counted as resolved, excluded, or unresolved, with zero unresolved members. Record separately:

- resolved extraction, translation, or preservation targets;
- items excluded as non-text or out of scope with evidence; and
- items whose meaning, boundary, or consumer remains unresolved.

Do not merge unresolved into excluded. If the denominator is not established, report remaining investigation rather than completion.

### 1.5 Volume survey before scaling translation

A technical PoC on a representative unit is different from a volume decision for distribution scope. When a static asset list or an established parser, table, or reference boundary can enumerate the declared scope without new assumptions, enumerate the full scope at that point. Do not make manual accumulation after each newly observed screen or file the default way to establish a denominator.

Measure by localization kind and consumer scope, distinguishing:

- the exhaustively enumerated population and counts of resolved, excluded, and unresolved items;
- exact values from established structure, lower bounds with unresolved scope, and estimates with limited evidence;
- containers or execution paths not enumerated, why they remain unresolved, and the next evidence or stopping condition;
- units that can change translation workload, storage, or representation design, such as entry count, source character or code units, raw bytes, and graphics-text blocks established by `references/strategy/graphics-text.md` §1.

Count shared strings and duplicate references separately as logical translation units and physical storage units. Do not add decoded or searched candidates to confirmed workload before they pass §1.2. Early volume is not completion, and source volume alone does not determine Korean length growth or unique-glyph demand.

A technical PoC or translation of a local scope with a known denominator may precede this decision. Before scaling translation to the whole distribution scope, determine for each declared target kind whether its population can be exhaustively enumerated, and exhaustively enumerate every population for which that is possible.

If structure prevents exhaustive enumeration, state the established lower bound, unresolved scope, and stopping condition. Do not scale while remaining uncertainty can change workload or technical design. Do not claim exact workload, completion percentage, or complete-corpus demand before establishing the population.

## 2. Encoding and glyph mapping

An encoding name labels a candidate; it does not establish actual interpretation. Confirm consumer semantics from:

- code units and character boundaries read by the consumer;
- branches from code to glyph, symbol, or control behavior;
- correspondence with actual screens or glyph supply; and
- reversible decode and encode of source codes.

A standard-like encoding may include game-specific external characters, reserved codes, and control tokens. Decoder failure does not make a value unused or invalid. Successful standard decoding does not prove that the game consumes the value with that meaning.

Separate mappings by renderer, file, or state when code tables differ. Merge them only after every consumer and source round trip satisfies one mapping. Apply `references/strategy/font-strategy.md` §2 when reusing code space for Hangul.

## 3. Control tokens

### 3.1 Boundaries and argument widths

A control-token definition includes argument count and width, termination, nesting or state effects, and the position after consumption, not only an opcode. Preserve established byte boundaries and argument widths even when meaning is unresolved. When character and token ranges overlap, distinguish them by the actual dispatch conditions.

### 3.2 Establishing meaning

Frequency and position generate hypotheses. Confirm meaning when independent evidence from consumer branches, state changes, and screen, audio, or event results agrees. Identical appearance does not make two tokens equivalent when internal state effects differ.

### 3.3 Scope-specific specifications

The same byte may mean different things in different engines. A token specification must identify its consumer and applicability. Do not assign an established name automatically to unresolved code outside that scope.

### 3.4 Unresolved tokens

When boundary and argument width are established but meaning is unresolved, assign `forbidden` and preserve opcode, arguments, source order, and position in consumption order as raw representation. Translation must not delete, modify, or move it. Promote the entry for distribution only when changes to surrounding length, placement, and timing are shown not to change the token's consumed result or subsequent state. If that cannot be verified, or boundary or argument width is unresolved, assign no token policy and block the entry from translation and distribution eligibility.

### 3.5 Detection error assessment

- **False positive**: A text or reference candidate is not consumed or is interpreted as another structure.
- **False negative**: Consumable text or a reference is missing from the extraction denominator.

A filter reducing candidate count does not by itself improve accuracy. Assess false positives and false negatives separately against an approved catalog, a structurally exhaustive scope, runtime consumption scope, or an independent extraction. A filter that silently discards unresolved candidates cannot satisfy completion.

## 4. Extraction artifact requirements

### 4.1 Stable identifiers

Each item needs identity and source coordinates that survive translation changes. Display order alone must not identify a reinsertion target. Follow `references/conventions/translation-artifacts.md` for preserved meaning and validation of identity, coordinates, and protected data. The project chooses field names and serialization.

### 4.2 Source preservation

Retain source codes, tokens, sharing relationships, and boundary-recovery data separately from translator-facing text. Human-editable representation must not become the only source evidence.

### 4.3 Applicability

An artifact must declare the revision, file, bank, script, consumer, and exclusions it represents. Fail on cross-scope key collisions or accidental application to unsupported input.

### 4.4 Token policy

Assign each token a policy from consumer meaning:

| Policy | Condition | Requirement |
|---|---|---|
| `preserve` | Source meaning and order are required, such as termination, event, or state | Preserve opcode, arguments, and order |
| `movable-layout` | Layout tokens such as line or page breaks may move | Constrain valid positions and reverify layout |
| `recompute` | Value derives from output, such as length or checksum | Recompute from the final result and verify |
| `translate` | Source and target consumers use different opcode or index meanings | Map to a verified equivalent token, or replace with an approved literal only after proving the value static; fail if dynamic value or execution effect is lost |
| `forbidden` | Boundary and argument width are established, but meaning is unresolved or editing is disallowed | Preserve raw opcode, arguments, source order, and consumption-order position; fail on edits or moves, and block distribution if surrounding changes cannot be shown harmless |

Do not force every token to remain at the same byte position, and do not let a layout engine move every token freely. Encoder and validator must consume the same policy definition.

## 5. Round trip and completeness

Verify an unchanged round trip before editing across every extraction, serialization, and reinsertion boundary.

- Apply the equivalence criteria in `references/conventions/project-conventions.md` §5.1, including preservation of reference relationships.
- Bytes outside the parser's declared read-write extent must remain unchanged.
- Every source character, token, argument, and sharing relationship must be recoverable without loss.

Round-trip success proves that extracted members can be written back. It does not prove that no text was missed. Completion also requires the §1.4 population and independent consumer or structural evidence; no single coverage score replaces them.

## 6. Text map and exclusions

The text map is a current account of the denominator and remaining uncertainty, not a file list or journal. It must distinguish:

- declared text and reference populations with resolution states;
- applicability of code tables, tokens, and boundary models;
- evidence for non-text and out-of-scope exclusions;
- unresolved candidates and the evidence needed for the next decision; and
- ranges eligible for relocation or space reclamation with evidence of reference completeness under `references/strategy/reinsertion.md` §5.

Repeated fill, decode failure, or zero current search hits does not prove non-text or free space. Include inline literals when a real consumer reads them. Apply the record semantics in `references/conventions/project-records.md`.

## 7. Completion

Text extraction is complete only when:

- Every member of the declared population is counted under §1.4 with zero unresolved items.
- Scaling to full distribution scope has passed the volume survey in §1.5.
- Code-table and token boundaries and argument widths are established; unresolved-meaning tokens have a policy or their entries are blocked.
- Extraction artifacts provide stable identity, source preservation, declared applicability, and token policies.
- Unchanged round trip passes the declared equivalence rule, and false positives and false negatives are assessed separately.
- The text map represents the current denominator and unresolved candidates.

Round trip, one coverage score, or one representative PoC does not replace these conditions.
