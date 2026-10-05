from components import *

PAGES = []

def tool_page(path, h1, eyebrow, lead, widget, article, faq, title, desc, vq, glyph, need="personal-report"):
    body = (hero(h1, lead, eyebrow) +
        f'<div class="wrap">{widget}</div>' +
        with_side(ad() + article + f'<h2>Watch</h2><div class="grid g2">{video(vq, glyph)}{video("chinese lucky numbers explained","八")}</div>'
                  + '<h2>FAQ</h2>' + faq_html(faq) + ad() + '<h2>More free tools</h2>' + tool_grid(exclude=path, n=6) + author(), need=need))
    PAGES.append(dict(path=path, title=title, desc=desc, body=body, faq=faq, modal=True, prio="0.9",
                      crumbs=[("Tools", "tools/index.html"), (h1, path)]))

# ---------- hub
PAGES.append(dict(path="tools/index.html", prio="0.9", crumbs=[("Tools","tools/index.html")],
  title="Free Chinese Lucky Number Tools — Analyzer, Almanac, Zodiac, Domain Valuer | 345789",
  desc="Nine free tools: number meaning analyzer, phone & plate luck, house numbers, numeric domain valuer, Chinese Almanac lucky dates, zodiac, Kua and number converter.",
  body=hero("Free lucky-number tools", "Instant, private, no sign-up. Every result explains why, not just a score.", "🧮 9 tools") +
       f'<div class="wrap">{tool_grid()}{ad()}<div class="cta-band" style="margin-top:20px"><div><h2>Need a human expert?</h2><p>Get a free personalised report reviewed by a specialist within 48 hours.</p></div><div><a class="btn btn-o" href="{{R}}get-your-report.html">Get my report</a></div></div></div>'))

# ---------- 1 analyzer
tool_page("tools/number-meaning-analyzer.html", "Number Meaning Analyzer", "数 Any number",
  "Type any number — a price, a birthday, a lottery-free lucky pick, a PIN you'd never share — and see how a Chinese speaker hears it.",
  analyser("any", "e.g. 168, 5201314, 345789", demo=""),
  '''<h2>How the analyzer reads a number</h2><p>Chinese speakers hear numbers as words. The analyzer does the same in four passes:</p>
<ol><li><b>Digits</b> — each digit's homophone (8 发 prosper, 4 死 death, 9 久 lasting…).</li><li><b>Combinations</b> — 50+ phrases such as 168 一路发 “prosperity all the way” or 514 我要死 “I want to die”.</li><li><b>Patterns</b> — repeats, AABB/ABAB, palindromes and ascending runs (步步高升).</li><li><b>Endings</b> — the last digits count most.</li></ol>
<p>Switch between <b>Mandarin</b>, <b>Cantonese</b> and <b>Teochew</b> readings: 54 is “I die” in Mandarin but “won't die” in Cantonese, and Teochew families often treat 4 as lucky.</p>
<h2>Quick reference</h2><table><tr><th>Lucky</th><th>Unlucky</th></tr><tr><td>8, 6, 9, 2 · 168, 518, 888, 1314, 520</td><td>4 · 14, 24, 514, 748, 250</td></tr></table>''',
  [("What is the luckiest number in Chinese?","8 — it sounds like 发 (fā), 'to prosper'. 888 and 8888 are even stronger."),
   ("Is my score a prediction?","No. It measures how auspicious a number sounds in Chinese culture — tradition and entertainment, not fortune-telling."),
   ("Why does my score change in Cantonese?","Some digits sound different. 2 is 'easy' in Cantonese, and 54 flips from 'I die' to 'won't die'.")],
  "Number Meaning Analyzer — What Does Your Number Mean in Chinese? | 345789",
  "Free Chinese number meaning analyzer. Score any number 0-100 with digit homophones, lucky combinations like 168 and 518, patterns and Cantonese readings.",
  "what does 8 mean in chinese", "数")

