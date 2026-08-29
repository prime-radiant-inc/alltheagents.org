---
name: "cuga-agent"
slug: "cuga-agent"
layout: "agent.njk"
category: "agent"
maker: "cuga-project"
license: "Apache-2.0"
url: "https://github.com/cuga-project/cuga-agent"
source_code_url: "https://github.com/cuga-project/cuga-agent"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-09-11"
current_release: "2026-08-19"
stars: "868"
language: "Python"
homepage: "https://cuga.dev"
mcp_support: "yes — full MCP support; wire MCP servers via mcp_servers.yaml; CUGA can also act as an MCP server itself (CUGA-as-MCP)"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes — CugaSupervisor orchestrates multiple agents; delegates tasks to specialized sub-agents; mixes local CugaAgent instances with remote A2A agents"
hooks: "yes — human-in-the-loop (HITL) approval gates at critical decision points; Tool Approval policy requiring human approval before tool execution"
plan_mode: "yes — planner-executor pattern with structured planning and task decomposition; Playbook policies provide step-by-step workflow guidance"
model_providers: "OpenAI, IBM WatsonX, Azure OpenAI, Groq, OpenRouter, LiteLLM"
pricing: "open-source"
install_method: "pip"
docs_url: "https://docs.cuga.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "\"Open-source generalist agent harness ranked"
---

CUGA, developed at IBM Research, targets enterprises that need agents to operate web applications and APIs under policy constraints rather than a developer's local code editor. Its architecture composes tools from OpenAPI specs, MCP servers, and LangChain integrations, layers a five-type policy system and human-in-the-loop approval gates over execution, and can delegate to specialized sub-agents through a supervisor that mixes local and remote A2A agents. The project's benchmark record (top of AppWorld from July 2025 and WebArena from February 2025) anchors its credibility, and deployment paths range from a local uv-managed install to Docker and Helm charts on Kubernetes. Users are enterprise automation teams, with models provisioned through OpenAI-compatible endpoints, watsonx, and other providers.
