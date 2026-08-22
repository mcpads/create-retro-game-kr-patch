# Sega Game Gear

Consult primary references for general Z80, VDP, and mapper specifications as needed. For patch decisions, keep bank-dependent execution coordinates, VDP ports, value producers, stored assets, and screen consumption distinct.

## 1. Logical addresses and bank identity

A 16-bit logical address does not determine a ROM file location. The slot, bank register, fixed window or RAM mapping, and mapper variant at access time are also required. Treat logical-address, bank, and file-offset conversion as specification only within an established mapping.

When a hook changes banks, verify code and data lifetime plus shared interrupt and callback state, then restore the entry bank and interrupt state. No one enable/disable sequence is a global solution.

## 2. ROM expansion

Changing file size and header size code does not expose an additional bank. Place assets there only when mapper selection, header and checksum consumers, save-RAM windows, and actual cartridge or loader support can represent the range.

## 3. VDP coordinates and write observation

VRAM and CRAM are consumed through VDP port I/O rather than ordinary memory writes. Absence from a normal memory-write log does not prove absence of a screen write.

Current VDP registers, scroll, and display state determine the relationship between internal name tables and the LCD viewport. Do not use one fixed row or column offset or theoretical tile count as every screen's coordinate or font budget.

Trace the path before and after transfer to determine whether a stored glyph is the final VDP tile representation or an intermediate RAM form.

## 4. From storage to screen consumption

A VDP port transfer is the final hardware upload or write boundary. It may be performed by a different writer than the one that produced the value, and it may occur at a different time from the asset load. Verify separately whether the write reaches the active name table or sprite data and the visible viewport. When using font data in a new bank or new VRAM slots, perform the link assessment in `references/strategy/runtime-assets.md` §2 and evaluate state-specific working sets through `references/strategy/font-strategy.md` §3.

## 5. Text and code space

Establish encoding, token width, and pointer rules from each game's consumers. For a new prefix or pair, count only the values actually accepted by the consumer as available code space after excluding source characters, controls, terminators, and values assigned meanings by separate renderers.

## 6. Code intervention and space

Derive hook shape and depth from real branch range, bank budget, live state, and source effects, then verify under `references/strategy/reinsertion.md` §4. For shared variable-width-font or tile-allocation state, identify every writer and initialization, transition, and release path.
