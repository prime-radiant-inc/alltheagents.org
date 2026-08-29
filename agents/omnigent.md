---
name: "Omnigent"
slug: "omnigent"
layout: "agent.njk"
category: "multiplexer"
maker: "omnigent-ai"
license: "Apache-2.0"
url: "https://github.com/omnigent-ai/omnigent"
source_code_url: "https://github.com/omnigent-ai/omnigent"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-06-11"
current_release: "2026-08-20"
stars: "9065"
language: "Python"
homepage: "https://omnigent.ai"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, OpenRouter, LiteLLM, Ollama, vLLM, Azure, Databricks, Amazon Bedrock, Google Vertex AI"
pricing: "open-source"
install_method: "pip"
docs_url: "https://omnigent.ai"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Open-source meta-harness providing harness-agnostic orchestration over multiple AI coding agents (Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, custom agents). Mix agents from different vendors in the same session -- ask one to review another's work. Any-device real-time sync across terminal, browser, phone, desktop app. Multi-user collaboration with shareable live sessions. Cloud sandbox execution (Modal, E2B, Daytona, Kubernetes, Databricks). Stackable policy/governance system at server, agent, and session levels. Agent-as-YAML: define custom agents with prompts, Python functions, MCP servers, and sub-agents in a short YAML file. Alpha stage."
---

Omnigent provides a uniform orchestration layer over existing coding agents, letting one session supervise a Claude Code instance while an OpenCode agent reviews its output. Harnesses swap without rewriting work, and custom agents are declared in YAML with tools of type mcp, type agent, or plain Python functions. Policies stack at server, agent, or session level for approve-before-shell, tool-call caps, and spend budgets, with OS-level sandboxing via bwrap or seatbelt. Sessions sync across terminal, browser, and phone, with cloud sandboxes on Modal, E2B, Kubernetes, and others. Credentials can be API keys, coding-plan subscriptions, or gateway base URLs, switchable mid-session. The project is in alpha with a large contributor base and permissive Apache-2.0 licensing.
