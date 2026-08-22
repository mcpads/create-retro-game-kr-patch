# Translation asset conventions

Preserve source text, review state, reversible control codes, and build-input eligibility required by translation strategy using the information and checks below. Retain an existing schema or work-management system that provides equivalent information and validation, including its serialization, directories, and field names.

## Contents

1. Required information
2. Representation boundary
3. Control-code tokens
4. Workflow states
5. Build-input eligibility

## 1. Required information

A translation-asset representation must distinguish at least:

- provenance identifying the source image and extraction region;
- stable entry identity that can be matched after re-extraction;
- source bytes and the decoded result derived from them;
- translator-authored wording and each selected wording decision, with stable identity and applicability;
- when a scope-specific wording decision differs from a broader applicable selection, their stable relationship, rationale, semantic impact, and approval;
- states distinguishing untranslated, in progress, needs review, needs human judgment, and distribution-eligible;
- evidence for adaptation, wording decisions, and unresolved interpretations; and
- structure required for reinsertion, or a stable link to analysis and build data containing it.

Source bytes, source text, structural information, and source or structural link identities in a translation asset are protected. Translation work may change only authored wording, wording selection, the applicability and lineage of a wording decision, review state, and decision evidence. A protected change requires re-extraction or an explicit structural change.

Do not duplicate wording when the same approved wording is reused unchanged. When a scope-specific wording decision differs, preserve both decisions and identities through structured fields or stable links; a free-form note alone does not provide a stable relationship. Follow `references/strategy/translation-workflow.md` §4.1 and §5.6 for authority and invalidation.

Apply `references/conventions/data-formats.md` to character mappings, raw control-code specifications, pointer catalogs, and reinsertion policy. A translation asset may link to them by stable ID and source identity or preserve protected information inside an established integrated artifact. Edit each value in only one location.

`references/strategy/translation-workflow.md` §3.1 determines agent translation and review-batch inputs. Preserve the protected values and extraction-baseline versions provided to a batch so the merge process can compare them with the current extraction baseline. Even when a batch copy displays these values, maintain each baseline in one location and never overwrite protected fields from an agent response.

Translations produced while evaluating another model or agent must identify the evaluation scope, conditions, and provenance. A human-approved sample may enter work in progress only if its source baseline, protected information, context, terminology, and voice still match the evaluated conditions. Evaluation does not complete review or grant distribution eligibility. Output that failed evaluation must not become build-selected translation.

Immediately before merging or reinserting, compare source identity and raw bytes against the supported source or the current extraction baseline regenerated from it, not merely against metadata copied among batches. A mismatch identifies output from an older baseline; do not merge until its impact has been assessed.

### 1.1 Approved terminology and voice decisions

The authoritative record for approved terms, repeated expressions, and voice must include a stable decision ID; the source referent or situation; the approved output; applicability by title, revision, scene, speaker relationship, and narrative point; evidence and transfer limit; and an approved, unresolved, or conflicting state. Because one source term may have scope-specific decisions, do not use the source string as a globally unique key. When new evidence changes a decision, retain enough lineage to identify affected batches requiring revalidation; do not silently overwrite it. The project chooses file count, table structure, and field names.

## 2. Representation boundary

Use a machine-readable representation satisfying `references/conventions/project-conventions.md` §3.2. Keep empty source slots in the established order and count, represent duplicate pointers and undecoded bytes without loss, and distinguish extractor-owned source values from authored wording. When one entry has several authored or scope-specific wording decisions, record their identities, applicability, selection, and lineage instead of overloading one text or notes field.

## 3. Control-code tokens

Represent control codes in human-editable source and translated text as tokens that map bijectively to their original bytes, including arguments and unresolved codes whose boundaries are established. Define escaping for literal syntax collisions. `references/strategy/text-extraction.md` §4.4 determines each token's policy. Build-input checks compare token set, order, parameters, and transformed output according to the applied policy; they do not require one-to-one position for every token.

## 4. Workflow states

Work management must distinguish at least these states. Names are examples:

| Example state | Meaning | Condition for transition |
|---|---|---|
| `untranslated` | Extraction baseline present, no translation | Work begins |
| `in_progress` | Translation or correction underway | Entry translation and established-constraint checks pass |
| `needs_review` | Awaiting independent review | Independent review completes, flagged language-heuristic candidates are reviewed, and established-constraint failures are resolved |
| `needs_human_review` | Human judgment required | Human decision and approval with evidence |
| `distribution_eligible` | Established checks and required human approval have passed | A defect or invalidating change returns the unit to the relevant prior state |

The existing project chooses representation. When file-level and entry-level states coexist, validate agreement and derive one from the other when possible.

`references/strategy/translation-workflow.md` §5.1 defines the boundary between established checks and language heuristics. Heuristics may generate human-review candidates but must not decide translation fitness from detection alone.

## 5. Build-input eligibility

Builds distinguish development or PoC input policy from release-candidate input policy. Development may continue before review of the declared localization scope is complete.

- A **development or PoC build** may explicitly select an ineligible translation produced under `references/strategy/translation-workflow.md` §3.1, but must carry a non-distribution marker that the build itself verifies. It must preserve extraction-baseline source text for unselected ineligible entries or fail. It must not mix ineligible translations silently or select output from a model or agent that failed evaluation. It may proceed with unmapped characters only when the unmapped set is declared and recorded with the artifact.
- A **pre-release test build** may be distributed to identified testers to obtain the human review a release candidate requires. It states which parts of the declared localization scope it covers, which remain unresolved, and every known issue relevant to the test, including severity under the current quality target and accepted limitations. Reports return units to the states in §4 but do not make them eligible by themselves.
- A **release-candidate build** consumes only eligible translations within the declared localization scope. Content intentionally left outside that scope, such as original branding or symbols, requires an approved exception recording the content, the reason, and the approving human. The build consumes that record and fails on unlisted content.

Distribution eligibility includes at least:

- protected fields match the extraction baseline;
- no missing translation, unapproved residual source character, or unknown state remains;
- token boundaries and argument widths are established so `references/strategy/text-extraction.md` §4.4 policies apply;
- control-code tokens parse and satisfy the policy assigned under `references/strategy/text-extraction.md` §4.4;
- glyph coverage and length or layout under confirmed consumer constraints pass;
- the build-selected wording and layout match their recorded identities, and any scope-specific wording selection retains its relation, applicability, and required approval; and
- the decision and supporting evidence for each human judgment are retained.

A failed check or new evidence revokes eligibility and returns the unit to the required review state. The decision, not a state name or storage location, determines build input.

When merging parallel or sequential batches, verify that each batch's extraction, context, terminology, and voice baselines and protected fields match current approved baselines and that stable IDs have no omissions, duplicates, or conflicts. Revalidate affected output after an extraction-baseline change. Conflicting translation, state, or evidence for one entry must remain for explicit review rather than being resolved by input order or last-writer-wins.
