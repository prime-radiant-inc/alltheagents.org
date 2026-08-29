---
name: "Crystal"
slug: "crystal"
layout: "agent.njk"
category: "multiplexer"
maker: "stravu"
license: "MIT"
url: "https://github.com/stravu/crystal"
source_code_url: "https://github.com/stravu/crystal"
source_available: "Yes"
platforms:
  - "Desktop"
first_released: "2025-06-05"
current_release: "2026-02-26"
stars: "3108"
language: "TypeScript"
homepage: "https://nimbalyst.com/"
mcp_support: null
plugin_support: "yes"
claude_code_plugin: "n/a"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic"
pricing: null
install_method: "binary"
docs_url: "https://docs.nimbalyst.com/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://nimbalyst.com/download/"
maintained: "dormant"
sources:
  - "brad"
what_makes_it_special: "Desktop app (now deprecated, replaced by Nimbalyst) for running multiple Codex and Claude Code sessions in parallel git worktrees to test, compare approaches, and manage AI-assisted development workflows."
---

Crystal solved a specific workflow problem: developers running multiple Claude Code or Codex sessions against the same repository would collide over working-tree state. The Electron app gave every session an isolated git worktree, letting users run competing approaches in parallel, compare diffs, and merge the winner. It was MIT-licensed and gathered about 3,100 stars before development ended. As of February 2026 the project was renamed to Nimbalyst, and the repository now directs users to the successor rather than accepting feature work; existing users can still run Crystal, but active development happens elsewhere.
