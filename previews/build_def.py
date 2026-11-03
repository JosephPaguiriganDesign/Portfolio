#!/usr/bin/env python3
"""Radical typographic previews D, E, F. Does not rewrite A–C."""
from html import escape
from pathlib import Path

import build as src

ROOT = Path(__file__).resolve().parent

FONTS = {
    "d": "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Caveat:wght@600;700&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap",
    "e": "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800&family=Public+Sans:wght@400;500;600;700&display=swap",
    "f": "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800&family=Fraunces:ital,opsz,wght@1,9..144,560;1,9..144,650&family=Newsreader:opsz,wght@6..72,400;6..72,600&display=swap",
}
PREVIEWS = [
    ("a", "A · Editorial"),
    ("b", "B · Swiss"),
    ("c", "C · Engineer"),
    ("d", "D · Proof"),
    ("e", "E · Broken / rebuilt"),
    ("f", "F · Signal"),
]


def e(text):
    return escape(text, quote=True)


def shell_open(theme, title):
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
<link href="{FONTS[theme]}" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body class="{theme}">
<a class="skip" href="#work">Skip to work</a>
"""


def edge(home=True):
    links = []
    for href, label in src.NAV:
        target = href if home else f"index.html{href}"
        links.append(f'<a href="{target}">{e(label)}</a>')
    links.append('<a class="phone" href="tel:3103087383">310.308.7383</a>')
    brand = "index.html" if not home else "#top"
    work = "#work" if home else "index.html#work"
    return f"""<header class="edge">
  <a class="who" href="{brand}">Joseph Paguirigan</a>
  <a class="jump" href="{work}">Case Studies</a>
  <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav id="site-nav" data-nav aria-label="Primary">{''.join(links)}</nav>
</header>
"""


def close(theme):
    bits = []
    for key, label in PREVIEWS:
        cls = ' class="now"' if key == theme else ""
        bits.append(f'<a href="../{key}/"{cls}>{e(label)}</a>')
    return f"""
<footer class="foot">
  <span>Joseph Paguirigan</span>
  <span>Senior Product Designer · 2026</span>
  <nav aria-label="Art direction previews">{''.join(bits)}</nav>
</footer>
<script src="../shared.js"></script>
<script src="../radical.js"></script>
</body>
</html>
"""


def dossiers():
    parts = []
    for p in src.PROJECTS:
        paras = "\n".join(f"<p>{e(t)}</p>" for t in p["paragraphs"])
        parts.append(f"""<article class="dossier">
  <div class="num">{p["num"]}</div>
  <div>
    <h3>{e(p["title"])}</h3>
    <p class="tags">{e(" · ".join(p["tags"]))}</p>
    {paras}
    {src.actions(p["ctas"])}
    {src.kpi(p)}
    <img src="{e(p["img"])}" alt="{e(p["alt"])}">
  </div>
</article>""")
    return "\n".join(parts)


def rest(slug_about, slug_stack, slug_gallery, slug_process, slug_contact):
    stats = "\n".join(f"<div><b>{e(n)}</b><span>{e(l)}</span></div>" for n, l in src.STATS)
    stack = "\n".join(
        "<div><h3>{}</h3><ul>{}</ul></div>".format(
            e(cat), "".join(f"<li>{e(t)}</li>" for t in tools)
        )
        for cat, tools in src.STACK
    )
    steps = "\n".join(
        f'<article><div class="n">{n}</div><h3>{e(name)}</h3><p>{e(desc)}</p>'
        + ('<span class="ai">AI-Augmented</span>' if ai else "")
        + "</article>"
        for n, name, desc, ai in src.STEPS
    )
    band = " ".join(e(w) for w in src.BAND)
    about = "".join(f"<p>{e(p)}</p>" for p in src.ABOUT)
    return f"""
<p class="dek">{e(src.HERO)}</p>
<div class="wrap">
  {dossiers()}
  <p class="band">{band}</p>
  <section id="about">
    <h2 class="slug">{slug_about}</h2>
    <div class="prose">{about}</div>
    <div class="stats">{stats}</div>
  </section>
  <section id="stack">
    <h2 class="slug">{slug_stack}</h2>
    <div class="stack cols">{stack}</div>
  </section>
  <section id="portfolio">
    <h2 class="slug">{slug_gallery}</h2>
    <div class="gallery">{src.gallery_buttons()}</div>
  </section>
  <section id="process">
    <h2 class="slug">{slug_process}</h2>
    <div class="steps">{steps}</div>
  </section>
  <section id="contact" class="contact">
    <h2 class="slug">{slug_contact}</h2>
    <p class="big">Let's Go.</p>
    <p><a class="mail" href="mailto:josephpaguirigan@gmail.com">josephpaguirigan@gmail.com</a></p>
    <div class="contact-actions">
      <a href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Download Résumé <span class="sr">(opens in a new tab)</span></a>
    </div>
    <p class="stamp phrase aside">I GET SHIT DONE</p>
  </section>
