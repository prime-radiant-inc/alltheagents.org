---
name: "golutra"
slug: "golutra"
layout: "agent.njk"
category: "multiplexer"
maker: "golutra"
license: "BSL-1.1"
url: "https://github.com/golutra/golutra"
source_code_url: "https://github.com/golutra/golutra"
source_available: "True"
platforms: []
first_released: "2026-02-15"
current_release: "2026-08-06"
stars: "3825"
language: "TypeScript, Rust"
homepage: "https://www.golutra.com"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, Gemini CLI, Codex CLI, OpenCode, Qwen Code, OpenClaw, any CLI"
pricing: "open-source"
install_method: "binary"
docs_url: "https://www.golutra.com/"
plugin_docs_url: "https://github.com/golutra/golutra-mcp"
config_docs_url: null
download_url: "https://github.com/golutra/golutra/releases"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Multi-agent AI orchestration workspace (Tauri desktop app) that unifies existing CLI coding tools into a parallel AI workforce. CLI-native approach — no migration, keeps existing CLI tools while adding multi-agent orchestration. Visual + terminal hybrid (Stealth Terminal with direct prompt injection into terminal streams), unlimited parallel multi-agent execution with automated result handoff, one-click template import/export, real-time monitoring. MCP via golutra-mcp, memory via EverOS. BSL-1.1 licensed (free for commercial software development). Early stage but actively developed."
---

Golutra is built for the solo developer running several CLI agents at once and refusing to migrate off them. The desktop app (Tauri, Vue 3 and Rust) hosts parallel sessions of Claude Code, Gemini CLI, Codex CLI, OpenCode, Qwen Code, or any CLI tool, adding orchestration, automated result handoff between agents, one-click workflow templates, and real-time monitoring, with prompts injected directly into terminal streams. An MCP bridge (golutra-mcp) connects tool servers and EverOS provides long-running memory, and the roadmap points toward month-long autonomous orchestration under a 'CEO Agent.' It is source-available under BSL-1.1, free for commercial software development, actively developed by a solo maintainer, and has reached 3.8k stars since early 2026.
