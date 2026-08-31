# Apparent disc gaps overlapped file extents

- **Search terms:** disc free space, LBA overlap, file gap, opening movie corruption, relocation, directory extents
- **Observed scope:** Relocated data-track files and an opening movie in a Dreamcast disc image.
- **Failure context:** A large gap between files was assumed free, causing a relocated file to overlap a later movie extent.
- **Evidence:** Every root-directory LBA extent was compared with the relocation result. A product artifact with the relocated data placed after the last recorded occupied extent played the opening movie successfully.
- **Established result:** New data was placed only after accounting for every file extent recorded by the directory, preventing movie overwrite in this image.
- **Transfer limit:** This placement rule applies only when the directory completely describes occupied regions and track, volume, and contiguity constraints are also satisfied.
- **Related criteria:** `references/strategy/reinsertion.md` §5, `references/strategy/build-and-verify.md` §2·§4.
