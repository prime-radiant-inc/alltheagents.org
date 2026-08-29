---
name: "HCS (Hashgraph Consensus Service)"
slug: "hcs-hashgraph-consensus-service"
layout: "agent.njk"
category: "other"
maker: null
license: "Apache-2.0"
url: "https://hol.org"
source_code_url: null
source_available: "True"
platforms:
  - "IDE"
first_released: null
current_release: null
stars: null
language: "TypeScript, Python"
homepage: "https://hol.org"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "none"
pricing: "free"
install_method: "npm install @hashgraphonline/standards-sdk; also available on PyPI (4 packages) and npm (10 packages)"
docs_url: "https://docs.hol.org"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Open standards (HCS-1 through HCS-28) for AI-agent infrastructure on Hedera's Hashgraph Consensus Service; neutral coordination layer covering registries, identity, payments, privacy/security, and inter-agent communication; 30+ founding partners; includes live Registry Broker and MCP plugins for Claude, Codex, Cursor."
---

Hashgraph Online maintains the Hiero Consensus Standards (HCS-1 through HCS-28), a suite of open specifications for AI-agent infrastructure built on the Hedera network under the Linux Foundation's Decentralized Trust umbrella. The standards cover the pieces an agent ecosystem needs beyond the model: on-chain file storage and registries (HCS-1/2/3), identity profiles and Universal Agent IDs (HCS-11/14), agent-to-agent communication (HCS-10), trust scores, privacy compliance, transparency logging, and agentic payment flows. Alongside the specifications, the ecosystem ships SDKs for TypeScript and Python, a Registry Broker that indexes agents across protocols such as A2A, MCP, and ERC-8004, and developer surfaces including registry skills for coding assistants and a Codex plugin. Its audience is developers building agent infrastructure — identity, payments, discovery — rather than coding harnesses themselves.
