---
name: "codebadger"
slug: "codebadger"
layout: "agent.njk"
category: "other"
maker: "Lekssays"
license: "GPL-3.0"
url: "https://github.com/Lekssays/codebadger"
source_code_url: "https://github.com/Lekssays/codebadger"
source_available: "True"
platforms: []
first_released: "2025-10-01"
current_release: "2026-08-03"
stars: "153"
language: "Python"
homepage: "https://dl.acm.org/doi/pdf/10.1145/3786165.3788441"
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "Free / open-source"
install_method: "Docker (Dockerfile, docker-compose.yml, Dockerfile.mcp) or Python (pyproject.toml, requirements.txt)"
docs_url: "https://github.com/Lekssays/codebadger/tree/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Bridges Joern Code Property Graphs with LLMs via MCP - enables AI agents to run CPGQL queries, trace data flow/taint, slice programs, and hunt vulnerabilities across 13+ languages. Scales with per-CPG worker pools, memory-aware scheduling, Postgres/Redis backend. Accepted at ICSE 2026 Software Vulnerability Management Workshop."
---

Codebadger, built at QCRI, gives LLM agents structured access to program analysis that plain code reading cannot provide. It constructs Joern Code Property Graphs from a git repository, local path, or pasted snippet, then exposes them over MCP so an external agent can run CPGQL queries, follow data-flow and taint paths, slice programs, and develop vulnerability proofs of concept across 13+ languages including Java, C/C++, Go, and Swift. The service scales through per-CPG worker pools with memory-aware scheduling on a Postgres and Redis backend, and documents an LLM workflow guide plus a security threat model for the analysis pipeline. It is a tools supplier rather than an agent: the repository is explicitly packaged as an MCP server (Dockerfile.mcp), with agents running externally, and it was published at the ICSE 2026 Software Vulnerability Management Workshop.
