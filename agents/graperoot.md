---
name: "GrapeRoot"
slug: "graperoot"
layout: "agent.njk"
category: "other"
maker: "kunal12203"
license: "Apache-2.0"
url: "https://github.com/kunal12203/GrapeRoot"
source_code_url: "https://github.com/kunal12203/GrapeRoot"
source_available: "True"
platforms: []
first_released: "2026-02-21"
current_release: "2026-08-04"
stars: "1023"
language: "Python, TypeScript"
homepage: "https://graperoot.dev"
mcp_support: "yes (stdio)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Claude Code, OpenAI Codex CLI, Cursor, Gemini CLI, OpenCode, GitHub Copilot, OpenClaw, Kilocode, MiMo Code, Antigravity, Kiro CLI, Command Code, MiniMax"
pricing: "freemium"
install_method: "pip, binary"
docs_url: "https://graperoot.dev/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/graperoot/"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Open-source context engine that builds a semantic graph of the codebase (files, symbols, imports, call chains) and pre-loads relevant code into every prompt before the AI sees it, reducing token waste and exploration turns. Session memory compounds across a session with up to 81% cost reduction. All processing is local — no code leaves your machine. Hard-capped token budget per turn."
---

GrapeRoot addresses the token cost of agentic exploration: rather than letting the model discover a codebase through repeated tool calls, it builds a local semantic graph of files, symbols, imports, and call chains, then packs the highest-ranked relevant code into the prompt before each turn. The graph also tracks session memory — files read, edited, or queried — so later turns carry less and less exploratory overhead, and per-turn token budgets are enforced with configurable caps. It integrates with Claude Code, Codex CLI, Cursor, Gemini CLI, OpenCode, GitHub Copilot, and other assistants through launcher commands, plus MCP tools (graph_read, graph_retrieve, graph_neighbors) for direct drill-down. All processing stays local, and the project claims roughly 43% average cost reduction on large codebases with turn counts dropping from 11.7 to 3.5. The launchers are Apache-2.0 open source while the core PyPI engine is proprietary and free to use.
