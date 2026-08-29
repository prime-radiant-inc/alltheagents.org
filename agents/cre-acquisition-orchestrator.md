---
name: "cre-acquisition-orchestrator"
slug: "cre-acquisition-orchestrator"
layout: "agent.njk"
category: "other"
maker: "ahacker-1"
license: "Apache-2.0"
url: "https://github.com/ahacker-1/cre-acquisition-orchestrator"
source_code_url: "https://github.com/ahacker-1/cre-acquisition-orchestrator"
source_available: "True"
platforms: []
first_released: "2026-03-16"
current_release: "2026-07-28"
stars: "104"
language: "TypeScript, React, Node.js, Python"
homepage: "https://www.theaiconsultingnetwork.com/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI Codex CLI / ChatGPT; deterministic offline simulation"
pricing: "Free / open source"
install_method: "git clone -> npm install -> npm run setup -- --skip-codex-install --skip-login -> npm run proof"
docs_url: "https://github.com/ahacker-1/cre-acquisition-orchestrator/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ahacker-1/cre-acquisition-orchestrator"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Most in-depth open-source CRE acquisition framework: 31-role AI deal team, source-backed extraction with provenance, human approval gates, local-first with optional live Codex web-search runtime, honest open evaluation harness reporting real weaknesses, deterministic Parkview demo requiring no API keys"
---

Multifamily acquisitions run on unstructured documents - rent rolls, T12s, offering memos - and CRE software has largely missed the agent wave, so this project models the entire deal lifecycle as an agent workflow. A 31-role team (six orchestrators, twenty-one acquisition specialists, four document-ingestion agents) processes uploads through document parsing (pandas, PyMuPDF, OCR) into extraction candidates that carry source provenance, and a human approval gate is required before any field becomes an underwriting input. The default runtime is live OpenAI Codex CLI with web search enabled so agents cite real market data, while a deterministic offline simulation engine backs demos and CI without credentials. A React/TypeScript dashboard, 28 JSON Schema contracts, and an eval harness over synthetic deals make the system testable. CRE analysts and AI-in-real-estate practitioners use it as a reference architecture rather than production software.
