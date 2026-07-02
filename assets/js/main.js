/* ==========================================================================
   BLACKNOVA — comportamiento compartido (nav, animaciones, cookies, FAQ)
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- Header scroll state ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 40);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.getElementById("mobileNav");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = toggle.classList.toggle("is-open");
      mobileNav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        toggle.classList.remove("is-open");
        mobileNav.classList.remove("is-open");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Active nav link ---------- */
  var current = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  if (current === "") current = "index.html";
  document.querySelectorAll(".main-nav a, .mobile-nav a").forEach(function (a) {
    var href = (a.getAttribute("href") || "").toLowerCase();
    if (href === current || (current === "index.html" && href === "./")) {
      a.classList.add("is-active");
    }
  });

  /* ---------- Reveal on scroll ---------- */
  var animated = document.querySelectorAll("[data-animate]");
  if ("IntersectionObserver" in window && animated.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    animated.forEach(function (el) { io.observe(el); });
  } else {
    animated.forEach(function (el) { el.classList.add("in-view"); });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    if (!q) return;
    q.addEventListener("click", function () {
      var wasOpen = item.classList.contains("is-open");
      item.closest(".faq-list").querySelectorAll(".faq-item").forEach(function (i) { i.classList.remove("is-open"); });
      if (!wasOpen) item.classList.add("is-open");
    });
  });

  /* ---------- Cookies RGPD/LSSI-CE ----------
     GTM/GA4 solo se cargan tras consentimiento explícito del usuario
     (RGPD art. 6-7 y LSSI-CE art. 22.2). Nunca antes. */
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.bnGtag = gtag;

  function bnLoadAnalytics() {
    if (document.getElementById("gtm-script")) return;
    var s = document.createElement("script");
    s.id = "gtm-script"; s.async = true;
    s.src = "https://www.googletagmanager.com/gtm.js?id=GTM-TBB2N38J";
    document.head.appendChild(s);
    var g = document.createElement("script");
    g.id = "ga-script"; g.async = true;
    g.src = "https://www.googletagmanager.com/gtag/js?id=G-DTP5WXLB81";
    document.head.appendChild(g);
    gtag("js", new Date());
    gtag("config", "G-DTP5WXLB81", { anonymize_ip: true });
  }

  var banner = document.getElementById("cookieBanner");
  var consent = localStorage.getItem("bn_cookie_consent");

  function setConsent(value) {
    localStorage.setItem("bn_cookie_consent", value);
    localStorage.setItem("bn_cookie_consent_date", new Date().toISOString());
    if (banner) banner.classList.remove("is-visible");
    if (value === "all") bnLoadAnalytics();
  }

  if (consent === "all") {
    bnLoadAnalytics();
  } else if (!consent && banner) {
    setTimeout(function () { banner.classList.add("is-visible"); }, 800);
  }

  var acceptBtn = document.getElementById("cookieAccept");
  var rejectBtn = document.getElementById("cookieReject");
  if (acceptBtn) acceptBtn.addEventListener("click", function () { setConsent("all"); });
  if (rejectBtn) rejectBtn.addEventListener("click", function () { setConsent("essential"); });
})();
