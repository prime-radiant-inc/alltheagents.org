---
name: "claude-memory-compiler"
slug: "claude-memory-compiler"
layout: "agent.njk"
category: "agent"
maker: "coleam00"
license: null
url: "https://github.com/coleam00/claude-memory-compiler"
source_code_url: "https://github.com/coleam00/claude-memory-compiler"
source_available: True
platforms: []
first_released: "2026-04-06"
current_release: "2026-04-06"
stars: "1277"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "Anthropic"
pricing: "free"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "No RAG / no vector DB / no embeddings — uses a markdown index.md that the LLM reads directly (inspired by Karpathy's LLM Knowledge Base architecture). Captures Claude Code conversations via hooks (SessionStart, SessionEnd, PreCompact), extracts decisions/lessons using Claude Agent SDK, compiles daily logs into cross-referenced knowledge articles. Runs on existing Claude subscription at no extra API cost."
---

No RAG / no vector DB / no embeddings — uses a markdown index.md that the LLM reads directly (inspired by Karpathy's LLM Knowledge Base architecture). Captures Claude Code conversations via hooks (SessionStart, SessionEnd, PreCompact), extracts decisions/lessons using Claude Agent SDK, compiles daily logs into cross-referenced knowledge articles. Runs on existing Claude subscription at no extra API cost.
