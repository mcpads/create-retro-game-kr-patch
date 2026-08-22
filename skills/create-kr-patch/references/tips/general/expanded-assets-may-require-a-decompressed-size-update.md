# Evidence-backed case

## Expanded assets may require a decompressed-size update

- **Search terms:** decompressed-size constant, expanded compressed font, zero tail, loader length, container size mismatch
- **Observed scope:** An expanded compressed font with a separate fixed decompression-size value in a Saturn title.
- **Failure context:** New glyphs existed at the end of the decompressed file, but the corresponding live font memory remained zero. Updated file and compressed sizes were mistaken for proof that the whole asset loaded.
- **Evidence:** Comparing decompressed data with live memory located the cutoff and exposed a fixed old decompression length. Updating it to the actual output size made the full range agree.
- **Established result:** Expanding a compressed asset also required the loader's decompressed-size value to match the real output.
- **Transfer limit:** Re-derive the size field's unit and the loader's tail-read behavior.
- **Related criteria:** `references/strategy/compression.md` §5, `references/strategy/reinsertion.md` §1.2·§3·§5, `references/strategy/runtime-assets.md` §2.
