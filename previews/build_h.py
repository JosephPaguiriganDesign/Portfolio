#!/usr/bin/env python3
"""Option H, Specimen. Does not rewrite A–G."""
from pathlib import Path
import build as src

ROOT = Path(__file__).resolve().parent
FONT = (
    "https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400..900,0..100"
    "&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,500"
    "&family=Barlow+Condensed:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;600;700"
    "&family=Share+Tech+Mono"
    "&family=Big+Shoulders+Stencil+Display:wght@700;800"
    "&family=IBM+Plex+Mono:wght@400;500"
    "&display=swap"
)
GLYPHS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + list("abcdefghijklmnop") + list("0123456789") + ["&", "?", "—"]
FALL = [
    (96, "Comps are a lie"),
    (72, "Design that ships"),
    (48, "I hand off products, not comps."),
    (36, "Sharp instincts. Shipped."),
    (24, "From Brief to Ship."),
    (12, "Senior Product Designer in Los Angeles."),
]
FACES = [
    ("sce", "case-sce.html", "SCE.com Rebuilt.", "01", "Barlow Condensed"),
    ("hire", "case-screening.html", "Screening Manager Reimagined.", "02", "Source Sans 3"),
    ("force", "case-relaystrat.html", "Space Force Ops Tools.", "03", "Big Shoulders Stencil"),
    ("halo", "case-halo.html", "Halo: Reach (2010) Menu UI (Schematic, for Bungie).", "04", "Share Tech Mono"),
]


def e(text):
    return src.e(text)


def typo(text):
    out = []
    opened = True
    for ch in text:
        if ch == "'":
            out.append("\u2019")
        elif ch == '"':
            out.append("\u201c" if opened else "\u201d")
            opened = not opened
        else:
            out.append(ch)
    return "".join(out)


GRAIN = """
<svg class="grain" aria-hidden="true"><filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#paper)"/></svg>
"""


def head(title, spread="cover"):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(src.DESC)}">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONT}" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body data-spread="{spread}">
<a class="skip" href="#work">Skip to work</a>
{GRAIN}
"""


def mast(home=True):
    links = []
    for href, label in src.NAV:
        target = href if home else "index.html" + href
        links.append(f'<a href="{target}">{e(label)}</a>')
    links.append('<a href="tel:3103087383">310.308.7383</a>')
    brand = "#top" if home else "index.html"
    return f"""<header class="mast">
  <a class="sc" href="{brand}">No. 00 · Joseph Paguirigan</a>
  <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav id="site-nav" data-nav aria-label="Primary">{''.join(links)}</nav>
</header>
"""


def colophon():
    bits = []
    for key in "abcdefg":
        bits.append(f'<a href="../{key}/">{key.upper()}</a>')
    bits.append('<a class="now" href="../h/">H</a>')
    return f"""
<footer class="colo" id="colophon">
  <h2>Colophon</h2>
  <p>Cover face. Fraunces, a variable optical-size serif. The word PAGUIRIGAN is the specimen. Scroll shifts its optical size, weight, and soft axis. Hovering the index sets that word in the case’s own cut.</p>
  <p>Spreads. No. 01 SCE.com, Barlow Condensed, a civic grotesk. No. 02 Screening Manager, Source Sans 3, a calm humanist. No. 03 Space Force, Big Shoulders Stencil with IBM Plex Mono. No. 04 Halo: Reach, Share Tech Mono.</p>
  <p>Text. Newsreader, with old-style figures, for the reading matter on the cover. Hairline rules, a leader-dot index, and an SVG noise grain. No photographs used as texture.</p>
  <p>Build. Static HTML and CSS. Joseph Paguirigan · Senior Product Designer · 2026</p>
