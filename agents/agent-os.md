---
name: "agent-os"
slug: "agent-os"
layout: "agent.njk"
category: "multiplexer"
maker: "saadnvd1"
license: "MIT"
url: "https://github.com/saadnvd1/agent-os"
source_code_url: "https://github.com/saadnvd1/agent-os"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-01-07"
current_release: "2026-08-12"
stars: "166"
language: "TypeScript"
homepage: "https://saadnaveed.com"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "agent CLIs bring their own providers (Claude Code, Codex, Aider, Gemini CLI, Amp, Pi, OpenCode, Cursor CLI)"
pricing: "Free/open-source (self-hosted); paid AgentOS Cloud VMs available"
install_method: "npm install -g @saadnvd1/agent-os; or curl -fsSL https://raw.githubusercontent.com/saadnvd1/agent-os/main/scripts/install.sh | bash; desktop app downloads; or manual git clone"
docs_url: "https://www.runagentos.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/saadnvd1/agent-os/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Mobile-first web UI for managing AI coding sessions (Claude Code, Codex, Aider, Gemini CLI, Amp, Pi); multi-pane parallel terminals (up to 4 side-by-side), voice-to-text dictation, git integration, session orchestration via MCP Conductor/worker model."
---

Agent sessions keep running after you step away from the desk, but checking on them usually means SSH from a phone with a tiny keyboard. AgentOS serves a mobile-first web UI over self-hosted sessions of Claude Code, Codex, Aider, Gemini CLI, Amp, Pi, and other CLIs, with up to four terminal panes side by side, voice-to-text for dictating prompts, and git integration covering status, diffs, commits, PRs, and worktrees. Session orchestration follows a Conductor/worker model over MCP, a Tauri desktop app wraps the same UI for desktop use, and a hosted cloud option exists at runagentos.com. Developers who kick off long agent runs and check in from phones or other machines are the users.
