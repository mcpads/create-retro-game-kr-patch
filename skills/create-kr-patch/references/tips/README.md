# Evidence-backed case index

This index preserves bounded failures, counterexamples, proven techniques, and operational caveats that are expensive to rediscover.

Select only a case whose judgment area and symptom match the current problem. Use its observed scope and transfer limit to choose what must be re-established. Completion is determined by the linked **Related criteria**, not by resemblance to the case.

Case placement follows the conclusion's applicability, not the platform where it was first observed. `general/` contains conclusions that can be tested without adopting one platform's storage or execution rules. `platforms/` contains cases whose conclusion depends on those rules. A platform named in a general case records the evidence boundary; it is not a routing condition.

Headings state the reusable conclusion directly. **Search terms** provide symptom, data-structure, and technical aliases for retrieval; they are not additional claims. Literal source or target strings remain unchanged when they are evidence. Search the index first. If its wording does not match, search the tips tree by the observed symptom or technical term, then read only the matching case section.

## Judgment areas

The labels below correspond to the strategy documents routed from `SKILL.md`. Convention and platform documents may appear in a case's related criteria but do not add a judgment area.

| Index label | Strategy document |
|---|---|
| Initial survey | `references/strategy/initial-survey.md` |
| Fonts and encoding | `references/strategy/font-strategy.md` |
| Text extraction | `references/strategy/text-extraction.md` |
| PoC | `references/strategy/poc.md` |
| Reinsertion and hooks | `references/strategy/reinsertion.md` |
| Translation | `references/strategy/translation-workflow.md` |
| Build and verification | `references/strategy/build-and-verify.md` |
| Debugging | `references/strategy/debugging.md` |
| Graphics text | `references/strategy/graphics-text.md` |
| Compression | `references/strategy/compression.md` |
| Runtime assets | `references/strategy/runtime-assets.md` |

## General cases

