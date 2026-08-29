---
name: "Graft"
slug: "graft"
layout: "agent.njk"
category: "other"
maker: "NanoNets"
license: "MIT"
url: "https://github.com/NanoNets/Graft"
source_code_url: "https://github.com/NanoNets/Graft"
source_available: "Yes"
platforms: []
first_released: "2026-07-03"
current_release: "2026-08-19"
stars: "3773"
language: "TypeScript"
homepage: "https://graft.nanonets.ai"
mcp_support: "yes (MCP server with 6 tools: graft_find_code, graft_file_api, graft_trace_calls, graft_find_all, graft_repo_map, graft_check_freshness; auto-registered via graft init)"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: null
hooks: "yes"
plan_mode: null
model_providers: "OpenAI, Anthropic, OpenRouter, Fireworks, Groq, local"
pricing: "free"
install_method: "npm"
docs_url: "https://graft.nanonets.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Open-source context layer that builds a linked markdown graph of a codebase once, then feeds it to coding agents (Claude Code, Cursor, Codex, Gemini) for faster, cheaper, better-contextualized work; up to 4x cheaper and +12 pts on SWE-bench Verified."
---

Graft addresses the cost and error rate that come from coding agents re-deriving codebase structure on every task. On initialization it builds a graft/ directory of linked markdown nodes describing subsystems with typed relationships such as depends_on, alongside a per-symbol wiring graph produced by tree-sitter parsing with no model calls. Registered coding agents — Claude Code, Cursor, Codex, Gemini, Copilot, Windsurf, and others — consume this graph through instruction files, lifecycle hooks that warn about blast radius and re-sync the graph, and an MCP server exposing six lookup tools like graft_find_code and graft_trace_calls. The structural analysis is local and free; optional LLM-written summaries use the developer's own API key across OpenAI, Anthropic, OpenRouter, Fireworks, Groq, or local models. NanoNets maintains it as an open-source project and reports measured gains on SWE-bench Verified alongside per-repo cost and latency reductions.
