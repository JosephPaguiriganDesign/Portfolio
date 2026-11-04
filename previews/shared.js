(function () {
  var btn = document.querySelector("[data-menu]");
  var nav = document.querySelector("[data-nav]");
  if (btn && nav) {
    function setOpen(open) {
      nav.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("nav-lock", open);
    }
    btn.addEventListener("click", function () {
      setOpen(!nav.classList.contains("is-open"));
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        setOpen(false);
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) setOpen(false);
    });
  }

  var themeBtn = document.querySelector("[data-theme-toggle]");
  if (themeBtn) {
    var root = document.documentElement;
    function apply(theme) {
      root.setAttribute("data-theme", theme);
      var dark = theme === "dark";
      themeBtn.setAttribute("aria-pressed", dark ? "true" : "false");
      themeBtn.textContent = dark ? "Light mode" : "Dark mode";
    }
    apply(localStorage.getItem("jp-theme") || "light");
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      localStorage.setItem("jp-theme", next);
      apply(next);
    });
  }

  var dialog = document.querySelector("[data-lightbox]");
  if (dialog && typeof dialog.showModal === "function") {
    var img = dialog.querySelector("img");
    var cap = dialog.querySelector("[data-lb-title]");
    var count = dialog.querySelector("[data-lb-count]");
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-gallery]"));
    var i = 0;
    function show(n) {
      if (!cards.length) return;
      i = (n + cards.length) % cards.length;
      var c = cards[i];
      img.src = c.getAttribute("data-img");
      img.alt = c.getAttribute("data-alt") || "";
      cap.textContent = c.getAttribute("data-title") || "";
      count.textContent = (i + 1) + " / " + cards.length;
    }
    cards.forEach(function (c, n) {
      c.addEventListener("click", function () {
        show(n);
        dialog.showModal();
      });
    });
    dialog.querySelector("[data-lb-prev]").addEventListener("click", function () { show(i - 1); });
    dialog.querySelector("[data-lb-next]").addEventListener("click", function () { show(i + 1); });
    dialog.querySelector("[data-lb-close]").addEventListener("click", function () { dialog.close(); });
    dialog.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); show(i + 1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); show(i - 1); }
    });
    dialog.addEventListener("click", function (e) {
      if (e.target === dialog) dialog.close();
    });
  }
})();
