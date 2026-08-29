---
name: "druk"
slug: "druk"
layout: "agent.njk"
category: "other"
maker: "letstri"
license: "MIT"
url: "https://github.com/letstri/druk"
source_code_url: "https://github.com/letstri/druk"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-07-24"
current_release: "2026-08-19"
stars: "596"
language: "TypeScript"
homepage: "https://druk.sh"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "binary"
docs_url: "https://druk.sh"
plugin_docs_url: null
config_docs_url: null
download_url: "https://druk.letstri.dev/install"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Self-contained single binary terminal code editor with file tree, tabs, fuzzy file open, project search/replace, PDF viewer, git integration (gutter marks, diffs, commit/push), markdown rendering, vim mode, review notes system (JSON-based, readable by external agents), extension market for 30+ languages and themes"
---

Druk compresses a GUI-class editor into one static binary that runs in any terminal: file tree, tabs, fuzzy open, project search/replace, tree-sitter highlighting for 30+ languages, language-server integration, inline diff and gutter git marks, PDF tabs, and a vim mode — with mouse support throughout and no runtime dependency on Node or Bun. Its one concession to the agent era is the review system: line-anchored issue/suggestion/question notes persist in review.json, and a coding agent reading that file can post threaded answers that appear live in the panel while druk is open. Everything else is a conventional, keyboard-first editor for developers who live in the terminal and want zero dependencies.
