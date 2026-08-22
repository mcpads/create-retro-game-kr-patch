# Moving flexible data first reclaimed constrained space

- **Search terms:** mixed pointer width, same-bank constraint, cross-bank pointer, reclaimed source region, space allocation
- **Observed scope:** Text relocation in an SNES title with both three-byte cross-bank references and two-byte same-bank references.
- **Decision context:** Constrained and relocatable strings competed for limited space in the original bank.
- **Evidence:** References were classified by their proven address range. Relocatable data moved out first, reclaiming its old region for same-bank-only data. Every pointer and the cleared source region were then checked.
- **Established result:** Allocation order had to account for source space reclaimed by earlier relocations, not only currently free space.
- **Transfer limit:** This applies only after all references and address ranges are known and the reclaimed region has no interior entry, interior pointer, or other consumer.
- **Related criteria:** `references/strategy/reinsertion.md` §2·§3·§5, `references/conventions/data-formats.md` §4.
