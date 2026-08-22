# Composed name input needs one identity across editing, storage, and reuse

- **Search terms:** Hangul name input, composition state, committed name record, save reload, dynamic name glyph, redisplay mismatch
- **Observed scope:** Hangul name entry in the Japanese Game Boy Color release of Arle no Bouken, limited to a declared repertoire.
- **Failure context:** A smaller fixed candidate table could prove selection and one dialogue, but it could not provide the adopted repertoire or establish that later consumers and saved records used the same syllable identity.
- **Evidence:** Editing state, the committed record, dialogue rendering, save data, title continuation, and field redisplay were bound to one identity. The declared repertoire was checked against both a reference model and the generated implementation; representative controller input then survived save, power cycle, and reload.
- **Established result:** Name support required one validated identity from input state through the committed record and every redisplay and persistence boundary, while static exhaustive coverage and representative runtime evidence remained separate claims.
- **Transfer limit:** Re-derive candidate order, edit stages, record structure, supported repertoire, save format, and every consumer. A reset or power-cycle test in the same emulator process does not prove persistence after restarting the emulator, and representative names do not provide human visual approval of the complete repertoire.
- **Related criteria:** `references/strategy/name-entry.md` §2·§4·§6, `references/strategy/font-strategy.md` §3, `references/strategy/runtime-assets.md` §2, `references/strategy/build-and-verify.md` §4·§5.
