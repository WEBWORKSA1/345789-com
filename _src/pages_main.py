from components import *

PAGES = []
def add(**k): PAGES.append(k)

# ------------------------------------------------------------------ HOME
add(path="index.html", prio="1.0", modal=True,
title="345789 · The Lucky Number Lab — Chinese Lucky Number Analyzer, Meanings & Tools",
desc="Free Chinese lucky-number tools: analyse any phone, plate, house or domain number, find lucky dates in the Chinese Almanac, zodiac lucky numbers and the meaning of every digit.",
faq=[("Which numbers are lucky in Chinese culture?","8 (发, prosper) is the luckiest, followed by 6 (smooth), 9 (long-lasting) and 2 (pairs). Combos like 168, 518 and 888 are prized."),
     ("Why is 4 unlucky?","4 (sì) sounds almost exactly like 死 (sǐ), 'death', so many buildings skip 4th floors and buyers discount addresses ending in 4."),
     ("Is 345789 a lucky number?","It scores about 64/100 (吉, auspicious): the 7-8-9 finish reads 起发久 'rise, prosper, endure' and the run ascends, but the 4 costs points.")],
body='''
<section class="hero"><div class="wrap hero-grid">
<div>
<span class="eyebrow">三四五七八九 · sān sì wǔ qī bā jiǔ</span>
<h1 style="margin-top:14px">Decode the <span>luck</span> in every number.</h1>
<p class="lead">Free analysers, data and guides on lucky and unlucky numbers in Chinese culture — for phone numbers, plates, addresses, wedding dates, business launches and numeric domains.</p>
<div class="digits-band" aria-label="345789 digit by digit"><b>3<i>生 life</i></b><b class="warn">4<i>死 death</i></b><b>5<i>我 me</i></b><b class="hot">7<i>起 rise</i></b><b class="hot">8<i>发 rich</i></b><b class="hot">9<i>久 last</i></b></div>
<p style="margin-top:34px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-p" href="{R}tools/index.html">Explore 9 free tools</a><a class="btn btn-o" href="{R}get-your-report.html">Get a free expert report</a></p>
</div>
<div>''' + analyser("any", "Try 168, 5201314 or your phone number", demo="345789") + '''</div>
</div></section>

<section class="s"><div class="wrap">
<div class="grid g4">
<div class="card stat reveal"><b>+65%</b><span class="muted small">price lift an 8 adds to a Hong Kong licence plate (2024–25 auctions)</span></div>
<div class="card stat reveal"><b>−2.2%</b><span class="muted small">discount on Vancouver homes whose address ends in 4</span></div>
<div class="card stat reveal"><b>¥2.33M</b><span class="muted small">paid for the phone number 8888-8888 in 2003</span></div>
<div class="card stat reveal"><b>8:08:08</b><span class="muted small">pm, 8/8/08 — the Beijing Olympics start time</span></div>
</div>
<p class="small muted center" style="margin-top:10px">Sources on the <a href="{R}records.html">Hall of Records</a>.</p>
</div></section>
''' + f'<div class="wrap">{ad("inContent")}</div>' + '''
<section class="s alt"><div class="wrap">
<div class="s-head"><h2>Nine free tools. Zero sign-up.</h2><p>Instant, private, in-browser results — built on the same digit, combination and pattern rules native speakers use.</p></div>
''' + tool_grid() + '''
</div></section>

<section class="s"><div class="wrap grid g2" style="align-items:center">
<div><span class="badge r">The meaning of 0–9</span><h2 style="margin-top:12px">Every digit has a sound. Every sound has a meaning.</h2>
<p class="muted">Chinese is full of homophones, so numbers are heard as words: 8 is 发 “prosper”, 9 is 久 “lasting”, 4 is 死 “death”. String them together and a number becomes a sentence — 518 is “I will prosper”, 1314 is “forever”.</p>
<p><a class="btn btn-o" href="{R}meanings/index.html">Browse all meanings &amp; 50+ combos</a></p></div>
<div class="grid g3" style="gap:10px">
<a class="card center" href="{R}meanings/number-8.html"><div style="font-size:2.4rem;font-weight:800">8</div><div class="zh">发 prosper</div></a>
<a class="card center" href="{R}meanings/number-6.html"><div style="font-size:2.4rem;font-weight:800">6</div><div class="zh">顺 smooth</div></a>
<a class="card center" href="{R}meanings/number-9.html"><div style="font-size:2.4rem;font-weight:800">9</div><div class="zh">久 lasting</div></a>
<a class="card center" href="{R}meanings/number-4.html"><div style="font-size:2.4rem;font-weight:800;color:var(--red)">4</div><div class="zh">死 death</div></a>
<a class="card center" href="{R}meanings/number-2.html"><div style="font-size:2.4rem;font-weight:800">2</div><div class="zh">双 pairs</div></a>
<a class="card center" href="{R}meanings/number-7.html"><div style="font-size:2.4rem;font-weight:800">7</div><div class="zh">起 rise</div></a>
</div></div></section>

<section class="s alt"><div class="wrap">
<div class="cta-band"><div><h2>Get your free Lucky Number Report</h2><p>Your personal lucky digits, best dates for the next 12 months, Kua directions — plus an expert review of any phone, plate, address or numeric domain you choose.</p></div>
<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-o" href="{R}get-your-report.html">Start — takes 60 seconds</a><a class="btn btn-g" href="{R}marketplace.html">Sell a lucky number</a></div></div>
</div></section>

<section class="s"><div class="wrap">
<div class="s-head"><h2>Watch &amp; learn</h2><p>Short explainers on lucky numbers, auctions and traditions.</p></div>
<div class="grid g3">''' + video("chinese lucky numbers explained","八") + video("hong kong license plate auction","车") + video("feng shui house number","宅") + '''</div>
<p class="center" style="margin-top:20px"><a class="btn btn-o" href="{R}videos.html">Video hub →</a></p>
</div></section>

<section class="s alt"><div class="wrap grid g3">
<div class="card"><div class="ic">奖</div><h3>Monthly Lucky Number Challenge</h3><p>Share the story behind your lucky number. Prizes every month.</p><p style="margin-top:12px"><a href="{R}contests.html">Enter the contest →</a></p></div>
<div class="card"><div class="ic">市</div><h3>Numeric Asset Marketplace</h3><p>List a numeric domain, vanity plate or phone number free — we route serious buyers to you.</p><p style="margin-top:12px"><a href="{R}marketplace.html">List or buy →</a></p></div>
<div class="card"><div class="ic">才</div><h3>We're hiring</h3><p>Writers, bilingual editors, video creators and SEO talent — remote.</p><p style="margin-top:12px"><a href="{R}careers.html">See open roles →</a></p></div>
</div></section>

<section class="s"><div class="narrow">
<div class="s-head"><h2>Questions people ask</h2></div>
''' + faq_html([("Which numbers are lucky in Chinese culture?","8 (发, prosper) is the luckiest, followed by 6 (smooth), 9 (long-lasting) and 2 (pairs). Combos like 168, 518 and 888 are prized."),
     ("Why is 4 unlucky?","4 (sì) sounds almost exactly like 死 (sǐ), 'death', so many buildings skip 4th floors and buyers discount addresses ending in 4."),
     ("Is 345789 a lucky number?","It scores about 64/100 (吉, auspicious): the 7-8-9 finish reads 起发久 'rise, prosper, endure' and the run ascends, but the 4 costs points.")]) + '''
<div style="margin-top:28px">''' + ad("footer") + '''</div>
</div></section>
''')

