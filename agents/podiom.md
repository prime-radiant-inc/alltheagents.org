---
name: "Podiom"
slug: "podiom"
layout: "agent.njk"
category: "multiplexer"
maker: "Podiom"
license: "MIT"
url: "https://github.com/Podiom/Podiom"
source_code_url: "https://github.com/Podiom/Podiom"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
  - "Autonomous"
first_released: "2026-06-29"
current_release: "2026-08-19"
stars: "4"
language: "Go"
homepage: "https://github.com/Podiom/Podiom/tree/master/docs"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "False"
model_providers: "Claude Code (Anthropic), OpenAI Codex"
pricing: "Free / open-source (MIT)"
install_method: "macOS/Linux: curl -fsSL https://github.com/Podiom/Podiom/releases/latest/download/install.sh | bash; Windows: irm https://github.com/Podiom/Podiom/releases/latest/download/install.ps1 | iex"
docs_url: "https://github.com/Podiom/Podiom/tree/master/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Podiom/Podiom/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Open-source, local-first workspace for Claude Code and OpenAI Codex that provides durable context, sessions, projects, tasks, and scheduling for local LLM agents while the native CLIs do the work. Thin orchestration layer with full audit trails and agent identities. Lead agents can delegate work to other agents and turn outcomes into roadmap tasks."
---

Podiom targets developers running Claude Code and OpenAI Codex side by side whose sessions, context, and task state live nowhere durable — each CLI restarts from scratch and nothing links the two. The Go daemon provides that missing layer: named agent identities with workspace, model, profile, and permission mode; projects with shared context and roadmap tasks; scheduled recurring runs; and Goals, where a lead agent pursues a long-running outcome, delegates to other agents, and converts outcomes into roadmap tasks with an auditable trail. Sessions keep canonical history and can replay it onto a fresh CLI session after a provider or profile switch, and the layer never replaces the CLIs' own models, tools, or authentication. State lives under ~/.podiom with an embedded web UI, native mobile apps, and a Home Assistant add-on option. Its early adopters are local-first developers running multi-agent workflows entirely on their own machines.
