/* 345789.com — shared UI */
(function () {
  "use strict";
  var S = window.SITE || {};
  var $ = function (q, c) { return (c || document).querySelector(q); };
  var $$ = function (q, c) { return Array.prototype.slice.call((c || document).querySelectorAll(q)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function sstore(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  window.$q = $; window.$$q = $$;

  /* contact routing (never rendered) */
  function route() { return (window.__k || []).slice().reverse().map(function (c) { return String.fromCharCode(c ^ 0x5A); }).join(""); }

  /* theme */
  var saved = store("theme"); if (saved) document.documentElement.setAttribute("data-theme", saved);
  function themeIcon() { var t = document.documentElement.getAttribute("data-theme"); var dark = t ? t === "dark" : matchMedia("(prefers-color-scheme: dark)").matches; $$(".theme-t").forEach(function (b) { b.textContent = dark ? "☀" : "☾"; b.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode"); }); }
  document.addEventListener("click", function (e) {
    var t = e.target.closest(".theme-t"); if (!t) return;
    var cur = document.documentElement.getAttribute("data-theme");
    var dark = cur ? cur === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    var next = dark ? "light" : "dark"; document.documentElement.setAttribute("data-theme", next); store("theme", next); themeIcon();
  });

  /* toast */
  window.toast = function (msg) { var t = $(".toast"); if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); } t.textContent = msg; t.classList.add("on"); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("on"); }, 3200); };

  document.addEventListener("DOMContentLoaded", function () {
    themeIcon();
    /* nav drawer */
    var nav = $(".nav"), scrim = $(".scrim"), burger = $(".burger");
    function close() { nav && nav.classList.remove("open"); scrim && scrim.classList.remove("on"); burger && burger.setAttribute("aria-expanded", "false"); }
    burger && burger.addEventListener("click", function () { var o = nav.classList.toggle("open"); scrim.classList.toggle("on", o); burger.setAttribute("aria-expanded", o); });
    scrim && scrim.addEventListener("click", close);
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { close(); $$(".modal.on").forEach(function (m) { m.classList.remove("on"); }); } });
    /* active link */
    var here = location.pathname.replace(/\/index\.html$/, "/");
    $$(".nav a").forEach(function (a) { var p = a.pathname.replace(/\/index\.html$/, "/"); if (p === here) a.classList.add("active"); });
    /* year */
    $$(".yr").forEach(function (e) { e.textContent = new Date().getFullYear(); });
    /* reveal */
    if ("IntersectionObserver" in window) { var io = new IntersectionObserver(function (es) { es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }); }, { threshold: .08 }); $$(".reveal").forEach(function (el) { io.observe(el); }); }
    else $$(".reveal").forEach(function (el) { el.classList.add("in"); });
    /* email-us links (assembled at click) */
    $$("[data-mail]").forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); location.href = "mai" + "lto:" + route() + "?subject=" + encodeURIComponent(a.getAttribute("data-mail") || "345789.com inquiry"); }); });
    /* tabs / segmented */
    $$("[data-seg]").forEach(function (seg) { seg.addEventListener("click", function (e) { var b = e.target.closest("button"); if (!b) return; $$("button", seg).forEach(function (x) { x.classList.toggle("on", x === b); x.setAttribute("aria-pressed", x === b); }); seg.dispatchEvent(new CustomEvent("segchange", { detail: b.dataset.v })); }); });
    /* share */
    $$("[data-share]").forEach(function (b) { b.addEventListener("click", function () { var d = { title: document.title, url: location.href }; if (navigator.share) navigator.share(d).catch(function () {}); else { try { navigator.clipboard.writeText(location.href); toast("Link copied"); } catch (e) {} } }); });
    ads(); videos(); forms(); donate(); leadModal(); hydrateHidden();
    if (S.GA4) { var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + S.GA4; document.head.appendChild(g); window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", S.GA4); }
  });

  /* ---------- ads ---------- */
  function ads() {
    var slots = $$(".ad-slot"); if (!slots.length) return;
    var root = document.body.getAttribute("data-root") || "";
    if (S.ADSENSE_CLIENT) {
      var sc = document.createElement("script"); sc.async = true; sc.crossOrigin = "anonymous";
      sc.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + S.ADSENSE_CLIENT; document.head.appendChild(sc);
      slots.forEach(function (el) {
        var kind = el.getAttribute("data-ad") || "inContent";
        var ins = document.createElement("ins"); ins.className = "adsbygoogle"; ins.style.display = "block";
        ins.setAttribute("data-ad-client", S.ADSENSE_CLIENT);
        if (S.AD_SLOTS && S.AD_SLOTS[kind]) ins.setAttribute("data-ad-slot", S.AD_SLOTS[kind]);
        ins.setAttribute("data-ad-format", "auto"); ins.setAttribute("data-full-width-responsive", "true");
        el.innerHTML = ""; el.appendChild(ins); try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
      });
    } else {
      var house = [
        ["Your brand here", "Reach people who care about luck, prosperity & numbers.", "advertise.html", "Advertise"],
        ["Own a lucky number?", "List your numeric domain, plate or phone number free.", "marketplace.html", "List it free"],
        ["Free Lucky Number Report", "Personal numbers, dates & directions — by email.", "get-your-report.html", "Get my report"],
        ["Keep this lab free", "Support research, prizes and new tools.", "donate.html", "Support us"]
      ];
      slots.forEach(function (el, i) { var h = house[(i + (location.pathname.length % 4)) % house.length]; el.innerHTML = '<div class="house"><b>' + h[0] + '</b><span>' + h[1] + '</span><a class="btn btn-sm btn-p" href="' + root + h[2] + '">' + h[3] + '</a></div>'; });
    }
  }

  /* ---------- YouTube ---------- */
  function lite(el, id, title) {
    el.innerHTML = '<img loading="lazy" alt="' + (title || "Video") + '" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><button aria-label="Play video">▶</button>';
    el.addEventListener("click", function () { el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (title || "YouTube video") + '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }, { once: true });
  }
  function videos() {
    var V = S.VIDEOS || [];
    $$("[data-yt]").forEach(function (el) {
      var topic = el.getAttribute("data-yt"), v = V.filter(function (x) { return !topic || x.topic === topic; })[0] || V[0];
      if (v) { el.classList.add("yt"); lite(el, v.id, v.title); }
      else {
        var q = el.getAttribute("data-q") || "chinese lucky numbers";
        el.outerHTML = '<a class="card vcard" target="_blank" rel="noopener" href="https://www.youtube.com/results?search_query=' + encodeURIComponent(q) + '"><div class="vthumb">' + (el.getAttribute("data-glyph") || "八") + '</div><h3>Watch: ' + q.replace(/\b\w/g, function (c) { return c.toUpperCase(); }) + '</h3><p>Curated videos on YouTube — our own channel is launching soon.</p></a>';
      }
    });
    var hub = $("#video-hub");
    if (hub && V.length) {
      hub.innerHTML = V.map(function (v) { return '<div class="card"><div class="yt" data-id="' + v.id + '" data-t="' + v.title + '"></div><h3 style="margin-top:12px">' + v.title + '</h3><span class="badge">' + v.topic + '</span></div>'; }).join("");
      $$(".yt", hub).forEach(function (el) { lite(el, el.dataset.id, el.dataset.t); });
    }
  }

  /* ---------- forms ---------- */
  function hydrateHidden() {
    var p = new URLSearchParams(location.search);
    $$("form[data-form]").forEach(function (f) {
      ["utm_source", "utm_medium", "utm_campaign"].forEach(function (k) { if (p.get(k)) addHidden(f, k, p.get(k)); });
      addHidden(f, "page", location.pathname); addHidden(f, "referrer", document.referrer || "direct");
      var pre = p.get("number"); if (pre) $$("[name=number]", f).forEach(function (i) { if (!i.value) i.value = pre; });
    });
  }
  function addHidden(f, k, v) { var i = f.querySelector('input[name="' + k + '"]'); if (!i) { i = document.createElement("input"); i.type = "hidden"; i.name = k; f.appendChild(i); } i.value = v; }
  function forms() {
    $$("form[data-form]").forEach(function (f) {
      f.addEventListener("submit", function (e) {
        e.preventDefault();
        var msg = f.querySelector(".form-msg");
        if (f.querySelector('[name="_honey"]') && f.querySelector('[name="_honey"]').value) return;
        if (!f.checkValidity()) { f.reportValidity(); return; }
        var data = {}; new FormData(f).forEach(function (v, k) { if (k === "_honey") return; data[k] = data[k] ? data[k] + ", " + v : v; });
        data._subject = "[345789.com] " + (f.getAttribute("data-form") || "Form") + " — " + (data.name || data.email || "new submission");
        data._template = "table"; data._captcha = "false"; data.form = f.getAttribute("data-form");
        var btn = f.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
        fetch("https://formsubmit.co/ajax/" + route(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
          .then(function (r) { return r.json().catch(function () { return {}; }); })
          .then(function () { done(true); })
          .catch(function () { done(false); });
        function done(ok) {
          if (btn) { btn.disabled = false; btn.textContent = btn._t; }
          if (ok) {
            if (msg) { msg.className = "form-msg ok"; msg.textContent = f.getAttribute("data-ok") || "Thank you! Your message has been received — we reply within 48 hours."; }
            toast("Sent ✓"); f.reset(); f.dispatchEvent(new CustomEvent("sent"));
            if (window.gtag) gtag("event", "generate_lead", { form: data.form });
          } else {
            if (msg) { msg.className = "form-msg err"; msg.innerHTML = 'Network issue — <a href="#" class="mail-fallback">open your email app</a> to send this instead.'; var a = msg.querySelector(".mail-fallback"); a.addEventListener("click", function (ev) { ev.preventDefault(); location.href = "mai" + "lto:" + route() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(Object.keys(data).filter(function (k) { return k[0] !== "_"; }).map(function (k) { return k + ": " + data[k]; }).join("\n")); }); }
          }
        }
      });
    });
    /* multi-step */
    $$("[data-steps]").forEach(function (f) {
      var steps = $$(".step", f), bars = $$(".steps i", f), cur = 0;
      function show(i, quiet) { cur = i; steps.forEach(function (s, k) { s.classList.toggle("on", k === i); }); bars.forEach(function (b, k) { b.classList.toggle("on", k <= i); }); f.dispatchEvent(new CustomEvent("step", { detail: i })); if (!quiet) { var top = f.getBoundingClientRect().top + scrollY - 100; if (Math.abs(scrollY - top) > 300) scrollTo({ top: top, behavior: "smooth" }); } }
      f.addEventListener("click", function (e) {
        if (e.target.closest("[data-next]")) { e.preventDefault(); var ok = $$("input,select,textarea", steps[cur]).every(function (i) { return i.checkValidity() || (i.reportValidity(), false); }); if (ok) show(Math.min(cur + 1, steps.length - 1)); }
        if (e.target.closest("[data-prev]")) { e.preventDefault(); show(Math.max(cur - 1, 0)); }
      });
      var pre = new URLSearchParams(location.search).get("need");
      if (pre) { var r = f.querySelector('input[name="need"][value="' + pre + '"]'); if (r) r.checked = true; }
      f.addEventListener("sent", function () { show(0); });
      show(0, true);
    });
    /* newsletter quick forms reuse same handler via data-form */
  }

  /* ---------- donations ---------- */
  function donate() {
    var D = S.DONATE || {}, box = $("#donate-links"); if (!box) return;
    var map = { paypal: "PayPal", kofi: "Ko-fi", bmac: "Buy Me a Coffee", stripe: "Card (Stripe)", crypto: "Crypto" };
    var links = Object.keys(map).filter(function (k) { return D[k]; });
    box.innerHTML = links.length ? links.map(function (k) { return '<a class="btn btn-o" target="_blank" rel="noopener" href="' + D[k] + '">' + map[k] + '</a>'; }).join("") : '<p class="small muted">Instant payment buttons are being activated. Use the pledge form below — we reply within 24 h with secure payment options (PayPal, card, bank transfer, crypto).</p>';
    var G = S.DONATION_GOAL; var gb = $("#goal"); if (gb && G) { var pct = Math.min(100, Math.round(G.raised / G.goal * 100)); gb.innerHTML = '<div class="meta"><b>' + G.label + '</b><span>$' + G.raised + ' of $' + G.goal + ' (' + pct + '%)</span></div><div class="progress" role="progressbar" aria-valuenow="' + pct + '" aria-valuemin="0" aria-valuemax="100"><i style="width:' + Math.max(pct, 2) + '%"></i></div>'; }
    $$("[data-amount]").forEach(function (b) { b.addEventListener("click", function () { var a = $("#pledge-amount"); if (a) { a.value = b.getAttribute("data-amount"); a.focus(); $("#pledge").scrollIntoView({ behavior: "smooth" }); } }); });
  }

  /* ---------- lead modal (once per session, tool pages) ---------- */
  function leadModal() {
    var m = $("#lead-modal"); if (!m) return;
    if (sstore("lm")) return;
    function open() { if (sstore("lm")) return; sstore("lm", "1"); m.classList.add("on"); }
    var fired = false;
    addEventListener("scroll", function () { if (fired) return; var p = (scrollY + innerHeight) / document.body.scrollHeight; if (p > .7) { fired = true; setTimeout(open, 600); } }, { passive: true });
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 5 && !fired) { fired = true; open(); } });
    m.addEventListener("click", function (e) { if (e.target === m || e.target.closest(".x")) m.classList.remove("on"); });
  }
})();
