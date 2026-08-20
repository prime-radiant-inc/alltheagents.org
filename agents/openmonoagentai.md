---
name: "OpenMonoAgent.ai"
slug: "openmonoagentai"
layout: "agent.njk"
category: "agent"
maker: "StartupHakk"
license: "AGPL-3.0"
url: "https://github.com/StartupHakk/OpenMonoAgent.ai"
source_code_url: "https://github.com/StartupHakk/OpenMonoAgent.ai"
source_available: True
platforms:
  - "CLI"
first_released: "2026-04-30"
current_release: "2026-08-20"
stars: "1775"
language: "C# / .NET 10"
homepage: null
mcp_support: "yes - stdio; auto-detects code-review-graph MCP server, configurable in settings.json"
plugin_support: "yes - Playbooks (YAML workflows)"
claude_code_plugin: "no"
subagents: "yes - 5 specialist sub-agents (Explore, Plan, Coder, Verify, general-purpose)"
hooks: "yes - pre/post hooks in 12-step tool pipeline"
plan_mode: "yes - plan-mode guard + dedicated Plan sub-agent"
model_providers: "Local llama.cpp (default), OpenAI (WIP), Anthropic (WIP), Ollama (WIP)"
pricing: "open-source"
install_method: "binary - one-command curl install script"
docs_url: "https://github.com/StartupHakk/OpenMonoAgent.ai/blob/main/docs/SETUP.md"
plugin_docs_url: "https://github.com/StartupHakk/OpenMonoAgent.ai/blob/main/docs/PLAYBOOKS.md"
config_docs_url: "https://github.com/StartupHakk/OpenMonoAgent.ai/blob/main/docs/CONFIG.md"
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "100% local-first coding agent bundled with llama.cpp in Docker; zero per-token cost, zero data egress. Auto-detects hardware (NVIDIA/CPU/Apple Silicon), supports distributed inference (agent on laptop, inference on remote GPU box), 20 built-in tools with 12-step pipeline, Docker sandboxing, Roslyn + LSP deep code intelligence, self-hosted SearXNG private web search, vision support, and a VS Code/Cursor extension. Philosophy: 'AI as infrastructure you own, not a subscription you rent.'"
---

100% local-first coding agent bundled with llama.cpp in Docker; zero per-token cost, zero data egress. Auto-detects hardware (NVIDIA/CPU/Apple Silicon), supports distributed inference (agent on laptop, inference on remote GPU box), 20 built-in tools with 12-step pipeline, Docker sandboxing, Roslyn + LSP deep code intelligence, self-hosted SearXNG private web search, vision support, and a VS Code/Cursor extension. Philosophy: 'AI as infrastructure you own, not a subscription you rent.'
