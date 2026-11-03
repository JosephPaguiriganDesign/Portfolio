#!/usr/bin/env python3
"""Option G. Does not rewrite A–F."""
from pathlib import Path
import build as src

ROOT = Path(__file__).resolve().parent

FONT = (
    "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800"
    "&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600"
    "&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,500"
    "&display=swap"
)

# margin-right in em, per letter, for Big Shoulders Display 800
KERN = {
    "DE": [-0.055, 0],
    "SIGN": [0.028, -0.072, -0.018, 0],
    "ER": [-0.04, 0],
    "JOSEPH": [-0.02, -0.048, 0.022, -0.03, 0.01, 0.16],
    "PAGUIRIGAN": [0.012, -0.03, -0.018, -0.04, -0.062, 0.012, -0.05, -0.02, -0.028, 0],
}


def e(text):
    return src.e(text)


def typo(text):
    """Curly apostrophes and quotes. Words stay the same."""
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


def letters(word, prefix):
    margins = KERN.get(word, [0] * len(word))
    bits = []
    for i, ch in enumerate(word):
        mr = margins[i] if i < len(margins) else 0
        bits.append(f'<span class="ch {prefix}{i}" style="margin-right:{mr:.3f}em">{e(ch)}</span>')
    return "".join(bits)


def chunk(word, cls):
    ink = letters(word, cls[:1] if False else "")
    # class names de0, sign0, er0 come from the word
    key = word.lower() if word != "SIGN" else "sign"
    if word == "DE":
        key = "de"
    elif word == "ER":
        key = "er"
    margins = KERN[word]
    spans = []
    ghost = []
    for i, ch in enumerate(word):
        mr = margins[i]
        spans.append(f'<span class="ch {key}{i}" style="margin-right:{mr:.3f}em">{e(ch)}</span>')
        ghost.append(f'<span class="ch" style="margin-right:{mr:.3f}em">{e(ch)}</span>')
    mis = ""
    if word in ("SIGN", "ER"):
        mis = f'<span class="mis" aria-hidden="true">{"".join(ghost)}</span>'
    return f'<span class="chunk {key}">{mis}{"".join(spans)}</span>'


GRAIN = """
<svg class="grain" aria-hidden="true">
  <filter id="paper">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="4" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <rect width="100%" height="100%" filter="url(#paper)"/>
</svg>
"""

MARKS = """
<i class="crop tl" aria-hidden="true"></i>
<i class="crop tr" aria-hidden="true"></i>
<i class="crop bl" aria-hidden="true"></i>
<i class="crop br" aria-hidden="true"></i>
<div class="pass" aria-hidden="true"></div>
"""

BARS = """
<div class="bars" aria-hidden="true">
  <span class="sc">Color</span>
  <b class="sc">C</b><i style="background:#0096d6"></i>
  <b class="sc">M</b><i style="background:#d1006f"></i>
  <b class="sc">Y</b><i style="background:#f0d000"></i>
  <b class="sc">K</b><i style="background:#16130e"></i>
</div>
"""


def head(title):
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
<body>
<a class="skip" href="#work">Skip to work</a>
{GRAIN}
{MARKS}
<div class="sheet">
{BARS}
"""


def edge(home=True):
    links = []
    for href, label in src.NAV:
        target = href if home else f"index.html{href}"
        links.append(f'<a href="{target}">{e(label)}</a>')
    links.append('<a href="tel:3103087383">310.308.7383</a>')
    brand = "#top" if home else "index.html"
    work = "#work" if home else "index.html#work"
    return f"""<header class="edge">
  <a class="who" href="{brand}">Joseph Paguirigan</a>
  <a class="jump" href="{work}">Case Studies</a>
  <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav id="site-nav" data-nav aria-label="Primary">{''.join(links)}</nav>
</header>
"""


def colophon():
    bits = []
    for key, label in [
        ("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("e", "E"), ("f", "F"), ("g", "G"),
    ]:
        cls = ' class="now"' if key == "g" else ""
        bits.append(f'<a href="../{key}/"{cls}>{label}</a>')
    return f"""
<footer class="colo" id="colophon">
  <h2>Colophon</h2>
  <p>Type. Big Shoulders Display, optically kerned, for the broken word. Newsreader for the text, with old-style figures in prose and lining figures in the index. Small caps for the labels. Fraunces italic for the proof notes.</p>
  <p>Grid. A 24px baseline runs under the page. Twelve columns. The collision field steps off that grid on purpose, then the case list locks back onto it.</p>
  <p>Ink. Black on proof paper. One accent, a press red, for the overprint, the strikes, and the notes. Cyan, magenta, yellow, and black appear only in the color bar.</p>
  <p>Build. Static HTML and CSS. No framework. The grain is an SVG noise filter, not a photograph.</p>
  <p>Joseph Paguirigan · Senior Product Designer · 2026</p>
</footer>
<nav class="foot" aria-label="Art direction previews">{''.join(bits)}</nav>
"""


def close():
    return f"""
