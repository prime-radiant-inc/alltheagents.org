---
name: "paper"
slug: "paper"
layout: "agent.njk"
category: "agent"
maker: null
license: "MIT"
url: "https://huggingface.co/papers/2510.05592"
source_code_url: null
source_available: "Yes"
platforms:
  - "Web"
first_released: null
current_release: null
stars: null
language: "Python"
homepage: "https://agentflow.stanford.edu/"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "yes"
hooks: null
plan_mode: "yes"
model_providers: "OpenAI, DashScope (Qwen-2.5), Gemini, Deepseek, Together, vLLM"
pricing: "open-source"
install_method: "bash setup.sh && source .venv/bin/activate"
docs_url: "https://agentflow.stanford.edu/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/lupantech/AgentFlow"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "A trainable agentic framework with 'in-the-flow' optimization using Flow-GRPO RL algorithm that optimizes the planner agent live inside the multi-turn interaction loop. Decomposes work across four specialized modules (Planner, Executor, Verifier, Generator). A 7B-scale backbone model (Qwen-2.5-7B-Instruct) surpasses GPT-4o (~200B) on several benchmarks. Accepted to ICLR 2026."
---

AgentFlow came out of Stanford to attack credit assignment in long-horizon agent runs, where a frozen LLM loops on failed tool calls and never learns from the outcome. The system splits work across a planner, an executor, a verifier, and a generator coordinated through shared memory, and trains only the planner by converting each multi-turn trajectory into single-turn policy updates with group-normalized advantages. After training, an agent that once repeated the same failed tool call instead self-corrects and changes strategy. The framework targets researchers studying trainable agentic systems, with code, project page, and a demo space available.
