# NES / Famicom

Consult primary references for the target mapper, CPU, PPU, cartridge image, and save hardware as needed. Keep cartridge representation, mapper state, CPU addresses, CHR ownership, and PPU consumption distinct.

## 1. Source representation and cartridge declaration

Headerless PRG and CHR data, iNES, and NES 2.0 images are different source representations. Identify the supported revision by content identity, representation, size, and header fields before converting addresses or applying a distribution patch. Do not make a comparison or prior-localization ROM the product source merely because it exposes useful structure.

The header declares mapper and submapper identity, mirroring, PRG and CHR sizes, and applicable RAM or nonvolatile memory. When a patch changes any of these conditions, verify the final declaration against the implemented circuit model, initialization, save path, emulator or hardware target, and applied distribution artifact. A valid payload with a stale header is not a valid release image.

## 2. Mapper-dependent CPU and file coordinates

A CPU address does not identify a PRG file offset without the mapper, active register state, window, and mirror behavior at access time. Establish fixed and switchable regions and every state transition that can select the target code or data.

When hooks or loaders change mapper state, verify entry mapping, interrupt and NMI interaction, nested calls, data visibility, and restoration on all exits. Growing PRG or CHR storage is usable only when the mapper, header, game code, and distribution target can select the new range.

## 3. CHR supply and PPU identity

Determine whether each consumer reads CHR ROM, CHR RAM, or a title-specific staging and upload path. Pattern bytes, name-table tile codes, attributes, palettes, sprite OAM, and logical text codes are different identities. The same tile code can display another glyph after a bank or runtime codebook change.

For dynamic Hangul pages, measure the active physical slots and establish which background, sprite, digit, control-produced, and variable-inserted glyphs must coexist throughout each relevant consumption lifetime. Apply `references/strategy/font-strategy.md` §3 and `references/strategy/runtime-assets.md` §2.

## 4. PPU transfer and frame lifetime

PPU and OAM updates must follow the target's display-off, blanking, NMI, DMA, and queue rules. A transfer that finishes eventually may still exceed the frame budget, show intermediate corruption, or race another writer.

When adding runtime tile generation or transfer, verify the worst applicable path through final machine code, including called routines. Observe the first request, every visible intermediate state, completion, reuse, invalidation, transition, and re-entry. One stable final frame does not prove a glitch-free transfer or correct lifetime.

## 5. Distribution patches and compatibility inputs

If users may possess headerless and headered forms of the same cartridge content, treat them as separate supported source profiles unless one canonical conversion is part of the documented application path. Each artifact must verify its declared source identity and reproduce the same intended cartridge content with the declarations required by its output representation.

Do not let compatibility input profiles create separate product builds or diverging write logic. Derive them from one integrated target and apply the source-representation and distribution checks in `references/strategy/build-and-verify.md` §2.
