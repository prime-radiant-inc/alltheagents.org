---
name: "bb"
slug: "bb"
layout: "agent.njk"
category: "agent"
maker: "get-bb"
license: "MIT"
url: "https://github.com/get-bb/bb"
source_code_url: "https://github.com/get-bb/bb"
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2026-02-24"
current_release: "2026-08-20"
stars: "2394"
language: "TypeScript"
homepage: "https://getbb.app"
mcp_support: null
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: null
plan_mode: null
model_providers: "BYOK"
pricing: "open-source"
install_method: "npm"
docs_url: "https://getbb.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/get-bb/bb/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Agentic IDE that builds itself — every surface (desktop app, web app, CLI, HTTP API) is first-class, with live steerable threads, agent hand-offs, and a community plugin marketplace."
---

bb is an open-source agentic IDE that is itself built and maintained by agents: its repo carries .bb/skills, AGENTS.md, CLAUDE.md, and its own plans directory, and the codebase is developed largely by agents working inside it. Every interface - Electron desktop app, web app, CLI, and HTTP API - is a first-class way to drive the IDE, so automation and human use share the same entry points. Work runs in live steerable threads that can be watched and redirected mid-flight, and threads can hand off to other agents mid-task. A plugin marketplace (community plus bundled and local-path sources) extends the editor, and multi-device access works over Tailscale. The project is MIT-licensed, rapidly evolving, and installed via npx bb-app or desktop releases, appealing to developers experimenting with agent-built tooling.
