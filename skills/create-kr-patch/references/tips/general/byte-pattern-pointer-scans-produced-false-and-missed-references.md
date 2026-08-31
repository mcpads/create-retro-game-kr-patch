# Byte-pattern pointer scans produced false and missed references

- **Search terms:** false pointer positive, missed pointer, byte-pattern scan, Shift_JIS trail byte, compressed pixels, reference catalog
- **Observed scope:** Raw values in Saturn command arguments, SNES compressed graphics, and PC-98 strings that resembled pointers or instructions.
- **Failure context:** Byte shape and numeric range admitted command arguments, compressed pixels, and encoded characters as references. A suffix blacklist then removed real references too.
- **Discriminating evidence:** Candidates were classified by their containing record, target range and alignment, and actual consumption format.
- **Established result:** Storage structure and consumer behavior, not byte shape, determined whether a value was a reference.
- **Transfer limit:** Do not discard interior string targets from overlap alone; they may be shared tails or interior entry points. Re-establish storage and read paths for every format.
- **Related criteria:** `references/strategy/text-extraction.md` §1.2·§1.3·§3.5, `references/strategy/reinsertion.md` §2.