</div>
{colophon()}
<script src="../shared.js"></script>
<script src="../radical.js"></script>
</body>
</html>
"""


def name_html():
    return (
        f'<h1 class="name">{letters("JOSEPH", "n")}{letters("PAGUIRIGAN", "n")}</h1>'
    )
    # letters() uses prefix n0.. which collides between the two words.
    # Fix below by not using this helper as-is.


def kerned_name():
    """JOSEPH then a word space then PAGUIRIGAN, classes n0–n15."""
    bits = []
    i = 0
    for word in ("JOSEPH", "PAGUIRIGAN"):
        margins = KERN[word]
        if word == "PAGUIRIGAN":
            bits.append(" ")
        for j, ch in enumerate(word):
            bits.append(f'<span class="ch n{i}" style="margin-right:{margins[j]:.3f}em">{e(ch)}</span>')
            i += 1
    return f'<h1 class="name">{"".join(bits)}</h1>'


def cases():
    rows = []
    for n, p in enumerate(src.PROJECTS, start=1):
        out = p["outcome"] or "Shipped"
        year = p["year"]
        fn = f'{p["role"]} · {year} · {out}'
        rows.append(
            f'<li><a class="row" href="{e(p["slug"])}">'
            f'<span class="num lining">{p["num"]}</span>'
            f'<span class="ttl">{e(p["title"])}<sup class="fn-n">{n}</sup></span>'
            f'<span class="out">{e(out)}</span>'
            f'<span class="fn">{e(fn)}</span>'
            f'</a></li>'
        )
    return f'<ol class="cases" id="work">{"".join(rows)}</ol>'


def dossiers():
    parts = []
    for p in src.PROJECTS:
        paras = "\n".join(f"<p>{e(typo(t))}</p>" for t in p["paragraphs"])
        parts.append(
            f'<article class="dossier"><div class="num lining">{p["num"]}</div><div>'
            f'<h3>{e(p["title"])}</h3><p class="sc">{e(" · ".join(p["tags"]))}</p>'
            f'{paras}{src.actions(p["ctas"])}{src.kpi(p)}'
            f'<img src="{e(p["img"])}" alt="{e(p["alt"])}"></div></article>'
        )
    return "\n".join(parts)


def home():
    stats = "\n".join(f'<div><b class="lining">{e(n)}</b><span>{e(l)}</span></div>' for n, l in src.STATS)
    stack = "\n".join(
        "<div><h3>{}</h3><ul>{}</ul></div>".format(
            e(cat), "".join(f"<li>{e(t)}</li>" for t in tools)
        )
        for cat, tools in src.STACK
    )
    steps = "\n".join(
        f'<article><div class="n">{n}</div><h3>{e(name)}</h3><p>{e(typo(desc))}</p>'
        + ('<span class="ai">AI-Augmented</span>' if ai else "")
        + "</article>"
        for n, name, desc, ai in src.STEPS
    )
    about = "".join(f"<p>{e(typo(t))}</p>" for t in src.ABOUT)
    band = " · ".join(src.BAND)
    body = f"""{edge(True)}
<main id="top">
  <div class="field">
    <p class="lockup" aria-hidden="true">{chunk("DE","de")}{chunk("SIGN","sign")}{chunk("ER","er")}</p>
  </div>
  {kerned_name()}
  <h2 class="sr">Selected Work.</h2>
  {cases()}
  <div class="dek-row">
    <p class="margin" aria-hidden="true"><s>comps</s><br>products</p>
    <p class="dek">{e(typo(src.HERO))}</p>
  </div>
  <div class="wrap">
    {dossiers()}
    <p class="sc">{e(band)}</p>
    <section id="about"><h2 class="slug">Sharp instincts. <em>Shipped.</em></h2><div class="prose">{about}</div><div class="stats">{stats}</div></section>
    <section id="stack"><h2 class="slug">The Stack.</h2><div class="stack">{stack}</div></section>
    <section id="portfolio"><h2 class="slug">Selects.</h2><div class="gallery">{src.gallery_buttons()}</div></section>
    <section id="process"><h2 class="slug">From Brief to Ship.</h2><div class="steps">{steps}</div></section>
    <section id="contact" class="contact">
      <h2 class="slug">Open to New Projects</h2>
      <p class="big">Let&rsquo;s Go.</p>
      <p><a class="mail" href="mailto:josephpaguirigan@gmail.com">josephpaguirigan@gmail.com</a></p>
      <p class="actions"><a href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Download Résumé <span class="sr">(opens in a new tab)</span></a></p>
      <p class="stamp">I get shit done</p>
    </section>
  </div>
