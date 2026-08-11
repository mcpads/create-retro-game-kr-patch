# Sega Saturn

Consult primary references for general SH-2, VDP, and CD-ROM specifications as needed. Keep moved-code literal and delay semantics, VDP1 and VDP2 consumption, modules, compression, and disc layers distinct.

## 1. Moved code and loaded modules

Which SH-2 and task execute target code is game-specific. When moving an instruction or growing a block, verify branch delay, PC-relative literal pools, alignment, live registers, PR, flags, and code versus inline-data boundaries.

## 2. Separate VDP1 and VDP2 consumers

VDP1 command and texture paths and VDP2 pattern and name-table paths have different asset, address, palette, clipping, and lifetime conditions. Do not generalize one renderer's Hangul PoC to another renderer, menu, battle, or graphics text.

Determine VDP2 character, palette, and flip meaning and active VRAM budget from current pattern-name data size, PNCN supplementary mode, color depth, character size, and plane configuration. Do not use theoretical total capacity or one fixed bit width as every screen's glyph limit.

For new glyphs, connect loader, work RAM, VRAM upload, and final command or name-table consumption through `references/strategy/runtime-assets.md`.

## 3. Text, pointers, and loadable modules

CPU endianness does not determine script-VM or container-field storage. When a loadable module or event script mixes absolute addresses, relative offsets, indexes, and inline code or data, establish each consumer and actual loaded module separately.

When a file grows, inspect load buffers, following code, literals and metadata, interior entries, shared tails, and duplicate address or size tables in other files as well as text pointers. One title's pointer pattern is not a platform rule.

## 4. Compressed assets

Establish the compression variant from the target loader and game decompressor. Names and magic only narrow candidates. Judge target-consumer compatibility and defect controls through `references/strategy/compression.md`.

## 5. Disc and ISO layers

Track and sector representation, filesystem extents, and game LBA or size tables are different layers. A valid ISO directory does not prove that the game loader reads a moved file. Treat a multi-extent file as one file through its final record, but do not introduce new placement without established loader support.

A new location must fit the data track and filesystem, avoid overlap with other extents, tracks, and pregaps, and satisfy game read alignment, buffers, and streaming. When changing raw user data, update only protection fields for the modified sector's actual mode and preserve untouched irregular fields.
