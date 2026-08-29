---
name: "pocketshell"
slug: "pocketshell"
layout: "agent.njk"
category: "multiplexer"
maker: "Big-Pony"
license: "Apache-2.0"
url: "https://github.com/Big-Pony/pocketshell"
source_code_url: "https://github.com/Big-Pony/pocketshell"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-18"
current_release: "2026-08-16"
stars: "161"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "whatever agents the user runs on the host (Claude Code, Codex, opencode, Kimi CLI)"
pricing: "Free/open-source"
install_method: "curl -fsSL https://raw.githubusercontent.com/Big-Pony/pocketshell/main/install.sh | sh; or download binary from Releases; or build from source with Bun"
docs_url: "https://github.com/Big-Pony/pocketshell"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Big-Pony/pocketshell/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Self-hosted mobile-first remote terminal for running CLI/TUI AI coding agents (Claude Code, Codex, opencode, Kimi CLI) or plain shell/vim/htop from a phone browser; resilient sessions with precise replay on reconnect, push notifications when an agent finishes or needs input, single zero-dependency binary, end-to-end encryption (Noise IK)."
---

pocketshell exists for the moment a long-running coding agent needs attention while the developer is away from the desk: it turns a phone browser into a resilient terminal onto the dev machine's tmux sessions, where agents like Claude Code, Codex, opencode, or Kimi CLI run alongside plain shell, vim, and htop. Sessions persist server-side, so a dropped connection loses nothing — on reconnect the terminal replays exactly the missing gap of output — and push notifications arrive even with the phone locked when an agent finishes or blocks on input. Setup is a single Bun-built binary plus a pairing string with a 300-second TTL; optional integration writes hook/notify entries into each agent's config (Claude Code settings, etc.) for finish-and-notify events, and delivery spans Web Push and webhooks to WeCom, Feishu, Slack, and Discord. Security got attention the hard way: a web admin page was removed in v1.8.0 over an anonymous-access vulnerability, with audit guidance for older deployments. Self-hosting developers who want phone-based agent supervision without a cloud relay are the audience.