# ------------------------------------------------------------------ LEAD GEN
NEEDS = [("personal-report","Personal lucky-number report"),("business-number","Business phone / number selection"),("date-selection","Wedding / opening / moving date"),
         ("domain-valuation","Numeric domain valuation"),("sell-asset","Sell my domain / plate / phone number"),("buy-asset","Buy a lucky number asset"),
         ("consultation","1-to-1 consultation"),("partnership","Business partnership / bulk")]
opts = "".join(f'<label class="opt"><input type="radio" name="need" value="{v}" required {"checked" if i==0 else ""}> {t}</label>' for i,(v,t) in enumerate(NEEDS))
add(path="get-your-report.html", prio="0.9", crumbs=[("Free Lucky Number Report","get-your-report.html")],
title="Free Lucky Number Report — Personal Numbers, Dates & Expert Number Review | 345789",
desc="Request a free personalised Chinese lucky-number report: best digits, lucky dates, Kua directions and an expert review of your phone, plate, address or numeric domain.",
body=hero("Your free Lucky Number Report", "Tell us what you need in 3 quick steps. A specialist reviews every request and replies within 48 hours — no spam, no obligation.", "🎁 Free · Human-reviewed · 48 h") + f'''
<div class="wrap layout"><div>
<div class="card" style="padding:28px">
<form class="form" data-form="Lead — Lucky Number Report" data-steps data-ok="Received! Your report request is in the queue — expect a reply within 48 hours.">
<div class="steps" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="step"><h3>1 · What do you need?</h3><div class="opt-grid">{opts}</div><button class="btn btn-p" data-next>Continue →</button></div>
<div class="step"><h3>2 · The details</h3>
<div><label for="f-num">Number(s), domain or plate to review</label><input id="f-num" name="number" placeholder="e.g. 138 8888 1688, 345789.com, plate 2828"></div>
<div id="mini" class="note" style="display:none"></div>
<div class="row"><div><label for="f-bd">Birth date (for personal numbers)</label><input id="f-bd" type="date" name="birth_date"></div>
<div><label for="f-g">Gender (for Kua number)</label><select id="f-g" name="gender"><option value="">Prefer not to say</option><option>Female</option><option>Male</option></select></div></div>
<div class="row"><div><label for="f-b">Budget</label><select id="f-b" name="budget"><option>Free report only</option><option>Under $100</option><option>$100–$1,000</option><option>$1,000–$10,000</option><option>$10,000+</option></select></div>
<div><label for="f-t">Timeline</label><select id="f-t" name="timeline"><option>Just exploring</option><option>Within 1 month</option><option>1–3 months</option><option>Urgent (this week)</option></select></div></div>
<div><label for="f-m">Anything else?</label><textarea id="f-m" name="message" rows="3" placeholder="Event date, business type, the story behind your number…"></textarea></div>
<div style="display:flex;gap:10px"><button class="btn btn-o" data-prev>← Back</button><button class="btn btn-p" data-next>Continue →</button></div></div>
<div class="step"><h3>3 · Where should we send it?</h3>
<div class="row"><div><label for="f-n">Name</label><input id="f-n" name="name" required autocomplete="name"></div><div><label for="f-e">Email</label><input id="f-e" type="email" name="email" required autocomplete="email"></div></div>
<div class="row"><div><label for="f-w">WhatsApp / WeChat / phone (optional)</label><input id="f-w" name="messenger"></div><div><label for="f-c">Country</label><input id="f-c" name="country" autocomplete="country-name"></div></div>
{form_footer()}
<div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-o" data-prev>← Back</button><button class="btn btn-p" type="submit">Send my free report request</button></div>
<div class="form-msg" role="status"></div></div>
</form></div>
<div class="grid g3" style="margin-top:24px">
<div class="card"><h3>🔒 Private</h3><p>Your details are used only to answer your request. Never sold.</p></div>
<div class="card"><h3>📚 Evidence-based</h3><p>Built on academic studies and auction data. <a href="{{R}}methodology.html">Our method</a>.</p></div>
<div class="card"><h3>⏱ 48-hour reply</h3><p>Every request is reviewed by a person, not just a script.</p></div></div>
{ad()}
<h2>What's inside the report</h2><ul><li>Your zodiac lucky &amp; unlucky digits and how to use them</li><li>12-month shortlist of favourable dates (Chinese Almanac)</li><li>Kua number with four lucky directions for desk and bed</li><li>Line-by-line review of up to 3 numbers (phone, plate, address, domain)</li><li>Concrete swaps to upgrade weak numbers</li></ul>
<h2>Selling or buying a numeric asset?</h2><p>Choose “Sell” or “Buy” in step 1. We connect qualified buyers and sellers of numeric domains, vanity plates and phone numbers and can arrange escrow through third-party providers.</p>
</div>{sidebar(need="consultation")}</div>
<script>document.addEventListener("DOMContentLoaded",function(){{var f=document.querySelector("[data-steps]");f.addEventListener("step",function(e){{if(e.detail!==1)return;}});var n=document.getElementById("f-num"),m=document.getElementById("mini");function upd(){{var v=(window.LNL&&LNL.clean(n.value))||"";if(v.length<2){{m.style.display="none";return;}}var r=LNL.analyse(v.slice(0,16));m.style.display="block";m.innerHTML="<b>Instant preview:</b> "+v.slice(0,16)+" scores "+r.score+"/100 — "+r.grade.zh+" "+r.grade.en+". Your full report adds dialect, pattern and personal fit.";}}n.addEventListener("input",upd);setTimeout(upd,300);}});</script>
''')

