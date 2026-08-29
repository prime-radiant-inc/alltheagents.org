---
name: "Omnara"
slug: "omnara"
layout: "agent.njk"
category: "multiplexer"
maker: "omnara-ai"
license: "MIT"
url: "https://www.omnara.com"
source_code_url: "https://github.com/omnara-ai/omnara"
source_available: "Yes"
platforms:
  - "Web"
  - "Mobile"
first_released: "2025-01-01"
current_release: "2026-08-20"
stars: "2747"
language: "TypeScript"
homepage: "https://www.omnara.com"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "BYO: OpenAI Responses, Chat Completions, or Anthropic Messages APIs (OpenRouter, LiteLLM, Ollama compatible)"
pricing: "freemium"
install_method: "git clone; docker compose -f compose.yaml --profile app up -d (self-hosted); or Omnara Cloud"
docs_url: "https://docs.omnara.com/introduction"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Positions itself as the API for production-grade agents — durable agent state committed atomically to Postgres with auto-recovery, hot-add/remove machines mid-run, and direct SQL access to agent state for analytics when self-hosted."
---

Omnara provides the execution and state layer for agents that teams define themselves, separating infrastructure from model choice, tooling, and user interface. Agent state commits atomically to Postgres so runs survive crashes and disconnects, and machines — cloud sandboxes or the operator's own hardware — can join or leave a run without restarts. Tools come from built-ins, custom code, skills, or MCP servers, and access control uses organization and project roles. Teams interact through a dashboard, a Slack connector, or the REST/TypeScript API rather than a chat product. The Apache-2.0 codebase self-hosts via Docker Compose, with a hosted cloud offering alongside it.