</div>
"""


def galleys_d():
    rows = []
    for p in src.PROJECTS:
        out = p["outcome"] or "Shipped"
        rows.append(
            f'<a class="galley" href="{e(p["slug"])}"><span class="num">{p["num"]}</span>'
            f'<span class="ttl">{e(p["title"])}</span><span class="out">{e(out)}</span></a>'
        )
    return "\n".join(rows)


def home_d():
    body = f"""{edge(True)}
<main id="top">
  <section class="poster" aria-label="Joseph Paguirigan">
    <p class="kill" aria-hidden="true"><span>Comps.</span></p>
    <h1>Joseph Paguirigan</h1>
  </section>
  <p class="pen" aria-hidden="true">not comps. ships.</p>
  <section class="galleys" id="work" aria-label="Selected Work.">
    <h2 class="sr">Selected Work.</h2>
    {galleys_d()}
  </section>
  {rest("Sharp instincts. <em>Shipped.</em>", "The Stack.", "Selects.", "From Brief to Ship.", "Open to New Projects")}
</main>
{src.lightbox()}
"""
    return shell_open("d", "Joseph Paguirigan, Senior Product Designer") + body + close("d")


def home_e():
    rows = []
    for p in src.PROJECTS:
        out = p["outcome"] or "Shipped"
        rows.append(
            f'<a class="row" href="{e(p["slug"])}"><span class="num">{p["num"]}</span>'
            f'<span class="ttl">{e(p["title"])}</span><span class="out">{e(out)}</span></a>'
        )
    body = f"""{edge(True)}
<main id="top">
  <h1 class="collision">
    <span class="w w1">De</span><span class="w w2">sign</span><span class="w w3">er</span>
  </h1>
  <section class="system" id="work">
    <h2>Selected Work.</h2>
    {''.join(rows)}
  </section>
  {rest("Sharp instincts. Shipped.", "The Stack.", "Selects.", "From Brief to Ship.", "Open to New Projects")}
</main>
{src.lightbox()}
"""
    return shell_open("e", "Joseph Paguirigan, Senior Product Designer") + body + close("e")


def home_f():
    ghosts = [
        ("Ship it.", "-8", "1"),
        ("Ship it.", "4", "2"),
        ("Research", "-3", "3"),
        ("Systems", "6", "4"),
    ]
    layers = []
    for word, rot, depth in ghosts:
        layers.append(
            f'<span data-drift data-rot="{rot}" data-d="{depth}" style="--rot:{rot}deg">{e(word)}</span>'
        )
    links = []
    for p in src.PROJECTS:
        out = p["outcome"] or "Shipped"
        links.append(
            f'<a href="{e(p["slug"])}"><span class="ttl">{e(p["title"])}</span>'
            f'<span class="out">{e(out)}</span></a>'
        )
    body = f"""{edge(True)}
<main id="top">
  <section class="poster">
    <div class="ghosts" aria-hidden="true">{''.join(layers)}</div>
    <p class="signal">Ship it.</p>
    <h1>Joseph Paguirigan</h1>
  </section>
  <nav class="wave" id="work" aria-label="Selected Work.">
    <h2 class="sr">Selected Work.</h2>
    {''.join(links)}
  </nav>
  {rest("Sharp instincts. Shipped.", "The Stack.", "Selects.", "From Brief to Ship.", "Open to New Projects")}
