---
name: "Agents"
slug: "agents"
layout: "agent.njk"
category: "agent-sdk"
maker: "aiwaves-cn"
license: "Apache-2.0"
url: "https://github.com/aiwaves-cn/agents"
source_code_url: "https://github.com/aiwaves-cn/agents"
source_available: "True"
platforms:
  - "IDE"
  - "Web"
  - "Autonomous"
first_released: "2023-07-18"
current_release: "2024-09-26"
stars: "5954"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "pip"
docs_url: "https://agentsv2.readthedocs.io/"
plugin_docs_url: null
config_docs_url: null
download_url: "pip install git+https://github.com/aiwaves-cn/agents@master"
maintained: "active"
sources:
  - "e2b"
  - "jim"
what_makes_it_special: "A data-centric, self-evolving autonomous language agent framework (Agents 2.0) that applies the connectionist learning procedure to agent training. Makes an analogy where the agent pipeline is a computational graph, nodes are layers, and prompts/tools are weights — implementing back-propagation and gradient-based weight update using 'language loss', 'language gradients', and 'language weights'. Can optimize multi-agent systems by treating nodes as different agents."
---

Agent pipelines are usually hand-tuned, and the AIWaves team asked whether the training machinery of neural networks could be transplanted to prompts and tools. In Agents 2.0 the pipeline is treated as a computational graph: execution records trajectories per node, a prompt-based language loss scores outcomes, and backward propagation yields textual 'language gradients' used to rewrite each node's prompts and tools — and to add or remove nodes. Because nodes can themselves be agents, multi-agent systems are optimized as a unit. The framework is a Python library installed from source, accompanied by the arXiv paper 2406.18532. Activity has concentrated around the June 2024 Agents 2.0 release, with the codebase largely stable since.
