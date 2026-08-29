---
name: "Pu.sh"
slug: "push"
layout: "agent.njk"
category: "agent"
maker: "NahimNasser"
license: "MIT"
url: "https://pu.dev"
source_code_url: "https://github.com/NahimNasser/pu"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2026-04-24"
current_release: "2026-08-06"
stars: "227"
language: "Shell"
homepage: "https://pu.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "curl -sL pu.dev/pu.sh -o pu.sh && chmod +x pu.sh && ./pu.sh"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/NahimNasser/pu"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A full coding-agent harness in under 400 lines of shell and under 50KB with zero package dependencies — it runs on just sh, curl, and awk plus an API key, making the entire agent loop readable, auditable shell. Includes conversation compaction despite the minimal footprint."
---

Pu.sh answers a question most harnesses never ask: how small can a working coding agent be? The entire implementation is a single POSIX shell script under 50KB that runs with sh, curl, and awk plus an API key — no npm, no Python, no Docker, no runtime beyond a Unix system. The script implements an agent loop where tool calls execute as shell commands the model requests, with conversation compaction built in to keep long sessions inside the context window. Because every line is readable shell, the mechanism is auditable in one sitting, which makes it useful as a reference implementation for anyone learning how agent loops actually work. Developers use it in constrained environments — containers, CI jobs, minimal servers — where installing a full harness is impractical, and as a starting point for building their own loop.
