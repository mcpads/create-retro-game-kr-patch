# Missing control sequences stopped progression

- **Search terms:** missing terminator, cutscene end, control-code audit, false missing-token warning, progression stop
- **Observed scope:** Event scripts in the Mega Drive release of Madou Monogatari.
- **Failure context:** Entries that lost dialogue-end or cutscene-end controls stopped progressing after input. A simple set comparison also produced false warnings when a prior version split one source entry across adjacent entries.
- **Discriminating evidence:** Control tokens were compared exhaustively per entry. Missing termination was classified as progression-critical, while adjacent split structure was inspected before accepting a warning.
- **Established result:** Real termination loss caused progression failure; token movement caused by an established adjacent-entry split did not.
- **Transfer limit:** Equal token sets do not prove equal order, arguments, or runtime meaning.
- **Related criteria:** `references/strategy/build-and-verify.md` §5, `references/strategy/text-extraction.md` §3.1·§4.4, `references/conventions/translation-artifacts.md` §3.
