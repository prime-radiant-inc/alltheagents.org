---
name: "Coro Code"
slug: "coro-code"
layout: "agent.njk"
category: "agent"
maker: "Blushyes"
license: "Apache-2.0, MIT (dual)"
url: "https://github.com/Blushyes/coro-code"
source_code_url: "https://github.com/Blushyes/coro-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-08-13"
current_release: "2025-10-30"
stars: "368"
language: "Rust"
homepage: "https://sofast.fun"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, Google, Azure OpenAI, OpenAI-compatible (DeepSeek)"
pricing: "Free / open-source"
install_method: "cargo install --git https://github.com/Blushyes/coro-code --bin coro"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "High-performance AI coding agent in Rust with rich terminal UI; cross-platform; extensible tool system; context export/restore persistence; OpenAI-compatible API support. MCP and plugin systems planned on roadmap. Positioned as a free alternative to Claude Code."
---

Claude Code established the terminal-agent workflow, but it is proprietary and tied to one vendor's models, leaving room for an open, inspectable equivalent. Coro Code implements that workflow in Rust: a single cross-platform binary runs an agent loop with bash execution, file operations, and an extensible tool system, presented through a rich terminal UI with real-time streaming. Session state persists via JSON context export and restore, and token compression keeps long sessions within budget. The LLM layer targets OpenAI and OpenAI-compatible endpoints (DeepSeek among them), with Anthropic and Google support on the roadmap alongside permission systems, sandboxing, and MCP extension. Developers wanting a self-hosted terminal agent they can inspect and modify - particularly in Rust ecosystems - are the audience; the project is early but actively developed.
