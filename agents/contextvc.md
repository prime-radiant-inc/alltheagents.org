---
name: "contextvc"
slug: "contextvc"
layout: "agent.njk"
category: "other"
maker: "HaochengLu"
license: "Apache-2.0"
url: "https://github.com/HaochengLu/contextvc"
source_code_url: "https://github.com/HaochengLu/contextvc"
source_available: "True"
platforms: []
first_released: "2026-07-05"
current_release: "2026-07-05"
stars: "143"
language: "Rust"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: null
pricing: "Free / open-source (Apache-2.0)"
install_method: "cargo install --locked --git https://github.com/HaochengLu/contextvc.git --tag v0.1.0 (requires Rust stable toolchain)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Git-native context control plane: treats agent memory as repo-level infrastructure (versioned, reviewed, merged, CI-checked, enforced). Single source of truth in .context/ compiles to multiple agent-native files (Claude Code, Cursor, Codex, Copilot, Gemini, Cline). Enforces constraints before risky actions via precheck gates. Human review queue for runtime-learned proposals. RepeatBench for failure-prevention benchmarking."
---

Agent instruction files - CLAUDE.md, AGENTS.md, Cursor rules - multiply across tools, drift out of sync, and receive none of the review discipline applied to code. ContextVC makes that memory a git-native control plane: typed Markdown objects (constraints, decisions, failures, how-tos, code maps, preferences) live in a .context/ directory, and a render command compiles them into each tool's native format while preserving human-written text outside managed blocks. Enforcement goes beyond documentation - precheck hooks return warn, ask, or block before risky actions, CI health checks fail on drift or stale bindings, and runtime failures feed a review workflow where a human accepts proposals before they become formal memory. A local stdio MCP server exposes search and status tools to any MCP client, and context objects support log, blame, diff, and revert through normal Git semantics. Teams running multiple agents over one repository use it to keep context consistent and reviewed.
