# General decision cases

## Pointer gaps do not define string boundaries

- **Search terms:** overlapping strings, shared tail, next pointer, terminator, nested script entries
- **Observed scope:** Overlapping script entries in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** The relocator treated the next scene pointer as the end of the current scene. Several entry points actually shared later dialogue and portrait controls and continued to the same terminator.
- **Decisive test:** For every scene start, the actual terminator was located and compared with the next scene start.
- **Established result:** The next scene pointer was not an end boundary; multiple scenes consumed a shared tail through the same terminator.
- **Transfer limit:** Determine overlap from each entry point's actual consumption range through its terminator.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3.

## Shared glyph slots have multiple consumers

- **Search terms:** shared glyph slot, tile alias, font collision, name-entry digits, reused graphics
- **Observed scope:** Shared glyph and tile slots across Dreamcast, SNES, Game Gear, Saturn, and PlayStation displays.
- **Failure context:** Changing a slot for one screen broke other labels, decoration, or numeric displays that consumed the same physical slot. On PlayStation, replacing name-entry digit codes also damaged month and day rendering.
- **Evidence:** All known consumers of each slot were enumerated. The fixes either allocated a new slot and updated its references, preserved shared pixels, or kept the date digit codes while changing only the remaining name-entry candidates.
- **Established result:** A physical slot was not owned by the first screen where it was found. Reassigning it without tracing shared consumers damaged other displays.
- **Transfer limit:** Enumerate text and non-text consumers again for every asset, then choose new allocation, shared-pixel preservation, or reference updates from the proven sharing relation.
- **Related criteria:** `references/strategy/font-strategy.md` §2·§5, `references/strategy/graphics-text.md` §2·§3, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4.

## Runtime screen evidence corrected extraction labels

- **Search terms:** wrong extraction label, metadata mismatch, tile indices, mislabeled segment, screen evidence
- **Observed scope:** Option and pause labels in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** A human-authored Japanese metadata label was translated even though it disagreed with the phrase assembled by the screen's tile indices. Removing the presumed display path did not remove the bad label.
- **Decisive test:** The segment's tile indices were decoded directly from the binary and their assembly order was retraced.
- **Established result:** A label attached during extraction was not source-text evidence. The tile data actually consumed by the screen corrected the mislabeled entry.
- **Transfer limit:** A removal test cannot isolate a labeling error if it also changes the input data or assembly order.
- **Related criteria:** `references/strategy/debugging.md` §2.2·§6, `references/strategy/text-extraction.md` §1.2·§4.2.

## Zero-filled space is not proven free

- **Search terms:** false free space, zero-filled region, no static references, indirect call, first boot crash
- **Observed scope:** Candidate insertion regions in a Dreamcast label table and Saturn executable code.
- **Failure context:** A zero-filled Dreamcast range with no patch overlap and a Saturn function with no direct calls or value references were treated as unused. The first failed on a clean boot; the second was called indirectly during dungeon entry.
- **Decisive test:** The first invalid instruction exposed overwritten conversion code and constants. After they were restored and the connected tables were relocated with all references fixed, the title booted cleanly and gameplay proceeded. Saturn candidates were tested with isolated trap builds along the same play path; non-execution was recorded only for the observed path.
- **Established result:** Zero-filled data and lack of static references did not prove free space. Observed execution proved use, while non-execution in a limited run did not prove global non-use.
- **Transfer limit:** Any unobserved mode, path, or later section limits the corresponding code- or data-space claim.
- **Related criteria:** `references/strategy/reinsertion.md` §4·§5, `references/strategy/initial-survey.md` §2.5·§3, `references/strategy/debugging.md` §6, `references/conventions/project-conventions.md` §5.2.

## Shorter dialogue can change voice timing

- **Search terms:** voice desync, dialogue timing, wait frames, shorter translation, early audio cutoff, padding
- **Observed scope:** Voice-synchronized dialogue windows and wait or transition controls in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** Shorter Korean text caused later voice lines to be cut off progressively earlier. Padding the unused scene bytes back to the original size was proposed as a timing fix.
- **Evidence:** Disassembly showed that bytes after the transition control were not consumed. Controlled wait-value changes altered both visible pacing and voice cutoff in scene-level runtime tests.
- **Established result:** Timing on this path depended on wait frames and per-line glyph display time, not serialized byte length. Unconsumed tail padding was removed and only missing display time was restored.
- **Transfer limit:** Measure wait structure, line layout, and the actual voice boundary separately for every scene.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1·§3.2, `references/strategy/translation-workflow.md` §4, `references/strategy/build-and-verify.md` §5.

## Generated layouts invalidate stale fixed writes

- **Search terms:** overlapping writes, stale fixed offset, literal pool corruption, generated layout, write ownership
- **Observed scope:** Generated code and its literal pool in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** After layout became generator-controlled, a leftover fixed-address write still overwrote the literal pool at its new location.
- **Evidence:** The generated ranges and manual writes were compared in the final binary and shown to modify the same bytes.
- **Established result:** Removing the obsolete direct write and leaving one generator responsible for the range eliminated the literal-pool corruption.
- **Transfer limit:** Recompute final write ranges and overlap for every new layout.
- **Related criteria:** `references/strategy/build-and-verify.md` §1, `references/conventions/project-conventions.md` §5.2.

## Apparent disc gaps overlapped file extents

- **Search terms:** disc free space, LBA overlap, file gap, opening movie corruption, relocation, directory extents
- **Observed scope:** Relocated data-track files and an opening movie in a Dreamcast disc image.
- **Failure context:** A large gap between files was assumed free, causing a relocated file to overlap a later movie extent.
- **Evidence:** Every root-directory LBA extent was compared with the relocation result. A build placed after the last recorded occupied extent played the opening movie successfully.
- **Established result:** New data was placed only after accounting for every file extent recorded by the directory, preventing movie overwrite in this image.
- **Transfer limit:** This placement rule applies only when the directory completely describes occupied regions and track, volume, and contiguity constraints are also satisfied.
- **Related criteria:** `references/strategy/reinsertion.md` §5, `references/strategy/build-and-verify.md` §2·§4.

## Font filenames do not identify the active font

- **Search terms:** wrong active font, multiple font sizes, font filename, glyph sheet probe, code-to-glyph mismatch
- **Observed scope:** One story-dialogue screen and multiple font sizes in the Dreamcast release of Sakura Wars 2.
- **Failure context:** A prior small-font experiment and filenames were used to assume that story dialogue used the same font. Slot numbers derived from one size were also transferred to another.
- **Evidence:** Distinctive probes were inserted across each candidate sheet. Runtime display selected a different sheet from the earlier experiment, and independent decoding showed that the same character occupied different slots between sizes.
- **Established result:** The active dialogue font and its code-to-glyph mapping had to be established independently; mappings were not shared across font sizes.
- **Transfer limit:** Prove the active font and that sheet's code-to-glyph mapping separately for every other screen.
- **Related criteria:** `references/strategy/font-strategy.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/poc.md` §3·§5.

## Final display-buffer tracing corrected coordinate assumptions

- **Search terms:** wrong window base, shifted price, dialogue order, staging buffer, final VRAM copy
- **Observed scope:** Shop prices and the Hangul renderer in the Game Gear release of Madou Monogatari 1.
- **Failure context:** Prices moved to the bottom of the window instead of appearing beside `금`, and later dialogue order also drifted. The final VRAM write only copied a completed row, so the price cursor was not the direct cause.
- **Decisive test:** Changes were traced backward from the work buffer to the VRAM transfer, and each window's tile base was compared with the original initialization table. Separating the shared-window and normal-window base values fixed both price placement and dialogue order.
- **Established result:** The wrong base selected before drawing the window, not the final price write, caused both symptoms.
- **Transfer limit:** Reconfirm slot placement and per-window base selection for every other UI.
- **Related criteria:** `references/platforms/gg.md` §4, `references/strategy/debugging.md` §3·§4.

## Late observation can miss one-time asset uploads

- **Search terms:** late breakpoint, save state, one-time VRAM upload, missed producer, cached asset
- **Observed scope:** A VRAM upload performed during scene initialization on Game Gear and a scrolling banner written once at scene start on SNES.
- **Failure context:** A save state retaining old VRAM or a breakpoint armed after the screen appeared was used to reject the real source candidate and write path. In both cases the load or write had already finished.
- **Decisive test:** Observation started before boot or scene entry, and the modified stored source was followed through loading and transfer to its consumer.
- **Established result:** A save state or late breakpoint did not prove the absence of a one-time load or write that had already occurred.
- **Transfer limit:** Start before the relevant load or write when a screen reuses cache or VRAM. Use save states only to reproduce later consumer behavior.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §2.1·§4.

