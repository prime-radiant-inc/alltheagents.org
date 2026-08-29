---
name: "ouijit"
slug: "ouijit"
layout: "agent.njk"
category: "multiplexer"
maker: "ouijit"
license: "AGPL-3.0"
url: "https://github.com/ouijit/ouijit"
source_code_url: "https://github.com/ouijit/ouijit"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-03"
current_release: "2026-08-20"
stars: "154"
language: "TypeScript"
homepage: "https://ouijit.com/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "none (launches whatever agent CLI is configured via hooks, e.g. claude, codex, opencode)"
pricing: "Free and open source; no account, no sign-in, no telemetry"
install_method: "Download prebuilt releases (macOS Apple Silicon/Intel, Linux x64) or build from source (git clone + npm install + npm start; requires Node.js 20+, git, C/C++ build tools)"
docs_url: "https://ouijit.com/docs/"
plugin_docs_url: null
config_docs_url: "https://ouijit.com/docs/"
download_url: "https://github.com/ouijit/ouijit/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Git worktree-based task and terminal session manager for agentic coding; Kanban board, live agent status with notifications, automatic worktree management for parallel workstreams, VM sandboxing for untrusted code, session-aware CLI with JSON output."
---

Parallel agent work on one repository collides over worktrees, ports, and context, and most managers solve it with configuration overhead. Ouijit takes the kanban route: starting a task creates an isolated git worktree via copy-on-write clone that preserves node_modules, attaches a terminal to the card, and provides dev-server runners, web previews, and markdown plan panels alongside. Integration with Claude Code, Codex, Pi, and OpenCode requires no setup because Ouijit shadows the agent binaries on PATH to inject lifecycle hooks, and agents themselves can move cards, create tasks, comment on diffs, and open panels through a session-aware ouijit CLI and local REST API. Per-terminal sandboxing runs commands inside a Lima VM or Seatbelt/Landlock via nono, and all state stays in local SQLite with no account or telemetry. Prebuilt releases cover macOS 13+ and Linux x64 under AGPL-3.0. Developers running parallel agent workstreams who want visual task tracking with sandboxing are the audience.
