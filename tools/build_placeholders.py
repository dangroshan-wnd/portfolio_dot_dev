"""Generate the five "See you soon..." placeholder pages.

Each page is a style demo starring Noodles and Shady (see docs/characters.md once written).
Run from anywhere:  python3 tools/build_placeholders.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [  # (slug, nav label, accent var)
    ("", "Home", "--home"),
    ("work", "Work", "--work"),
    ("projects", "Projects", "--projects"),
    ("movies", "Movies", "--movies"),
    ("games", "Games", "--games"),
]


def page(slug, title, chip, label, scene, extra_css=""):
    up = "../" if slug else ""
    links = []
    for s, name, var in PAGES:
        href = f"{up}{s}/" if s else (up or "./")
        cur = ' aria-current="page"' if s == slug else ""
        links.append(f'      <a href="{href}" style="--c:var({var})"{cur}><span class="dot"></span>{name}</a>')
    nav = "\n".join(links)
    doc_title = "Dan Groshan" if not slug else f"{title} · Dan Groshan"
    style = f"\n  <style>{extra_css}\n  </style>" if extra_css else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="dark">
  <title>{doc_title}</title>
  <meta name="description" content="See you soon...">
  <link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@1,9..144,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{up}style.css">{style}
</head>
<body class="page-{slug or 'home'}">
  <aside class="sidebar">
    <a class="brand" href="{up or './'}">dangroshan.dev</a>
    <nav class="nav" aria-label="Pages">
{nav}
    </nav>
  </aside>

  <main>
    <div class="headline">
      <h1>See you soon...</h1>
      <span class="chip">{chip}</span>
    </div>
    <svg viewBox="0 0 1200 800" preserveAspectRatio="xMidYMax slice" role="img" aria-label="{label}">
{scene}
    </svg>
  </main>
  <script src="{up}site.js"></script>
</body>
</html>
"""


def stars(points, fill="#e8edf7"):
    return "\n".join(
        f'      <circle class="twinkle" cx="{x}" cy="{y}" r="{r}" fill="{fill}" style="animation-delay:-{(i * .37) % 2.4:.2f}s"/>'
        for i, (x, y, r) in enumerate(points))


STARS = [(90, 90, 1.6), (210, 160, 1.2), (330, 70, 2), (420, 210, 1.3), (520, 250, 1.4), (150, 300, 1.2),
         (700, 230, 1.8), (1010, 80, 1.8), (1090, 170, 1.3), (1150, 60, 1.5), (1060, 330, 1.2),
         (260, 360, 1.1), (470, 330, 1.3), (1140, 400, 1.2), (80, 420, 1.5), (820, 300, 1.4), (40, 200, 1.1)]

# --------------------------------------------------------------------------------------
# Character parts (flat). Both face RIGHT. Origin = body centre.
#   Noodles: Mini Goldendoodle, apricot curls, smaller; feet at y=+52.
#   Shady:   Mini Aussiedoodle, black/grey merle + white flecks, ~2x Noodles' weight,
#            long legs, floppy ears, tongue out; feet at y=+70.
# --------------------------------------------------------------------------------------
N = dict(coat="#e3a868", dark="#c98a4c", light="#f0c48e", nose="#2e2420")
S = dict(coat="#3a3f4a", dark="#2a2e37", merle="#8d96a8", white="#e8e6e1", nose="#15171c", tongue="#f27d9c")


