#!/usr/bin/env python3
"""Generate static art-direction previews from the portfolio copy."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FONTS = {
    "a": "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Caveat:wght@600&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap",
    "b": "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Public+Sans:wght@400;500;600;700&display=swap",
    "c": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Source+Sans+3:wght@400;500;600;700&display=swap",
}

DESC = (
    "Joseph Paguirigan — Senior Product Designer. I hand off products, not comps. "
    "UX/UI and product design for Bungie, Norton, HireRight, and the US Space Force."
)
HERO = (
    "Senior Product Designer in Los Angeles. I turn complicated workflows into products "
    "people can actually use, from research through design systems to shipped code. "
    "Recent work for SCE.com, HireRight, and the U.S. Space Force."
)
ABOUT = [
    "I've designed Halo: Reach (2010) menu UI (agency work for Bungie), Norton security apps, mission software for the U.S. Space Force, and the new SCE.com. The common thread: I figure out what needs to exist, then I make it.",
    "I use Figma, Claude, and code to move quickly from idea to tested prototype, so more time goes to the decisions that matter.",
]
STATS = [
    ("15M", "People served by SCE.com"),
    ("40K+", "Organizations on Screening Manager"),
    ("88", "Usability tests for Space Force"),
]
STACK = [
    ("AI Tools", ["Claude", "Perplexity", "Nano Banana"]),
    ("Design", ["Figma", "Photoshop", "Illustrator", "After Effects"]),
    ("Engineering", ["HTML / CSS", "React / JSX", "GitHub"]),
    ("Research", ["User Interviews", "Usability Testing", "AI Synthesis", "Design Systems"]),
]
BAND = [
    "Research", "Systems Thinking", "AI-Native Design", "Vibe Coding",
    "Product Design", "Prototyping", "Design Systems", "Ship It",
]
GALLERY = [
    ("../../portfolio-insights.jpg", "Insights: HR Analytics Dashboard", "Insights HR analytics dashboard", ["Dashboard", "Data Viz"], "Insights"),
    ("../../portfolio-cannes-lions.jpg", "Cannes Lions: Interactive Installation", "Cannes Lions interactive installation", ["Installation", "Touch UI"], "Cannes Lions"),
    ("../../portfolio-target-ticket.jpg", "Target Ticket: Entertainment Platform", "Target Ticket entertainment platform", ["Product", "Streaming"], "Target Ticket"),
    ("../../portfolio-kobayashi-maru.jpg", "Kobayashi Maru: Defense Tech Brand", "Kobayashi Maru defense tech brand", ["Brand", "Defense"], "Kobayashi Maru"),
    ("../../portfolio-section31.jpg", "Section 31: Brand & Product Design", "Section 31 brand and product design", ["Brand", "Product"], "Section 31"),
    ("../../portfolio-norton-combined.jpg", "Norton: Security & 360 for Gamers", "Norton Security and Norton 360 for Gamers mobile apps", ["Mobile", "iOS"], "Norton"),
    ("../../portfolio-twc.jpg", "Time Warner Cable: On Demand UI", "Time Warner Cable On Demand UI", ["TV/OTT", "Product"], "Time Warner Cable"),
    ("../../portfolio-affirm-combined.jpg", "Affirm: Mobile App & Website", "Affirm mobile app and website", ["Mobile", "Web", "Fintech"], "Affirm"),
]
STEPS = [
    ("01", "Discover", "Interviews, competitive analysis, stakeholder alignment. I talk to users before I open Figma.", True),
    ("02", "Define", "Figure out the actual problem before trying to solve it. Personas, jobs-to-be-done, a real north star. Not glamorous. Completely necessary.", False),
    ("03", "Design", "Rough ideas in Claude, polished in Figma, interactive in Framer. That lets me compare more options before the design review.", True),
    ("04", "Test", "Real users, real tasks, real feedback. I run the sessions, Claude helps make sense of it. If something's broken, we find out before it ships.", True),
    ("05", "Ship", "Design systems, component handoff, or I just build the thing myself. The gap between design and production is a choice. I choose to close it.", False),
]
NAV = [
    ("#work", "Case Studies"),
    ("#about", "About"),
    ("#stack", "Toolkit"),
    ("#portfolio", "Gallery"),
    ("#process", "Process"),
    ("#contact", "Contact"),
]
CASES = [
    ("case-sce.html", "SCE.com Rebuilt."),
    ("case-screening.html", "Screening Manager Reimagined."),
    ("case-relaystrat.html", "Space Force Ops Tools."),
    ("case-halo.html", "Halo: Reach (2010) Menu UI (Schematic, for Bungie)."),
]

DS = "https://josephpaguirigandesign.github.io/SEC-DesignSystem"
VOICE = "https://josephpaguirigandesign.github.io/SEC-BrandVoiceTool/"

PROJECTS = [
    {
        "num": "01",
        "slug": "case-sce.html",
        "title": "SCE.com Rebuilt.",
        "tags": ["Brand Overhaul", "Design System"],
        "img": "../../case-sce-assets/T01-home-desktop.jpg",
        "alt": "SCE.com homepage preview",
        "paragraphs": [
            "SCE.com serves 15 million people, and the site had drifted into a patchwork. I led the rebuild from the ground up: a modular template system that scales from outage alerts to clean-energy storytelling, built on a new design language, component library, and layout standards. One system, one source of truth.",
            "Then I took it further and built the design system parent-down from Figma. Pixel-faithful components, a live Storybook, real tokens engineers could pull straight into code. The Figma file and the codebase, finally in sync.",
            "Then I did the same for words. Built the Brand Voice Tool: real-time scoring across six brand dimensions, one-click AI rewrites, the whole Brand Copy Playbook baked right in. Anyone can ship on-brand copy without waiting on a reviewer. Both tools are live, links below.",
        ],
        "ctas": [
            ("case-sce.html", "Case Study", False),
            (DS, "Design System", True),
            (VOICE, "Brand Voice Tool", True),
        ],
        "outcome": "9 Templates",
        "note": "9 page templates and one component library now run SCE.com, with a live Storybook design system and Brand Voice Tool in production.",
        "tools": "Figma · Claude · Design Tokens",
        "role": "Lead",
        "year": "—",
        "status": "In production",
    },
    {
        "num": "02",
        "slug": "case-screening.html",
        "title": "Screening Manager Reimagined.",
        "tags": ["SaaS Product", "End-to-End Design"],
        "img": "../../case-screening-assets/hireright-preview.jpg",
        "alt": "HireRight Screening Manager preview",
        "paragraphs": [
            "HireRight runs background checks for 40,000+ organizations, and its core screening tool had buckled under its own complexity. I led the rebuild end to end as Lead Product Designer, driving a team of three: research, competitor teardowns, and user interviews, then wireframes straight to production. I collapsed a tangle of order statuses into six states that read the same in Dallas or Düsseldorf, and turned the densest documents in HR into something a recruiter can scan in seconds.",
        ],
        "ctas": [("case-screening.html", "Case Study", False)],
        "outcome": "27 → 6",
        "note": "27 regional status labels reduced to 6, and adjudication review ~30% faster, on a platform used by 40,000+ organizations.",
        "tools": "Figma · Sketch · Prototyping",
        "role": "Lead Product Designer",
        "year": "—",
        "status": "Production",
    },
    {
        "num": "03",
        "slug": "case-relaystrat.html",
        "title": "Space Force Ops Tools.",
        "tags": ["Defense Tech", "Mission-Critical UX"],
        "img": "../../case-relaystrat-preview.jpg",
        "alt": "Relay Strat operations platform preview",
        "paragraphs": [
            "The US Space Force needed real software for the Space Tasking Cycle, not stock-photo UI. I ran 42+ operator co-design sessions and 88 usability sessions on the watch floor, not in a lab. The result is an SOD authoring tool that turns 12 document types into reusable, structured components. Shipped in 2022 and still in active use across the CFSCC mission set.",
        ],
        "ctas": [("case-relaystrat.html", "Case Study", False)],
        "outcome": "In Use",
        "note": "Shipped in 2022 and still in use across the CFSCC mission set. Reviewer time-to-comment dropped from ~14 to under 4 minutes after 42+ operator co-design sessions and 88 usability tests.",
        "tools": "Figma · Sketch · User Research",
        "role": "Product Designer",
        "year": "2022",
        "status": "In Use",
    },
    {
        "num": "04",
        "slug": "case-halo.html",
        "title": "Halo: Reach (2010) Menu UI (Schematic, for Bungie).",
        "tags": ["Game UI", "Interaction Design"],
        "img": "../../portfolio-halo-reach.jpg",
        "alt": "Halo: Reach game UI preview",
        "paragraphs": [
            "At Schematic, I designed menu systems and game UI for Halo: Reach as agency work for Bungie. Console-first and controller-driven, where a clumsy menu is the first thing a player feels.",
        ],
        "ctas": [("case-halo.html", "Case Study", False)],
        "outcome": "",
        "note": "Menu UI shipped in Halo: Reach (2010), played by millions.",
        "tools": "Photoshop · Illustrator · After Effects",
        "role": "Designer, Schematic",
        "year": "2010",
        "status": "Shipped",
    },
]


def e(text):
    return escape(text, quote=True)


def ext(href, label):
    if href.startswith("http"):
        return (
            f'<a href="{e(href)}" target="_blank" rel="noopener">{e(label)}'
            f'<span class="sr"> (opens in a new tab)</span></a>'
        )
    return f'<a href="{e(href)}">{e(label)}</a>'


def head(theme, title, desc=DESC):
    return f"""<!doctype html>
