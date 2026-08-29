---
name: "Bazed"
slug: "bazed"
layout: "agent.njk"
category: "agent-sdk"
maker: "sagentic-ai"
license: "Business Source License 1.1"
url: "https://github.com/bazed-ai/bazed-af"
source_code_url: "https://github.com/bazed-ai/bazed-af"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2023-12-31"
current_release: "2026-06-09"
stars: "78"
language: "TypeScript"
homepage: "https://sagentic.ai"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI"
pricing: "open-source"
install_method: "npx @sagentic-ai/sagentic-af init my-project"
docs_url: "https://sagentic.ai/introduction.html"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Sagentic.ai Agent Framework, a unified platform for building, running, and scaling autonomous agents. Features a dev server with hot reloading and spawning agents locally via an HTTP /spawn endpoint. Not specifically a coding agent harness; it's a general autonomous agent framework."
---

Bazed, now the Sagentic.ai Agent Framework (the bazed-ai/bazed-af repo redirects to sagentic-ai/sagentic-af), is a platform for building and running autonomous agents as services. A scaffold command creates a project, a dev server with hot reloading lets agents be edited and re-run locally, and agents are spawned through a POST /spawn HTTP endpoint with a JSON payload, so the framework treats agents as addressable services rather than interactive chat sessions. It is TypeScript-based with typedoc, jest, and pnpm workspaces, installed via npx @sagentic-ai/sagentic-af init, and documented at sagentic.ai. Licensing is Business Source License 1.1 (not OSI open source) under Ahyve AI Inc. Activity is low and the project appears dormant, with modest stars and no releases. It fits the census as 'other': agent infrastructure rather than a coding harness.
