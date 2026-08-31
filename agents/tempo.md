---
name: "Tempo"
slug: "tempo"
layout: "agent.njk"
category: "multiplexer"
maker: "Tempo Labs"
license: "Proprietary"
url: "https://www.tempolabs.ai"
source_code_url: null
source_available: "False"
platforms:
  - "Web"
first_released: "2025"
current_release: "2026"
stars: null
language: null
homepage: "https://www.tempolabs.ai"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "True"
subagents: "True"
hooks: "no"
plan_mode: "yes"
model_providers: "Claude Code, OpenAI Codex (bring your own agent)"
pricing: "subscription"
install_method: "Desktop app download for macOS (ARM/Intel), Windows, and Linux"
docs_url: "https://tempolabs.mintlify.app/"
plugin_docs_url: null
config_docs_url: "https://tempolabs.mintlify.app/"
download_url: "https://www.tempo.new/download/dmg_arm64"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "AI collaborative workspace and IDE where designers, PMs, and engineers ship together. Canvases are code in your repo built from real components and tokens. Agents (Triage, Spec and Design, Bug Fixer, Feature Builder) work in parallel on separate branches. Bring Your Own Agent powered by Claude Code and Codex. Y Combinator backed. Made in Toronto."
---

Tempo targets the coordination gap between product managers, designers, and engineers by putting all three on one working surface layered over a real repository. PRDs and specs live as linked documents, an issue board ties cards to branches and pull requests, and a Figma-style canvas renders live frames backed by the actual components and routes in the codebase, with edits writing back to source. Agents — the product names roles like Triage, Spec and Design, Bug Fixer, and Feature Builder — trigger from Slack messages, issue changes, GitHub events, schedules, or approvals rather than one-off prompts, and each run stops at decisions that require a person, producing a reviewable artifact such as a pull request. Underneath, Tempo runs Claude Code or Codex in an isolated git worktree per chat session so the main tree stays clean, and a Tempo MCP server exposes the platform to external tooling. The product ships as a web workspace and a desktop app, and Y Combinator-backed Tempo Labs sells it to product teams that want specs, designs, and code changes to share a single source of truth.