# ---------- 2 phone
tool_page("tools/phone-number-luck.html", "Phone Number Luck Checker", "机 Mobile & business lines",
  "Check how lucky your mobile or business number is. The final four digits get special weight — exactly how buyers in China, Hong Kong and Singapore judge them.",
  analyser("phone", "e.g. +86 138 8888 1688", label="Phone number"),
  '''<h2>Why phone numbers matter</h2><p>In 2003 Sichuan Airlines paid about US$280,000 for +86 28 8888 8888. Telecoms in China, Hong Kong, Singapore and Malaysia sell “golden numbers” (靓号) at premium prices, and businesses print lucky numbers on every sign and card.</p>
<h2>What makes a phone number lucky</h2><ul><li><b>Ending:</b> the last 4 digits matter most — endings in 8, 88, 168, 1688 or 6688 are prized.</li><li><b>No 4s:</b> especially avoid 14, 24 and 514 at the end.</li><li><b>Patterns:</b> AABB (6688), ABAB (1818) and triple repeats (888) are easy to remember.</li><li><b>Reading:</b> on the phone, 1 is read <i>yāo</i> (幺), so 18 sounds like 要发 “will prosper”.</li></ul>
<h2>Choosing a business number</h2><p>Pick a line where the last 4 digits score 80+ and avoid 4. For a phrase number, consider 518 (“I will prosper”) or 1688.</p>''',
  [("Which part of a phone number matters most?","The last four digits — they are what people remember and what Chinese buyers judge first."),
   ("Is 4 always bad in a phone number?","For most Mandarin and Cantonese speakers yes, particularly as the final digit. Teochew speakers may see it as lucky."),
   ("Can you help me find a lucky number?","Yes — request a business number selection in the free report form.")],
  "Phone Number Luck Checker — Is My Mobile Number Lucky in Chinese? | 345789",
  "Free lucky phone number checker. Score your mobile or business number with Chinese numerology, final-four weighting, combos like 1688 and the 4 warning.",
  "lucky phone number china", "机", need="business-number")

# ---------- 3 plate
tool_page("tools/license-plate-luck.html", "License Plate Luck Checker", "车 Vehicle plates",
  "See how your plate reads to a Chinese speaker — and why plates with an 8 sell for multiples at Hong Kong auctions.",
  analyser("plate", "e.g. AB 2828 or 168", label="Plate number (letters are ignored)"),
  '''<h2>The plate economy</h2><p>Hong Kong's Transport Department auctions registration marks, and numbers carry enormous premiums: “28” sold for HK$18.1M in 2016 and “9” for HK$13M in 1994. A 2024–25 study of 1,067 auctions found an 8 lifts a plate's value by roughly 65%.</p>
<h2>Plate-reading rules</h2><ul><li>Short is premium: 1–2 digits beat long plates.</li><li>8, 6, 9 and 2 add value; 4 subtracts.</li><li>Pairs like 28 (易发), 68 (路发) and 88 (发发) carry extra premiums.</li></ul>
<h2>Regions</h2><p><b>Hong Kong:</b> regular TD auctions plus personalised plates. <b>Singapore:</b> LTA bidding with a minimum bid, plus a secondary market. <b>Malaysia &amp; mainland China:</b> special-number bidding systems. Check local rules before buying or selling.</p>''',
  [("Why are plates with 8 so expensive?","8 sounds like 发 'prosper'. Auction research measures a large premium for every 8 on a plate."),
   ("Can I sell my lucky plate here?","List it free in our marketplace; transfers must follow your local transport authority's rules."),
   ("Do letters matter?","In Chinese numerology we read the digits. Letters can carry their own meaning (e.g. initials) but aren't scored.")],
  "License Plate Luck Checker — Lucky Car Plate Numbers in Chinese Culture | 345789",
  "Check if your car plate number is lucky in Chinese culture. Learn why plates with 8 sell at huge premiums in Hong Kong and Singapore auctions.",
  "hong kong license plate auction", "车", need="sell-asset")

