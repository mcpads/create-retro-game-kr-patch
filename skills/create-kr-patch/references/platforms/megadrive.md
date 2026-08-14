# Sega Mega Drive / Genesis

Consult primary references for general CPU and VDP specifications as needed. For patch decisions, keep ROM coordinates, stored glyphs, VDP consumption, and expanded-media boundaries distinct.

## 1. Execution coordinates and data meaning

68000 execution endianness and alignment apply to hooks and directly read tables. They do not determine storage order in archives, VMs, or byte streams. Judge each field from the reader's loads, swaps, and address calculations.

When moving code, verify source instruction boundaries, PC-relative operands, branch targets, live registers, and condition codes at the new location.

## 2. ROM mapping and expansion

Direct CPU-address-to-file-offset mapping applies only within an established mapper-free range. Growing a file or changing header size representation does not expose the new ROM range to the CPU, hardware, or loader.

When using expanded space, verify mapper selection, header and checksum consumption, SRAM and peripheral mappings, and final-size support on distribution targets.

## 3. Stored glyphs and VDP consumption

ROM font bytes need not be the final VDP tile representation. When compression, RAM staging, or runtime conversion exists, connect stored assets, transformed output, VRAM transfer, and name-table or sprite consumption.

VRAM is shared with other screen assets. Separate total repertoire from state-specific working sets. Judge residency, reload, eviction, and last-writer lifetime through `references/strategy/font-strategy.md` §3 and `references/strategy/runtime-assets.md`.

Transfers must fit the game's DMA and interrupt-managed display state. Do not generalize success on a dialogue plane to Window, sprite, menu, or HUD paths.

## 4. Text and references

Do not derive encoding, token width, or pointer width, base, and alignment from the platform name. Establish them from actual fetch, dispatch, glyph lookup, and pointer consumers.

Apply `references/strategy/text-extraction.md` §4.4 to token policy and `references/strategy/text-extraction.md` plus `references/strategy/reinsertion.md` to extraction and relocation.
