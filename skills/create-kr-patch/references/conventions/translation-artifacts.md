# Translation asset conventions

Preserve source text, review state, reversible control codes, and build-input eligibility required by translation strategy through the meanings and checks below. Retain an existing schema or work-management system that provides equivalent meaning and validation, including its serialization, directories, and field names.

## Contents

1. Required meaning
2. Optional JSON profile
3. Control-code tokens
4. Progress-state meaning
5. Build-input eligibility

## 1. Required meaning

A translation-asset representation must distinguish at least:

- provenance identifying the source image and extraction region;
- stable entry identity comparable after re-extraction;
- source bytes and the decoded result derived from them;
- translator-edited output;
- states distinguishing untranslated, in progress, needs review, needs human judgment, and distribution-eligible;
- evidence for adaptation, wording decisions, and unresolved interpretations; and
- structure required for reinsertion, or a stable link to analysis and build data containing it.

Source bytes, source text, structural information, and link identities in a translation asset are protected. Translation work may change only translated output, review state, and decision evidence. A protected change requires re-extraction or an explicit structural change.

Apply `references/conventions/data-formats.md` to character mappings, raw control-code specifications, pointer catalogs, and reinsertion policy. A translation asset may link to them by stable ID and source identity or preserve protected information inside an established integrated artifact. Edit each value in only one location.

`references/strategy/translation-workflow.md` §3.1 determines agent translation and review-batch inputs. Preserve the protected values and extraction-baseline versions provided to a batch so merge can compare them with the current extraction baseline. Even when a batch copy displays these values, maintain each baseline in one location and never overwrite protected fields from an agent response.

Translation made while evaluating another model or agent must identify evaluation scope, conditions, and provenance. A human-approved sample may enter work in progress only while source baseline, protected information, context, terminology, and voice match the evaluation. Evaluation does not complete review or grant distribution eligibility. Output that failed evaluation must not become build-selected translation.

Immediately before merge or reinsertion, compare source identity and raw bytes against supported source or the current extraction baseline regenerated from it, not merely against metadata copied among batches. A mismatch identifies output from an older baseline; do not merge until its impact has been assessed.

### 1.1 Approved terminology and voice decisions

The approved basis for terms, repeated expressions, and voice must record a stable decision ID; the source referent or situation; the approved output; applicability by title, revision, scene, speaker relationship, and narrative point; evidence and transfer limit; and an approved, unresolved, or conflicting state. Because one source term may have scope-specific decisions, do not use the source string as a globally unique key. When new evidence changes a decision, retain enough lineage to identify affected batches requiring revalidation; do not silently overwrite it. The project chooses file count, table structure, and field names.

## 2. Illustrative JSON example

This JSON only illustrates required meaning and protected boundaries. Do not migrate an equivalent existing structure to this form.

```json
{
  "table_id": "dialog_group",
  "source": {
    "pointer_table": "0x000000",
    "entry_count": 2,
    "base": "0x000000",
    "method": "pointer_table",
    "terminators": ["FE"]
  },
  "entries": [
    {
      "entry_id": 0,
      "ptr_value": "0x0000",
      "file_offset": "0x000000",
      "raw_hex": "...FE",
      "text": "source{end}",
      "ko": "translation{end}",
      "status": "in_progress",
      "notes": null,
      "flags": []
    },
    {
      "entry_id": 1,
      "ptr_value": null,
      "file_offset": null,
      "raw_hex": null,
      "text": null,
      "ko": "",
      "status": "untranslated",
      "notes": null,
      "flags": ["null_entry"]
    }
  ]
}
```

This example also follows the machine-readable I/O requirements in `references/conventions/project-conventions.md` §3.2.

- Keep `table_id` and `entry_id` stable. Empty slots remain part of entry order and count.
- `raw_hex` and `text` are protected fields written by the extractor. `ko`, `status`, and `notes` are translation-stage fields.
- Represent duplicate pointers and undecoded bytes using `flags` or an equivalent project representation that preserves meaning and round-trip fidelity.

## 3. Control-code tokens

Represent control codes in human-editable source and translated text as tokens reversible to their original bytes. Optional syntax examples:

- no arguments: `{br}`, `{wait}`, `{end}`
- arguments: `{delay:1E}`, `{face:02,05}`
- undecoded code: `{op27:0B}`
- undecoded raw byte with established boundary: `{raw:XX}`

Token syntax must be bijective with byte sequences. Define escaping for literal syntax collisions. `references/strategy/text-extraction.md` §4.4 determines each token's policy. Build-input checks compare token set, order, parameters, and transformed output according to the applied policy. Do not require one-to-one position for every token. Projects may rename tokens and punctuation while preserving reversibility and verification.

## 4. Progress-state meaning

Work management must distinguish at least these meanings. Names are examples:

| Example state | Meaning | Minimum condition for the next state |
|---|---|---|
| `untranslated` | Extraction baseline present, no translation | Work begins |
| `in_progress` | Translation or correction underway | Entry translation and established-constraint checks pass |
| `needs_review` | Cross-review required | Applicable independent review, review of selected language-heuristic candidates, and resolution of established-constraint failures |
| `needs_human_review` | Human judgment required | Human decision and approval with evidence |
| `distribution_eligible` | Established checks and required human approval have passed | Regress when a defect is found |

The existing project chooses representation. When file-level and entry-level states coexist, validate agreement and derive one from the other when possible.

`references/strategy/translation-workflow.md` §5.1 defines the boundary between established checks and language heuristics. Heuristics may generate human-review candidates but must not decide translation fitness from detection alone.

## 5. Build-input eligibility

Builds distinguish development or PoC input policy from release-candidate input policy. Development may continue before review of the declared localization scope is complete.

- A **development or PoC build** may explicitly select an ineligible translation produced under `references/strategy/translation-workflow.md` §3.1, but must carry a non-distribution marker its own build verifies. It must preserve extraction-baseline source text for unselected ineligible entries or fail. It must not mix ineligible translations silently or select output from a model or agent that failed evaluation. It may proceed with unmapped characters only when the unmapped set is declared and recorded with the artifact.
- A **pre-release test build** may be distributed to identified testers to obtain the human review a release candidate requires. It states which parts of the declared localization scope it covers, which remain unresolved, and every known critical defect. Reports return units to the states in §4 and establish no eligibility by themselves.
- A **release-candidate build** consumes only eligible translations within declared localization scope. Content intentionally left outside that scope, such as source branding or symbols, requires an approved exception recording the content, the reason, and the approving human. The build consumes that record and fails on unlisted content.

Distribution eligibility includes at least:

- protected fields match the extraction baseline;
- no missing translation, unapproved residual source character, or unknown state remains;
- token boundaries and argument widths are established so `references/strategy/text-extraction.md` §4.4 policies apply;
- control-code tokens parse and satisfy the policy assigned under `references/strategy/text-extraction.md` §4.4;
- glyph coverage and length or layout under confirmed consumer constraints pass; and
- the decision and supporting evidence for each human judgment are retained.

A failed check or new evidence revokes eligibility and returns the unit to the required review state. The decision, not a state name or storage location, determines build input.

When merging parallel or sequential batches, verify that each batch's extraction, context, terminology, and voice baselines and protected fields match current approved baselines and that stable IDs have no omissions, duplicates, or conflicts. Revalidate affected output after an extraction-baseline change. Conflicting translation, state, or evidence for one entry must remain for explicit review rather than being resolved by input order or last-writer-wins.
