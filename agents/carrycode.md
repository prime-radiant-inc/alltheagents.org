---
name: "carrycode"
slug: "carrycode"
layout: "agent.njk"
category: "agent"
maker: "zhangliang605"
license: "Custom (source-available; commercial use allowed but prohibits modifying Logo/Banner/identifying marks without permission)"
url: "https://github.com/zhangliang605/carrycode"
source_code_url: "https://github.com/zhangliang605/carrycode"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-01-24"
current_release: "2026-03-15"
stars: "44"
language: "Rust and TypeScript"
homepage: "https://carrycode.ai"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "OpenAI, Anthropic, Google Gemini, DeepSeek, Moonshot/Kimi, ZhipuAI, MiniMax, Alibaba Cloud, xAI, SiliconFlow, Ollama, vLLM, any OpenAI-compatible"
pricing: "open-source"
install_method: "curl -fsSL https://carrycode.ai/install.sh | sudo sh (macOS/Linux) or irm https://carrycode.ai/install.ps1 | iex (Windows); VSCode Extension marketplace search 'carrycode'; build from source using Rust, Node.js, Bun"
docs_url: "https://carrycode.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://carrycode.ai/install.sh"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Terminal-native AI coding agent connecting to 17+ LLM providers with beautiful terminal UI (themes, syntax highlighting, code diff previews, Mermaid diagram rendering). Supports MCP protocol (via /mcp), VSCode extension plugin, AGENTS.md project instructions, LSP diagnostics integration, smart context compaction, Skills system compatible with Claude Code, SkillHub integration (Tencent), approval modes for autonomy control. Dual Build and Plan modes."
---

carrycode is a terminal-first coding agent built in Rust with a TypeScript layer, aimed at developers who live in the shell and want agent capability without leaving it. It renders a rich TUI with themes, syntax-highlighted diffs, and Mermaid diagrams rendered as ASCII, and supports MCP servers, a skills system compatible with Claude Code, AGENTS.md project rules, LSP diagnostics, and context compaction for long sessions. Agent autonomy is governed through explicit modes — a read-only Plan mode for analysis and a Build mode gated by approval levels — and a single-shot CLI mode supports scripting. Model access spans 17+ providers (OpenAI, Anthropic, Gemini, DeepSeek, Kimi, GLM, MiniMax, Qwen, xAI, SiliconFlow, Ollama, vLLM, and OpenAI-compatible endpoints). The project is source-available under a custom license, installs via curl or a VS Code extension, and is actively maintained with frequent releases; a VS Code extension extends the same engine into the editor.