| Case | Judgment areas | Read when | First observed on | Reference |
|---|---|---|---|---|
| Pointer gaps do not define string boundaries | Text extraction | Pointer-based slices overlap or contain nested entries | Dreamcast | `references/tips/general/cases.md#pointer-gaps-do-not-define-string-boundaries` |
| Shared glyph slots have multiple consumers | Fonts and encoding / Graphics text / Runtime assets / Build and verification | Changing one glyph or tile damages unrelated labels, digits, or graphics | Dreamcast / SNES / Game Gear / Saturn / PlayStation | `references/tips/general/cases.md#shared-glyph-slots-have-multiple-consumers` |
| Runtime screen evidence corrected extraction labels | Debugging / Text extraction | A translated label does not match the text the screen displays | Dreamcast | `references/tips/general/cases.md#runtime-screen-evidence-corrected-extraction-labels` |
| Zero-filled space is not proven free | Reinsertion and hooks / Initial survey / Debugging | Code or data placed in an apparently unused region crashes on entry | Dreamcast / Saturn | `references/tips/general/cases.md#zero-filled-space-is-not-proven-free` |
| Shorter dialogue can change voice timing | Text extraction / Translation / Build and verification | Voice playback ends progressively earlier after translation | Dreamcast | `references/tips/general/cases.md#shorter-dialogue-can-change-voice-timing` |
| Generated layouts invalidate stale fixed writes | Build and verification | A fixed write overlaps a generated literal pool or relocated block | Dreamcast | `references/tips/general/cases.md#generated-layouts-invalidate-stale-fixed-writes` |
| Apparent disc gaps overlapped file extents | Reinsertion and hooks / Build and verification | A large apparent gap corrupts a later disc file | Dreamcast | `references/tips/general/cases.md#apparent-disc-gaps-overlapped-file-extents` |
| Font filenames do not identify the active font | Fonts and encoding / Runtime assets / PoC | A plausible font file or earlier PoC does not affect active dialogue | Dreamcast | `references/tips/general/cases.md#font-filenames-do-not-identify-the-active-font` |
| Final display-buffer tracing corrected coordinate assumptions | Debugging | Prices and following dialogue shift together | Game Gear | `references/tips/general/cases.md#final-display-buffer-tracing-corrected-coordinate-assumptions` |
| Late observation can miss one-time asset uploads | Runtime assets / Debugging | A producer appears absent after loading a save state or attaching late | Game Gear / SNES | `references/tips/general/cases.md#late-observation-can-miss-one-time-asset-uploads` |
| Decoder correction left stale-source translations | Translation | Corrected decoding leaves translations based on the old source text | Game Gear | `references/tips/general/cases.md#decoder-correction-left-stale-source-translations` |
| Shared string tails constrain allocation | Reinsertion and hooks | Multiple pointer tables reference suffixes inside the same strings | Game Gear | `references/tips/general/cases.md#shared-string-tails-constrain-allocation` |
| Lost page-local controls changed portrait state | Text extraction / Translation | Portrait or expression state disappears on some pages | Game Gear | `references/tips/general/cases.md#lost-page-local-controls-changed-portrait-state` |
| Equal raw bytes can have different consumer semantics | Translation / Text extraction / Initial survey | A token copied from another patch moves or renders differently | Game Gear / NES | `references/tips/general/cases.md#equal-raw-bytes-can-have-different-consumer-semantics` |
| Zero-length entries may point to runtime text | Reinsertion and hooks / Runtime assets | An empty table entry actually resolves to composed runtime text | Game Gear | `references/tips/general/cases.md#zero-length-entries-may-point-to-runtime-text` |
| Shared hooks corrupted caller-specific state | Reinsertion and hooks / Debugging | One caller fails after a hook works elsewhere | Game Gear | `references/tips/general/cases.md#shared-hooks-corrupted-caller-specific-state` |
| Layout limits vary by window state | Text extraction / Translation / Build and verification / Reinsertion and hooks | A script passes a wide-window check but overflows in a narrow state | Game Gear | `references/tips/general/cases.md#layout-limits-vary-by-window-state` |
| Cleanup behavior may be caller-specific | Debugging / Reinsertion and hooks / Runtime assets | Stale tiles remain only for one caller or alignment mode | Game Gear | `references/tips/general/cases.md#cleanup-behavior-may-be-caller-specific` |
| Missing control sequences stopped progression | Build and verification / Text extraction | Progress stops at one translated line | Mega Drive | `references/tips/general/cases.md#missing-control-sequences-stopped-progression` |
| String-only context misidentified speaker and display role | Translation | A string-only translation loses speaker changes or system narration | Mega Drive / PC-98 | `references/tips/general/cases.md#string-only-context-misidentified-speaker-and-display-role` |
| Repeated glyph blocks may encode pre-shifted variants | Fonts and encoding / Runtime assets | Similar data repeats per glyph and variable-width output clips or shifts | Mega Drive | `references/tips/general/cases.md#repeated-glyph-blocks-may-encode-pre-shifted-variants` |
| Input glyphs and result glyphs may use different assets | Fonts and encoding / Runtime assets | Name-entry candidates change but the confirmed name does not | Nintendo DS | `references/tips/general/cases.md#input-glyphs-and-result-glyphs-may-use-different-assets` |
| Asset expansion without metadata growth halted before title | Runtime assets / Reinsertion and hooks / Debugging | Adding one asset entry causes a pre-title halt | Nintendo DS | `references/tips/general/cases.md#asset-expansion-without-metadata-growth-halted-before-title` |
| Image header mismatch hid required runtime memory | Initial survey / Build and verification / Debugging | A prior patch uses memory not declared by the image header | NES | `references/tips/general/cases.md#image-header-mismatch-hid-required-runtime-memory` |
| Standard-decoder rejection does not prove free code space | Fonts and encoding / Text extraction | An apparently unused lead byte is chosen from decoder statistics alone | PC-98 | `references/tips/general/cases.md#standard-decoder-rejection-does-not-prove-free-code-space` |
| Shared boundary logic let generator errors pass validation | Fonts and encoding / Build and verification | A generator and its validator agree but the displayed glyph is wrong | PC-98 | `references/tips/general/cases.md#shared-boundary-logic-let-generator-errors-pass-validation` |
| String pools can provide capacity beyond local gaps | Reinsertion and hooks / Build and verification | Long text cannot fit between adjacent terminators | PC-98 | `references/tips/general/cases.md#string-pools-can-provide-capacity-beyond-local-gaps` |
| Original-coordinate planning prevented multi-insertion drift | Reinsertion and hooks / Build and verification | Several growing regions cause missed or double-adjusted pointers | PC-98 | `references/tips/general/cases.md#original-coordinate-planning-prevented-multi-insertion-drift` |
| Pointerless strings may be fixed-position data | Text extraction / Reinsertion and hooks / Build and verification | Moving an unreferenced leading string changes neighboring names | PC-98 | `references/tips/general/cases.md#pointerless-strings-may-be-fixed-position-data` |
| Speculative splitting changed unknown shared consumers | Translation / Text extraction / Reinsertion and hooks | A shared string has consumers whose roles are not all known | PC-98 | `references/tips/general/cases.md#speculative-splitting-changed-unknown-shared-consumers` |
| Logical tile indices are not physical coordinates | Graphics text | Graphics move or damage the background after a tile-number conversion | PC Engine CD / SNES | `references/tips/general/cases.md#logical-tile-indices-are-not-physical-coordinates` |
| Cooked offsets corrupted raw-sector images | Build and verification | User-data offsets are applied directly to a raw-sector image | PC Engine CD | `references/tips/general/cases.md#cooked-offsets-corrupted-raw-sector-images` |
| Existing glyph upload paths avoided a new renderer | Fonts and encoding / Reinsertion and hooks / Runtime assets / PoC | A new renderer seems necessary despite an existing glyph upload path | PC Engine CD / PlayStation | `references/tips/general/cases.md#existing-glyph-upload-paths-avoided-a-new-renderer` |
| Translated screens may have multiple visual layers | Graphics text / Runtime assets / Build and verification | Japanese text remains after replacing the background layer | PC Engine CD | `references/tips/general/cases.md#translated-screens-may-have-multiple-visual-layers` |
| Duplicate text does not imply interchangeable pointers | Text extraction / Reinsertion and hooks | Deduplication changes another pointer slot or leaves an interior suffix | PlayStation | `references/tips/general/cases.md#duplicate-text-does-not-imply-interchangeable-pointers` |
| Small-label contrast changed across UI states | Graphics text / Fonts and encoding / Build and verification | A compact label needs readable fill and outline in selected states | PlayStation | `references/tips/general/cases.md#small-label-contrast-changed-across-ui-states` |
| Visible text does not exclude runtime side effects | Reinsertion and hooks / Runtime assets / Build and verification | Hangul displays but the first asset load interrupts audio or another subsystem | PlayStation | `references/tips/general/cases.md#visible-text-does-not-exclude-runtime-side-effects` |
| Self round-trips do not prove compressor compatibility | Compression / Initial survey / Debugging | Recompressing untouched original data still breaks in the game | Saturn | `references/tips/general/cases.md#self-round-trips-do-not-prove-compressor-compatibility` |
| Byte-pattern pointer scans produced false and missed references | Text extraction / Reinsertion and hooks | Byte-pattern scans produce false references or miss real ones | Saturn / SNES / PC-98 | `references/tips/general/cases.md#byte-pattern-pointer-scans-produced-false-and-missed-references` |
| Unchanged labels may come from preloaded graphics | Graphics text / Runtime assets | Main-font changes do not affect a label and no new write occurs on entry | Saturn | `references/tips/general/cases.md#unchanged-labels-may-come-from-preloaded-graphics` |
| Glyph reduction prioritized low-semantic-cost substitutions | Fonts and encoding / Translation | A temporary glyph budget forces wording changes | Saturn | `references/tips/general/cases.md#glyph-reduction-prioritized-low-semantic-cost-substitutions` |
| Coupled geometry parameters disambiguated graphics assets | Graphics text / Initial survey / Runtime assets | Several bpp, width, height, offset, and stride combinations look plausible | Saturn / PlayStation | `references/tips/general/cases.md#coupled-geometry-parameters-disambiguated-graphics-assets` |
| Aligned variants reconstructed clean backgrounds | Graphics text | Several label variants share a background but no clean source exists | Saturn | `references/tips/general/cases.md#aligned-variants-reconstructed-clean-backgrounds` |
| Internal structures can have independent alignment | Reinsertion and hooks | A file is aligned overall but later internal pages fail | Saturn / Mega Drive | `references/tips/general/cases.md#internal-structures-can-have-independent-alignment` |
| Record regrouping broke interior pointers | Text extraction / Reinsertion and hooks | A pointer enters a substring inside one translation record | Saturn | `references/tips/general/cases.md#record-regrouping-broke-interior-pointers` |
| Incorrect fixed-slot padding and truncation broke consumers | Text extraction / Reinsertion and hooks | Padding or truncation causes a halt, blank page, joined spaces, or bad glyph | Saturn / PlayStation | `references/tips/general/cases.md#incorrect-fixed-slot-padding-and-truncation-broke-consumers` |
| A glyph mapping may be range-local | Text extraction / Fonts and encoding / Debugging | Early text maps correctly but later messages decode as other glyphs | Saturn | `references/tips/general/cases.md#a-glyph-mapping-may-be-range-local` |
| State changes may reload a different font asset | Fonts and encoding / Runtime assets | A replacement font disappears after character or mode selection | Saturn | `references/tips/general/cases.md#state-changes-may-reload-a-different-font-asset` |
| Expanded assets may require a decompressed-size update | Compression / Reinsertion and hooks / Runtime assets | An expanded file loads only up to the old decompressed length | Saturn | `references/tips/general/cases.md#expanded-assets-may-require-a-decompressed-size-update` |
| Broad pointer relocation failed before full UI proof | Reinsertion and hooks / Runtime assets / Build and verification | Broad pointer-shaped relocation halts, or a direct read is mistaken for UI completion | Saturn | `references/tips/general/cases.md#broad-pointer-relocation-failed-before-full-ui-proof` |
| Address reads do not prove semantic consumption | Debugging / Compression / Runtime assets | A read breakpoint hits reused RAM during an unrelated decompression | Saturn | `references/tips/general/cases.md#address-reads-do-not-prove-semantic-consumption` |
| Incomplete-token truncation consumed terminators | Reinsertion and hooks / Text extraction | Fixed-byte truncation leaves an incomplete prefix and consumes the terminator | SNES | `references/tips/general/cases.md#incomplete-token-truncation-consumed-terminators` |
| Token width follows the consumer read unit | Text extraction / Initial survey | Text renders correctly until a control code, then every following character shifts | SNES | `references/tips/general/cases.md#token-width-follows-the-consumer-read-unit` |
| Later original writes overwrote replacements | Runtime assets / Reinsertion and hooks | Original transfers overwrite a translated logo or subtitle | SNES / PC Engine CD | `references/tips/general/cases.md#later-original-writes-overwrote-replacements` |
| Isolated removal rejected the suspected root cause | Debugging | Removing one suspected hook leaves the symptom unchanged | SNES | `references/tips/general/cases.md#isolated-removal-rejected-the-suspected-root-cause` |
| Rare paths may depend on table-tail entries | Build and verification / Text extraction / Reinsertion and hooks / Initial survey | Only one branch corrupts immediately after entry | SNES | `references/tips/general/cases.md#rare-paths-may-depend-on-table-tail-entries` |
| Terminators may be multi-byte stateful sequences | Text extraction | A scanner treats the first byte of a control sequence as termination | SNES | `references/tips/general/cases.md#terminators-may-be-multi-byte-stateful-sequences` |
| Post-decompression patches reused downstream transfers | Compression / Runtime assets / Reinsertion and hooks | Part of a compressed UI needs replacement without a compatible recompressor | SNES | `references/tips/general/cases.md#post-decompression-patches-reused-downstream-transfers` |
| Whole-canvas rendering preserved cross-tile effects | Graphics text / Runtime assets / Build and verification | Outlines, gradients, or highlights break at tile seams | SNES | `references/tips/general/cases.md#whole-canvas-rendering-preserved-cross-tile-effects` |
| Moving flexible data first reclaimed constrained space | Reinsertion and hooks | Same-bank and cross-bank references compete for limited space | SNES | `references/tips/general/cases.md#moving-flexible-data-first-reclaimed-constrained-space` |
| Font parsing success does not prove usable glyphs | Fonts and encoding | A parsed font rasterizes to empty glyphs | SNES | `references/tips/general/cases.md#font-parsing-success-does-not-prove-usable-glyphs` |
| Runtime samples can locate compressed source assets | Compression / Initial survey / Runtime assets / Debugging | Live glyphs are known but the compressed source location is not | SNES | `references/tips/general/cases.md#runtime-samples-can-locate-compressed-source-assets` |
| Layout limits include physical writes and clear lifetime | Reinsertion and hooks / Runtime assets / Translation / Build and verification | Text fits logically but leaves residue or damages adjacent UI | SNES / NES / Mega Drive | `references/tips/general/cases.md#layout-limits-include-physical-writes-and-clear-lifetime` |
| Static overlays overwrote runtime-updated cells | Graphics text / Runtime assets / Reinsertion and hooks | A translated static tilemap overwrites dynamic UI state | SNES | `references/tips/general/cases.md#static-overlays-overwrote-runtime-updated-cells` |
| Asset reachability does not prove readable text | PoC / Runtime assets / Fonts and encoding | Patched bytes reach VRAM but the intended glyph is not legible | SNES | `references/tips/general/cases.md#asset-reachability-does-not-prove-readable-text` |
| Visible layout and screen bounds determined dialogue-window size | Translation / Reinsertion and hooks / Build and verification | Korean dialogue exceeds a fixed window or the screen edge | SNES | `references/tips/general/cases.md#visible-layout-and-screen-bounds-determined-dialogue-window-size` |
| Selection highlighting depended on data and consumer range | Graphics text / Runtime assets / Reinsertion and hooks / Build and verification | Highlighting covers only the source-length prefix of a translated row | SNES | `references/tips/general/cases.md#selection-highlighting-depended-on-data-and-consumer-range` |
| Pointer tables may not be reread between states | Text extraction / Reinsertion and hooks / Runtime assets | Changing a second table entry has no effect after a transition | SNES | `references/tips/general/cases.md#pointer-tables-may-not-be-reread-between-states` |
| Reused slots retain unwritten data | Translation / Reinsertion and hooks / Runtime assets / Build and verification | Short or empty entries leave old cells in a scrolling buffer | SNES | `references/tips/general/cases.md#reused-slots-retain-unwritten-data` |

