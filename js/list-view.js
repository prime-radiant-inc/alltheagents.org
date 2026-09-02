// Client-side filtering + sorting + pagination for card-grid list pages.
// Works on any page with [data-filter-bar] + [data-card-grid]: reads data-*
// attributes off each .agent-card, filters on input/select change, then
// paginates the filtered result into pages of a user-selectable size.
(function () {
  const bar = document.querySelector("[data-filter-bar]");
  const grid = document.querySelector("[data-card-grid]");
  if (!bar || !grid) return;

  const cards = Array.from(grid.querySelectorAll(".agent-card"));
  const search = bar.querySelector("[data-filter-search]");
  const selects = Array.from(bar.querySelectorAll("[data-filter-select]"));
  const sortSel = bar.querySelector("[data-filter-sort]");
  const sizeSel = bar.querySelector("[data-filter-pagesize]");
  const countEl = bar.querySelector("[data-filter-count]");
  const pagerEl = document.querySelector("[data-pagination]");
  const emptyEl = document.querySelector("[data-filter-empty]");

  const SIZES = [25, 50, 100];
  const DEFAULT_SIZE = 50;
  const SIZE_KEY = "hc:pagesize";

  let size = DEFAULT_SIZE;
  try {
    const saved = parseInt(localStorage.getItem(SIZE_KEY), 10);
    if (SIZES.indexOf(saved) !== -1) size = saved;
  } catch (e) {}

  let page = readHashPage();

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

  if (sizeSel) {
    sizeSel.value = String(size);
    sizeSel.addEventListener("change", () => {
      const v = parseInt(sizeSel.value, 10);
      size = SIZES.indexOf(v) !== -1 ? v : DEFAULT_SIZE;
      try {
        localStorage.setItem(SIZE_KEY, String(size));
      } catch (e) {}
      resetToFirstPage();
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

  function readHashPage() {
    const m = /[#&]p=(\d+)/.exec(location.hash);
    const n = m ? parseInt(m[1], 10) : 1;
    return n > 0 ? n : 1;
  }

  // Compact page list: 1 … (current-2 … current+2) … last
  function pageWindow(current, total) {
    if (total <= 9) {
      const all = [];
      for (let i = 1; i <= total; i++) all.push(i);
      return all;
    }
    const out = [1];
    if (current > 4) out.push("…");
    const lo = Math.max(2, current - 2);
    const hi = Math.min(total - 1, current + 2);
    for (let i = lo; i <= hi; i++) out.push(i);
    if (current < total - 3) out.push("…");
    out.push(total);
    return out;
  }

  function renderPager(current, total) {
    if (!pagerEl) return;
    if (total <= 1) {
      pagerEl.innerHTML = "";
      return;
    }
    pagerEl.innerHTML = pageWindow(current, total)
      .map((x) => {
        if (x === "…") return '<span class="page-ellipsis">…</span>';
        if (x === current) return '<span class="page-current">' + x + "</span>";
        return '<a href="#p=' + x + '" data-page="' + x + '">' + x + "</a>";
      })
      .join("");
  }

  function renderCount(n) {
    if (!countEl) return;
    if (n === 0) {
      countEl.textContent = "0 shown";
    } else if (n < size) {
      countEl.textContent = n + " of " + n + " shown";
    } else {
      countEl.textContent = n + " shown";
    }
  }

  function render() {
    const matched = applySort(cards.filter(cardMatches));
    const pageCount = Math.max(1, Math.ceil(matched.length / size));
    if (page > pageCount) page = pageCount;
    if (page < 1) page = 1;

    const start = (page - 1) * size;
    const visible = matched.slice(start, start + size);

    for (const c of cards) c.hidden = true;
    for (const c of visible) {
      c.hidden = false;
      grid.appendChild(c); // reorder DOM to match sort
    }

    renderPager(page, pageCount);
    renderCount(visible.length);
    if (emptyEl) emptyEl.hidden = matched.length > 0;
    grid.classList.add("js-paginated"); // release the pre-JS :nth-child cap
  }

  // Filter / sort / size change: back to page 1, drop any #p= from the URL,
  // no new history entry.
  function resetToFirstPage() {
    page = 1;
    try {
      history.replaceState(null, "", location.pathname + location.search);
    } catch (e) {}
    render();
  }

  // Explicit page-link click: new history entry so back/forward works.
  function goToPage(n) {
    page = n;
    try {
      history.pushState({ p: n }, "", n > 1 ? "#p=" + n : location.pathname + location.search);
    } catch (e) {}
    render();
    window.scrollTo(0, 0);
  }

  if (pagerEl) {
    pagerEl.addEventListener("click", (e) => {
      const a = e.target.closest("a[data-page]");
      if (!a) return;
      e.preventDefault();
      goToPage(parseInt(a.dataset.page, 10));
    });
  }

  // Back/forward, and any external or hand-edited #p= change.
  function syncFromHash() {
    page = readHashPage();
    render();
  }
  window.addEventListener("popstate", syncFromHash);
  window.addEventListener("hashchange", syncFromHash);

  let debounce;
  search.addEventListener("input", () => {
    clearTimeout(debounce);
    debounce = setTimeout(resetToFirstPage, 120);
  });
  selects.forEach((s) => s.addEventListener("change", resetToFirstPage));
  if (sortSel) sortSel.addEventListener("change", resetToFirstPage);

  render();
})();
