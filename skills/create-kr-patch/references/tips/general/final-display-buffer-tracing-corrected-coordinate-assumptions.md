# Final display-buffer tracing corrected coordinate assumptions

- **Search terms:** wrong window base, shifted price, dialogue order, staging buffer, final VRAM copy
- **Observed scope:** Shop prices and the Hangul renderer in the Game Gear release of Madou Monogatari 1.
- **Failure context:** Prices moved to the bottom of the window instead of appearing beside `금`, and later dialogue order also drifted. The final VRAM write only copied a completed row, so the price cursor was not the direct cause.
- **Decisive test:** Changes were traced backward from the work buffer to the VRAM transfer, and each window's tile base was compared with the original initialization table. Separating the shared-window and normal-window base values fixed both price placement and dialogue order.
- **Established result:** The wrong base selected before drawing the window, not the final price write, caused both symptoms.
- **Transfer limit:** Reconfirm slot placement and per-window base selection for every other UI.
- **Related criteria:** `references/platforms/gg.md` §4, `references/strategy/debugging.md` §3·§4.
