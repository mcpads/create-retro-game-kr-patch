# Cooked offsets corrupted raw-sector images

- **Search terms:** cooked ISO offset, raw 2352-byte sector, 2048-byte user data, pregap, CUE INDEX, wrong sector
- **Observed scope:** User-data and raw-sector representations of a PC Engine CD image.
- **Failure context:** A prior graphics offset used a pregap-free 2048-byte user-data ISO, while the build input was a 2352-byte Mode 1 BIN with pregap. Mixing those coordinate systems targeted another sector.
- **Decisive test:** A unique original byte sequence was located in extracted user data, pregap was calculated from CUE INDEX values, and the coordinate difference matched that calculation before only the affected sectors were rewritten.
- **Established result:** Converting the prior user-data offset into the target track's raw-sector coordinates aligned the source bytes and accounted for the pregap difference.
- **Transfer limit:** Recalculate the conversion from the target image's sector representation and track origin.
- **Related criteria:** `references/platforms/pce.md` §4, `references/strategy/build-and-verify.md` §2·§3.