# ---------- 4 house
tool_page("tools/house-number-luck.html", "House & Floor Number Checker", "宅 Address · unit · floor",
  "Score a street address, apartment unit or floor before you buy or rent — the way Chinese buyers do.",
  analyser("house", "e.g. 1688 or unit 2808", label="House, unit or floor number"),
  '''<h2>Addresses move prices</h2><p>In Greater Vancouver, homes whose address ended in 4 sold at a 2.2% discount and those ending in 8 at a 2.5% premium in Chinese-majority neighbourhoods. In Chengdu, apartments on 8-ending floors sold for about 235 RMB/m² more.</p>
<h2>The skip-4 rule</h2><p>Many towers in Hong Kong, China, Singapore, Taiwan and Chinese-Canadian communities skip floors 4, 14, 24 and sometimes all of 40–49. Some also skip 13 for Western buyers.</p>
<h2>Feng shui tips</h2><ul><li>Add the digits (e.g. 1688 → 23 → 5) for a single “house number” many feng shui schools use.</li><li>A 4-address is often “fixed” by adding a letter (12A) or using the Teochew reading.</li><li>Pair the number with your <a href="{R}tools/personal-lucky-numbers.html">Kua directions</a>.</li></ul>''',
  [("Should I avoid buying a house with a 4?","If you may sell to Chinese buyers, data suggests a small discount. If the property is right, many owners simply use a unit letter."),
   ("Why do buildings skip the 4th floor?","Because 4 sounds like 'death'. Developers relabel floors to protect sale prices."),
   ("Is 8 always good for an address?","Yes in most readings; 88, 168 and 1688 are especially popular.")],
  "House Number Luck — Is My Address or Floor Number Lucky? (Chinese Feng Shui) | 345789",
  "Check if a house, apartment unit or floor number is lucky in Chinese culture and feng shui. Research on the 4 discount and 8 premium included.",
  "feng shui house number", "宅")

# ---------- 5 domain
tool_page("tools/numeric-domain-valuer.html", "Numeric Domain Valuer", "域 6N · 5N · 4N",
  "Tier any all-numeric domain for the Chinese market — length, no-4, 8-count, patterns — with historical reference ranges.",
  '<div class="analyser" id="domain-tool"><form novalidate><label for="dom-in">Numeric domain</label><div class="an-row"><input id="dom-in" class="big-input" placeholder="e.g. 345789.com" autocomplete="off"><button class="btn btn-p" type="submit">Value it</button></div></form><div class="result" aria-live="polite"></div></div>',
  '''<h2>Why numeric domains are a Chinese-market asset</h2><p>Pinyin is hard to type and English words are foreign to many users, so short number domains act as brand names in China (think of sites named after number strings). Industry interviews estimate around <b>80% of numeric-domain buyers are Chinese</b>.</p>
<h2>The valuation rules</h2><table><tr><th>Factor</th><th>Effect</th></tr><tr><td>Length</td><td>2N &gt; 3N &gt; 4N &gt; 5N &gt; 6N — each extra digit sharply cuts value</td></tr><tr><td>Digit 4</td><td>Dealers cite up to −50%</td></tr><tr><td>Digit 8</td><td>More 8s, more buyers</td></tr><tr><td>Leading 0</td><td>Discount</td></tr><tr><td>Patterns</td><td>AABB, ABAB, ABBA, AAAA, ABCABC add premium</td></tr><tr><td>Extension</td><td>.com first; .cn, .net and .cc a distant second</td></tr></table>
<h2>Reference points</h2><ul><li>6N .com: mostly tens to low hundreds of USD; 888-ending 6Ns have sold near US$7k.</li><li>5N .com: wholesale floor near US$100 in 2023; patterned 5Ns can top US$4k.</li><li>4N and 3N .com: thousands to tens of thousands of USD and up, much more for “Chinese-premium” digits.</li></ul>
<p class="small muted">Prices are historical reference points, not a guarantee; markets move. See the <a href="{R}guides/numeric-domain-investing.html">numeric domain investing guide</a> for sources.</p>''',
  [("Is this an appraisal?","No — it's an indicative tier. For a real estimate, request a free pro valuation using comparable sales."),
   ("What is a 'Chinese-premium' number?","A number using only digits Chinese buyers like — usually no 4 and often no 7 — such as 8, 6, 9, 5, 3, 2, 1, 0."),
   ("Can you sell my numeric domain?","List it free in the marketplace or request broker introductions through the report form.")],
  "Numeric Domain Valuer — 6N, 5N, 4N .com Value for the Chinese Market | 345789",
  "Free numeric domain valuation tool: tier any number domain by length, no-4, 8-count and pattern (AABB, ABAB) with reference prices for 4N, 5N and 6N .com.",
  "numeric domain names investing", "域", need="domain-valuation")

