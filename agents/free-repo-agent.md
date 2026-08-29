---
name: "Free Repo Agent"
slug: "free-repo-agent"
layout: "agent.njk"
category: "agent"
maker: "SUMITKUMARSINGH"
license: "MIT"
url: "https://open-vsx.org/extension/SUMITKUMARSINGH/free-repo-agent"
source_code_url: "https://github.com/sumitsingh4411/repo-agent.git"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-07-31"
current_release: null
stars: null
language: null
homepage: "https://github.com/sumitsingh4411/repo-agent#readme"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic, DeepSeek"
pricing: "BYOK"
install_method: "Install from Open VSX"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-vsx.org/extension/SUMITKUMARSINGH/free-repo-agent"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Free repo-aware autonomous coding agent (DeepSeek) that edits files and runs commands"
---

The extension targets developers who want Copilot-style autonomous editing without a subscription, using DeepSeek V4 Flash (default, 1M context) or V4 Pro models behind a user-supplied API key, with any OpenAI-compatible provider configurable as a fallback. It indexes the repository and injects relevant files into answers, applies edits across files with Keep/Undo inline controls, and runs shell commands behind an approval gate. After editing, it runs typecheck or build and repairs errors before declaring a task done, and it keeps project context in a memory.md file plus a generated codebase brief. Vision input routes through a free Gemini endpoint by default, and one-click MCP plugins add GitHub, web search, Postgres, Playwright, and filesystem tools.
