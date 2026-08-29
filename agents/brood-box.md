---
name: "brood-box"
slug: "brood-box"
layout: "agent.njk"
category: "multiplexer"
maker: "stacklok"
license: "Apache-2.0"
url: "https://github.com/stacklok/brood-box"
source_code_url: "https://github.com/stacklok/brood-box"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-02-13"
current_release: "2026-08-19"
stars: "58"
language: "Go"
homepage: "https://github.com/stacklok/brood-box"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
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

brood-box exists because letting a coding agent run arbitrary commands on a developer machine is a trust problem that containers only partially solve. Stacklok's Go CLI boots a lightweight virtual machine via libkrun (KVM on Linux, Hypervisor.framework on macOS), snapshots the workspace copy-on-write, and launches the chosen agent — Claude Code, Codex, OpenCode, Hermes, or Gemini CLI — inside it over an ephemeral SSH session. An egress firewall restricts network access to LLM providers and package registries by profile, with a locked mode allowing only the LLM endpoint; ToolHive MCP servers are auto-discovered and proxied into the VM. When the agent exits, the tool computes a diff and the user reviews each file before changes are flushed back, with hash re-verification guarding against tampering. Stacklok positions it as experimental infrastructure for teams that want hardware isolation, DNS-aware egress control, and zero persistent state around agents they run daily.