# ---------- 6 almanac
tool_page("tools/lucky-date-finder.html", "Lucky Date Finder — Chinese Almanac", "历 Tong Shu 2026–2028",
  "Find auspicious days for a wedding, moving house, opening a business or signing a contract, using traditional Chinese Almanac (通书) rules.",
  '''<div class="analyser" id="almanac-tool"><div class="row form" style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
<div><label for="alm-purpose">Purpose</label><select id="alm-purpose"><option value="">All days</option><option value="嫁娶|结婚姻|纳采">Wedding / engagement</option><option value="搬移|入宅">Moving house</option><option value="开市|开张">Opening a business</option><option value="立券交易|立券|纳财">Signing contracts &amp; trading</option><option value="出行">Travel</option><option value="修造|破土|营建">Renovation / groundbreaking</option><option value="求医疗病">Seeing a doctor</option><option value="祈福">Praying for blessings</option></select></div>
<div><label for="alm-month">Month</label><div class="an-row"><button class="btn btn-o btn-sm" id="alm-prev" type="button" aria-label="Previous month">‹</button><select id="alm-month"></select><button class="btn btn-o btn-sm" id="alm-next" type="button" aria-label="Next month">›</button></div></div></div>
<p id="alm-summary" class="small" style="margin:12px 0"></p><div id="alm-grid" class="cal" aria-label="Calendar"></div><div id="alm-detail" style="margin-top:16px"></div>
<p class="small muted" style="margin-top:10px">Each cell shows the lunar month/day. Green = traditionally favourable; faded = poor. Tradition &amp; entertainment.</p></div>''',
  '''<h2>What is the Chinese Almanac?</h2><p>The Tong Shu (通书), also called the Huang Li (黄历), is a centuries-old calendar used across Chinese communities to choose days for weddings, moves, openings, travel and ceremonies. Each day has a lunar date, a stem-branch “day pillar”, a clashing zodiac animal, a list of favourable activities (宜) and activities to avoid (忌).</p>
<h2>How to use it</h2><ol><li>Choose a purpose to outline the best days in gold.</li><li>Click a day to see the lunar date, clash animal and the full do/avoid list.</li><li>Avoid days that clash with the birth animal of the people involved.</li><li>Many families also avoid the 7th lunar month (Ghost Month) for weddings and moves.</li></ol>
<h2>Popular uses</h2><ul><li><b>Weddings:</b> look for 嫁娶 (marriage) on a good-quality day.</li><li><b>Business openings:</b> 开市 / 开张.</li><li><b>Moving in:</b> 入宅 and 搬移.</li><li><b>Contracts:</b> 立券交易.</li></ul>''',
  [("How accurate is this almanac?","It follows standard Tong Shu rules (day officers, stars, clash animals). Different almanac schools can disagree on some days."),
   ("Which dates are best for a wedding?","Days marked favourable for 嫁娶 with good day quality and no clash with the couple's birth animals."),
   ("Why do some days say 'avoid major events'?","Traditional rules mark certain days (e.g. 月破, 四离, 四绝) as unsuitable for most major activities.")],
  "Lucky Date Finder — Chinese Almanac (Tong Shu) Auspicious Days 2026–2028 | 345789",
  "Find auspicious dates for weddings, moving house, business openings and contracts with the Chinese Almanac (Tong Shu/Huang Li), 2026 to 2028, in English.",
  "chinese wedding date selection", "历", need="date-selection")

