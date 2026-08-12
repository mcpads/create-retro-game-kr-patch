# PC Engine / CD-ROM²

Consult primary references for general HuC6280, VDC, and CD-ROM² specifications as needed. Keep MPR-derived coordinates, CD loading and runtime overlays, stored fonts, and screen consumption distinct.

## 1. MPR and address identity

A logical address does not determine a ROM, RAM, or file location. The MPR state at access time and the medium's physical layout are also required; CD-loaded code and buffers additionally require the loader's sector or file to RAM relationship.

When a pointer stores only a logical address, current MPR and base are part of the specification. A bank-changing hook must verify interrupt and callback shared pages, code and data lifetime, and return mapping. Do not represent current mapping as a constant before identifying the executing overlay.

## 2. Stored glyphs and VDC consumption

A ROM or RAM font need not be the final VDC pattern representation. With compression, staging, or runtime composition, connect stored assets, pre-transfer representation, VRAM, and BAT or sprite consumption.

VRAM is shared with other screen assets, so theoretical capacity is not a font budget. Evidence from dialogue, menus, sprites, graphics text, and BIOS font paths applies only to each consumer. Judge a new font page or cache through `references/strategy/runtime-assets.md`.

## 3. HuCard and CD-loaded boundaries

A HuCard file extension does not expose a new physical segment to hardware or the loader. The mapper and distribution target must actually select the range.

Connecting a CD-game runtime address to disc location requires track and sector representation, file or sector start and read length, destination RAM and MPR, and overlay reload identity. Do not generalize a BIOS call name or one title's loader sequence to all CD paths.

When claiming support for a System Card, identify that target and verify the final candidate on its execution path.

## 4. CD images and sectors

Do not mix cooked user-data offsets with raw-sector file offsets. When writing raw output, the serialization boundary updates protection fields for the actual sector mode. Do not normalize untouched audio, irregular sectors, or track padding without evidence.

When moving a file or asset, verify game sector and length tables, read alignment, RAM buffers, and streaming timing in addition to the filesystem. A range resembling empty sectors is not free space until other tracks, pregaps, and streaming reservations are excluded.

## 5. Text and new runtime paths

Establish encoding, tokens, and pointer boundaries from the real consumer. When adding subtitles to voiced or cutscene paths, connect applicable CD-DA or ADPCM state, VDC BAT or sprite layers, and subtitle lifetime and consumption across scenes and overlays. Judge display, progression, input, and synchronization through `references/strategy/build-and-verify.md` §5.

Hangul visibility through a BIOS font path proves only that path, not new code space, complete glyph supply, or another renderer. Judge remaining conditions through PoCs in `references/strategy/poc.md`.
