---
name: "caveman-code"
slug: "caveman-code"
layout: "agent.njk"
category: "agent"
maker: "JuliusBrussee"
license: "MIT"
url: "https://github.com/JuliusBrussee/caveman-code"
source_code_url: "https://github.com/JuliusBrussee/caveman-code"
source_available: True
platforms:
  - "CLI"
first_released: "2026-04-08"
current_release: "2026-08-14"
stars: "922"
language: "TypeScript"
homepage: "https://caveman.so/"
mcp_support: "yes — full, Claude Code-compatible superset; transports: stdio, Streamable HTTP, in-process; OAuth 2.1 + PKCE"
plugin_support: "yes — plugin marketplace via caveman plugin command"
claude_code_plugin: "no"
subagents: "yes — up to 7 parallel, worktree-isolated subagents; 5 ship by default; triggered via Task tool"
hooks: "yes — identical to Claude Code hooks; run as observers, never block"
plan_mode: "yes — /plan toggles read-only mode (model restricted to read/grep/find/ls); /act executes the saved plan"
model_providers: "Anthropic, OpenAI, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, DeepSeek, Google Gemini, GitHub Copilot, Claude Pro/Max, ChatGPT Plus/Pro, and more (20+)"
pricing: "open-source"
install_method: "npm"
docs_url: "https://caveman.so/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "abandoned"
sources:
  - "github_topic2"
what_makes_it_special: "4-layer token compression always on (Caveman Mode, Tool Budgets, Read Dedup, RTK); ~2x fewer tokens than Codex CLI on identical tasks; Claude Code-compatible superset — paste existing settings/commands/skills/agents/.mcp.json configs and they work."
---

4-layer token compression always on (Caveman Mode, Tool Budgets, Read Dedup, RTK); ~2x fewer tokens than Codex CLI on identical tasks; Claude Code-compatible superset — paste existing settings/commands/skills/agents/.mcp.json configs and they work.