<html lang="en"{" data-theme=\"light\"" if theme == "c" else ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="icon" href="../../favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="../../apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS[theme]}" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#work">Skip to work</a>
"""


def footer(theme):
    links = [("a", "A · Editorial"), ("b", "B · Swiss"), ("c", "C · Engineer")]
    bits = []
    for key, label in links:
        cls = ' class="now"' if key == theme else ""
        href = "../" + key + "/"
        bits.append(f'<a href="{href}"{cls}>{e(label)}</a>' if cls else f'<a href="{href}">{label}</a>')
    return f"""
<footer class="foot">
  <span>Joseph Paguirigan</span>
  <span>Senior Product Designer · 2026</span>
  <nav aria-label="Art direction previews">{''.join(bits)}</nav>
</footer>
<script src="../shared.js"></script>
</body>
</html>
"""


def lightbox():
    return """
<dialog class="lb" data-lightbox aria-label="Gallery">
  <div class="lb-bar">
    <p data-lb-title></p>
    <span data-lb-count></span>
    <button type="button" data-lb-prev>← Prev</button>
    <button type="button" data-lb-next>Next →</button>
    <button type="button" data-lb-close>Close ✕</button>
  </div>
  <img alt="">
</dialog>
"""


def actions(ctas, primary=False):
    out = ['<div class="actions">']
    for i, (href, label, external) in enumerate(ctas):
        cls = ""
        if primary and i == 0:
            cls = ' class="primary"'
        if external:
            out.append(
                f'<a{cls} href="{e(href)}" target="_blank" rel="noopener">{e(label)}'
                f'<span class="sr"> (opens in a new tab)</span></a>'
            )
        else:
            out.append(f'<a{cls} href="{e(href)}">{e(label)}</a>')
    out.append("</div>")
    return "\n".join(out)


def kpi(p):
    value = f'<div class="val">{e(p["outcome"])}</div>' if p["outcome"] else ""
    return f"""<dl class="kpi">
  <dt>Key Outcome</dt>
  <dd>{value}{e(p["note"])}</dd>
  <dt>Tools Used</dt>
  <dd>{e(p["tools"])}</dd>
