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
  var animated = document.querySelectorAll("[data-animate], [data-animate-group]");
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

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isTouch = window.matchMedia && window.matchMedia("(hover: none), (pointer: coarse)").matches;

  /* ---------- Animated stat counters ---------- */
  var counters = document.querySelectorAll("[data-count]");
  if ("IntersectionObserver" in window && counters.length && !reduceMotion) {
    var countIO = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var target = parseInt(el.getAttribute("data-count"), 10) || 0;
          var suffix = el.getAttribute("data-suffix") || "";
          var duration = 1400;
          var start = null;
          function step(ts) {
            if (!start) start = ts;
            var progress = Math.min((ts - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.round(eased * target) + suffix;
            if (progress < 1) requestAnimationFrame(step);
          }
          requestAnimationFrame(step);
          countIO.unobserve(el);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) { countIO.observe(el); });
  }

  /* ---------- Magnetic buttons ---------- */
  if (!isTouch && !reduceMotion) {
    document.querySelectorAll(".btn-magnetic").forEach(function (btn) {
      btn.addEventListener("mousemove", function (e) {
        var r = btn.getBoundingClientRect();
        var x = e.clientX - r.left - r.width / 2;
        var y = e.clientY - r.top - r.height / 2;
        btn.style.transform = "translate(" + x * 0.18 + "px," + y * 0.35 + "px)";
      });
      btn.addEventListener("mouseleave", function () { btn.style.transform = ""; });
    });
  }

  /* ---------- Tilt cards ---------- */
  if (!isTouch && !reduceMotion) {
    document.querySelectorAll(".tilt-card").forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = "perspective(700px) rotateX(" + (-py * 6) + "deg) rotateY(" + (px * 8) + "deg) translateY(-4px)";
      });
      card.addEventListener("mouseleave", function () { card.style.transform = ""; });
    });
  }

  /* ---------- Hero glow parallax ---------- */
  if (!isTouch && !reduceMotion) {
    var hero = document.querySelector(".hero");
    var glows = hero ? hero.querySelectorAll(".nova-glow") : [];
    if (hero && glows.length) {
      hero.addEventListener("mousemove", function (e) {
        var r = hero.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        glows.forEach(function (g, i) {
          var depth = i % 2 === 0 ? 22 : -16;
          g.style.transform = "translate(" + px * depth + "px," + py * depth + "px)";
        });
      });
    }
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
