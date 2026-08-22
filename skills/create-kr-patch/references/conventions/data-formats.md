# Data conventions for analysis and builds

Machine-readable data exchanged among text extraction, translation, reinsertion, and font building must preserve the required information and satisfy the pass criteria defined by strategy. When the project already has an equivalent format and validation, retain its serialization and field names. Human-tracked decisions such as text maps, PoCs, HITL, and QA follow `references/conventions/project-records.md`.

## Contents

1. Common rules
2. Character mapping tables
3. Control-code specifications
4. Pointer catalogs
5. Reinsertion policy data
6. Font-rendering profiles
7. Validation binding

## 1. Common rules

Apply the authoritative-source and machine-readable I/O requirements in `references/conventions/project-conventions.md` §1, §3.2. Preserve this domain information as well:

- Source coordinates, source bytes, and raw pointer values are protected analysis and build data. Do not mix them with translations or presentation parameters for manual editing.
- Serialize offsets, addresses, and byte strings with visible radix and width for human review.
- Represent a population exhaustively established on fixed source input as exact constants or a catalog. The build must not adopt heuristic rediscovery silently. A difference from the established population indicates the source revision or specification must be reassessed. Use `references/strategy/initial-survey.md` §3.1 to decide which values are fixed and which derive from output.

Apply `references/conventions/translation-artifacts.md` to source text presented to translators, authored wording, state, tokens, and approvals. Link analysis data and translation assets by stable ID and source identity. Maintain character mappings, pointers, and reinsertion policies, each in a single analysis/build-data location.

## 2. Character mapping tables

Retain the project's existing representation. The mapping must preserve code-unit boundaries, one-to-many and many-to-one mappings, and undecoded bytes without loss, and one definition must drive both decoding and encoding. Normalize control-code labels to the reversible tokens in `references/conventions/translation-artifacts.md`; do not guess characters for undecoded bytes. When the mapping changes, re-extract and review differences instead of editing protected fields in existing translation assets.

## 3. Control-code specifications

Keep one control-code specification consumed by both the extractor and the reinsertion tool. It must express at least:

- code bytes or identifying pattern;
- argument count and each argument's width, endianness, and preservation rule;
- whether it terminates a string or message;
- human-editable token name and meaning;
- applicable file, region, and renderer scope; and
- which arguments remain in raw source data and which are recomputed after relocation.

Record byte boundaries and argument widths even when meaning remains unclear. Use a neutral name and preserve the full byte sequence. A later change in semantic interpretation must not change established parsing boundaries silently.

## 4. Pointer catalogs

When an exhaustively verified pointer population for a fixed source revision is represented as a catalog, it must allow every pointer recorded in source coordinates to be rewritten for the rebuilt image. Apply the promotion conditions in `references/strategy/initial-survey.md` §3.1. The catalog must recover at least:

- source storage location of the pointer bytes;
- width, endianness, and address basis such as file, RAM, bank, or table-relative;
- raw source value and interpreted source target;
- whether splice or relocation moves the storage location itself;
- a pattern or boundary condition validating the adjusted target; and
- for an interior-string pointer, an anchor identifying the same structural point after translation.

Field names and JSON are optional. For an established revision catalog, keep raw source values and storage coordinates fixed rather than rereading pointers from a post-splice buffer. Repeated builds consume the approved catalog. A discovery scanner proposes additions or updates but never adopts them silently.

Do not disguise multiple revisions, runtime-generated data, or unresolved structures as a fixed catalog. A table whose schema determines every count and boundary may instead be parsed directly on each build. Either route must fail when a heuristic candidate is adjusted without review or an established pointer disappears without an explicit mapping decision.

## 5. Reinsertion policy data

Keep per-entry policy in build data separate from translator-edited prose. If translation assets reference it, use a stable entry key and treat the policy as protected information.

The representation must preserve the following information; field names are examples:

| Example field | Meaning |
|---|---|
| `mode` | Established length and placement policy: `fixed`, `relocate`, or `grow` |
| `overflow_policy` | Selected response such as failure, approved translation adjustment, or relocation; automatic truncation is forbidden |
| `pad_byte` | Byte sequence established as no-op padding for the target engine |
| `pad_position` | Established insertion position before or after termination, or in a fixed-slot remainder |
| `terminator_policy` | Boundary handling such as preserve, regenerate, or absent |
| `alignment` | Required byte alignment for an entry or block |

Do not define global defaults for padding, terminators, or alignment. A profile default may apply only to an explicit scope with the same verified consumer boundary. Missing required values must fail the build and return to boundary investigation rather than selecting arbitrary defaults.

## 6. Font-rendering profiles

When `references/strategy/font-strategy.md` §5 requires per-path profiles, each profile must link presentation inputs and verification output to one target consumer without ambiguity.

Declare only the properties needed by the target render path:

- project-relative source-glyph identity, exact version, and license evidence;
- target render path, cell, baseline, and margins;
- rasterization, thresholding, outline, and other parameters that affect pixels;
- bit depth, palette, packing, and subtile order defining game representation; and
- identities showing that comparison output and build artifacts use the same profile.

The project chooses field names, serialization, and how values are selected. Applicability must be unambiguous; unknown targets, values, or omissions are errors. Review output and builds must use the same established values.

Do not mix reverse-engineered structural constants such as memory addresses, banks, and encoding boundaries into a presentation profile. Keep frequently adjusted presentation values separate from established structure.

## 7. Validation binding

The representation must allow mechanical decisions that:

- re-encoding translation-artifact source text reproduces protected source bytes at the recorded source location;
- stable IDs and extraction baseline link each source entry to applicable reinsertion data without missing required links, cross-scope collisions, or loss of intentional sharing and duplicate references;
- every control code consumes exactly its argument width, with no undecoded or truncated code;
- interpreting a raw pointer under its address basis produces the recorded source target, and inverse conversion reproduces the raw value;
- every catalog pointer after reinsertion satisfies valid range and target checks, with no unannounced catalog-size change; and
- every font-profile target uses the same interpretation in build artifacts and comparison output.

Concrete test code follows the project language and test structure. A field-name change must update tests in the same commit. Do not tolerate unknown fields for compatibility; provide an explicit schema conversion when compatibility is required.
