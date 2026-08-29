---
name: "supaterm"
slug: "supaterm"
layout: "agent.njk"
category: "multiplexer"
maker: "supabitapp"
license: "Elastic License 2.0"
url: "https://github.com/supabitapp/supaterm"
source_code_url: "https://github.com/supabitapp/supaterm"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-10"
current_release: "2026-08-20"
stars: "174"
language: "Swift"
homepage: "https://supaterm.com"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "False"
model_providers: null
pricing: null
install_method: null
docs_url: "https://github.com/supabitapp/supaterm#readme"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "A terminal designed for the coding agents age. Integrates with Claude Code, Codex, and Pi coding agents via a hook-based settings bridge (Claude/Codex) and extension package (Pi). Injects pane context into terminal processes, routes structured agent events through the 'sp' CLI over a socket, and manages UI state (tab activity, notifications, session binding). Features terminal phase detection and session-identity model shared across all supported agents."
---

supaterm rethinks the terminal for developers whose primary 'applications' are coding agents. Rather than embedding agents, it bridges into them: hook-based settings injection for Claude Code and Codex, an extension package for Pi, and a shared session-identity model so the terminal can bind panes to agent sessions, track phase (working, waiting, done), and surface notifications and tab activity accordingly. Agents receive pane context injected through settings bridges, and structured events flow back to the app over a socket controlled by the sp CLI. Theming, session management, and integration docs live in the repository, and the same team ships the supacode worktree manager. Development is fast-moving (2,500+ commits) under the Elastic License 2.0.