</footer>
<nav class="foot" aria-label="Art direction previews">{''.join(bits)}</nav>
"""


def close():
    return colophon() + '<script src="../shared.js"></script><script src="specimen.js"></script></body></html>'


def index_block():
    rows = []
    for key, href, title, num, face in FACES:
        rows.append(
            f'<li><a data-face="{key}" href="{e(href)}">'
            f'<span class="no">No. {num}</span>'
            f'<span class="ttl">{e(title)}</span>'
            f'<span class="lead" aria-hidden="true"></span>'
            f'<span class="pg">{num}</span>'
            f'</a></li>'
        )
    return f'<ol class="index" id="work">{"".join(rows)}</ol>'


def waterfall():
    items = []
    for size, line in FALL:
        items.append(
            f'<li><span class="pt">{size}</span>'
            f'<span class="ln cut" style="font-size:{size}px">{e(line)}</span></li>'
        )
    return f'<ol class="fall" aria-label="Size waterfall">{"".join(items)}</ol>'


def glyphs():
    cells = "".join(f"<span>{e(g)}</span>" for g in GLYPHS)
    return f'<div class="glyphs cut" aria-hidden="true">{cells}</div>'


def home():
    about = "".join(f"<p>{e(typo(t))}</p>" for t in src.ABOUT)
    stats = "".join(f'<div><b class="lining">{e(n)}</b><span>{e(l)}</span></div>' for n, l in src.STATS)
    stack = "".join(
        "<div><h3>{}</h3><ul>{}</ul></div>".format(e(cat), "".join(f"<li>{e(t)}</li>" for t in tools))
        for cat, tools in src.STACK
    )
    steps = "".join(
        f'<article><p class="sc">{n}</p><h3>{e(name)}</h3><p>{e(typo(desc))}</p>'
        + ('<p class="sc">AI-Augmented</p>' if ai else "")
        + "</article>"
        for n, name, desc, ai in src.STEPS
    )
    dossiers = []
    for p in src.PROJECTS:
        paras = "".join(f"<p>{e(typo(t))}</p>" for t in p["paragraphs"])
        out = p["outcome"] or "Shipped"
        dossiers.append(
            f'<article class="dossier"><p class="no lining">{p["num"]}</p><div>'
            f'<h3>{e(p["title"])}</h3><p class="sc">{e(" · ".join(p["tags"]))} · {e(p["role"])} · {e(p["year"])} · {e(out)}</p>'
            f'{paras}{src.actions(p["ctas"])}{src.kpi(p)}'
            f'<img src="{e(p["img"])}" alt="{e(p["alt"])}"></div></article>'
        )
    n_chars = len("PAGUIRIGAN")
    body = f"""{mast(True)}
<main id="top">
  <div class="hero">
    <p class="specimen cut" id="specimen">
      <span class="ink" aria-hidden="true">PAGUIRIGAN</span>
      <span class="face">PAGUIRIGAN</span>
    </p>
  </div>
  <div class="meta-line">
    <p class="showing sc">Cut <span id="cut">Fraunces</span> · {n_chars} characters · display</p>
    <p class="sc">fi fl ff · ligatures</p>
  </div>
  {glyphs()}
  <div class="liga cut" aria-label="Ligatures">
    <b>fi</b><b>fl</b><b>ff</b>
    <span class="sc">ligatures in this cut</span>
  </div>
  <div class="stage">
    {waterfall()}
    {index_block()}
  </div>
  <p class="dek">{e(typo(src.HERO))}</p>
  <div class="wrap">
    {''.join(dossiers)}
    <p class="sc">{e(" · ".join(src.BAND))}</p>
    <section id="about"><h2 class="slug">Sharp instincts. Shipped.</h2><div class="prose">{about}</div><div class="stats">{stats}</div></section>
    <section id="stack"><h2 class="slug">The Stack.</h2><div class="stack">{stack}</div></section>
    <section id="portfolio"><h2 class="slug">Selects.</h2><div class="gallery">{src.gallery_buttons()}</div></section>
    <section id="process"><h2 class="slug">From Brief to Ship.</h2><div class="steps">{steps}</div></section>
    <section class="contact" id="contact">
      <h2 class="slug">Open to New Projects</h2>
      <p class="big">Let’s Go.</p>
      <p><a class="mail" href="mailto:josephpaguirigan@gmail.com">josephpaguirigan@gmail.com</a></p>
      <p class="actions"><a href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Download Résumé <span class="sr">(opens in a new tab)</span></a></p>
      <p class="sc">I get shit done</p>
    </section>
  </div>
