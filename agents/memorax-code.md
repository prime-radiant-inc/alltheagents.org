---
name: "memorax-code"
slug: "memorax-code"
layout: "agent.njk"
category: "other"
maker: "memorax-ai"
license: "MIT"
url: "https://github.com/memorax-ai/memorax-code"
source_code_url: "https://github.com/memorax-ai/memorax-code"
source_available: "True"
platforms: []
first_released: "2026-08-01"
current_release: "2026-08-19"
stars: "399"
language: "TypeScript"
homepage: "https://code.memorax.net/"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: null
hooks: "True"
plan_mode: null
model_providers: null
pricing: null
install_method: "npm install -g @memorax/memorax-code --foreground-scripts"
docs_url: "https://code.memorax.net/"
plugin_docs_url: null
config_docs_url: "https://github.com/memorax-ai/memorax-code/blob/main/docs/configuration.md"
download_url: "https://www.npmjs.com/package/@memorax/memorax-code"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Memory plugin giving Codex, Claude Code, DeepSeek Harness, and OpenCode a shared memory layer; four memory boundaries (Coding, Repo, Personal, Procedure); background memory writeback; preference continuity; procedure reuse; local Memory Viewer; semantic deduplication."
---

Coding agents restart every session with no memory of the fixes, conventions, and preferences learned in earlier runs, and each tool stores what it does remember in its own silo. MemoraX Code addresses this by persisting knowledge into typed boundaries: verified fixes and failed approaches under Coding, architecture maps with commit and PR evidence under Repo, style and format preferences under Personal, and reusable checklists under Procedure. Integration is agent-native rather than API-based, using each host's skill mechanism plus a CLI, and writeback runs in the background so the primary coding session is uninterrupted. A cloud backend carries memory across machines, with a free 90-day guest mode before an account is required, and a local Memory Viewer lets users inspect what the agent remembers. Developers running several different agent CLIs over the same codebase use it to stop re-explaining the same context to each one.
