#!/usr/bin/env python3
"""345789.com static site generator.
Run:  python3 build.py   → regenerates every .html page from the content modules in /_src.
No dependencies. Output is plain static HTML that GitHub Pages serves as-is."""
import json, os, sys, html, datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "_src"))
from components import *          # noqa
import pages_main, pages_tools, pages_content

BASE = os.path.dirname(os.path.abspath(__file__))
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

BASE404 = """<script>document.write('<base href="'+(location.pathname.indexOf('/345789-com/')===0?'/345789-com/':'/')+'">')</script>"""

def page(p):
    path = p["path"]; depth = path.count("/"); r = "../" * depth
    title = p["title"]; desc = p["desc"]
    canon = SITE_URL + ("" if path == "index.html" else path)
    ld = [ {"@context":"https://schema.org","@type":"WebSite","name":"345789 · The Lucky Number Lab","url":SITE_URL,
            "potentialAction":{"@type":"SearchAction","target":SITE_URL+"tools/number-meaning-analyzer.html?n={number}","query-input":"required name=number"}} ] if path == "index.html" else []
    if p.get("crumbs"):
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":i+1,"name":n,"item":SITE_URL+h} for i,(n,h) in enumerate([("Home","")]+p["crumbs"])]})
    if p.get("faq"):
        ld.append({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]})
    if p.get("article"):
        ld.append({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"dateModified":TODAY,
                   "author":{"@type":"Organization","name":"345789 Editorial Team"},"publisher":{"@type":"Organization","name":"345789.com"}})
    if path == "index.html":
        ld.append({"@context":"https://schema.org","@type":"Organization","name":"345789.com","url":SITE_URL,"logo":SITE_URL+"assets/img/logo.svg"})
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    crumbs = ""
    if p.get("crumbs"):
        parts = [f'<a href="{r}index.html">Home</a>'] + [f'<a href="{r}{h}">{html.escape(n)}</a>' for n,h in p["crumbs"][:-1]] + [html.escape(p["crumbs"][-1][0])]
        crumbs = f'<nav class="crumbs wrap" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'
    scripts = f'<script src="{r}assets/js/config.js"></script><script src="{r}assets/js/app.js" defer></script>'
    if p.get("tools", True):
        scripts += f'<script src="{r}assets/js/numbers.js" defer></script><script src="{r}assets/js/tools.js" defer></script>'
    body = p["body"].replace("{R}", r)
    modal = lead_modal(r) if p.get("modal") else ""
    noindex = '<meta name="robots" content="noindex">' if p.get("noindex") else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{BASE404 if path == "404.html" else ""}<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{noindex}<link rel="canonical" href="{canon}">
<meta property="og:type" content="{'article' if p.get('article') else 'website'}">
<meta property="og:site_name" content="345789 · The Lucky Number Lab">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#C8102E">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ldh}
{scripts}
</head>
<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar" role="note">Contact, if you are interested in this <b>website / domain name / Sponsorship / Advertisement / Partnership</b> → <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{r}index.html" aria-label="345789 home">{LOGO}<span>345789<small>The Lucky Number Lab</small></span></a>
<nav class="nav" id="nav" aria-label="Main">{nav_html(r)}</nav>
<div class="hdr-cta"><button class="icon-btn theme-t" aria-label="Toggle dark mode">☾</button><button class="icon-btn burger" aria-controls="nav" aria-expanded="false" aria-label="Menu">☰</button></div>
</div></header>
<div class="scrim"></div>
{crumbs}
<main id="main">
{body}
</main>
{footer(r)}
<div class="mcta"><a class="btn btn-p" href="{r}get-your-report.html">🎁 Free Lucky Number Report</a></div>
{modal}
</body>
</html>
'''

def main():
    pages = pages_main.PAGES + pages_tools.PAGES + pages_content.PAGES
    urls = []
    for p in pages:
        out = os.path.join(BASE, p["path"]); os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w", encoding="utf-8").write(page(p))
        if not p.get("noindex"): urls.append((p["path"], p.get("prio", "0.7")))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        loc = SITE_URL + ("" if u == "index.html" else u)
        sm.append(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    open(os.path.join(BASE, "sitemap.xml"), "w").write("\n".join(sm))
    print(f"Built {len(pages)} pages")

if __name__ == "__main__":
    main()
