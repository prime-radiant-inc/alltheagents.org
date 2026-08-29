---
name: "vibe-annotations"
slug: "vibe-annotations"
layout: "agent.njk"
category: "other"
maker: "RaphaelRegnier"
license: "PolyForm Shield 1.0.0"
url: "https://github.com/RaphaelRegnier/vibe-annotations"
source_code_url: "https://github.com/RaphaelRegnier/vibe-annotations"
source_available: "True"
platforms: []
first_released: "2025-07-16"
current_release: "2026-08-17"
stars: "141"
language: "JavaScript"
homepage: "https://www.vibe-annotations.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "Browser extension (Chrome Web Store) + npx vibe-annotations-server init (global server setup wizard)"
docs_url: "https://vibe-annotations.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://chromewebstore.google.com (Chrome extension) + npm vibe-annotations-server"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Visual feedback/annotation tool for localhost web development; annotate page elements, make design tweaks, and share with AI coding agents or teammates to auto-implement fixes via MCP. Configures Claude Code, Cursor, Windsurf, Codex, OpenClaw, VS Code."
---

Visual feedback in web development usually dies in screenshots: someone marks up a page, and the annotations become tickets or re-typed prompts. Vibe-annotations closes that loop for AI-driven development — the Chrome extension annotates elements directly on localhost pages across multiple pages per session, and a companion server (installed with a single npx command that also configures the coding agent) exposes those annotations over MCP so Claude Code, Cursor, Windsurf, Codex, or VS Code receive structured fix requests instead of screenshots. Annotations can also be copied to the clipboard or shared with teammates through file sharing and watch mode, making the same channel useful for human review. Front-end developers iterating on design with AI agents are the users; the project is under the PolyForm Shield license, actively maintained with CI and community health files.
