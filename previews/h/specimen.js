(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hero = document.getElementById("specimen");
  var cut = document.getElementById("cut");
  var cuts = document.querySelectorAll(".cut");
  if (!hero) return;

  var faces = {
    cover: { name: "Fraunces", family: '"Fraunces", Georgia, serif' },
    sce: { name: "Barlow Condensed", family: '"Barlow Condensed", "Arial Narrow", sans-serif' },
    hire: { name: "Source Sans 3", family: '"Source Sans 3", "Source Sans Pro", sans-serif' },
    force: { name: "Big Shoulders Stencil", family: '"Big Shoulders Stencil Display", Impact, sans-serif' },
    halo: { name: "Share Tech Mono", family: '"Share Tech Mono", ui-monospace, monospace' }
  };

  function apply(key) {
    var face = faces[key] || faces.cover;
    cuts.forEach(function (el) { el.style.fontFamily = face.family; });
    hero.classList.toggle("is-swap", key !== "cover");
    if (cut) cut.textContent = face.name;
    if (key !== "cover") hero.style.fontVariationSettings = "normal";
  }

  function restore() {
    cuts.forEach(function (el) { el.style.fontFamily = ""; });
    hero.classList.remove("is-swap");
    hero.style.fontVariationSettings = "";
    if (cut) cut.textContent = faces.cover.name;
  }

  document.querySelectorAll("[data-face]").forEach(function (row) {
    var key = row.getAttribute("data-face");
    row.addEventListener("pointerenter", function () { apply(key); });
    row.addEventListener("pointerleave", function () {
      if (document.activeElement !== row) restore();
    });
    row.addEventListener("focus", function () { apply(key); });
    row.addEventListener("blur", restore);
  });

  if (reduce) return;

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      if (hero.classList.contains("is-swap")) return;
      var t = Math.min(1, (window.scrollY || 0) / 520);
      var opsz = (144 - t * 96).toFixed(1);
      var wght = (720 - t * 240).toFixed(0);
      var soft = (8 + t * 50).toFixed(0);
      hero.style.fontVariationSettings = '"opsz" ' + opsz + ', "wght" ' + wght + ', "SOFT" ' + soft;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();
