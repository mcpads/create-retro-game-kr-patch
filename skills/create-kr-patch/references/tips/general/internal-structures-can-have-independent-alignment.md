# Evidence-backed case

## Internal structures can have independent alignment

- **Search terms:** internal alignment, subheader boundary, final file aligned, later page corrupt, pointer table, padding
- **Observed scope:** Internal structures following text in a Saturn title, and subheaders connecting multiple pages in a Mega Drive title.
- **Failure context:** The final file was aligned, but changed preceding data moved pointer tables, controls, or subheaders off the boundaries required by their consumers. Early content worked while later structures stopped or decoded corrupt metadata.
- **Decisive test:** Every consumed structure start was checked independently and padded after the preceding data as required.
- **Established result:** Alignment applied to each directly consumed internal structure, not only the final file end.
- **Transfer limit:** Derive both alignment unit and target boundaries from each structure's consumer.
- **Related criteria:** `references/strategy/reinsertion.md` §1.2·§3·§6, `references/conventions/data-formats.md` §5.
