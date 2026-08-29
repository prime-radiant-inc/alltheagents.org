---
name: "CodeKanban"
slug: "codekanban"
layout: "agent.njk"
category: "multiplexer"
maker: "fy0"
license: "Apache-2.0"
url: "https://github.com/fy0/CodeKanban"
source_code_url: "https://github.com/fy0/CodeKanban"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-11-11"
current_release: "2026-08-13"
stars: "223"
language: "Go (backend), Vue 3 + TypeScript (frontend)"
homepage: null
mcp_support: null
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free"
install_method: "npx codekanban or npm install -g codekanban@latest"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/fy0/CodeKanban"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Manages all your terminals and AI coding tools (Claude Code / Codex) from one unified page — multi-project/terminal management, AI tool status detection (idle/working/needs approval), conversation history, Git worktree management, multi-tab notes. Ships installable Codex skill bundle (codekanban-cli)."
---

CodeKanban addresses the scattered-window problem of running several AI coding sessions at once: terminals for Claude Code and Codex live in one web page, organized as projects on a kanban board. The system detects each agent's state — idle, working, or waiting for approval — and notifies on completion, while conversation and prompt history stays searchable per session. Git worktree management is built in, using a hybrid of go-git and the system git binary, so parallel agents can work in isolated checkouts, and a multi-tab notes panel captures working context alongside the sessions. The backend is a single Go binary with an embedded local database and a Vue 3 frontend, launched with npx, and it ships a codekanban-cli Codex skill bundle for board interaction from inside an agent session.
