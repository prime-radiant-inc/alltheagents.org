---
name: "AgentTeams"
slug: "agentteams"
layout: "agent.njk"
category: "multiplexer"
maker: "agentscope-ai"
license: "Apache-2.0"
url: "https://github.com/agentscope-ai/AgentTeams"
source_code_url: "https://github.com/agentscope-ai/AgentTeams"
source_available: "True"
platforms: []
first_released: "2026-02-21"
current_release: "2026-08-19"
stars: "5443"
language: "Multi-runtime (Node.js, Python)"
homepage: "https://www.aliyun.com/product/agentteams"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "yes"
plan_mode: "no"
model_providers: "OpenAI, DeepSeek, Qwen"
pricing: "open-source"
install_method: "docker"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Collaborative multi-agent runtime (by Alibaba/AgentScope) using a Manager-Workers architecture over self-hosted Matrix IM rooms. Zero-credential security model — Workers never see real API keys, only consumer tokens via Higress AI Gateway. Human-in-the-loop by default, Kubernetes-native CRD management, multi-runtime Workers (OpenClaw/Node, QwenPaw/Python, Hermes), 80,000+ community skills."
---

Multi-agent setups usually hide agent-to-agent traffic in black-box calls, and leaked API keys from a compromised worker are the standard failure mode. AgentTeams, from the AgentScope team, instead places a Manager agent and its Workers in self-hosted Matrix rooms alongside the human, with declarative Worker/Team/Human definitions and runtime swaps (OpenClaw, QwenPaw, Hermes) via commands like agt update worker --runtime hermes. Security rests on the Higress AI gateway holding every real credential — workers receive consumer tokens only, so a compromised worker exposes no LLM, GitHub, or MCP keys. A MinIO-backed shared filesystem reduces token spend between agents. Deployment is a one-command install script or a Helm chart bundling Higress, Tuwunel, MinIO, and the controller, with the project backed by Alibaba/Aliyun.
