---
name: "sre"
slug: "sre"
layout: "agent.njk"
category: "agent-sdk"
maker: "SmythOS"
license: "MIT"
url: "https://github.com/SmythOS/sre"
source_code_url: "https://github.com/SmythOS/sre"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-06-07"
current_release: "2026-04-03"
stars: "1291"
language: "TypeScript"
homepage: "https://smythos.com"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google AI, AWS Bedrock, Groq, Perplexity"
pricing: "open-source"
install_method: "npm"
docs_url: "https://smythos.github.io/sre/sdk/"
plugin_docs_url: "https://github.com/SmythOS/sre/blob/main/examples"
config_docs_url: "https://smythos.github.io/sre/core/"
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "OS-level cloud-native runtime and SDK for production AI agents ('The Linux of AI Agents'). Unified Resource Abstraction — same API works across all providers (swap providers without changing code). Built-in Candidate/ACL security system. 40+ production-ready components. Run agents via SDK or load .smyth files from visual builder."
---

SRE (Smyth Runtime Environment) targets the plumbing layer of agent development: the same TypeScript SDK calls abstract resources — storage (Local, S3, GCS, Azure), LLMs (OpenAI, Anthropic, Google AI, Bedrock, Groq, Perplexity), vector databases (Pinecone, Milvus), cache, and secrets vaults — so infrastructure can be swapped per deployment without touching agent logic. Around the kernel sit 40+ components for generation, search, scraping, API calls, and classification, a Candidate/ACL security model with credential vaults, and the ability to run agents from code or from .smyth files exported by the SmythOS visual builder. It installs via npm as an SDK or CLI and runs local, cloud, or edge. Teams building agents that must survive provider and infrastructure changes are the audience, rather than end-user coding sessions.