# ------------------------------------------------------------------ MARKETPLACE
add(path="marketplace.html", prio="0.8", crumbs=[("Marketplace","marketplace.html")],
title="Lucky Number Marketplace — Buy & Sell Numeric Domains, Vanity Plates & Phone Numbers | 345789",
desc="List your numeric domain, lucky licence plate or vanity phone number free, or post a buyer request. Pattern guide (AABB, ABAB, 6N, no-4) and broker introductions.",
body=hero("The Lucky Number Marketplace", "List numeric domains, vanity plates and lucky phone numbers free. Post what you want to buy. We match serious buyers and sellers and introduce escrow.", "市 Numeric assets") + f'''
<div class="wrap">
<div class="grid g4">
<div class="card"><h3>AAAA / AAAAAA</h3><p>All-same digits — 8888, 666666. Top tier when the digit is 8, 6 or 9.</p></div>
<div class="card"><h3>AABB · ABAB · ABBA</h3><p>Rhythmic patterns that are easy to remember and resell.</p></div>
<div class="card"><h3>No-4 · 8-rich</h3><p>The Chinese-market filters. A single 4 can halve buyer interest.</p></div>
<div class="card"><h3>Meaningful</h3><p>168, 518, 1314, 5201314 — numbers that read as phrases.</p></div>
</div>
<h2 style="margin-top:40px">Featured listings <span class="badge">Examples</span></h2>
<p class="muted small">Sample cards show how listings appear. Featured placement for real listings is available — <a href="{{R}}advertise.html">see rates</a>.</p>
<div class="grid g3">
<div class="card"><span class="badge">Domain · 6N</span><h3 style="margin-top:8px">345789.com</h3><p>Ascending run, ends 789 “rise·prosper·endure”. Contains 4.</p><p style="margin-top:10px"><a class="btn btn-sm btn-p" href="https://web.works/contact" target="_blank" rel="noopener">Make an offer</a></p></div>
<div class="card"><span class="badge">Example · Plate</span><h3 style="margin-top:8px">“2828”</h3><p>ABAB · Cantonese 易发易发 “easy prosperity”.</p><p style="margin-top:10px"><a class="btn btn-sm btn-o" href="#buy">Request similar</a></p></div>
<div class="card"><span class="badge">Example · Phone</span><h3 style="margin-top:8px">…-1688</h3><p>Ends 1688 “prosper all the way, twice”.</p><p style="margin-top:10px"><a class="btn btn-sm btn-o" href="#buy">Request similar</a></p></div>
</div>
{ad()}
<div class="grid g2" style="margin-top:20px">
<div class="card" id="sell"><h2>List your asset — free</h2>
<form class="form" data-form="Marketplace — Seller listing" data-ok="Listing received! We'll verify ownership and publish within 72 hours.">
<div class="row"><div><label>Asset type</label><select name="asset_type" required><option>Numeric domain</option><option>Licence plate</option><option>Phone number</option><option>Other</option></select></div><div><label>The number / domain</label><input name="number" required placeholder="e.g. 88168.com"></div></div>
<div class="row"><div><label>Asking price (USD)</label><input name="asking_price" inputmode="numeric" placeholder="or 'make offer'"></div><div><label>Country / region</label><input name="region"></div></div>
<div><label>Notes (registrar, transfer method, story)</label><textarea name="message" rows="3"></textarea></div>
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="featured" value="interested"> I'm interested in a featured listing</label>
{form_footer()}<button class="btn btn-p" type="submit">Submit listing</button><div class="form-msg" role="status"></div></form></div>
<div class="card" id="buy"><h2>Post a buyer request</h2>
<form class="form" data-form="Marketplace — Buyer request" data-ok="Request received! We'll send matching options within 72 hours.">
<div class="row"><div><label>Looking for</label><select name="asset_type" required><option>Numeric domain</option><option>Licence plate</option><option>Phone number</option></select></div><div><label>Pattern / digits wanted</label><input name="pattern" placeholder="e.g. 5N no-4, ends 88"></div></div>
<div class="row"><div><label>Budget (USD)</label><select name="budget"><option>Under $500</option><option>$500–$5,000</option><option>$5,000–$50,000</option><option>$50,000+</option></select></div><div><label>Region</label><input name="region" placeholder="HK, SG, CN, US…"></div></div>
<div><label>Use case</label><textarea name="message" rows="3" placeholder="Brand, gift, investment…"></textarea></div>
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
{form_footer()}<button class="btn btn-p" type="submit">Send request</button><div class="form-msg" role="status"></div></form></div>
</div>
<div class="note" style="margin-top:24px">345789.com is an introduction service, not a party to any transaction. Always transact through a licensed escrow provider and verify ownership. Plate and phone-number transfers are subject to local regulations.</div>
<p style="margin-top:20px"><a class="btn btn-o" href="{{R}}tools/numeric-domain-valuer.html">Value a numeric domain first →</a></p>
</div>''')

# ------------------------------------------------------------------ VIDEOS
add(path="videos.html", crumbs=[("Videos","videos.html")],
title="Lucky Number Videos — Chinese Numerology, Plate Auctions & Feng Shui | 345789",
desc="Video hub: Chinese lucky numbers explained, Hong Kong licence-plate auctions, feng shui house numbers, Chinese New Year traditions and numeric domain investing.",
body=hero("Video hub", "Explainers, auction highlights and how-tos. Our own channel is in production — subscribe to be first.", "▶ Watch") + f'''
<div class="wrap"><div class="grid g3" id="video-hub">
{video("chinese lucky numbers explained","八")}{video("why is 4 unlucky in chinese culture","四")}{video("hong kong license plate auction","车")}
{video("feng shui house number","宅")}{video("chinese new year traditions","春")}{video("chinese zodiac explained","龙")}
{video("numeric domain names investing","域")}{video("chinese wedding date selection","囍")}{video("learn chinese numbers","九")}
</div>{ad()}
<div class="cta-band"><div><h2>Create with us</h2><p>Are you a creator covering Chinese culture, feng shui or domains? We commission explainers and sponsor integrations.</p></div><div><a class="btn btn-o" href="{{R}}careers.html">Pitch a video</a></div></div></div>''')