def noodles_flat(tail_origin):
    c = N
    return f"""
        <g class="wag" style="transform-origin:{tail_origin}">
          <circle cx="-52" cy="-20" r="12" fill="{c['dark']}"/><circle cx="-60" cy="-33" r="10" fill="{c['dark']}"/><circle cx="-54" cy="-44" r="8" fill="{c['dark']}"/>
        </g>
        <g fill="{c['dark']}"><rect x="-40" y="8" width="16" height="44" rx="8"/><rect x="24" y="8" width="16" height="44" rx="8"/></g>
        <g fill="{c['coat']}"><rect x="-24" y="10" width="16" height="42" rx="8"/><rect x="38" y="10" width="16" height="42" rx="8"/></g>
        <ellipse cx="0" cy="0" rx="50" ry="30" fill="{c['coat']}"/>
        <g fill="{c['coat']}"><circle cx="-36" cy="-22" r="10"/><circle cx="-18" cy="-28" r="10"/><circle cx="0" cy="-29" r="10"/><circle cx="18" cy="-27" r="10"/><circle cx="-46" cy="-6" r="9"/></g>
        <g fill="{c['light']}" opacity=".7"><circle cx="-24" cy="-12" r="4"/><circle cx="-4" cy="-4" r="4"/><circle cx="14" cy="-14" r="4"/><circle cx="-12" cy="10" r="4"/><circle cx="8" cy="12" r="3.5"/></g>
        <circle cx="46" cy="-34" r="26" fill="{c['coat']}"/>
        <g fill="{c['coat']}"><circle cx="30" cy="-54" r="10"/><circle cx="46" cy="-60" r="11"/><circle cx="62" cy="-54" r="9"/></g>
        <ellipse cx="34" cy="-24" rx="11" ry="20" fill="{c['dark']}" transform="rotate(15 34 -24)"/>
        <ellipse cx="68" cy="-24" rx="15" ry="12" fill="{c['light']}"/>
        <ellipse cx="81" cy="-28" rx="6" ry="5" fill="{c['nose']}"/>
        <circle cx="54" cy="-40" r="3.6" fill="#1d1512"/><circle cx="55.2" cy="-41.2" r="1.1" fill="#fff"/>
        <path d="M64 -16 q7 6 14 0" fill="none" stroke="{c['nose']}" stroke-width="2" stroke-linecap="round"/>"""


def shady_flat(tail_origin):
    c = S
    return f"""
        <g class="wag" style="transform-origin:{tail_origin};animation-duration:.3s">
          <path d="M-64 -12 q-30 -10 -30 -42 q14 4 16 18 q4 -14 14 -16 q-6 20 6 34z" fill="{c['coat']}"/>
        </g>
        <g fill="{c['dark']}"><rect x="-52" y="6" width="18" height="64" rx="9"/><rect x="30" y="6" width="18" height="64" rx="9"/></g>
        <g fill="{c['coat']}"><rect x="-30" y="8" width="18" height="62" rx="9"/><rect x="50" y="8" width="18" height="62" rx="9"/></g>
        <g fill="{c['white']}"><rect x="-30" y="56" width="18" height="14" rx="7"/><rect x="50" y="56" width="18" height="14" rx="7"/></g>
        <ellipse cx="0" cy="0" rx="66" ry="34" fill="{c['coat']}"/>
        <g fill="{c['merle']}"><ellipse cx="-30" cy="-10" rx="16" ry="10"/><ellipse cx="8" cy="10" rx="12" ry="8"/><ellipse cx="26" cy="-18" rx="10" ry="7"/><ellipse cx="-48" cy="12" rx="8" ry="6"/></g>
        <g fill="{c['white']}"><circle cx="-14" cy="-20" r="2.2"/><circle cx="-38" cy="4" r="1.8"/><circle cx="14" cy="-4" r="2"/><circle cx="-2" cy="18" r="1.8"/><circle cx="36" cy="2" r="2"/></g>
        <ellipse cx="54" cy="10" rx="15" ry="20" fill="{c['white']}"/>
        <circle cx="70" cy="-40" r="30" fill="{c['coat']}"/>
        <ellipse cx="82" cy="-46" rx="6" ry="17" fill="{c['white']}" transform="rotate(20 82 -46)"/>
        <ellipse cx="98" cy="-28" rx="18" ry="13" fill="{c['merle']}"/>
        <ellipse cx="114" cy="-33" rx="7" ry="6" fill="{c['nose']}"/>
        <path d="M90 -18 q12 10 24 0z" fill="#5a2232"/>
        <path class="pant" d="M98 -15 q2 26 10 26 q8 0 6 -26z" fill="{c['tongue']}"/>
        <circle cx="80" cy="-50" r="4" fill="#0b0c10"/><circle cx="81.3" cy="-51.3" r="1.2" fill="#fff"/>
        <path d="M54 -62 q-20 10 -16 48 q12 6 18 -6 q2 -28 -2 -42z" fill="{c['dark']}"/>
        <g fill="{c['white']}"><circle cx="62" cy="-58" r="1.8"/><circle cx="74" cy="-22" r="1.6"/></g>"""