## Decoder correction left stale-source translations

- **Search terms:** decoder correction, stale translation, raw 0x7F, Japanese full stop, impact audit
- **Observed scope:** Early Japanese decoding for the Game Gear release of Madou Monogatari 1 and Korean translations derived from it.
- **Failure context:** An old decoder rendered raw `0x7F` as an asterisk, but source and screen comparison established it as Japanese `。`. Fixing only the decoder and extracted source left many stale asterisks and misinterpretations in the Korean translation.
- **Decisive test:** ROM frequency and context, runtime samples, and another source version established the punctuation. Every Korean asterisk position was then audited, retranslated where affected, and cross-reviewed.
- **Established result:** Correcting an upstream decoder did not repair translations already authored from its wrong output; the affected translation set required its own source comparison.
- **Transfer limit:** Do not infer the impact from a character search alone. Compare stable source identities with the changed decoding rule and audit the full affected range.
- **Related criteria:** `references/conventions/translation-artifacts.md` §1·§5, `references/strategy/translation-workflow.md` §3.1, `references/conventions/data-formats.md` §2.

## Shared string tails constrain allocation

- **Search terms:** shared string tail, suffix deduplication, pointer table scope, bank allocator, aliasing
- **Observed scope:** Several Game Gear text pointer tables relocated into the same spare bank.
- **Decision context:** Sharing string suffixes saved space, but one global sharing pool across unrelated tables allowed a layout change in one table to break references in another.
- **Evidence:** Bank allocation remained shared while suffix candidates were rebuilt independently for every pointer table. All consumer paths ran correctly when sharing remained within each table.
- **Established result:** A suffix could be shared only within a table whose references used the same base, read path, lifetime, and change unit—not merely anywhere in the same physical bank.
- **Transfer limit:** Expand sharing only across tables proven to have the same reference representation, base, path, lifetime, and update boundary.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§5.

## Lost page-local controls changed portrait state

- **Search terms:** portrait control, page prefix, control-code count, expression order, missing token
- **Observed scope:** All translated entries and portrait-selection controls in the Game Gear release of Madou Monogatari 2.
- **Failure context:** Portrait controls disappeared during translation. Matching only the total control count could move the same value to another page or after visible text, changing expression timing.
- **Evidence:** Every source and translation page was checked for the same wait and output boundaries, and every original portrait control was confirmed before visible text. Value, order, duplication, and reset were restored per page, then compared against a control-free build and the actual handler state.
- **Established result:** Portrait changes were restored by matching control values and order in each page prefix, not by matching a whole-string count.
- **Transfer limit:** Use this correspondence only when page boundaries match and exhaustive evidence shows the controls live in page prefixes. Do not infer it across mid-page controls or changed page structure.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1·§3.3, `references/strategy/translation-workflow.md` §4, `references/conventions/translation-artifacts.md` §3.

## Equal raw bytes can have different consumer semantics

- **Search terms:** token semantic mismatch, same raw byte, prior patch, position control, punctuation code
- **Observed scope:** A Game Gear engine derived from an English-language release and a consumer in a Japanese NES release that assigned different meanings to the same raw values.
- **Failure context:** Variable and punctuation tokens from prior material were preserved numerically, but the target consumers interpreted them as literal string content or position controls.
- **Decisive test:** Each target token handler, pointer mapping, glyph mapping, and runtime value was compared with its source. Only confirmed static values became localized text, while position-control codes remained reserved from glyph allocation.
- **Established result:** Matching numeric tokens or glyph shapes in a prior patch did not establish matching semantics in the target engine.
- **Transfer limit:** Before preserving or replacing a token, re-establish its meaning and runtime variability in the target consumer.
- **Related criteria:** `references/strategy/translation-workflow.md` §3.1·§4, `references/strategy/text-extraction.md` §3.3·§4.4, `references/conventions/translation-artifacts.md` §3, `references/strategy/initial-survey.md` §4.

## Zero-length entries may point to runtime text

- **Search terms:** zero-length entry, external string pointer, runtime-composed text, WRAM string, null pointer
- **Observed scope:** A Game Gear string table and dynamic money or status text assembled for the field screen.
- **Failure context:** A zero-length entry was treated as an empty string and its pointer was cleared, causing the game to parse boot code as text.
- **Decisive test:** An exhaustive comparison of the original table showed that only the failing entries pointed outside the file bank into runtime-composed WRAM strings. Preserving the original pointers restored the display.
- **Established result:** Length zero represented an external runtime string reference in this range, not null or empty data.
- **Transfer limit:** Classify each empty-looking entry as null, empty text, an external range, or runtime-composed text before choosing how to preserve it.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§6, `references/strategy/runtime-assets.md` §2, `references/conventions/data-formats.md` §4.

## Shared hooks corrupted caller-specific state

- **Search terms:** shared hook, caller-saved register, Z80 B register, loop counter corruption, graphics plane state
- **Observed scope:** A glyph-expansion hook shared by two Game Gear text loops.
- **Failure context:** The hook used `B` as a temporary prefix index. That worked for one caller, but another used `B` as its per-line character counter, so return changed the loop into a wraparound and prevented screen transfer.
- **Decisive test:** Entry and return register meanings were compared across every caller of the shared routine. Preserving `B` and normalizing each caller's graphics-plane state restored glyph expansion and transfer on dialogue and field paths.
- **Established result:** The shared hook worked only after preserving the second caller's character counter and the plane state expected by each path.
- **Transfer limit:** Adopt a shared hook only after accounting for every observed caller's inputs, outputs, and original behavior. Re-derive preserved registers per path.
- **Related criteria:** `references/strategy/reinsertion.md` §4, `references/strategy/debugging.md` §3·§5.

## Layout limits vary by window state

- **Search terms:** dialogue width, window tag, page break, narrow window, line reflow, portrait state
- **Observed scope:** A narrow dialogue state and a page-transition control in the Game Gear release of Madou Monogatari 2.
- **Failure context:** Assuming one wide window for a script region missed a narrower state in the same region, while a width-only checker also rejected text that could be reflowed or moved to the next page.
- **Evidence:** Source pages were compared with the active window geometry and the overflow was reproduced. Width and row usage were checked after reflow, and continuous play confirmed that the control cleared the window, opened the next page, and preserved the first character.
- **Established result:** The active window tag, not the containing script region, determined capacity. Width and row count had to be evaluated together, with confirmed page transitions available for text that could not fit.
- **Transfer limit:** Before adding a page, verify that the control preserves portrait, window, input, and event state on that path.
- **Related criteria:** `references/strategy/text-extraction.md` §4.4, `references/strategy/translation-workflow.md` §4, `references/strategy/build-and-verify.md` §5, `references/strategy/reinsertion.md` §6.

## Cleanup behavior may be caller-specific

