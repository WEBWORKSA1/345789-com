# 345789.com — Phase-wise Build Prompts

Copy each prompt into Claude (or any capable coding agent) in order. Each phase is self-contained, ends with an acceptance checklist, and builds on the previous phase's repo state. Stack: **static HTML + CSS + vanilla JS, zero build step, hosted free on GitHub Pages** (repo `webworksa1/345789-com`).

---

## Global rules (paste at the top of every phase)

```
Project: 345789.com — "345789 · The Lucky Number Lab", a Chinese lucky-number intelligence hub
with free analysers, guides, videos and a numeric-asset lead marketplace.
Stack: static HTML5, one shared CSS file, vanilla ES2020 JS, JSON data files. No frameworks, no
server, must run on GitHub Pages free plan (relative links only, .nojekyll, custom 404.html).
Design: modern, mobile-first, red (#C8102E) / imperial gold (#D4A017) / ink (#121212) palette,
light + dark mode, rounded cards, subtle motion, WCAG AA contrast, Lighthouse ≥ 90.
Mandatory on EVERY page:
 1. A top bar ABOVE the header: "Contact, if you are interested in this website / domain name /
    Sponsorship / Advertisement / Partnership" linking to https://web.works/contact (new tab).
 2. Header with logo, mega-menu (Tools, Meanings, Guides, Videos, Marketplace, Community), theme toggle.
 3. Footer with sitemap links, newsletter form, legal links and the trademark/copyright disclosure line.
 4. At least 2 ad slots (in-content + sidebar/footer) driven by assets/js/config.js.
Email rule: the ONLY contact email is the owner's Gmail address. It must NEVER appear as text in
HTML, JS literals, meta tags or the repo. Store it only as an XOR-obfuscated char-code array in
config.js and assemble at runtime for form POSTs (FormSubmit AJAX endpoint) and "Email us" links.
Trademark: never claim "345789" as a trademark; no third-party logos/brands; original copy only.
Cultural content is labelled "tradition & entertainment — not financial advice".
```

---

## Phase 1 — Foundation, design system & shell

```
Create the repo skeleton:
/index.html, /404.html, /robots.txt, /sitemap.xml, /ads.txt (template), /site.webmanifest, /.nojekyll,
/assets/css/style.css, /assets/js/{config.js,app.js,numbers.js}, /assets/img/{logo.svg,og.svg,favicon.svg},
/build.py (Python generator that renders every page from one header/footer template so the site
stays consistent and expandable — run `python3 build.py` to regenerate).
style.css: CSS variables for colours/spacing/radii, light+dark themes (prefers-color-scheme + toggle
persisted in localStorage inside try/catch), fluid type, grid utilities, cards, buttons, badges,
forms, tabs, accordion, toast, sticky header, mobile drawer nav, top contact bar, ad-slot styles,
print styles, reduced-motion support.
app.js: nav drawer, theme toggle, active link, accordion, tabs, toast, scroll-reveal, year stamp,
newsletter + generic form handler (see Phase 6), AdSense loader, YouTube lite-embed, share buttons.
SEO: unique <title>/meta description per page, canonical, Open Graph/Twitter cards, JSON-LD
(Organization, WebSite+SearchAction, BreadcrumbList, FAQPage where relevant).
Acceptance: every page passes HTML validation, top bar visible on all pages at 360px width, no
horizontal scroll, theme toggle works, 404 page styled.
```

## Phase 2 — Number intelligence engine (numbers.js)

```
Build a reusable analysis engine:
- DIGITS[0-9]: hanzi, pinyin, jyutping, homophones (Mandarin & Cantonese), sentiment score (-3..+3),
  short + long meaning.
- COMBOS dictionary (≥60 entries): 168, 518, 888, 88, 8888, 66, 666, 99, 999, 28, 68, 58, 18, 38,
  1314, 520, 5201314, 3344, 1688, 14, 24, 44, 514, 748, 7414, 74, 250, 54, 5354, 9413, 7456, 448,
  548, 167, 886, 233, 555, 789, 345 ... each with reading, meaning, dialect, score.
- PATTERNS: all-same, AABB, ABAB, ABBA, ABCABC, ascending run (步步高升), descending run, palindrome,
  ending digit weighting (last digit ×2), count of 8/6/9, presence of 4/14/24/514/748.
- analyse(numberString, {dialect:'mandarin'|'cantonese', context:'phone'|'plate'|'house'|'date'|'domain'|'any'})
  → {score 0-100, grade (大吉/吉/平/小凶/凶), perDigit[], combosFound[], patterns[], warnings[],
     suggestions[] (e.g. swap 4 → 8/9, end on 8), chineseReading, pinyinReading}.
- Deterministic, unit-testable, no network.
Acceptance: analyse('345789') returns the 4-warning, the 789 "rise·prosper·endure" combo and the
ascending-run pattern; analyse('168888') scores ≥ 90; analyse('514') scores ≤ 20.
```

