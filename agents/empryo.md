---
name: "Empryo"
slug: "empryo"
layout: "agent.njk"
category: "agent"
maker: "proxysoul"
license: "NOASSERTION"
url: "https://github.com/proxysoul/Empryo"
source_code_url: "https://github.com/proxysoul/Empryo"
source_available: "True"
platforms: []
first_released: "2026-03-01"
current_release: "2026-08-10"
stars: "971"
language: "TypeScript"
homepage: "https://empryo.com/"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google, Groq, DeepSeek, Bedrock, Ollama, LM Studio, OpenAI-compatible endpoints, LLM Gateway (22 providers total)"
pricing: "free"
install_method: "binary"
docs_url: "https://empryo.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://empryo.com/download"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI coding agent that builds a live dependency graph (genome) of the repo using tree-sitter, then edits code through AST symbol-level operations rather than find-and-replace strings. 65+ atomic AST operations with rollback across 30+ languages, blast-radius analysis before edits, 5.7x fewer input tokens than competitors, time machine (git checkpoint per prompt), and free structural context compaction (no LLM call). Three surfaces: desktop, TUI, and headless CLI."
---

Empryo (successor to SoulForge) was built around the observation that string-level find-and-replace edits are the dominant failure mode of LLM coding agents. On launch it parses the repository with tree-sitter into a live graph of symbols, imports, and call sites, ranked by PageRank and git co-change frequency to estimate blast radius, and graph queries run locally at zero token cost. Edits are batches of atomic symbol-level operations with all-or-nothing rollback and a typecheck gate, and a multi-agent layer routes ten roles (brain, spark, explore, verify, and others) across 22 model providers so cheap models scout while strong models write. It ships as CLI, TUI, desktop app, and headless CLI on macOS, Linux, and Windows, with any MCP server and 576+ LSP servers attachable.
