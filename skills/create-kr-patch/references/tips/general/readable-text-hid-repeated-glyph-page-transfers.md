# Readable text hid repeated glyph page transfers

- **Search terms:** frame slowdown, idle menu, repeated glyph upload, page thrashing, partial residency, transfer synchronization
- **Observed scope:** World labels and an item-description window in a PlayStation game's paged Hangul supplier.
- **Failure context:** Readable labels repeatedly uploaded a whole glyph page. A separate window alternated its UI and description pages while idle. These uploads used an already-resident package, not repeated disc reads.
- **Discriminating evidence:** Collect caller, upload and synchronization events over defined frame intervals without event loss, separating first supply from idle repetition. Trace which callers request each page and compare actual serialized glyph pixels, since different catalog IDs may alias identical cells.
- **Established result:** Bounded world-label uploads and reuse of proven common glyphs removed unnecessary work in the observed paths. The item-window idle sample changed from 1,024 uploads in six frames to none. An intermediate partial-load candidate reduced transfers but left the next menu blank: clearing its page identity broke replacement eligibility. Retaining partial residency separately allowed the menu to request full supply.
- **Transfer limit:** Measure the target transition and preserve replacement, pinning and buffer lifetimes while reducing work. Removing waits from a reused scratch buffer had corrupted uploads in an earlier trial. Event-count reductions do not prove device FPS, all-scene performance, or elimination of first-load cost; discard overflowed traces from exact counts.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/font-strategy.md` §3, `references/strategy/debugging.md` §3·§5.