- **Search terms:** stale tiles, missing clear, caller-specific cleanup, bottom-aligned text, battle message residue
- **Observed scope:** A Game Gear battle window shared by a bottom-aligned critical-hit message and the preceding spell name.
- **Failure context:** After Korean alignment moved the standard message row, one critical-message caller failed to clear the window and left part of the previous spell name. Clearing all dialogue or changing the shared clear routine did not match the caller-local omission.
- **Decisive test:** Stale tiles were observed at the failure point and compared with normal messages drawn after a clear. Callers lacking a clear were enumerated, and only the failing caller was redirected through an existing clear-capable path.
- **Established result:** The residue came from caller-specific cleanup responsibility, not a defect in the shared clearing logic.
- **Transfer limit:** Before redirecting a path, verify each caller's prior clear, coordinates, alignment, and semantic role, then regress the unaffected callers too.
- **Related criteria:** `references/strategy/debugging.md` §3·§5, `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2.

## Missing control sequences stopped progression

- **Search terms:** missing terminator, cutscene end, control-code audit, false missing-token warning, progression stop
- **Observed scope:** Event scripts in the Mega Drive release of Madou Monogatari.
- **Failure context:** Entries that lost dialogue-end or cutscene-end controls stopped progressing after input. A simple set comparison also produced false warnings when a prior version split one source entry across adjacent entries.
- **Decisive test:** Control tokens were compared exhaustively per entry. Missing termination was classified as progression-critical, while adjacent split structure was inspected before accepting a warning.
- **Established result:** Real termination loss caused progression failure; token movement caused by an established adjacent-entry split did not.
- **Transfer limit:** Equal token sets do not prove equal order, arguments, or runtime meaning.
- **Related criteria:** `references/strategy/build-and-verify.md` §5, `references/strategy/text-extraction.md` §3.1·§4.4, `references/conventions/translation-artifacts.md` §3.

## String-only context misidentified speaker and display role

- **Search terms:** wrong speaker, dialogue attribution, system narration, reaction line, speaker control, series terminology
- **Observed scope:** Speaker-switching dialogue on Mega Drive and separate character-reaction and status-narration strings on PC-98.
- **Failure context:** Translating isolated strings collapsed multi-speaker dialogue into a monologue or turned a character's reaction into objective system narration.
- **Decisive test:** Speaker controls, the actual display window, and surrounding output order were compared with the source. Existing series translations were consulted only after their speaker and situation were shown to apply.
- **Established result:** The consumer path, not the string alone, determined speaker and display role.
- **Transfer limit:** Do not assign a role from similar wording or a prior translation. Limit the conclusion to entries whose speaker controls and display path are known.
- **Related criteria:** `references/strategy/translation-workflow.md` §2.4.

## Repeated glyph blocks may encode pre-shifted variants

- **Search terms:** pre-shifted glyph copies, variable-width font, four repeated blocks, X-coordinate alignment, clipped glyph
- **Observed scope:** 16x16 variable-width glyph data and its selector in the Mega Drive release of Madou Monogatari.
- **Failure context:** Four similar blocks per glyph looked duplicated or unused. Generating only one copy made glyphs disappear or clip at some horizontal alignments.
- **Evidence:** Consumer disassembly showed that the low two bits of the X coordinate selected one of four copies. The generator therefore produced glyphs shifted by 0, 1, 2, and 3 pixels.
- **Established result:** The repeated blocks were pre-shifted copies for variable-width alignment states.
- **Transfer limit:** Trace the copy-selection expression, composition method, and coordinate unit again to derive the required shifts for another renderer.
- **Related criteria:** `references/strategy/font-strategy.md` §4·§5, `references/strategy/runtime-assets.md` §2.

## Input glyphs and result glyphs may use different assets

- **Search terms:** name-entry candidates, result glyph mismatch, BNCG, MES font, NFTR no effect, multiple render paths
- **Observed scope:** Name-entry candidates and post-selection name rendering in revision 0 of the Japanese Nintendo DS release of Dragon Quest IX.
- **Failure context:** Replacing an `い` glyph in the apparent NFTR did not change the screen. It was easy to assume that the candidate grid and selected-name display shared one font because they belonged to the same UI.
- **Evidence:** A BNCG-only build changed only the candidate grid. Changing both BNCG and the matching MES slot made the grid, editing and confirmation displays, and later name displays agree.
- **Established result:** The candidate grid came from pre-rendered BNCG graphics, while the selected name came from MES glyphs. Both consumers had to change for one logical character slot.
- **Transfer limit:** Trace candidate and result supply paths separately for every screen. An NFTR that has no effect on one path remains a candidate elsewhere.
- **Related criteria:** `references/strategy/font-strategy.md` §5, `references/strategy/runtime-assets.md` §2.

## Asset expansion without metadata growth halted before title

- **Search terms:** white screen before title, container item count, font expansion, metadata layout, equal-size control build
- **Observed scope:** GP2 initialization and builds that added MES font entries to revision 0 of the Japanese Nintendo DS release of Dragon Quest IX.
- **Failure context:** A ROM with many added Hangul glyphs stayed on a white screen before the title. Code-table order, internal file size, and entry count changed together, so the failing boundary was not isolated.
- **Evidence:** Code order and MES expansion were separated. Builds differing by one internal entry changed the initialization result even without changing the candidate grid. A build that kept physical file size but restored the header and entry layout of a booting control reached the title again.
- **Established result:** Failure followed internal entry structure even when file size stayed equal; physical container growth alone did not explain this build set.
- **Transfer limit:** Separate physical size, entry count, metadata, and data placement with controlled builds. Treat initialization and actual consumption of the added assets as separate claims.
- **Related criteria:** `references/strategy/runtime-assets.md` §1·§2, `references/strategy/reinsertion.md` §1.2, `references/strategy/debugging.md` §2.2·§3.

## Image header mismatch hid required runtime memory

- **Search terms:** PRG-RAM header mismatch, prior patch, unmapped execution, analysis copy, iNES declaration
- **Observed scope:** An analysis copy of a prior English patch for the NES release of Parodius Da!.
- **Failure context:** The prior patch stored and read expanded data in PRG-RAM while its image header declared no PRG-RAM. After normal progress, execution jumped to an unmapped value and departed from valid control flow.
- **Decisive test:** After tracing the first control-flow departure, only the PRG-RAM declaration in the analysis copy was corrected. The same play path then continued.
- **Established result:** The header correction was necessary for studying that prior-patch copy, not evidence that a patch built from the Japanese original should change its header.
- **Transfer limit:** Correcting the declaration isolates this cause only; it does not validate the prior patch as a whole or authorize changing the production patch input.
- **Related criteria:** `references/strategy/initial-survey.md` §2.1·§3·§4, `references/strategy/build-and-verify.md` §1·§2, `references/strategy/debugging.md` §2.2.

## Standard-decoder rejection does not prove free code space

- **Search terms:** CP932 decoder rejection, custom Shift_JIS, unused lead byte, code-space collision, 0xEB
- **Observed scope:** A game-specific Shift_JIS-like consumer in the PC-98 Madou Monogatari titles.
- **Failure context:** Statistics limited to byte pairs accepted by standard CP932 classified lead byte `0xEB` as unused, while the source contained game-specific pairs rejected by the standard decoder.
- **Decisive test:** Every parser-reachable two-byte pair in the source was counted, game-specific pairs were reserved, and the Hangul encoder was verified not to emit them.
- **Established result:** `0xEB` was not free code space because the game consumed non-CP932 pairs under that lead byte.
- **Transfer limit:** This result covers direct two-byte codes only. Evaluate the code-space budget for escape forms of other lengths separately.
- **Related criteria:** `references/strategy/font-strategy.md` §2.1, `references/strategy/text-extraction.md` §2, `references/platforms/pc98.md` §5.

## Shared boundary logic let generator errors pass validation

- **Search terms:** shared generator bug, shared validator formula, JIS boundary, Shift_JIS 0x7F, exhaustive glyph display
- **Observed scope:** JIS-to-Shift_JIS conversion at an extension-row boundary in PC-98 titles.
- **Failure context:** An odd-row boundary formula mapped cell `0x5F` to forbidden trail byte `0x7F`. The glyph generator and validator shared the same error, so agreement between them did not expose it.
- **Evidence:** Independent enumeration of both row parities and runtime markers at the boundary established the required skip from `0x7E` to `0x80` and added a separate forbidden-value check.
- **Established result:** Independent boundary enumeration and real consumer display found a defect hidden by two components sharing one formula.
- **Transfer limit:** Do not establish an encoding boundary from generator-validator agreement when they share logic. Independently test forbidden and boundary values and compare them with the real consumer.
- **Related criteria:** `references/strategy/font-strategy.md` §2·§4, `references/strategy/build-and-verify.md` §4·§5, `references/conventions/project-conventions.md` §5.1.

## String pools can provide capacity beyond local gaps

- **Search terms:** pooled string region, long credits, NUL gaps, pointer table, relocation capacity, empty-entry sentinel
- **Observed scope:** Ending credits and a word pointer table containing empty-entry values in PC-98 titles.
- **Failure context:** Treating every NUL gap as an independent fixed slot could not fit longer Korean credits, while the consumer actually entered each string through the pointer table.
- **Evidence:** Every valid pointer target and update site was linked. Strings were repacked inside the established region, pointers were updated, overlay size and following code were preserved, and display plus next-entry progress were verified.
- **Established result:** The whole region, rather than each original gap, could provide capacity because its complete reference model preserved independent entry points.
- **Transfer limit:** Use pooled capacity only after establishing every entry pointer, empty sentinel, pointer width, and following structure boundary.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3·§5, `references/strategy/build-and-verify.md` §3·§4.

## Original-coordinate planning prevented multi-insertion drift

- **Search terms:** multiple growing regions, original-coordinate plan, reverse-order insertion, pointer-site shift, pointer-target shift
- **Observed scope:** Multiple expanded data ranges followed by pointers, directories, and structure addresses in PC-98 game files.
- **Failure context:** Changes safe in isolation could miss or duplicate corrections when later edits used already-shifted positions, or when pointer storage sites and pointer targets received the same accumulated delta.
- **Evidence:** Every change was planned in original coordinates and growing ranges were applied in descending original-offset order. Storage-site and target deltas were calculated separately, and following structures were assigned their final positions once. Static and runtime checks then covered the combined artifact.
- **Established result:** Original-coordinate planning, reverse application, and separate site-versus-target shifts moved each position-dependent structure exactly once.
- **Transfer limit:** Use reverse application only for an established set of original-coordinate variable ranges and following structures. Re-enumerate references, interior entry points, structure addresses, fixed constants, and load capacity on new input.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3, `references/strategy/build-and-verify.md` §3·§4, `references/conventions/project-conventions.md` §5.2.

## Pointerless strings may be fixed-position data

- **Search terms:** pointerless string, fixed absolute offset, leading menu names, compaction corruption, no rewritable reference
- **Observed scope:** Name strings before the first pointer target in a PC-98 menu-data file.
- **Failure context:** Compacting those leading strings because no pointer-table reference was visible made names blank or changed them to neighboring entries; a consumer read them at fixed offsets.
- **Decisive test:** Pointer tables and actual consumers were traced together. Confirmed fixed-offset strings remained in place with local fill, while later movable strings retained normal relocation.
- **Established result:** Absence of a rewritable pointer did not grant relocation permission; a consumer could read an absolute position directly.
- **Transfer limit:** Do not mark every pointerless entry fixed. Decide from the real consumer and the existence of a rewritable reference.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §1.2·§2·§3, `references/strategy/build-and-verify.md` §3·§4.

## Speculative splitting changed unknown shared consumers

- **Search terms:** shared string, unknown consumer, speculative split, neutral translation, alias set, semantic conflict
- **Observed scope:** Two PC-98 slots sharing one source string when only one slot's spell-learning consumer was known.
- **Failure context:** The known slot's meaning was used to break sharing and assign a different translation to the still-unknown slot, despite no evidence of a semantic difference.
- **Decisive test:** The accompanying name table and runtime display were compared. A translation valid for the confirmed scope remained shared, and splitting was deferred until the unknown consumer demonstrated a conflict.
- **Established result:** Identifying one consumer of a shared string did not establish the meaning of the other consumers.
- **Transfer limit:** Do not split shared entries based on semantic possibility alone. If a real conflict later requires a split, bind the evidence to the exact slot and alias set.
- **Related criteria:** `references/strategy/translation-workflow.md` §2.1·§2.3·§3, `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §2, `references/conventions/translation-artifacts.md` §1.1.

