---
name: draw-noodles-and-shady
description: Draw Dan's dogs Noodles and Shady on-model in the site's paper-cutout style, either as a full placeholder scene or as a small animated cameo on a real page. Use whenever a page needs the dogs or any new illustration.
---

# Draw Noodles and Shady

1. **Read** `docs/characters.md` and the "Illustration style" and "Motion" sections of `docs/style-guide.md`. Don't skip this. Off-model dogs are the main failure.

2. **Reuse the canonical drawings** instead of redrawing:
   - In `tools/build_placeholders.py`: `noodles()`, `noodles_leaping()`, `shady()`, plus props `frisbee()` and `soccer_ball()`, and scenery helpers `cut()`, `zigzag()`, `waves()`, `moon()` and `cloud()`.
   - Static copies are in `assets/characters/*.svg`. Both dogs face right, with the origin at the centre of the body.
   - To face left, wrap in `scale(-1 1)`. Scale both dogs by the **same factor** so Shady stays clearly bigger.
   - If you need a new pose (sitting, play-bow, lying down), add it as a new function next to the others, using the same colors and proportions. Then export it in the `__main__` block so `assets/characters/` stays the full reference set.

3. **Pick a pose that fits the dog:**
   - Noodles is calm, friendly and mature, and loves frisbee and swimming.
   - Shady is goofy and energetic, and loves soccer balls and tug-of-war; her tongue is out and she wags fast.

4. **Make it paper:** flat fills and no outlines, with each object wrapped in the `#paper` drop-shadow filter (`cut()` in the script). Any SVG outside the generated pages needs that `<filter id="paper">` copied into its own `<defs>`.

5. **Animate it** only with the shared classes in `style.css` (`wag`, `pant`, `float`, `paddle`, `tide`, `spin`, `tug`, `bounce`, `twinkle`). Keep it ambient: nothing reacts to hover or taps.

6. **Place it.**
   - **Placeholder scene:** add or edit an entry in `SPECS` in `tools/build_placeholders.py` and run `python3 tools/build_placeholders.py`. Keep the top 200 units clear for the headline and the action between x = 290 and 990.
   - **Cameo on a real page:** use one or two per page, inline `<svg aria-hidden="true">`, about 80–200px tall, in a margin, corner or gap between sections. It must not cover text or controls or shift the layout at any width. Put the motion classes inside the SVG, and add a `prefers-reduced-motion` rule if the cameo sits outside `main svg`.

7. **Check it** by screenshotting the page at 1440×900 and 600×1100 (commands in `AGENTS.md`) and looking at the images. Check that Shady is bigger than Noodles, the colors match the sheet, nothing overlaps text, and nothing important is cropped on the phone view.
