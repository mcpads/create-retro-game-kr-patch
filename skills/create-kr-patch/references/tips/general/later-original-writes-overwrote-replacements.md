# Later original writes overwrote replacements

- **Search terms:** later original write, overwritten translation, last writer, VRAM collision, subtitle, logo
- **Observed scope:** A layered SNES logo and PC Engine CD subtitles overwritten by later original writes.
- **Failure context:** Korean pixels were written before later source fragments or while an automatic transfer to the same region remained active.
- **Discriminating evidence:** Every write to the affected VRAM range was traced. Applying the replacement after the final transfer, or suppressing only the transfer that continually overwrote it, preserved both the Korean asset and unrelated screen updates.
- **Established result:** Adding a replacement write did not remove later original writers; the intervention had to follow the last write or isolate the confirmed collision.
- **Transfer limit:** Re-derive address, timing, and display lifetime for each scene, and do not disable unrelated original updates.
- **Related criteria:** `references/strategy/runtime-assets.md` §2, `references/strategy/reinsertion.md` §4.
