---
name: "pi-web"
slug: "pi-web"
layout: "agent.njk"
category: "multiplexer"
maker: "jmfederico"
license: "MIT"
url: "https://github.com/jmfederico/pi-web"
source_code_url: "https://github.com/jmfederico/pi-web"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-05-07"
current_release: "2026-08-19"
stars: "572"
language: "TypeScript"
homepage: "https://pi-web.dev/"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "whatever the host pi runtime supports (multi-provider via pi)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://pi-web.dev/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jmfederico/pi-web"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Keeps Pi Coding Agent sessions persistently alive in real workspaces on your machine or server; sessions survive browser disconnects; supervise multiple parallel sessions from any browser/device; remote-first design with fleet/machine management"
---

pi-web addresses the fragility of terminal-based coding agents: close the laptop and the session dies, and supervising several parallel runs means juggling terminals. The server hosts pi sessions in real workspaces on the user's machine or server, so browser disconnects never interrupt the agent, and any browser or device can attach to a running session or start a new one. Fleet management treats other pi-web runtimes as remote machines, proxying projects, files, git state, terminals, and settings through one control surface; access runs over private networks, SSH tunnels, or trusted reverse proxies since the system is explicitly not a multi-tenant sandbox. Trusted browser plugins and sessiond-backed workspace providers extend the platform. Developers running pi on headless boxes or across several machines use it as the durable control surface for those sessions.
