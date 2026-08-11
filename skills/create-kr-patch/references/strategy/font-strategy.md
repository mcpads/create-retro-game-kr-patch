# Font strategy

Determine the target revision's code-to-glyph mapping, stored repertoire, state-specific active working sets, representation, and verification criteria. Do not assume a font product, conversion tool, cell size, or cache implementation. Investigate constraints that can change the design, and keep distinct budgets separate.

## 1. Conditions to establish

Investigate an answer when it can change a later choice:

- Which dialogue, UI, battle, and graphics consumers share a code table and glyph provider?
- Which characters are required by the distribution corpus and runtime insertion values?
- How does a stored code reach glyph selection and pixel consumption?
- What limits the complete stored repertoire, and what separately limits glyphs active in one state?
- Which cell, bit depth, layout, palette, and clearing range does the real consumer require?
- Can the adopted glyph source and transform inputs be reproduced and distributed?

Read the applicable `references/platforms/` document for hardware or media facts that change a branch. Use a conditional test from `references/strategy/poc.md` when pixel reachability or capacity remains design-critical and unresolved.

## 2. Character-code-to-glyph mapping

### 2.1 Reusing an existing code space

Assign an apparently free code, lead, pair, or slot only when all of these conditions hold:

1. The distribution string population and parser-reachable candidate range are established.
2. Source characters, external characters, control tokens, terminators, and reserved values are distinguished.
3. Every decoder, lookup, and bypass path consuming the value understands the new mapping.
4. Encoder, decoder, font builder, and validators consume the same explicit mapping.
5. An undeclared source value or new collision fails the build.

A non-distribution PoC with unresolved population may use a temporary mapping only for its declared representative scope. It does not prove collision freedom or the unused-code set for distribution.

A standard decoder returning no character, or zero occurrences in one file, does not prove a value unused. Preserve source-used combinations. Reuse the remainder only if every consumer can distinguish it safely.

A reservation remains while the source consumes the character. It may become a reassignment candidate after the declared localization scope removes every source use. Do not reclaim it if non-text graphics use the slot, untranslated or approved exceptional content still needs it under `references/conventions/translation-artifacts.md` §5, or an external provider such as BIOS or font ROM supplies it.

For a fixed supported revision, treat exhaustively verified code sets and mappings as explicit specification, not heuristics. Use heuristic search only to find candidates or audit specification drift; never let the build choose an arbitrary fallback mapping.

### 2.2 Precomposed and compositional Hangul

- Consider precomposed glyphs when the complete repertoire fits and the existing one-code-to-one-glyph path can consume it.
- Consider composition when the complete repertoire cannot fit, supply cannot be expanded, and an additional composition, placement, and clearing path can be verified.
- An existing composition or dynamic glyph path is only a candidate. Verify its input range and state lifetime before applying it to Hangul.

Neither representation guarantees readability in a small cell or layout fitness. Judge the target output.

## 3. Total repertoire and active working set

### 3.1 Two different budgets

| Budget | Compared population | Typical constraints |
|---|---|---|
| **Total repertoire** | Every unique glyph required by the distribution corpus and runtime inputs | Code space, on-media storage, persistent mapping and catalog representation |
| **Active working set** | Glyphs that must coexist during one screen, scene, or frame interval | Active RAM or VRAM, texture slots, index representation, transfer and replacement timing |

Only a design that keeps every glyph in fixed one-to-one slots may use the smaller budget as a global glyph limit. With verified dynamic loading or remapping, compare the complete corpus with the total-repertoire budget and each runtime state with the active budget separately.

Classify index width by role. A code that directly selects a permanent slot limits the total repertoire. A code remapped to a state-specific active slot limits the working set and mapping table. Static array size alone does not decide the role.

### 3.2 Budget decision

Before finalizing corpus demand, establish distribution scope and unresolved regions through `references/strategy/text-extraction.md` §1.5.

