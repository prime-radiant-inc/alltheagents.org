---
name: "Better Agent"
slug: "better-agent"
layout: "agent.njk"
category: "multiplexer"
maker: "ofekron"
license: "Source-available (non-commercial)"
url: "https://github.com/ofekron/better-agent"
source_code_url: "https://github.com/ofekron/better-agent"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-06-24"
current_release: "2026-08-19"
stars: "56"
language: "Python, JavaScript"
homepage: "https://ofek-dev.com/better-agent/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude, Codex, Antigravity, Gemini"
pricing: "Free to install; commercial licensing requires written permission"
install_method: "One-liner scripts (macOS/Linux), PowerShell (Windows), Homebrew (brew tap ofekron/better-agent && brew install better-agent), or from source (git clone + ./run.sh)"
docs_url: "https://ofek-dev.com/better-agent/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ofekron/better-agent"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Unifies multiple coding agents (Claude, Codex, Gemini, Antigravity) into one durable local workspace with persistent sessions, detached agents surviving restarts, offline-first capture, local inspection of all traces/tool calls, and multi-agent orchestration accessible from browser, desktop, or mobile."
---

Better Agent addresses a practical pain point: developers running several AI coding agents in parallel lose sessions on restart, lose context across terminals, and have no unified surface to inspect what each agent did. It provides one durable local workspace where Claude Code, Codex, Gemini, and Antigravity agents run as detached processes with persistent sessions that survive restarts, and it captures work offline-first so results survive connectivity loss. Local inspection and reattachment let developers review and resume agent work across restarts. It is a workspace/session multiplexer rather than a coding agent - it manages agents rather than writing code itself. The project is a small free open-source utility, actively iterated, suited to developers running multiple agent CLIs locally.
