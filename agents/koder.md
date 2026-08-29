---
name: "koder"
slug: "koder"
layout: "agent.njk"
category: "agent"
maker: "feiskyer"
license: "MIT"
url: "https://github.com/feiskyer/koder"
source_code_url: "https://github.com/feiskyer/koder"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-07-28"
current_release: "2026-07-19"
stars: "91"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "yes"
model_providers: "OpenAI, Anthropic, Google/Gemini, GitHub Copilot, Azure, OpenRouter, 100+ LiteLLM providers, custom OpenAI-compatible"
pricing: "open-source"
install_method: "uv tool install koder | pip install koder"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Local-first (no session uploads), bring-your-own-model across 100+ providers with universal KODER_* env vars and OAuth-backed subscription logins (Google, Claude, ChatGPT, Antigravity, GitHub Copilot); durable long-running work with goals, token budgets, cron-backed scheduled loops, and resume; SQLite sessions with rewind/thinkback/AutoDream consolidation; rich multi-agent workflows (subagents, teams, tmux teammates, mailbox routing); extensible via skills/plugins/MCP/channels/Magic Docs; sandbox-aware permissions; optional voice dictation. Alpha/experimental, learning-focused."
---

koder is an alpha-stage, single-author Python terminal agent built around local inspectability: sessions, transcripts, tokens, and permissions live in SQLite under ~/.koder, and a /privacy-settings surface shows exactly what leaves the machine. Subscription access is handled through OAuth logins (koder auth login claude|chatgpt|github-copilot|...) while OpenAI, Anthropic, Gemini, OpenRouter, Azure, and LiteLLM providers work via API keys or KODER_* environment variables. Background subagents, tmux teammates, mailbox routing, cron-backed scheduled loops, and goal continuation with token budgets support longer-running work. As an explicitly experimental project by feiskyer, it is used for learning agentic-system design and for BYO-model terminal work rather than production deployment.
