---
name: "LangGraph"
slug: "langgraph"
layout: "agent.njk"
category: "agent-sdk"
maker: null
license: null
url: "https://langchain-ai.github.io/langgraph/"
source_code_url: null
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: null
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "pip install -U langgraph  (or uv add langgraph)"
docs_url: "https://docs.langchain.com/oss/python/langgraph/overview"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "vinkius"
what_makes_it_special: "Low-level orchestration framework and runtime for long-running, stateful agents; combines deterministic and agentic steps in one graph; durable execution, streaming, human-in-the-loop, persistence, comprehensive memory; inspired by Pregel and Apache Beam; fine-grained control focused on agent orchestration."
---

LangGraph exists because prompt-loop agents fail at production concerns: they lose state across restarts, cannot pause for human approval, and interleave poorly with deterministic logic. It represents workflows as graphs where nodes share state, cycles are first-class, and every step checkpoints to durable storage, so long-running agents survive crashes and resume exactly. Human-in-the-loop interrupts, time-travel debugging, and persistence make it the substrate teams choose when building their own coding agents rather than adopting one. Klarna, Uber, LinkedIn, Elastic, Replit, and Cloudflare have publicly described using it, primarily from Python with a JavaScript port alongside.
