---
name: "49IDE"
slug: "49agents"
layout: "agent.njk"
category: "multiplexer"
maker: "alpbahadur"
license: "BSL-1.1 (free for individuals and small teams; converts to MIT 2030-02-26)"
url: "https://github.com/alpbahadur/49Agents"
source_code_url: "https://github.com/alpbahadur/49Agents"
source_available: "True"
platforms:
  - "Web"
  - "Desktop"
first_released: "2026-02-27"
current_release: "2026-08-18"
stars: 408
language: "JavaScript"
homepage: "https://49agents.com"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "delegates to the connected agent CLIs"
pricing: "free"
install_method: "Self-host via ./49ctl setup and ./49ctl start (localhost:1071), or download the macOS desktop app (.dmg)"
docs_url: "https://github.com/alpbahadur/49Agents/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/alpbahadur/49Agents/releases"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "The first 2D agentic IDE: an infinite zoomable canvas where terminals, agents, files, git graphs, and issue tables are panes you place anywhere, running real tmux sessions via ttyd, with broadcast input typing into many terminals at once and multi-machine agents connecting over WebSocket through a relay with no SSH."
---

49Agents bills itself as the first 2D agentic IDE — all agents, all terminals, all projects, all machines, one unified space. Instead of tabs and splits, panes live on an infinite zoomable canvas you arrange freely with the layout persisting: real tmux sessions served through ttyd run Claude Code, Codex, and other agent CLIs in their native form, alongside a Monaco editor, git graphs, Beads interactive issue tables, and markdown notes. Broadcast input types once into many terminals simultaneously, which is the key move for steering a fleet of agents, and agents on different machines — MacBook, PC, cloud VMs — all connect through a WebSocket relay with a HUD showing CPU, RAM, and API usage across machines, reachable from phone, tablet, or laptop via Tailscale, LAN, or the hosted relay with no terminal data stored server-side. It ships as a self-hosted Node/TypeScript web stack, a macOS desktop app, or an upcoming hosted version at 49agents.com.