# ------------------------------------------------------------------ RECORDS
add(path="records.html", article=True, crumbs=[("Meanings","meanings/index.html"),("Hall of Records","records.html")],
title="Hall of Records — Most Expensive Lucky Numbers, Plates & the Economics of 8 | 345789",
desc="Record prices for lucky licence plates and phone numbers, plus peer-reviewed studies on how 8 and 4 move house, apartment and plate prices.",
body=hero("Hall of Records", "When superstition meets money: verified record prices and the research that measures the lucky-number premium.", "📈 Data") + with_side('''
<h2>Record prices</h2><div class="tbl-wrap"><table><tr><th>Asset</th><th>Price</th><th>Year</th><th>Why it matters</th></tr>
<tr><td>Hong Kong plate “W”</td><td>HK$26M (~US$3.3M)</td><td>2021</td><td>Single-letter record</td></tr>
<tr><td>Hong Kong plate “28”</td><td>HK$18.1M</td><td>2016</td><td>易发 “easy prosperity” in Cantonese</td></tr>
<tr><td>Hong Kong plate “18”</td><td>HK$16.5M</td><td>2008</td><td>实发 “sure to prosper”</td></tr>
<tr><td>Hong Kong plate “9”</td><td>HK$13M</td><td>1994</td><td>久 “everlasting”</td></tr>
<tr><td>Hong Kong plate “12”</td><td>HK$7.1M</td><td>2005</td><td>“Certainly easy” in Cantonese</td></tr>
<tr><td>HK personalised plate “168888”</td><td>HK$210,000</td><td>2023</td><td>一路发发发发 personalised-plate record</td></tr>
<tr><td>Phone number +86 28 8888 8888</td><td>~US$280,000 (¥2.33M)</td><td>2003</td><td>Bought by Sichuan Airlines</td></tr>
</table></div>
<h2>What the research says</h2>
<h3>Hong Kong licence plates, 2024–25</h3><p>A University of Virginia study of 1,067 auctioned plates found the digit 8 raises a plate’s value by about <b>64.8%</b>; the pairs 28, 68 and 88 add a further 42.9%, 42.3% and 37.4%. 2, 6 and 9 each add roughly 19–33%. Prices ranged 18,000-fold, from the HK$1,000 reserve to HK$11.4M.</p>
<h3>Hong Kong plates over 15 years</h3><p>Woo, Horowitz, Luk &amp; Lai (2008) modelled 30,000+ auctions; numerology alone explained much of the willingness to pay (adjusted R² 0.73).</p>
<h3>Vancouver houses, 2000–2005</h3><p>Across ~117,000 sales, homes with addresses ending in 4 sold at a <b>2.2% discount</b> and those ending in 8 at a <b>2.5% premium</b> in neighbourhoods with above-average Chinese population (Fortin, Hill &amp; Huang).</p>
<h3>Chengdu apartments, 2004–2006</h3><p>Second-hand units on floors ending in 8 sold for ~<b>235 RMB/m² more</b>; lucky floors in new buildings sold about 7 days faster (Shum, Sun &amp; Ye, 2014).</p>
<h2>Famous 8s</h2><ul><li>Beijing Olympics opened 8/8/2008 at 8:08:08 pm.</li><li>Airlines reserve 8-heavy flight numbers on China routes (e.g. UA888, CX888, KL888).</li><li>The Petronas Towers have 88 floors.</li></ul>
<h3>Sources</h3><ol class="small"><li><a href="https://economics.virginia.edu/sites/economics.as.virginia.edu/files/2025-05/Yingying%20Elisa%20Hu.pdf" rel="noopener" target="_blank">Hu (2025), University of Virginia</a></li><li><a href="https://www.sciencedirect.com/science/article/abs/pii/S016748700700027X" rel="noopener" target="_blank">Woo et al. (2008), Journal of Economic Psychology</a></li><li><a href="https://economics.ubc.ca/wp-content/uploads/sites/38/2013/05/pdf_paper_nicole-fortin-supersitition-housing-market.pdf" rel="noopener" target="_blank">Fortin, Hill &amp; Huang, UBC</a></li><li><a href="https://ideas.repec.org/a/eee/jcecon/v42y2014i1p109-117.html" rel="noopener" target="_blank">Shum, Sun &amp; Ye (2014), J. Comparative Economics</a></li><li><a href="https://www.cnn.com/style/article/hong-kong-auctioned-vanity-car-plates-intl-hnk/index.html" rel="noopener" target="_blank">CNN — Hong Kong vanity plates</a></li><li><a href="https://en.wikipedia.org/wiki/Chinese_numerology" rel="noopener" target="_blank">Wikipedia — Chinese numerology</a></li></ol>
''' + ad() + author(), need="sell-asset"))

# ------------------------------------------------------------------ STORY
add(path="the-345789-story.html", article=True, crumbs=[("Meanings","meanings/index.html"),("The 345789 Story","the-345789-story.html")],
title="What Does 345789 Mean? The Story of a Rising Number | 345789",
desc="345789 read in Chinese: sān sì wǔ qī bā jiǔ. Why the 789 finish reads 'rise, prosper, endure', why the 4 matters, and how it scores.",
body=hero("The 345789 story", "Six digits, one staircase: why this number is the perfect lesson in Chinese number luck — fear and fortune in a single string.", "三四五七八九") + with_side('''
<div class="digits-band"><b>3<i>生</i></b><b class="warn">4<i>死</i></b><b>5<i>我</i></b><b class="hot">7<i>起</i></b><b class="hot">8<i>发</i></b><b class="hot">9<i>久</i></b></div>
<h2 style="margin-top:40px">Read it aloud</h2><p>In Mandarin, 345789 is <i>sān sì wǔ qī bā jiǔ</i> — <span class="zh">三四五七八九</span>. Native listeners hear each digit as a word, so the number reads like a sentence.</p>
<h2>The finish: 7-8-9 = rise, prosper, endure</h2><p>Endings carry the most weight in Chinese number reading. Here the last three digits line up as <span class="zh">起·发·久</span> (<i>qǐ · fā · jiǔ</i>): <b>rise</b>, <b>prosper</b>, <b>last</b>. It is a modern reading rather than a fixed idiom, but every element is a classic lucky sound.</p>
<h2>The climb: an ascending run</h2><p>Every digit is bigger than the one before. Rising sequences echo <span class="zh">步步高升</span> “rising step by step”, a phrase used for promotions and business growth.</p>
<h2>The honest part: the 4</h2><p>The second digit is 4, <span class="zh">四</span> — a near-homophone of <span class="zh">死</span> “death”. Numeric-domain dealers say a single 4 can sharply reduce Chinese-market demand, and buildings across East Asia skip the 4th floor. We think that makes 345789 the ideal mascot for this site: it holds the most feared digit and the most prized one (8) side by side.</p>
<h2>Score</h2><p>Our analyser rates 345789 at about <b>64/100 — 吉 (auspicious)</b>: the 789 finish and the climb outweigh the 4, but not by much. <a href="{R}tools/number-meaning-analyzer.html?n=345789">See the full breakdown</a>.</p>
<blockquote>No trademark is claimed in “345789”, and this site isn't affiliated with any business, phone number, plate, lottery or stock code that uses the same digits.</blockquote>
''' + ad() + author()))

