# Relocated label addresses also identified items

- **Search terms:** item name relocation, item use rejected, address comparison, identity guard, progression blocker
- **Observed scope:** Inventory-label relocation across three PC-98 scenarios, with an observed route-item failure in one scenario.
- **Failure context:** A moved label remained displayable, but the item-use handler compared the selected record's label address with the old address. The correct route item was rejected.
- **Discriminating evidence:** Decode the complete item-use guard and connect its comparison operand to a renderer-proven inventory record. The pre-fix record and comparison differed; a real-source regression failed on that mismatch. Text spans and incomplete or unrelated instruction patterns were excluded from rewrite ownership.
- **Established result:** Identity comparisons moved with their labels. On the corrected scenario, native save loading followed by ordinary item use retained refusal at the wrong location and completed the intended event and floor transition at the correct location, without a new event or route-item injection.
- **Transfer limit:** A string address may serve both rendering and identity. Search the target's use and comparison paths when relocating it, but matching numeric constants alone do not authorize edits. The observed scenario does not prove every item or every scenario's runtime path.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§2·§3, `references/strategy/text-extraction.md` §1.3.
