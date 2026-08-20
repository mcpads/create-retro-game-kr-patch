# Game Boy and Game Boy Color

Consult primary references for the target cartridge hardware, CPU, PPU, and save device as needed. Keep logical addresses, mapper state, stored tiles, VRAM consumption, and persistent records distinct.

## 1. Cartridge identity and banked addresses

A 16-bit logical address does not determine a ROM file offset in a switchable window. Establish the cartridge controller, fixed and switchable windows, selected bank, and any bank-number normalization used by the target at each access.

When a hook or far-call changes banks, verify code and data availability, interrupt-visible state, nested calls, and restoration on every return path. Do not transfer one title's bank-switch sequence to another cartridge controller or assume that a bank value has the same meaning in ROM, RAM, and a build tool.

## 2. ROM growth and cartridge declarations

Growing a ROM file does not make additional banks selectable. Verify that the cartridge controller, header representation, bank-selection code, and actual distribution target can address the final range. Recompute fields affected by the final image only after establishing their consumers, and keep copier or container bytes outside the cartridge image distinct from the cartridge header.

If a patch changes cartridge type, ROM size, RAM size, color compatibility, or other execution declarations, verify initialization, save mapping, boot behavior, and target emulator or hardware support. A build that boots in one tolerant emulator does not prove a valid cartridge image.

## 3. Stored graphics and PPU consumption

ROM graphics, work-RAM staging, VRAM tiles, tile maps, attributes, palettes, and sprite data are separate representations. Establish which bank and transfer path supplies each edited screen. A candidate keyboard, an editing field, and later name displays may use different tile sources even when they show the same logical character.

When a patch writes or streams tiles dynamically, verify access timing, transfer amount, active VRAM bank on Game Boy Color, destination ownership, and later writers. Apply `references/strategy/runtime-assets.md` to load, residency, clearing, transition, and re-entry. Evidence from a background path does not establish sprite or alternate color-mode consumption.

## 4. Persistent cartridge RAM

Persistent data depends on the actual RAM enable, bank selection, cartridge controller, battery or save-device declaration, and the game's serialization path. Bytes observed in active RAM do not prove that the target persisted them or that a later process will reopen the same storage.

When changing player names or other saved text, apply `references/strategy/name-entry.md` §4 and §6. Separate same-session redisplay, native reset or power-cycle behavior, and a fresh emulator or device session. Bind evidence to the exact ROM and save identity, and record any launcher or save-directory behavior that can replace or discard the save.

## 5. Text, input, and runtime composition

Establish character width, control values, input tables, and glyph lookup from actual consumers. Do not use visible keyboard order as source-tile order or stored-code order without tracing the selector and copy path.

For broad Hangul input or runtime-composed glyphs, measure ROM-bank space, emitted-code space, active tile supply, and cache lifetime separately. Apply `references/strategy/name-entry.md` to the input and persistence chain and `references/strategy/font-strategy.md` to repertoire, composition, and working-set decisions.