</main>
{src.lightbox()}
"""
    return head("Joseph Paguirigan, Senior Product Designer") + body + close()


SPREADS = {
    "case-sce.html": ("sce", "No. 01", "Powering the new sce.com", "Barlow Condensed", src.SCE_BLOCKS, "../../case-sce.html", "../../case-sce-assets/T01-home-desktop.jpg", "SCE Home, Desktop", "A modular page-template system for Southern California Edison, 15 million people, one coherent web experience. Designed to scale from outage alerts to clean-energy storytelling.", [("Role", "Lead"), ("Outcome", "9 Templates"), ("Tools", "Figma · Claude · Design Tokens")]),
    "case-screening.html": ("hire", "No. 02", "Screening, at the speed of hiring.", "Source Sans 3", src.SCREEN_BLOCKS, "../../case-screening.html", "../../case-screening-assets/hireright-preview.jpg", "HireRight Screening Manager preview", "Reimagining HireRight Screening Manager, a global background-check platform used by 40,000+ organizations, into a real-time command center for HR teams.", [("Role", "Lead Product Designer"), ("Outcome", "27 → 6"), ("Tools", "Figma · Sketch · Prototyping")]),
    "case-relaystrat.html": ("force", "No. 03", "Real tools for real missions.", "Big Shoulders Stencil", src.RELAY_BLOCKS, "../../case-relaystrat.html", "../../portfolio-relay-strat.jpg", "Relay Strat shipped product", "Software for the Space Tasking Cycle, designed in partnership with U.S. Space Force operators and strategists. User research and usability testing weren’t optional, they were the job. No stock photo UI here.", [("Role", "Product Designer"), ("Outcome", "In Use"), ("Year", "2022")]),
    "case-halo.html": ("halo", "No. 04", "Halo: Reach (2010) Menu UI (Schematic, for Bungie).", "Share Tech Mono", src.HALO_BLOCKS, "../../case-halo.html", "../../portfolio-halo-reach.jpg", "Halo: Reach game UI", "Menu systems and game UI for Halo: Reach. Console-first, controller-driven, and seen by millions of players every time they booted up.", [("Role", "Designer, Schematic"), ("Outcome", "Shipped"), ("Year", "2010")]),
}


def case_page(slug):
    spread, num, title, face, blocks, original, img, alt, lede, meta = SPREADS[slug]
    meta_html = "".join(f"<div><dt class=\"sc\">{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in meta)
    count = len(title)
    body = f"""{mast(False)}
<main>
  <article class="spread" id="work">
    <p class="margin-note">{e(num)} · {e(face)} · {count} characters</p>
    <h1 class="voice"><span class="ink" aria-hidden="true">{e(title)}</span>{e(title)}</h1>
    <p class="lede voice">{e(typo(lede))}</p>
    <p><a class="back" href="index.html#work">Back to Portfolio</a><a class="back" href="{e(original)}">View Project</a></p>
    <figure class="plate"><img src="{e(img)}" alt="{e(alt)}"><figcaption>{e(alt)}</figcaption></figure>
    <dl class="meta" style="display:flex;flex-wrap:wrap;gap:8px 20px">{meta_html}</dl>
  </article>
  {src.blocks_html(blocks)}
  {src.case_jumps(slug)}
</main>
"""
    return head(title + " — Joseph Paguirigan", spread) + body + close()


def main():
    folder = ROOT / "h"
    folder.mkdir(parents=True, exist_ok=True)
    html = home()
    (folder / "index.html").write_text(html, encoding="utf-8")
    for slug in SPREADS:
        (folder / slug).write_text(case_page(slug), encoding="utf-8")
    print("h", len(html))


if __name__ == "__main__":
    main()
