---
name: add-game
description: Add one of Dan's small vibe-coded games to dangroshan.dev under games/<slug>/. It must be plain HTML/JS, need no build step, and work on phone and desktop. Use when Dan wants to add or publish a game on the site.
---

# Add a game

1. **Agree on the slug and title with Dan**, using a short kebab-case slug like `games/shady-goal/`. Dan writes any description or blurb about the game. Short in-game labels (Score, Play again, Paused) are fine for you to write.

2. **Create `games/<slug>/index.html`**, self-contained:
   - Plain HTML, CSS and JS. No framework, bundler or build step.
   - Put extra files (sprites, sounds) in the same folder with relative paths.
   - If you need a library, load it from a CDN with an exact pinned version; otherwise use none.
   - Include `<meta name="viewport" content="width=device-width, initial-scale=1">`, `<meta name="color-scheme" content="dark">` and a `<title>` of the form "<Game> · Dan Groshan".
   - Link `../../style.css` for the tokens and fonts, and use the dark-blue palette. If the game has art, follow `docs/style-guide.md`. Use the `draw-noodles-and-shady` skill if the dogs appear (they should, when it fits).
   - Add a visible "← Games" link back to `../`.

3. **It must work on phones and on desktop:**
   - **Input:** support touch (pointer events) and keyboard or mouse. Show on-screen controls on touch devices.
   - **Size:** the canvas or board fits the viewport in both portrait and landscape, and re-fits on resize and on orientation change. Nothing scrolls by accident: set `touch-action: none` on the play area.
   - **Pausing:** pause when the tab is hidden (`visibilitychange`), and leave the sound off until the first user interaction.
   - **Reduced motion:** respect `prefers-reduced-motion` for decorative effects.

4. **Make it embeddable, and add it to the Games page.** The Games page (`games/index.html`) plays games inside an iframe, with one tab per game.
   - Add `{ slug, title }` to the `GAMES` array in `games/index.html`. That creates the tab and the `#<slug>` link.
   - In the game, detect embedding (`window.self !== window.top`) and hide its standalone header ("← Games" link and title), keeping only essential controls such as Sound. See `games/shadys-snack-attack/` for the pattern.
   - The game must size itself to its own viewport (the iframe), not assume it has the whole window.
   - Check it both embedded (`/games/#<slug>`) and standalone (`/games/<slug>/`).

5. **Test it** by serving the site locally (`python3 -m http.server 8765`):
   - Play it at desktop size and at a phone size (Chrome DevTools device mode, with touch on).
   - Screenshot at 1440×900 and 600×1100 (commands in `AGENTS.md`) and look at both.
   - Check the console for errors.

6. **Commit and push** on Dan's go-ahead, since pushing deploys. Then confirm `https://dangroshan.dev/games/<slug>/` returns 200 and loads.
