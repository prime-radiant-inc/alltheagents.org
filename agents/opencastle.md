---
name: "OpenCastle"
slug: "opencastle"
layout: "agent.njk"
category: "other"
maker: "monkilabs"
license: "MIT"
url: "https://github.com/monkilabs/opencastle"
source_code_url: "https://github.com/monkilabs/opencastle"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-02-26"
current_release: "2026-08-10"
stars: "61"
language: "TypeScript"
homepage: "http://www.opencastle.dev/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "none of its own (capability tiers premium/standard/economy resolved by each target assistant)"
pricing: "open-source"
install_method: "npx opencastle init"
docs_url: "https://www.opencastle.dev/docs/"
plugin_docs_url: null
config_docs_url: "https://www.opencastle.dev/docs/"
download_url: "https://www.npmjs.com/package/opencastle"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Compiles one source AI assistant config into multiple assistant formats (Claude Code, GitHub Copilot, Cursor, Windsurf, OpenCode, Codex CLI, Antigravity); detects drift and keeps configs in sync across CI; includes 13 role definitions and experimental Convoy Engine that executes multi-step tasks across git worktrees with planning, execution, and quality gates"
---

Teams running several AI coding assistants maintain parallel config files — CLAUDE.md, .cursorrules, .windsurfrules, AGENTS.md, .github agents — that diverge the first time someone updates one and forgets the rest. OpenCastle treats the assistant config as a compiled artifact: a TypeScript CLI reads one source config, inspects the repository for frameworks and existing configs, and emits native-format outputs for Claude Code, GitHub Copilot, Cursor, Windsurf, OpenCode, Codex CLI, and Antigravity, including MCP server definitions in each assistant's expected shape. A status command reports drift across targets, sync --check gates CI against drift, and npx opencastle init scaffolds without overwriting existing files. Thirteen role agents, 31 domain skills, and nine workflow templates ship in the box, and an experimental Convoy engine adds multi-agent orchestration across isolated git worktrees with SQLite-backed resume. Platform teams standardizing assistant behavior across tool estates are the audience.
