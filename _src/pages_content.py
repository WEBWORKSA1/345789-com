from components import *

PAGES = []

DIG = [
 (0,"零","líng","ling4","良 good · 圆 completeness",["Completeness and the beginning of all things","Trailing zeros look 'round' and prestigious — 8000, 1000","A leading zero reads as 'nothing first' and is discounted in numeric domains"],["8000 — big round prosperity","10 — 十全十美 'perfect in every way'"]),
 (1,"一","yī / yāo","jat1","要 will/want · first place",["Unity, leadership and being first","In combos often read yāo, heard as 要 'will' — 18 = 'will prosper'","Alone it can suggest being single: Singles' Day is 11/11"],["168 一路发 prosperity all the way","1314 一生一世 forever"]),
 (2,"二 / 两","èr / liǎng","ji6","双 pairs · 易 easy (Cantonese)",["Good things come in pairs — 好事成双","Cantonese 2 sounds like 易 'easy'","Avoid 250 (二百五), a classic insult"],["28 易发 easy prosperity","520 我爱你 I love you"]),
 (3,"三","sān","saam1","生 life · 散 scatter",["Cantonese: 生 life, birth, growth","Mandarin can hear 散 'to break apart'","Heaven, earth and humanity — a classical triad"],["3344 生生世世 life after life","38 生发 growth and wealth (Cantonese)"]),
 (4,"四","sì","sei3","死 death",["The most avoided digit in China, Hong Kong, Taiwan, Singapore, Japan, Korea and Vietnam","Buildings skip 4th, 14th and 24th floors","In Teochew culture 4 echoes 喜 'happiness' and is lucky; the Ox's lucky numbers include 4"],["14 要死 will die","514 我要死 I want to die","54 唔死 won't die (Cantonese — lucky!)"]),
 (5,"五","wǔ","ng5","吾/我 me · 无 none · 五行 Five Elements",["Balance — the Five Elements and five directions","In combos 5 often means 'I' — 518 'I will prosper'","In Cantonese 5 (ng) can mean 'not', flipping a phrase"],["518 我要发 I will prosper","520 我爱你 I love you"]),
 (6,"六","liù","luk6","顺 smooth · 禄 fortune",["六六大顺 — everything goes smoothly","Cantonese 6 sounds like 禄 'fortune/salary'","666 is internet slang for 'awesome'"],["66 smooth all the way","68 路发 road to fortune"]),
 (7,"七","qī","cat1","起 rise · 齐 together · 气 energy",["Togetherness: Qixi (7/7) is Chinese Valentine's Day","Heard as 起 'to rise'","7th lunar month is Ghost Month; 74 'angry to death'"],["78 起发 rise to prosperity","789 起发久 rise, prosper, endure"]),
 (8,"八","bā","baat3","发 prosper",["The luckiest digit — 发 'to prosper, get rich'","88 looks like 囍 double happiness","Beijing Olympics opened 8/8/08 at 8:08:08 pm"],["168 一路发","888 发发发","518 我要发"]),
 (9,"九","jiǔ","gau2","久 long-lasting",["Longevity and lasting love — popular for weddings","The emperor's number — the highest single digit","9 roses or 99 roses for eternal love"],["99 久久 forever","1314/9999 eternal"]),
]

