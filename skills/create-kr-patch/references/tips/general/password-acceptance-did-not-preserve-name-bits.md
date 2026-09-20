# Password acceptance did not preserve name bits

- **Search terms:** password roundtrip, blank imported name, truncated Hangul tag, display alphabet, legacy password
- **Observed scope:** Character export and import through a PlayStation game's password system, alongside a separate CPU-configuration password.
- **Failure context:** Relabeling the password alphabet allowed native re-entry and acceptance, but the accepted character lost its Hangul name. The original encoder narrowed name words to byte values; the decoder could not reconstruct the discarded tags.
- **Discriminating evidence:** Compare the source name, encoded payload and complete decoded character record, rather than acceptance or displayed symbols alone. Source-code execution exposed narrowing. After buffer relocation, a native CPU-password check also found an encoder still writing the old destination while display read the new one.
- **Established result:** An extended character codec preserved complete name words and retained legacy imports with explicit format discrimination. Generated-code checks covered admitted names, malformed inputs and preserved character data; native re-entry preserved representative Hangul names. The separate CPU codec retained its original format after its missed destination was corrected.
- **Transfer limit:** Establish payload capacity, format discrimination, validation and every shared buffer writer/reader before changing a codec. Compare all fields promised by the export, not only the name. Alphabet conversion cannot restore lost payload bits or make an extended export compatible with the original decoder; already-lossy exports require a surviving source record.
- **Related criteria:** `references/strategy/name-entry.md` §4·§6, `references/strategy/reinsertion.md` §2·§3.