## Logical tile indices are not physical coordinates

- **Search terms:** logical tile number, physical tile coordinate, tile base, CHR index, round-trip graphics
- **Observed scope:** Background tilemap encoders for PC Engine CD and SNES assets.
- **Failure context:** One encoder used logical tile numbers as physical coordinates; another assumed a nonzero original tile base was zero. Both damaged the screen or protected background.
- **Decisive test:** Original screen data was encoded without edits and compared with the actual upload destination and physical tiles. Applying the source's number transform restored both round-trip equality and protected regions.
- **Established result:** Tilemap numbering and physical storage coordinates had to be derived from the consumer, not chosen as encoder defaults.
- **Transfer limit:** Re-derive the logical-to-upload transform for every screen and background layer.
- **Related criteria:** `references/platforms/pce.md` §2, `references/strategy/graphics-text.md` §2·§4.

## Cooked offsets corrupted raw-sector images

- **Search terms:** cooked ISO offset, raw 2352-byte sector, 2048-byte user data, pregap, CUE INDEX, wrong sector
- **Observed scope:** User-data and raw-sector representations of a PC Engine CD image.
- **Failure context:** A prior graphics offset used a pregap-free 2048-byte user-data ISO, while the build input was a 2352-byte Mode 1 BIN with pregap. Mixing those coordinate systems targeted another sector.
- **Decisive test:** A unique original byte sequence was located in extracted user data, pregap was calculated from CUE INDEX values, and the coordinate difference matched that calculation before only the affected sectors were rewritten.
- **Established result:** Converting the prior user-data offset into the target track's raw-sector coordinates aligned the source bytes and accounted for the pregap difference.
- **Transfer limit:** Recalculate the conversion from the target image's sector representation and track origin.
- **Related criteria:** `references/platforms/pce.md` §4, `references/strategy/build-and-verify.md` §2·§3.

## Existing glyph upload paths avoided a new renderer

- **Search terms:** system font hook, glyph provider, 1bpp to 4bpp, reuse upload path, VRAM cache
- **Observed scope:** System glyph-provider calls followed by bitmap conversion and VRAM upload on PC Engine CD and PlayStation.
- **Decision context:** A complete replacement renderer appeared necessary for Hangul, but the original path already handled conversion, cache, and upload after obtaining a glyph.
- **Evidence:** Only the provider boundary was replaced with a compatible source while the original downstream path remained. Hangul and existing characters were displayed together.
- **Established result:** Both consumers could reuse the original conversion and upload path by replacing only the glyph-provider interface.
- **Transfer limit:** Recheck provider ABI, bit layout, buffer lifetime, cache identity, and downstream conversion for every caller.
- **Related criteria:** `references/strategy/font-strategy.md` §5, `references/strategy/reinsertion.md` §4, `references/strategy/runtime-assets.md` §2, `references/strategy/poc.md` §3·§5.

## Translated screens may have multiple visual layers

- **Search terms:** duplicate title layer, sprite overlay, background edit, multiple entry paths, palette cycle, Japanese residue
- **Observed scope:** A PC Engine CD title subtitle duplicated in the background and a high-priority sprite, reached through two entry paths.
- **Failure context:** Editing only the background left the Japanese subtitle sprite over the Korean graphic. Fixing one entry path did not establish the other path.
- **Decisive test:** Background and sprite consumers were traced separately, the sprite was rebuilt from the final Korean background, and both entry paths were checked while the palette cycled.
- **Established result:** Every overlapping graphics layer and entry path had to be updated to remove the original presentation.
- **Transfer limit:** Enumerate actual graphics layers and entry paths rather than inferring them from file count.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.

## Duplicate text does not imply interchangeable pointers

- **Search terms:** merged duplicate strings, stable pointer slot ID, interior pointer, shared control block, translated offset
- **Observed scope:** A PlayStation story script where one pointer entered a complete control block inside another message and extraction merged the overlapping strings.
- **Failure context:** Renumbering deduplicated entries by list order translated the wrong pointer slot. Copying the interior tail as a separate source block left Japanese text when the interior pointer was used.
- **Evidence:** Extraction preserved original pointer-slot IDs and reinsertion prioritized them. Interior pointers were recalculated from corresponding complete control-block boundaries in source and translation, then checked with synthetic data for every entry path.
- **Established result:** Deduplication could not replace stable source pointer identities, and interior targets had to follow preserved structure rather than original byte distance.
- **Transfer limit:** This works only when the same structural boundary can be identified in both source and translation.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3·§4.1·§4.2, `references/strategy/reinsertion.md` §1.2·§2·§3, `references/conventions/data-formats.md` §4.

## Small-label contrast changed across UI states

- **Search terms:** small UI label, outline contrast, selected background, limited palette, pixel typography, clipping
- **Observed scope:** Small confirmation labels and their real selected-state background in a PlayStation UI.
- **Decision context:** The label needed separate background, outline, and body roles within a limited palette and without antialiasing.
- **Evidence:** Output was restricted to the three declared palette indices and displayed as `예` and `아니오` on the real confirmation screen. Outline and body remained distinguishable without clipping or adjacent-UI damage.
- **Established result:** Pixel typography constrained to three semantic palette roles preserved contrast and legibility on the actual selected background.
- **Transfer limit:** Recheck contrast, clipping, and surrounding UI under the real palette and state background of every other surface.
- **Related criteria:** `references/strategy/graphics-text.md` §2·§4, `references/strategy/font-strategy.md` §4, `references/strategy/build-and-verify.md` §5.

## Visible text does not exclude runtime side effects