# ----------------------------------- 1. HOME: flat vector -----------------------------------
HOME = f"""
{stars(STARS)}
      <circle cx="960" cy="235" r="90" fill="#f3ead8" opacity=".07"/>
      <circle cx="960" cy="235" r="52" fill="#f3ead8"/>
      <circle cx="946" cy="222" r="8" fill="#e2d7bf"/><circle cx="974" cy="250" r="6" fill="#e2d7bf"/>
      <path d="M0 600 Q300 540 600 590 T1200 570 V800 H0Z" fill="#16294d"/>
      <path d="M0 690 Q400 660 800 690 T1200 680 V800 H0Z" fill="#1d3460"/>
      <g fill="#ffd36b">
        <circle class="twinkle" cx="330" cy="560" r="3" style="animation-duration:1.7s"/>
        <circle class="twinkle" cx="880" cy="600" r="3" style="animation-duration:2.1s;animation-delay:-.8s"/>
        <circle class="twinkle" cx="1010" cy="540" r="2.5" style="animation-duration:1.4s;animation-delay:-.3s"/>
        <circle class="twinkle" cx="240" cy="640" r="2.5" style="animation-duration:1.9s;animation-delay:-1.1s"/>
      </g>
      <ellipse cx="480" cy="694" rx="70" ry="8" fill="#0a1222" opacity=".5"/>
      <ellipse cx="720" cy="694" rx="92" ry="9" fill="#0a1222" opacity=".5"/>
      <g transform="translate(470 628) scale(1.2)">{noodles_flat("90% 90%")}
      </g>
      <g transform="translate(730 606) scale(-1.2 1.2)">{shady_flat("90% 90%")}
      </g>"""