# ---------- 7 zodiac
tool_page("tools/chinese-zodiac-calculator.html", "Chinese Zodiac Calculator", "龙 1900–2100",
  "Find your true zodiac animal using the exact Lunar New Year date for your birth year — plus element, lucky numbers, colours and matches.",
  '<div class="analyser" id="zodiac-tool"><form novalidate><label for="z-in">Date of birth</label><div class="an-row"><input id="z-in" type="date" min="1900-01-31" max="2100-12-31" required><button class="btn btn-p" type="submit">Find my sign</button></div></form><div class="result" aria-live="polite"></div></div>',
  '''<h2>Why your birth date matters, not just the year</h2><p>The zodiac year begins at Lunar New Year, which falls between 21 January and 20 February. If you were born in January or early February, you may belong to the previous year's animal. This calculator checks the exact date for every year from 1900 to 2100.</p>
<h2>The twelve animals</h2><table><tr><th>Animal</th><th>Lucky numbers</th><th>Unlucky</th></tr>
<tr><td>Rat 鼠</td><td>2, 3</td><td>5, 9</td></tr><tr><td>Ox 牛</td><td>1, 4</td><td>5, 6</td></tr><tr><td>Tiger 虎</td><td>1, 3, 4</td><td>6, 7, 8</td></tr><tr><td>Rabbit 兔</td><td>3, 4, 6</td><td>1, 7, 8</td></tr><tr><td>Dragon 龙</td><td>1, 6, 7</td><td>3, 8</td></tr><tr><td>Snake 蛇</td><td>2, 8, 9</td><td>1, 6, 7</td></tr><tr><td>Horse 马</td><td>2, 3, 7</td><td>1, 5, 6</td></tr><tr><td>Goat 羊</td><td>3, 4, 9</td><td>6, 7, 8</td></tr><tr><td>Monkey 猴</td><td>4, 9</td><td>2, 7</td></tr><tr><td>Rooster 鸡</td><td>5, 7, 8</td><td>1, 3, 9</td></tr><tr><td>Dog 狗</td><td>3, 4, 9</td><td>1, 6, 7</td></tr><tr><td>Pig 猪</td><td>2, 5, 8</td><td>1, 7</td></tr></table>
<p class="small muted">Lucky and unlucky digits per animal as commonly listed in popular Chinese astrology references; schools vary.</p>
<h2>2026 and 2027</h2><p>2026 is the year of the Fire Horse (from 17 February 2026); 2027 is the Fire Goat (from 6 February 2027).</p>''',
  [("When does the zodiac year start?","At Lunar New Year (between Jan 21 and Feb 20). Feng shui calculations instead use Li Chun, around Feb 4."),
   ("What is my element?","It follows the last digit of the zodiac year: 0–1 Metal, 2–3 Water, 4–5 Wood, 6–7 Fire, 8–9 Earth."),
   ("Is the Ox's lucky number really 4?","Yes, several astrology references list 1 and 4 for the Ox — a reminder that 'unlucky 4' is not universal.")],
  "Chinese Zodiac Calculator — Find Your Animal, Element & Lucky Numbers (Exact Lunar New Year) | 345789",
  "Free Chinese zodiac calculator with exact Lunar New Year dates 1900-2100. Find your animal, element, yin/yang, lucky numbers, colours and best matches.",
  "chinese zodiac explained", "龙")