# --- meanings index
cards = "".join(f'<a class="card center reveal" href="{{R}}meanings/number-{d}.html"><div style="font-size:2.6rem;font-weight:800{";color:var(--red)" if d==4 else ""}">{d}</div><div class="zh" style="font-size:1.3rem">{zh}</div><p>{snd}</p></a>' for d,zh,py,jp,snd,_,_ in DIG)
PAGES.append(dict(path="meanings/index.html", prio="0.9", crumbs=[("Meanings","meanings/index.html")],
 title="Chinese Number Meanings 0–9 & 50+ Lucky and Unlucky Combinations | 345789",
 desc="The meaning of every digit 0-9 in Chinese culture plus a searchable dictionary of 50+ number combinations: 168, 518, 520, 1314, 14, 514, 748 and more.",
 faq=[("What does 520 mean in Chinese?","520 (wǔ èr líng) sounds like 我爱你 'I love you'. May 20 is an unofficial Valentine's Day in China."),("What does 1314 mean?","一生一世 'one life, one lifetime' — forever. 5201314 means 'I love you forever'.")],
 body=hero("Chinese number meanings", "Every digit is a sound, every sound a word. Start with a digit or search the combination dictionary.", "0–9 · 50+ combos") +
 f'<div class="wrap"><div class="grid g4" style="grid-template-columns:repeat(auto-fill,minmax(150px,1fr))">{cards}</div>{ad()}'
 '<div class="card" id="combo-search" style="margin-top:20px"><h2>Combination dictionary</h2><div class="an-row" style="flex-wrap:wrap"><input placeholder="Search 168, love, death…" aria-label="Search combinations" style="flex:1;min-width:200px"><div class="seg" data-seg><button type="button" class="on" data-v="all">All</button><button type="button" data-v="lucky">Lucky</button><button type="button" data-v="unlucky">Unlucky</button></div></div>'
 '<div class="tbl-wrap"><table class="tbl" id="combo-table"><thead><tr><th>Number</th><th>Reads as</th><th>Meaning</th><th>Verdict</th></tr></thead><tbody></tbody></table></div></div>'
 '<div class="narrow" style="margin-top:30px">' + faq_html([("What does 520 mean in Chinese?","520 (wǔ èr líng) sounds like 我爱你 'I love you'. May 20 is an unofficial Valentine's Day in China."),("What does 1314 mean?","一生一世 'one life, one lifetime' — forever. 5201314 means 'I love you forever'.")]) + '</div></div>'))

for d,zh,py,jp,snd,pts,combos in DIG:
    prev_, next_ = (d-1)%10, (d+1)%10
    verdict = {4:"Unlucky (with exceptions)",8:"Most lucky",6:"Lucky",9:"Lucky",2:"Lucky",0:"Mildly lucky",1:"Neutral",3:"Mixed",5:"Neutral",7:"Mixed"}[d]
    body = hero(f'Number {d} <span class="zh">{zh}</span> — meaning in Chinese culture', f'Pronounced <i>{py}</i> (Cantonese <i>{jp}</i>), {d} sounds like {snd}. Verdict: <b>{verdict}</b>.', f'Digit {d}') + with_side(
      f'<div class="digits-band"><b class="{"warn" if d==4 else "hot" if d in (6,8,9) else ""}">{d}<i>{zh.split(" ")[0]}</i></b></div>'
      f'<h2 style="margin-top:36px">What {d} means</h2><ul>' + "".join(f"<li>{p}</li>" for p in pts) + '</ul>'
      f'<h2>Popular combinations with {d}</h2><ul>' + "".join(f"<li>{c}</li>" for c in combos) + '</ul>' + ad() +
      f'<h2>Check a number with {d}</h2>' + analyser("any", f"Try a number with {d}", demo=str(d)*3 if d!=4 else "514", dialects=True, big=False) +
      f'<h2>Using {d} in real life</h2><p>{"Avoid it at the end of phone numbers, plates and prices; if you are stuck with it, a unit letter or the Teochew reading softens it." if d==4 else "Put it at the end of phone numbers, prices, plates and dates for the strongest effect." if d in (6,8,9) else "Its meaning depends on its neighbours — check combinations before choosing."}</p>'
      f'<p><a href="{{R}}meanings/number-{prev_}.html">← Number {prev_}</a> · <a href="{{R}}meanings/index.html">All numbers</a> · <a href="{{R}}meanings/number-{next_}.html">Number {next_} →</a></p>' + author())
    PAGES.append(dict(path=f"meanings/number-{d}.html", article=True, modal=True, crumbs=[("Meanings","meanings/index.html"),(f"Number {d}",f"meanings/number-{d}.html")],
      title=f"Number {d} Meaning in Chinese ({zh}) — Lucky or Unlucky? | 345789",
      desc=f"What does {d} mean in Chinese culture? {d} ({zh}, {py}) sounds like {snd.split(' · ')[0]}. Meanings, combinations, dialect differences and a free checker.", body=body))