# ----------------------------------- 2. WORK: ink line art -----------------------------------
INK = "#e9e2cf"
WORK = f"""
      <defs>
        <filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
          <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4"/>
          <feDisplacementMap in="SourceGraphic" scale="3.5"/>
        </filter>
      </defs>
      <g filter="url(#ink)" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
        <g stroke-width="1.6">
          <path d="M120 120 v10 M115 125 h10 M330 80 v12 M324 86 h12 M1060 120 v10 M1055 125 h10 M200 300 v8 M196 304 h8 M1120 300 v10 M1115 305 h10 M460 260 v8 M456 264 h8"/>
        </g>
        <circle cx="950" cy="250" r="56"/>
        <path d="M915 215 l18 -10 M908 235 l34 -20 M906 258 l48 -28 M912 278 l52 -30 M926 294 l42 -24" stroke-width="1.3" opacity=".7"/>
        <path d="M0 560 L140 500 L230 535 L360 470 L480 545" />
        <path d="M720 545 L840 490 L960 530 L1080 470 L1200 520"/>
        <path d="M0 600 H1200" stroke-width="1.6"/>
        <g stroke-width="1.5" opacity=".8">
          <path d="M60 640 q20 -6 40 0 t40 0 M220 700 q20 -6 40 0 t40 0 M880 660 q20 -6 40 0 t40 0 M1000 720 q20 -6 40 0 t40 0 M140 760 q20 -6 40 0 t40 0 M760 760 q20 -6 40 0 t40 0"/>
        </g>
        <g stroke-width="2">
          <path d="M150 600 q-4 -60 6 -110 M170 600 q6 -50 -2 -90 M1060 600 q-6 -70 4 -120 M1080 600 q4 -50 -4 -80"/>
        </g>
        <g fill="{INK}" stroke="none"><ellipse cx="157" cy="482" rx="5" ry="14"/><ellipse cx="1065" cy="472" rx="5" ry="14"/></g>

        <g class="ripple"><ellipse cx="600" cy="640" rx="120" ry="16"/></g>
        <g class="ripple" style="animation-delay:-1.5s"><ellipse cx="600" cy="640" rx="120" ry="16"/></g>

        <g transform="translate(790 650)">
          <ellipse cx="0" cy="0" rx="34" ry="9" fill="#0f1d3a"/>
          <ellipse cx="0" cy="-2" rx="22" ry="5"/>
        </g>

        <g class="paddle">
          <g transform="translate(520 640) scale(1.7)" fill="#0f1d3a">
            <path d="M-56 -4 q-6 -18 4 -24 q4 10 -4 24" />
            <path d="M-44 0 q10 -16 30 -14 q14 -2 22 6"/>
            <circle cx="46" cy="-34" r="26"/>
            <circle cx="30" cy="-54" r="10"/><circle cx="46" cy="-60" r="11"/><circle cx="62" cy="-54" r="9"/>
            <path d="M28 -40 q-6 4 -4 10 M36 -60 q4 -4 8 0 M52 -64 q4 -3 8 1" stroke-width="1.2"/>
            <ellipse cx="34" cy="-24" rx="11" ry="20" transform="rotate(15 34 -24)"/>
            <path d="M28 -34 q6 4 4 12 M30 -18 q4 2 6 8" stroke-width="1"/>
            <ellipse cx="68" cy="-24" rx="15" ry="12"/>
            <ellipse cx="81" cy="-28" rx="6" ry="5" fill="{INK}"/>
            <circle cx="54" cy="-40" r="3" fill="{INK}" stroke="none"/>
            <path d="M64 -16 q7 6 14 0"/>
            <path d="M-20 0 h110" stroke="#0f1d3a" stroke-width="6"/>
          </g>
          <path d="M440 642 q20 -7 40 0 t40 0 t40 0 t40 0 t40 0 t40 0" stroke-width="2"/>
          <path d="M470 660 q14 -5 28 0 M600 662 q14 -5 28 0" stroke-width="1.6" opacity=".7"/>
        </g>
      </g>"""

# ----------------------------------- 3. PROJECTS: paper cutout -----------------------------------
def leaping_noodles():
    c = N
    return f"""
          <g fill="{c['dark']}">
            <rect x="-40" y="0" width="16" height="44" rx="8" transform="rotate(62 -32 6)"/>
            <rect x="26" y="0" width="16" height="44" rx="8" transform="rotate(-70 34 6)"/>
          </g>
          <g fill="{c['coat']}">
            <rect x="-26" y="2" width="16" height="42" rx="8" transform="rotate(50 -18 6)"/>
            <rect x="38" y="2" width="16" height="42" rx="8" transform="rotate(-82 46 6)"/>
          </g>
          <g fill="{c['dark']}"><circle cx="-56" cy="-8" r="11"/><circle cx="-68" cy="-14" r="9"/><circle cx="-78" cy="-16" r="7"/></g>
          <ellipse cx="0" cy="0" rx="54" ry="26" fill="{c['coat']}"/>
          <g fill="{c['coat']}"><circle cx="-36" cy="-18" r="10"/><circle cx="-16" cy="-24" r="10"/><circle cx="4" cy="-25" r="10"/><circle cx="22" cy="-22" r="10"/></g>
          <circle cx="50" cy="-30" r="26" fill="{c['coat']}"/>
          <g fill="{c['coat']}"><circle cx="34" cy="-50" r="10"/><circle cx="50" cy="-56" r="11"/><circle cx="66" cy="-50" r="9"/></g>
          <path d="M30 -38 q-24 -4 -30 -26 q16 -2 28 12z" fill="{c['dark']}"/>
          <ellipse cx="72" cy="-20" rx="15" ry="12" fill="{c['light']}"/>
          <ellipse cx="85" cy="-25" rx="6" ry="5" fill="{c['nose']}"/>
          <circle cx="58" cy="-37" r="3.6" fill="#1d1512"/><circle cx="59.2" cy="-38.2" r="1.1" fill="#fff"/>
          <path d="M70 -10 q8 6 16 -2" fill="#5a2232"/>"""


