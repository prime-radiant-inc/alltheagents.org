---
name: "formax"
slug: "formax"
layout: "agent.njk"
category: "agent"
maker: "yusifeng"
license: "MIT"
url: "https://github.com/yusifeng/formax"
source_code_url: "https://github.com/yusifeng/formax"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-30"
current_release: "2026-07-24"
stars: "191"
language: "TypeScript"
homepage: "https://github.com/yusifeng/formax"
mcp_support: "False"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, OpenAI-compatible"
pricing: "Free / open-source (Beta)"
install_method: "npm i -g @yusifeng/formax@beta"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@yusifeng/formax"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Open-source implementation of a Claude Code-style AI assistant built 100% with Codex (AI-assisted development traces intentionally kept in repo); implements Claude Code behavior by reverse-engineering/observation; offers both terminal (TUI) and web (GUI) interfaces modeled after the Codex UI. Beta stage, suited for learning/experimentation."
---

Claude Code is closed source, and formax exists to answer the question of what a Claude Code-style harness looks like on the inside. The author reconstructed its behavior from network traces and observation, then rebuilt it in a TypeScript/Node monorepo with an Ink-based TUI, a web GUI, and a JSON-RPC app-server with a WebSocket bridge mode. It supports Anthropic and OpenAI-compatible endpoints, mirrors Claude Code workflows such as /init CLAUDE.md generation, plan mode, and sub-agent code review, and documents MCP and hooks as known gaps. The repository deliberately preserves the Codex build artifacts, plans, and docs, which makes it a reference for developers studying how agentic coding harnesses are constructed.
