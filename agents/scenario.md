---
name: "scenario"
slug: "scenario"
layout: "agent.njk"
category: "other"
maker: "langwatch"
license: "Apache-2.0"
url: "https://github.com/langwatch/scenario"
source_code_url: "https://github.com/langwatch/scenario"
source_available: "True"
platforms: []
first_released: "2025-04-04"
current_release: "2026-08-19"
stars: "952"
language: "Python, TypeScript"
homepage: "https://scenario.langwatch.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, LiteLLM, Vercel AI SDK, ElevenLabs, Gemini"
pricing: "open-source"
install_method: "pip"
docs_url: "https://scenario.langwatch.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Simulation-based agent testing framework that tests real agent behavior by simulating users in different scenarios; first-class voice agent support, built-in red teaming with crescendo escalation, cross-language (Python/TypeScript)."
---

Agent failures are conversational and stateful — a chatbot that handles turn three wrong, a voice agent that crumbles under background noise — which example-based unit tests miss; Scenario addresses that by simulating users and judging real transcripts. The SDK exposes a script DSL where engineers hardcode or generate messages, assert on tool calls and state, and mix in external evals, with a debug mode that steps through conversations in slow motion. It integrates with pytest and vitest for CI, caches runs for repeatability, and works framework-agnostic against any agent exposing a single call method. Python, TypeScript, and Go SDKs ship under Apache-2.0, with LangWatch visualization optional. It is used by teams building conversational and voice agents who need regression confidence beyond static benchmarks.
