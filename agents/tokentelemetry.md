---
name: "tokentelemetry"
slug: "tokentelemetry"
layout: "agent.njk"
category: "other"
maker: "VasiHemanth"
license: "MIT"
url: "https://github.com/VasiHemanth/tokentelemetry"
source_code_url: "https://github.com/VasiHemanth/tokentelemetry"
source_available: "True"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2026-04-24"
current_release: "2026-08-18"
stars: "315"
language: "Python, TypeScript"
homepage: "https://tokentelemetry.com/docs/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "n/a"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, Google, OpenAI, xAI, Meta (Muse), Qwen (provider-aware pricing across direct/OpenRouter/Together/Fireworks)"
pricing: "Free/open-source (MIT)"
install_method: "macOS/Linux: curl -fsSL https://tokentelemetry.com/install.sh | bash; Windows: irm https://tokentelemetry.com/install.ps1 | iex; or clone and run ./start.sh / start.bat / node bin/cli.js"
docs_url: "https://tokentelemetry.com/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/VasiHemanth/tokentelemetry"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "100% local observability dashboard for AI coding agents and autonomous agents: tracks token usage, LLM costs, tool calls, session traces, and reasoning steps. Zero-config (auto-detects agent logs), no signup, no SDK, no cloud - unlike Langfuse/LangSmith/Helicone. Includes a dedicated Hermes Agent autonomous-agent dashboard across 38 source platforms."
---

tokentelemetry is a local-first observability dashboard for AI coding and autonomous agents, built on the observation that most agents already write detailed JSONL logs that nobody aggregates. It watches those files directly — Claude Code's session logs, Gemini CLI, Codex, Cursor, Copilot, OpenCode, and more — parsing token counts, tool calls, session traces, and reasoning steps without any SDK, instrumentation, or account, then renders dashboards for usage, per-project costs with provider-aware pricing, budgets, and traces; a dedicated Hermes Agent view covers that autonomous agent's 38 source platforms, skills, memory, and subagents. The stack is FastAPI plus Next.js, state lives in plain JSON under ~/.tokentelemetry, and everything binds to localhost with optional token-authed remote access; the only outbound calls are an update check and opt-in, content-free telemetry. It is MIT-licensed, installable via a curl script, and positioned against cloud APM tools like Langfuse and LangSmith for developers who want cost and behavior visibility without sending data anywhere.
