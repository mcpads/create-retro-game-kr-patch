# Data conventions for analysis and builds

Machine-readable data exchanged among text extraction, translation, reinsertion, and font building must preserve the meanings and pass criteria required by strategy. When the project already has an equivalent format and validation, retain its serialization and field names. Human-tracked decisions such as text maps, PoCs, HITL, and QA follow `references/conventions/project-records.md`.

## Contents

1. Common rules
2. Character mapping tables
3. Control-code specifications
4. Pointer catalogs
5. Reinsertion policy data
6. Font render profiles
7. Validation binding

## 1. Common rules

Apply the single-basis and machine-readable I/O requirements in `references/conventions/project-conventions.md` §1, §3.2. Preserve these domain meanings as well:

- Source coordinates, source bytes, and raw pointer values are protected analysis and build data. Do not mix them with translations or presentation parameters for manual editing.
- Serialize offsets, addresses, and byte strings with visible radix and width for human review.
- Represent a population exhaustively established on fixed source input as exact constants or a catalog. The build must not adopt heuristic rediscovery silently. A difference from the established population indicates the source revision or specification must be reassessed. Use `references/strategy/initial-survey.md` §3.1 to decide which values are fixed and which derive from output.

The JSON below is an optional illustration of field meaning. Retain another structure or serialization that provides the same meaning and checks. Apply `references/conventions/translation-artifacts.md` to translator-edited source text, translation, state, tokens, and approvals. Link analysis data and translation assets by stable ID and source identity. Maintain character mappings, pointers, and reinsertion policies in one analysis/build-data location each.

## 2. Character mapping tables

Follow the project's existing representation for mapping custom-encoding bytes to characters or strings. When no representation exists and a simple mapping is sufficient, a `.tbl` form may be used:

```text
41=あ
42=い
F0=のは
FF00=[END]
```

- The left side is a hexadecimal byte sequence without whitespace and preserves byte boundaries.
- The right side may contain one character or a multi-character DTE/MTE expansion.
- A tool may place control-code names in brackets. Normalize them to reversible tokens from `references/conventions/translation-artifacts.md` when producing extraction artifacts.
- Do not guess a character for an undecoded byte. Investigation output may expose a raw form such as `<XX>`. `references/strategy/text-extraction.md` §3.4 decides when editable translation assets may retain a reversible raw token.
- When the table changes, re-extract and review differences instead of manually changing protected fields in existing translation assets.

An implementation without `.tbl` must still share one mapping definition between decode and encode and represent many-to-one mappings, one-to-many mappings, and undecoded bytes without loss.

## 3. Control-code specifications

Keep one control-code specification consumed by both extractor and reinsertor. It must express at least:

- code bytes or identifying pattern;
- argument count and each argument's width, endianness, and preservation rule;
- whether it terminates a string or message;
- human-editable token name and meaning;
- applicable file, region, and renderer scope; and
- which arguments remain in source raw data and which are recomputed after relocation.

One optional structured representation is:

```json
{
  "code": "FF05",
  "name": "delay",
  "arguments": [{ "width": 2, "endian": "big", "policy": "preserve" }],
  "terminates": false,
  "scope": "dialog"
}
```

Record byte boundaries and argument widths even when meaning remains unclear. Use a neutral name and preserve the full byte sequence. A later change in semantic interpretation must not change established parsing boundaries silently.

## 4. Pointer catalogs

When an exhaustively verified pointer population for a fixed source revision is represented as a catalog, it must allow every pointer recorded in source coordinates to be rewritten for the rebuilt image. Apply the promotion conditions in `references/strategy/initial-survey.md` §3.1. The catalog must recover at least:

- source storage location of the pointer bytes;
- width, endianness, and address basis such as file, RAM, bank, or table relative;
- raw source value and interpreted source target;
- whether splice or relocation moves the storage location itself;
- a pattern or boundary condition validating the adjusted target; and
- for an interior-string pointer, an anchor identifying the same structural point after translation.

An optional JSON representation is:

```json
{
  "pointer_id": "dialog/0001/ref-0",
  "storage_offset": "0x000000",
  "width_bits": 16,
  "endian": "little",
  "basis": "ram",
  "base": "0x00000000",
  "raw_value": "0x0000",
  "target_offset": "0x000000",
  "storage_moves": true,
  "target_check": { "kind": "prefix", "bytes": "FF03" },
  "anchor": null
}
```

Field names and JSON are optional. For an established revision catalog, keep source raw values and storage coordinates fixed rather than rereading pointers from a post-splice buffer. Repeated builds consume the approved catalog. A discovery scanner proposes additions or updates but never adopts them silently.

Do not disguise multiple revisions, runtime-generated data, or unresolved structures as a fixed catalog. A table whose schema determines every count and boundary may instead be parsed directly on each build. Either route must fail when a heuristic candidate is adjusted without review or an established pointer disappears without an explicit mapping decision.

## 5. Reinsertion policy data

Keep per-entry policy in build data separate from translator-edited prose. If translation assets reference it, use a stable entry key and treat the policy as protected information.

The representation must preserve these meanings; field names are examples:

| Example field | Meaning |
|---|---|
| `mode` | Established length and placement policy: `fixed`, `relocate`, or `grow` |
| `overflow_policy` | Selected response such as failure, approved translation adjustment, or relocation; automatic truncation is forbidden |
| `pad_byte` | Byte sequence established as no-op padding for the target engine |
| `pad_position` | Established insertion position before or after termination, or in a fixed-slot remainder |
| `terminator_policy` | Boundary handling such as preserve, regenerate, or absent |
| `alignment` | Required byte alignment for an entry or block |

Do not define global defaults for padding, terminators, or alignment. A profile default may apply only to an explicit scope with the same verified consumer boundary. Missing required values must fail the build and return to boundary investigation rather than selecting arbitrary defaults.

## 6. Font render profiles

When `references/strategy/font-strategy.md` §5 requires per-path profiles, each profile must link presentation inputs and verification output to one target consumer without ambiguity.

Declare only meanings needed by the target render path:

- project-relative source-glyph identity, exact version, and license evidence;
- target render path, cell, baseline, and margins;
- rasterization, thresholding, outline, and other parameters that affect pixels;
- bit depth, palette, packing, and subtile order defining game representation; and
- identity linking comparison output and actual build artifacts made from the same profile.

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
