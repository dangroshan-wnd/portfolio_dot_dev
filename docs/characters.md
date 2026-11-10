# Character sheet: Noodles and Shady

Dan's two dogs are the site's only characters. Real photos of them are on Instagram at @noodlegram_. The canonical drawings are the `noodles()`, `noodles_leaping()` and `shady()` functions in `tools/build_placeholders.py`. They are exported to `assets/characters/` as reference SVGs, and all of them face right with the origin at the centre of the body.

Always draw them in the paper-cutout style ([style-guide.md](style-guide.md)).

## Side by side

| | Noodles | Shady |
|---|---|---|
| Breed | Mini Goldendoodle | Mini Aussiedoodle |
| Sex | not recorded (ask Dan) | female |
| Size | the smaller dog | **markedly bigger: about double Noodles' weight** |
| Coat | apricot gold curls | black/charcoal with grey merle patches and white flecks; wavy, not tight curls |
| Face | round, fluffy teddy-bear face; curly topknot; dark nose; soft smile | white blaze up the face, grey muzzle, black nose, **pink tongue almost always out** |
| Ears | floppy, darker apricot | long, floppy, near-black |
| Build | compact and rounded | leaner and leggier, with a deep chest |
| Markings | lighter curls scattered on the body | white chest bib, white socks, white flecks on the coat and ears |
| Tail | fluffy curled pom | feathery plume |
| Personality | happy, friendly, **mature**: the calm, gracious one | **goofy, crazy, energetic**: chaos in a dog |
| Loves | **frisbee, swimming** | **soccer balls, tug-of-war** |

## Colors

| Part | Noodles | Shady |
|---|---|---|
| Main coat | `#e3a868` | `#3a3f4a` |
| Shade (far legs, ears) | `#c98a4c` | `#2a2e37` |
| Light (muzzle, curls) | `#f0c48e` | grey muzzle `#8d96a8`, white `#e8e6e1` |
| Nose | `#2e2420` | `#15171c` |
| Mouth and tongue | mouth `#5a2232` | mouth `#5a2232`, tongue `#f27d9c` |

## Proportions (in the drawing units of the canonical code)

- **Noodles:** body 100 wide × 60 tall, head radius 26, feet at y = +52.
- **Shady:** body 132 wide × 68 tall, head radius 30, legs about 64 long, feet at y = +70.
- **Draw them at the same scale factor.** Shady must always read as clearly the bigger dog. Don't shrink her to fit.
- To make a dog face left, mirror it with `scale(-1 1)`. Don't redraw it.

## Poses and behavior that fit

- **Noodles:** sitting politely, trotting, leaping for a frisbee, paddling with just the head and back above water, lying down calmly, a gentle tail wag.
- **Shady:** zoomies, play-bow, dribbling or chasing a soccer ball, yanking a rope, upside-down flops, tongue flapping, a fast tail wag.
- **Together:** tug-of-war (Shady pulling hardest), Noodles calmly watching Shady's chaos, the two of them face to face.
- **Animate them** with the shared classes. Noodles' tail wags at the default speed. Shady's is faster (`animation-duration: .3s`) and her tongue pants.

## Don'ts

- Don't make Noodles goofy or Shady dignified. Their personalities stay as described.
- Don't make Shady the same size as Noodles or smaller.
- Don't give either dog clothes or accessories, change their colors, or add human features.
- Don't bring back the goose or the pig.
