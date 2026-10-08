# Removed install data left an active installation path

- **Search terms:** first boot, data installation, empty install dialog, removed payload, optional feature hang
- **Observed scope:** First-boot data installation in a PSP game under GUI PPSSPP.
- **Failure context:** A patched ISO with its installation payload removed supported ordinary play when installation was declined. Accepting installation instead opened an empty dialog and stopped progress.
- **Discriminating evidence:** With no save present, the same input sequence started installation on the Japanese source ISO but stalled on the patch. The emulator repeatedly reported an installation request with no files or data; the patched image's installation directory had been emptied.
- **Established result:** Payload removal left a reachable consumer requiring the missing files. Ordinary-play observations had bypassed that choice. The record established this failure mechanism, not a verified repair or behavior on PSP hardware.
- **Transfer limit:** When removing an optional payload, trace the entry points and completion behavior that still depend on it. Keeping, replacing, or retiring the feature depends on the target and adopted support scope.
- **Related criteria:** `references/strategy/runtime-assets.md` §2·§3, `references/strategy/build-and-verify.md` §4·§5·§6.
