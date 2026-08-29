---
name: "iosm-cli"
slug: "iosm-cli"
layout: "agent.njk"
category: "agent"
maker: "rokoss21"
license: "MIT"
url: "https://github.com/rokoss21/iosm-cli"
source_code_url: "https://github.com/rokoss21/iosm-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-09"
current_release: "2026-04-11"
stars: "151"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/iosm-cli"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Google, Groq, OpenRouter, Mistral, xAI, Cerebras, AWS Bedrock"
pricing: "Free / open-source (MIT); model provider costs apply separately"
install_method: "npm install -g iosm-cli or npx iosm-cli (requires Node.js >=20.6.0)"
docs_url: "https://github.com/rokoss21/iosm-cli/blob/main/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Terminal-native AI runtime (not a chat interface) for controlled engineering execution. Features the IOSM methodology (Improve -> Optimize -> Shrink -> Modularize) with 6 canonical metrics, IOSM-Index health score, deterministic orchestration (/contract -> /singular -> /swarm), filesystem checkpointing/rollback, session persistence, and artifact history."
---

iosm-cli enforces a measurable engineering discipline on top of LLM execution: every change cycle passes through Improve, Optimize, Shrink, and Modularize phases in strict order, scored on six canonical metrics rolled into an IOSM-Index, with guardrail breaches blocking progression. Complex work follows /contract to define the change, /singular to pick among three trade-off options, and /swarm for deterministic parallel execution with scopes, locks, and gates. Safety tooling includes checkpoints, rollback, snapshot/restore, a trust ledger, and optional bwrap sandboxing. Profiles switch between everyday coding, read-only planning, and orchestration-first meta mode, and integrations span JSON-RPC for IDEs, a Telegram bridge, and a TypeScript SDK.
