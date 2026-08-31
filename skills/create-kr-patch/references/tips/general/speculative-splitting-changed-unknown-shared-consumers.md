# Speculative splitting changed unknown shared consumers

- **Search terms:** shared string, unknown consumer, speculative split, neutral translation, alias set, semantic conflict
- **Observed scope:** Two PC-98 slots sharing one source string when only one slot's spell-learning consumer was known.
- **Failure context:** The known slot's meaning was used to break sharing and assign a different translation to the still-unknown slot, despite no evidence of a semantic difference.
- **Discriminating evidence:** The accompanying name table and runtime display were compared. A translation valid for the confirmed scope remained shared, and splitting was deferred until the unknown consumer demonstrated a conflict.
- **Established result:** Identifying one consumer of a shared string did not establish the meaning of the other consumers.
- **Transfer limit:** Do not split shared entries based on semantic possibility alone. If a real conflict later requires a split, bind the evidence to the exact slot and alias set.
- **Related criteria:** `references/strategy/translation-workflow.md` §2.1·§2.3·§3, `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §2, `references/conventions/translation-artifacts.md` §1.1.
