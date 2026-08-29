---
name: "tig"
slug: "tig"
layout: "agent.njk"
category: "agent"
maker: "rsrohan99"
license: null
url: "https://github.com/rsrohan99/tig"
source_code_url: "https://github.com/rsrohan99/tig"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-04-20"
current_release: "2025-05-02"
stars: "153"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google, DeepSeek, Groq, Ollama, OpenRouter"
pricing: "open-source"
install_method: "pip install tig-code"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/tig-code/"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Terminal-based autonomous AI coding agent similar to Claude Code/OpenAI Codex but works with many more LLMs; uses LlamaIndex Workflow, Tree-sitter, Ripgrep, and Google's diff-match-patch. Has an Architect mode (designs system) and Code mode (implements plan)."
---

Tig is a terminal coding agent built in the vein of Claude Code but with provider breadth as its main feature: it runs against Gemini, OpenAI, Claude, DeepSeek, Groq, OpenRouter, or local Ollama models, selected through environment variables. Work is split into two modes — Architect, which discusses a design with the user and saves it to a markdown file, and Code, which implements the plan step by step with approval gates (or --auto-approve for unattended runs). Under the hood it composes LlamaIndex Workflows for orchestration, tree-sitter for symbol search and syntax validation, ripgrep for fast text search, and diff-match-patch for reviewable diffs. The project is a compact Python package (pip install tig-code) with a YouTube build-along series, which doubles as its documentation. It suits developers who want a Claude Code-style loop untethered from any single vendor.
