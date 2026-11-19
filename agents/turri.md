---
name: "turri"
slug: "turri"
layout: "agent.njk"
category: "agent"
maker: "turri-oss"
license: "MIT"
url: "https://github.com/turri-oss/turri"
source_code_url: "https://github.com/turri-oss/turri"
source_available: "True"
homepage: "https://turri.dev"
docs_url: "https://github.com/turri-oss/turri/blob/main/docs/README.md"
download_url: null
install_method: "npm install -g @turri-dev/cli, then turri doctor"
platforms:
  - "CLI"
  - "Desktop"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-09-22"
current_release: "2026-11-15"
maintained: "active"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://github.com/turri-oss/turri/blob/main/docs/config.md"
model_providers: "any provider pi supports (Anthropic, OpenAI, Google, Amazon Bedrock, OpenRouter, local), plus subscription logins via pi extensions"
pricing: "BYOK"
stars: "48"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "You maintain the system's definition — specs, tests and ADRs written in ***plain — and turri regenerates the affected code from it as intent evolves, verifying each generation against conformance tests the coding agent cannot change."
---

turri is an open-source coding agent built by Žan Jonke, who writes at codeplain, the company behind the ***plain specification language. His motivation was that agents ship features fast but leave you accountable for code you no longer understand: turri's answer is regenerative software, where the durable artifact is a structured system definition (functional specs, architecture decisions and tests in ***plain) and the code itself is disposable. You describe what you want, turri captures it as a reviewable definition, generates the code, and verifies the result against independently defined conformance tests — when requirements change, it regenerates the affected parts rather than stacking patch on patch, and drift/lineage commands report how far the code has moved from its definition and every generation of a module. It runs as an npm CLI or a desktop app, is built on the pi coding agent as a pinned dependency with turri's own tools, skills and gates layered on top, and uses three models: a capable harness model for defining and planning, and smaller coding and judge models for building and conformance runs. It supports headless regeneration overnight or in CI, a sandboxed execution layer, and a gated skill system that enforces review steps in code rather than prompts. It suits developers who want to engineer the definition of their system and let the harness keep the implementation honest.