- **Search terms:** first font load, CD read, background music stops, runtime asset side effect, Hangul visible
- **Observed scope:** The first runtime CD load of Hangul font data and concurrent background-music state on PlayStation.
- **Failure context:** Hangul became visible after replacing the BIOS provider, but music stopped during the first font read. Visible glyphs were mistaken for completion of the whole font path.
- **Evidence:** Music still stopped in a build that added CD-command completion and mode restoration around the first font load.
- **Established result:** Glyph display and preservation of audio during the first CD load were separate claims. The former was proven; an audio-safe load path was not.
- **Transfer limit:** For every new runtime load, verify concurrent audio, input, and display state in addition to the asset's visible result.
- **Related criteria:** `references/strategy/reinsertion.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4·§5, `references/platforms/ps1.md` §5.

## Self round-trips do not prove compressor compatibility

- **Search terms:** incompatible recompressor, self round-trip passes, original data recompressed, invalid back-reference, CNX v2
- **Observed scope:** CNX v2-compressed battle assets in a Saturn title.
- **Failure context:** Battle animation broke even though the changed file was isolated and the custom compressor-decompressor round-trip passed.
- **Decisive test:** Unmodified decompressed Japanese data was recompressed and reproduced the defect in the game while still passing the custom round-trip, isolating a semantic difference from the game decompressor.
- **Established result:** The compressor created matches against zero-filled output positions that had not yet been produced, while the game safely referenced only completed output. Restricting distance to produced bytes restored compatibility.
- **Transfer limit:** A self round-trip does not prove target-consumer compatibility. Test an unmodified recompressed asset in the real consumer.
- **Related criteria:** `references/strategy/compression.md` §4.1, `references/strategy/initial-survey.md` §3, `references/strategy/debugging.md` §2.2.

## Byte-pattern pointer scans produced false and missed references

- **Search terms:** false pointer positive, missed pointer, byte-pattern scan, Shift_JIS trail byte, compressed pixels, reference catalog
- **Observed scope:** Raw values in Saturn command arguments, SNES compressed graphics, and PC-98 strings that resembled pointers or instructions.
- **Failure context:** Byte shape and numeric range admitted command arguments, compressed pixels, and encoded characters as references. A suffix blacklist then removed real references too.
- **Decisive test:** Candidates were classified by their containing record, target range and alignment, and actual consumption format.
- **Established result:** Storage structure and consumer behavior, not byte shape, determined whether a value was a reference.
- **Transfer limit:** Do not discard interior string targets from overlap alone; they may be shared tails or interior entry points. Re-establish storage and read paths for every format.
- **Related criteria:** `references/strategy/text-extraction.md` §1.2·§1.3·§3.5, `references/strategy/reinsertion.md` §2.

## Unchanged labels may come from preloaded graphics

- **Search terms:** menu label unchanged, no VRAM write, preloaded sprite text, selected and unselected states, wrong main font
- **Observed scope:** Two-state battle-menu tabs in a Saturn title.
- **Failure context:** The Japanese tab survived main-font edits, and opening the menu produced no new VRAM write, rejecting a draw-time main-font hypothesis.
- **Decisive test:** Selected and unselected label pairs were decoded directly from a decompressed sprite asset and matched to the screen. Replacing both states changed the complete tab.
- **Established result:** The edit target was a pair of preloaded sprite images, not the main font.
- **Transfer limit:** Absence of a draw-time write does not identify a stored file or offset. Connect decoded storage to the visible result.
- **Related criteria:** `references/strategy/graphics-text.md` §1, `references/strategy/runtime-assets.md` §2.

## Glyph reduction prioritized low-semantic-cost substitutions

- **Search terms:** glyph budget, translation compromise, spelling loss, unique syllable count, human approval, synonym
- **Observed scope:** Translation wording changed because of a limited glyph supply in a Saturn title.
- **Failure context:** Technical substitutions such as `부숴` to `부셔` entered translation data and could become indistinguishable from editorial intent.
- **Decisive test:** Occurrence count and actual reduction in unique glyph demand were calculated separately, then each candidate's meaning and voice loss were reviewed.
- **Established result:** Changes with substantial spelling distortion were reverted. Only natural alternatives that truly reduced unique-glyph demand remained, with original intent and required glyphs recorded.
- **Transfer limit:** First determine whether supply can grow. A wording reduction requires human review of corpus-wide glyph savings and semantic loss.
- **Related criteria:** `references/strategy/font-strategy.md` §3.2, `references/strategy/translation-workflow.md` §4·§5.3·§5.4, `references/conventions/translation-artifacts.md` §1.1.

## Coupled geometry parameters disambiguated graphics assets

- **Search terms:** unknown bpp, width, height, offset, stride, padding, plausible partial image, asset boundary
- **Observed scope:** Saturn and PlayStation graphics with several bit-depth, width, height, and start-offset candidates of equal stored length.
- **Decision context:** Some candidates produced plausible letters or icons, while different regions used different stride or padding and adjacent effects or buttons could be misclassified as one image.
- **Evidence:** Row byte count, full-image continuity, repeated block structure, palette distribution, and neighboring asset boundaries were compared, and only established regions were re-encoded.
- **Established result:** Stored length and a plausible partial rendering did not establish bit depth, dimensions, or boundaries.
- **Transfer limit:** Select discriminating evidence again for each asset and do not apply one region's interpretation to the whole file.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§2·§3, `references/strategy/initial-survey.md` §2.2, `references/strategy/runtime-assets.md` §2.

## Aligned variants reconstructed clean backgrounds

- **Search terms:** reconstruct clean background, 4bpp label variants, nibble comparison, palette semantics, no text-free source
- **Observed scope:** Several 4bpp label variants sharing one background in a Saturn title.
- **Decision context:** No text-free original existed. Byte-wise maximum and OR operations either ignored the two separate pixels in each byte or mixed color bits.
- **Evidence:** Variants with matching coordinates and palettes were compared per 4-bit pixel to choose the value where text disappeared. New text overwrote only non-background pixels.
- **Established result:** A text-free background could be recovered by comparing individual pixels across variants that truly shared background, coordinates, and palette.
- **Transfer limit:** Pixels covered by text in every variant remain unknown. If palette index order does not match brightness, derive background selection from color meaning instead of numeric extrema.
- **Related criteria:** `references/strategy/graphics-text.md` §2·§4.

## Internal structures can have independent alignment

- **Search terms:** internal alignment, subheader boundary, final file aligned, later page corrupt, pointer table, padding
- **Observed scope:** Internal structures following text in a Saturn title, and subheaders connecting multiple pages in a Mega Drive title.
- **Failure context:** The final file was aligned, but changed preceding data moved pointer tables, controls, or subheaders off the boundaries required by their consumers. Early content worked while later structures stopped or decoded corrupt metadata.
- **Decisive test:** Every consumed structure start was checked independently and padded after the preceding data as required.
- **Established result:** Alignment applied to each directly consumed internal structure, not only the final file end.
- **Transfer limit:** Derive both alignment unit and target boundaries from each structure's consumer.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§3·§6, `references/conventions/data-formats.md` §5.

## Record regrouping broke interior pointers

- **Search terms:** sub-string pointer, grouped translation entry, interior entry point, per-item padding, delimiter boundary
- **Observed scope:** A grouped translation entry whose component strings were independently referenced by a Saturn game.
- **Failure context:** Applying one total length delta to several names made earlier growth clip later names or move an interior pointer into another name.
- **Evidence:** Source and translation were split at the same delimiters and component counts were compared. Fixed slots were padded per component and direct pointers were recalculated from each component's original start and individual movement.
- **Established result:** Length and pointer correction had to use the sub-strings consumed by the game, not the enclosing translation record.
- **Transfer limit:** Apply this correspondence only when delimiter, component count, and consumption structure are preserved. Reject the grouped record or handle it separately when they cannot be matched.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3·§4.1·§4.2, `references/strategy/reinsertion.md` §1.1·§1.2·§2, `references/conventions/data-formats.md` §4.

## Incorrect fixed-slot padding and truncation broke consumers

- **Search terms:** fixed slot, padding before terminator, trailing controls, zero is not space, token-safe truncation, blank page
- **Observed scope:** Fixed-slot strings, trailing control sequences, and strings concatenated with later text on Saturn and PlayStation.
- **Failure context:** Padding after a terminator or inside a trailing control group became an argument and stopped execution. Padding every short string inserted unwanted gaps, and zero bytes were error glyphs on some paths rather than spaces.
- **Evidence:** Valid space tokens, trailing control groups, terminators, and concatenation behavior were established per string path. Padding position varied accordingly, and overlength input preserved character and control-token boundaries.
- **Established result:** Slot size alone did not determine tail handling; behavior depended on how the consumer read trailing controls and bytes after termination.
- **Transfer limit:** Re-establish valid space, control extent, odd-byte behavior, and post-terminator reads for every path. Truncation is allowed only for a separately approved wording reduction.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1·§4.4, `references/strategy/reinsertion.md` §1.1·§6, `references/conventions/data-formats.md` §5.

## A glyph mapping may be range-local

- **Search terms:** false global glyph map, range-local mapping, first-occurrence order, later text corrupt, unknown mapping switch
- **Observed scope:** Message text and a built-in glyph pool in a Saturn title.
- **Failure context:** Early samples suggested first-occurrence glyph order, so each new code across the file was assigned the next global glyph slot. Later kanji messages decoded incorrectly.
- **Evidence:** The glyph pool exceeded the number of globally found codes, the same code selected different glyphs by range, the global map rendered broken messages, and runtime consumers read different contiguous glyph regions.
- **Established result:** A single file-wide map was rejected. No global extraction or reinsertion map was adopted while the range-switch rule remained unknown.
- **Transfer limit:** Map and transform only ranges whose switch rule and consumer index calculation are established.
- **Related criteria:** `references/strategy/text-extraction.md` §2, `references/strategy/font-strategy.md` §2, `references/strategy/debugging.md` §2.2.

## State changes may reload a different font asset

- **Search terms:** state-specific font reload, character selection, replacement not registered, existing loader, post-selection asset
- **Observed scope:** State-specific font loading after character selection in a Saturn title.
- **Failure context:** Observation stopped before selection and the replacement file was not registered in the image, leading to the false conclusion that no later reload existed.
- **Evidence:** Tracing from confirmed selection through the original loader showed a marked replacement passing through the existing open and decompression path into the live font region.
- **Established result:** An existing post-selection load path supplied the state-specific font and could carry a replacement asset.
- **Transfer limit:** Do not extend this result to other entry, return, or reload paths. Derive glyph capacity from each state's actual allocation and consumer.
- **Related criteria:** `references/strategy/font-strategy.md` §3·§5, `references/strategy/runtime-assets.md` §2.

## Expanded assets may require a decompressed-size update

- **Search terms:** decompressed-size constant, expanded compressed font, zero tail, loader length, container size mismatch
- **Observed scope:** An expanded compressed font with a separate fixed decompression-size value in a Saturn title.
- **Failure context:** New glyphs existed at the end of the decompressed file, but the corresponding live font memory remained zero. Updated file and compressed sizes were mistaken for proof that the whole asset loaded.
- **Evidence:** Comparing decompressed data with live memory located the cutoff and exposed a fixed old decompression length. Updating it to the actual output size made the full range agree.
- **Established result:** Expanding a compressed asset also required the loader's decompressed-size value to match the real output.
- **Transfer limit:** Re-derive the size field's unit and the loader's tail-read behavior.
- **Related criteria:** `references/strategy/compression.md` §5, `references/strategy/reinsertion.md` §1.2·§3·§5, `references/strategy/runtime-assets.md` §2.

## Broad pointer relocation failed before full UI proof

- **Search terms:** pointer relocation overreach, partial runtime proof, UI not initialized, string consumed but not displayed, interaction QA
- **Observed scope:** A Saturn path that consumed a relocated string before UI initialization and a selection screen where display and interaction were fully observable.
- **Failure context:** Relocating every pointer-shaped value in range stopped progress despite passing restoration and load-size checks. Even a safe direct pointer proved neither window capacity nor display and interaction.
- **Evidence:** The pre-UI path preserved source structure and moved one confirmed direct pointer, proving entry and 16-bit character reads only. The real selection screen combined pointer, load size, window position, and width and verified full display, cursor movement, cancel, selection, and progress.
- **Established result:** Broad range-based relocation was rejected. One path proved complete UI behavior; the earlier path proved only string reachability and consumption.
- **Transfer limit:** Do not transfer one screen's success to another file or event. Recheck direct references, added-region boundary, alignment, terminator, load size, display, interaction, and progress per path.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.

## Address reads do not prove semantic consumption

- **Search terms:** read breakpoint false positive, RAM reuse, decompressor back-reference, semantic consumption, wrong execution phase
- **Observed scope:** A read breakpoint on an added string address in a Saturn title.
- **Failure context:** The read was attributed to a choice renderer, but a later compressed asset reused the same physical RAM and its decompressor back-reference read that address.
- **Decisive test:** The hit's instruction, call path, source, destination, and current buffer role were connected. It was a post-choice decompression copy and separate from the choice consumer.
- **Established result:** An address read did not prove that the bytes were read as text; RAM reuse produced a false semantic signal.
- **Transfer limit:** Treat a read breakpoint as consumption evidence only when execution phase, call path, buffer role, and decoded result are connected.
- **Related criteria:** `references/strategy/debugging.md` §2.2·§3·§4, `references/strategy/compression.md` §2·§3, `references/strategy/runtime-assets.md` §2.

## Incomplete-token truncation consumed terminators

- **Search terms:** token-boundary truncation, incomplete prefix, fixed slot, terminator consumed, `FB`, `FA`
- **Observed scope:** A two-byte prefix encoding in an SNES text path.
- **Failure context:** Truncating a translation to the source byte length left a lone `FB` or `FA` prefix. The game consumed the following `FF` terminator as the second character byte and lost the terminator.
- **Decisive test:** The truncated output was parsed again with the same tokenizer. Removing an incomplete final token and returning to the previous character boundary removed the failure.
- **Established result:** Fixed-byte truncation had to end at a complete game token, not merely at the target byte count.
- **Transfer limit:** An even byte count does not prove a valid boundary in every variable-length encoding. This case selects the cut point only after a shortening decision has been approved.
- **Related criteria:** `references/strategy/reinsertion.md` §1.1, `references/strategy/text-extraction.md` §2.

## Token width follows the consumer read unit

- **Search terms:** consumer read width, two-byte tokens, odd alignment, one-byte control, 65816
- **Observed scope:** An SNES text path whose consumer always read and advanced by two bytes.
- **Failure context:** An early Korean encoder emitted one-byte spaces and controls, shifting every following tile pair onto an odd boundary.
- **Decisive test:** The consumer's two-byte read and advance were confirmed. Serializing every token as a word and rejecting controls at odd positions removed the alignment failure.
- **Established result:** Token width followed the consumer's read unit, not the visible character format.
- **Transfer limit:** The use of a 65816 CPU does not by itself establish a two-byte text unit.
- **Related criteria:** `references/strategy/text-extraction.md` §2, `references/strategy/initial-survey.md` §2.2, `references/platforms/snes.md` §5.

## Later original writes overwrote replacements

- **Search terms:** later original write, overwritten translation, last writer, VRAM collision, subtitle, logo
- **Observed scope:** A layered SNES logo and PC Engine CD subtitles overwritten by later original writes.
- **Failure context:** Korean pixels were written before later source fragments or while an automatic transfer to the same region remained active.
- **Decisive test:** Every write to the affected VRAM range was traced. Applying the replacement after the final transfer, or suppressing only the transfer that continually overwrote it, preserved both the Korean asset and unrelated screen updates.
- **Established result:** Adding a replacement write did not remove later original writers; the intervention had to follow the last write or isolate the confirmed collision.
- **Transfer limit:** Re-derive address, timing, and display lifetime for each scene, and do not disable unrelated original updates.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §4.

## Isolated removal rejected the suspected root cause

- **Search terms:** wrong root cause, suspected hook removed, symptom persists, WRAM overlap, DMA source
- **Observed scope:** Corrupted SNES tiles initially attributed to a VRAM hook.
- **Failure context:** Several observations fit the hook hypothesis, but they did not distinguish it from another writer corrupting the DMA source.
- **Decisive test:** A build with only the suspected hook removed still failed. Following the DMA source then showed that the Korean font occupied WRAM used by the game.
- **Established result:** The actual cause was a WRAM collision, not the suspected hook.
- **Transfer limit:** Removing a suspect is a valid rejection test only when the removal does not change other relevant paths.
- **Related criteria:** `references/strategy/debugging.md` §2.2.

## Rare paths may depend on table-tail entries

- **Search terms:** one branch corrupt, missing sentinel pointer, table tail, off-by-one address, pointer coverage
- **Observed scope:** A branch-specific SNES text failure.
- **Failure context:** The build omitted a special pointer at the end of a table and started the first text byte one byte early, overwriting that pointer.
- **Decisive test:** The failing branch's actual load path was disassembled and compared with the source constants, pointer count, and first text address.
- **Established result:** Restoring the complete fixed table and correcting the first text address repaired the branch.
- **Transfer limit:** Do not assume that story branch count equals consumer-path count.
- **Related criteria:** `references/strategy/build-and-verify.md` §4, `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §3, `references/strategy/initial-survey.md` §3.1, `references/conventions/data-formats.md` §4.

