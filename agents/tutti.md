---
name: "tutti"
slug: "tutti"
layout: "agent.njk"
category: "multiplexer"
maker: "tutti-os"
license: "Apache-2.0"
url: "https://github.com/tutti-os/tutti"
source_code_url: "https://github.com/tutti-os/tutti"
source_available: "Yes"
platforms: []
first_released: "2026-06-12"
current_release: "2026-08-20"
stars: "3311"
language: "Go"
homepage: "https://tutti.sh/"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI"
pricing: "freemium"
install_method: "binary"
docs_url: "https://tutti.sh/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://tutti.sh/desktop/download"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Real-time shared workspace where multiple AI coding agents (Claude Code, Codex, Hermes) collaborate and share context, files, and tasks seamlessly via 'Big @' cross-agent references and a control center."
---

Tutti targets the messenger role humans play between coding agents: without a shared surface, Codex cannot pick up Claude's output without losing context, and coordinating several agents means manual copy-paste. It provides a GUI-first, real-time workspace — no terminal required — where context, files, running tasks, and app outputs are shared across agents; 'Big @' references pull in past conversations or other agents' work, tasks coordinate agents across providers in parallel or sequence, and a control center centralizes conversations, approvals, and status. Both humans and agents can invoke workspace apps (image generation, UI/UX design, documentation, presentations), keeping outputs in the shared space. Teams and power users running Claude Code, Codex, or Hermes subscriptions use it; the open-source app runs locally for a single user, while Tutti · VM adds multi-user Rooms with cross-device access and localhost-preview sharing.
