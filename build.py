#!/usr/bin/env python3
"""345789.com page generator (Jekyll edition).
Run:  python3 build.py
Writes every page as <path>.html with Jekyll front matter + body, plus _layouts/default.html,
_includes/*.html and sitemap.xml. GitHub Pages (free plan, Jekyll) then wraps each page in the
shared layout on its servers — no build workflow needed.
Custom domain: set `baseurl: ""` in _config.yml."""
import json, os, sys, html, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "_src"))
import components
R = "{{ site.baseurl }}/"
_real_sidebar = components.sidebar
components.sidebar = lambda r="{R}", need="personal-report": '{%% include sidebar.html need="%s" %%}' % need
from components import LOGO, footer, lead_modal  # noqa
import pages_main, pages_tools, pages_content

SITE_URL = "https://345789.com/"
TODAY = datetime.date.today().isoformat()

NAV = [
  ("Tools", "tools/index.html", [
    ("Number Meaning Analyzer", "tools/number-meaning-analyzer.html"),
    ("Phone Number Luck", "tools/phone-number-luck.html"),
    ("License Plate Luck", "tools/license-plate-luck.html"),
    ("House & Floor Number", "tools/house-number-luck.html"),
    ("Numeric Domain Valuer", "tools/numeric-domain-valuer.html"),
    ("Lucky Date Finder (Almanac)", "tools/lucky-date-finder.html"),
    ("Chinese Zodiac Calculator", "tools/chinese-zodiac-calculator.html"),
    ("Personal Lucky Numbers & Kua", "tools/personal-lucky-numbers.html"),
    ("Chinese Number Converter", "tools/chinese-number-converter.html"),
  ]),
  ("Meanings", "meanings/index.html", [
    ("All Digits & Combos", "meanings/index.html"),
    ("The 345789 Story", "the-345789-story.html"),
    ("Hall of Records", "records.html"),
    ("Methodology", "methodology.html"),
  ]),
  ("Guides", "guides/index.html", None),
  ("Videos", "videos.html", None),
  ("Marketplace", "marketplace.html", None),
  ("Community", "contests.html", [
    ("Contests & Prizes", "contests.html"),
    ("Support / Donate", "donate.html"),
    ("Careers — We're Hiring", "careers.html"),
    ("Advertise & Sponsor", "advertise.html"),
    ("About", "about.html"),
    ("Contact", "contact.html"),
  ]),
]

def nav_html(r):
    out = []
    for label, href, sub in NAV:
        if sub:
            items = "".join(f'<a href="{r}{h}">{t}</a>' for t, h in sub)
            out.append(f'<div class="dd"><button class="dd-t" aria-haspopup="true">{label} ▾</button><div class="dd-m">{items}</div></div>')
        else:
            out.append(f'<a href="{r}{href}">{label}</a>')
    out.append(f'<a class="btn btn-p btn-sm" style="color:#fff;margin-left:6px" href="{r}get-your-report.html">Free Report</a>')
    return "".join(out)