## Terminators may be multi-byte stateful sequences

- **Search terms:** multi-byte terminator, single `FF`, `00 00`, `00 FF`, scanner misparse
- **Observed scope:** Multi-byte controls in an SNES text path.
- **Failure context:** A scanner treated a lone `FF` as a terminator even though the game rendered it as the character `今`.
- **Decisive test:** Following the consumer separated `00 00` termination, `00 FF` button wait, and lone `FF` character data. The affected range was then re-extracted.
- **Established result:** Testing only the first byte of a control sequence caused the extraction error.
- **Transfer limit:** Derive the complete terminator sequence and parser state for every other consumer.
- **Related criteria:** `references/strategy/text-extraction.md` §3.1.

## Post-decompression patches reused downstream transfers

- **Search terms:** post-decompression patch, reuse DMA, no recompressor, compressed UI, WRAM overwrite
- **Observed scope:** Several compressed UI assets in an SNES title.
- **Decision context:** Only part of each decompressed asset needed replacement, and preserving the game's existing transfer path avoided introducing a new compressor or DMA path.
- **Evidence:** Each decompression call was connected to its input identity, bounded WRAM output, and downstream DMA destination. Full replacements used verified decompressed results; partial replacements changed only the required WRAM region after original decompression. Entry and re-entry were tested on multiple screens.
- **Established result:** Replacing the required region immediately after the original decompression allowed the existing DMA path to carry the modified asset.
- **Transfer limit:** Intervene only where input identity, output bound, call state, downstream consumer, and last writer are all connected.
- **Related criteria:** `references/strategy/compression.md` §5, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §4.

