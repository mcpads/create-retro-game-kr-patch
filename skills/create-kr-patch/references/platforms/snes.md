# SNES / Super Famicom

Consult primary references for general 65816, PPU, and ROM-mapping specifications as needed. Keep execution mode and instruction boundaries, ROM coordinates, stored fonts, and PPU consumption distinct.

## 1. Execution mode and hook invariants

The 65816 M/X state changes immediate-instruction length as well as register width. A hook or any relocated code must preserve the original instruction boundaries and effects for the entry M/X state, bank, direct page, stack, and live flags.

## 2. ROM coordinates and expansion

CPU-address-to-file-offset conversion applies only within an established mapping mode, mirror, copier-header representation, and special-chip mapping. Do not transfer one mapping's formula to another mode or expanded region.

Growing the ROM file does not make a new bank readable by the CPU, hardware, or loader. Place assets in expanded space only after verifying that the mapper can select it, the header and checksum can represent it, it does not conflict with save-memory or mirror mappings, and the actual distribution target supports it.

## 3. Stored fonts and PPU consumption

Font bytes in ROM or WRAM need not be the final PPU tile representation. With compression, staging, or runtime layout conversion, connect stored assets, pre-transfer representation, VRAM coordinates, and tilemap or OBJ consumption.

VRAM register coordinates and file byte offsets may use different units. Declare units at the conversion boundary and use one established coordinate conversion. Do not generalize dialogue BG success to OBJ, menu, or graphics-text paths.

## 4. Transfer and asset lifetime

VRAM writes and DMA must fit the game's blanking, NMI queue, and transfer order. If a patch appears briefly and disappears, identify every writer, the last writer, reloads after screen transition and re-entry, and other consumers of the staging region.

For a new font bank, overlay tile, or additional slot, verify load, residency, and consumption through `references/strategy/runtime-assets.md`.

## 5. Text and references

Establish character and token width from actual fetch mode and pointer advancement, not CPU name. A pointer cannot determine a file target without current bank, base, and mapping.
