---
name: "Wienerdog"
slug: "wienerdog"
layout: "agent.njk"
category: "other"
maker: "wienerdog-ai"
license: "MIT"
url: "https://github.com/wienerdog-ai/wienerdog"
source_code_url: "https://github.com/wienerdog-ai/wienerdog"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-02"
current_release: "2026-08-03"
stars: 14
language: "JavaScript"
homepage: "https://www.npmjs.com/package/wienerdog"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "yes"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "npx wienerdog@latest init"
docs_url: "https://github.com/wienerdog-ai/wienerdog/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/wienerdog"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Gives Claude Code and Codex CLI persistent memory, skills, and scheduled routines using nothing but plain files: an interview-generated CLAUDE.md/AGENTS.md profile, a git-versioned markdown memory vault in the Obsidian PARA convention shared by both tools, and a nightly dreaming job that promotes important info to long-term memory and turns repeated workflows into skills behind approval gates."
---

Wienerdog is an enhancement layer for the AI coding assistants you already have — Claude Code and Codex CLI — rather than an agent itself. It generates a CLAUDE.md or AGENTS.md profile through an interview so the assistant knows who you are at the start of each session, maintains a shared memory vault of markdown files following Obsidian's PARA convention and versioned in git that both tools read, and runs a nightly dreaming job that reviews conversations, promotes important information into long-term memory, and converts repeated workflows into reusable skills, with approval gates before anything changes. Optional extras include read-first Google Workspace access (Gmail, Calendar, Drive) and scheduled routines like a morning digest and weekly review via the OS's native scheduler. There is no daemon, no server, and no telemetry — the project describes itself as just files, fully uninstallable — and it contrasts itself with personal-agent apps like OpenClaw that require running daemons. It is pre-1.0 and largely written by AI models under its maintainer's spec system.