</main>
{src.lightbox()}
"""
    return shell_open("f", "Joseph Paguirigan, Senior Product Designer") + body + close("f")


CASES = {
    "case-sce.html": dict(
        kicker="Case Study / 01",
        title="Powering the new sce.com",
        title_html="Powering the new <em>sce.com</em>",
        kill="Patchwork.",
        lede="A modular page-template system for Southern California Edison, 15 million people, one coherent web experience. Designed to scale from outage alerts to clean-energy storytelling.",
        meta=[("Role", "Lead"), ("Outcome", "9 Templates"), ("Tools", "Figma · Claude · Design Tokens"), ("Status", "In production")],
        img="../../case-sce-assets/T01-home-desktop.jpg",
        alt="SCE Home, Desktop",
        blocks=src.SCE_BLOCKS,
        original="../../case-sce.html",
        lines=["Powering", "the new", "sce.com"],
    ),
    "case-screening.html": dict(
        kicker="Case Study / 02",
        title="Screening, at the speed of hiring.",
        title_html="Screening, at the speed of hiring.",
        kill="Maze.",
        lede="Reimagining HireRight Screening Manager, a global background-check platform used by 40,000+ organizations, into a real-time command center for HR teams.",
        meta=[("Role", "Lead Product Designer"), ("Outcome", "27 → 6"), ("Tools", "Figma · Sketch · Prototyping"), ("Status", "Production")],
        img="../../case-screening-assets/hireright-preview.jpg",
        alt="HireRight Screening Manager preview",
        blocks=src.SCREEN_BLOCKS,
        original="../../case-screening.html",
        lines=["Screening,", "at the speed", "of hiring."],
    ),
    "case-relaystrat.html": dict(
        kicker="Case Study / 03",
        title="Real tools for real missions.",
        title_html="Real tools for real missions.",
        kill="Stock-photo.",
        lede="Software for the Space Tasking Cycle, designed in partnership with U.S. Space Force operators and strategists. User research and usability testing weren't optional, they were the job. No stock photo UI here.",
        meta=[("Role", "Product Designer"), ("Outcome", "In Use"), ("Tools", "Figma · Sketch · User Research"), ("Year", "2022")],
        img="../../portfolio-relay-strat.jpg",
        alt="Relay Strat shipped product",
        blocks=src.RELAY_BLOCKS,
        original="../../case-relaystrat.html",
        lines=["Real tools", "for real", "missions."],
    ),
    "case-halo.html": dict(
        kicker="Case Study / 04",
        title="Halo: Reach (2010) Menu UI (Schematic, for Bungie).",
        title_html="Halo: Reach (2010) Menu UI (Schematic, for Bungie).",
        kill="Clumsy.",
        lede="Menu systems and game UI for Halo: Reach. Console-first, controller-driven, and seen by millions of players every time they booted up.",
        meta=[("Role", "Designer, Schematic"), ("Outcome", "Shipped"), ("Tools", "Photoshop · Illustrator · After Effects"), ("Year", "2010")],
        img="../../portfolio-halo-reach.jpg",
        alt="Halo: Reach game UI",
        blocks=src.HALO_BLOCKS,
        original="../../case-halo.html",
        lines=["Halo: Reach", "Menu UI", "Bungie"],
    ),
}


def case_page(theme, slug):
    c = CASES[slug]
    meta = "".join(f"<div><dt>{e(dt)}</dt><dd>{e(dd)}</dd></div>" for dt, dd in c["meta"])
    plate = (
        f'<figure class="plate"><img src="{e(c["img"])}" alt="{e(c["alt"])}">'
        f"<figcaption>{e(c['alt'])}</figcaption></figure>"
    )
    if theme == "d":
        hero = f"""<p class="kill" aria-hidden="true"><span>{e(c["kill"])}</span></p>
    <h1>{c["title_html"]}</h1>
    <p class="pen" aria-hidden="true">stet — ships</p>"""
    elif theme == "e":
        lines = []
        for i, line in enumerate(c["lines"]):
            hot = ' class="hot"' if i == len(c["lines"]) - 1 else ""
            lines.append(f"<span{hot}>{e(line)}</span>")
        hero = f'<h1 class="stack-title">{"".join(lines)}</h1>'
    else:
        ghosts = "".join(
            f'<span data-drift data-rot="{rot}">{e(c["lines"][0])}</span>'
            for rot in ("-8", "5", "-2")
        )
        hero = f"""<div class="ghosts" aria-hidden="true">{ghosts}</div>
    <h1>{c["title_html"]}</h1>"""
    body = f"""{edge(False)}
<main>
  <article class="case-hero" id="work">
    <p class="kicker">{e(c["kicker"])}</p>
    {hero}
    <p class="lede">{e(c["lede"])}</p>
    <p><a class="back" href="index.html#work">Back to Portfolio</a></p>
    <p><a class="back" href="{e(c["original"])}">View Project</a></p>
    {plate}
    <dl class="meta">{meta}</dl>
  </article>
  {src.blocks_html(c["blocks"])}
  {src.case_jumps(slug)}
</main>
"""
    plain = c["title"] + " — Joseph Paguirigan"
    return shell_open(theme, plain) + body + close(theme)


def main():
    homes = {"d": home_d(), "e": home_e(), "f": home_f()}
    for theme, html in homes.items():
        folder = ROOT / theme
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(html, encoding="utf-8")
        for slug in CASES:
            (folder / slug).write_text(case_page(theme, slug), encoding="utf-8")
        print(theme, "bytes", len(html))


if __name__ == "__main__":
    main()
