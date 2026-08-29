---
name: "Explorer"
slug: "explorer"
layout: "agent.njk"
category: "other"
maker: "invariantlabs-ai"
license: "Apache-2.0"
url: "https://github.com/invariantlabs-ai/explorer"
source_code_url: "https://github.com/invariantlabs-ai/explorer"
source_available: "True"
platforms: []
first_released: "2024-12-09"
current_release: "2026-01-12"
stars: "58"
language: "Python"
homepage: "https://invariantlabs.ai/blog/explorer"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "open-source"
install_method: "pip install invariant-ai then run invariant explorer (Docker Compose required)"
docs_url: "https://invariantlabs.ai/blog/explorer"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "A tool for visualizing, exploring, testing, inspecting, and analyzing AI Agent traces."
---

Explorer grew out of Invariant Labs' agent-safety research as the local companion to their analysis stack: a Python API (pip install invariant-ai) plus a web UI that ingests agent traces, exposes tool calls and state for inspection, and supports structured comparison across runs. Teams used it to debug agents — locating the exact tool call where a run went wrong, comparing trajectories across model versions, and turning failures into regression test cases. Deployment ran locally via Docker Compose or the pip package with data stored in ./data, keeping traces on the developer's machine. Invariant Labs was absorbed into Snyk's AI security efforts, the hosted version was shut down in January 2026, and development on the repository has ceased.
