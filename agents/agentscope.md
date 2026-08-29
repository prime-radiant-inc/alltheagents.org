---
name: "AgentScope"
slug: "agentscope"
layout: "agent.njk"
category: "agent-sdk"
maker: "agentscope-ai"
license: "Apache-2.0"
url: "https://github.com/modelscope/agentscope"
source_code_url: "https://github.com/modelscope/agentscope"
source_available: "Yes"
platforms: []
first_released: "2024-01-12"
current_release: "2026-08-19"
stars: "29062"
language: "Python"
homepage: "https://docs.agentscope.io/"
mcp_support: "yes (MCP servers, GitHub MCP Registry & ClawHub)"
plugin_support: "yes (Skills, MCP servers, Python Toolkit, Hub system)"
claude_code_plugin: "no"
subagents: "yes (Agent Team leader-worker orchestration)"
hooks: "yes (composable middleware hooks across the loop)"
plan_mode: "yes (Task/plan tools)"
model_providers: "OpenAI, Anthropic, Google (Gemini), DashScope, DeepSeek, Moonshot, xAI, Ollama"
pricing: "open-source"
install_method: "pip (uv pip install agentscope)"
docs_url: "https://docs.agentscope.io/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/agentscope/"
maintained: "active"
sources:
  - "jim"
  - "caramaschi"
what_makes_it_special: "A model-centric (not framework-centric) agent service designed for increasingly agentic LLMs, shipping a full FastAPI backend + Web UI with multi-tenancy, leader-worker agent teams, 8 sandbox backends, and fine-grained permission control out of the box."
---

Most agent frameworks stop at an SDK and leave serving, sandboxing, and permissions to the application layer. AgentScope 2.0 takes a model-centric stance: because modern LLMs already reason and call tools well, the framework provides composable building blocks (ReAct agent, Toolkit with MCP servers and skills, context middleware, permission and human-in-the-loop controls, memory backends) instead of constraining orchestration. The service layer adds a FastAPI backend with a pre-built Web UI, multi-tenancy, RAG, scheduling, and channels into enterprise chat platforms, so a deployment is production-shaped from the start. Agent Teams let a leader agent spawn and coordinate workers, and isolated execution runs across Local, Docker, Apple Container, Bubblewrap, E2B, OpenSandbox, Daytona, and K8s backends. It targets developers building agent applications on Alibaba's ModelScope stack, with Apache-2.0 code, Python 3.11+ packaging on PyPI, and documentation at docs.agentscope.io.
