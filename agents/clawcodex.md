---
name: "clawcodex"
slug: "clawcodex"
layout: "agent.njk"
category: "agent"
maker: "agentforce314"
license: "MIT"
url: "https://github.com/agentforce314/clawcodex"
source_code_url: "https://github.com/agentforce314/clawcodex"
source_available: "True"
platforms: []
first_released: "2026-04-20"
current_release: "2026-08-17"
stars: "864"
language: "Python"
homepage: "https://clawcodex.app"
mcp_support: "partial — MCP-oriented tools and wiring implemented; clawcodex mcp serve re-exposes tools as MCP stdio server; OAuth server auth; full protocol polish ongoing"
plugin_support: "partial — plugins listed under Phase 4 roadmap (in progress); markdown-based SKILL.md slash commands as plugin-like system"
claude_code_plugin: "no"
subagents: "yes — Agent fan-out with parallel execution, isolated AbortControllers, concurrency-cap; /advisor worker/reviewer pairing; coordinator mode; Team/Brief tools"
hooks: "yes — production as of v1.0.0; types: UserPromptSubmit, PreToolUse (permissionDecision), PermissionRequest, MCP elicitation, teammate TaskCompleted/TeammateIdle stop hooks"
plan_mode: "yes — /plan mode with implicit entry/exit; keeps restraining edits even in Full Access sessions; --permission-mode plan flag"
model_providers: "Anthropic, OpenAI, DeepSeek, MiniMax, Gemini, OpenRouter, Ollama, vLLM, sglang, Groq, Cerebras, xAI, and more (30 total); subscription auth: Claude Pro/Max, ChatGPT Plus/Pro"
pricing: "open-source"
install_method: "pip"
docs_url: "https://clawcodex.app"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/agentforce314/clawcodex/releases"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Production-oriented Python rebuild of Claude Code (~310K lines); Terminal-Bench 2.1 score 80.9%; 30 model providers vs Claude Code's Claude-only limitation; /eco token compression (80% fewer Bash-output tokens); DeepSeek prefix cache (~230x cheaper); three UIs (TUI, Web, Desktop)."
---

ClawCodex keeps Claude Code's architecture - the same query loop, tool set, two-tier state, and hooks - while removing its single-vendor constraint: thirty providers from Anthropic and OpenAI to DeepSeek, MiniMax, Ollama, and vLLM are supported, plus subscription OAuth for Claude Pro/Max and ChatGPT. Its /eco toggle applies deterministic output filters (failure-focused test summaries, git and package-manager ceremony stripping, log dedup) to cut Bash output tokens by roughly 80 percent, with full output teed to disk so nothing is lost. The agent core is shared by CLI, TUI, Desktop, and Web surfaces, and releases ship weekly with published benchmark claims. Engineers who want the Claude Code workflow on cheaper or local models are the target users.
