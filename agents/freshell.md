---
name: "freshell"
slug: "freshell"
layout: "agent.njk"
category: "multiplexer"
maker: "danshapiro"
license: "MIT"
url: "https://github.com/danshapiro/freshell"
source_code_url: "https://github.com/danshapiro/freshell"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-01-29"
current_release: "2026-08-20"
stars: "93"
language: "TypeScript, Rust"
homepage: "https://freshell.net/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Codex, OpenCode, Gemini, Kimi, Amplifier"
pricing: "Free / open-source (MIT)"
install_method: "git clone --branch v0.7.5, npm install, npm run serve (Node.js 18+, 20+ recommended)"
docs_url: "https://freshell.net/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "The 'loving child of tmux and Claude Code': an agentic IDE that unifies coding agents, shells, editors, and browsers into a tabbed/paned workspace across desktop, laptop, and phone (VPN/Tailscale); cross-device session resumption ('speak with the dead' - resume any Claude/Codex/OpenCode session from any device); Freshclaude interactive alternative to Claude CLI with rich chat UI; Stream Deck hardware integration; extension system (client/server/CLI pane types); self-configuring workspace where agents can create tabs, panes, browsers, and subagents programmatically."
---

Agent CLI sessions are normally trapped in one terminal on one machine, which breaks when work spans a desk machine, a laptop, and a phone. Freshell is a self-hosted web workspace (React front end over node-pty) that hosts Claude Code, Codex, OpenCode, Gemini, and Kimi sessions alongside shells, editors, and browser panes, indexes their session histories, and lets any device resume a session where it left off. Agents can configure the workspace themselves through an extension API that creates tabs, panes, browsers, and subagents programmatically, and a Freshclaude chat UI wraps the Claude CLI with a richer interface. It is MIT-licensed, installed from source with Node 18+, and used by developers who juggle several agent CLIs across devices.
