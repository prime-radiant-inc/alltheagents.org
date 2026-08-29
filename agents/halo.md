---
name: "HALO"
slug: "halo"
layout: "agent.njk"
category: "other"
maker: "context-labs"
license: "MIT"
url: "https://github.com/context-labs/HALO"
source_code_url: "https://github.com/context-labs/HALO"
source_available: "True"
platforms: []
first_released: "2026-04-21"
current_release: "2026-08-19"
stars: "1151"
language: "Python, TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI-compatible (OpenAI, OpenRouter, any OpenAI-compatible base URL)"
pricing: "open-source"
install_method: "binary, pip"
docs_url: "https://docs.inference.net"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Uses specialized Recursive Language Models (RLMs) instead of general-purpose LLMs to analyze production agent execution traces and identify systemic failure modes. Creates a recursively self-improving loop: collect traces, analyze, fix harness, redeploy, repeat. Feeds reports into coding agents (Cursor, Claude Code) to iteratively improve the harness. Demonstrated +10-16 point improvements on AppWorld benchmarks purely through harness optimization."
---

HALO addresses the problem that agent harnesses accumulate fixable flaws — hallucinated tool calls, redundant arguments, refusal loops — that general-purpose coding agents fail to diagnose when handed raw execution traces, because traces are long and the agent fixates on single-run errors. HALO instead feeds OpenTelemetry-compatible traces into a Recursive Language Model engine tuned for trace decomposition, which identifies systemic failure modes and emits a findings report; a separate coding agent (Cursor, Claude Code) then applies the recommended harness edits, and the cycle repeats on fresh traces. The approach treats harness improvement as a measurable loop: on AppWorld, optimizing only the harness raised Gemini 3 Flash from 36.8% to 52.6% and Sonnet 4.6 from 73.7% to 89.5% dev SGC, with held-out verification against overfitting. It ships as a pip package and desktop app aimed at teams operating production agents at scale.
