---
name: "ifai"
slug: "ifai"
layout: "agent.njk"
category: "agent"
maker: "peterfei"
license: "MIT"
url: "https://github.com/peterfei/ifai"
source_code_url: "https://github.com/peterfei/ifai"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-12-13"
current_release: "2026-06-10"
stars: "99"
language: "Rust, TypeScript, React"
homepage: "https://docs.ifai.today"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "DeepSeek, Kimi, Qwen, NVIDIA NIM, local LLMs, custom API (5 providers, 80+ models)"
pricing: "Free / open source"
install_method: "git clone + npm install + npm run tauri dev (requires Node.js >=18, Rust >=1.80)"
docs_url: "https://docs.ifai.today/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/peterfei/ifai/releases"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "AI-native architecture with 9+ agents orchestrated via YAML DAG workflows, 120 FPS rendering with Rust core, local-first privacy with edge model support, shell-level agent autonomy, symbol-aware RAG via tree-sitter, declarative intent routing (O(1)), and Composer 2.0 for parallel multi-file AI editing"
---

ifai (若爱) is built as an editor where agents, not humans, do most of the typing: a Rust/Tauri core hosts nine-plus agents — explore, review, refactor, test, plan, ReAct, git-commit, debug, doc — that can call each other to a depth of five and run in parallel through call_agent_parallel. Workflows are declared in YAML and scheduled by topological sort, with a React Flow view of node status. Composer 2.0 handles parallel multi-file edits with diff accept/reject and rollback, backed by tree-sitter symbol-aware RAG. Routing is a declarative O(1) lookup, and agents hold shell-level autonomy to configure and heal themselves. Five provider backends cover DeepSeek, Kimi, Qwen, NVIDIA NIM, and local models, keeping a local-first privacy posture.
