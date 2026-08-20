# Nintendo DS-specific cases

## NFTR tags and CMAP order follow on-disk consumer semantics

- **Search terms:** NFTR, reversed chunk tags, RTFN, CMAP, PAMC, first-match mapping, linked chunks
- **Observed scope:** Original and Hangul-extended NFTR files from the Nintendo DS release of LovePlus.
- **Failure context:** It was tempting to search the raw file for chunk names as written in documentation, or to append a new mapping after the existing CMAP chain and assume the consumer would reach it.
- **Evidence:** Source and extended files were parsed and serialized back byte-identically. Chunk tags appeared byte-reversed on disk, such as `NFTR` as `RTFN` and `CMAP` as `PAMC`, and the original CMAP chains ended in a catch-all mapping. A build that linked the Hangul mapping before that entry still booted and rendered the existing Japanese menu.
- **Established result:** Byte-identical serialization required the on-disk tag order and linked pointers. Prepending the new mapping preserved loading and existing glyphs, but the consumer's CMAP lookup order and actual consumption of the new Hangul glyphs were not proven.
- **Transfer limit:** Reconfirm tag byte order in every target file. Do not adopt a mapping order as a reinsertion rule until the consumer's lookup behavior and a new glyph's display are both proven.
- **Related criteria:** `references/strategy/font-strategy.md` §2, `references/strategy/runtime-assets.md` §1·§2, `references/strategy/poc.md` §3, `references/platforms/nds.md` §2·§3, `references/conventions/project-conventions.md` §5.1.