## Whole-canvas rendering preserved cross-tile effects

- **Search terms:** composite canvas, tile seams, outline, gradient, shine, render then split
- **Observed scope:** Multi-tile labels whose outline, background, gradient, or highlight crossed physical tile boundaries.
- **Decision context:** Rendering each tile independently broke continuous visual effects at tile seams.
- **Evidence:** The complete label was composed as one canvas, then split according to the verified tile, subtile, palette, storage, and transfer order. Tests on multiple entry screens confirmed that the seams and effects remained intact.
- **Established result:** Rendering the full label before splitting it produced continuous cross-tile effects.
- **Transfer limit:** Re-derive canvas coordinates, protected regions, and storage order for each asset.
- **Related criteria:** `references/strategy/graphics-text.md` §2·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.

## Moving flexible data first reclaimed constrained space

- **Search terms:** mixed pointer width, same-bank constraint, cross-bank pointer, reclaimed source region, space allocation
- **Observed scope:** Text relocation with both three-byte cross-bank references and two-byte same-bank references.
- **Decision context:** Constrained and relocatable strings competed for limited space in the original bank.
- **Evidence:** References were classified by their proven address range. Relocatable data moved out first, reclaiming its old region for same-bank-only data. Every pointer and the cleared source region were then checked.
- **Established result:** Allocation order had to account for source space reclaimed by earlier relocations, not only currently free space.
- **Transfer limit:** This applies only after all references and address ranges are known and the reclaimed region has no interior entry, interior pointer, or other consumer.
- **Related criteria:** `references/strategy/reinsertion.md` §2·§3·§5, `references/conventions/data-formats.md` §4.

## Font parsing success does not prove usable glyphs

- **Search terms:** empty glyph, font parses, zero-size raster, bitmap-only font, rasterizer compatibility
- **Observed scope:** A bitmap-embedded font whose outline path returned empty Hangul rasters.
- **Failure context:** File parsing succeeded, but representative Hangul glyphs rasterized to `0×0`, allowing the build to emit empty font pages.
- **Evidence:** Bitmap tables, effectively empty outlines, representative glyph dimensions, and the total empty-glyph count were inspected. An outline-based font through the same path returned pixels.
- **Established result:** Successful font parsing did not prove usable glyph output; representative dimensions and empty-glyph counts caused the bad asset to be rejected.
- **Transfer limit:** Repeat the representative-glyph check when font structure, code points, rasterizer, or raster path changes.
- **Related criteria:** `references/strategy/font-strategy.md` §3.2·§4·§6, `references/conventions/project-conventions.md` §4·§5.3.

## Runtime samples can locate compressed source assets

- **Search terms:** runtime sample reverse search, compressed font source, LZ scan, missed breakpoint, glyph cache
- **Observed scope:** Locating an unknown compressed font source from live glyph bytes.
- **Failure context:** WRAM and VRAM breakpoints repeatedly missed the initial load because the game used an accumulated glyph cache and DMA, while several live glyph samples and a verified decompressor were available.
- **Evidence:** Candidate ROM positions were decompressed with the verified format and bounded output. Results containing multiple live glyph tiles were rendered and compared byte-for-byte with WRAM samples.
- **Established result:** Reverse-searching verified decompression outputs with several runtime glyph samples located the compressed source and internal glyph layout.
- **Transfer limit:** Confirm a candidate only when the compression format and output bound are known and multiple live samples plus final display agree.
- **Related criteria:** `references/strategy/compression.md` §2·§3, `references/strategy/initial-survey.md` §2.2·§2.5, `references/strategy/runtime-assets.md` §2, `references/strategy/debugging.md` §4.

## Layout limits include physical writes and clear lifetime

- **Search terms:** physical write footprint, stale tile, clear lifetime, logical width, adjacent HUD damage
- **Observed scope:** Dialogue, ending, and map-label regions whose physical writes outlived their logical text.
- **Failure context:** Placement used visible blank space or cursor advance as the limit. Old tiles remained, physical cells reached adjacent UI, or later states did not clear the covered background.
- **Evidence:** Written cells and cells cleared or overwritten by later states were traced separately. Logical advance and physical footprint were measured independently, and reused regions were either fully cleared or kept within the original update area.
- **Established result:** The usable layout limit depended on both the physical write footprint and the lifetime over which later states cleared or overwrote it, not on visible space alone.
- **Transfer limit:** Confirm terminators, physical footprint, and following state transitions before removing padding, extending rows, or placing labels.
- **Related criteria:** `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/translation-workflow.md` §4, `references/strategy/build-and-verify.md` §5.

## Static overlays overwrote runtime-updated cells