## Phase 3 — Tool pages (traffic engine)

```
Create one page per tool, each with: H1, instant-result widget, explanatory article (600-1,200 words),
FAQ accordion with FAQPage schema, related tools, 2 ad slots, a YouTube embed, and a lead CTA card.
Tools:
 1. /tools/number-meaning-analyzer.html (any number; dialect toggle; share result)
 2. /tools/phone-number-luck.html (strip formatting, analyse last 4/8 digits separately)
 3. /tools/license-plate-luck.html (letters ignored, digits analysed, HK/SG/Malaysia notes)
 4. /tools/house-number-luck.html (house + unit + floor; skip-4-floor explainer)
 5. /tools/numeric-domain-valuer.html (length class 2N-8N, pattern family, no-4 flag, 8-count,
    leading-zero penalty, Chinese-premium tier A-E, reference ranges with sources, "get pro valuation" CTA)
 6. /tools/chinese-zodiac-calculator.html (exact Lunar New Year table 1900-2100 from cny.json;
    animal, element, yin/yang, lucky & unlucky numbers, colours, compatibility)
 7. /tools/personal-lucky-numbers.html (birth date + gender → zodiac numbers + Kua number +
    4 lucky / 4 unlucky directions)
 8. /tools/lucky-date-finder.html (Chinese Almanac / Tong Shu 2026-2028 from almanac.json:
    lunar date, day pillar, clash animal, good-for/avoid activities translated to English, day
    quality; filter "best days for wedding / moving / opening a business / signing contracts")
 9. /tools/chinese-number-converter.html (Arabic → 中文, financial 大写, pinyin, digit-by-digit
    phone reading with 幺 for 1, Cantonese jyutping)
Acceptance: all tools work offline after load, results < 50 ms, inputs validated, keyboard accessible.
```

## Phase 4 — Content & programmatic SEO

```
Create: /meanings/index.html (digit grid + searchable combo dictionary), /meanings/number-0.html …
number-9.html (generated by build.py from DIGITS), /the-345789-story.html (the domain's own reading:
3-4-5 then 7-8-9 = rise·prosper·endure; honest note on the 4), /records.html (hall of records:
HK plates, 8888-8888 phone, Vancouver & Chengdu housing studies, HK 2024-25 plate study — cite sources),
/guides/ with 6 long-form articles: angel numbers vs Chinese lucky numbers, why 4 is unlucky (and
where it is lucky), the economics of 8, choosing a lucky wedding date, choosing a lucky business
phone number, numeric-domain investing 101 (6N/5N/4N, no-4, Chinese buyers).
Each article: TOC, author box, updated date, sources list, internal links to ≥3 tools, 2-3 ad slots.
Acceptance: sitemap.xml lists every URL; every page has ≥ 3 internal links in and out.
```

## Phase 5 — Monetisation layer

```
config.js holds: ADSENSE_CLIENT ('' until approved), AD_SLOTS map, YOUTUBE_CHANNEL url, VIDEOS list
(id, title, topic), DONATION links (PayPal.me, Ko-fi, Buy Me a Coffee, Stripe Payment Link,
crypto) — all optional.
- If ADSENSE_CLIENT is set: inject adsbygoogle once, render <ins> per .ad-slot; else show a styled
  "Advertise here" house ad linking to /advertise.html (inventory is never empty).
- /videos.html: YouTube hub with lite-embeds (thumbnail → iframe on click, youtube-nocookie),
  topic filter, subscribe CTA; when VIDEOS is empty, show curated YouTube search cards per topic.
- /advertise.html: audience stats placeholders, ad formats & rate card (banner, sponsored tool,
  newsletter sponsor, featured marketplace listing, YouTube integration), sponsorship inquiry form.
- ads.txt template with the publisher-id placeholder.
Acceptance: no console errors with empty config; enabling ADSENSE_CLIENT renders slots.
```

