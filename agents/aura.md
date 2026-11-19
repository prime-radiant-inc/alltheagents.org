---
name: "AURA"
slug: "aura"
layout: "agent.njk"
category: "agent"
maker: "mezmo"
license: "Apache-2.0"
url: "https://github.com/mezmo/aura"
source_code_url: "https://github.com/mezmo/aura"
source_available: "True"
homepage: "https://www.mezmo.com/aura"
docs_url: "https://docs.mezmo.com/aura"
download_url: null
install_method: "curl -fsSL https://raw.githubusercontent.com/mezmo/aura/main/scripts/install.sh | bash (Linux/macOS, verifies checksums); docker run mezmo/aura; Helm chart for Kubernetes; embed the Rust core as a library"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "devops"
language: "Rust"
first_released: "2026-03-02"
current_release: "2026-10-30"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://docs.mezmo.com/aura/configuration-reference"
model_providers: "OpenAI, Anthropic, AWS Bedrock, Google Gemini, Ollama, OpenRouter"
pricing: "free"
stars: "414"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A production-tested SRE agent platform that began as Mezmo's internal operations harness: teams of specialist agents investigate production incidents across observability and infrastructure tools, the whole agent system is defined in reviewable TOML, sensitive actions wait for human approval, and it runs self-hosted or air-gapped with OpenTelemetry traces on every decision."
---

AURA started life as the internal harness Mezmo built to run its own SaaS, and is now the Apache-2.0 core of their operations story: a Rust agent runtime you can install on Linux or macOS in minutes and point at your own stack. The whole agent system lives in reviewable TOML — models, specialist agent teams, per-agent prompts, tools, approval policies and guardrails — so an SRE team can version its incident-response setup like code. In action, a preconfigured team of agents investigates incidents by correlating the tools you already run: PagerDuty, Datadog, Prometheus, Kubernetes, Argo CD, AWS, and more, reached through built-in integrations and MCP servers over Streamable HTTP, SSE or STDIO, with Qdrant or Bedrock knowledge bases grounding runbook lookups. Guardrails are the design center: sensitive tool calls wait for explicit human approval (webhook or in-conversation, failing closed on timeout or transport error), oversized tool results park on disk for selective retrieval, and every model, tool and orchestration decision exports as OpenTelemetry spans. It runs interactively as a terminal chat assistant, as a daemon wired to monitoring systems, as the mezmo/aura container or a Helm-charted Kubernetes workload, or embedded as a Rust library — and it serves agents through an OpenAI-compatible API, so existing chat clients work unchanged. Mezmo's engineering and SRE teams still run it in production, teams outside Mezmo run it in their own environments, and it powers thousands of agent sessions a month inside Mezmo's hosted observability platform; the self-hosted project itself carries no paid tier.