# ---------- 8 personal
tool_page("tools/personal-lucky-numbers.html", "Personal Lucky Numbers & Kua", "卦 Feng shui",
  "Your zodiac lucky digits, your Kua (Gua) number and the four directions traditionally best for your desk, bed and front door.",
  '<div class="analyser" id="lucky-tool"><form novalidate class="form"><div class="row"><div><label for="p-d">Date of birth</label><input id="p-d" type="date" required min="1900-01-01" max="2100-12-31"></div><div><label for="p-g">Gender (Kua formula)</label><select id="p-g"><option value="f">Female</option><option value="m">Male</option></select></div></div><button class="btn btn-p" type="submit">Reveal my numbers</button></form><div class="result" aria-live="polite" style="margin-top:14px"></div></div>',
  '''<h2>What is a Kua number?</h2><p>In Eight Mansions (八宅) feng shui, your Kua number (1–9, never 5) is calculated from your birth year and gender. It places you in the East group (1, 3, 4, 9) or West group (2, 6, 7, 8) and gives four favourable directions:</p>
<ul><li><b>Sheng Qi 生气</b> — success and wealth</li><li><b>Tian Yi 天医</b> — health</li><li><b>Yan Nian 延年</b> — relationships</li><li><b>Fu Wei 伏位</b> — personal growth</li></ul>
<h2>How to use your directions</h2><p>Face your best direction at your desk, point the head of your bed toward a favourable direction and, where possible, choose a front door in your group. Use the year starting at Li Chun (about 4 February).</p>''',
  [("Why does gender matter?","The traditional Kua formula differs for men and women. We offer both; choose the one you identify with."),
   ("Why is there no Kua 5?","Kua 5 becomes 2 for men and 8 for women in the traditional system."),
   ("Are these directions scientific?","They're a traditional practice — use them as cultural guidance.")],
  "Personal Lucky Numbers & Kua Number Calculator — Lucky Directions (Feng Shui) | 345789",
  "Calculate your personal Chinese lucky numbers, Kua (Gua) number and four lucky feng shui directions from your birth date.",
  "kua number feng shui", "卦")

# ---------- 9 converter
tool_page("tools/chinese-number-converter.html", "Chinese Number Converter", "壹 中文 · 大写 · pinyin",
  "Convert any number to Chinese characters, financial (cheque) characters, pinyin and Cantonese — and see its luck reading.",
  '<div class="analyser" id="converter-tool"><form novalidate><label for="c-in">Number (up to 16 digits)</label><div class="an-row"><input id="c-in" class="big-input" inputmode="numeric" maxlength="20"><button class="btn btn-p" type="submit">Convert</button></div></form><div class="result" aria-live="polite" style="margin-top:14px"></div></div>',
  '''<h2>Three ways to write a number in Chinese</h2><table><tr><th>Style</th><th>Example (345,789)</th><th>Used for</th></tr><tr><td>Arabic</td><td>345789</td><td>Everyday</td></tr><tr><td>Lower-case 小写</td><td class="zh">三十四万五千七百八十九</td><td>Text, speech</td></tr><tr><td>Financial 大写</td><td class="zh">叁拾肆万伍仟柒佰捌拾玖</td><td>Cheques, invoices, contracts — hard to forge</td></tr></table>
<h2>Big numbers group by 10,000</h2><p>Chinese counts in units of 万 (10,000) and 亿 (100 million), not thousands. So 345,789 is 34万5789 — “thirty-four ten-thousands, five thousand…”.</p>
<h2>Phone-style reading</h2><p>When reading digits one by one, 1 is usually <i>yāo</i> (幺) to avoid confusion with 7 (<i>qī</i>).</p>''',
  [("What is 大写 used for?","Financial documents — the complex characters can't be altered as easily as 一 or 二."),
   ("How do you say 345789 in Chinese?","Sān shí sì wàn wǔ qiān qī bǎi bā shí jiǔ (三十四万五千七百八十九), or digit by digit: sān sì wǔ qī bā jiǔ."),
   ("Does it handle zeros correctly?","Yes — internal zeros become 零 once per gap, following standard rules.")],
  "Chinese Number Converter — Numbers to Chinese Characters, 大写 & Pinyin | 345789",
  "Convert numbers to Chinese characters (小写), financial/cheque characters (大写), pinyin and Cantonese Jyutping, with a lucky-number reading.",
  "learn chinese numbers", "九")