PROJECTS = f"""
      <defs>
        <filter id="paper" x="-10%" y="-10%" width="120%" height="130%">
          <feDropShadow dx="0" dy="5" stdDeviation="4" flood-color="#030712" flood-opacity=".55"/>
        </filter>
        <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="2"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .06 0"/></filter>
      </defs>
{stars(STARS[::2], "#f3ead8")}
      <g filter="url(#paper)">
        <circle cx="950" cy="250" r="54" fill="#f3e6c4"/>
        <circle cx="972" cy="236" r="44" fill="#12294a"/>
      </g>
      <g filter="url(#paper)" fill="#2b4a75">
        <path d="M120 200 q10 -30 40 -26 q14 -24 44 -12 q30 -6 34 22 q20 4 18 22 h-150 q-6 -4 14 -6z"/>
      </g>
      <g filter="url(#paper)"><path d="M0 560 L120 500 L220 540 L350 470 L470 530 L600 480 L740 545 L860 490 L1000 530 L1200 470 V800 H0Z" fill="#1d3a63"/></g>
      <g filter="url(#paper)"><path d="M0 620 Q200 580 420 610 T860 600 T1200 590 V800 H0Z" fill="#26497a"/></g>
      <g filter="url(#paper)">
        <path d="M0 690 L30 676 L60 690 L90 674 L120 690 L150 676 L180 690 L210 674 L240 690 L270 676 L300 690 L330 674 L360 690 L390 676 L420 690 L450 674 L480 690 L510 676 L540 690 L570 674 L600 690 L630 676 L660 690 L690 674 L720 690 L750 676 L780 690 L810 674 L840 690 L870 676 L900 690 L930 674 L960 690 L990 676 L1020 690 L1050 674 L1080 690 L1110 676 L1140 690 L1170 674 L1200 690 V800 H0Z" fill="#2f5a8e"/>
      </g>
      <g filter="url(#paper)" fill="#3f6ea6">
        <path d="M180 690 v-60 l-16 20 M180 650 l18 -24" stroke="#3f6ea6" stroke-width="6" stroke-linecap="round"/>
        <path d="M1020 690 v-50 l-14 16 M1020 660 l14 -18" stroke="#3f6ea6" stroke-width="6" stroke-linecap="round"/>
      </g>
      <ellipse cx="600" cy="712" rx="80" ry="10" fill="#0b1729" opacity=".5"/>
      <g class="float">
        <g filter="url(#paper)" transform="translate(560 440) rotate(-12) scale(1.3)">{leaping_noodles()}
        </g>
        <g filter="url(#paper)" transform="translate(682 350) rotate(-14)">
          <g class="spin"><ellipse cx="0" cy="0" rx="32" ry="11" fill="#e85d4a"/><ellipse cx="0" cy="-2" rx="20" ry="5" fill="#c94a3a"/></g>
        </g>
        <path d="M730 330 q30 -10 60 4 M736 352 q26 0 50 12" fill="none" stroke="#f3e6c4" stroke-width="3" stroke-linecap="round" opacity=".6"/>
      </g>
      <rect width="1200" height="800" filter="url(#grain)" pointer-events="none"/>"""