- **Search terms:** dynamic tile overwritten, static overlay, state-dependent cells, broad post-DMA hook, save UI
- **Observed scope:** Save-slot, delete, and copy tilemaps containing both static and runtime-updated cells.
- **Failure context:** Reapplying a complete static Korean tilemap after every related transfer replaced dynamic slot and confirmation text. A temporary-buffer trigger also ran on neighboring screens.
- **Evidence:** Activation was narrowed by the final decompressed asset identity, dynamic cells were excluded, and only state-required static additions were applied. Occupied and empty slots, confirm and cancel, re-entry, and neighboring screens were checked.
- **Established result:** Excluding runtime-updated cells preserved dynamic state while allowing the fixed labels to remain translated.
- **Transfer limit:** Reconnect dynamic cells, stable state signal, asset identity, and write order for each target screen.
- **Related criteria:** `references/strategy/graphics-text.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §4·§6.

## Asset reachability does not prove readable text

- **Search terms:** false Hangul PoC, bytes reach VRAM, wrong tile, legibility, reachability versus visibility
- **Observed scope:** An early graphics-tile PoC and a later dialogue-font PoC in the same SNES project.
- **Failure context:** Patched bytes matched VRAM, but the changed tile was decoration or blank space and did not form legible Hangul.
- **Evidence:** Magnified runtime captures disproved the first interpretation. A later dialogue path connected storage, load, transformation, and display and rendered legible Hangul in the dialogue box.
- **Established result:** The first experiment proved asset reachability only; the later experiment proved both reachability and visible Hangul.
- **Transfer limit:** Storage and VRAM byte agreement does not prove the intended glyph or its legibility.
- **Related criteria:** `references/strategy/poc.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/font-strategy.md` §6.

## Visible layout and screen bounds determined dialogue-window size

- **Search terms:** dialogue box width, dialogue box height, visible glyph count, control tokens, line count, screen boundary
- **Observed scope:** Dynamic battle-dialogue window sizing for Korean text.
- **Failure context:** Longer or multiline Korean text overflowed a fixed-size window designed for Japanese text, while serialized byte or token counts also overestimated visible width by counting controls and line changes.
- **Evidence:** Korean text was tokenized like the consumer. Controls were excluded from width, line changes determined row count, and the resulting window was independently clamped to the actual screen boundary. Tests in runtime battle scenes confirmed both the window size and text layout.
- **Established result:** Maximum visible width and line count determined content size, while the screen edge remained a separate placement limit.
- **Transfer limit:** Re-measure token semantics, coordinate system, and visible boundary for every other window consumer.
- **Related criteria:** `references/strategy/translation-workflow.md` §4, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.

## Selection highlighting depended on data and consumer range

- **Search terms:** selection highlight too short, source-length read, highlight asset, static proof only, selected state
- **Observed scope:** A translated selection row longer than the source-language highlight range.
- **Failure context:** The Korean row grew, but selection highlighting still covered only the original prefix. Expanding highlight data alone did not change the consumer's source-length read.
- **Evidence:** Data-only expansion had no effect, and static analysis tied the read range to the original length. Both ranges were adjusted, but selected and unselected runtime transitions were not yet observed.
- **Established result:** Static evidence established that both highlight data and its read range had to cover the full translated row.
- **Transfer limit:** Do not mark the screen complete until runtime evidence shows every row changing state through its final cell.
- **Related criteria:** `references/strategy/graphics-text.md` §1·§3·§4, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.

## Pointer tables may not be reread between states

- **Search terms:** second pointer ignored, sequential block, pointer lifetime, table not reread, contiguous placement
- **Observed scope:** Consecutive menu and rule-editor text blocks in an SNES title.
- **Failure context:** Both blocks had table entries, suggesting that changing the second entry would redirect the second screen. The consumer instead advanced and reused the current text-object pointer after the first block.
- **Decisive test:** Pointer initialization, increment, and reuse were traced across the transition. Placing both new blocks contiguously and updating both references preserved menu entry, value changes, and return.
- **Established result:** A table entry's existence did not prove that the consumer reread it during the transition.
- **Transfer limit:** Re-derive table rereads and object-pointer lifetime for every other entry path. Require contiguous placement only for the proven path.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §2·§6, `references/strategy/runtime-assets.md` §2.

## Reused slots retain unwritten data

- **Search terms:** ring buffer residue, fixed-width slot, blank trailing slot, partial write, scrolling banner
- **Observed scope:** A horizontally scrolling ending banner that reused fixed-width slots.
- **Failure context:** Overlong text clipped or overlapped the next slot, while short or empty trailing slots left previous content in unwritten cells.
- **Decisive test:** Slot width and count were derived from the consumer, every slot containing text and every blank slot was written to the exact width, and the final slots were observed through reuse.
- **Established result:** The reused buffer did not clear unwritten cells; blank slots and unused cells required explicit space data.
- **Transfer limit:** Re-derive slot width, count, reuse order, and clearing behavior for each consumer. Do not transfer the numeric limits.
- **Related criteria:** `references/strategy/translation-workflow.md` §4, `references/strategy/reinsertion.md` §4·§6, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §5.

## Composed name input needs one identity across editing, storage, and reuse

- **Search terms:** Hangul name input, composition state, committed name record, save reload, dynamic name glyph, redisplay mismatch
- **Observed scope:** Hangul name entry in the Japanese Game Boy Color release of Arle no Bouken, limited to a declared repertoire.
- **Failure context:** A smaller fixed candidate table could prove selection and one dialogue, but it could not provide the adopted repertoire or establish that later consumers and saved records used the same syllable identity.
- **Evidence:** Editing state, the committed record, dialogue rendering, save data, title continuation, and field redisplay were bound to one identity. The declared repertoire was checked against both a reference model and the generated implementation; representative controller input then survived save, power cycle, and reload.
- **Established result:** Name support required one validated identity from input state through the committed record and every redisplay and persistence boundary, while static exhaustive coverage and representative runtime evidence remained separate claims.
- **Transfer limit:** Re-derive candidate order, edit stages, record structure, supported repertoire, save format, and every consumer. A reset or power-cycle test in the same emulator process does not prove persistence after restarting the emulator, and representative names do not provide human visual approval of the complete repertoire.
- **Related criteria:** `references/strategy/name-entry.md` §2·§4·§6, `references/strategy/font-strategy.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4·§5.

## Residual correction turned composition into exact glyph compression

- **Search terms:** compositional Hangul compression, residual rows, XOR correction, exact glyph reconstruction, finished-font bank budget
- **Observed scope:** Runtime reconstruction of name glyphs for a finite Hangul repertoire in the Japanese Game Boy Color release of Arle no Bouken.
- **Decision context:** Storing every finished glyph exceeded the chosen bank budget, while exposing a rough component-only result would have reduced the approved visual target.
- **Evidence:** Common initial-medial and final components were combined, and only differing rows received sparse XOR corrections. An independent decoder and the generated target implementation reproduced every declared finished glyph exactly and rejected undeclared combinations.
- **Established result:** Composition served as a compression basis rather than the visible font style; bounded residual data restored the tracked finished glyphs exactly within the measured bank.
- **Transfer limit:** Recompute component classes, residual population, serialized indexes, code size, and output equivalence for the target font and cell. The measured savings and source-font choice do not transfer to another repertoire or renderer.
- **Related criteria:** `references/strategy/font-strategy.md` §2.2·§4, `references/strategy/name-entry.md` §5, `references/strategy/build-and-verify.md` §1.

## Retained display slots define glyph co-residency across transitions

- **Search terms:** stale line buffer, glyph codebook transition, retained glyph set, retained tile code, dynamic font page
- **Observed scope:** Dynamic dialogue pages and dialogue-to-menu transitions in the Japanese NES release of Fire Emblem.
- **Failure context:** Individual pages and a static integrated image fit their glyph budgets, but the next record left prior line slots visible while selecting a new codebook, so retained tile codes changed meaning.
- **Evidence:** Writer and clear paths showed that record initialization retained prior line buffers. Requiring every glyph in the record to coexist was unnecessarily large; requiring only glyphs still present in retained slots fit. Runtime then exposed a separate loss of the completed page during the following menu state.
- **Established result:** The required working set and code assignment were defined by observed transitions, retained physical slots, dynamic insertions, and release timing, not by isolated page demand or an unconditional union of all records.
- **Transfer limit:** Enumerate writers, clears, visible transitions, inserted values, and codebook changes for the target. Re-derive which slots persist and require one compatible mapping only for their proven shared lifetime.
- **Related criteria:** `references/strategy/font-strategy.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §6, `references/strategy/build-and-verify.md` §4·§5.

## Manual layout decisions must precede faithful static previews

- **Search terms:** inferred dialogue layout, static preview approval, explicit page ranges, presentation evidence
- **Observed scope:** Dialogue translation review for the Japanese PlayStation release of Puyo Puyo Box.
- **Failure context:** Automatic wrapping and inferred line proportions produced plausible images before the window, page, line, and control placement had been established, risking approval of a layout that was not derived from the game.
- **Evidence:** The review path rejected inferred previews, kept wording selection separate, and required explicit text ranges in display order, tied to the chosen text, controls, and geometry, before static reproduction. Static previews, runtime evidence obtained through intervention, and evidence from normal play remained distinct.
- **Established result:** A static preview became faithful evidence only after layout was an explicit input; it did not itself decide layout, approve wording, or prove runtime consumption.
- **Transfer limit:** Use automatic layout when a complete deterministic consumer model establishes it. Otherwise require the target's actual geometry and the necessary human layout decision, and revalidate downstream evidence whenever text, controls, or geometry changes.
- **Related criteria:** `references/strategy/translation-workflow.md` §5.6, `references/strategy/build-and-verify.md` §5, `references/conventions/project-records.md` §7.2.

## Relocated call-like controls need an explicit return target

- **Search terms:** call-like text control, return address, relocated continuation, physical successor, resume target
- **Observed scope:** Text continuations using call and return controls in the Japanese Sega Saturn release of Waku Waku Puyo Puyo Dungeon.
- **Failure context:** Relocating a continuation preserved its terminal control bytes but changed the physical byte immediately after the call-like control, so return resumed at the wrong content.
- **Decisive test:** Consumer analysis showed that the control saved the address following the token before jumping to a shared block. The relocated path reconstructed that return target explicitly, and a source entry from the game verified the return path rather than only terminal-byte equality.
- **Established result:** Control-token preservation was insufficient because physical placement participated in control flow; relocation had to preserve or explicitly reconstruct the original return target.
- **Transfer limit:** Re-derive call depth, pushed address, target base, return operation, physical adjacency, and nested continuation behavior. Do not treat every branch-like token as a call or reuse the observed control values.
- **Related criteria:** `references/strategy/text-extraction.md` §4.4, `references/strategy/reinsertion.md` §1.2·§3, `references/strategy/build-and-verify.md` §5.
