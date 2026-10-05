"""Reusable HTML components for 345789.com"""
import html as _h

LOGO = ('<svg viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#C8102E"/><stop offset=".6" stop-color="#E0452B"/><stop offset="1" stop-color="#D4A017"/></linearGradient></defs>'
        '<circle cx="32" cy="32" r="30" fill="url(#lg)"/><circle cx="32" cy="32" r="22" fill="none" stroke="#F4D774" stroke-width="2"/>'
        '<rect x="24" y="24" width="16" height="16" rx="2" fill="#FFFBF5"/><text x="32" y="37.5" text-anchor="middle" font-size="13" font-weight="800" fill="#C8102E" font-family="Arial">8</text></svg>')

def esc(s): return _h.escape(s)

def ad(kind="inContent", cls=""):
    return f'<div class="ad-slot {cls}" data-ad="{kind}" aria-label="Advertisement"></div>'

def analyser(ctx="any", placeholder="Enter any number, e.g. 345789", demo="", label="Your number", dialects=True, big=True):
    seg = ('<div class="seg" data-seg role="group" aria-label="Dialect" style="margin-top:12px">'
           '<button type="button" class="on" data-v="mandarin" aria-pressed="true">Mandarin</button>'
           '<button type="button" data-v="cantonese" aria-pressed="false">Cantonese</button>'
           '<button type="button" data-v="teochew" aria-pressed="false">Teochew (4 = lucky)</button></div>') if dialects else ""
    d = f' data-demo="{demo}"' if demo else ""
    return (f'<div class="analyser" data-analyser="{ctx}"{d}><form novalidate><label for="an-{ctx}">{label}</label>'
            f'<div class="an-row"><input id="an-{ctx}" class="an-in {"big-input" if big else ""}" inputmode="numeric" autocomplete="off" placeholder="{placeholder}" maxlength="40">'
            f'<button class="btn btn-p" type="submit">Analyse</button></div>{seg}</form><div class="result" aria-live="polite"></div></div>')

def faq_html(items):
    return '<div class="acc">' + "".join(f'<details><summary>{esc(q)}</summary><div><p>{esc(a)}</p></div></details>' for q, a in items) + '</div>'

def lead_card(r="{R}", title="Want the expert version?", text="Get a personalised Lucky Number Report — your best numbers, dates and directions, plus a review of any phone, plate, address or domain.", need="personal-report"):
    return (f'<div class="card" style="border:2px solid var(--gold)"><span class="badge">Free · 48 h</span><h3 style="margin-top:10px">{title}</h3>'
            f'<p>{text}</p><p style="margin-top:12px"><a class="btn btn-p btn-block" href="{r}get-your-report.html?need={need}">Get my free report →</a></p></div>')

def newsletter(r="{R}", dark=False):
    return (f'<form class="form" data-form="Newsletter" data-ok="You\'re in! Your first lucky number arrives soon."><div class="nl">'
            f'<input type="email" name="email" required placeholder="you@email.com" aria-label="Email address"><button class="btn btn-g" type="submit">Join</button></div>'
            f'<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true"><div class="form-msg" role="status"></div></form>')

def sidebar(r="{R}", need="personal-report"):
    return (f'<aside class="side"><div class="sticky">{lead_card(r, need=need)}'
            f'<div class="card" data-lotd></div>{ad("sidebar","side-ad")}'
            f'<div class="card"><h3>Popular tools</h3><ul class="small" style="padding-left:1.1em;margin:0">'
            f'<li><a href="{r}tools/number-meaning-analyzer.html">Number Meaning Analyzer</a></li>'
            f'<li><a href="{r}tools/lucky-date-finder.html">Lucky Date Finder</a></li>'
            f'<li><a href="{r}tools/numeric-domain-valuer.html">Numeric Domain Valuer</a></li>'
            f'<li><a href="{r}tools/phone-number-luck.html">Phone Number Luck</a></li>'
            f'<li><a href="{r}tools/chinese-zodiac-calculator.html">Chinese Zodiac Calculator</a></li></ul></div>'
            f'<div class="card"><h3>Support the lab</h3><p>Free tools, funded by readers.</p><p style="margin-top:10px"><a class="btn btn-o btn-sm" href="{r}donate.html">Donate</a></p></div>'
            f'</div></aside>')

TOOLS = [
  ("数", "Number Meaning Analyzer", "Score any number 0–100 with digit, combo and pattern readings.", "tools/number-meaning-analyzer.html"),
  ("机", "Phone Number Luck", "Check your mobile or business line — last 4 digits weighted.", "tools/phone-number-luck.html"),
  ("车", "License Plate Luck", "Read your plate the way Hong Kong & Singapore buyers do.", "tools/license-plate-luck.html"),
  ("宅", "House & Floor Number", "Addresses, unit and floor numbers — and the skip-4 rule.", "tools/house-number-luck.html"),
  ("域", "Numeric Domain Valuer", "Tier any numeric domain for the Chinese market.", "tools/numeric-domain-valuer.html"),
  ("历", "Lucky Date Finder", "Chinese Almanac 2026–2028: weddings, moves, openings.", "tools/lucky-date-finder.html"),
  ("龙", "Chinese Zodiac Calculator", "Exact Lunar New Year cut-off, 1900–2100.", "tools/chinese-zodiac-calculator.html"),
  ("卦", "Personal Lucky Numbers & Kua", "Your digits, Kua number and four lucky directions.", "tools/personal-lucky-numbers.html"),
  ("壹", "Chinese Number Converter", "中文, financial 大写, pinyin & Cantonese readings.", "tools/chinese-number-converter.html"),
]

