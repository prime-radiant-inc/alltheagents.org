---
name: "qm"
slug: "qm"
layout: "agent.njk"
category: "agent"
maker: "yc-software"
license: "MIT"
url: "https://github.com/yc-software/qm"
source_code_url: "https://github.com/yc-software/qm"
source_available: "Yes"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-07-29"
current_release: "2026-08-20"
stars: "13967"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Harness-agnostic: the agent loop drives Pi, OpenCode, Codex, or Claude Code as swappable 'substrates'; models are admin-configured per org"
pricing: "open-source"
install_method: "npm exec --yes --package=@yc-software/qm@latest -- qm init . --org <slug> --target <fly-or-aws>"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/yc-software/qm"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A 'multiplayer agent harness for work': each employee gets an isolated workspace (own memory, files, keychain view, crons, durable sandbox) while collaborating through shared Slack channels and projects, with the agent loop itself pluggable across Pi, OpenCode, Codex, or Claude Code. Contributions are accepted as written ADRs, not code — maintainers implement proposals themselves."
---

qm is built for companies that want one agent platform shared across employees rather than a personal CLI: each person gets an isolated workspace with their own memory, files, keychain view, permissions, and durable sandbox, while shared scopes cover Slack channels, group messages, and team projects. The headless TypeScript core runs an agent loop over a fixed tool surface — notably an execute tool confined to each scope's sandbox — with Postgres storing sessions, memory, and queue state, and the web UI, admin panel, and Slack integration all plugins over its HTTP API. Which underlying harness (Pi, OpenCode, Codex, or Claude Code) drives the loop is an org-level configuration, behind interfaces swapped through one wiring file. Security postures range from per-tool human approval to a classifier-screened auto mode, with hard denials for destructive commands in all postures and auditing throughout. Organizations self-host it in their own Fly or AWS accounts, and contribute architectural proposals as written ADRs that maintainers implement.
