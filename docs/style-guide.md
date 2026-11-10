# dangroshan.dev style guide

These decisions were settled with Dan on 2026-11-09. Change them only when Dan asks.

## Who it's for and how it should feel

- **Audience:** Dan first, then future employers and recruiters.
- **Feel:** whimsical and illustrated everywhere, a cozy night-time storybook. It should be fun to click around, and still easy to read when someone wants the facts.
- **Words are Dan's.** Agents lay out and illustrate. They never write copy (see `AGENTS.md`).

## Color: dark only, cool dark blues

There is no light mode and no theme toggle. Every value lives as a token in `style.css`; use the token, not the hex.

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#0d1526` | page background |
| `--panel` | `#0f1a2e` | sidebar, raised panels |
| `--raised` | `#17243f` | hover and selected states |
| `--line` | `#22324f` | borders, dividers |
| `--text` | `#e8edf7` | body text |
| `--muted` | `#97a6c4` | secondary text, inactive nav |
| `--cream` | `#f3ead8` | headings, highlights |
| `--noodles` | `#e3a868` | Noodles' apricot: primary warm accent |
| `--shady` | `#8d96a8` | Shady's merle grey: secondary accent |
| `--tongue` | `#f27d9c` | Shady's tongue pink: small pops only |

Each section also has its own accent, used for its nav dot, its selected-nav bar, and highlights on that page:

| Section | Token | Hex |
|---|---|---|
| Home | `--home` | `#e3a868` |
| Work | `--work` | `#6d8cff` |
| Projects | `--projects` | `#5fc28a` |
| Movies | `--movies` | `#b084e8` |
| Games | `--games` | `#f2789c` |

Keep text contrast at WCAG AA or better. `--text` and `--cream` on `--bg` both pass. `--muted` is for secondary text only.

## Type

- **Headings:** Fraunces italic 600 (Google Fonts, already linked on every page).
- **Body and long reading** (project write-ups, Work): a readable serif, either Fraunces regular or Source Serif. Pick one the first time a long-text page is built, then record it here.
- **UI** (nav, buttons, labels, chips): the system sans-serif stack, `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

## Illustration style: paper cutout

Every illustration on the site, from full scenes to small cameos, is drawn as layered cut paper. The canonical code is `tools/build_placeholders.py`. Reuse its helpers (`cut`, `zigzag`, `waves`, `moon`, `cloud`, `noodles`, `shady`, `frisbee`, `soccer_ball`) instead of redrawing.

**Do:**
- Use flat, solid fills. Every shape is a single color.
- Make each object its own paper layer: wrap it in the `#paper` drop-shadow filter (`dy 5`, blur `4`, `#030712` at 55%), or use `cut()` in the script.
- Stack scenery back to front in the layer blues `#1d3a63`, `#26497a`, `#2f5a8e`, `#3f6ea6`, lighter toward the viewer.
- Give edges a cut-paper feel: zigzags, soft waves, rounded hills, simple clouds.
- Use paper cream `#f3e6c4` for the moon, chalk lines and small highlights.
- Let color come from the dogs and their props: the red frisbee `#e85d4a`, the white and black soccer ball, the gold rope.
- Set scenes at night: stars, a crescent moon, fireflies.
- Lay a light paper grain over the scene panel. `main::after` in `style.css` already does this.

**Don't:**
- Outline shapes. The only strokes allowed are thin cream "chalk" lines and motion lines.
- Use gradients inside shapes, glossy highlights, realistic shading, or photos.
- Use other illustration styles (pixel, ink, puppet, 3D) on the site's pages. Those were tried in the demo and rejected. Games are the exception (see below).
- Draw off-model dogs. See `docs/characters.md`.

**Scenes are 1200×800 SVGs** with `preserveAspectRatio="xMidYMax slice"`, fitted by `site.js`.
- Keep the top 200 units clear for the headline.
- Keep the important action between x = 290 and 990, because on portrait screens only that part shows.
- Give every scene SVG `role="img"` and an `aria-label` that describes it. Give purely decorative cameos `aria-hidden="true"` instead.

## Games: their own art style

Each game under `games/` may use whatever art style suits it (for example, *Shady's Snack Attack* is SNES-style pixel art). The dogs must still be recognizable in any style:
- **Shady:** black and grey merle with white flecks, white blaze, bib and socks, pink tongue out, and clearly bigger than Noodles.
- **Noodles:** apricot curls and a round face.

If Dan appears in a game, he's a plain, inconspicuous figure: a grey sweatsuit and a navy beanie. Game pages still use the site's dark-blue page chrome (`style.css` tokens) around the game.

## Motion

- Use gentle, ambient loops only: wagging tails, panting tongues, twinkling stars, a bobbing float, drifting tides, a spinning frisbee or ball.
- Nothing is interactive. Cameos don't react to hover, taps or scrolling.
- Use the shared classes in `style.css`: `twinkle`, `wag`, `pant`, `float`, `paddle`, `tide`, `spin`, `tug`, `bounce`. Add a new one there rather than inline.
- Respect reduced motion: when a visitor has turned animations off in their system settings, everything holds still. A rule in `style.css` already does this for anything inside `main svg`.

## Placeholder pages vs. real pages

- **Placeholder pages** (current): one full-panel paper scene plus "See you soon...".
- **Real pages:** no full-screen scenes. Content comes first, with **one or two small animated cameos of Noodles and/or Shady per page**. Cameos:
  - sit in margins, corners or between sections, and are roughly 80–200px tall
  - never cover text or controls, and never shift the layout
  - are in character, using the poses and hobbies in `docs/characters.md`
- **Downloads:** Work and project write-ups may link to a plain printable version (a PDF CV or write-up). The site itself stays playful.

## Layout and navigation

- **Sidebar** on the left, 210px wide, in the order Home, Work, Projects, Movies, Games. The current page gets `aria-current="page"`, `--raised` and an inset bar in its section color.
- **On phones** (700px wide or less) the sidebar becomes a horizontal top bar.
- **Every page must work on phones and desktop.**
- **Real-page layout is undecided.** Ask Dan before choosing a structure for Work, Projects, Movies or Games.
