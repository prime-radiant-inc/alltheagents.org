---
name: "routa"
slug: "routa"
layout: "agent.njk"
category: "multiplexer"
maker: "phodal"
license: "MIT"
url: "https://github.com/phodal/routa"
source_code_url: "https://github.com/phodal/routa"
source_available: "Yes"
platforms:
  - "Web"
  - "Desktop"
first_released: "2026-02-16"
current_release: "2026-08-13"
stars: "1796"
language: "TypeScript"
homepage: "https://phodal.github.io/routa/"
mcp_support: "yes (MCP, ACP, A2A, AG-UI, A2UI, REST, SSE)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes (webhooks and schedules for automation)"
plan_mode: "yes"
model_providers: "BYOK (normalized through adapters)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://phodal.github.io/routa/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/phodal/routa/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Workspace-first multi-agent coordination platform that uses a Kanban board as both planning surface and coordination bus, with each lane backed by a different specialist prompt with increasingly strict evidence contracts. The review boundary is a real gate. Works in local-first desktop mode or self-hosted web mode."
---

Routa treats software delivery as a board rather than a chat: work enters as cards, moves through Backlog, Todo, Dev, Review, and Done lanes, and each lane's agent operates under the constraints and evidence requirements that lane defines. Sessions stream live, can be reconnected after interruption, and expose traces for inspection, while worktree management keeps parallel agents from colliding in one checkout. Schedules, webhooks, and background tasks drive unattended runs, and GitHub repositories can be imported as virtual workspaces without a local clone. Teams use it to enforce stage discipline on multi-agent delivery — the coordinator splits work, crafters implement, and verifiers gate the merge — with MIT-licensed desktop and web builds.
