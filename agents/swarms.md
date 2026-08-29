---
name: "Swarms"
slug: "swarms"
layout: "agent.njk"
category: "agent-sdk"
maker: "kyegomez"
license: "Apache-2.0"
url: "https://github.com/kyegomez/swarms/"
source_code_url: "https://github.com/kyegomez/swarms"
source_available: "True"
platforms:
  - "Web"
first_released: "2023-05-11"
current_release: "2026-08-19"
stars: "7069"
language: "Python"
homepage: "https://docs.swarms.world"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Groq"
pricing: "open-source"
install_method: "pip"
docs_url: "https://docs.swarms.world"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/swarms/"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Enterprise-grade multi-agent orchestration framework with 60+ prebuilt multi-agent architectures (sequential, concurrent, hierarchical). AutoSwarmBuilder auto-generates specialized agents, SwarmRouter is a universal orchestrator, x402 payment protocol support, Agent Orchestration Protocol for distributed deployment. Backwards-compatible with LangChain/AutoGen/CrewAI and MCP-enabled via mcp_url/mcp_urls."
---

Swarms packages multi-agent orchestration as a pip-installable Python framework aimed at production deployments rather than notebooks. Individual Agents bind a model, system prompt, and tool set — including tools discovered from MCP servers — and prebuilt workflow classes such as SequentialWorkflow, ConcurrentWorkflow, GraphWorkflow, MixtureOfAgents, and HierarchicalSwarm route work between them, with a director-style planning pattern in HierarchicalSwarm and a universal SwarmRouter that selects an architecture per task. AutoSwarmBuilder generates an entire team spec from a job description, GraphWorkflow nodes accept completion callbacks for streaming and progress tracking, and backward-compatibility layers accept agents written for LangChain, AutoGen, or CrewAI. The Swarms Marketplace lets teams publish and reuse agents and prompts, and x402 payment protocol support enables per-use monetization of deployed agents. Engineering teams building multi-agent pipelines in Python are the primary users.