# ----------------------------------- 4. MOVIES: muppet / puppet -----------------------------------
MOVIES = """
      <defs>
        <filter id="felt" x="-15%" y="-15%" width="130%" height="130%">
          <feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" seed="7" result="n"/>
          <feDisplacementMap in="SourceGraphic" in2="n" scale="7" xChannelSelector="R" yChannelSelector="G" result="d"/>
          <feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="1" seed="3" result="n2"/>
          <feColorMatrix in="n2" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.2 .9" result="speck"/>
          <feComposite in="speck" in2="d" operator="in" result="speckIn"/>
          <feMerge><feMergeNode in="d"/><feMergeNode in="speckIn"/></feMerge>
        </filter>
        <radialGradient id="spot" cx="50%" cy="55%" r="50%">
          <stop offset="0" stop-color="#3a4a8a" stop-opacity=".9"/><stop offset="1" stop-color="#0c1226" stop-opacity="0"/>
        </radialGradient>
        <linearGradient id="velvet" x1="0" x2="1">
          <stop offset="0" stop-color="#4a1424"/><stop offset=".25" stop-color="#7a2236"/><stop offset=".5" stop-color="#561a2a"/><stop offset=".75" stop-color="#7a2236"/><stop offset="1" stop-color="#4a1424"/>
        </linearGradient>
      </defs>
      <ellipse cx="620" cy="460" rx="520" ry="330" fill="url(#spot)"/>

      <g class="tug">
        <!-- Noodles puppet (left, facing right) -->
        <g filter="url(#felt)" transform="rotate(-4 460 520)">
          <path d="M370 640 q0 -90 90 -96 q90 6 90 96z" fill="#d99a58"/>
          <circle cx="460" cy="480" r="78" fill="#e3a868"/>
          <g fill="#e8b273"><circle cx="410" cy="418" r="24"/><circle cx="448" cy="402" r="26"/><circle cx="490" cy="408" r="24"/><circle cx="520" cy="432" r="18"/></g>
          <path d="M392 450 q-50 20 -34 96 q30 8 42 -24 q4 -40 -8 -72z" fill="#c98a4c"/>
          <path d="M470 520 q60 -24 92 4 q-10 52 -60 50 q-34 -4 -32 -54z" fill="#3a1020"/>
          <path d="M470 520 q60 -24 92 4 q-36 -4 -92 -4z" fill="#f0c48e"/>
          <ellipse cx="548" cy="498" rx="20" ry="16" fill="#2e2420"/>
        </g>
        <g class="jiggle"><circle cx="458" cy="456" r="20" fill="#fff" stroke="#1a1a1a" stroke-width="2"/><circle cx="466" cy="460" r="9" fill="#111"/></g>
        <g class="jiggle" style="animation-delay:-.25s"><circle cx="500" cy="452" r="17" fill="#fff" stroke="#1a1a1a" stroke-width="2"/><circle cx="507" cy="457" r="8" fill="#111"/></g>

        <!-- rope -->
        <path d="M530 548 Q640 572 750 540" fill="none" stroke="#d9c08a" stroke-width="14" stroke-linecap="round"/>
        <path d="M530 548 Q640 572 750 540" fill="none" stroke="#a88a52" stroke-width="14" stroke-dasharray="4 10"/>

        <!-- Shady puppet (right, facing left, bigger) -->
        <g filter="url(#felt)" transform="rotate(5 800 500)">
          <path d="M690 640 q0 -110 110 -116 q110 6 110 116z" fill="#353a45"/>
          <ellipse cx="868" cy="600" rx="34" ry="40" fill="#e8e6e1"/>
          <circle cx="810" cy="450" r="96" fill="#3a3f4a"/>
          <g fill="#8d96a8"><ellipse cx="850" cy="400" rx="26" ry="18"/><ellipse cx="770" cy="470" rx="16" ry="12"/><ellipse cx="880" cy="470" rx="14" ry="10"/></g>
          <g fill="#e8e6e1"><circle cx="820" cy="380" r="5"/><circle cx="868" cy="440" r="4"/><circle cx="790" cy="420" r="4"/><circle cx="845" cy="500" r="5"/><circle cx="760" cy="440" r="3.5"/></g>
          <path d="M792 360 q10 60 -10 110 q-14 -10 -10 -60 q4 -40 20 -50z" fill="#e8e6e1"/>
          <path d="M890 380 q66 20 50 120 q-36 12 -50 -24 q-6 -56 0 -96z" fill="#2a2e37"/>
          <path d="M790 504 q-72 -36 -112 4 q16 62 70 60 q40 -6 42 -64z" fill="#3a1020"/>
          <path d="M790 504 q-72 -36 -112 4 q42 -6 112 -4z" fill="#8d96a8"/>
          <path d="M720 540 q-6 56 18 60 q24 0 22 -54z" fill="#f27d9c"/>
          <ellipse cx="690" cy="482" rx="24" ry="19" fill="#15171c"/>
        </g>
        <g class="jiggle" style="animation-delay:-.1s"><circle cx="770" cy="420" r="22" fill="#fff" stroke="#1a1a1a" stroke-width="2"/><circle cx="761" cy="426" r="10" fill="#111"/></g>
        <g class="jiggle" style="animation-delay:-.35s"><circle cx="818" cy="414" r="25" fill="#fff" stroke="#1a1a1a" stroke-width="2"/><circle cx="806" cy="420" r="11" fill="#111"/></g>
      </g>

      <!-- puppet stage -->
      <rect x="0" y="620" width="1200" height="180" fill="#3b2418"/>
      <rect x="0" y="620" width="1200" height="14" fill="#5a3824"/>
      <rect x="0" y="634" width="1200" height="3" fill="#d4a84a"/>
      <path d="M0 0 H250 Q210 300 240 620 H0Z" fill="url(#velvet)"/>
      <path d="M1200 0 H950 Q990 300 960 620 H1200Z" fill="url(#velvet)"/>
      <path d="M0 0 H1200 V54 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0 q-50 34 -100 0Z" fill="#7a2236"/>
      <path d="M0 54 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0 q50 34 100 0" fill="none" stroke="#d4a84a" stroke-width="4"/>"""

