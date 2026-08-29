---
name: "OpenSpec"
slug: "openspec"
layout: "agent.njk"
category: "other"
maker: "Fission-AI"
license: "MIT"
url: "https://github.com/Fission-AI/OpenSpec"
source_code_url: "https://github.com/Fission-AI/OpenSpec"
source_available: "Yes"
platforms: []
first_released: "2025-08-05"
current_release: "2026-08-19"
stars: "65558"
language: "TypeScript"
homepage: "https://openspec.dev/"
mcp_support: "no"
plugin_support: "yes (community schemas)"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "yes"
model_providers: "BYOK (works with 30+ AI assistants)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://openspec.dev/"
plugin_docs_url: null
config_docs_url: "https://github.com/Fission-AI/OpenSpec/blob/main/docs"
download_url: "https://www.npmjs.com/package/@fission-ai/openspec"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Adds a lightweight spec layer for AI coding assistants to agree on what to build before code is written, using an artifact-guided workflow with plain Markdown; supports 30+ tools and enables cross-repo planning via 'Stores.'"
---

AI coding assistants routinely build the wrong thing because intent lives in a chat transcript rather than a reviewable artifact. OpenSpec inserts a lightweight spec process: openspec init scaffolds a convention directory, and each change becomes a proposal, spec deltas, design notes, and a task list in plain Markdown that the assistant must follow before writing code. Slash commands (/opsx:explore, /opsx:propose, /opsx:apply, /opsx:archive) adapt to whichever tool is in use — Claude Code, Cursor, GitHub Copilot, Amazon Q, Codex, and 30-plus others — and archived changes remain in the repo as a decision record. Beta 'Stores' let teams share specs across repositories, and anonymous telemetry (command names only) is opt-out. The npm CLI installs globally under MIT and requires Node 20.19+, and the project dogfoods itself with 66k stars. Teams that want lightweight, tool-agnostic specification discipline ahead of agent-driven implementation are the audience.
