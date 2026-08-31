# Sega Dreamcast

Consult primary references for general SH-4, GD-ROM, and texture specifications as needed. For patch decisions, keep disc representation, execution representation, track coordinates, stored textures, and renderer consumption distinct.

## 1. Stored executables and runtime code

Converting a runtime address to a file offset requires the target executable or module's real load address, file layout, relocation, and decompression. Do not apply a conventional load address or high-address-bit rule to every title.

When the boot path scrambles or packs an executable, disc bytes and runtime instruction bytes are different representations. Before selecting an edit boundary, verify an unchanged round trip for the boot transform and identify the loaded target module.

When moving code, establish SH-4 branch-delay and PC-relative-literal semantics from current architecture references, then reverify source effects, targets, and literals after final placement. Apply `references/conventions/project-conventions.md` §2.3.

## 2. GDI track coordinates

Track LBA in the GDI descriptor, sector index inside a track, backing-file byte offset, and filesystem LBA are different coordinates. Do not transfer arithmetic from one coordinate to another, especially across tracks with different sector representations.

Verify descriptor and backing-file sector structure, size, and order together. Preserve data and audio distinctions, sessions, and pregaps. When moving an ISO file, inspect game-specific LBA and size tables plus streaming consumers in addition to directory extents.

Do not assume conversion to CDI or another container preserves source GDI track structure. Keep converted output distinct from the baseline GDI artifact and reverify boot, audio, streaming, and file content.

## 3. Texture and glyph consumption

Do not treat a texture encoder as technically verified from a file signature, extension, or decoded image alone. Establish pixel format, layout, palette, and size rules read by the target descriptor and upload path. If representation is not canonical, declare equivalence for decoded pixels, protected metadata, and consumer meaning.

The same label may use different textures or slots across different states, screens, and 2D or 3D renderers. Do not generalize one atlas result to every font or UI path. Apply `references/strategy/runtime-assets.md` when adding, growing, or moving an asset.

## 4. Text and references

Establish encoding, script VM, and pointer representation from actual read code. CPU endianness does not determine container or VM field order. Judge entry boundaries and pointer completeness through `references/strategy/text-extraction.md` and `references/strategy/reinsertion.md`.
