---
name: "Chaterm"
slug: "chaterm"
layout: "agent.njk"
category: "agent"
maker: "chaterm"
license: "NOASSERTION"
url: "https://github.com/chaterm/Chaterm"
source_code_url: "https://github.com/chaterm/Chaterm"
source_available: "Yes"
platforms:
  - "CLI"
  - "Web"
first_released: "2025-04-14"
current_release: "2026-08-20"
stars: "3017"
language: "TypeScript"
homepage: "https://chaterm.ai"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Alibaba, Google"
pricing: "open-source"
install_method: "npm"
docs_url: "https://chaterm.ai/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://chaterm.ai/download"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Open-source AI-native terminal for cloud and infrastructure management that uses natural language to deploy services, troubleshoot, and automate operations across servers and Kubernetes, with a knowledge base and agent skills."
---

Chaterm is an AI-native terminal built for infrastructure work: engineers describe a task in natural language and the agent plans and executes it across servers and Kubernetes clusters, handling deployment, troubleshooting, and rollback with an auditable trail rather than raw shell commands. Under the hood it combines an agent layer adapted from Cline with a knowledge-base subsystem that ingests technical manuals and internal documentation, retrievable through hybrid vector-plus-keyword search with RRF fusion; a plugin system handles authentication across cloud providers and Kubernetes clusters. It also carries a database workspace for common SQL databases, cross-device session sync, and voice input, positioning itself as an operations console rather than a developer IDE. SRE and infrastructure teams use it to reduce the gap between natural-language intent and multi-host execution, and the project carries OpenSSF Best Practices certification and a CNCF Landscape listing alongside roughly 3,000 stars.
