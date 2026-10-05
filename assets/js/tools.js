/* 345789.com — interactive tools (requires numbers.js + app.js) */
(function () {
  "use strict";
  var L = window.LNL, $ = window.$q, $$ = window.$$q;
  var root = document.body.getAttribute("data-root") || "";
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function chip(t, cls) { return '<span class="chip ' + (cls || "") + '">' + t + '</span>'; }
  function cls(sc) { return sc > 0 ? "good" : sc < 0 ? "bad" : "mid"; }

  /* ---------- generic analyser ---------- */
  function renderAnalysis(r, ctx) {
    if (!r) return '<p class="muted">Enter at least one digit.</p>';
    var h = '<div class="score-wrap"><div class="gauge" style="--p:' + r.score + '"><span>' + r.score + '</span></div><div><div class="grade"><span class="zh">' + r.grade.zh + '</span> · ' + r.grade.en + '</div>' +
      '<div class="muted">Reading: <span class="zh">' + r.zh + '</span> · <i>' + r.py + '</i></div>' +
      '<div class="chips">' + chip(r.input.length + " digits") + (r.counts[8] ? chip(r.counts[8] + "× 8 发", "good") : "") + (r.counts[4] ? chip(r.counts[4] + "× 4 死", "bad") : "") + (r.counts[9] ? chip(r.counts[9] + "× 9 久", "good") : "") + (r.counts[6] ? chip(r.counts[6] + "× 6 顺", "good") : "") + '</div></div></div>';
    if (r.input.length <= 16) h += '<div class="digit-row">' + r.perDigit.map(function (d) { return '<div class="dcell ' + (d.score > 0.6 ? "pos" : d.score < 0 ? "neg" : "") + '"><b>' + d.d + '</b><span class="zh">' + d.zh.split(" ")[0] + '</span><small>' + esc(d.short) + '</small></div>'; }).join("") + '</div>';
    if (r.combos.length) h += '<h4>Meaningful combinations</h4><div class="chips">' + r.combos.map(function (c) { return chip('<b>' + c.p + '</b> <span class="zh">' + c.zh + '</span> — ' + esc(c.meaning), cls(c.score)); }).join("") + '</div>';
    if (r.patterns.length) h += '<h4>Patterns</h4><div class="chips">' + r.patterns.map(function (p) { return chip(esc(p.label), cls(p.score)); }).join("") + '</div>';
    if (r.warnings.length) h += '<h4>Watch-outs</h4><ul>' + r.warnings.map(function (w) { return '<li>' + esc(w) + '</li>'; }).join("") + '</ul>';
    h += '<h4>Suggestions</h4><ul>' + r.suggestions.map(function (w) { return '<li>' + esc(w) + '</li>'; }).join("") + '</ul>';
    h += '<div class="chips" style="margin-top:14px"><a class="btn btn-p btn-sm" href="' + root + 'get-your-report.html?number=' + r.input + '&need=' + (ctx === "domain" ? "domain-valuation" : "personal-report") + '">Get the full expert report →</a><button class="btn btn-o btn-sm" data-copy>Copy result</button></div>';
    h += '<p class="small muted" style="margin-top:10px">Cultural tradition &amp; entertainment — not financial advice. <a href="' + root + 'methodology.html">How we score</a>.</p>';
    return h;
  }
  window.renderAnalysis = renderAnalysis;

  $$("[data-analyser]").forEach(function (box) {
    var ctx = box.getAttribute("data-analyser"), inp = $("input.an-in", box), out = $(".result", box), dialect = "mandarin", teo = false;
    var seg = $("[data-seg]", box);
    function prep(v) {
      v = L.clean(v);
      if (ctx === "phone" && v.length > 8) { return v; }
      return v;
    }
    function run(push) {
      var v = prep(inp.value); if (!v) { out.innerHTML = ""; return; }
      var r = L.analyse(v, { dialect: dialect, teochew: teo, context: ctx });
      var extra = "";
      if (ctx === "phone" && v.length > 6) { var last4 = L.analyse(v.slice(-4), { dialect: dialect }); var pr = L.phoneReading(v); extra = '<div class="note" style="margin-bottom:12px"><b>Last 4 digits (' + v.slice(-4) + '):</b> ' + last4.score + '/100 · ' + last4.grade.en + '. In China the final 4 digits are judged most. Read aloud as: <span class="zh">' + pr.zh + '</span> <i>' + pr.py + '</i></div>'; }
      if (ctx === "plate") extra = '<div class="note" style="margin-bottom:12px">Letters are ignored; digits analysed: <b>' + v + '</b>. Hong Kong auction research links an 8 on a plate to a ~65% price premium.</div>';
      if (ctx === "house" && /4/.test(v)) extra = '<div class="note" style="margin-bottom:12px">Many Chinese buyers avoid addresses containing 4 — Vancouver data showed a 2.2% discount for addresses ending in 4.</div>';
      out.innerHTML = extra + renderAnalysis(r, ctx);
      var cp = $("[data-copy]", out); if (cp) cp.addEventListener("click", function () { try { navigator.clipboard.writeText(v + " — " + r.score + "/100 " + r.grade.zh + " (" + r.grade.en + ") via 345789.com"); toast("Copied"); } catch (e) {} });
      if (push && history.replaceState) history.replaceState(null, "", "?n=" + v);
    }
    $("form", box).addEventListener("submit", function (e) { e.preventDefault(); run(true); });
    inp.addEventListener("input", function () { if (L.clean(inp.value).length >= 2) run(false); });
    if (seg) seg.addEventListener("segchange", function (e) { dialect = e.detail === "cantonese" ? "cantonese" : "mandarin"; teo = e.detail === "teochew"; run(false); });
    var q = new URLSearchParams(location.search).get("n"); if (q) { inp.value = q; run(false); } else if (box.hasAttribute("data-demo")) { inp.value = box.getAttribute("data-demo"); run(false); }
  });

  /* ---------- numeric domain valuer ---------- */
  var dt = $("#domain-tool");
  if (dt) {
    var di = $("input", dt), dout = $(".result", dt);
    function rd() {
      var raw = di.value.trim().toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "");
      var name = raw.split(".")[0], tld = raw.indexOf(".") > -1 ? raw.slice(raw.indexOf(".")) : ".com";
      if (!/^\d+$/.test(name)) { dout.innerHTML = '<p class="form-msg err" style="display:block">Enter an all-numeric domain, e.g. 345789.com or 8868.net</p>'; return; }
      var p = L.domainProfile(name);
      dout.innerHTML = '<div class="score-wrap"><div class="gauge" style="--p:' + ({ A: 95, B: 78, C: 58, D: 38, E: 18 }[p.tier]) + '"><span>' + p.tier + '</span></div><div><div class="grade">' + esc(name + tld) + ' · ' + p.cls + '</div><div class="muted">Chinese-market premium tier ' + p.tier + ' (A = top) · number-luck score ' + p.analysis.score + '/100 <span class="zh">' + p.analysis.grade.zh + '</span></div>' +
        (tld !== ".com" ? '<div class="chips">' + chip("Non-.com: expect a fraction of .com pricing", "mid") + '</div>' : "") + '</div></div>' +
        '<h4>Signals</h4><ul>' + p.notes.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join("") + '</ul>' +
        '<h4>Historic reference range (' + p.cls + ' .com)</h4><p>' + esc(p.reference) + ' <a href="' + root + 'guides/numeric-domain-investing.html">Sources &amp; method</a>.</p>' +
        '<div class="chips"><a class="btn btn-p btn-sm" href="' + root + 'get-your-report.html?need=domain-valuation&number=' + encodeURIComponent(name + tld) + '">Request a free pro valuation →</a><a class="btn btn-o btn-sm" href="' + root + 'marketplace.html?number=' + encodeURIComponent(name + tld) + '#sell">List it for sale free</a></div>' +
        '<p class="small muted">Indicative only — not an appraisal. Real prices depend on live comparable sales and buyer demand.</p>';
    }
    $("form", dt).addEventListener("submit", function (e) { e.preventDefault(); rd(); });
    var dq = new URLSearchParams(location.search).get("d"); di.value = dq || "345789.com"; rd();
  }

  /* ---------- converter ---------- */
  var ct = $("#converter-tool");
  if (ct) {
    var ci = $("input", ct), co = $(".result", ct);
    function rc() {
      var v = L.clean(ci.value); if (!v) { co.innerHTML = ""; return; }
      var pr = L.phoneReading(v);
      co.innerHTML = '<div class="tbl-wrap"><table class="tbl"><tr><th>Format</th><th>Result</th></tr>' +
        '<tr><td>Chinese numerals (小写)</td><td class="zh" style="font-size:1.3rem">' + L.toChinese(v) + '</td></tr>' +
        '<tr><td>Financial / cheque (大写)</td><td class="zh" style="font-size:1.3rem">' + L.toChinese(v, true) + (v.length < 17 ? '元整' : '') + '</td></tr>' +
        '<tr><td>Digit-by-digit (phone style)</td><td><span class="zh">' + pr.zh + '</span><br><i>' + pr.py + '</i></td></tr>' +
        '<tr><td>Cantonese (Jyutping)</td><td><i>' + pr.jp + '</i></td></tr>' +
        '<tr><td>Luck reading</td><td>' + L.analyse(v).score + '/100 · <span class="zh">' + L.analyse(v).grade.zh + '</span> <a href="' + root + 'tools/number-meaning-analyzer.html?n=' + v + '">details</a></td></tr></table></div>';
    }
    ci.addEventListener("input", rc); $("form", ct).addEventListener("submit", function (e) { e.preventDefault(); rc(); }); ci.value = "345789"; rc();
  }

  /* ---------- zodiac + personal numbers ---------- */
  var CNY = null;
  function loadCNY(cb) { if (CNY) return cb(CNY); fetch(root + "assets/data/cny.json").then(function (r) { return r.json(); }).then(function (j) { CNY = j; cb(j); }).catch(function () { cb({}); }); }
  var zt = $("#zodiac-tool");
  if (zt) {
    $("form", zt).addEventListener("submit", function (e) {
      e.preventDefault(); var v = $("input[type=date]", zt).value; if (!v) return;
      var p = v.split("-").map(Number);
      loadCNY(function (c) {
        var z = L.zodiacFor(p[0], p[1], p[2], c), a = z.animal;
        var cn = c[z.year] ? " (Lunar New Year " + z.year + ": " + c[z.year].slice(0, 2) + "/" + c[z.year].slice(2) + ")" : "";
        $(".result", zt).innerHTML = '<div class="score-wrap"><div class="gauge" style="--p:100"><span class="zh">' + a.zh + '</span></div><div><div class="grade">' + z.element + ' ' + a.en + ' <span class="zh">' + z.elementZh + a.zh + '</span></div><div class="muted">Zodiac year ' + z.year + cn + ' · ' + z.yin + '</div></div></div>' +
          '<div class="grid g2" style="margin-top:16px"><div class="card"><h3>Lucky numbers</h3><div class="chips">' + a.lucky.map(function (n) { return chip(n, "good"); }).join("") + '</div><h3>Unlucky numbers</h3><div class="chips">' + a.unlucky.map(function (n) { return chip(n, "bad"); }).join("") + '</div></div>' +
          '<div class="card"><h3>Personality</h3><p>' + a.trait + '</p><h3 style="margin-top:10px">Lucky colours</h3><p>' + a.colors + '</p><h3 style="margin-top:10px">Best matches</h3><p>' + a.best + '</p></div></div>' +
          '<p style="margin-top:14px"><a class="btn btn-p btn-sm" href="' + root + 'get-your-report.html?need=personal-report">Get my full personal lucky-number report →</a></p>';
      });
    });
  }
  var lt = $("#lucky-tool");
  if (lt) {
    $("form", lt).addEventListener("submit", function (e) {
      e.preventDefault(); var v = $("input[type=date]", lt).value, gsel = $("select", lt).value; if (!v) return;
      var p = v.split("-").map(Number);
      loadCNY(function (c) {
        var z = L.zodiacFor(p[0], p[1], p[2], c), k = L.kua(p[0], p[1], p[2], gsel);
        var life = String(p[0]) + String(p[1]) + String(p[2]); var lp = life.split("").reduce(function (s, x) { return s + +x; }, 0); while (lp > 9) lp = String(lp).split("").reduce(function (s, x) { return s + +x; }, 0);
        var names = ["Sheng Qi 生气 — wealth & success", "Tian Yi 天医 — health", "Yan Nian 延年 — love & relationships", "Fu Wei 伏位 — personal growth"];
        var bad = ["Huo Hai 祸害 — mishaps", "Wu Gui 五鬼 — conflict", "Liu Sha 六煞 — setbacks", "Jue Ming 绝命 — total loss"];
        $(".result", lt).innerHTML = '<div class="grid g3"><div class="card"><div class="ic">' + z.animal.zh + '</div><h3>' + z.element + ' ' + z.animal.en + '</h3><p>Zodiac lucky digits</p><div class="chips">' + z.animal.lucky.map(function (n) { return chip(n, "good"); }).join("") + '</div><p>Avoid</p><div class="chips">' + z.animal.unlucky.map(function (n) { return chip(n, "bad"); }).join("") + '</div></div>' +
          '<div class="card"><div class="ic">卦</div><h3>Kua number ' + k.kua + '</h3><p>' + k.info.group + ' group (feng shui year ' + k.year + ')</p><ul class="small">' + k.info.dir.map(function (d, i) { return '<li><b>' + d + '</b> — ' + names[i] + '</li>'; }).join("") + '</ul></div>' +
          '<div class="card"><div class="ic">数</div><h3>Birth-date digit ' + lp + '</h3><p>Your date digits reduce to <b>' + lp + '</b>: ' + L.DIGITS[lp].short + '.</p><p class="small">Directions to avoid: ' + k.info.bad.map(function (d, i) { return d + ' (' + bad[i].split(" — ")[0] + ')'; }).join(", ") + '</p></div></div>' +
          '<p style="margin-top:14px"><a class="btn btn-p btn-sm" href="' + root + 'get-your-report.html?need=personal-report">Email me a personalised report →</a></p>';
      });
    });
  }

  /* ---------- almanac / lucky date finder ---------- */
  var at = $("#almanac-tool");
  if (at) {
    var EN = { "祭祀":"Ancestral offerings","沐浴":"Bathing / cleansing","纳财":"Receiving wealth","牧养":"Raising livestock","补垣":"Repairing walls","覃恩":"Granting favours","雪冤":"Clearing grievances","筑堤防":"Building embankments","缮城郭":"Repairing city walls","安抚边境":"Securing borders","塞穴":"Sealing holes","裁制":"Tailoring","恤孤茕":"Helping the needy","选将":"Appointing leaders","嫁娶":"Wedding","上表章":"Submitting proposals","修置产室":"Preparing a nursery","开渠":"Digging channels","穿井":"Digging a well","破土":"Breaking ground","安葬":"Burial","启攒":"Exhumation","修仓库":"Repairing storage","出师":"Launching a campaign","上册":"Registration","营建":"Construction","疗目":"Eye treatment","针刺":"Acupuncture","布政事":"Policy making","诸事不宜":"Avoid major events","出行":"Travel","结婚姻":"Marriage arrangements","宴会":"Banquets / parties","上官":"Taking office","进人口":"Hiring / adopting","竖柱上梁":"Raising the roof beam","经络":"Weaving","扫舍宇":"House cleaning","栽种":"Planting","颁诏":"Announcements","纳采":"Betrothal gifts","临政":"Governing","解除":"Cleansing / removing","祈福":"Praying for blessings","宣政事":"Public announcements","招贤":"Recruiting talent","举正直":"Promoting the honest","求嗣":"Praying for children","施恩":"Charity","立券交易":"Signing contracts & trading","庆赐":"Celebrations","酝酿":"Brewing","搬移":"Moving house","剃头":"Haircut","冠带":"Coming-of-age ceremony","畋猎":"Hunting","取鱼":"Fishing","修造":"Renovation","开市":"Opening a business","修宫室":"Repairing halls","远回":"Returning from afar","安床":"Placing a bed","求医疗病":"Seeing a doctor","安碓硙":"Installing a mill","破屋坏垣":"Demolition","修饰垣墙":"Decorating walls","开仓":"Opening a warehouse","纳畜":"Acquiring animals","整容":"Grooming / beauty","整手足甲":"Manicure","入宅":"Moving into a new home","鼓铸":"Metal casting","平治道涂":"Road repair","乘船渡水":"Boat travel","捕捉":"Catching","赴任":"Starting a new job","诉讼":"Lawsuits","苫盖":"Roofing","立券":"Signing agreements","伐木":"Felling trees","开张":"Grand opening","入学":"Starting school","诸事不忌":"No restrictions" };
    var LV = { "0": ["Excellent day", "q0"], "1": ["Good day", "q1"], "2": ["Fair day", "q2"], "3": ["Mixed — caution", "q3"], "4": ["Poor day", "q4"], "5": ["Very poor day", "q5"], "-1": ["Neutral day", "q2"] };
    var CLASH = { "鼠":"Rat","牛":"Ox","虎":"Tiger","兔":"Rabbit","龙":"Dragon","蛇":"Snake","马":"Horse","羊":"Goat","猴":"Monkey","鸡":"Rooster","狗":"Dog","猪":"Pig" };
    var LM = ["", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"];
    var ALM = null, view = new Date(), sel = null, purpose = "";
    var mSel = $("#alm-month"), pSel = $("#alm-purpose"), grid = $("#alm-grid"), det = $("#alm-detail"), sum = $("#alm-summary");
    var start = new Date(2026, 0, 1), end = new Date(2028, 11, 31);
    if (view < start || view > end) view = new Date(2026, 0, 1);
    for (var y = 2026; y <= 2028; y++) for (var m = 0; m < 12; m++) { var o = document.createElement("option"); o.value = y + "-" + m; o.textContent = new Date(y, m, 1).toLocaleString("en", { month: "long", year: "numeric" }); mSel.appendChild(o); }
    mSel.value = view.getFullYear() + "-" + view.getMonth();
    function decodeAlm(j) {
      if (j.days) return j;
      var A = [], V = {}; for (var c = 40; c < 126; c++) if (c !== 92) A.push(String.fromCharCode(c));
      A.forEach(function (ch, i) { V[ch] = i; });
      var S = "甲乙丙丁戊己庚辛壬癸", B = "子丑寅卯辰巳午未申酉戌亥", Z = "鼠牛虎兔龙蛇马羊猴鸡狗猪";
      var days = j.d.split("#").map(function (s, i) {
        var p = s.slice(4).split("!"), n = (j.anchor + i) % 60, br = n % 12;
        return [V[s[0]], V[s[1]], s[2] === "1" ? 1 : 0, S[n % 10] + B[br], Z[br] + "日冲" + Z[(br + 6) % 12],
          p[0].split("").map(function (x) { return V[x]; }), p[1].split("").map(function (x) { return V[x]; }), V[s[3]] - 1, j.st[i] || ""];
      });
      return { terms: j.terms, days: days };
    }
    function idx(d) { return Math.round((Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) - Date.UTC(2026, 0, 1)) / 864e5); }
    function rec(d) { return ALM.days[idx(d)]; }
    function tr(list) { return list.map(function (i) { var t = ALM.terms[i]; return (EN[t] || t) + ' <span class="zh small muted">' + t + '</span>'; }); }
    function good(r, pIdx) { return pIdx.some(function (i) { return r[5].indexOf(i) > -1; }) && r[7] <= 2; }
    function draw() {
      var ym = mSel.value.split("-").map(Number), first = new Date(ym[0], ym[1], 1), days = new Date(ym[0], ym[1] + 1, 0).getDate();
      var pIdx = purpose ? purpose.split("|").map(function (t) { return ALM.terms.indexOf(t); }).filter(function (i) { return i > -1; }) : [];
      var h = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].map(function (d) { return '<div class="dh">' + d + '</div>'; }).join("");
      for (var i = 0; i < first.getDay(); i++) h += '<div class="empty"></div>';
      var matches = [];
      for (var d = 1; d <= days; d++) {
        var dt = new Date(ym[0], ym[1], d), r = rec(dt), q = LV[String(r[7])], mt = pIdx.length && good(r, pIdx);
        if (mt) matches.push(d);
        var isSel = sel && sel.getTime() === dt.getTime();
        h += '<button type="button" data-d="' + d + '" class="' + q[1] + (mt ? " match" : "") + (isSel ? " sel" : "") + '" aria-label="' + dt.toDateString() + ', ' + q[0] + '"><b>' + d + '</b><small>' + (r[2] ? "闰" : "") + LM[r[0]].replace(/\D+/, "") + "/" + r[1] + '</small>' + (r[8] ? '<small>' + r[8] + '</small>' : "") + '</button>';
      }
      grid.innerHTML = h;
      sum.innerHTML = purpose ? (matches.length ? '<b>' + matches.length + ' recommended day(s)</b> for ' + pSel.options[pSel.selectedIndex].text.toLowerCase() + ' this month: ' + matches.join(", ") + ' (outlined in gold).' : 'No strongly recommended days for this purpose this month — try the next month.') : 'Pick a purpose to highlight the best days. Green = traditionally favourable days.';
    }
    function detail(dt) {
      var r = rec(dt), q = LV[String(r[7])], clash = r[4].replace(/.*冲/, "");
      var lmn = r[0], ghost = lmn === 7 && !r[2];
      var dstr = String(dt.getFullYear()) + String(dt.getMonth() + 1).padStart(2, "0") + String(dt.getDate()).padStart(2, "0");
      var nr = L.analyse(dstr);
      det.innerHTML = '<div class="card"><div class="meta"><span class="badge' + (r[7] >= 4 ? " r" : "") + '">' + q[0] + '</span><span>' + dt.toDateString() + '</span></div>' +
        '<h3 style="margin-top:10px">Lunar ' + (r[2] ? "leap " : "") + LM[lmn] + ' month, day ' + r[1] + ' · Day pillar <span class="zh">' + r[3] + '</span></h3>' +
        '<p>Clashes with: <b>' + (CLASH[clash] || clash) + '</b> <span class="zh">(' + r[4] + ')</span> — people born in that year traditionally avoid big events today.' + (r[8] ? ' Solar term: <span class="zh">' + r[8] + '</span>.' : '') + (ghost ? ' <b>Ghost Month</b> — weddings and moves are traditionally avoided.' : '') + '</p>' +
        '<div class="grid g2"><div><h4>✓ Favourable for</h4><ul class="small">' + tr(r[5]).map(function (x) { return '<li>' + x + '</li>'; }).join("") + '</ul></div><div><h4>✕ Avoid</h4><ul class="small">' + tr(r[6]).slice(0, 14).map(function (x) { return '<li>' + x + '</li>'; }).join("") + (r[6].length > 14 ? '<li>…and ' + (r[6].length - 14) + ' more</li>' : '') + '</ul></div></div>' +
        '<p class="small">Date digits <b>' + dstr + '</b> score ' + nr.score + '/100 (' + nr.grade.en + ').</p>' +
        '<a class="btn btn-p btn-sm" href="' + root + 'get-your-report.html?need=date-selection">Get a personalised date shortlist →</a></div>';
    }
    grid.addEventListener("click", function (e) { var b = e.target.closest("button[data-d]"); if (!b) return; var ym = mSel.value.split("-").map(Number); sel = new Date(ym[0], ym[1], +b.dataset.d); draw(); detail(sel); });
    mSel.addEventListener("change", draw); pSel.addEventListener("change", function () { purpose = pSel.value; draw(); });
    $("#alm-prev").addEventListener("click", function () { if (mSel.selectedIndex > 0) { mSel.selectedIndex--; draw(); } });
    $("#alm-next").addEventListener("click", function () { if (mSel.selectedIndex < mSel.options.length - 1) { mSel.selectedIndex++; draw(); } });
    fetch(root + "assets/data/almanac.json").then(function (r) { return r.json(); }).then(function (j) { ALM = decodeAlm(j); draw(); var t = new Date(); t = new Date(t.getFullYear(), t.getMonth(), t.getDate()); if (t >= start && t <= end) { sel = t; draw(); detail(t); } }).catch(function () { grid.innerHTML = '<p>Could not load almanac data. Please refresh.</p>'; });
  }

  /* ---------- combo dictionary search ---------- */
  var cs = $("#combo-search");
  if (cs) {
    var tb = $("#combo-table tbody"), si = $("input", cs), fl = "all";
    function rows() {
      var q = si.value.trim().toLowerCase();
      tb.innerHTML = L.COMBOS.filter(function (c) { var s = c[1]; if (fl === "lucky" && s <= 0) return false; if (fl === "unlucky" && s >= 0) return false; return !q || (c[0] + c[3] + c[4]).toLowerCase().indexOf(q) > -1; })
        .map(function (c) { return '<tr><td><a href="' + root + 'tools/number-meaning-analyzer.html?n=' + c[0] + '"><b>' + c[0] + '</b></a></td><td class="zh">' + c[3] + '</td><td>' + esc(c[4]) + '</td><td>' + chip(c[1] > 0 ? "Lucky" : c[1] < 0 ? "Unlucky" : "Neutral", cls(c[1])) + (c[1] !== c[2] ? ' ' + chip("Cantonese: " + (c[2] > 0 ? "lucky" : c[2] < 0 ? "unlucky" : "neutral"), cls(c[2])) : "") + '</td></tr>'; }).join("") || '<tr><td colspan="4">No match — try the <a href="' + root + 'tools/number-meaning-analyzer.html">analyser</a>.</td></tr>';
    }
    si.addEventListener("input", rows); var sg = $("[data-seg]", cs); if (sg) sg.addEventListener("segchange", function (e) { fl = e.detail; rows(); }); rows();
  }

  /* ---------- lucky number of the day ---------- */
  $$("[data-lotd]").forEach(function (el) {
    var t = new Date(), seed = t.getFullYear() * 1000 + (t.getMonth() + 1) * 50 + t.getDate();
    var good = L.COMBOS.filter(function (c) { return c[1] >= 2; }), c = good[seed % good.length];
    el.innerHTML = '<div class="meta"><span class="badge">Today · ' + t.toLocaleDateString("en", { month: "short", day: "numeric" }) + '</span></div><div style="font-size:2.6rem;font-weight:800;margin:6px 0">' + c[0] + '</div><div class="zh" style="font-size:1.2rem">' + c[3] + '</div><p class="muted">' + esc(c[4]) + '</p><a class="btn btn-sm btn-o" href="' + root + 'tools/number-meaning-analyzer.html?n=' + c[0] + '">Analyse it</a>';
  });
})();
