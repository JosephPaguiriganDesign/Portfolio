(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (!reduce) {
    var root = document.documentElement;
    var onScroll = function () {
      if (window.scrollY > 48) root.classList.add("set");
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    var drifts = document.querySelectorAll("[data-drift]");
    if (drifts.length) {
      var px = 0;
      var py = 0;
      var sy = 0;
      var tx = 0;
      var ty = 0;
      window.addEventListener("pointermove", function (e) {
        tx = e.clientX / window.innerWidth - 0.5;
        ty = e.clientY / window.innerHeight - 0.5;
      }, { passive: true });
      window.addEventListener("scroll", function () {
        sy = window.scrollY || 0;
      }, { passive: true });
      var tick = function () {
        px += (tx - px) * 0.08;
        py += (ty - py) * 0.08;
        drifts.forEach(function (el, i) {
          var depth = (i + 1) * 0.35;
          var y = py * 28 * depth + sy * (0.04 + i * 0.03);
          var x = px * 36 * depth;
          el.style.transform = "translate3d(" + x.toFixed(1) + "px," + y.toFixed(1) + "px,0) rotate(" + el.getAttribute("data-rot") + "deg)";
        });
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }
  }
})();