# ----------------------------------- 5. GAMES: pixel art -----------------------------------
P = 8
PAL = {"k": S["coat"], "d": S["dark"], "g": S["merle"], "w": S["white"], "n": "#0b0c10",
       "p": S["tongue"], "e": "#0b0c10", "m": "#5a2232", "c": "#f3ead8", "b": "#111318",
       "G": "#2f6b4f", "H": "#3f8a62", "D": "#1e2f4a", "E": "#26395a"}

SHADY_PX = [
    "................dddd....",
    "...............kkkkkk...",
    "kk............kkkwkkkk..",
    ".kk..........dkkkwkkekk.",
    "..kk.........ddkkwkgggn.",
    "...kkkkkkkkkkddkkwgggggm",
    "...kkgkkkwkkkddkkkkkmpm.",
    "..kkggkkkkkkkkgkkkkk.p..",
    "..kkkkkwkkkgggkkwwww.p..",
    "..kkkkkkkkkkkkkkwwww....",
    "...kkkkkkkkkkkkkwww.....",
    "...kk.kk.......kk.kk....",
    "...kk.kk.......kk.kk....",
    "...kk.kk.......kk.kk....",
    "...ww.ww.......ww.ww....",
]
BALL_PX = [
    "..cccc..",
    ".cccccc.",
    "cccbbccc",
    "ccbbbbcc",
    "ccbbbbcc",
    "cccbbccc",
    ".bccccb.",
    "..bccb..",
]
MOON_PX = [
    "..cccc..",
    ".ccccc..",
    "cccc....",
    "ccc.....",
    "ccc.....",
    "cccc....",
    ".ccccc..",
    "..cccc..",
]


