---
name: "QodeAssist"
slug: "qodeassist"
layout: "agent.njk"
category: "agent"
maker: "Palm1r"
license: "GPL-3.0"
url: "https://github.com/Palm1r/QodeAssist"
source_code_url: "https://github.com/Palm1r/QodeAssist"
source_available: "True"
platforms: []
first_released: "2024-08-27"
current_release: "2026-08-03"
stars: "435"
language: "C++, QML"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Ollama, llama.cpp, LM Studio, Anthropic Claude, OpenAI (Chat + Responses), Google Gemini, Mistral/Codestral, Qwen, DeepSeek, OpenRouter, OpenAI-compatible"
pricing: "Free / open-source (GPL-3.0); commercial license available on request"
install_method: "Via Qt Creator Extension Registry (add external repository URL) or manual plugin archive installation through Help -> About Plugins"
docs_url: "https://github.com/Palm1r/QodeAssist/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Palm1r/QodeAssist/releases"
maintained: "dormant"
sources:
  - "github_deep"
what_makes_it_special: "AI-powered coding assistant plugin for Qt Creator providing code completion, chat, quick refactoring, and project-aware tool calling for C++ and QML; dual MCP server/client support; agent skills compatible with Claude Code/Cursor skill format. Winding down / maintenance-only; no new features, issues and PRs closed"
---

QodeAssist fills a gap most AI coding tools ignore: native AI assistance inside Qt Creator for C++ and QML development. Its chat and quick-refactor modes drive project-aware tools — reading and editing files, searching, building and reading compiler diagnostics, running terminal commands with confirmation, and tracking multi-step work through a todo tool. Unusually for an IDE plugin, it works bidirectionally with MCP: it can serve its project context to external clients like Claude Code or Cursor, and consume tools from external MCP servers itself. It implements the open Agent Skills format, discovering skills from project and global .claude/skills directories compatible with the Claude Code ecosystem. Completion and chat models come from local runtimes (Ollama, llama.cpp, LM Studio) or cloud providers, with FIM completion trigger modes that control API spend. The author has placed the project in maintenance-only status, so it remains useful for Qt developers but is not gaining features.
