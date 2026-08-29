---
name: "onUI"
slug: "onui"
layout: "agent.njk"
category: "other"
maker: "onllm-dev"
license: "GPL-3.0"
url: "https://github.com/onllm-dev/onUI"
source_code_url: "https://github.com/onllm-dev/onUI"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-02-12"
current_release: "2026-04-28"
stars: "94"
language: "TypeScript"
homepage: "https://onui.onllm.dev"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free / open-source (GPL-3.0)"
install_method: "Chrome Web Store / Edge Add-ons / installer from GitHub releases (curl or PowerShell)"
docs_url: "https://onui.onllm.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/onllm-dev/onUI/releases"
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Annotation-first UI pair programming: a browser extension (Chrome + Edge + Firefox) that lets humans visually mark up UI elements/regions for AI agents via in-page annotation and draw mode; local-only MCP bridge with no cloud backend, privacy-preserving; auto-registers onui-local MCP for Claude Code and Codex; shadow DOM isolation for stable styling; multi-format export (compact to forensic) for varying agent context needs; batch annotation via Shift+click. Powered by onLLM.dev."
---

onUI addresses the gap between what a developer sees in a browser and what a coding agent can understand from a screenshot or text description. The extension adds annotate and draw modes to any web page, letting users tag elements or regions with intent and severity before exporting structured context at several detail levels. A local MCP server hands that context to agents such as Claude Code or Codex, with no cloud service in the path. Because annotations target the rendered page, no instrumentation of the target application is required, and the extension stays off by default per tab. The project ships as a Chrome, Edge, and Firefox extension with a native bridge for the MCP server.