# --- guides
GUIDES = [
 ("angel-numbers-vs-chinese-lucky-numbers","Angel Numbers vs Chinese Lucky Numbers: 111, 444, 888 Compared","Western 'angel numbers' and Chinese lucky numbers often disagree — 444 is a 'protection' sign in one and a triple death in the other.",
  '''<p>“Angel numbers” — repeating sequences like 111, 222 or 444 — are a fast-growing Western spiritual trend, with search interest concentrated among young women. Chinese number luck is far older and rooted in sound, not symbolism. The two systems often clash.</p>
<h2>Side by side</h2><table><tr><th>Number</th><th>Angel-number reading</th><th>Chinese reading</th></tr>
<tr><td>111</td><td>New beginnings, manifestation</td><td>Neutral; 1 = 'will' in combos</td></tr>
<tr><td>222</td><td>Balance, partnership</td><td>Positive — pairs, 'easy' in Cantonese</td></tr>
<tr><td>333</td><td>Growth, ascended masters</td><td>Mixed — 生 life / 散 scatter</td></tr>
<tr><td>444</td><td>Protection, angels nearby</td><td><b>Very negative</b> — 死死死</td></tr>
<tr><td>555</td><td>Big change</td><td>Internet slang for crying (呜呜呜)</td></tr>
<tr><td>666</td><td>Imbalance (often feared)</td><td><b>Very positive</b> — 六六大顺, slang 'awesome'</td></tr>
<tr><td>777</td><td>Luck, spiritual alignment</td><td>Mixed — rise/together vs Ghost Month</td></tr>
<tr><td>888</td><td>Abundance</td><td><b>Very positive</b> — 发发发</td></tr>
<tr><td>999</td><td>Endings, completion</td><td><b>Positive</b> — 久久久, everlasting</td></tr></table>
<h2>Why they differ</h2><p>Angel numbers assign meaning to patterns; Chinese luck comes from homophones. That's why 666 — feared in Western culture — is celebrated in China, and why 444 flips from comforting to alarming.</p>
<h2>Which should you use?</h2><p>For anything that will be seen by Chinese-speaking customers, partners or buyers — prices, phone numbers, addresses, product codes — the Chinese reading has measurable market effects. For personal reflection, use whichever resonates with you.</p>'''),
 ("why-4-is-unlucky","Why Is 4 Unlucky in Chinese Culture? (And Where It's Lucky)","Tetraphobia explained: the death homophone, missing floors, measured price discounts — and the cultures that love 4.",
  '''<p>Four (四, <i>sì</i>) sounds almost exactly like death (死, <i>sǐ</i>). In Cantonese the two are nearly identical (<i>sei3</i> vs <i>sei2</i>). This fear of four — tetraphobia — is shared in Japan and Korea (where 4 is also read <i>shi/sa</i>) and Vietnam.</p>
<h2>Where you'll see it</h2><ul><li><b>Buildings:</b> floors 4, 14, 24 and sometimes 40–49 skipped; one Hong Kong tower labels its top floor 88.</li><li><b>Hospitals and hotels:</b> rooms ending in 4 avoided.</li><li><b>Products:</b> some phone and car makers skip model numbers with 4 in Asian markets.</li><li><b>Gifts:</b> sets of four items are avoided.</li></ul>
<h2>What it costs</h2><p>Vancouver homes with addresses ending in 4 sold at a 2.2% discount in Chinese-majority areas (2000–2005). Numeric-domain dealers say a single 4 can cut a domain's Chinese-market value by up to half.</p>
<h2>Where 4 is lucky</h2><ul><li><b>Teochew (潮州) culture:</b> 4 sounds like 喜 'happiness' or 丝 'silk'; red packets and oranges are given in fours.</li><li><b>Cantonese 54:</b> 唔死 'won't die'.</li><li><b>Zodiac:</b> popular astrology tables list 4 as lucky for the Ox, Tiger, Rabbit, Goat, Monkey and Dog.</li><li><b>Classical Chinese:</b> four seasons, four directions, four treasures of the study.</li></ul>
<h2>Living with a 4</h2><p>Add a letter (14A), use the Teochew reading, or pair it with 8: in Cantonese a 4 followed by 8 can read as 世发 'prosper for generations'. Test yours in the <a href="{R}tools/number-meaning-analyzer.html?n=48">analyzer</a>.</p>'''),
 ("economics-of-8","The Economics of 8: How a Lucky Number Moves Real Prices","From HK$18M plates to Olympic start times — the measured premium of the number 8.",
  '''<p>Eight (八, <i>bā</i>) rhymes with 发 (<i>fā</i>), 'to prosper'. That single homophone has become one of the most valuable sounds on earth.</p>
<h2>The evidence</h2><ul><li><b>Plates:</b> an 8 adds ~65% to a Hong Kong plate's auction price (2024–25 data). Plate “28” sold for HK$18.1M.</li><li><b>Homes:</b> Vancouver addresses ending in 8 carried a 2.5% premium in Chinese-majority neighbourhoods.</li><li><b>Apartments:</b> Chengdu floors ending in 8 sold for ~235 RMB/m² more.</li><li><b>Phones:</b> 8888-8888 sold for ¥2.33M in 2003.</li></ul>
<h2>8 in business</h2><ul><li>Prices ending in 8 (¥88, $188) in Chinese retail.</li><li>Grand openings on the 8th, 18th or 28th.</li><li>Airlines use flight numbers like 888 on China routes.</li><li>The Beijing Olympics: 8/8/08, 8:08:08 pm.</li></ul>
<h2>How to use 8</h2><p>End on it, double it (88), or phrase it (168, 518, 1688). Check your idea in the <a href="{R}tools/number-meaning-analyzer.html?n=1688">analyzer</a>.</p>'''),
 ("lucky-wedding-dates","How to Choose a Lucky Chinese Wedding Date","A step-by-step guide to almanac-approved wedding dates: 嫁娶 days, clash animals, Ghost Month and lucky numbers.",
  '''<p>Picking the date (择日) is one of the most important steps of a Chinese wedding. Families traditionally consult the almanac or a master.</p>
<h2>Step 1 — Avoid the obvious</h2><ul><li>The 7th lunar month (Ghost Month).</li><li>Days that clash with the bride's or groom's birth animal.</li><li>Dates heavy in 4s (e.g. the 4th, 14th, 24th).</li></ul>
<h2>Step 2 — Look for 嫁娶</h2><p>Use the <a href="{R}tools/lucky-date-finder.html">Lucky Date Finder</a>, choose “Wedding”, and pick gold-outlined days of good quality.</p>
<h2>Step 3 — Add number luck</h2><p>Many couples like dates with 8, 9 (久, lasting) or meaningful combos — 5/20 (我爱你), 2/14 in Western style, or 9/9 for longevity.</p>
<h2>Step 4 — Confirm with family</h2><p>Families may follow different almanac schools. Share a shortlist and let elders choose.</p>
<p>Want a shortlist made for you? <a href="{R}get-your-report.html?need=date-selection">Request a free date selection</a>.</p>'''),
 ("lucky-business-phone-number","Choosing a Lucky Business Phone Number","How Chinese businesses pick phone numbers — last-four rules, golden numbers and costly mistakes.",
  '''<p>For customers who read numbers as words, your phone number is part of your brand. Telecoms across Greater China sell premium 'golden numbers' (靓号) for this reason.</p>
<h2>Rules that matter</h2><ol><li><b>Judge the last four digits first.</b></li><li><b>No 4 in the last four</b> — especially 14, 24, 54 (Mandarin) or 514.</li><li><b>End on 8, 6 or 9.</b></li><li><b>Prefer patterns:</b> 6688, 1818, 8888.</li><li><b>Consider a phrase:</b> 1688 'prosper all the way', 518 'I will prosper'.</li></ol>
<h2>Mistakes to avoid</h2><ul><li>250 anywhere (an insult).</li><li>748 / 7414 ('go die').</li><li>Descending runs (… 9876), read as 'going downhill'.</li></ul>
<h2>Test before you buy</h2><p>Paste candidates into the <a href="{R}tools/phone-number-luck.html">Phone Number Luck Checker</a> — or ask us to shortlist numbers for your business.</p>'''),
 ("numeric-domain-investing","Numeric Domain Investing 101: 6N, 5N, 4N and the Chinese Market","How number domains are valued, why 4 kills value, and what 6N, 5N and 4N .com names have sold for.",
  '''<p>Numeric domains are a niche where culture directly sets price. Industry interviews estimate roughly 80% of buyers are Chinese, because numbers work as brand names across language barriers.</p>
<h2>The classes</h2><table><tr><th>Class</th><th>Count</th><th>Reference prices (historical)</th></tr><tr><td>2N .com</td><td>100</td><td>Ultra-rare; six to seven figures</td></tr><tr><td>3N .com</td><td>1,000</td><td>Tens of thousands of USD+ for no-4 names</td></tr><tr><td>4N .com</td><td>10,000</td><td>Low thousands and up; premium digits far more</td></tr><tr><td>5N .com</td><td>100,000</td><td>Wholesale floor ~US$100 (2023); patterned US$4k+</td></tr><tr><td>6N .com</td><td>1,000,000</td><td>Most tens–low hundreds; 888-endings near US$7k</td></tr></table>
<h2>The value drivers</h2><ul><li><b>No 4</b> (dealers cite up to −50% with a 4).</li><li><b>More 8s</b>, then 6 and 9.</li><li><b>No leading zero.</b></li><li><b>Patterns</b>: AAAA, AABB, ABAB, ABBA, ABCABC.</li><li><b>Meaning</b>: 5201314, 168, 518.</li></ul>
<h2>Where they trade</h2><p>Western marketplaces and auction houses plus Chinese platforms such as Juming, eName and 4.cn; prices often differ between the two markets. Always use escrow.</p>
<h2>Monetising instead of selling</h2><p>Developing a numeric domain into a content or tool site (like this one) or offering vanity email addresses can earn while you hold.</p>
<p>Value a name with the <a href="{R}tools/numeric-domain-valuer.html">Numeric Domain Valuer</a> or <a href="{R}marketplace.html#sell">list it free</a>.</p>
<h3>Sources</h3><ul class="small"><li><a href="https://domainsherpa.com/giuseppe-graziano-numeric-domains-interview/" target="_blank" rel="noopener">DomainSherpa — numeric domains interview</a></li><li><a href="https://domainnamewire.com/2015/09/17/expired-domain-report-what-are-6-digit-domains-worth/" target="_blank" rel="noopener">Domain Name Wire — what are 6-digit domains worth</a></li><li><a href="https://www.namepros.com/threads/the-chinese-domain-market-a-complete-guide-for-western-investors-2026-edition.1384515/" target="_blank" rel="noopener">NamePros — Chinese domain market guide</a></li></ul>'''),
]
gcards = "".join(f'<a class="card reveal" href="{{R}}guides/{slug}.html"><span class="badge">Guide</span><h3 style="margin-top:8px">{t}</h3><p>{d}</p></a>' for slug,t,d,_ in GUIDES)
PAGES.append(dict(path="guides/index.html", prio="0.8", crumbs=[("Guides","guides/index.html")],
  title="Guides — Lucky Numbers, Wedding Dates, Business Numbers & Numeric Domains | 345789",
  desc="In-depth guides on Chinese lucky numbers: angel numbers vs Chinese meanings, why 4 is unlucky, the economics of 8, wedding dates, business phone numbers and numeric domain investing.",
  body=hero("Guides", "Deep dives that turn culture into decisions.", "📚 Learn") + f'<div class="wrap"><div class="grid g3">{gcards}</div>{ad()}</div>'))
for slug,t,d,content in GUIDES:
    toc = "".join(f'<li>{h}</li>' for h in __import__("re").findall(r"<h2>(.*?)</h2>", content))
    PAGES.append(dict(path=f"guides/{slug}.html", article=True, modal=True, crumbs=[("Guides","guides/index.html"),(t.split(":")[0],f"guides/{slug}.html")],
      title=f"{t} | 345789", desc=d,
      body=hero(t, d, "Guide") + with_side(f'<div class="meta"><span>By 345789 Editorial Team</span><span>Updated October 2026</span><span>~6 min read</span><button class="btn btn-sm btn-o" data-share>Share</button></div><div class="toc" style="margin:18px 0"><b>Contents</b><ol>{toc}</ol></div>' + content.replace("<h2>", ad() + "<h2>", 1) + ad() + author())))
