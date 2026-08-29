---
name: "Nimbalyst"
slug: "nimbalyst"
layout: "agent.njk"
category: "multiplexer"
maker: "nimbalyst"
license: "MIT"
url: "https://github.com/nimbalyst/nimbalyst"
source_code_url: "https://github.com/nimbalyst/nimbalyst"
source_available: "True"
platforms:
  - "Desktop"
first_released: "2025-10-30"
current_release: "2026-08-19"
stars: "1525"
language: "TypeScript (Electron) + Swift (iOS)"
homepage: "https://nimbalyst.com/"
mcp_support: "yes"
plugin_support: "yes - Extension System with pluggable editors (Astro, visual git log, mindmap, slides, 3D object editor) via EditorHost contract"
claude_code_plugin: "n/a - Claude Code is a first-class supported agent; .claude/ and CLAUDE.md present"
subagents: "no"
hooks: "no - .githooks present but not a documented feature"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "binary - GitHub Releases (.dmg/.exe/.AppImage)"
docs_url: "https://docs.nimbalyst.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/nimbalyst/nimbalyst/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Open-source local visual workspace and session/task manager for coding agents (Codex, Claude Code, OpenCode, Copilot). Visual WYSIWYG collaboration: see agent changes as red/green diffs, approve/edit/annotate directly in markdown, mockups, Mermaid, Excalidraw, CSV, data models, Monaco. Parallel session management (Kanban board, search/resume, link files to sessions) plus task tracking both humans and agents can edit. Mobile companion iOS app. Extension system for custom visual editors. Free desktop app for macOS/Windows/Linux."
---

Nimbalyst gives developers a visual surface for working with coding agents instead of reading terminal transcripts. Parallel sessions run in isolated git worktrees managed from a kanban board, and agent changes land as inspectable diffs that a human steps through before anything is committed. Task tracking, git staging, AI-drafted commits, and an embedded Ghostty terminal live alongside the editors, and an MCP client renders tool results as visual widgets. Everything is plain files in the user's git repository with no proprietary store, and iOS/Android companions surface which agents need attention. The project is MIT-licensed Electron/TypeScript with an open collaboration wire protocol.
