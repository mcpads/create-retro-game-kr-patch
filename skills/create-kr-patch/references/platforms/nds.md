# Nintendo DS

Consult primary references for general NDS header, NitroFS, and VRAM specifications as needed. Connect execution images, overlays, files, and VRAM consumers through their own coordinates and identities.

## 1. Execution images and overlay identity

ARM9 and ARM7 images have separate load ranges. Which CPU handles text, fonts, or file loading is a game-specific fact. Establish responsibility through actual call and load paths.

Converting a runtime address to ROM location requires the current image's ROM extent, load extent, and transform state. Linear mapping applies only inside an uncompressed static image. Identify an overlay by overlay entry, file ID, FAT extent, and current load state; do not patch by RAM address alone when another overlay reuses it.

When compression, relocation, or initialization exists, do not compare stored overlay bytes directly with executed bytes. If the stored overlay grows or moves, verify file ID, FAT extent, stored size, and loader read buffer. If the decompressed runtime address or size, BSS bounds, or static initializers change, verify overlay entries, adjacent RAM, and initialization consumers separately. A change in stored file size does not imply a change in runtime placement.

## 2. Filenames and loader behavior

FNT names, FAT file IDs, raw ROM offsets, and game-specific archives may coexist. Finding one named SDK-style file does not establish the storage rule for every asset.

When a file grows or moves, follow the identity selected by the real loader and verify every referenced FAT extent, overlay entry, and game-specific offset or size table. A matching name or magic does not justify a standard serializer when the reader consumes fields, sections, or compression differently.

## 3. Stored assets and screen consumption

Decompression, RAM transforms, VRAM bank mapping, and caches may separate a stored font or bitmap from final BG, OBJ, bitmap, or 3D texture representation. Do not use a glyph observed in one engine or state as evidence for another.

When changing VRAM mapping, transfer timing, or cache slots, verify concurrent consumers and lifetime across screen transitions, sleep, and resume. Storing an asset and having a renderer locate, retain, and consume it are separate claims. Apply `references/strategy/runtime-assets.md` to such changes.

## 4. Secure-area and banner boundaries

The complete secure area, encrypted prefix within it, markers, and CRC ranges are different concepts. Determine whether the input is encrypted or decrypted, and which representation the distribution path requires, only when modifying this region. Do not re-encrypt or normalize an untouched secure area.

A banner may be absent, and Korean title slots and CRC ranges depend on the banner version. If a version increase is required, update and verify the complete banner length, version-specific fields and CRC ranges, any ROM data that follows the banner, and the target loader, not only the version word. Do not impose a banner upgrade on product artifacts whose declared changes do not modify it.