# ------------------------------------------------------------------ METHODOLOGY
add(path="methodology.html", crumbs=[("Meanings","meanings/index.html"),("Methodology","methodology.html")],
title="How We Score Numbers — Methodology | 345789",
desc="How the 345789 Number Intelligence Engine scores digits, combinations, patterns and endings, and which sources it draws on.",
body=hero("Methodology", "Transparent rules, cited sources, honest limits.", "⚙ How it works") + with_side('''
<h2>1. Digit values</h2><p>Each digit 0–9 carries a sentiment value from −3 (4, “death”) to +3 (8, “prosper”) based on its common Mandarin homophones. We also check Cantonese readings and an optional Teochew mode in which 4 is lucky.</p>
<h2>2. Position weighting</h2><p>The last digit counts double and the second-to-last 1.4×, because Chinese readers judge numbers by how they end (phone numbers by the last four digits).</p>
<h2>3. Combinations</h2><p>We look for 50+ meaningful combinations (168, 518, 1314, 514, 748…), longest first and without overlap. A combination replaces most of the weight of its digits and counts more at the end of the number.</p>
<h2>4. Patterns</h2><p>All-same, AABB, ABAB, ABBA, ABCABC, palindromes, repeaters, ascending runs (bonus) and descending runs (penalty).</p>
<h2>5. The 4-penalty</h2><p>Every 4 that isn't part of a positive phrase costs an extra 6 points, reflecting measured price discounts.</p>
<h2>6. Grades</h2><table><tr><th>Score</th><th>Grade</th></tr><tr><td>85–99</td><td>大吉 Very auspicious</td></tr><tr><td>64–84</td><td>吉 Auspicious</td></tr><tr><td>45–63</td><td>平 Balanced</td></tr><tr><td>30–44</td><td>小凶 Caution</td></tr><tr><td>1–29</td><td>凶 Inauspicious</td></tr></table>
<h2>7. Almanac data</h2><p>The Lucky Date Finder uses traditional Chinese Almanac (Tong Shu) rules — lunar date, day pillar, clash animal, day quality and favourable/avoid activities — computed for 2026–2028 and translated into English.</p>
<h2>Limits</h2><p>Number luck is a cultural belief, and readings vary by region, dialect and family. The economic premiums we cite are real market effects driven by that belief. Use these tools for culture, fun and negotiation insight — not as financial advice.</p>
''' + author()))

# ------------------------------------------------------------------ DONATE
add(path="donate.html", crumbs=[("Community","contests.html"),("Donate","donate.html")],
title="Support 345789 — Donate to Keep the Lucky Number Lab Free",
desc="Support free lucky-number tools and research. Donations fund operations, promotion and marketing, hiring talent, and contest prizes.",
body=hero("Keep the lab free", "Every tool here is free and ad-light. Your support pays for servers, research, new tools, creators and the monthly contest prize pool.", "❤ Support") + f'''
<div class="wrap">
<div class="card" id="goal" style="margin-bottom:24px"></div>
<div class="grid g4">
<div class="card tier"><h3>Supporter</h3><div class="amt">$8</div><p>One 发 for the lab. Name on the donor wall.</p><p style="margin-top:12px"><button class="btn btn-o btn-block" data-amount="8">Choose $8</button></p></div>
<div class="card tier feat"><span class="badge">Most popular</span><h3 style="margin-top:8px">Patron</h3><div class="amt">$88</div><p>Double prosperity. Early access to new tools + free full report.</p><p style="margin-top:12px"><button class="btn btn-p btn-block" data-amount="88">Choose $88</button></p></div>
<div class="card tier"><h3>Sponsor</h3><div class="amt">$888</div><p>Logo on a tool page for 3 months and a contest prize named after you.</p><p style="margin-top:12px"><button class="btn btn-o btn-block" data-amount="888">Choose $888</button></p></div>
<div class="card tier"><h3>Custom</h3><div class="amt">$__</div><p>Monthly or one-off — any amount helps.</p><p style="margin-top:12px"><button class="btn btn-o btn-block" data-amount="">Choose amount</button></p></div>
</div>
<h2 style="margin-top:40px">Where your money goes</h2>
<div class="grid g4"><div class="card"><div class="ic">⚙</div><h3>Operations</h3><p>Hosting, data, almanac computation and maintenance.</p></div><div class="card"><div class="ic">📣</div><h3>Promotion &amp; marketing</h3><p>Reaching more readers in English and Chinese.</p></div><div class="card"><div class="ic">才</div><h3>Hiring talent</h3><p>Paying native-speaker writers, editors and video creators.</p></div><div class="card"><div class="ic">奖</div><h3>Contests &amp; prizes</h3><p>Funding the monthly Lucky Number Challenge.</p></div></div>
<div class="grid g2" style="margin-top:30px">
<div class="card"><h2>Pay instantly</h2><div id="donate-links" style="display:flex;gap:10px;flex-wrap:wrap"></div></div>
<div class="card" id="pledge"><h2>Pledge form</h2>
<form class="form" data-form="Donation pledge" data-ok="Thank you! We'll email secure payment options within 24 hours.">
<div class="row"><div><label for="pledge-amount">Amount (USD)</label><input id="pledge-amount" name="amount" inputmode="numeric" required></div><div><label>Frequency</label><select name="frequency"><option>One-time</option><option>Monthly</option><option>Yearly</option></select></div></div>
<div><label>Earmark (optional)</label><select name="earmark"><option>Where needed most</option><option>Operations</option><option>Promotion &amp; marketing</option><option>Hiring talent</option><option>Contest prizes</option></select></div>
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<label class="check"><input type="checkbox" name="public" value="yes"> Show my name on the donor wall</label>
{form_footer()}<button class="btn btn-p" type="submit">Send pledge</button><div class="form-msg" role="status"></div></form></div></div>
<h2 style="margin-top:40px">Donor wall</h2><p class="muted">Be the first name here. 🧧</p>
<p class="small muted">345789.com is not a registered charity; contributions are not tax-deductible.</p></div>''')

