---
name: "Vanna.AI"
slug: "vannaai"
layout: "agent.njk"
category: "other"
maker: null
license: "MIT"
url: "https://vanna.ai/"
source_code_url: null
source_available: "Yes"
platforms: []
first_released: null
current_release: null
stars: null
language: "Python"
homepage: "https://vanna.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Ollama, Azure, Google Gemini, AWS Bedrock, Mistral"
pricing: "open-source"
install_method: "pip install vanna"
docs_url: "https://vanna.ai/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/vanna-ai/vanna"
maintained: "dead"
sources:
  - "e2b"
what_makes_it_special: "Text-to-SQL via Agentic Retrieval; user-aware permissions at every layer including row-level SQL security filtering per user; pre-built framework-agnostic <vanna-chat> web component with streaming rich UI (tables, charts, summaries); enterprise features (audit logs, rate limiting, lifecycle hooks)."
---

Vanna exists because text-to-SQL fails in production when the model guesses: schemas are idiosyncratic, business terms are ambiguous, and permissions vary per user. Vanna's mechanism is a training corpus — DDL, documentation, and past validated queries — retrieved at question time so generated SQL reflects the organization's actual conventions, with each answered question feeding back into the store. The MIT-licensed Python framework (pip install vanna) works with any LLM (OpenAI, Anthropic, Gemini, Ollama, and others) and any major database, while the hosted cloud tier adds access control, observability, agent memory, and audit logging. Data teams and product builders embed it for natural-language analytics, and enterprise deployments use its per-user row-level security filtering; self-hosting is free, with paid cloud and enterprise tiers.
