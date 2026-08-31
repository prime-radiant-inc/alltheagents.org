---
name: "IX"
slug: "ix"
layout: "agent.njk"
category: "agent-sdk"
maker: "kreneskyp"
license: "MIT"
url: "https://github.com/kreneskyp/ix"
source_code_url: "https://github.com/kreneskyp/ix"
source_available: "True"
platforms:
  - "IDE"
  - "Autonomous"
first_released: "2023-04-05"
current_release: "2026-01-01"
stars: "1044"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Google PaLM, Anthropic, Llama"
pricing: "open-source"
install_method: "pip, docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "e2b"
  - "jim"
what_makes_it_special: "Platform for designing and deploying autonomous and semi-autonomous LLM-powered agents and workflows with a no-code visual agent editor for connecting nodes into a cognitive graph. Multi-agent chat interface with smart input auto-completion, where an IX moderator agent delegates tasks to specialized agents. Horizontally scalable message-queue-driven agent workers."
---

IX arrived when GPT-4 agent platforms were the frontier: a Django + React app where you compose an agent's cognitive graph from LangChain components on a node canvas, then deploy it behind a moderator-agent chat room and Celery workers that scale on message queues. Use cases spanned QA chatbots, code generation, data extraction, and research assistants, with OpenAI as the primary backend and PaLM, Anthropic, and Llama experimental. The visual editor, embedded chat debugging, and horizontal worker scaling were its distinguishing ideas. Development has since stalled — the branding and model list date it to 2023 — and it survives as historical agent-platform engineering.
