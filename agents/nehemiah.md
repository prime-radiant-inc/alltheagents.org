---
name: "nehemiah"
slug: "nehemiah"
layout: "agent.njk"
category: "agent"
maker: "boringcomputers"
license: "Apache-2.0"
url: "https://github.com/boringcomputers/nehemiah"
source_code_url: "https://github.com/boringcomputers/nehemiah"
source_available: True
platforms:
  - "CLI"
  - "Web"
first_released: "2026-06-30"
current_release: "2026-08-11"
stars: "305"
language: "Go, TypeScript"
homepage: "https://boringcomputers.com"
mcp_support: True
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Preinstalled agents: Claude, Codex, Cursor, Pi; MCP integration with any MCP-compatible client"
pricing: null
install_method: "git clone; npm install; run infra/latitude/provision.sh; set apps/web/.env; npm run dev -w web (full runbook at infra/latitude/README.md)"
docs_url: "https://boringcomputers.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/boringcomputers/nehemiah"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "On-demand Linux computers you can hand to an AI via real Firecracker microVMs that boot in milliseconds. Each machine is a full Linux desktop (VNC) or headless shell with coding agents preinstalled, driven by an AI that can browse the screen or write/run code. Real hardware-virtualized isolation (a kernel per machine, not a shared container), memory snapshot restoration in ~3ms, machine forking in ~35ms with exact live state, and network-isolated guests behind an egress firewall."
---

On-demand Linux computers you can hand to an AI via real Firecracker microVMs that boot in milliseconds. Each machine is a full Linux desktop (VNC) or headless shell with coding agents preinstalled, driven by an AI that can browse the screen or write/run code. Real hardware-virtualized isolation (a kernel per machine, not a shared container), memory snapshot restoration in ~3ms, machine forking in ~35ms with exact live state, and network-isolated guests behind an egress firewall.