def tool_grid(r="{R}", exclude=None, n=9):
    items = [t for t in TOOLS if t[3] != exclude][:n]
    return '<div class="grid g3">' + "".join(f'<a class="card reveal" href="{r}{h}"><div class="ic">{g}</div><h3>{t}</h3><p>{d}</p></a>' for g, t, d, h in items) + '</div>'

def video(q, glyph="八"):
    return f'<div data-yt="" data-q="{esc(q)}" data-glyph="{glyph}"></div>'

def form_footer(consent=True):
    c = ('<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="{R}privacy.html">privacy policy</a> and to be contacted about my request.</label>') if consent else ""
    return c + '<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'

def lead_modal(r):
    return (f'<div class="modal" id="lead-modal" role="dialog" aria-modal="true" aria-labelledby="lm-t"><div class="box"><button class="icon-btn x" aria-label="Close">✕</button>'
            f'<span class="badge">Free gift</span><h2 id="lm-t" style="margin-top:10px">Your 2027 Lucky Days Calendar</h2>'
            f'<p class="muted">Best dates for weddings, moves and business openings + your personal lucky numbers. Delivered by email.</p>'
            f'<form class="form" data-form="Lead magnet — Lucky Days Calendar" data-ok="Done! Check your inbox within 48 hours.">'
            f'<input name="name" required placeholder="First name" aria-label="First name"><input type="email" name="email" required placeholder="Email" aria-label="Email">'
            f'<input type="date" name="birth_date" aria-label="Birth date (optional)"><button class="btn btn-p btn-block" type="submit">Send my calendar</button>'
            f'{form_footer().replace("{R}", r)}<div class="form-msg" role="status"></div></form></div></div>')

def footer(r):
    return f'''<footer class="ftr"><div class="wrap"><div class="cols">
<div><a class="logo" href="{r}index.html" style="color:#fff">{LOGO}<span>345789<small style="color:#BBA894">The Lucky Number Lab</small></span></a>
<p style="margin-top:14px;font-size:.93rem">Free tools, data and guides on lucky and unlucky numbers in Chinese culture — and the economy built around them.</p>
<p style="font-size:.9rem;margin-bottom:8px"><b>Daily lucky number by email</b></p>{newsletter(r, True)}</div>
<div><h4>Tools</h4><ul><li><a href="{r}tools/number-meaning-analyzer.html">Number Analyzer</a></li><li><a href="{r}tools/phone-number-luck.html">Phone Number</a></li><li><a href="{r}tools/license-plate-luck.html">License Plate</a></li><li><a href="{r}tools/numeric-domain-valuer.html">Domain Valuer</a></li><li><a href="{r}tools/lucky-date-finder.html">Lucky Dates</a></li><li><a href="{r}tools/chinese-zodiac-calculator.html">Zodiac</a></li></ul></div>
<div><h4>Learn</h4><ul><li><a href="{r}meanings/index.html">Number Meanings</a></li><li><a href="{r}guides/index.html">Guides</a></li><li><a href="{r}records.html">Hall of Records</a></li><li><a href="{r}the-345789-story.html">The 345789 Story</a></li><li><a href="{r}videos.html">Videos</a></li><li><a href="{r}methodology.html">Methodology</a></li></ul></div>
<div><h4>Work with us</h4><ul><li><a href="{r}get-your-report.html">Free Report</a></li><li><a href="{r}marketplace.html">Marketplace</a></li><li><a href="{r}advertise.html">Advertise</a></li><li><a href="{r}careers.html">Careers</a></li><li><a href="{r}contests.html">Contests</a></li><li><a href="{r}donate.html">Donate</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{r}about.html">About</a></li><li><a href="{r}contact.html">Contact</a></li><li><a href="https://web.works/contact" target="_blank" rel="noopener">Buy / partner on this domain</a></li><li><a href="{r}privacy.html">Privacy</a></li><li><a href="{r}terms.html">Terms</a></li><li><a href="{r}legal.html">Trademark &amp; Copyright</a></li></ul></div>
</div>
<div class="legal"><p>© <span class="yr">2026</span> 345789.com. All original content and code © 345789.com. “345789” is used as a descriptive numeral string; no trademark is claimed and the site is not affiliated with any company, product, lottery, phone number, stock code or vehicle plate using the same digits. Cultural readings are tradition &amp; entertainment — not financial, legal or medical advice. See <a href="{r}legal.html">Trademark &amp; Copyright Disclosure</a>.</p></div>
</div></footer>'''

def hero(title, lead, eyebrow=""):
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'<section class="page-hero"><div class="wrap">{eb}<h1 style="margin-top:12px">{title}</h1><p class="lead">{lead}</p></div></section>'

def with_side(main, r="{R}", need="personal-report"):
    return f'<div class="wrap layout"><article class="prose">{main}</article>{sidebar(r, need)}</div>'

def author(updated="October 2026"):
    return ('<div class="author"><div class="av">数</div><div><b>345789 Editorial Team</b><br><span class="small muted">Researched from academic studies, auction records and native-speaker review · Updated ' + updated + ' · <a href="{R}methodology.html">Methodology</a></span></div></div>')
