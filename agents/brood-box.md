---
name: "brood-box"
slug: "brood-box"
layout: "agent.njk"
category: "multiplexer"
maker: "stacklok"
license: "Apache-2.0"
url: "https://github.com/stacklok/brood-box"
source_code_url: "https://github.com/stacklok/brood-box"
source_available: True
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-02-13"
current_release: "2026-08-19"
stars: "58"
language: "Go"
homepage: null
mcp_support: True
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: False
plan_mode: False
model_providers: "Anthropic (Claude Code), OpenAI (Codex), OpenCode, Hermes, Gemini"
pricing: "Free/open source"
install_method: "Download pre-built binary from GitHub Releases, or build from source with task build"
docs_url: "https://github.com/stacklok/brood-box/blob/main/docs/USER_GUIDE.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/stacklok/brood-box/releases"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Runs coding agents inside hardware-isolated microVMs (KVM/Hypervisor.framework via libkrun), not just containers; copy-on-write workspace snapshots with interactive per-file diff review; DNS-aware egress firewall; ephemeral per-session SSH keys; zero persistent state."
---

Runs coding agents inside hardware-isolated microVMs (KVM/Hypervisor.framework via libkrun), not just containers; copy-on-write workspace snapshots with interactive per-file diff review; DNS-aware egress firewall; ephemeral per-session SSH keys; zero persistent state.
