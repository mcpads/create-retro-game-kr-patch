# Font strategy

Determine the target revision's code-to-glyph mapping, total repertoire, state-specific active working sets, representation, and verification criteria. Do not assume a font product, conversion tool, cell size, or cache implementation. Investigate constraints that can change the design, and keep distinct budgets separate.

## 1. Conditions to establish

Investigate a question only when its answer can change a later choice:

- Which dialogue, UI, battle, and graphics consumers share a code table and glyph provider?
- Which characters are required by the distribution corpus and runtime insertion values?
- How does a stored code reach glyph selection and pixel consumption?
- What limits the total repertoire, and what separately limits glyphs active in one state?
- Which cell, bit depth, layout, palette, and clearing range does the real consumer require?
- Can the adopted glyph source and transform inputs be reproduced and distributed?

Read the applicable `references/platforms/` document for hardware or media facts that change a branch. Use a conditional test from `references/strategy/poc.md` when pixel reachability or capacity remains design-changing and unresolved.

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

- Consider a fixed precomposed representation when the target can accommodate its code, storage, active-slot, and consumer-path requirements.
- Consider composition or a hybrid representation when the target can accommodate its component storage, mapping, runtime generation, clearing, and lifetime requirements.
- Treat an existing composition or dynamic glyph path as one candidate. Verify its input range, state lifetime, and output before adopting it.

No representation guarantees readability, layout fitness, or lower total cost. Compare candidates against the measured repertoire, storage, active working set, runtime work, and visual target.

When a representation compresses an established finished font, define the supported output and verify every glyph against the declared pixel or visual equivalence. Verify serialized data with an independent decoder. Apply `references/strategy/name-entry.md` §5 when the representation serves player-created text.

## 3. Total repertoire and active working set

### 3.1 Two different budgets

| Budget | Compared population | Typical constraints |
|---|---|---|
| **Total repertoire** | Every unique glyph required by the distribution corpus and runtime inputs | Code space, on-media storage, persistent mapping and catalog representation |
| **Active working set** | Glyphs that must coexist throughout their proven consumption lifetime, including transitions across which slots remain live | Active RAM or VRAM, texture slots, index representation, transfer and replacement timing |

Only a design that keeps every glyph in fixed one-to-one slots may treat the active-slot budget as the total-repertoire limit. With verified dynamic loading or remapping, compare the complete corpus with the total-repertoire budget and each runtime state with the active budget separately.

Classify index width by role. A code that directly selects a permanent slot limits the total repertoire. A code remapped to a state-specific active slot limits the working set and mapping table. Static array size alone does not decide the role.

### 3.2 Budget decision

Before finalizing corpus demand, establish distribution scope and unresolved regions through `references/strategy/text-extraction.md` §1.5.

- Count required glyphs across the complete distribution corpus and actual runtime insertion values. An unfinished translation sample is a risk signal, not a final bound.
- Measure code-space, storage, mapping, and active-slot limits from target consumers and record each value's applicability.
- Fail the build on an unmapped character, a required glyph that rasterizes empty, or applicable budget overflow. Report the missing set, and the limiting resource for an overflow. A development build follows `references/conventions/translation-artifacts.md` §5.
- Count non-glyph resources, unused slots, or source glyphs eliminated by complete translation as supply only after excluding every reference and state. State whether this expands total repertoire or active working set.
- If total repertoire is insufficient, establish the exact bottleneck and feasible supply, wording, and scope alternatives far enough to compare their cost and effect. Vocabulary reduction or character substitution requires a human decision when it changes approved terminology, names, hints, characterization, meaning, or voice; record a material choice under `references/conventions/project-records.md` §1.1.
- If the active budget is smaller than a state's working set, prove that load, replacement, pinning, and release preserve every glyph throughout its consumption lifetime. Otherwise the dynamic design fails.

For player-created text, total demand includes the complete allowed input set rather than only the translated corpus. Apply `references/strategy/name-entry.md` §1 and §5 to membership, stored identity, composition, and later consumer demand.

When demand must shrink, do not rank candidates by occurrence count alone. Compare the unique-glyph delta, distribution by scene, speaker, and function, available synonymous phrasing using existing glyphs, and effects on approved terminology, names, hints, and characterization. Replacing many occurrences of one glyph saves one slot; introducing another glyph may save none.

Other phrasing adjustments follow `references/strategy/translation-workflow.md`.

If a glyph asset change triggers `references/strategy/runtime-assets.md` §1, verify the links in `references/strategy/runtime-assets.md` §2 as well.

