---
name: "Aip-Identity"
slug: "aip-identity"
layout: "agent.njk"
category: "other"
maker: "The-Nexus-Guard"
license: "MIT"
url: "https://github.com/the-nexus-guard/aip"
source_code_url: "https://github.com/the-nexus-guard/aip"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Web"
first_released: "2026-02-01"
current_release: "2026-03-22"
stars: "15"
language: "Python"
homepage: "https://the-nexus-guard.github.io/aip/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: null
install_method: "pip install aip-identity (or clone and pip install -e .)"
docs_url: "https://aip-service.fly.dev/docs"
plugin_docs_url: null
config_docs_url: "https://the-nexus-guard.github.io/aip/"
download_url: "https://pypi.org/project/aip-identity/"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Agent Identity Protocol (AIP) — decentralized cryptographic identity (Ed25519 keypairs), verifiable trust chains (vouching), and E2E encrypted messaging for AI agents. Enables secure, verifiable agent-to-agent communication without a central authority. Integrates with MCP to sign MCP requests and fill the 'agent identity gap.'"
---

Multi-agent systems lack a way to prove who an agent is or whether to trust its output; AIP addresses this with three layers: cryptographic identity (Ed25519 keypairs, did:aip DIDs, challenge-response verification), trust chains built from signed vouches with scopes and decaying trust scores, and relay-based E2E encrypted messaging where the relay only ever sees ciphertext. A Python SDK (pip install aip-identity), CLI, MCP server, GitHub Action for trust-gated deployments, and integrations with LangChain, CrewAI, AutoGen, and A2A make it consumable from existing frameworks. It is MIT-licensed, actively versioned (v0.5.46, 325 commits), and early — 15 stars — with vouch lookup and messaging still depending on a hosted Fly.io relay.