</main>
{src.lightbox()}
"""
    return head("Joseph Paguirigan, Senior Product Designer") + body + close()


CASES = {
    "case-sce.html": dict(
        kill="Patchwork.",
        lines=[("Powering", False), ("the new", False), ("sce.com", True)],
        lede="A modular page-template system for Southern California Edison, 15 million people, one coherent web experience. Designed to scale from outage alerts to clean-energy storytelling.",
        note="stet — one system",
        meta=[("Role", "Lead"), ("Outcome", "9 Templates"), ("Tools", "Figma · Claude · Design Tokens"), ("Status", "In production")],
        img="../../case-sce-assets/T01-home-desktop.jpg",
        alt="SCE Home, Desktop",
        blocks=src.SCE_BLOCKS,
        original="../../case-sce.html",
        kicker="Case Study / 01",
        title="Powering the new sce.com",
    ),
    "case-screening.html": dict(
        kill="Maze.",
        lines=[("Screening,", False), ("at the speed", False), ("of hiring.", True)],
        lede="Reimagining HireRight Screening Manager, a global background-check platform used by 40,000+ organizations, into a real-time command center for HR teams.",
        note="six states, not twenty-seven",
        meta=[("Role", "Lead Product Designer"), ("Outcome", "27 → 6"), ("Tools", "Figma · Sketch · Prototyping"), ("Status", "Production")],
        img="../../case-screening-assets/hireright-preview.jpg",
        alt="HireRight Screening Manager preview",
        blocks=src.SCREEN_BLOCKS,
        original="../../case-screening.html",
        kicker="Case Study / 02",
        title="Screening, at the speed of hiring.",
    ),
    "case-relaystrat.html": dict(
        kill="Stock-photo.",
        lines=[("Real tools", False), ("for real", False), ("missions.", True)],
        lede="Software for the Space Tasking Cycle, designed in partnership with U.S. Space Force operators and strategists. User research and usability testing weren’t optional, they were the job. No stock photo UI here.",
        note="still in use, 2022",
        meta=[("Role", "Product Designer"), ("Outcome", "In Use"), ("Tools", "Figma · Sketch · User Research"), ("Year", "2022")],
        img="../../portfolio-relay-strat.jpg",
        alt="Relay Strat shipped product",
        blocks=src.RELAY_BLOCKS,
        original="../../case-relaystrat.html",
        kicker="Case Study / 03",
        title="Real tools for real missions.",
    ),
    "case-halo.html": dict(
        kill="Clumsy.",
        lines=[("Halo: Reach", False), ("Menu UI", False), ("Bungie", True)],
        lede="Menu systems and game UI for Halo: Reach. Console-first, controller-driven, and seen by millions of players every time they booted up.",
        note="shipped, 2010",
        meta=[("Role", "Designer, Schematic"), ("Outcome", "Shipped"), ("Tools", "Photoshop · Illustrator · After Effects"), ("Year", "2010")],
        img="../../portfolio-halo-reach.jpg",
        alt="Halo: Reach game UI",
        blocks=src.HALO_BLOCKS,
        original="../../case-halo.html",
        kicker="Case Study / 04",
        title="Halo: Reach (2010) Menu UI (Schematic, for Bungie).",
    ),
}


def case_page(slug):
    c = CASES[slug]
    lines = []
    for i, (line, hot) in enumerate(c["lines"]):
        cls = " hot" if hot else ""
        # light optical tighten on the accent line
        inner = letters(line.replace(" ", ""), "x") if False else e(line)
        lines.append(f'<span class="{cls.strip()}">{inner}</span>' if cls else f"<span>{inner}</span>")
    # fix hot class
    lines = []
    for line, hot in c["lines"]:
        cls = ' class="hot"' if hot else ""
        lines.append(f"<span{cls}>{e(line)}</span>")
    meta = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in c["meta"])
    body = f"""{edge(False)}
<main>
  <article class="case-top" id="work">
    <p class="sc">{e(c["kicker"])}</p>
    <p class="kill" aria-hidden="true"><span>{e(c["kill"])}</span></p>
    <h1 class="stack-title">{"".join(lines)}</h1>
    <p class="caret" aria-hidden="true">{e(c["note"])}</p>
    <p class="lede">{e(typo(c["lede"]))}</p>
    <p><a class="back" href="index.html#work">Back to Portfolio</a><a class="back" href="{e(c["original"])}">View Project</a></p>
    <figure class="plate"><img src="{e(c["img"])}" alt="{e(c["alt"])}"><figcaption>{e(c["alt"])}</figcaption></figure>
    <dl class="meta">{meta}</dl>
  </article>
  {src.blocks_html(c["blocks"])}
  {src.case_jumps(slug)}
</main>
"""
    # blocks contain straight quotes; leave them as authored in the source blocks
    # and rely on CSS. Apostrophes in blocks stay unless we post-process.
    return head(c["title"] + " — Joseph Paguirigan") + body + close()


def main():
    folder = ROOT / "g"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(home(), encoding="utf-8")
    for slug in CASES:
        (folder / slug).write_text(case_page(slug), encoding="utf-8")
    print("g ok", (folder / "index.html").stat().st_size)


if __name__ == "__main__":
    main()
