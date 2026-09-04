module.exports = function(eleventyConfig) {
  // The entry template is documentation, not an entry — keep it out of the build
  // entirely (collections, pages, and the agents.json search index pipeline).
  eleventyConfig.ignores.add("agents/_TEMPLATE.md");

  // Internal docs and agent pointer files are not site pages.
  eleventyConfig.ignores.add("docs/**");
  eleventyConfig.ignores.add("AGENTS.md");
  eleventyConfig.ignores.add("CLAUDE.md");

  // Passthrough for static assets
  eleventyConfig.addPassthroughCopy("css");
  eleventyConfig.addPassthroughCopy("js");
  // Custom domain for GitHub Pages — must land in the built output
  eleventyConfig.addPassthroughCopy("CNAME");

  // Collection: all agent harnesses (only category === "agent")
  eleventyConfig.addCollection("agent", function(collectionApi) {
    return collectionApi.getFilteredByGlob("agents/*.md").filter(
      item => item.data.category === "agent"
    );
  });

  // Collection: all published entries (for the /all/ page — every category except "other")
  eleventyConfig.addCollection("all-entries", function(collectionApi) {
    return collectionApi.getFilteredByGlob("agents/*.md").filter(
      item => item.data.category !== undefined && item.data.category !== "other"
    );
  });

  // Filter: build the homepage search index from a collection, so it can never
  // drift from the published entries (fields match what index.njk's Fuse setup uses)
  eleventyConfig.addFilter("searchIndex", function(items) {
    return (items || []).map(item => {
      const d = item.data;
      const body = String(item.rawInput || "").replace(/^---[\s\S]*?---\s*/, "");
      return {
        name: d.name,
        slug: d.slug,
        category: d.category,
        maker: d.maker,
        license: d.license,
        language: d.language,
        stars: d.stars,
        description: body.trim().slice(0, 200),
      };
    });
  });

  // Collection: multiplexers (tools that orchestrate/run other agent harnesses)
  eleventyConfig.addCollection("multiplexer", function(collectionApi) {
    return collectionApi.getFilteredByGlob("agents/*.md").filter(
      item => item.data.category === "multiplexer"
    );
  });

  // Collection: agent SDKs / frameworks (build-your-own-agent toolkits; ship no coding agent)
  eleventyConfig.addCollection("agent-sdk", function(collectionApi) {
    return collectionApi.getFilteredByGlob("agents/*.md").filter(
      item => item.data.category === "agent-sdk"
    );
  });

  // Filter: entries sharing a maker (for related-entries sidebars)
  eleventyConfig.addFilter("filterByMaker", function(collection, maker) {
    if (!maker || !collection) return [];
    return collection.filter(item => item.data && item.data.maker === maker);
  });

  // Filter: format date
  eleventyConfig.addFilter("dateFmt", function(dateStr) {
    if (!dateStr || dateStr === "null") return "—";
    return dateStr;
  });

  // Filter: format stars
  eleventyConfig.addFilter("starFmt", function(stars) {
    if (!stars || stars === "null") return "—";
    if (stars >= 1000) return (stars / 1000).toFixed(1) + "k";
    return stars.toString();
  });

  // Filter: format an integer with thousands separators (1347 -> "1,347")
  eleventyConfig.addFilter("numFmt", function(n) {
    const num = Number(n);
    return Number.isFinite(num) ? num.toLocaleString("en-US") : n;
  });

  // Filter: size (for arrays/collections)
  eleventyConfig.addFilter("size", function(arr) {
    if (!arr) return 0;
    if (arr.length !== undefined) return arr.length;
    if (typeof arr === 'object') return Object.keys(arr).length;
    return 0;
  });

  // Filter: keys (for objects)
  eleventyConfig.addFilter("keys", function(obj) {
    return Object.keys(obj || {});
  });

  // Filter: sort by stars descending
  eleventyConfig.addFilter("sortByStars", function(arr) {
    return [...arr].sort((a, b) => (b.data.stars || 0) - (a.data.stars || 0));
  });

  // Filter: sort by name
  eleventyConfig.addFilter("sortByName", function(arr) {
    return [...arr].sort((a, b) => (a.data.name || "").localeCompare(b.data.name || ""));
  });

  // Filter: sort by date
  eleventyConfig.addFilter("sortByDate", function(arr) {
    return [...arr].sort((a, b) => (b.data.first_released || "").localeCompare(a.data.first_released || ""));
  });

  // Filter: group by
  eleventyConfig.addFilter("groupBy", function(arr, key) {
    const groups = {};
    for (const item of arr) {
      const val = item.data[key];
      if (Array.isArray(val)) {
        for (const v of val) {
          if (!groups[v]) groups[v] = [];
          groups[v].push(item);
        }
      } else {
        const v = val || "Unknown";
        if (!groups[v]) groups[v] = [];
        groups[v].push(item);
      }
    }
    return groups;
  });

  // Filter: filter open source
  eleventyConfig.addFilter("isOpenSource", function(arr) {
    return arr.filter(item => {
      const lic = item.data.license;
      return lic && !["Proprietary", "Unknown", "null", ""].includes(lic);
    });
  });

  eleventyConfig.addFilter("isProprietary", function(arr) {
    return arr.filter(item => {
      const lic = item.data.license;
      return lic === "Proprietary";
    });
  });

  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts",
      data: "_data",
    },
    pathPrefix: "/",
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