## 4. Glyph sources and representation

Do not set a global font family, source class, cell size, bit depth, or transform. Established fonts and project-authored glyph sets, including sets authored with generative tools, are source candidates. Select candidates whose differences can change the decision under the approved visual target, provenance and distribution conditions, required coverage, cost, or target consumer. An established font is often a low-cost candidate when its source and coverage are known; a generatively authored set is permitted when the intended visual direction warrants new letterforms. Do not require every source class to be compared when current evidence has already made one irrelevant.

Generative authoring produces design candidates. A human selects the visual direction and exact glyph set. If the agent would otherwise invent letterforms through fixed stroke rules, geometric primitives, or ad hoc per-pixel plotting, use an identifiable established font as the letterform source and treat the procedure as a deterministic transform or correction instead. This does not prohibit a verified runtime representation that composes adopted initial, medial, final, or other component glyphs; representation and consumer behavior remain separate from letterform authorship.

Once selected, the exact authored asset becomes an identified project input. Record the selected asset's identity and approval scope, the authoring provenance, references, and tool conditions needed to review or revise it, and the rights basis for the intended distribution. Exact regeneration of a nondeterministic creative process is not a build requirement when the selected asset itself is fixed. The primary build consumes that asset and deterministically performs rasterization, sizing, adjustment, packing, and mapping; it does not rerun creative generation. A newly generated result is a new candidate input and requires the affected visual decisions and evidence to be reassessed.

Local additions or corrections are a low-cost choice when an established font otherwise meets the approved target. Do not infer a need for a new set merely from PoC convenience. A complete custom font, whether made through conventional or generative authoring, remains a human product and visual-design choice when the approved target justifies its cost. When limited additions cannot cover the selected scope, treat it as one technical option and present any material cost, quality, or scope tradeoff under `references/conventions/project-records.md` §1.1.

Font names, stated use or size labels, and previews only narrow the candidates. Distinguish functional failures such as missing glyphs, empty output, clipping, and spacing errors from aesthetic preferences such as stroke impression or mood. Require fill, outline, shadow, highlight, or gloss only when they are part of the approved visual target or necessary for readability or state distinction on the real consumer path. Do not make one source style or effect a global default.

Adoption requires all of these:

- Every required glyph exists, and actual ink remains within the cell and clearing range.
- Samples include continuous translated sentences, syllables carrying final consonants, compound vowels, and high stroke density, and the spaces, punctuation, digits, and Latin characters used on the path.
- On the real background and palette, those samples retain contrast and readability, maintain consistent baselines, line heights, and spacing, avoid clipping at cell, window, and screen bounds, and do not overlap adjacent UI.
- Every required fill, outline, shadow, highlight, or gloss layer retains its intended role in consumed output.
- The exact selected asset and its approval scope are identified. A third-party source has an exact version and license; a project-authored asset has sufficient provenance and a rights basis for the intended distribution.
- Fixed selected assets and transform rules reproduce the same game data without rerunning creative generation.
- Output satisfies the consumer's layout, bit depth, palette, and subtile ordering.

Reusing the game's existing glyph presentation may minimize impact but is not mandatory. If cell, bit depth, layout, or bytes per glyph change, update and verify every address calculation, transfer length, index, clearing, and layout rule that consumes them. If stored and active representations differ, establish the transform boundary and buffer lifetime separately.

## 5. Multiple render paths

When dialogue, UI, name entry, or graphics paths use different providers or representation rules, determine code table, glyph source, cell, and budgets per path. Do not generalize one path's PoC to the whole game.

Use one explicit input when several paths truly share presentation parameters. Split font-rendering profiles only when parameters differ and one setting would overwrite another or make build and review output disagree. Record profile definitions under `references/conventions/data-formats.md` §6.

Keep revision-specific structural constants such as addresses, banks, and code boundaries separate from presentation tuning. Preserve those constants as explicit specification with expected bytes.

## 6. Completion

Font work is complete only when all of these hold:

- Every required character in the distribution scope maps through an approved mapping for each target consumer, with zero unmapped characters.
- Total repertoire and every active working set with distinct membership or lifetime pass their corresponding budgets.
- Transform boundaries pass verification against source samples or a declared semantic-equivalence criterion.
- Representative sentences and boundary glyphs render correctly on every target path without invading adjacent UI or graphics.
- A glyph asset change triggered under `references/strategy/runtime-assets.md` §1 passes the link assessment in `references/strategy/runtime-assets.md` §2.
- Adopted sources or selected authored assets, mappings, structural constants, and evidence remain identified build inputs and records.