# ------------------------------------------------------------------ CONTESTS
add(path="contests.html", crumbs=[("Community","contests.html"),("Contests","contests.html")],
title="Lucky Number Challenge — Monthly Contest & Prizes | 345789",
desc="Enter the monthly Lucky Number Challenge: share your lucky number and its story, win cash prizes, gift cards and a featured profile.",
faq=[("Is there an entry fee?","No. Entry is free and no purchase is necessary."),("Who can enter?","Adults 18+ where such contests are legal. Void where prohibited."),("How are winners chosen?","A panel scores originality (40%), cultural insight (30%) and storytelling (30%).")],
body=hero("The Lucky Number Challenge", "Every number has a story. Tell us yours — the best ones win prizes and a feature on 345789.com.", "奖 Monthly contest") + f'''
<div class="wrap">
<div class="grid g3">
<div class="card tier feat"><span class="badge">1st prize</span><div class="amt" style="margin-top:8px">$88</div><p>Cash or gift card + featured story + free premium report</p></div>
<div class="card tier"><span class="badge">2nd prize</span><div class="amt" style="margin-top:8px">$38</div><p>Gift card + featured story</p></div>
<div class="card tier"><span class="badge">3rd prize</span><div class="amt" style="margin-top:8px">$18</div><p>Gift card + shout-out</p></div>
</div>
<div class="grid g2" style="margin-top:30px">
<div><h2>This month's theme: “The number that changed my luck”</h2>
<ol><li><b>Enter</b> by the last day of the month (23:59 UTC).</li><li><b>Judging</b> in the first week of the next month.</li><li><b>Winners</b> announced here and by email.</li></ol>
<h3>Official rules (summary)</h3><ul class="small"><li>No purchase necessary. Free to enter. One entry per person per month.</li><li>Open to individuals aged 18+ where such contests are legal; void where prohibited.</li><li>Entries must be original, up to 300 words, and free of third-party copyrighted material.</li><li>Judging: originality 40%, cultural insight 30%, storytelling 30%. Judges' decisions are final.</li><li>By entering you grant 345789.com a non-exclusive licence to publish your entry with credit.</li><li>Prizes are non-transferable; winners are responsible for any taxes. Unclaimed prizes after 30 days are forfeited.</li><li>Personal data is handled under our <a href="{{R}}privacy.html">privacy policy</a>.</li></ul>
<h3>Sponsor a prize</h3><p>Brands can sponsor a monthly prize pool. <a href="{{R}}advertise.html">Contest sponsorship →</a></p></div>
<div class="card"><h2>Submit your entry</h2>
<form class="form" data-form="Contest entry" data-ok="Entry received — good luck! 🍀">
<div><label>Your lucky number</label><input name="number" required></div>
<div><label>Your story (max 300 words)</label><textarea name="story" rows="7" required maxlength="2000"></textarea></div>
<div class="row"><div><label>Name / display name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<div><label>Country</label><input name="country"></div>
<label class="check"><input type="checkbox" name="age_18" value="yes" required> I am 18+ and accept the official rules.</label>
{form_footer()}<button class="btn btn-p" type="submit">Enter the challenge</button><div class="form-msg" role="status"></div></form></div></div>
<h2 style="margin-top:30px">Past winners</h2><p class="muted">The first winners will be announced after this month's challenge closes.</p>
<div class="narrow" style="margin-top:20px">{faq_html([("Is there an entry fee?","No. Entry is free and no purchase is necessary."),("Who can enter?","Adults 18+ where such contests are legal. Void where prohibited."),("How are winners chosen?","A panel scores originality (40%), cultural insight (30%) and storytelling (30%).")])}</div></div>''')

# ------------------------------------------------------------------ CAREERS
ROLES = [("Chinese-culture content writer","Remote · freelance","Long-form guides on numbers, festivals and traditions. Native or near-native Mandarin a plus."),
         ("Bilingual editor (EN / 中文)","Remote · part-time","Fact-check and localise content for a Simplified-Chinese edition."),
         ("Short-video creator","Remote · per video","YouTube Shorts / TikTok explainers on lucky numbers and auctions."),
         ("SEO & programmatic content specialist","Remote · contract","Scale pages for combos, zodiac years and almanac dates."),
         ("Partnerships & ad sales manager","Remote · commission","Sell sponsorships, featured listings and brand integrations."),
         ("Community & contest moderator","Remote · part-time","Run the monthly challenge and the marketplace inbox.")]
add(path="careers.html", crumbs=[("Community","contests.html"),("Careers","careers.html")],
title="Careers at 345789 — Writers, Editors, Video Creators & SEO (Remote)",
desc="Join the Lucky Number Lab: remote roles for Chinese-culture writers, bilingual editors, short-video creators, SEO specialists and partnership managers.",
body=hero("We're hiring talent", "Small, remote, fast-moving. Help build the world's best resource on numbers and luck.", "才 Careers") + '<div class="wrap"><div class="grid g3">' +
"".join(f'<div class="card"><span class="badge">{t2}</span><h3 style="margin-top:8px">{t}</h3><p>{d}</p></div>' for t,t2,d in ROLES) + f'''</div>
<div class="grid g2" style="margin-top:30px"><div><h2>Why work with us</h2><ul><li>100% remote, async, flexible hours</li><li>Paid per project or monthly retainer — your choice</li><li>Byline credit and portfolio-grade work</li><li>Revenue share on content that performs</li></ul><h3>Also open to</h3><p>Interns, translators (Cantonese, Teochew, Hokkien, Vietnamese, Korean, Japanese) and data researchers.</p></div>
<div class="card"><h2>Apply</h2><form class="form" data-form="Job application" data-ok="Application received — we review every one and reply within a week.">
<div><label>Role</label><select name="role" required>{"".join(f"<option>{t}</option>" for t,_,_ in ROLES)}<option>Other / open application</option></select></div>
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<div class="row"><div><label>Portfolio / LinkedIn URL</label><input type="url" name="portfolio" placeholder="https://"></div><div><label>Languages</label><input name="languages"></div></div>
<div><label>Why you? (short)</label><textarea name="message" rows="4" required></textarea></div>
<div><label>Expected rate</label><input name="rate" placeholder="e.g. $0.10/word or $40/hr"></div>
{form_footer()}<button class="btn btn-p" type="submit">Send application</button><div class="form-msg" role="status"></div></form></div></div></div>''')

