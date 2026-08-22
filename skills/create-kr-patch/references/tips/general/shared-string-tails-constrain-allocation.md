# Shared string tails constrain allocation

- **Search terms:** shared string tail, suffix deduplication, pointer table scope, bank allocator, aliasing
- **Observed scope:** Several Game Gear text pointer tables relocated into the same spare bank.
- **Decision context:** Sharing string suffixes saved space, but one global sharing pool across unrelated tables allowed a layout change in one table to break references in another.
- **Evidence:** Bank allocation remained shared while suffix candidates were rebuilt independently for every pointer table. All consumer paths ran correctly when sharing remained within each table.
- **Established result:** A suffix could be shared only within a table whose references used the same base, read path, lifetime, and change unit—not merely anywhere in the same physical bank.
- **Transfer limit:** Expand sharing only across tables proven to have the same reference representation, base, path, lifetime, and update boundary.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§5.
