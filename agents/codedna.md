---
name: "codedna"
slug: "codedna"
layout: "agent.njk"
category: "other"
maker: "Larens94"
license: "MIT"
url: "https://github.com/Larens94/codedna"
source_code_url: "https://github.com/Larens94/codedna"
source_available: "True"
platforms: []
first_released: "2026-03-15"
current_release: "2026-07-12"
stars: "144"
language: "Python"
homepage: "https://larens94.github.io/codedna"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: null
model_providers: "Anthropic, Google, DeepSeek, Ollama"
pricing: "Free (structural-only mode); LLM mode ~$0.40/200 files (DeepSeek); free with local Ollama"
install_method: "Claude plugin (claude plugin marketplace add Larens94/codedna && claude plugin install codedna@codedna) or pipx install git+https://github.com/Larens94/codedna.git (Python 3.11+)"
docs_url: "https://github.com/Larens94/codedna/blob/main/SPEC.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "In-source communication protocol - AI agents embed architectural context (exports, used_by, related, rules, message) directly in code files. No external memory, retrieval pipeline, or infrastructure needed. Code carries its own context across sessions, models, and multi-agent teams."
---

CodeDNA proposes that the durable fix for agent context loss is to store architectural knowledge in the code itself rather than in an external memory system. Source files carry structured headers — exports, used_by reverse-dependency links, related semantic links, hard rules, and agent-to-agent messages that can be promoted to rules — and a Python CLI (codedna init/verify/impact/check/manifest) verifies that annotations stay accurate as code changes, with git hooks gating commits on stale annotations. The spec targets 12 languages, and integrations reach Claude Code (as an installable plugin), Codex, OpenCode, Aider, Cursor, Copilot, Cline, and Windsurf through instruction files. The project reports benchmark results including a 17-percentage-point navigation F1 gain on SWE-bench navigation tasks with DeepSeek and a 1.6x speedup for multi-agent teams, published alongside a Zenodo DOI for independent replication.