</dl>"""


def gallery_buttons():
    bits = []
    for src, title, alt, tags, name in GALLERY:
        bits.append(
            f"""<button type="button" class="shot" data-gallery data-img="{e(src)}" data-alt="{e(alt)}" data-title="{e(title)}">
  <img src="{e(src)}" alt="">
  <b>{e(name)}</b>
  <i>{e(" · ".join(tags))}</i>
  <span class="view">View Project</span>
</button>"""
        )
    return "\n".join(bits)


def case_jumps(current):
    bits = []
    for slug, title in CASES:
        cur = ' aria-current="page"' if slug == current else ""
        bits.append(f'<a href="{slug}"{cur}>{e(title)}</a>')
    return f'<nav class="case-jump" aria-label="Case studies">{"".join(bits)}</nav>'


# ---------- homes ----------

def home_a():
    projects = []
    for i, p in enumerate(PROJECTS):
        paras = "\n".join(f"<p>{e(t)}</p>" for t in p["paragraphs"])
        media = ""
        cls = "project"
        if i == 0:
            cls = "project lead"
        else:
            media = f"""<a class="media" href="{e(p["slug"])}">
    <img src="{e(p["img"])}" alt="{e(p["alt"])}">
  </a>"""
        projects.append(f"""<article class="{cls}">
  <div>
    <p class="tags">{e(" · ".join(p["tags"]))}</p>
    <h3>{e(p["title"])}</h3>
    {paras}
    {actions(p["ctas"])}
    {kpi(p)}
  </div>
  {media}
</article>""")
    stats = "\n".join(f"<div><b>{e(n)}</b><span>{e(l)}</span></div>" for n, l in STATS)
    stack = "\n".join(
        "<div><h3>{}</h3><ul>{}</ul></div>".format(e(cat), "".join(f"<li>{e(t)}</li>" for t in tools))
        for cat, tools in STACK
    )
    steps = "\n".join(
        f'<article><div class="n">{n}</div><h3>{e(name)}</h3><p>{e(desc)}</p>'
        + ('<span class="ai">AI-Augmented</span>' if ai else "")
        + "</article>"
        for n, name, desc, ai in STEPS
    )
    nav = "\n".join(f'<a href="{href}">{e(label)}</a>' for href, label in NAV)
    band = " ".join(f"<span>{e(w)}</span>" for w in BAND)
    first = PROJECTS[0]
    return head("a", "Joseph Paguirigan, Senior Product Designer") + f"""
<header class="top">
  <a class="brand" href="#top">Joseph Paguirigan</a>
  <a class="phone" href="tel:3103087383">310.308.7383</a>
  <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav class="nav" id="site-nav" data-nav>
    {nav}
    <a class="nav-phone" href="tel:3103087383">310.308.7383</a>
  </nav>
</header>
<main class="wrap" id="top">
  <section class="hero" id="work">
    <div class="crop">
      <h1>Joseph <em class="acc">Paguirigan</em></h1>
      <p class="proof" aria-hidden="true"><span class="hand">crop</span></p>
    </div>
    <div class="hero-copy">
      <p class="eyebrow">Senior Product Designer · Los Angeles</p>
      <p class="dek">{e(HERO)}</p>
      <a class="cta" href="#selected">Case Studies</a>
    </div>
    <a class="hero-work" href="{e(first["slug"])}">
      <span class="overprint-num" aria-hidden="true">01</span>
      <img src="{e(first["img"])}" alt="{e(first["alt"])}">
      <span class="hero-cap"><b>{e(first["title"])}</b><em>{e(first["outcome"])}</em></span>
    </a>
  </section>

  <header class="opener" id="selected">
    <p class="kicker">03 / Case Studies</p>
    <h2>Selected Work.</h2>
    <svg class="scribble" viewBox="0 0 92 46" aria-hidden="true"><path d="M6 28c10-18 70-22 80-2 3 8-12 16-30 14C32 38 4 34 8 22" fill="none" stroke="#7f1d1d" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="rule-note" aria-hidden="true">ok</span>
  </header>
  {''.join(projects)}

  <p class="band" aria-label="Practice">{band}</p>

  <section id="about">
    <header class="opener">
      <p class="kicker">01 / About</p>
      <h2>Sharp instincts. <em>Shipped.</em></h2>
      <span class="rule-note" aria-hidden="true">stet</span>
    </header>
    <div class="about">
      <div></div>
      <div>
        {''.join(f'<p>{e(p)}</p>' for p in ABOUT)}
        <div class="stats">{stats}</div>
      </div>
    </div>
  </section>

  <section id="stack">
    <header class="opener">
      <p class="kicker">02 / Toolkit</p>
      <h2>The Stack.</h2>
    </header>
    <div class="stack">{stack}</div>
  </section>

  <section id="portfolio">
    <header class="opener">
      <p class="kicker">04 / Gallery</p>
      <h2>Selects.</h2>
    </header>
    <div class="gallery">{gallery_buttons()}</div>
  </section>

  <section id="process">
    <header class="opener">
      <p class="kicker">05 / Process</p>
      <h2>From Brief to Ship.</h2>
    </header>
    <div class="steps">{steps}</div>
  </section>

  <section id="contact">
    <header class="opener">
      <p class="kicker">Open to New Projects</p>
    </header>
    <div class="contact">
      <p class="lede">Let's Go.</p>
      <a class="mail" href="mailto:josephpaguirigan@gmail.com">josephpaguirigan@gmail.com</a>
      <div class="contact-actions">
        <a href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Download Résumé <span class="sr">(opens in a new tab)</span></a>
      </div>
      <p class="stamp">I GET SHIT DONE</p>
    </div>
  </section>