1. Count required glyphs across the complete distribution corpus and actual runtime insertion values. An unfinished translation sample is a risk signal, not a final bound.
2. Measure code-space, storage, mapping, and active-slot limits from target consumers and record each value's applicability.
3. Fail the build on an unmapped character or applicable budget overflow, and report the missing set and limiting resource.
4. Count non-glyph resources, unused slots, or source glyphs eliminated by complete translation as supply only after excluding every reference and state. State whether this expands total repertoire or active working set.
5. If total repertoire is insufficient, establish the exact bottleneck and determine whether supply can expand. Vocabulary reduction or character substitution requires human approval when it changes meaning or voice.
6. If the active budget is smaller than a state's working set, prove that load, replacement, pinning, and release preserve every glyph throughout its consumption lifetime. Otherwise the dynamic design fails.

When demand must shrink, do not rank candidates by occurrence count alone. Compare the unique-glyph delta, distribution by scene, speaker, and function, available synonymous phrasing using existing glyphs, and effects on approved terminology, names, hints, and characterization. Replacing many occurrences of one glyph saves one slot; introducing another glyph may save none.

Changes to approved terminology, names, hints, characterization, meaning, or voice require human approval. Other phrasing adjustments follow `references/strategy/translation-workflow.md`.

If a glyph asset change triggers `references/strategy/runtime-assets.md` §1, verify the links in `references/strategy/runtime-assets.md` §2 as well.

## 4. Glyph sources and representation

Do not set a global font family, cell size, bit depth, or transform. Unless evidence requires new letterforms, begin with an established font whose provenance, distribution terms, and required character coverage are known. Compare candidates by sending the same strings through the target game's transform. Do not draw a new character set when size, baseline, rasterization, or margin adjustments make an existing source meet the requirement.

Author or correct glyphs only after an established font supplies the main character set, and only for local missing symbols or glyphs that still fail an established UX requirement such as readability or state distinction. If the adopted font lacks `…`, add that symbol rather than redrawing Hangul. Consider a complete custom font only when limited additions cannot cover the distribution scope and an established UX requirement justifies the larger design.

Font names, stated uses or sizes, and previews only narrow candidates. Distinguish functional failures such as missing glyphs, empty output, clipping, and spacing errors from aesthetic preferences such as stroke impression or mood. Require fill, outline, shadow, highlight, or gloss only when they are part of the approved visual target or necessary for readability or state distinction on the real consumer path. Do not make one source style or effect a global default.

Adoption requires:

- Every required glyph exists, and actual ink remains within the cell and clearing range.
- Samples include continuous translated sentences, dense Hangul forms, and the spaces, punctuation, digits, and Latin characters used on the path. On the real background and palette they retain contrast and readability, align baseline, line height, and spacing, avoid clipping at cell, window, and screen bounds, and do not overlap adjacent UI.
- Every required fill, outline, shadow, highlight, or gloss layer retains its intended role in consumed output.
- The exact source version and license permit distribution of derivatives and any required source files.
- Fixed inputs and transform rules reproduce the same game data.
- Output satisfies the consumer's layout, bit depth, palette, and subtile ordering.

Reusing source presentation may minimize impact but is not mandatory. If cell, bit depth, layout, or bytes per glyph change, update and verify every address calculation, transfer length, index, clearing, and layout rule that consumes them. If stored and active representations differ, establish the transform boundary and buffer lifetime separately.

## 5. Multiple render paths

When dialogue, UI, name entry, or graphics paths use different providers or representation rules, determine code table, glyph source, cell, and budgets per path. Do not generalize one path's PoC to the whole game.

Use one explicit input when several paths truly share presentation parameters. Split target profiles only when parameters differ and one setting would overwrite another or make build and review output disagree. The project chooses profile serialization and override mechanisms, but unknown targets, values, and omissions must fail.

Keep revision-specific structural constants such as addresses, banks, and code boundaries separate from presentation tuning. Preserve those constants as explicit specification with expected bytes.

## 6. Completion

Font work is complete only when:

- Every required character in the distribution scope maps through an approved mapping for each target consumer, with zero unmapped characters.
- Total repertoire and representative runtime working sets pass their corresponding budgets.
- Transform boundaries pass source samples or a declared semantic-equivalence criterion.
- Representative sentences and boundary glyphs render correctly on every target path without invading adjacent UI or graphics.
- A glyph asset change triggered under `references/strategy/runtime-assets.md` §1 passes the link assessment in `references/strategy/runtime-assets.md` §2.
- Adopted sources, mappings, structural constants, and evidence remain reproducible build inputs and records.
