---
name: "Loopsy"
slug: "loopsy"
layout: "agent.njk"
category: "multiplexer"
maker: "leox255"
license: "Apache-2.0"
url: "https://github.com/leox255/loopsy"
source_code_url: "https://github.com/leox255/loopsy"
source_available: "Yes"
platforms:
  - "CLI"
  - "Mobile"
first_released: "2026-02-21"
current_release: "2026-07-28"
stars: "139"
language: "TypeScript"
homepage: null
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: "npm (loopsy); relay self-hosted via npx @loopsy/deploy-relay"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "It pairs a Flutter mobile app with a machine-resident daemon over a self-hostable Cloudflare Worker relay (npx @loopsy/deploy-relay, no port forwarding), giving full PTY terminal control of Claude Code, Codex, or any shell from a phone, plus an mDNS-paired LAN mode where agents exchange commands, files, and context across machines over MCP."
---

Long-running agent sessions strand developers at their desks, and loopsy solves the away-from-keyboard problem: a daemon on the workstation bridges to the user's phone through a Cloudflare relay that can be the maintainer's or self-hosted on the free tier in about thirty seconds. The mobile client renders a real PTY terminal with ANSI, scrollback, and resize, so TUI-based agents work normally, and sessions survive phone locks and signal loss. Its second mode is agent-to-agent: daemons discover each other via mDNS on a LAN, pair with a 6-digit code, and expose MCP tools so an agent on one machine can run commands, transfer files, or share key/value context on another - for example, dispatching an iOS build to a Mac Studio from a laptop session. Developers running Claude Code, Codex, or Gemini CLI across multiple machines use it as the connective layer.