## Phase 6 — Lead generation (highest priority for revenue)

```
Build /get-your-report.html — the dedicated, high-converting lead page:
- Hero promise + trust strip (methodology, sources, privacy promise, "answered within 48 h").
- 3-step progressive form with progress bar: (1) What do you need? [Personal lucky-number report |
  Business phone/number selection | Wedding / opening date | Numeric domain valuation | Sell my
  numeric domain/plate/phone | Buy a lucky number asset | Consultation] (2) Details (number(s),
  birth date optional, budget, timeline, country) (3) Contact (name, email, WhatsApp/WeChat
  optional, consent checkbox).
- Instant mini-result shown before the contact step (result-first pattern).
- Exit-intent / scroll 60% modal on tool pages offering the free report (once per session).
- Inline lead cards on every tool page; sticky mobile CTA bar.
- /marketplace.html: "List your lucky number asset free" seller form + buyer request form,
  pattern-family explainer, featured listings grid (sample, clearly marked "example").
Form transport: POST JSON to https://formsubmit.co/ajax/<email assembled at runtime>, fields
_subject, _template=table, _captcha=false, honeypot _honey; client-side validation; success toast;
offline fallback opens a mailto built at runtime. The email must never be visible in source.
Acceptance: grep of the repo for the address returns nothing; all forms submit; UTM + page source
captured in a hidden field.
```

## Phase 7 — Community, donations, contests, hiring

```
- /donate.html: why support, 4 tiers (Supporter $8, Patron $88, Sponsor $888, Custom), what funds
  pay for (operations, promotions & marketing, hiring talent, contest prizes), progress bar toward
  a monthly goal, donor wall placeholder, buttons driven by DONATION config, pledge form fallback.
- /contests.html: monthly "Lucky Number Challenge" (submit a number + the story behind it), prize
  tiers, timeline, official rules (no purchase necessary, void where prohibited, eligibility,
  judging criteria, privacy), entry form, past-winners placeholder.
- /careers.html: open roles (Chinese-culture writer, bilingual editor, short-video creator, SEO
  specialist, partnerships manager, community moderator), perks, application form with portfolio URL.
- /about.html, /contact.html (all forms, no exposed email), /privacy.html, /terms.html,
  /legal.html (trademark & copyright disclosure, cultural/entertainment disclaimer, affiliate &
  advertising disclosure, AdSense/cookie notice).
Acceptance: each page has its form wired through the shared handler and the top contact bar.
```

## Phase 8 — QA, performance & launch on GitHub Pages

```
- Run a link checker, HTML validator, axe accessibility scan, Lighthouse mobile.
- Verify no page exposes the email (grep built files and rendered DOM via Playwright).
- Test at 360 / 768 / 1280 px; dark & light.
- Push to github.com/webworksa1/345789-com (main). Settings → Pages → Deploy from branch → main / root.
- Custom domain: add CNAME file "345789.com"; DNS A records → 185.199.108.153, 185.199.109.153,
  185.199.110.153, 185.199.111.153; CNAME www → webworksa1.github.io; enable "Enforce HTTPS".
- First form submission triggers a FormSubmit activation email — click "Activate" once.
- Submit sitemap to Google Search Console; apply for AdSense once 20+ quality pages are indexed.
```

## Phase 9 — Growth (post-launch, expandable)

```
- Simplified-Chinese mirror (/zh/) generated by build.py from the same data.
- Embeddable "Lucky number of the day" widget (iframe/JS snippet) for backlinks.
- Programmatic pages for 100-999 combos and every year's zodiac (2026-2040).
- Newsletter automation (daily lucky number) via a free ESP; YouTube Shorts series per tool.
- Partner integrations: numeric-domain marketplaces & plate dealers (revenue share), escrow.
- Analytics: GA4 / Plausible events for tool use, lead step completion, donation clicks.
```
