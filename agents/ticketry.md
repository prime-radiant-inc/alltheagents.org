---
name: "Ticketry"
slug: "ticketry"
layout: "agent.njk"
category: "multiplexer"
maker: "ticketry-hq"
license: "MIT"
url: "https://github.com/ticketry-hq/ticketry"
source_code_url: "https://github.com/ticketry-hq/ticketry"
source_available: "True"
homepage: null
docs_url: "https://github.com/ticketry-hq/ticketry/blob/main/README.md"
download_url: "https://github.com/ticketry-hq/ticketry/releases"
install_method: "Download Ticketry_0.2.0_aarch64.dmg from the GitHub releases (macOS 11+ on Apple silicon; tmux required, installed via Homebrew; unsigned build — approve in macOS privacy settings), or run from source with npm install && npm run desktop:dev"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Rust"
first_released: "2026-07-27"
current_release: "2026-08-21"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "delegates to the installed agent CLIs (Claude Code, Codex, Gemini CLI, Agy) that the user approves as absolute paths; each provider brings its own models and auth"
pricing: "free"
stars: "5"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A macOS workbench that turns written ideas into grill-spec-split-implement-review work items and launches agent CLIs on them in durable tmux sessions, tracking each run as a first-class record with a dependency graph, retry policy, and an MCP listener that agents connect back through."
---

Ticketry is a Tauri desktop app (React frontend, Rust services, SeaORM database with a generated GraphQL schema) that applies a disciplined ticket workflow to agentic coding: an idea becomes a work item, and the app takes it through grilling, speccing, splitting into tickets, implementation, and review — the workflow the HN author described as based on Matt Pocock's coding process. The agent CLIs it drives — Claude Code, Codex, Gemini CLI, and Agy — are not bundled: the desktop discovers them, checks name, executable bit, architecture, and version, and requires the user to approve each absolute path before anything launches. Runs live in tmux sessions rendered by an embedded native libghostty terminal, so agent work survives the app and the window; every launch is a durable Agent Run record with launch policy, dependency-graph execution, retry attempts, and reconciliation after restarts. Agents connect back to the work database through an MCP listener on a unix socket in the app's data directory via a packaged stdio hook bridge, so an agent can read and file findings on work items from inside its own session. The current 0.2.0 build targets macOS 11+ on Apple silicon only, is an unsigned developer build (the author says "open anyway" in privacy settings), and requires tmux. It suits a solo developer or small team who want the paper trail of tickets with agents doing the writing.
