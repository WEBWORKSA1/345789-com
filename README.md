# 345789.com — The Lucky Number Lab

Chinese lucky-number intelligence hub: free analysers, a Chinese Almanac lucky-date finder, zodiac and Kua calculators, a numeric-domain valuer, guides, a video hub and a lead-generation marketplace. Static HTML/CSS/JS, hosted on the GitHub Pages free plan.

## Structure
```
index.html, get-your-report.html (lead gen), marketplace.html, donate.html, contests.html,
careers.html, advertise.html, videos.html, records.html, the-345789-story.html, methodology.html,
about.html, contact.html, legal.html, privacy.html, terms.html, 404.html
tools/      9 interactive tools + hub
meanings/   digits 0–9 + combination dictionary
guides/     6 long-form guides
assets/css/style.css     design system (light/dark)
assets/js/config.js      ← the only file you edit for AdSense, YouTube, donations, GA4
assets/js/numbers.js     number-intelligence engine
assets/js/tools.js       tool UIs
assets/js/app.js         nav, theme, forms, ads, video, modals
assets/data/cny.json     Lunar New Year dates 1900–2100 (almanac runs in-browser via lunar-javascript, MIT)
_src/                    page content (Python) → `python3 build.py` regenerates all pages + sitemap
project-docs/            RESEARCH.md (findings & decision) · BUILD-PROMPTS.md (phase-wise prompts)
```

## How publishing works
GitHub Pages builds this repo with Jekyll on the free plan — no workflow needed. Every page file (`*.html`) holds front matter plus its body; `_layouts/default.html` adds the shared head, top contact bar, header, footer and lead modal; `_includes/sidebar.html` is the shared sidebar. To change content, edit `_src/*.py` and run `python3 build.py`, then commit the regenerated pages.

Pages source: Settings → Pages → Deploy from a branch → `main` / root (or `gh-pages`).

## Go-live checklist
1. **Forms:** the first submission sends a FormSubmit activation email to the site inbox — click *Activate Form* once. All forms then deliver there. The address is never shown on the site (it is assembled at runtime from an obfuscated array in `config.js`).
2. **AdSense:** once approved, set `ADSENSE_CLIENT` (and optional slot ids) in `assets/js/config.js`, and put your publisher id in `ads.txt`. Until then, slots show house ads.
3. **YouTube:** add video ids to `VIDEOS` in `config.js`.
4. **Donations:** add PayPal.me / Ko-fi / Buy Me a Coffee / Stripe links to `DONATE` in `config.js`.
5. **Custom domain:** set `baseurl: ""` in `_config.yml`, add a `CNAME` file containing `345789.com`; at the registrar set A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and `www` CNAME → `webworksa1.github.io`; then enable *Enforce HTTPS* in Settings → Pages.
6. Submit `sitemap.xml` in Google Search Console.

## Regenerating locally
```
pip install lunardate
python3 gen_data.py   # Lunar New Year data
python3 build.py      # rebuild pages from _src/
```

## Legal
“345789” is used as a descriptive numeral string; no trademark is claimed. See `legal.html`.