</main>
{lightbox()}
""" + footer("a")


def home_b():
    rows = []
    dossiers = []
    for p in PROJECTS:
        rows.append(f"""<a class="row" href="{e(p["slug"])}">
  <span class="no">{p["num"]}</span>
  <img src="{e(p["img"])}" alt="">
  <span class="name">{e(p["title"])}<span class="sub">{e(" · ".join(p["tags"]))}</span></span>
  <span class="role">{e(p["role"])}</span>
  <span class="year">{e(p["year"])}</span>
  <span class="out">{e(p["outcome"] or "Shipped")}</span>
</a>""")
        paras = "\n".join(f"<p>{e(t)}</p>" for t in p["paragraphs"])
        dossiers.append(f"""<article class="dossier">
  <div class="no">{p["num"]}</div>
  <div>
    <h3>{e(p["title"])}</h3>
    {paras}
    {actions(p["ctas"])}
    {kpi(p)}
  </div>
  <a href="{e(p["slug"])}"><img src="{e(p["img"])}" alt="{e(p["alt"])}"></a>
</article>""")
    nav = "\n".join(f'<a href="{href}">{e(label)}</a>' for href, label in NAV)
    stats = "\n".join(f"<div><b>{e(n)}</b><span>{e(l)}</span></div>" for n, l in STATS)
    stack = "\n".join(
        "<div><h3>{}</h3><ul>{}</ul></div>".format(e(cat), "".join(f"<li>{e(t)}</li>" for t in tools))
        for cat, tools in STACK
    )
    steps = "\n".join(
        f'<article><div class="n">{n}</div><h3>{e(name)}</h3><p>{e(desc)}</p>'
        + ('<span class="ai">AI-Augmented</span>' if ai else "")
        + "</article>"
        for n, name, desc, ai in STEPS
    )
    band = "".join(f"<span>{e(w)}</span>" for w in BAND)
    return head("b", "Joseph Paguirigan, Senior Product Designer") + f"""
<header class="mast">
  <div class="frame" style="padding-bottom:0">
    <div class="id-row">
      <div>
        <h1>Joseph Paguirigan</h1>
        <p class="role">Senior Product Designer · Los Angeles</p>
      </div>
      <a class="phone" href="tel:3103087383">310.308.7383</a>
    </div>
    <nav class="nav" aria-label="Primary">{nav}</nav>
  </div>
</header>
<main class="frame">
  <p class="dek">{e(HERO)}</p>
  <section class="index" id="work">
    <h2>Selected Work.</h2>
    <div class="head" aria-hidden="true"><span>No.</span><span></span><span>Project</span><span>Role</span><span>Year</span><span>Outcome</span></div>
    {''.join(rows)}
  </section>
  {''.join(dossiers)}
  <p class="band">{band}</p>

  <section class="section" id="about">
    <h2>01 / About — Sharp instincts. Shipped.</h2>
    <div class="split">
      {''.join(f'<p>{e(p)}</p>' for p in ABOUT)}
    </div>
    <div class="stats">{stats}</div>
  </section>

  <section class="section" id="stack">
    <h2>02 / Toolkit — The Stack.</h2>
    <div class="cols4">{stack}</div>
  </section>

  <section class="section" id="portfolio">
    <h2>04 / Gallery — Selects.</h2>
    <div class="gallery">{gallery_buttons()}</div>
  </section>

  <section class="section" id="process">
    <h2>05 / Process — From Brief to Ship.</h2>
    <div class="cols5">{steps}</div>
  </section>

  <section class="section contact" id="contact">
    <h2>Open to New Projects — Let's Go.</h2>
    <p><a class="mail" href="mailto:josephpaguirigan@gmail.com">josephpaguirigan@gmail.com</a></p>
    <div class="contact-actions">
      <a href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Download Résumé <span class="sr">(opens in a new tab)</span></a>
    </div>
    <p class="aside">I GET SHIT DONE</p>
  </section>
</main>
{lightbox()}
""" + footer("b")


def home_c():
    cards = []
    for p in PROJECTS:
        paras = "\n".join(f"<p>{e(t)}</p>" for t in p["paragraphs"])
        out = e(p["outcome"]) if p["outcome"] else "Shipped"
        year = "" if p["year"] == "—" else " · " + e(p["year"])
        cards.append(f"""<article class="card">
  <span class="topline" aria-hidden="true"></span>
  <span class="anno">CaseStudy · {p["num"]} · {e(p["status"])}</span>
  <a href="{e(p["slug"])}"><img src="{e(p["img"])}" alt="{e(p["alt"])}"></a>
  <h3>{e(p["title"])}</h3>
  <p class="tags">{e(" · ".join(p["tags"]))}</p>
  <div class="out"><b>{out}</b><span>{e(p["role"])}{year}</span></div>
  {paras}
  {actions(p["ctas"], primary=True)}
  <span class="anno">padding 12 · radius 12 · {e(p["tools"])}</span>
  <p class="kpi-note">{e(p["note"])}</p>
</article>""")
    # kpi note needs a style - I'll use a plain p which is already styled
    nav = "\n".join(f'<a href="{href}">{e(label)}</a>' for href, label in NAV)
    stats = "\n".join(
        f'<div class="stat"><b>{e(n)}</b><span>{e(l)}</span><i>stat / {e(n.lower())}</i></div>'
        for n, l in STATS
    )
    tools = "\n".join(
        "<section class=\"tool\"><h3>{}</h3><ul>{}</ul></section>".format(
            e(cat), "".join(f"<li>{e(t)}</li>" for t in items)
        )
        for cat, items in STACK
    )
    steps = "\n".join(
        f'<article class="step"><div class="n">{n}</div><h3>{e(name)}</h3><p>{e(desc)}</p>'
        + ('<span class="chip">AI-Augmented</span>' if ai else "")
        + "</article>"
        for n, name, desc, ai in STEPS
    )
    band = "".join(f"<span>{e(w)}</span>" for w in BAND)
    return head("c", "Joseph Paguirigan, Senior Product Designer") + f"""
