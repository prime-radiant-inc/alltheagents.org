---
name: "pi-extensions"
slug: "pi-extensions"
layout: "agent.njk"
category: "agent"
maker: "ogulcancelik"
license: "MIT"
url: "https://github.com/ogulcancelik/pi-extensions"
source_code_url: "https://github.com/ogulcancelik/pi-extensions"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-17"
current_release: "2026-08-14"
stars: "405"
language: "TypeScript"
homepage: "https://github.com/ogulcancelik/pi-extensions"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "yes"
plan_mode: "no"
model_providers: "whatever the host pi session uses (pi is multi-provider)"
pricing: "Free / open-source"
install_method: "pi install npm:@ogulcancelik/<package-name>"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ogulcancelik/pi-extensions"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "A working collection of extensions for the pi terminal coding agent, ranging from core daily drivers to experimental utilities (e.g., pi-codex-subagents for session-scoped subagents, pi-goal for parallel worker agents, pi-model-thinking)."
---

pi-extensions grew out of one developer's daily use of pi, and the collection's organization reflects that: packages are ranked by how often the author actually uses them, from a minimal footer with context and subscription gauges to experimental utilities that may disappear. Functionally the packages fill gaps in pi's core — searching past sessions, context-aware Bash permissions with automated guardian review, session-scoped Codex-shaped subagents, Codex-style remote compaction via pi's compaction lifecycle, and Herdr worktree management. Each package installs individually through pi's package manager, so users pick only what they need rather than adopting a bundle. The MIT-licensed repo is moderately active with 400+ stars, and its audience is pi users who want the ecosystem's extensions from one maintained source rather than hunting across npm.
