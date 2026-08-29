---
name: "AgentFlow"
slug: "agentflow"
layout: "agent.njk"
category: "agent"
maker: "lupantech"
license: "MIT"
url: "https://github.com/lupantech/AgentFlow"
source_code_url: "https://github.com/lupantech/AgentFlow"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2025-09-27"
current_release: "2026-02-08"
stars: "2006"
language: "Python"
homepage: "https://agentflow.stanford.edu"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI, DashScope (Qwen), Gemini, DeepSeek, Together AI, vLLM (local)"
pricing: "open-source"
install_method: "pip"
docs_url: "https://agentflow.stanford.edu"
plugin_docs_url: null
config_docs_url: "https://github.com/lupantech/AgentFlow/blob/main/train/config.yaml"
download_url: "https://github.com/lupantech/AgentFlow"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "A trainable multi-agent framework with four specialized modules (Planner, Executor, Verifier, Generator) coordinated through in-the-flow online optimization via the Flow-GRPO algorithm. A 7B backbone model outperforms GPT-4o on 10 benchmarks. Accepted at ICLR 2026."
---

AgentFlow approaches agentic systems as trainable rather than hand-prompted: four modules (Planner, Executor, Verifier, Generator) share an evolving memory and coordinate through tool calls — python execution, web and Wikipedia search — while the Flow-GRPO algorithm optimizes the planner online against sparse long-horizon rewards. The published results show a 7B backbone outperforming GPT-4o on 10 benchmarks spanning search, agentic, math, and science tasks, with gains of roughly 14-15% on the agentic suites. Models come from OpenAI, Google, DashScope, DeepSeek, Together, or local vLLM, and training configuration lives in train/config.yaml. Researchers in agentic RL and tool use are the users, and the paper was accepted at ICLR 2026.