## Platform-specific cases

| Case | Judgment areas | Read when | Required platform context | Reference |
|---|---|---|---|---|
| NFTR tags and CMAP order follow on-disk consumer semantics | Fonts and encoding / Runtime assets / PoC | Documented NFTR tags do not match raw bytes or a new CMAP entry is ignored | Nintendo DS | `references/tips/platforms/nds.md#nftr-tags-and-cmap-order-follow-on-disk-consumer-semantics` |
| MPR state resolved HuC6280 bank identity | Initial survey / Debugging | An immediate value in a handler is being treated as a physical bank ID | PC Engine | `references/tips/platforms/pce.md#mpr-state-resolved-huc6280-bank-identity` |
| Reloaded hooks mixed instruction-cache line states | Reinsertion and hooks / Runtime assets / Debugging | A reloaded hook mixes original and patched instructions across cache lines | PlayStation | `references/tips/platforms/ps1.md#reloaded-hooks-mixed-instruction-cache-line-states` |
| Composite glyph layout changed tilemap arithmetic | Fonts and encoding / Runtime assets | A 16×16 glyph's tile arithmetic confuses horizontal stride with a 2×2 layout | SNES | `references/tips/platforms/snes.md#composite-glyph-layout-changed-tilemap-arithmetic` |
| NMI graphics hooks leaked across screen states | Reinsertion and hooks / Debugging / Runtime assets / Build and verification | A graphics overwrite also runs on re-entry or neighboring screens | SNES | `references/tips/platforms/snes.md#nmi-graphics-hooks-leaked-across-screen-states` |
| One-time OBJ uploads ignored later WRAM patches | Runtime assets / Graphics text / Reinsertion and hooks | WRAM changes do not affect text already uploaded to OBJ VRAM | SNES | `references/tips/platforms/snes.md#one-time-obj-uploads-ignored-later-wram-patches` |
