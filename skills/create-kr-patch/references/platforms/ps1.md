# PlayStation

Consult primary references for general MIPS, GPU, CD-ROM, and ISO 9660 specifications as needed. Keep runtime code, stored assets, raw sectors, and filesystem coordinates distinct.

## 1. Execution code and module identity

Converting a runtime address to file location requires the current executable, overlay, or module's load extent, relocation, and decompression. Do not transfer a conventional load address or one executable's conversion to another module.

Code bytes read from RAM may differ from the instruction stream executed through CPU cache. For dynamically loaded or overwritten code, establish the loaded module, aliases and cache state, and update time. Verify hooks and moved instructions against current ISA references for delay, load hazards, and live state. Apply `references/conventions/project-conventions.md` §2.3 to generation and reinterpretation.

## 2. Fonts and GPU consumption

The presence of a BIOS glyph service does not prove that a target game or every screen uses it. Connect an established call path's return representation, game transforms and cache, VRAM upload, and actual primitive consumption.

Do not approve a custom font or texture from decoded file output alone. Connect stored asset, RAM representation, VRAM coordinates and CLUT, and screen consumption. Apply `references/strategy/runtime-assets.md` when adding, growing, or moving it.

## 3. Text, archives, and references

CPU endianness does not determine character bytes, archive fields, or script-VM storage order. Establish them from the reader's loads, swaps, pointer increments, and consumers.

A script module may mix absolute RAM pointers, module-relative offsets, indexes, and inline code. When text grows, inspect following code and metadata plus internal position-dependent values, not only string references. A shared extension or developer precedent is a candidate; re-establish it through unchanged round trip and the target reader.

## 4. Raw-sector and ISO coordinates

Mode 2 sectors may use different forms within one data track. Determine duplicated subheader and form for each modified sector and apply only its EDC/ECC rules. Do not normalize untouched irregular or protected sectors.

An ISO file need not have one continuous extent. Collect multi-extent records through the terminating record, then update duplicate-endian extent and length plus every moved directory, path, and game-specific LBA or size field. Do not introduce new multi-extent layout without proving loader support.

Filesystem LBA, raw-track sector, and image byte offset are different coordinates. Raw-sector output requires revalidation of protection fields even for same-size in-place replacement. Use an apparently empty region only when data track, filesystem, and loader all permit new consumption.

## 5. Runtime CD state

A new asset read may compete with the existing CD state machine, IRQ and DMA, and XA, CDDA, or movie streaming. Neither reuse of an existing loader nor separate device control is a default solution.

When changing a read path, prove initialization and re-entry at call time, read mode, sector form, buffer, concurrent streaming, restoration of command, IRQ, and DMA state, and asset lifetime across scene transitions. One successful read does not prove long-lived consumption.
