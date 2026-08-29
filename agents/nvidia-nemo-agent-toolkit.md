---
name: "NVIDIA NeMo Agent Toolkit"
slug: "nvidia-nemo-agent-toolkit"
layout: "agent.njk"
category: "agent-sdk"
maker: "NVIDIA"
license: "Apache-2.0"
url: "https://developer.nvidia.com/nemo-agent-toolkit"
source_code_url: "https://github.com/NVIDIA/NeMo"
source_available: "True"
platforms:
  - "CLI"
  - "Library"
first_released: "2024"
current_release: "2026"
stars: null
language: "Python"
homepage: "https://developer.nvidia.com/nemo-agent-toolkit"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "NVIDIA NIMs (build.nvidia.com)"
pricing: "Free / open source (Apache-2.0)"
install_method: "pip install nvidia-nat (PyPI); optional extras e.g. pip install 'nvidia-nat[langchain]'"
docs_url: "https://docs.nvidia.com/nemo/agent-toolkit/latest/"
plugin_docs_url: "https://docs.nvidia.com/nemo/agent-toolkit/latest/extend-modules.html"
config_docs_url: "https://docs.nvidia.com/nemo/agent-toolkit/latest/workflows/build.html"
download_url: "https://pypi.org/project/nvidia-nat/"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Open-source library for connecting and optimizing teams of AI agents across any framework. Supports MCP as both client and server (FastMCP), a public Plugin API, distributed agent teams via Agent-to-Agent (A2A) Protocol with authentication, and runtime telemetry hooks. Enterprise-grade instrumentation, observability, and continuous learning."
---

NeMo Agent Toolkit connects teams of AI agents to data sources and tools without requiring replatforming onto NVIDIA's stack, wrapping existing frameworks rather than replacing them. Workflows are declared in a YAML file with pre-built agent types (ReAct, ReWOO, reasoning, router, parallel/sequential executors) and run via the nat CLI. Evaluation and profiling are first-class: workflow-level tracing down to individual tools with token and timing attribution, optimizers, and trajectory formats for evaluation runs. A public plugin API covers custom LLM providers, retrievers, evaluators, memory providers, and telemetry exporters, shareable as packages. The A2A protocol support allows distributed agent teams, and observability integrates with LangSmith, Phoenix, Langfuse, and OpenTelemetry.
