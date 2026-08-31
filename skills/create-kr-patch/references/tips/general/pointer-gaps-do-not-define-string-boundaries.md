# Pointer gaps do not define string boundaries

- **Search terms:** overlapping strings, shared tail, next pointer, terminator, nested script entries
- **Observed scope:** Overlapping script entries in the Dreamcast release of Puyo Puyo~n.
- **Failure context:** The relocator treated the next scene pointer as the end of the current scene. Several entry points actually shared later dialogue and portrait controls and continued to the same terminator.
- **Discriminating evidence:** For every scene start, the actual terminator was located and compared with the next scene start.
- **Established result:** The next scene pointer was not an end boundary; multiple scenes consumed a shared tail through the same terminator.
- **Transfer limit:** Determine overlap from each entry point's actual consumption range through its terminator.
- **Related criteria:** `references/strategy/text-extraction.md` §1.3, `references/strategy/reinsertion.md` §2.
