---
name: "Claude Engineer"
slug: "claude-engineer"
layout: "agent.njk"
category: "agent"
maker: "Doriandarko"
license: "MIT"
url: "https://github.com/Doriandarko/claude-engineer"
source_code_url: "https://github.com/Doriandarko/claude-engineer"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2024-06-24"
current_release: "2024-12-12"
stars: null
language: "Python"
homepage: "https://github.com/Doriandarko/claude-engineer"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude 3.5 Sonnet)"
pricing: "free"
install_method: "git clone, uv venv, uv run app.py (web) or uv run ce3.py (CLI)"
docs_url: "https://github.com/Doriandarko/claude-engineer#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Doriandarko/claude-engineer"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "jim"
  - "ishandutta"
what_makes_it_special: "Self-improving architecture — Claude can autonomously identify capability gaps, design, and implement new tools during conversations, making the framework more powerful with continued use; available as both CLI and web interface."
---

Claude Engineer was an early (2024) demonstration that an agent's toolset could be emergent rather than fixed: when a task exceeds the built-in tools (file operations, E2B code execution, web search), the model designs and implements a new tool during the conversation, and the runtime loads it without restart. Both a web UI and CLI expose the same agent, with image analysis and token-usage visualization. The approach trades reliability for extensibility, since self-written tools vary in quality. It attracted a large following (over 11k stars) as a reference design for self-improving agents, but the maintainer stopped committing in December 2024, leaving many pull requests unmerged.
