/* 345789 Number Intelligence Engine — original work, cultural/entertainment use */
(function (g) {
  "use strict";
  var DIGITS = [
    { d:0, zh:"零", py:"líng", jp:"ling4", sound:"良 liáng (good) · 圆 completeness", score:1,
      short:"Wholeness, a fresh start", long:"Zero represents completeness and the beginning of all things. Trailing zeros make numbers look round, rich and prestigious (e.g. 8000), though a leading zero can feel like 'nothing' in front." },
    { d:1, zh:"一", py:"yī / yāo", jp:"jat1", sound:"要 yào (will / want) in combos · 'first place'", score:0.5,
      short:"Leadership, 'will', number one", long:"One means unity and being first. In combinations it is often read 'yāo' and heard as 要 'will/want', so 18 = 'will prosper'. Alone it can suggest loneliness (Singles' Day is 11/11)." },
    { d:2, zh:"二 / 两", py:"èr / liǎng", jp:"ji6", sound:"易 easy (Cantonese) · 'good things come in pairs'", score:1,
      short:"Harmony, pairs, ease", long:"Chinese culture loves pairs — double happiness, paired couplets, twin lions. In Cantonese 2 sounds like 易 'easy', so 28 = 'easy prosperity'. Avoid 250, a classic insult meaning 'fool'." },
    { d:3, zh:"三", py:"sān", jp:"saam1", sound:"生 life/birth (Cantonese saang) · 散 scatter (Mandarin sàn)", score:0.5,
      short:"Life & growth — or scattering", long:"Three is two-sided. Cantonese speakers hear 生 'life, birth, growth'; Mandarin speakers can hear 散 'to break apart'. In combos it usually reads as 'life': 3344 = 生生世世 'life after life'." },
    { d:4, zh:"四", py:"sì", jp:"sei3", sound:"死 sǐ / séi — death", score:-3,
      short:"The most avoided digit", long:"Four sounds almost exactly like 死 'death', so many East Asian buildings skip 4th, 14th and 24th floors and buyers pay less for addresses ending in 4. Notable exception: in Teochew culture 4 echoes 喜 'happiness' and is lucky." },
    { d:5, zh:"五", py:"wǔ", jp:"ng5", sound:"吾/我 me, I · 无 none · Five Elements", score:0,
      short:"Balance, the self, the Five Elements", long:"Five is the number of the Five Elements and imperial symbolism. In combos it often means 'I/me' (518 = 'I will prosper', 520 = 'I love you'), but it can also mean 'not' (Cantonese 唔), flipping a phrase's meaning." },
    { d:6, zh:"六", py:"liù", jp:"luk6", sound:"溜/流 smooth flow · 禄 fortune (Cantonese)", score:2,
      short:"Everything goes smoothly", long:"Six means things flow smoothly: 六六大顺 'smooth sailing all the way'. Businesses love 6 and 66 in prices, phone numbers and opening dates; 666 is Chinese internet slang for 'awesome'." },
    { d:7, zh:"七", py:"qī", jp:"cat1", sound:"起 rise · 齐 together · 气 vital energy · 欺 cheat", score:0.5,
      short:"Rising together — with a Ghost-Month caveat", long:"Seven is the number of togetherness (Qixi, the Chinese Valentine's Day, falls on 7/7) and is heard as 起 'to rise'. The 7th lunar month is Ghost Month, and 74 ('angry to death') is avoided." },
    { d:8, zh:"八", py:"bā", jp:"baat3", sound:"发 fā — prosper, get rich", score:3,
      short:"Prosperity — the luckiest digit", long:"Eight sounds like 发 'to prosper'. The Beijing Olympics opened at 8:08:08 pm on 8/8/08, airlines reserve 8-flight numbers for China routes and Hong Kong plates with an 8 sell for far more at auction." },
    { d:9, zh:"九", py:"jiǔ", jp:"gau2", sound:"久 jiǔ — long-lasting, eternal", score:2,
      short:"Longevity and lasting love", long:"Nine sounds like 久 'long-lasting' — a favourite for weddings and long relationships. As the highest single digit it was the emperor's number: the Forbidden City is said to have 9,999 rooms." }
  ];

  // [pattern, mandarin score, cantonese score, reading, meaning]
  var COMBOS = [
    ["5201314",3,3,"我爱你一生一世","I love you for a lifetime"],
    ["1314520",3,3,"一生一世我爱你","A lifetime of love"],
    ["168888",3,3,"一路发发发发","Prosperity all the way, multiplied"],
    ["8888",3,3,"发发发发","Quadruple prosperity"],
    ["1688",3,3,"一路发发","Prosper all the way, twice"],
    ["1314",2,2,"一生一世","One life, one lifetime — forever"],
    ["3344",1,1,"生生世世","Life after life, forever"],
    ["9999",2,2,"久久久久","Everlasting"],
    ["7456",-2,-1,"气死我了","You're making me furious"],
    ["7414",-3,-2,"去死一死","Go and die"],
    ["5354",-1,-2,"唔生唔死","Neither alive nor dead (Cantonese)"],
    ["9413",-1,-1,"九死一生","Nine deaths, one life — a narrow escape"],
    ["888",3,3,"发发发","Triple prosperity"],
    ["666",2,2,"六六六","Smooth all the way · slang for 'awesome'"],
    ["999",2,2,"久久久","Lasting forever"],
    ["168",3,3,"一路发","Prosperity all the way"],
    ["518",3,2,"我要发","I will prosper"],
    ["520",2,2,"我爱你","I love you"],
    ["521",1,1,"我愿意","I'm willing / I do"],
    ["789",2,2,"起发久","Rise, prosper, endure (345789 reading)"],
    ["198",1,1,"要久发","Lasting prosperity"],
    ["514",-3,-2,"我要死","I want to die"],
    ["748",-3,-2,"去死吧","Go to hell"],
    ["448",-2,-2,"死先发","Rich only after death"],
    ["548",-1,-2,"唔使发","No need to prosper (Cantonese)"],
    ["167",-1,-2,"粗口","Vulgar in Cantonese"],
    ["250",-2,-1,"二百五","Fool / idiot (insult)"],
    ["886",0,0,"拜拜了","Bye-bye (texting slang)"],
    ["555",-1,-1,"呜呜呜","Crying (texting slang)"],
    ["233",0,0,"哈哈","LOL (internet slang)"],
    ["345",0,0,"三四五","Ascending start — contains 4"],
    ["88",3,3,"发发 / 囍","Double prosperity · looks like 囍 double happiness"],
    ["66",2,2,"六六大顺","Everything goes smoothly"],
    ["99",2,2,"久久","Forever and ever"],
    ["28",2,3,"易发","Easy prosperity (Cantonese)"],
    ["68",2,2,"路发","Road to fortune"],
    ["18",2,2,"要发 / 实发","Will prosper"],
    ["38",0,2,"生发 · 三八","Growth & wealth (Cantonese) · insult in Mandarin"],
    ["58",2,-1,"我发 · 唔发","I prosper (Mandarin) · won't prosper (Cantonese)"],
    ["98",2,2,"久发","Long-lasting wealth"],
    ["78",1,1,"起发","Rise to prosperity"],
    ["86",1,1,"发路","Path of wealth"],
    ["69",1,1,"顺久","Smooth and lasting"],
    ["14",-3,-3,"要死","Will die"],
    ["24",-2,-3,"易死","Easy to die (Cantonese)"],
    ["44",-3,-3,"死死","Double death"],
    ["74",-2,-2,"气死","Angry to death"],
    ["54",-2,1,"我死 · 唔死","I die (Mandarin) · won't die (Cantonese)"],
    ["94",-1,-1,"久死","Long suffering"],
    ["13",0,1,"实生","Western-unlucky; 'sure to live' (Cantonese)"]
  ];

  function clean(s) { return String(s || "").replace(/[^0-9]/g, ""); }
  function pyRead(s) { return s.split("").map(function (c) { return DIGITS[+c].py.split(" ")[0]; }).join(" "); }
  function zhRead(s) { var z = ["零","一","二","三","四","五","六","七","八","九"]; return s.split("").map(function (c) { return z[+c]; }).join(""); }

  function patterns(s) {
    var out = [], n = s.length;
    if (n >= 3 && /^(\d)\1+$/.test(s)) out.push({ k:"all-same", label:"All-same digits (" + s[0] + "×" + n + ")", score:s[0]==="4"?-6:6 });
    if (/^(\d)\1(\d)\2$/.test(s) && s[0]!==s[2]) out.push({ k:"AABB", label:"AABB pattern", score:3 });
    if (/^(\d)(\d)\1\2$/.test(s) && s[0]!==s[1]) out.push({ k:"ABAB", label:"ABAB pattern", score:3 });
    if (/^(\d)(\d)\2\1$/.test(s) && s[0]!==s[1]) out.push({ k:"ABBA", label:"ABBA mirror", score:2 });
    if (n === 6 && s.slice(0,3) === s.slice(3)) out.push({ k:"ABCABC", label:"ABCABC repeat", score:3 });
    if (n >= 4 && s === s.split("").reverse().join("") && !/^(\d)\1+$/.test(s)) out.push({ k:"palindrome", label:"Palindrome", score:2 });
    var up = 0, dn = 0;
    for (var i = 1; i < n; i++) { if (+s[i] > +s[i-1]) up++; if (+s[i] < +s[i-1]) dn++; }
    if (n >= 3 && up === n - 1) out.push({ k:"ascending", label:"Ascending run — 步步高升 rising step by step", score:4 });
    if (n >= 3 && dn === n - 1) out.push({ k:"descending", label:"Descending run — 'going downhill'", score:-4 });
    var m = s.match(/(\d)\1{2,}/g); if (m && !/^(\d)\1+$/.test(s)) m.forEach(function (r) { out.push({ k:"repeat", label:"Repeater " + r, score:r[0]==="4"?-4:(r[0]==="8"||r[0]==="6"||r[0]==="9")?4:2 }); });
    return out;
  }

  function analyse(input, opts) {
    opts = opts || {};
    var dialect = opts.dialect === "cantonese" ? 2 : 1;
    var s = clean(input);
    if (!s) return null;
    var res = { input:s, perDigit:[], combos:[], patterns:[], warnings:[], suggestions:[], counts:{} };
    var n = s.length, i, j;
    for (i = 0; i < n; i++) { var d0 = DIGITS[+s[i]]; res.counts[d0.d] = (res.counts[d0.d] || 0) + 1; res.perDigit.push(d0); }
    // combos (longest first, non-overlapping greedy)
    var used = new Array(n).fill(0), adj = 0;
    COMBOS.forEach(function (c) {
      var p = c[0], idx = s.indexOf(p);
      while (idx !== -1) {
        var free = true; for (j = idx; j < idx + p.length; j++) if (used[j]) free = false;
        if (free) {
          var sc = c[dialect], atEnd = idx + p.length === n;
          for (j = idx; j < idx + p.length; j++) used[j] = sc;
          res.combos.push({ p:p, zh:c[3], meaning:c[4], score:sc, end:atEnd });
          adj += sc * (3 + p.length * 0.6) * (atEnd ? 1.3 : 1);
        }
        idx = s.indexOf(p, idx + 1);
      }
    });
    var sum = 0, wsum = 0, fours = 0;
    for (i = 0; i < n; i++) {
      var d = DIGITS[+s[i]], w = (i === n - 1) ? 2 : (i === n - 2 ? 1.4 : 1);
      if (used[i]) w *= 0.5;
      var ds = d.score; if (d.d === 4 && opts.teochew) ds = 2;
      sum += ds * w; wsum += w;
      if (d.d === 4 && !opts.teochew && !(used[i] > 0)) fours++;
    }
    res.patterns = patterns(s);
    res.patterns.forEach(function (p) { adj += p.score; });
    adj -= fours * 6;
    var score = Math.round(50 + (sum / wsum) * 11 + adj);
    score = Math.max(1, Math.min(99, score));
    res.score = score;
    res.grade = score >= 85 ? { zh:"大吉", en:"Very auspicious", cls:"good" } :
                score >= 64 ? { zh:"吉", en:"Auspicious", cls:"good" } :
                score >= 45 ? { zh:"平", en:"Balanced / neutral", cls:"mid" } :
                score >= 30 ? { zh:"小凶", en:"Use with caution", cls:"bad" } :
                              { zh:"凶", en:"Inauspicious", cls:"bad" };
    // warnings & suggestions
    if (res.counts[4] && !opts.teochew) res.warnings.push("Contains " + res.counts[4] + "× digit 4 (死 'death' sound) — the single biggest value-killer for Chinese buyers.");
    if (s[n-1] === "4" && !opts.teochew) res.warnings.push("Ends in 4 — endings carry the most weight in Chinese number reading.");
    if (s[0] === "0" && n > 1) res.warnings.push("Leading zero — reads as 'nothing first'; numeric-domain buyers discount it.");
    if (/250/.test(s)) res.warnings.push("Contains 250 (二百五), a common insult.");
    if (res.counts[4] && !opts.teochew) res.suggestions.push("Swap each 4 for an 8 (prosper), 6 (smooth) or 9 (lasting): " + s.replace(/4/g, "8") + ".");
    if (s[n-1] !== "8" && s[n-1] !== "9" && s[n-1] !== "6") res.suggestions.push("Ending on 8, 6 or 9 lifts the reading — e.g. …" + s.slice(Math.max(0, n-3), n-1) + "8.");
    if (!res.counts[8]) res.suggestions.push("Add at least one 8 (发) — research on Hong Kong plates links an 8 to a ~65% price premium.");
    if (res.suggestions.length === 0) res.suggestions.push("Strong number — keep it, protect it, and consider it an asset.");
    res.zh = zhRead(s); res.py = pyRead(s);
    return res;
  }

  /* ---- Numeric domain classifier ---- */
  function domainProfile(input) {
    var s = clean(input), n = s.length;
    if (!s) return null;
    var a = analyse(s);
    var pats = a.patterns.map(function (p) { return p.k; });
    var tier, notes = [];
    var has4 = /4/.test(s), lead0 = s[0] === "0", eights = (s.match(/8/g) || []).length;
    var premium = 0;
    if (!has4) { premium += 2; notes.push("No 4 — the main Chinese-market filter (dealers cite up to −50% when a 4 is present)."); }
    else notes.push("Contains 4 — expect a sharply smaller Chinese buyer pool.");
    if (lead0) { premium -= 1; notes.push("Leading zero — commonly discounted."); }
    if (eights) { premium += Math.min(3, eights); notes.push(eights + "× 8 — each 8 widens buyer interest."); }
    if (/[0]$/.test(s)) { premium += 0.5; notes.push("Trailing 0 reads round and premium."); }
    if (pats.length) { premium += 2; notes.push("Pattern: " + a.patterns.map(function(p){return p.label;}).join(", ") + "."); }
    if (/^[0-9]*[0-35-9]*$/.test(s) && !/[47]/.test(s)) { premium += 0.5; notes.push("'Chinese-premium' digits only (no 4 or 7)."); }
    var len = n <= 2 ? 0 : n === 3 ? 1 : n === 4 ? 2 : n === 5 ? 3 : n === 6 ? 4 : 5;
    var lenScore = [10, 8.5, 6.5, 4.5, 3, 1.5][len];
    var total = lenScore + premium;
    tier = total >= 11 ? "A" : total >= 8 ? "B" : total >= 6 ? "C" : total >= 4 ? "D" : "E";
    var ref = {
      "2N": "Ultra-rare. Historic sales in the six-to-seven-figure range.",
      "3N": "Tens of thousands of USD and up for no-4 names (historic floor, dated).",
      "4N": "Low thousands of USD and up; Chinese-premium 4N trade far higher.",
      "5N": "Ordinary 5N .com wholesale ~US$100+ (2023); patterned 5N can exceed US$4k.",
      "6N": "Most 6N .com sell for tens to low hundreds of USD; patterned/888-ending 6N have reached ~US$7k.",
      "7N+": "Mostly registration-value unless highly patterned or meaningful (e.g. 5201314)."
    }[n <= 6 ? n + "N" : "7N+"];
    return { input:s, len:n, cls: n <= 6 ? n + "N" : n + "N (long)", tier:tier, notes:notes, reference:ref, analysis:a, premium:premium };
  }

  /* ---- Chinese numeral converter ---- */
  function toChinese(numStr, financial) {
    var s = clean(numStr).replace(/^0+(?=\d)/, "");
    if (!s) return "";
    if (s.length > 16) return "(too long)";
    var D = financial ? ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"] : ["零","一","二","三","四","五","六","七","八","九"];
    var U = financial ? ["","拾","佰","仟"] : ["","十","百","千"];
    var BIG = ["","万","亿","万亿"];
    if (s === "0") return D[0];
    var groups = []; for (var i = s.length; i > 0; i -= 4) groups.unshift(s.slice(Math.max(0, i - 4), i));
    var out = "", zeroPending = false;
    groups.forEach(function (gp, gi) {
      var gs = "", gz = false, bigIdx = groups.length - 1 - gi;
      gp = gp.padStart(4, "0");
      if (gp === "0000") { zeroPending = out !== ""; return; }
      for (var k = 0; k < 4; k++) {
        var c = +gp[k];
        if (c === 0) { gz = gs !== "" || out !== ""; continue; }
        if (gz || (zeroPending && gs === "")) gs += D[0];
        gz = false; zeroPending = false;
        gs += D[c] + U[3 - k];
      }
      out += gs + BIG[bigIdx];
    });
    if (!financial) out = out.replace(/^一十/, "十");
    return out;
  }
  var JYUT = ["ling4","jat1","ji6","saam1","sei3","ng5","luk6","cat1","baat3","gau2"];
  function phoneReading(s) {
    s = clean(s);
    var py = ["líng","yāo","èr","sān","sì","wǔ","liù","qī","bā","jiǔ"];
    var zh = ["零","幺","二","三","四","五","六","七","八","九"];
    return { zh: s.split("").map(function(c){return zh[+c];}).join(""), py: s.split("").map(function(c){return py[+c];}).join(" "), jp: s.split("").map(function(c){return JYUT[+c];}).join(" ") };
  }

  /* ---- Zodiac ---- */
  var ANIMALS = [
    { en:"Rat", zh:"鼠", lucky:[2,3], unlucky:[5,9], colors:"Blue, gold, green", best:"Dragon, Monkey, Ox", trait:"Quick-witted, resourceful, versatile" },
    { en:"Ox", zh:"牛", lucky:[1,4], unlucky:[5,6], colors:"White, yellow, green", best:"Rat, Snake, Rooster", trait:"Diligent, dependable, determined" },
    { en:"Tiger", zh:"虎", lucky:[1,3,4], unlucky:[6,7,8], colors:"Blue, grey, orange", best:"Dragon, Horse, Pig", trait:"Brave, confident, competitive" },
    { en:"Rabbit", zh:"兔", lucky:[3,4,6], unlucky:[1,7,8], colors:"Red, pink, purple, blue", best:"Goat, Monkey, Dog, Pig", trait:"Gentle, elegant, responsible" },
    { en:"Dragon", zh:"龙", lucky:[1,6,7], unlucky:[3,8], colors:"Gold, silver, grey-white", best:"Rooster, Rat, Monkey", trait:"Confident, ambitious, charismatic" },
    { en:"Snake", zh:"蛇", lucky:[2,8,9], unlucky:[1,6,7], colors:"Black, red, yellow", best:"Dragon, Rooster", trait:"Wise, intuitive, enigmatic" },
    { en:"Horse", zh:"马", lucky:[2,3,7], unlucky:[1,5,6], colors:"Yellow, green", best:"Tiger, Goat, Rabbit", trait:"Energetic, independent, warm" },
    { en:"Goat", zh:"羊", lucky:[3,4,9], unlucky:[6,7,8], colors:"Brown, red, purple", best:"Rabbit, Horse, Pig", trait:"Calm, gentle, creative" },
    { en:"Monkey", zh:"猴", lucky:[4,9], unlucky:[2,7], colors:"White, blue, gold", best:"Ox, Rabbit", trait:"Clever, curious, playful" },
    { en:"Rooster", zh:"鸡", lucky:[5,7,8], unlucky:[1,3,9], colors:"Gold, brown, yellow", best:"Ox, Snake", trait:"Observant, hardworking, courageous" },
    { en:"Dog", zh:"狗", lucky:[3,4,9], unlucky:[1,6,7], colors:"Red, green, purple", best:"Rabbit", trait:"Loyal, honest, kind" },
    { en:"Pig", zh:"猪", lucky:[2,5,8], unlucky:[1,7], colors:"Yellow, grey, brown, gold", best:"Tiger, Rabbit, Goat", trait:"Generous, compassionate, diligent" }
  ];
  var ELEMENTS = ["Metal","Metal","Water","Water","Wood","Wood","Fire","Fire","Earth","Earth"];
  var ELZH = { Metal:"金", Water:"水", Wood:"木", Fire:"火", Earth:"土" };
  function zodiacFor(y, m, d, cny) {
    var yr = y;
    if (cny && cny[y]) { var md = cny[y]; var cm = +md.slice(0,2), cd = +md.slice(2); if (m < cm || (m === cm && d < cd)) yr = y - 1; }
    else if (m === 1 || (m === 2 && d < 4)) yr = y - 1;
    var a = ANIMALS[((yr - 4) % 12 + 12) % 12];
    var el = ELEMENTS[((yr % 10) + 10) % 10];
    return { year:yr, animal:a, element:el, elementZh:ELZH[el], yin: yr % 2 ? "Yin 阴" : "Yang 阳" };
  }
  var KUA = {
    1:{dir:["SE","E","S","N"],bad:["W","NE","NW","SW"],group:"East"}, 2:{dir:["NE","W","NW","SW"],bad:["E","SE","S","N"],group:"West"},
    3:{dir:["S","N","SE","E"],bad:["SW","NW","NE","W"],group:"East"}, 4:{dir:["N","S","E","SE"],bad:["NW","SW","W","NE"],group:"East"},
    6:{dir:["W","NE","SW","NW"],bad:["SE","E","N","S"],group:"West"}, 7:{dir:["NW","SW","NE","W"],bad:["N","S","SE","E"],group:"West"},
    8:{dir:["SW","NW","W","NE"],bad:["E","SE","S","N"],group:"West"}, 9:{dir:["E","SE","N","S"],bad:["NE","W","SW","NW"],group:"East"}
  };
  function reduce(n) { while (n > 9) n = String(n).split("").reduce(function (a, b) { return a + +b; }, 0); return n; }
  function kua(y, m, d, gender) {
    var yr = (m === 1 || (m === 2 && d < 4)) ? y - 1 : y;   // feng shui year starts ~Feb 4 (Li Chun)
    var r = reduce(yr % 100 === 0 ? 0 : reduce(yr % 100));
    var k;
    if (gender === "m") { k = yr < 2000 ? 10 - r : 9 - r; k = reduce(k === 0 ? 9 : k); if (k === 5) k = 2; }
    else { k = yr < 2000 ? 5 + r : 6 + r; k = reduce(k); if (k === 5) k = 8; }
    return { kua:k, info:KUA[k], year:yr };
  }

  g.LNL = { DIGITS:DIGITS, COMBOS:COMBOS, analyse:analyse, domainProfile:domainProfile, toChinese:toChinese,
            phoneReading:phoneReading, zodiacFor:zodiacFor, ANIMALS:ANIMALS, kua:kua, clean:clean, zhRead:zhRead, pyRead:pyRead };
})(typeof window !== "undefined" ? window : globalThis);
if (typeof module !== "undefined") module.exports = globalThis.LNL;
