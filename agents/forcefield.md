---
name: "Forcefield"
slug: "forcefield"
layout: "agent.njk"
category: "agent"
maker: "fabledruns"
license: "Apache-2.0"
url: "https://github.com/fabledruns/forcefield"
source_code_url: "https://github.com/fabledruns/forcefield"
source_available: "True"
homepage: null
docs_url: "https://github.com/fabledruns/forcefield/blob/main/docs/Index.md"
download_url: "https://github.com/fabledruns/forcefield/releases"
install_method: "curl -fsSL https://raw.githubusercontent.com/fabledruns/forcefield/main/scripts/install.sh | sh (macOS/Linux); irm https://raw.githubusercontent.com/fabledruns/forcefield/main/scripts/install.ps1 | iex (Windows); or go build from source (single static binary, CGO_ENABLED=0)"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Go"
first_released: "2026-07-24"
current_release: "2026-11-14"
maintained: "active"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "False"
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://github.com/fabledruns/forcefield/blob/main/docs/Config.md"
model_providers: "Ollama, LM Studio, llama.cpp, AMD Lemonade (local); Anthropic, OpenAI, Google Gemini, Google Vertex AI, AWS Bedrock, Azure AI, NVIDIA NIM, Groq, Mistral, Together, OpenRouter, OpenCode (cloud)"
pricing: "BYOK"
stars: "8"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A local-first runtime that ships as one static Go binary with zero accounts, cloud, or telemetry, and treats runtime invariants as architecture: atomic fsync-renamed session writes, three-state permission gating evaluated before any host action, credential redaction in tool arguments and outputs, and bounded subagent delegation with hard depth/concurrency caps."
---

Forcefield is a single-binary Go runtime that owns the whole multi-turn agent loop — the model streams single turns while the runtime validates permissions, dispatches tools, and hands results back — aimed at developers who want a local-first harness with no accounts and no telemetry, configurable against local inference engines or a dozen-plus cloud providers. Sessions persist project-locally through temp-file, fsync, and atomic rename so an interrupted turn recovers cleanly, shell execution runs natively or inside a pinned WSL distribution on Windows, and a catalog of Markdown skills loads on demand to keep the base prompt small. Seven built-in agent personas (coding, cyber, research, legal, docs, devops, general) filter the tool set per profile, and an optional orchestration mode exposes a delegate tool for bounded child agents. It is an Apache-2.0 project of superprime, under active development, with an unusually deep docs tree that documents its own adversarial testing and audit record.
