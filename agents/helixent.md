---
name: "helixent"
slug: "helixent"
layout: "agent.njk"
category: "agent"
maker: "MagicCube"
license: "MIT"
url: "https://github.com/MagicCube/helixent"
source_code_url: "https://github.com/MagicCube/helixent"
source_available: "yes"
platforms: []
first_released: "2026-04-06"
current_release: "2026-05-21"
stars: "649"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "yes"
model_providers: "OpenAI-compatible (any OpenAI-compatible endpoint)"
pricing: "open-source"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/helixent"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "TypeScript library and CLI for building ReAct-style AI agent loops. Three-layer architecture (Foundation, Agent Loop, Coding Agent) keeping provider integrations decoupled and reusable. Bun-powered (same runtime as Claude Code, fast cold starts, compiles to a single self-contained native binary). First-class middleware/hooks: 8 hooks (beforeAgentRun, afterAgentRun, beforeAgentStep, afterAgentStep, beforeModel, afterModel, beforeToolUse, afterToolUse). Human-in-the-loop approval of tool calls. Long-term memory via automatic AGENTS.md pickup. Standard agent skills format (agentskills.io) support with multi-directory discovery. Subagents are on the roadmap (not yet implemented)."
---

helixent is both a TypeScript library for building ReAct-style agent loops and a usable coding agent built on top of them. Its three layers separate concerns: a foundation of provider-agnostic model, message, and tool primitives; a domain-agnostic agent loop with parallel tool invocation, middleware hooks at eight lifecycle points, and human-in-the-loop approval; and a coding layer with bash, file editing, patching, and search tools plus a todo-based plan mode. Skills follow the standard agentskills.io format and are auto-discovered from global and project directories, and AGENTS.md files at the repo root serve as project guidance. The whole stack runs on Bun — chosen deliberately because Claude Code uses the same runtime — with Ink/React for the TUI and single-binary compilation for distribution. It targets developers who want a readable, modifiable agent codebase as much as a daily coding tool.
