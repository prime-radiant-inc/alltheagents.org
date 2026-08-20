---
name: "CoreCoder"
slug: "corecoder"
layout: "agent.njk"
category: "agent"
maker: "he-yufeng"
license: "MIT"
url: "https://github.com/he-yufeng/CoreCoder"
source_code_url: "https://github.com/he-yufeng/CoreCoder"
source_available: True
platforms: []
first_released: "2026-04-01"
current_release: "2026-08-04"
stars: "1657"
language: "Python 3.10+"
homepage: "https://pypi.org/project/corecoder/"
mcp_support: "no - explicitly listed as a missing feature to add in a fork"
plugin_support: "no"
claude_code_plugin: "no - standalone reimplementation inspired by Claude Code"
subagents: "yes - agent tool spawns sub-agents with isolated context, one fewer tool, shorter round limit"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, DeepSeek, Ollama, Kimi, Qwen, 100+ via LiteLLM"
pricing: "open-source"
install_method: "pip"
docs_url: "https://github.com/he-yufeng/CoreCoder"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "'The nanoGPT of coding agents' - radical minimalism at ~1,081 lines across 8 core files, readable in an afternoon. A genuinely runnable teaching tool (86 tests green) that reads/writes files, runs shell, spawns sub-agents, compacts context in 3 tiers (50%/70%/90% thresholds), and reports token cost. Unique-match search/replace editing anchors on unique snippets instead of line numbers. Sub-agents constrained by tool-withholding rather than rules. Companion bilingual essay series walking through how agents like Claude Code work."
---

'The nanoGPT of coding agents' - radical minimalism at ~1,081 lines across 8 core files, readable in an afternoon. A genuinely runnable teaching tool (86 tests green) that reads/writes files, runs shell, spawns sub-agents, compacts context in 3 tiers (50%/70%/90% thresholds), and reports token cost. Unique-match search/replace editing anchors on unique snippets instead of line numbers. Sub-agents constrained by tool-withholding rather than rules. Companion bilingual essay series walking through how agents like Claude Code work.
