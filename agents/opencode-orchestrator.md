---
name: "opencode-orchestrator"
slug: "opencode-orchestrator"
layout: "agent.njk"
category: "agent"
maker: "agnusdei1207"
license: "MIT"
url: "https://github.com/agnusdei1207/opencode-orchestrator"
source_code_url: "https://github.com/agnusdei1207/opencode-orchestrator"
source_available: "True"
platforms: []
first_released: "2026-01-13"
current_release: "2026-08-18"
stars: "225"
language: "TypeScript, Rust"
homepage: "https://github.com/agnusdei1207/opencode-orchestrator/issues"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "subagents inherit the primary agent's model unless per-agent overrides are set via agent.<name>.model"
pricing: "Free"
install_method: "npm install -g opencode-orchestrator"
docs_url: "https://agnusdei1207.github.io/opencode-orchestrator/"
plugin_docs_url: null
config_docs_url: "https://github.com/agnusdei1207/opencode-orchestrator#configuration"
download_url: "https://www.npmjs.com/package/opencode-orchestrator"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Multi-agent mission control plugin for OpenCode that coordinates AI-agent workflows (Commander, Planner, Worker, Reviewer roles) with autonomous verification and local-first memory. Install hook auto-registers in opencode.json."
---

OpenCode handles interactive sessions well, but long objectives — multi-file refactors, feature builds — lose structure and verification discipline as context grows. This plugin overlays a mission loop: /task starts a persisted mission under .opencode/, where a Commander orchestrates, a Planner decomposes the objective into ordered file-level tasks, Workers implement with isolated context and TDD, and a Reviewer gates completion on verified test evidence and builds. Memory is local-first and deliberately low-tech — BM25 retrieval, tags, and a graph with Ebbinghaus-style decay replace any external vector database — and a Rust companion CLI provides an optional TCP shell listener for control. Per-role concurrency and per-agent model overrides are configured in opencode.json. Install is one npm command with an auto-registering plugin hook; missions persist across restarts. Solo OpenCode users running autonomous multi-step work with review gates are the audience.
