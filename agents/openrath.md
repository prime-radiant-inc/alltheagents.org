---
name: "OpenRath"
slug: "openrath"
layout: "agent.njk"
category: "agent"
maker: "Rath-Team"
license: "BSD-3-Clause"
url: "https://github.com/Rath-Team/OpenRath"
source_code_url: "https://github.com/Rath-Team/OpenRath"
source_available: True
platforms: []
first_released: "2026-05-04"
current_release: "2026-07-31"
stars: "930"
language: "Python"
homepage: "https://www.openrath.com/"
mcp_support: "yes — stdio MCP tools adapted into the loop as FlowToolCall instances"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes — multi-agent collaboration; agents share session state; sessions can be forked/merged across agents with lineage tracking"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic (OpenAI-compatible providers)"
pricing: "open-source"
install_method: "pip"
docs_url: "https://docs.openrath.com"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "PyTorch-like runtime for dynamic multi-agent and multi-session workflows — Session as the central flowing value (like a Tensor); composable agents like nn.Linear; durable execution with checkpointing, leases, effect ledgers, and human-in-the-loop interrupts."
---

PyTorch-like runtime for dynamic multi-agent and multi-session workflows — Session as the central flowing value (like a Tensor); composable agents like nn.Linear; durable execution with checkpointing, leases, effect ledgers, and human-in-the-loop interrupts.