# ------------------------------------------------------------------ ADVERTISE
add(path="advertise.html", crumbs=[("Community","contests.html"),("Advertise","advertise.html")],
title="Advertise & Sponsor on 345789 — Reach Lucky-Number, Feng Shui & Numeric-Asset Audiences",
desc="Advertising, sponsorship and partnership options on 345789.com: display banners, sponsored tools, newsletter, featured marketplace listings, contest and YouTube integrations.",
body=hero("Advertise, sponsor, partner", "Put your brand in front of people making high-intent decisions about numbers — phone lines, plates, homes, wedding dates and domains.", "📣 Media kit") + f'''
<div class="wrap">
<div class="note" style="margin-bottom:24px">Interested in buying or partnering on this <b>website or the 345789.com domain</b>? Contact <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</div>
<div class="grid g3">
<div class="card"><h3>Display banners</h3><p>In-content and sidebar placements on tool and guide pages. CPM or flat monthly.</p><p class="small"><b>From $99/mo</b></p></div>
<div class="card"><h3>Sponsored tool</h3><p>“Presented by” branding on a tool such as the Lucky Date Finder or Domain Valuer.</p><p class="small"><b>From $299/mo</b></p></div>
<div class="card"><h3>Newsletter sponsor</h3><p>Exclusive slot in the daily lucky-number email.</p><p class="small"><b>From $149/issue-week</b></p></div>
<div class="card"><h3>Featured marketplace listing</h3><p>Top placement for a numeric domain, plate or phone number.</p><p class="small"><b>From $49/mo</b></p></div>
<div class="card"><h3>Contest sponsorship</h3><p>Name the monthly prize pool; logo on contest pages and emails.</p><p class="small"><b>From $250/month</b></p></div>
<div class="card"><h3>Video integration</h3><p>Brand integration in our YouTube explainers and Shorts.</p><p class="small"><b>Custom quote</b></p></div>
</div>
<h2 style="margin-top:40px">Good fits</h2><p>Registrars and domain marketplaces · escrow services · feng shui consultants · jewellers (8-themed gifts) · wedding planners · telecoms with vanity numbers · real-estate agents serving Chinese buyers · language schools · travel to Asia.</p>
<p class="small muted">We don't accept gambling, lottery, adult, crypto-speculation or misleading “guaranteed luck” ads. Sponsored content is always labelled.</p>
{ad()}
<div class="card" style="margin-top:20px"><h2>Sponsorship &amp; partnership inquiry</h2>
<form class="form" data-form="Advertising / sponsorship inquiry" data-ok="Thanks! Our media kit and rates are on the way.">
<div class="row"><div><label>Company</label><input name="company" required></div><div><label>Website</label><input name="website" type="url" placeholder="https://"></div></div>
<div class="row"><div><label>Interested in</label><select name="interest"><option>Display banners</option><option>Sponsored tool</option><option>Newsletter</option><option>Featured listing</option><option>Contest sponsorship</option><option>Video integration</option><option>Partnership / acquisition of this site or domain</option></select></div><div><label>Monthly budget</label><select name="budget"><option>Under $250</option><option>$250–$1,000</option><option>$1,000–$5,000</option><option>$5,000+</option></select></div></div>
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<div><label>Goals / message</label><textarea name="message" rows="4"></textarea></div>
{form_footer()}<button class="btn btn-p" type="submit">Request media kit</button><div class="form-msg" role="status"></div></form></div></div>''')

# ------------------------------------------------------------------ ABOUT / CONTACT / LEGAL
add(path="about.html", crumbs=[("About","about.html")],
title="About 345789 — The Lucky Number Lab",
desc="345789.com is an independent lab of free tools, data and guides on lucky and unlucky numbers in Chinese culture and the economy around them.",
body=hero("About the Lucky Number Lab", "We turn a 2,000-year-old cultural instinct into clear tools and honest data.", "关于我们") + with_side('''
<h2>Our mission</h2><p>Hundreds of millions of people choose phone numbers, plates, addresses, prices and wedding dates with numbers in mind. Most English-language content on the subject is shallow lists. We build real tools, cite real research and explain the culture with respect.</p>
<h2>What we believe</h2><ul><li><b>Culture, not superstition-shaming.</b> Number beliefs are part of language and identity.</li><li><b>Evidence over hype.</b> We separate measured market effects from folklore.</li><li><b>Free at the core.</b> Tools stay free, funded by ads, sponsors, reports and donations.</li></ul>
<h2>Why “345789”?</h2><p>It rises step by step, ends in 起发久 “rise, prosper, endure” — and contains the dreaded 4. <a href="{R}the-345789-story.html">Read the story</a>.</p>
<h2>Independence</h2><p>We aren't affiliated with any government auction body, telecom, registrar, lottery or company that uses these digits. Sponsored content is always labelled.</p>
<p><a class="btn btn-p" href="{R}contact.html">Contact us</a> <a class="btn btn-o" href="https://web.works/contact" target="_blank" rel="noopener">Acquire / partner</a></p>'''))

add(path="contact.html", crumbs=[("Contact","contact.html")],
title="Contact 345789 — Questions, Partnerships & Press",
desc="Contact the 345789 Lucky Number Lab for questions, corrections, partnerships, press and advertising.",
body=hero("Contact us", "Questions, corrections, partnerships or press — we read everything and reply within 48 hours.", "联系") + f'''
<div class="wrap grid g2" style="padding-bottom:20px">
<div class="card"><form class="form" data-form="Contact" data-ok="Message received — we'll reply within 48 hours.">
<div><label>Topic</label><select name="topic"><option>General question</option><option>Correction / feedback</option><option>Report request</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Interest in buying this website / domain</option><option>Press</option></select></div>
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<div><label>Message</label><textarea name="message" rows="6" required></textarea></div>
{form_footer()}<button class="btn btn-p" type="submit">Send message</button><div class="form-msg" role="status"></div></form></div>
<div class="grid" style="align-content:start">
<div class="card"><h3>Website, domain, sponsorship or partnership?</h3><p>For acquisition, advertising and partnership interest in 345789.com, use our partner desk.</p><p style="margin-top:12px"><a class="btn btn-g" href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact →</a></p></div>
<div class="card"><h3>Prefer email?</h3><p>Open a pre-addressed email in your mail app.</p><p style="margin-top:12px"><a class="btn btn-o" href="#" data-mail="345789.com inquiry">✉ Email us</a></p></div>
<div class="card"><h3>Free report</h3><p>Want a number reviewed? Use the dedicated form.</p><p style="margin-top:12px"><a class="btn btn-p" href="{{R}}get-your-report.html">Get my report</a></p></div></div></div>''')

