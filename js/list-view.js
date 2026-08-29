// Client-side filtering + sorting for card-grid list pages.
// Works on any page with [data-filter-bar] + [data-card-grid]:
// reads data-* attributes off each .agent-card, filters on input/select change.
(function () {
  const bar = document.querySelector("[data-filter-bar]");
  const grid = document.querySelector("[data-card-grid]");
  if (!bar || !grid) return;

  const cards = Array.from(grid.querySelectorAll(".agent-card"));
  const search = bar.querySelector("[data-filter-search]");
  const selects = Array.from(bar.querySelectorAll("[data-filter-select]"));
  const sortSel = bar.querySelector("[data-filter-sort]");
  const countEl = bar.querySelector("[data-filter-count]");
  const emptyEl = document.querySelector("[data-filter-empty]");
  const SOURCE = bar.dataset.source; // "agents-only" etc. (reserved)

  // Populate license/platform dropdowns from the data present on the page
  for (const sel of selects) {
    const field = sel.dataset.field;
    const values = new Set();
    for (const c of cards) {
      const v = (c.dataset[field] || "").trim();
      if (field === "platforms") {
        v.split(",").forEach((p) => p.trim() && values.add(p.trim()));
      } else if (v) {
        values.add(v);
      }
    }
    const first = sel.querySelector("option");
    Array.from(values)
      .filter(Boolean)
      .sort((a, b) => a.localeCompare(b))
      .forEach((v) => {
        const o = document.createElement("option");
        o.value = v;
        o.textContent = v;
        sel.appendChild(o);
      });
  }

  function norm(s) {
    return (s || "").toLowerCase().trim();
  }

  function cardMatches(c) {
    const q = norm(search.value);
    if (q) {
      const hay = norm(c.dataset.name + " " + c.dataset.maker + " " + c.dataset.language + " " + (c.dataset.platforms || ""));
      // substring match on every token
      if (!q.split(/\s+/).every((tok) => hay.includes(tok))) return false;
    }
    for (const sel of selects) {
      const v = sel.value;
      if (!v) continue;
      const field = sel.dataset.field;
      const val = c.dataset[field] || "";
      if (field === "platforms") {
        if (!val.split(",").map((p) => p.trim()).includes(v)) return false;
      } else if (val !== v) {
        return false;
      }
    }
    return true;
  }

  function applySort(list) {
    const mode = sortSel ? sortSel.value : "name";
    const sorted = list.slice();
    if (mode === "stars") {
      sorted.sort((a, b) => (parseInt(b.dataset.stars, 10) || 0) - (parseInt(a.dataset.stars, 10) || 0));
    } else if (mode === "released") {
      sorted.sort((a, b) => (b.dataset.released || "").localeCompare(a.dataset.released || ""));
    } else {
      sorted.sort((a, b) => (a.dataset.name || "").localeCompare(b.dataset.name || ""));
    }
    return sorted;
  }

  function render() {
    const visible = applySort(cards.filter(cardMatches));
    for (const c of cards) c.hidden = true;
    for (const c of visible) c.hidden = false;
    // reorder DOM to match sort
    for (const c of visible) grid.appendChild(c);
    if (countEl) countEl.textContent = visible.length + " of " + cards.length + " shown";
    if (emptyEl) emptyEl.hidden = visible.length > 0;
  }

  let debounce;
  search.addEventListener("input", () => {
    clearTimeout(debounce);
    debounce = setTimeout(render, 120);
  });
  selects.forEach((s) => s.addEventListener("change", render));
  if (sortSel) sortSel.addEventListener("change", render);
  render();
})();
