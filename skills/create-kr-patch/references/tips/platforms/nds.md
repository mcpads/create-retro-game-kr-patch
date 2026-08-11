# Nintendo DS-specific cases

## NFTR tags and CMAP order follow on-disk consumer semantics

- **Search terms:** NFTR, reversed chunk tags, RTFN, CMAP, PAMC, first-match mapping, linked chunks
- **Observed scope:** Original and Hangul-extended LC10 and LC12 NFTR files from the Nintendo DS release of LovePlus.
- **Failure context:** It was tempting to search the raw file for chunk names as written in documentation, or to append a new mapping after the existing CMAP chain and assume the consumer would reach it.
- **Evidence:** Two original and two extended files were parsed and serialized back byte-identically. `NFTR`, `FINF`, `CGLP`, `CWDH`, and `CMAP` were stored as `RTFN`, `FNIF`, `PLGC`, `HDWC`, and `PAMC`. Both originals ended their CMAP chain with a mapping covering `0x0000..0xFFFF`. A build that linked the Hangul mapping before that range still booted and rendered the existing Japanese menu.
- **Established result:** Byte-identical serialization of these four files required their reversed on-disk tags and linked pointers. Prepending the new mapping preserved loading and existing glyphs, but the consumer's CMAP lookup order and actual consumption of the new Hangul glyphs were not proven.
- **Transfer limit:** Reconfirm tag byte order in every target file. Do not adopt a mapping order as a reinsertion rule until the consumer's lookup behavior and a new glyph's display are both proven.
- **Related criteria:** `references/strategy/font-strategy.md` §2, `references/conventions/project-conventions.md` §5.1.
