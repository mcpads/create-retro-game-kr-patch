# Evidence-backed case

## State changes may reload a different font asset

- **Search terms:** state-specific font reload, character selection, replacement not registered, existing loader, post-selection asset
- **Observed scope:** State-specific font loading after character selection in a Saturn title.
- **Failure context:** Observation stopped before selection and the replacement file was not registered in the image, leading to the false conclusion that no later reload existed.
- **Evidence:** Tracing from confirmed selection through the original loader showed a marked replacement passing through the existing open and decompression path into the live font region.
- **Established result:** An existing post-selection load path supplied the state-specific font and could carry a replacement asset.
- **Transfer limit:** Do not extend this result to other entry, return, or reload paths. Derive glyph capacity from each state's actual allocation and consumer.
- **Related criteria:** `references/strategy/font-strategy.md` §3·§5, `references/strategy/runtime-assets.md` §2.
