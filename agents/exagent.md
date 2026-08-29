---
name: "ExAgent"
slug: "exagent"
layout: "agent.njk"
category: "agent"
maker: "exqqstar"
license: "Apache-2.0, MIT"
url: "https://github.com/exqqstar/ExAgent"
source_code_url: "https://github.com/exqqstar/ExAgent"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2026-06-16"
current_release: "2026-07-14"
stars: "54"
language: "Rust, TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open-source; BYOK"
install_method: "Download signed/notarized macOS DMG from GitHub Releases; or npm ci + npm run tauri:dev for dev build"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Local desktop-first agent workbench with a Rust runtime and Tauri/React GUI; durable sessions, approval-gated tools, subagents, goal tracking, project memory, MCP tools, workflows, and live runtime inspection."
---

ExAgent is built for running a personal coding agent entirely on one's own workstation with no hosted component. The Rust runtime normalizes provider APIs into unified conversation, tool-call, and streaming types, configured per-provider in the GUI with API-key or OAuth credentials stored locally; the Tauri/React shell adds projects, durable sessions, and a live inspector over the agent's event stream. Tool use is approval-gated by default, subagents and workflow runs (such as deep search) extend capability, SKILL.md files define reusable procedures, and event replay makes past runs auditable. The project explicitly targets personal use — no production sandbox isolation, hosted collaboration, or public SDK — and remains a single-author, early-stage effort.