<header class="bar">
  <a class="brand" href="#top">JP</a>
  <nav class="nav" aria-label="Primary">{nav}</nav>
  <button class="theme" type="button" data-theme-toggle aria-pressed="false">Dark mode</button>
  <a class="resume-link" href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Résumé<span class="sr"> (opens in a new tab)</span></a>
</header>
<main class="page" id="top">
  <section class="intro">
    <div>
      <p class="status"><span class="dot" aria-hidden="true"></span> Open to New Projects</p>
      <h1>Joseph Paguirigan</h1>
      <p class="job">Senior Product Designer · Los Angeles</p>
      <p class="dek">{e(HERO)}</p>
      <p><a href="tel:3103087383">310.308.7383</a></p>
    </div>
    <div class="statrow">{stats}</div>
  </section>

  <section id="work">
    <div class="sec-label"><h2>Selected Work.</h2><span>03 / Case Studies</span></div>
    <div class="cards">{''.join(cards)}</div>
  </section>

  <div class="band" aria-label="Practice">{band}</div>

  <section id="about">
    <div class="sec-label"><h2>Sharp instincts. Shipped.</h2><span>01 / About</span></div>
    <div class="about-copy">{''.join(f'<p>{e(p)}</p>' for p in ABOUT)}</div>
  </section>

  <section id="stack">
    <div class="sec-label"><h2>The Stack.</h2><span>02 / Toolkit · 4 groups</span></div>
    <div class="tools">{tools}</div>
  </section>

  <section id="portfolio">
    <div class="sec-label"><h2>Selects.</h2><span>04 / Gallery</span></div>
    <div class="gallery">{gallery_buttons()}</div>
  </section>

  <section id="process">
    <div class="sec-label"><h2>From Brief to Ship.</h2><span>05 / Process</span></div>
    <div class="steps">{steps}</div>
  </section>

  <section id="contact">
    <div class="sec-label"><h2>Let's Go.</h2><span>Open to New Projects</span></div>
    <div class="contact">
      <a class="mail" href="mailto:josephpaguirigan@gmail.com">josephpaguirigan@gmail.com</a>
      <div class="contact-actions">
        <a href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Download Résumé <span class="sr">(opens in a new tab)</span></a>
      </div>
      <p class="phrase">I GET SHIT DONE</p>
    </div>
  </section>
</main>
{lightbox()}
""" + footer("c")


# ---------- case studies ----------

def flow(nodes):
    """nodes: ('p', text) ('h3', text) ('img', src, alt) ('note', h, p) ('video', src)"""
    html = []
    for n in nodes:
        kind = n[0]
        if kind == "p":
            html.append(f"<p>{e(n[1])}</p>")
        elif kind == "h3":
            html.append(f"<h3>{e(n[1])}</h3>")
        elif kind == "img":
            html.append(f'<figure class="single"><img src="{e(n[1])}" alt="{e(n[2])}"><figcaption>{e(n[2])}</figcaption></figure>')
        elif kind == "pair":
            figs = []
            for src, alt in n[1]:
                figs.append(f'<figure><img src="{e(src)}" alt="{e(alt)}"><figcaption>{e(alt)}</figcaption></figure>')
            html.append(f'<div class="pair">{"".join(figs)}</div>')
        elif kind == "notes":
            cards = []
            for h, p in n[1]:
                cards.append(f"<article><h3>{e(h)}</h3><p>{e(p)}</p></article>")
            html.append(f'<div class="notes">{"".join(cards)}</div>')
        elif kind == "stack":
            bits = []
            for h, p in n[1]:
                body = f"<p>{e(p)}</p>" if p else ""
                bits.append(f"<article><h3>{e(h)}</h3>{body}</article>")
            html.append(f'<div class="stack-notes">{"".join(bits)}</div>')
        elif kind == "video":
            html.append(
                f'<video controls playsinline preload="metadata"><source src="{e(n[1])}" type="video/mp4">Your browser does not support the video tag.</video>'
            )
    return "\n".join(html)


def blocks_html(blocks):
    parts = []
    for b in blocks:
        inner = flow(b.get("flow", []))
        h = f'<h2>{e(b["h2"])}</h2>' if b.get("h2") else ""
        line = '<span class="topline" aria-hidden="true"></span>' if True else ""
        parts.append(f'<section class="block">{line}{h}{inner}</section>')
    return "\n".join(parts)


def case_page(theme, current, kicker, title_html, lede, meta, hero_img, hero_alt, blocks, original=None):
    meta_html = []
    for dt, dd in meta:
        meta_html.append(f"<div><dt>{e(dt)}</dt><dd>{e(dd)}</dd></div>")
    orig = ""
    if original:
        orig = f'<p><a class="back" href="{e(original)}">View Project</a></p>'
    hero_fig = ""
    if hero_img:
        hero_fig = f'<figure><img src="{e(hero_img)}" alt="{e(hero_alt)}"><figcaption>{e(hero_alt)}</figcaption></figure>'
    # title_html is trusted (we build it)
    nav_links = []
    # case pages link home anchors
    labels = NAV
    if theme == "a":
        links = "\n".join(f'<a href="index.html{href}">{e(label)}</a>' for href, label in labels)
        header = f"""<header class="top">
  <a class="brand" href="index.html">Joseph Paguirigan</a>
  <a class="phone" href="tel:3103087383">310.308.7383</a>
  <button class="menu-btn" type="button" data-menu aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav class="nav" id="site-nav" data-nav>{links}<a class="nav-phone" href="tel:3103087383">310.308.7383</a></nav>
</header>
<main class="wrap">"""
    elif theme == "b":
        links = "\n".join(f'<a href="index.html{href}">{e(label)}</a>' for href, label in labels)
        header = f"""<header class="mast">
  <div class="frame" style="padding-bottom:0">
    <div class="id-row">
      <div><h1 style="font-size:22px"><a href="index.html" style="color:inherit;text-decoration:none">Joseph Paguirigan</a></h1>
      <p class="role">Senior Product Designer · Los Angeles</p></div>
      <a class="phone" href="tel:3103087383">310.308.7383</a>
    </div>
    <nav class="nav" aria-label="Primary">{links}</nav>
  </div>
