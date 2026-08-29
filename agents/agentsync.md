---
name: "agentsync"
slug: "agentsync"
layout: "agent.njk"
category: "other"
maker: "dallay"
license: "MIT"
url: "https://github.com/dallay/agentsync"
source_code_url: "https://github.com/dallay/agentsync"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-01-15"
current_release: "2026-08-19"
stars: "54"
language: "Rust, TypeScript"
homepage: "https://dallay.github.io/agentsync/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: null
pricing: "Free / open-source (MIT)"
install_method: "npm install -g @dallay/agentsync; or cargo install agentsync; or GitHub Releases binaries"
docs_url: "https://dallay.github.io/agentsync/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/dallay/agentsync/releases"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Fast portable CLI that synchronizes AI agent configurations and MCP servers across multiple AI coding assistants (Claude Code, Gemini CLI, Cursor, Copilot, Codex, OpenCode) using symlinks from a single source of truth in .agents/."
---

Teams running several AI assistants must keep CLAUDE.md, .cursor/rules, copilot-instructions.md, and per-tool MCP configs in sync by hand. AgentSync makes .agents/ the single source of truth — agentsync.toml, AGENTS.md, commands, skills, and prompts — and generates each tool's native files from it, with MCP servers defined once and emitted as .mcp.json, .codex/config.toml, .gemini/settings.json, and equivalents. Symlink-based targets (symlink, symlink-contents, nested-glob for monorepos, module-map) mean edits take effect without re-running a copy step, and existing files are backed up before replacement. A Rust core ships as a single static binary behind an npm wrapper, with commands for init, apply, status, clean, doctor, and skill management. Cross-platform support includes a documented Windows symlink setup path.
