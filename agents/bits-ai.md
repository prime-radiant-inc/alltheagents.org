---
name: "Bits AI"
slug: "bits-ai"
layout: "agent.njk"
category: "agent"
maker: "Datadog"
license: "Proprietary"
url: "https://www.datadoghq.com"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: "https://www.datadoghq.com/product/ai/bits-code/"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "subscription"
install_method: "web (embedded in the Datadog platform; 14-day trial)"
docs_url: "https://docs.datadoghq.com/bits_ai/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Datadog's AI agents for incident investigation and dev fixes"
---

Bits AI is Datadog's umbrella for embedded AI agents across investigation, remediation, security, data analysis, and code. The coding component, Bits Code, exists because errors surface first in Datadog's observability data and someone still has to translate them into fixes: the agent triages the signal, locates the offending code using logs, traces, metrics, and runtime variables, writes a fix with unit tests, and opens a GitHub PR carrying the full investigative context. Engineers iterate by leaving PR comments, which the agent answers with updated code, and scheduled prompts or rule-based triggers can automate remediation across Error Tracking, Test Optimization, APM recommendations, and profiling insights. Enterprise controls include zero-retention agreements with model providers and RBAC. It is used by teams already running Datadog who want error triage to end in a reviewable pull request rather than a dashboard alert.
