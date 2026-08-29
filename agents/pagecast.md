---
name: "pagecast"
slug: "pagecast"
layout: "agent.njk"
category: "other"
maker: "Amal-David"
license: "MIT"
url: "https://github.com/Amal-David/pagecast"
source_code_url: "https://github.com/Amal-David/pagecast"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-06-04"
current_release: "2026-08-18"
stars: "187"
language: "JavaScript (Node.js)"
homepage: "https://pagecasthq.pages.dev"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "False"
hooks: "True"
plan_mode: "no"
model_providers: "none (tool is model-agnostic; invoked by coding agents via an MCP server mode and a publish-report skill)"
pricing: "Free / open-source"
install_method: "npx pagecast (no global install); or docker ghcr.io/amal-david/pagecast:latest; or from source npm start"
docs_url: "https://pagecasthq.pages.dev/"
plugin_docs_url: null
config_docs_url: "https://github.com/Amal-David/pagecast/blob/main/ARCHITECTURE.md"
download_url: "https://www.npmjs.com/package/pagecast"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Local-first publishing tool that previews HTML reports, Markdown docs, and static mini apps, then publishes them to shareable Cloudflare Pages URLs from the terminal or coding agents. Context-aware publishing (upserts update same URL in same agent session), edge-level password protection, immutable deploy history, activity analytics, and integrations via MCP, Claude Code plugin, and Codex skill."
---

Coding agents generate HTML reports, dashboards, and static demos that are awkward to share: screenshots lose fidelity, and full hosting setups are disproportionate for a disposable artifact. Pagecast runs locally (npx pagecast, or Docker), previews the artifact in an admin UI, and publishes it to a shareable Cloudflare Pages URL after a one-time scoped OAuth connection or API-token setup. Edge Functions enforce optional password protection, links expire after a default 30 days, and deploy history supports pruning and revocation; self-hosted analytics via a Worker plus D1 are optional. Coding agents integrate directly through an MCP server mode and a publish-report skill listed on Skills.sh, so a Claude Code or Codex session can publish mid-task. Static assets only — server-rendered apps need a backend and are out of scope. Developers and agents that need fast, access-controlled, disposable sharing of generated pages are the audience, under an MIT license.
