# Evidence-backed case

## Asset expansion without metadata growth halted before title

- **Search terms:** white screen before title, container item count, font expansion, metadata layout, equal-size control build
- **Observed scope:** GP2 initialization and builds that added MES font entries to revision 0 of the Japanese Nintendo DS release of Dragon Quest IX.
- **Failure context:** A ROM with many added Hangul glyphs stayed on a white screen before the title. Code-table order, internal file size, and entry count changed together, so the failing boundary was not isolated.
- **Evidence:** Code order and MES expansion were separated. Builds differing by one internal entry changed the initialization result even without changing the candidate grid. A build that kept physical file size but restored the header and entry layout of a booting control reached the title again.
- **Established result:** Failure followed internal entry structure even when file size stayed equal; physical container growth alone did not explain this build set.
- **Transfer limit:** Separate physical size, entry count, metadata, and data placement with controlled builds. Treat initialization and actual consumption of the added assets as separate claims.
- **Related criteria:** `references/strategy/runtime-assets.md` §1·§2, `references/strategy/reinsertion.md` §1.2, `references/strategy/debugging.md` §2.2·§3.
