---
name: "nehemiah"
slug: "nehemiah"
layout: "agent.njk"
category: "other"
maker: "boringcomputers"
license: "Apache-2.0"
url: "https://github.com/boringcomputers/nehemiah"
source_code_url: "https://github.com/boringcomputers/nehemiah"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-06-30"
current_release: "2026-08-11"
stars: "305"
language: "Go, TypeScript"
homepage: "https://boringcomputers.com"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: null
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Preinstalled agents: Claude, Codex, Cursor, Pi; MCP integration with any MCP-compatible client"
pricing: "open-source"
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

Nehemiah addresses the problem that AI coding agents need isolated, disposable computers with real isolation guarantees rather than shared containers. Machines boot from signed release artifacts provisioned onto enrolled bare-metal hosts, boot in milliseconds from snapshots, and can be forked mid-run or backed by persistent S3 volumes. An agent drives each machine either through computer use over VNC or by writing and running code, with results exposed as live URLs and forwarded ports. Integration happens through an MCP server for desktop clients and an Effect-native TypeScript SDK. Deployment is deliberately not one-command: hosts are enrolled through a signed-artifact runbook on providers such as Latitude.sh, reflecting a self-host with your own keys philosophy.
