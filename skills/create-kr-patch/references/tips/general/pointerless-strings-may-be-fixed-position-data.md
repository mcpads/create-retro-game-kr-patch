# Pointerless strings may be fixed-position data

- **Search terms:** pointerless string, fixed absolute offset, leading menu names, compaction corruption, no rewritable reference
- **Observed scope:** Name strings before the first pointer target in a PC-98 menu-data file.
- **Failure context:** Compacting those leading strings because no pointer-table reference was visible made names blank or changed them to neighboring entries; a consumer read them at fixed offsets.
- **Decisive test:** Pointer tables and actual consumers were traced together. Confirmed fixed-offset strings remained in place with local fill, while later movable strings retained normal relocation.
- **Established result:** Absence of a rewritable pointer did not grant relocation permission; a consumer could read an absolute position directly.
- **Transfer limit:** Do not mark every pointerless entry fixed. Decide from the real consumer and the existence of a rewritable reference.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §1.2·§2·§3, `references/strategy/build-and-verify.md` §3·§4.