LEGAL_INTRO = '<p class="small muted">Last updated: October 2026</p>'
add(path="legal.html", crumbs=[("Trademark & Copyright","legal.html")],
title="Trademark & Copyright Disclosure | 345789",
desc="Trademark and copyright disclosure, cultural-content disclaimer, and advertising and affiliate disclosure for 345789.com.",
body=hero("Trademark &amp; copyright disclosure", "Plain-language statements about names, content ownership, advertising and the limits of cultural readings.", "⚖ Legal") + with_side(LEGAL_INTRO + '''
<h2>1. The numeral “345789”</h2><p>“345789” is a sequence of Arabic numerals used on this site descriptively, as the domain name and as an example of Chinese number reading. <b>No trademark rights are claimed</b> in the numeral string “345789”, and nothing on this site should be read as a trademark claim. 345789.com is <b>not affiliated with, endorsed by or connected to</b> any company, product, brand, lottery, telephone number, stock or securities code, postal code, vehicle registration mark or other entity that uses the same or similar digits. Any such third-party uses belong to their respective owners.</p>
<h2>2. Third-party marks</h2><p>Names of companies, platforms, airlines, events or services mentioned in articles (for example to cite news or research) are the property of their owners and are used only for identification and commentary (nominative fair use). Their mention does not imply endorsement or partnership. No third-party logos are used.</p>
<h2>3. Copyright</h2><p>All original text, data compilations, tools, code, graphics and layouts on 345789.com are © 2026 345789.com, all rights reserved, unless stated otherwise. Short factual data points (auction prices, study findings) are cited with links to their original sources. Traditional Chinese Almanac rules, number homophones and zodiac associations are public-domain cultural knowledge; our English translations, presentation and software are original works.</p>
<p>You may quote up to 100 words with a link back to the source page. Republishing whole pages, scraping tools or data, or framing the site requires written permission via the <a href="{R}contact.html">contact form</a>.</p>
<h2>4. Copyright complaints (DMCA-style notice)</h2><p>If you believe content here infringes your rights, send a notice through the <a href="{R}contact.html">contact form</a> with: the work concerned, the URL on our site, your contact details, a good-faith statement, and a statement that the information is accurate and you are authorised to act. We respond promptly and remove infringing material.</p>
<h2>5. Cultural and entertainment disclaimer</h2><p>Lucky-number readings, almanac dates, zodiac traits, Kua directions and scores are presented as <b>cultural tradition and entertainment</b>. They are not predictions and are <b>not financial, investment, legal, medical or real-estate advice</b>. Domain “tiers” and reference ranges are indicative and are not appraisals.</p>
<h2>6. Advertising, sponsorship and affiliate disclosure</h2><p>This site may display Google AdSense and other advertising, sponsored placements and affiliate links, and may receive referral fees for introductions made through the marketplace or report service. Sponsored content is labelled. Advertisers do not influence our scores or editorial content.</p>
<h2>7. Domain and website inquiries</h2><p>For interest in this website, the domain name, sponsorship, advertising or partnership, contact <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p>'''))

add(path="privacy.html", crumbs=[("Privacy","privacy.html")],
title="Privacy Policy | 345789",
desc="How 345789.com collects, uses and protects information, including forms, cookies and Google AdSense advertising.",
body=hero("Privacy policy", "Short version: tools run in your browser, forms go only to us, and we never sell your data.", "🔒 Privacy") + with_side(LEGAL_INTRO + '''
<h2>What we collect</h2><ul><li><b>Tool inputs</b> (numbers, dates) are processed in your browser and are not sent to us.</li><li><b>Form submissions</b> (name, email, message and details you choose to give) are delivered to our inbox through a form-relay service (FormSubmit) to answer your request.</li><li><b>Preferences</b> such as light/dark mode are stored in your browser's local storage.</li><li><b>Analytics</b> (if enabled) collect aggregated usage data.</li></ul>
<h2>Advertising and cookies</h2><p>We may use Google AdSense. Google and its partners use cookies to serve ads based on your prior visits to this and other websites. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>. Embedded YouTube videos load in privacy-enhanced mode only after you click play.</p>
<h2>How we use information</h2><p>To answer requests, deliver reports and newsletters you asked for, run contests, process applications and improve the site. We don't sell or rent personal data.</p>
<h2>Retention and your rights</h2><p>We keep form data only as long as needed for the purpose. You can request access, correction or deletion at any time through the <a href="{R}contact.html">contact form</a>. EU/UK (GDPR), California (CCPA) and Canadian (PIPEDA) residents have the rights their laws provide.</p>
<h2>Children</h2><p>The site is not directed at children under 13, and contests are for adults 18+.</p>
<h2>Hosting</h2><p>The site is static and hosted on GitHub Pages, which may log IP addresses for security.</p>'''))

add(path="terms.html", crumbs=[("Terms","terms.html")],
title="Terms of Use | 345789",
desc="Terms of use for 345789.com tools, content, marketplace introductions, contests and reports.",
body=hero("Terms of use", "The rules for using 345789.com.", "📄 Terms") + with_side(LEGAL_INTRO + '''
<h2>Use of the site</h2><p>By using 345789.com you agree to these terms. Tools and content are provided “as is” for information and entertainment, with no warranty of accuracy or fitness for any purpose.</p>
<h2>No advice</h2><p>Nothing here is financial, investment, legal, medical or real-estate advice. Make your own decisions and consult qualified professionals.</p>
<h2>Marketplace</h2><p>Listings and buyer requests are introductions only. 345789.com is not a broker of record, escrow agent or party to any sale unless agreed in writing. Users are responsible for verifying ownership, legality and local transfer rules.</p>
<h2>Reports and services</h2><p>Free reports are provided at our discretion. Paid services, if offered, are described before purchase.</p>
<h2>User submissions</h2><p>You confirm you have the right to submit content and grant us a non-exclusive licence to use it for the stated purpose. Don't submit unlawful, infringing or personal data of others.</p>
<h2>Intellectual property</h2><p>See the <a href="{R}legal.html">Trademark &amp; Copyright Disclosure</a>.</p>
<h2>Liability</h2><p>To the extent permitted by law, 345789.com is not liable for indirect or consequential losses arising from use of the site.</p>
<h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>'''))

add(path="404.html", noindex=True, title="Page not found | 345789", desc="This page doesn't exist.",
body='<section class="hero"><div class="narrow center"><h1>4<span>0</span>4</h1><p class="lead" style="margin-inline:auto">Of course it has a 4 in it. Let&rsquo;s get you somewhere luckier.</p><p><a class="btn btn-p" href="{R}index.html">Home</a> <a class="btn btn-o" href="{R}tools/index.html">Tools</a></p></div></section>')
