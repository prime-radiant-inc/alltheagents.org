---
name: "conduit-release"
slug: "conduit-release"
layout: "agent.njk"
category: "multiplexer"
maker: "lostintangent"
license: null
url: "https://github.com/lostintangent/conduit-release"
source_code_url: "https://github.com/lostintangent/conduit-release"
source_available: "False"
platforms:
  - "CLI"
first_released: "2025-11-15"
current_release: "2026-03-12"
stars: "230"
language: null
homepage: "https://trl.mx/conduit"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "User-defined agents (Claude Code, Codex, etc.) invoked via slash commands; none bundled"
pricing: "free"
install_method: "Download .dmg (macOS only)"
docs_url: "https://gistpad.dev/#/share/654a7ab37a00328334de5826588b124c"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/lostintangent/conduit-release/releases/latest/download/Conduit.dmg"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Terminal-centric workspace manager (DIY-DE) for parallelizing coding tasks with agents across local and cloud compute; organizes dev workflows as flexible tabs of terminals, editors, and browsers. Release-only repo, no source code."
---

Developers now run several different coding agents in a day, and each product wants to own the entire interface; Conduit argues the shared surface should be the terminal instead. The macOS app composes workspaces from flexible tabs of terminals, editors, and browser panes, and coding agents - whatever CLIs the user defines - are invoked through slash commands from any pane. Each agent session gets a sandbox with automatic git worktree management so parallel tasks stay branch-isolated, and cloud terminals extend the same layout to remote compute. Synchronized terminal panes, focus mode, design mode, and a conduit CLI round out the workspace model. The application is closed source, distributed as a macOS-only binary through this release-tracking repository, and is explicitly framed as an exploration rather than a product by its Microsoft-affiliated author.
