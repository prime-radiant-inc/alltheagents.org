---
name: "great_cto"
slug: "great-cto"
layout: "agent.njk"
category: "multiplexer"
maker: "avelikiy"
license: "MIT"
url: "https://github.com/avelikiy/great_cto"
source_code_url: "https://github.com/avelikiy/great_cto"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-04-05"
current_release: "2026-08-19"
stars: "78"
language: "JavaScript"
homepage: "https://greatcto.systems"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "yes"
plan_mode: "yes"
model_providers: "Claude (Anthropic), OpenAI Codex"
pricing: "open-source"
install_method: "npx great-cto init"
docs_url: "https://github.com/avelikiy/great_cto/blob/main/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/great-cto"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Orchestration layer that sits on top of coding agents (Claude Code, OpenAI Codex) to automate the full software development lifecycle using a pipeline of 69 specialist agents (architect, senior-dev, code-reviewer, QA, security, devops, etc.). User intervenes only at two approval gates: design and deploy. Ships as a Claude Code plugin (.claude-plugin), includes an mcp-servers directory, 60 known product archetypes across 15 industries, 6 reusable pipelines, per-agent cost tracking, DORA metrics, and a local board UI at localhost:3141."
---

great_cto turns a single developer's coding agent into an assembly line for whole products. Installed as a plugin, it drives Claude Code or OpenAI Codex through a fixed sequence — architecture, data model, backend, frontend, tests, deployment — with 69 specialist agents whose scopes are enforced at write time so a stage's agent cannot modify files outside its brief. Each stage hands its output to a second model for verification, which returns a verified, rework, or unverifiable verdict before downstream work proceeds. A self-updating board on localhost:3141 shows pipeline state, pending gates, and per-session cost, and three human approval gates (product, plan, deploy) are configurable from product-only through fully automatic, with compliance gates never skipped. The developer stays in the loop at gates while the pipeline runs, and the project publishes cost benchmarks alongside its releases.