LAYOUT = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{ page.title }}</title>
<meta name="description" content="{{ page.description }}">
{% if page.noindex %}<meta name="robots" content="noindex">{% endif %}<link rel="canonical" href="https://345789.com{{ page.url | replace: 'index.html', '' }}">
<meta property="og:type" content="{% if page.article %}article{% else %}website{% endif %}">
<meta property="og:site_name" content="345789 · The Lucky Number Lab">
<meta property="og:title" content="{{ page.title }}">
<meta property="og:description" content="{{ page.description }}">
<meta property="og:url" content="https://345789.com{{ page.url | replace: 'index.html', '' }}">
<meta property="og:image" content="https://345789.com/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#C8102E">
<link rel="icon" href="{{ site.baseurl }}/assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{{ site.baseurl }}/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/style.css">
<script src="{{ site.baseurl }}/assets/js/config.js"></script><script src="{{ site.baseurl }}/assets/js/app.js" defer></script><script src="{{ site.baseurl }}/assets/js/numbers.js" defer></script><script src="{{ site.baseurl }}/assets/js/tools.js" defer></script>
</head>
<body data-root="{{ site.baseurl }}/">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">Contact, if you are interested in this <b>website / domain name / Sponsorship / Advertisement / Partnership</b> → <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{{ site.baseurl }}/index.html" aria-label="345789 home">''' + LOGO + '''<span>345789<small>The Lucky Number Lab</small></span></a>
<nav class="nav" id="nav" aria-label="Main">''' + nav_html(R) + '''</nav>
<div class="hdr-cta"><button class="icon-btn theme-t" aria-label="Toggle dark mode">☾</button><button class="icon-btn burger" aria-controls="nav" aria-expanded="false" aria-label="Menu">☰</button></div>
</div></header>
<div class="scrim"></div>
<main id="main">
{{ content }}
</main>
''' + footer(R) + '''
<div class="mcta"><a class="btn btn-p" href="{{ site.baseurl }}/get-your-report.html">🎁 Free Lucky Number Report</a></div>
{% if page.modal %}''' + lead_modal(R) + '''{% endif %}
</body>
</html>
'''

def ld_and_crumbs(p):
    path = p["path"]; title = p["title"]; desc = p["desc"]
    ld = []
    if path == "index.html":
        ld.append({"@context":"https://schema.org","@type":"WebSite","name":"345789 · The Lucky Number Lab","url":SITE_URL,
                   "potentialAction":{"@type":"SearchAction","target":SITE_URL+"tools/number-meaning-analyzer.html?n={number}","query-input":"required name=number"}})
        ld.append({"@context":"https://schema.org","@type":"Organization","name":"345789.com","url":SITE_URL,"logo":SITE_URL+"assets/img/logo.svg"})
    if p.get("crumbs"):
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":i+1,"name":n,"item":SITE_URL+h} for i,(n,h) in enumerate([("Home","")]+p["crumbs"])]})
    if p.get("faq"):
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]})
    if p.get("article"):
        ld.append({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"dateModified":TODAY,
                   "author":{"@type":"Organization","name":"345789 Editorial Team"},"publisher":{"@type":"Organization","name":"345789.com"}})
    out = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    if p.get("crumbs"):
        parts = [f'<a href="{R}index.html">Home</a>'] + [f'<a href="{R}{h}">{html.escape(n)}</a>' for n,h in p["crumbs"][:-1]] + [html.escape(p["crumbs"][-1][0])]
        out += f'\n<nav class="crumbs wrap" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'
    return out

def yq(s): return json.dumps(s, ensure_ascii=False)   # JSON strings are valid YAML

def page_file(p):
    fm = ["---", "layout: default", "title: " + yq(p["title"]), "description: " + yq(p["desc"])]
    if p.get("modal"): fm.append("modal: true")
    if p.get("article"): fm.append("article: true")
    if p.get("noindex"): fm.append("noindex: true")
    if p["path"] == "404.html": fm.append("permalink: /404.html")
    fm.append("---")
    return "\n".join(fm) + "\n" + ld_and_crumbs(p) + "\n" + p["body"].replace("{R}", R) + "\n"

def main():
    pages = pages_main.PAGES + pages_tools.PAGES + pages_content.PAGES
    os.makedirs(os.path.join(HERE, "_layouts"), exist_ok=True); os.makedirs(os.path.join(HERE, "_includes"), exist_ok=True)
    open(os.path.join(HERE, "_layouts/default.html"), "w", encoding="utf-8").write(LAYOUT)
    open(os.path.join(HERE, "_includes/sidebar.html"), "w", encoding="utf-8").write(_real_sidebar(R, "{{ include.need }}") + "\n")
    urls = []
    for p in pages:
        out = os.path.join(HERE, p["path"]); os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(page_file(p))
        if not p.get("noindex"): urls.append((p["path"], p.get("prio", "0.7")))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        sm.append(f"<url><loc>{SITE_URL}{'' if u == 'index.html' else u}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(HERE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    print(f"Built {len(pages)} pages")

if __name__ == "__main__":
    main()
