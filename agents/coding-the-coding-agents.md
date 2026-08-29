---
name: "coding-the-coding-agents"
slug: "coding-the-coding-agents"
layout: "agent.njk"
category: "other"
maker: "zencoderai"
license: null
url: "https://github.com/zencoderai/coding-the-coding-agents"
source_code_url: "https://github.com/zencoderai/coding-the-coding-agents"
source_available: "True"
platforms: []
first_released: "2025-03-10"
current_release: "2026-05-08"
stars: "94"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: "Poetry (pyproject.toml + poetry.lock)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/zencoderai/coding-the-coding-agents"
maintained: "dormant"
sources:
  - "github_topic3"
what_makes_it_special: "Educational repository with progressive AI agent code examples for a talk: basic agent, multi-agent, agent-to-agent (a2a) communication, and agent with MCP integration (agent_w_mcp). Not a production harness."
---

Engineers learning to build coding agents usually face production codebases too large to learn from, so Zencoder released the companion code for its talk on building coding agents as a graded series. Five Python examples implement the same problem at increasing sophistication: a baseline, a basic agent loop, an agent integrated with the Model Context Protocol, a multi-agent setup, and an agent-to-agent configuration using the A2A protocol. Each stage isolates one architectural concept so a reader can diff successive stages and see precisely what a multi-agent layer or MCP integration adds. Poetry manages the Python project, and the repository carries no license file, so reuse terms are unstated. Developers studying agent construction use it as reference material rather than as a tool.
