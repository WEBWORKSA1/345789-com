/* =========================================================
   345789.com — site configuration (edit this file only)
   ========================================================= */
window.SITE = {
  name: "345789 · The Lucky Number Lab",
  domain: "345789.com",
  partnerContact: "https://web.works/contact",

  /* Google AdSense — paste your publisher id (e.g. "ca-pub-1234567890123456") after approval.
     Leave empty to show house ads that promote /advertise.html. */
  ADSENSE_CLIENT: "",
  AD_SLOTS: { inContent: "", sidebar: "", footer: "" },   // AdSense ad-unit slot ids

  /* YouTube — channel URL and video ids to embed. Empty list = curated topic cards. */
  YOUTUBE_CHANNEL: "https://www.youtube.com/results?search_query=chinese+lucky+numbers",
  VIDEOS: [
    // { id: "VIDEO_ID", title: "What does 8 really mean?", topic: "meanings" },
  ],

  /* Donation links (optional). Empty = pledge form is used instead. */
  DONATE: { paypal: "", kofi: "", bmac: "", stripe: "", crypto: "" },
  DONATION_GOAL: { label: "October 2026 operations goal", raised: 0, goal: 888 },

  /* Analytics (optional) — GA4 measurement id e.g. "G-XXXXXXX" */
  GA4: ""
};

/* Contact routing — obfuscated; assembled only at runtime. Do not replace with plain text. */
window.__k = [55,53,57,116,54,51,59,55,61,26,107,59,41,49,40,53,45,56,63,45];
