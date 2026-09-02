// Entries categorized "other" stay in the repo and the README taxonomy but are
// not published on the site: no page, and excluded from every collection.
// Every published entry lives at /agents/<slug>/, the URL cards and search link
// to. Deriving it from the slug also keeps agents/agents.md from being treated
// as the directory index (Eleventy maps dir/dir.md to /dir/ by default).
module.exports = {
  eleventyComputed: {
    permalink: (data) => (data.category === "other" ? false : `/agents/${data.slug}/`),
    eleventyExcludeFromCollections: (data) => data.category === "other",
  },
};