def sprite(rows, x0, y0, px=P):
    out = []
    for j, row in enumerate(rows):
        i = 0
        while i < len(row):
            ch = row[i]
            if ch == ".":
                i += 1
                continue
            k = i
            while k < len(row) and row[k] == ch:
                k += 1
            out.append(f'<rect x="{x0 + i * px}" y="{y0 + j * px}" width="{(k - i) * px}" height="{px}" fill="{PAL[ch]}"/>')
            i = k
    return "".join(out)


def ground():
    out = []
    for i in range(0, 1200 // P):
        x = i * P
        out.append(f'<rect x="{x}" y="688" width="{P}" height="{P}" fill="{PAL["H" if i % 3 else "G"]}"/>')
        out.append(f'<rect x="{x}" y="696" width="{P}" height="{P}" fill="{PAL["G"]}"/>')
    out.append(f'<rect x="0" y="704" width="1200" height="96" fill="{PAL["D"]}"/>')
    for i in range(0, 1200 // P, 5):
        for j in range(3):
            out.append(f'<rect x="{i * P + (j * 24) % 40}" y="{720 + j * 24}" width="{P}" height="{P}" fill="{PAL["E"]}"/>')
    return "".join(out)


def goal(x0=900, y0=560):
    out = [f'<g fill="#e8edf7">',
           f'<rect x="{x0}" y="{y0}" width="{P}" height="128"/>',
           f'<rect x="{x0}" y="{y0}" width="136" height="{P}"/>',
           f'<rect x="{x0 + 128}" y="{y0}" width="{P}" height="128"/></g>',
           f'<g fill="#97a6c4" opacity=".55">']
    for i in range(1, 8):
        out.append(f'<rect x="{x0 + i * 16}" y="{y0 + P}" width="2" height="120"/>')
    for j in range(1, 8):
        out.append(f'<rect x="{x0 + P}" y="{y0 + j * 16}" width="120" height="2"/>')
    out.append("</g>")
    return "".join(out)


pixel_stars = "\n".join(
    f'      <rect class="twinkle" x="{(x // P) * P}" y="{(y // P) * P}" width="{P if r > 1.4 else P // 2}" height="{P if r > 1.4 else P // 2}" fill="#e8edf7" style="animation-delay:-{(i * .41) % 2.4:.2f}s;animation-timing-function:steps(2)"/>'
    for i, (x, y, r) in enumerate(STARS))

GAMES = f"""
      <g shape-rendering="crispEdges">
{pixel_stars}
      {sprite(MOON_PX, 944, 200, 10)}
      {ground()}
      {goal()}
      <g class="hop">{sprite(SHADY_PX, 496, 568)}</g>
      <g class="bounce">{sprite(BALL_PX, 712, 632)}</g>
      </g>"""

# ----------------------------------- write -----------------------------------
SPECS = [
    ("", "Home", "Style demo 1/5 · Flat vector", "Noodles and Shady together under the moon", HOME),
    ("work", "Work", "Style demo 2/5 · Ink line art", "Noodles swimming toward a floating frisbee, drawn in ink lines", WORK),
    ("projects", "Projects", "Style demo 3/5 · Paper cutout", "Noodles leaping to catch a frisbee, as a paper cutout", PROJECTS),
    ("movies", "Movies", "Style demo 4/5 · Puppet", "Noodles and Shady as felt puppets playing tug-of-war on a puppet stage", MOVIES),
    ("games", "Games", "Style demo 5/5 · Pixel art", "Pixel-art Shady with a bouncing soccer ball and a goal", GAMES),
]

for slug, title, chip, label, scene in SPECS:
    path = os.path.join(ROOT, slug, "index.html") if slug else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(page(slug, title, chip, label, scene))
    print("wrote", os.path.relpath(path, ROOT))
