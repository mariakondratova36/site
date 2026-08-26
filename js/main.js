// =========================================================
// Mobile nav toggle, active-page marker, and EN/RU language
// switcher.
//
// Language model:
//   - Every translatable text element carries data-en / data-ru
//     attributes. Its rendered text always matches data-en on
//     first paint (so the page is correct with JS disabled),
//     then gets swapped in place when the language changes.
//   - Nav links are a special case: they show the *current*
//     language plainly, and reveal the *other* language on
//     hover/focus (see .nav-reveal in css/style.css).
//   - The choice persists via localStorage under "site-lang"
//     so it carries across pages.
// =========================================================
(function () {
  var STORAGE_KEY = "site-lang";

  function getStoredLang() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setStoredLang(lang) {
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {
      /* ignore — private browsing etc. */
    }
  }

  function applyLanguage(lang) {
    var isRu = lang === "ru";
    document.documentElement.setAttribute("lang", isRu ? "ru" : "en");

    // Plain text swaps: anything with data-en/data-ru, excluding nav
    // links (handled separately below) and the always-bilingual
    // page titles (which never swap — both languages stay visible).
    var nodes = document.querySelectorAll(
      "[data-en]:not(.nav-link):not(.lang-en):not(.lang-ru)"
    );
    nodes.forEach(function (el) {
      var text = isRu ? el.getAttribute("data-ru") : el.getAttribute("data-en");
      if (text != null) el.textContent = text;
    });

    // Nav links: primary label shows the current language, the
    // hidden-until-hover reveal shows the other one.
    document.querySelectorAll(".nav-link").forEach(function (link) {
      var en = link.getAttribute("data-en");
      var ru = link.getAttribute("data-ru");
      var primary = link.querySelector(".nav-label-primary");
      var secondary = link.querySelector(".nav-label-secondary");
      if (!primary || !secondary) return;

      primary.textContent = isRu ? ru : en;
      primary.setAttribute("lang", isRu ? "ru" : "en");

      secondary.textContent = isRu ? en : ru;
      secondary.setAttribute("lang", isRu ? "en" : "ru");
    });

    // Document title.
    var titleEn = document.body.getAttribute("data-title-en");
    var titleRu = document.body.getAttribute("data-title-ru");
    if (titleEn) document.title = isRu && titleRu ? titleRu : titleEn;

    // Toggle button active state.
    document.querySelectorAll(".lang-toggle button").forEach(function (btn) {
      var active = btn.getAttribute("data-lang") === (isRu ? "ru" : "en");
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    // ---- Mobile nav toggle ----
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.querySelector(".primary-nav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var isOpen = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      });
    }

    // ---- Mark the current page's nav link ----
    var here = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".primary-nav a").forEach(function (link) {
      if (link.getAttribute("href") === here) link.classList.add("current");
    });

    // ---- Language: apply stored preference, wire up toggle ----
    var lang = getStoredLang() === "ru" ? "ru" : "en";
    applyLanguage(lang);

    document.querySelectorAll(".lang-toggle button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var chosen = btn.getAttribute("data-lang") === "ru" ? "ru" : "en";
        setStoredLang(chosen);
        applyLanguage(chosen);
      });
    });
  });
})();