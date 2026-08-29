---
name: "RepoAgent"
slug: "repoagent"
layout: "agent.njk"
category: "other"
maker: "OpenBMB"
license: "Apache-2.0"
url: "https://github.com/OpenBMB/RepoAgent"
source_code_url: "https://github.com/OpenBMB/RepoAgent"
source_available: "True"
platforms: []
first_released: "2023-11-28"
current_release: "2024-12-23"
stars: "1029"
language: "Python"
homepage: "https://github.com/OpenBMB/RepoAgent"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "open-source"
install_method: "pip"
docs_url: "https://arxiv.org/abs/2402.16667v1"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/repoagent/"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "LLM-powered framework for automatic repository-level code documentation generation using AST-based per-object analysis with bidirectional invocation relationship detection. Multi-threaded concurrent generation, seamless Markdown replacement on code changes, and pre-commit hook for team-wide automated doc maintenance. Prototype Chat With Repo feature for Q&A and code explanation."
---

Repository documentation rots because writing it is unpaid labor and updating it after every refactor is worse; RepoAgent automates the maintenance part. It parses the project into an AST, produces per-object Markdown entries that record callers and callees in both directions, and stores the results as a Gitbook-style book inside the repo. On each commit, a diff-driven pass regenerates only the affected objects, which keeps cost and review surface proportional to the change. Generation is multi-threaded with customizable prompts and output language, and an optional chat-with-repo service answers questions from the generated corpus. Research groups and Python project maintainers use it to keep documentation synchronized with code; Java and C++ support remains future work.