</header>
<main class="frame">"""
    else:
        links = "\n".join(f'<a href="index.html{href}">{e(label)}</a>' for href, label in labels)
        header = f"""<header class="bar">
  <a class="brand" href="index.html">JP</a>
  <nav class="nav" aria-label="Primary">{links}</nav>
  <button class="theme" type="button" data-theme-toggle aria-pressed="false">Dark mode</button>
  <a class="resume-link" href="../../joseph-paguirigan-resume.pdf" target="_blank" rel="noopener">Résumé<span class="sr"> (opens in a new tab)</span></a>
</header>
<main class="page">"""
    return head(theme, title_html.replace("<em>", "").replace("</em>", "") + " — Joseph Paguirigan") + header + f"""
<article class="case-hero" id="work">
  <div class="case-top">
    <div>
      <p class="kicker">{e(kicker)}</p>
      <h1>{title_html}</h1>
      <p class="lede">{e(lede)}</p>
      <a class="back" href="index.html#work">Back to Portfolio</a>
      {orig}
    </div>
    {hero_fig}
  </div>
  <dl class="meta">{''.join(meta_html)}</dl>
</article>
{blocks_html(blocks)}
{case_jumps(current)}
</main>
""" + footer(theme)


SCE_BLOCKS = [
    {"h2": "One brand. Hundreds of pages. No system.", "flow": [
        ("p", "SCE.com serves 15 million people, from wildfire alerts to rate plans. But every team built pages their own way. Components were rebuilt from scratch, layouts drifted, and the brand looked different depending on where you landed. Shipping anything meant reinventing the basics first."),
    ]},
    {"h2": "A homepage built for crisis & calm.", "flow": [
        ("p", "Wildfire and outage messaging is always available without blocking the everyday tasks that keep the lights on, literally. The same four quicklinks anchor every page on the site."),
        ("pair", [
            ("../../case-sce-assets/T01-home-desktop.jpg", "SCE Home, Desktop"),
            ("../../case-sce-assets/T01-home-mobile.jpg", "SCE Home, Mobile"),
        ]),
        ("notes", [
            ("Crisis lives above the fold.", "The hero swaps between seasonal storytelling and active wildfire/outage alerts, without ever pushing the four quicklinks below the fold."),
            ("Four jobs, one row.", "Pay Bill, Outage, Moving, Payment Assistance, the high-intent actions every customer arrives looking for. Anchored on a yellow rail across every template."),
            ("Newsroom + community.", "Below the fold, the home page hands off to editorial: programs, scam alerts, PSPS guidance, and community stories, surfaced when relevant, quiet when not."),
        ]),
    ]},
    {"h2": "When a section needs its own front door.", "flow": [
        ("p", "A photo-led landing that stages programs as equal peers. Six cards, one clear path in, from EV charging to workforce development. Pair this template with a strong hero photo and the system does the rest."),
        ("pair", [
            ("../../case-sce-assets/T02-landing-a-desktop.jpg", "Clean Energy & Efficiency, Desktop"),
            ("../../case-sce-assets/T02-landing-a-mobile.jpg", "Clean Energy & Efficiency, Mobile"),
        ]),
    ]},
    {"h2": "One system, two cadences.", "flow": [
        ("p", "Landing B leans editorial, longer-form cards that breathe. Landing C is denser, a six-up grid for sections with many siblings. Same components, different rhythms."),
        ("pair", [
            ("../../case-sce-assets/T03-landing-b-desktop.jpg", "Landing B, Desktop"),
            ("../../case-sce-assets/T03-landing-b-mobile.jpg", "Landing B, Mobile"),
        ]),
        ("p", "Stacked full-bleed cards. Each tile gets room to breathe."),
        ("pair", [
            ("../../case-sce-assets/T04-landing-c-desktop.jpg", "Landing C, Desktop"),
            ("../../case-sce-assets/T04-landing-c-mobile.jpg", "Landing C, Mobile"),
        ]),
        ("p", "Six-up grid for parents with many children. Compact & scannable."),
    ]},
    {"h2": "Five layouts for five kinds of content.", "flow": [
        ("p", "From a single-column long read to a three-column rate comparison, the detail family covers everything below a landing. Editors pick the structure, the system handles the typography."),
        ("pair", [
            ("../../case-sce-assets/T05-details-1col-desktop.jpg", "One-column detail, desktop"),
            ("../../case-sce-assets/T05-details-1col-mobile.jpg", "One-column detail, mobile"),
        ]),
        ("pair", [
            ("../../case-sce-assets/T06-details-2col-desktop.jpg", "Two-column detail, desktop"),
            ("../../case-sce-assets/T06-details-2col-mobile.jpg", "Two-column detail, mobile"),
        ]),
        ("pair", [
            ("../../case-sce-assets/T07-details-3col-desktop.png", "Three-column detail, desktop"),
            ("../../case-sce-assets/T07-details-3col-mobile.jpg", "Three-column detail, mobile"),
        ]),
        ("pair", [
            ("../../case-sce-assets/T08-details-1over2-desktop.jpg", "One-over-two detail, desktop"),
            ("../../case-sce-assets/T08-details-1over2-mobile.jpg", "One-over-two detail, mobile"),
        ]),
        ("pair", [
            ("../../case-sce-assets/T09-details-sidebar-desktop.jpg", "Sidebar detail, desktop"),
            ("../../case-sce-assets/T09-details-sidebar-mobile.jpg", "Sidebar detail, mobile"),
        ]),
    ]},
    {"h2": "One system the whole site runs on.", "flow": [
        ("p", "The Figma file and the codebase finally agree. New pages now ship from the system instead of from scratch."),
    ]},
]

SCREEN_BLOCKS = [
    {"h2": "The most critical workflow in HR, buried in its own complexity.", "flow": [
        ("p", "HireRight screens candidates for 40,000+ organizations. But the tool recruiters lived in had grown into a maze. Order statuses overlapped and meant different things to different people. Candidate reports were so dense no one could scan them. The experience drifted from region to region. The work was mission-critical, and the interface was working against it."),
    ]},
    {"h2": "Every candidate, every status, one screen.", "flow": [
        ("p", "Recruiters live here. A real-time list of every background check in flight, filterable, sortable, exportable, with status pills that mean the same thing whether you're hiring in Dallas or Düsseldorf."),
        ("h3", "Orders and Reports"),
        ("notes", [
            ("Six states, globally consistent.", "The old system had 27 status strings across regions. We collapsed them to six clear states, In progress, Awaiting consent, Needs review, Flagged, Complete, Cancelled, with a single color language that survives translation."),
            ("Updated, not refreshed.", "Behind the dashboard, a websocket bus pushes status changes within seconds of upstream vendors completing a check. Recruiters stop refreshing; the table just updates."),
            ("Built for power users.", 'Every recruiter has a "Mine, urgent" view. Operations has "Stalled > 5 days." Legal has "Flagged, North America." Filters compose into saved URLs they paste into Slack.'),
        ]),
    ]},
    {"h2": "Compliance-dense. Decision-ready.", "flow": [
        ("p", "A background report is one of the densest documents in HR, criminal history, education, identity, credit, drug testing, motor-vehicle records. The redesign organizes it so a hiring manager can read it in two minutes, and adjudicators can act in five."),
        ("h3", "Renata Polanski"),
        ("stack", [
            ("Identity & right to work", ""),
            ("Education & credentials", ""),
            ("Employment history (5 yr)", ""),
            ("Criminal · civil · sanctions", ""),
            ("Activity timeline", ""),
            ("Adjudicator recommendation", ""),
        ]),
        ("notes", [
            ("Decision first, data underneath.", 'A red "Needs review" headline pill, the count of clear/flagged checks, then the dense detail. Hiring managers scan; adjudicators read; everyone gets what they need.'),
            ("Every event, timestamped.", "Right-side activity feed shows the order's full life, consent, vendor calls, returns, escalations. The same audit log that compliance officers used to dig out of database exports."),
            ("Rules transparent, never hidden.", 'When the rules engine recommends "Engage," it shows its work, which policy, what thresholds. Adjudicators retain full FCRA-compliant override authority.'),
        ]),
    ]},
    {"h2": "Hiring at a glance, compliance under the hood.", "flow": [
        ("p", "Insights pulls every order, every adjudication, every vendor SLA into one place, so HR leaders can spot regional drift, slow vendors, or hiring bottlenecks before they cost a quarter."),
        ("img", "../../case-screening-assets/hireright-preview.jpg", "HireRight Screening Manager, Management Reports"),
        ("h3", "Management Reports"),
        ("h3", "Orders by region · last 90 days"),
        ("h3", "Turnaround by package"),
        ("p", "Orders, turnaround, clear rate, SLA misses, ranked by what HR leaders actually report to the board."),
        ("p", "Stacked bars reveal regional volume shifts, APAC hiring crept up; EMEA spiked in March."),
        ("p", "Color hardens as packages drift past SLA. Executive +0.8d, the conversation starts here."),
        ("p", "Every card ends with one sentence: what this chart actually means for the program this week."),
    ]},
    {"h2": "Same product, on the train.", "flow": [
        ("p", "A recruiter on the go needs to triage, not order. Mobile collapses to the few moves that matter: see what needs attention, see one candidate, kick off the next screen."),
        ("p", "The 12 items needing me, ordered by SLA. Tap a row → full report. Pull to refresh; nothing else."),
        ("p", "The full report compressed to what matters on a phone: status, counts, what to do next."),
        ("p", "Four steps to a screening: candidate, package, consent, review. Region rules apply themselves; the recruiter just answers."),
    ]},
    {"h2": "A command center recruiters can actually run.", "flow": [
        ("p", "Statuses that mean the same thing in Dallas or Düsseldorf. Reports a recruiter can scan in seconds. The most critical workflow in HR, rebuilt to get out of its own way."),
    ]},
]

RELAY_BLOCKS = [
    {"h2": None, "flow": [
        ("stack", [
            ("Operators first.", "Every screen co-designed with the people who'd use it on a console. Weekly hands-on usability tests, not a single throwaway persona."),
            ("Mission scale.", "From a single sensor MX entry to a multi-payload launch schedule, the same component system holds together. Designed to scale with the cycle."),
            ("Classification-aware.", "Markings, paragraph portion marks, releasability rails. The interface treats classification as a first-class data type, not an afterthought."),
            ("Built to ship.", "Shipping software to active operators on real timelines. No stock-photo UI, no theoretical workflows, only patterns that survive a watch shift."),
        ]),
    ]},
    {"h2": "Field over theory.", "flow": [
        ("p", "This wasn't enterprise software with a side of compliance. It was compliance-first software where every interaction was tested against a console operator's reality, and rejected if it didn't survive it."),
        ("notes", [
            ("Sit at the console first.", "Before sketching a single screen, we shadowed strategists writing SODs by hand and operators receiving them. We mapped the artifact's full lifecycle, draft, review, publish, distribute, revise, with the people who lived it."),
            ("Whiteboards > mockups.", "Weekly sessions with Space Force operators and strategists. We didn't bring polished comps to validate, we brought rough flows to break. The orange rail, classification markings, and section nav all came out of those rooms."),
            ("Tested where it ships.", "Usability testing wasn't a lab moderated study. It was operators running a real SOD draft through Relay Strat on a real console, on a real day. If a pattern didn't survive a shift, it didn't ship."),
        ]),
    ]},
    {"h2": "Before the first pixel.", "flow": [
        ("p", "Strategists were drafting SODs in Word docs, marking up classification by hand, and emailing PDFs for review. We mapped the full lifecycle of the artifact, from blank cursor to published & distributed at echelon, with the people who lived it."),
        ("h3", "SOD lifecycle, current state, summer 2020"),
    ]},
    {"h2": "Whiteboard to shipped.", "flow": [
        ("p", "Three rough sketches set the spine of the product, an editable section tree, classification chips inline with content, and a per-paragraph review state. The hi-fi wireframe locked the layout. Every UI element you see in the final composition traces back to a marker on these boards."),
        ("h3", "Mid-fi wireframe, SOD authoring view"),
        ("p", "Left rail mirrors SOD doctrine. Section state surfaced as colored dots so authors find their unfinished work."),
        ("p", 'Draft · Preview · Published replace ambiguous "Final v3 (revised) FINAL.docx" filenames. State is system, not folklore.'),
        ("p", "Schedules & rosters that strategists used to type into paragraphs became structured data, sortable, filterable, exportable."),
        ("p", "Single CTA collapses two anxious steps. Locking implies review-ready; review-ready implies locked. No half-states."),
    ]},
    {"h2": "If it didn't survive a shift, it didn't ship.", "flow": [
        ("p", "Eight rounds of moderated tests on the watch floor and over secure VTC. Each round produced a findings log scored for severity and confidence, and a redesign pass that shipped to the next round, no patterns went forward unless operators confirmed them."),
        ("h3", "Save · Submit · Approve"),
        ("h3", "Autosave + Lock & Review"),
        ("p", "By R4, every operator could tell a saved draft from a submitted one at a glance. Time-to-comment dropped from 14 minutes to under 4, reviewers went straight to their own paragraphs instead of scrolling whole documents, and the offline-PDF workaround became a first-class export."),
    ]},
    {"h2": "The real thing, in production.", "flow": [
        ("p", "Relay Strat, live across the CFSCC mission set since 2022."),
        ("img", "../../portfolio-relay-strat.jpg", "Relay Strat shipped product"),
        ("img", "../../case-relaystrat-assets/relay-strat-composition.jpg", "Relay Strat interface, authoring and review"),
    ]},
]

HALO_BLOCKS = [
    {"h2": "Designed for a controller, at ten feet.", "flow": [
        ("p", "Console-first and controller-driven: every menu had to read instantly and navigate cleanly on a gamepad, from the couch. In a game, a clumsy menu isn't a papercut — it's the first thing a player feels, every single session. Tight constraints, high stakes, zero room for confusion."),
        ("video", "../../case-halo-assets/halo_casestudy.mp4"),
    ]},
    {"h2": "The screens millions of players touched.", "flow": [
        ("p", "The menus and in-game UI players navigated every session. Tight constraints, high stakes, zero room for confusion."),
        ("img", "../../portfolio-halo-reach.jpg", "Halo: Reach game UI"),
    ]},
    {"h2": "The Outcome", "flow": [
        ("p", "Menu UI shipped in Halo: Reach (2010), played by millions."),
    ]},
]


def all_cases(theme):
    pages = {}
    pages["case-sce.html"] = case_page(
        theme, "case-sce.html", "Case Study / 01",
        "Powering the new <em>sce.com</em>",
        "A modular page-template system for Southern California Edison, 15 million people, one coherent web experience. Designed to scale from outage alerts to clean-energy storytelling.",
        [("Role", "Lead"), ("Outcome", "9 Templates"), ("Tools", "Figma · Claude · Design Tokens"), ("Status", "In production")],
        "../../case-sce-assets/T01-home-desktop.jpg", "SCE Home, Desktop",
        SCE_BLOCKS, "../../case-sce.html",
    )
    pages["case-screening.html"] = case_page(
        theme, "case-screening.html", "Case Study / 02",
        "Screening, at the speed of hiring.",
        "Reimagining HireRight Screening Manager, a global background-check platform used by 40,000+ organizations, into a real-time command center for HR teams.",
        [("Role", "Lead Product Designer"), ("Outcome", "27 → 6"), ("Tools", "Figma · Sketch · Prototyping"), ("Status", "Production")],
        "../../case-screening-assets/hireright-preview.jpg", "HireRight Screening Manager preview",
        SCREEN_BLOCKS, "../../case-screening.html",
    )
    pages["case-relaystrat.html"] = case_page(
        theme, "case-relaystrat.html", "Case Study / 03",
        "Real tools for real missions.",
        "Software for the Space Tasking Cycle, designed in partnership with U.S. Space Force operators and strategists. User research and usability testing weren't optional, they were the job. No stock photo UI here.",
        [("Role", "Product Designer"), ("Outcome", "In Use"), ("Tools", "Figma · Sketch · User Research"), ("Year", "2022")],
        "../../portfolio-relay-strat.jpg", "Relay Strat shipped product",
        RELAY_BLOCKS, "../../case-relaystrat.html",
    )
    pages["case-halo.html"] = case_page(
        theme, "case-halo.html", "Case Study / 04",
        "Halo: Reach (2010) Menu UI (Schematic, for Bungie).",
        "Menu systems and game UI for Halo: Reach. Console-first, controller-driven, and seen by millions of players every time they booted up.",
        [("Role", "Designer, Schematic"), ("Outcome", "Shipped"), ("Tools", "Photoshop · Illustrator · After Effects"), ("Year", "2010")],
        "../../portfolio-halo-reach.jpg", "Halo: Reach game UI",
        HALO_BLOCKS, "../../case-halo.html",
    )
    return pages


def main():
    homes = {"a": home_a(), "b": home_b(), "c": home_c()}
    for theme, html in homes.items():
        folder = ROOT / theme
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "index.html").write_text(html, encoding="utf-8")
        for name, page in all_cases(theme).items():
            (folder / name).write_text(page, encoding="utf-8")
        print(theme, "ok", len(html))


if __name__ == "__main__":
    main()
