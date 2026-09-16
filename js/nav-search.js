// Global nav search: Fuse over the /agents.json index, top-8 dropdown.
// Runs on every page (loaded from _layouts/base.njk). No-ops when the
// nav search box is absent.
(function () {
  var input = document.getElementById("nav-search");
  var box = document.getElementById("nav-search-results");
  if (!input || !box) return;
  var wrap = input.closest(".nav-search");
  var indexUrl = (wrap && wrap.dataset.indexUrl) || "/agents.json";
  var agentBase = (wrap && wrap.dataset.agentBase) || "/agents/";

  fetch(indexUrl)
    .then(function (r) { return r.json(); })
    .then(function (data) {
      // Fuse is loaded from CDN in base.njk before this script.
      if (typeof Fuse === "undefined") return;
      var fuse = new Fuse(data, {
        keys: ["name", "maker", "description", "license", "language"],
        threshold: 0.3,
        includeScore: true,
      });

      function starFmt(n) {
        if (n === null || n === undefined) return "";
        return n >= 1000 ? (n / 1000).toFixed(1) + "k" : String(n);
      }

      // Truncate at a word boundary with an ellipsis; never cut mid-word.
      function trunc(s, n) {
        if (!s || s.length <= n) return s || "";
        return s.slice(0, n).replace(/\s+\S*$/, "") + "…";
      }

      input.addEventListener("input", function () {
        var q = input.value.trim();
        if (!q) {
          box.classList.remove("open");
          box.innerHTML = "";
          return;
        }
        var matches = fuse.search(q).slice(0, 8);
        box.innerHTML = matches.map(function (m) {
          var item = m.item;
          var meta = [item.maker, item.stars ? "★ " + starFmt(item.stars) : ""]
            .filter(Boolean).join(" · ");
          return (
            '<a class="search-result" style="display:block;color:inherit" href="' +
            agentBase + item.slug + '/">' +
            "<div><strong>" + item.name + "</strong>" +
            ' <span class="badge badge-cat badge-cat-' + item.category + '">' +
            item.category + "</span>" +
            (meta ? ' <span class="result-meta">' + meta + "</span>" : "") +
            "</div>" +
            (item.description
              ? '<p class="result-desc">' + trunc(item.description, 110) + "</p>"
              : "") +
            "</a>"
          );
        }).join("") || '<p class="nav-search-none">No matches.</p>';
        box.classList.add("open");
      });

      document.addEventListener("click", function (e) {
        if (!e.target.closest(".nav-search")) box.classList.remove("open");
      });
      input.addEventListener("keydown", function (e) {
        if (e.key === "Escape") box.classList.remove("open");
      });
    });
})();
