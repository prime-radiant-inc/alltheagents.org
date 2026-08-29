---
name: "Pi"
slug: "pi"
layout: "agent.njk"
category: "agent"
maker: "earendil-works"
license: "MIT"
url: "https://github.com/earendil-works/pi"
source_code_url: "https://github.com/earendil-works/pi"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-08-09"
current_release: "2026-08-19"
stars: null
language: "TypeScript"
homepage: "https://pi.dev"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google"
pricing: "Free / open source (MIT)"
install_method: "npm install -g @earendil-works/pi-coding-agent"
docs_url: "https://pi.dev/docs/latest"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/earendil-works/pi"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
  - "tiennm"
what_makes_it_special: "Self-extensible interactive coding agent CLI providing a unified multi-provider LLM API, agent runtime with tool calling and state management, and a terminal UI library."
---

pi grew out of Mario Zechner's argument that coding agents had become opaque products, and its design publishes everything as inspectable, replaceable parts: a coding-agent CLI, a core runtime with tool calling and state management, a unified multi-provider LLM API, a terminal UI library, and telemetry contracts, each independently consumable. The agent is self-extensible by design — users add tools, skills, and extensions at runtime, and a large third-party ecosystem of memory systems, shells, GUIs, and Emacs/Neovim front ends has grown on those interfaces. Security posture is explicit rather than implicit: no built-in permission system, with documented paths for running inside a Gondolin micro-VM, Docker, or OpenShell sandbox, plus aggressive supply-chain hardening (pinned deps, min-release-age, --ignore-scripts). Maintained actively by earendil-works with public RFCs and a Discord community, pi serves developers who want a minimal, inspectable agent they can extend rather than a managed product.
