---
name: "claude-code-merge-queue"
slug: "claude-code-merge-queue"
layout: "agent.njk"
category: "other"
maker: "funador"
license: "MIT"
url: "https://github.com/funador/claude-code-merge-queue"
source_code_url: "https://github.com/funador/claude-code-merge-queue"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-10"
current_release: "2026-08-24"
stars: 124
language: "TypeScript"
homepage: "https://www.npmjs.com/package/claude-code-merge-queue"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "npm (claude-code-merge-queue); requires Node 18+"
docs_url: "https://github.com/funador/claude-code-merge-queue/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/claude-code-merge-queue"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A local, zero-cost merge queue that serializes landings when multiple parallel Claude Code agents work in the same repo: numbered lanes in git worktrees, a FIFO queue onto the integration branch, a WorktreeCreate hook, a machine-wide build lock, and a pre-push hook that blocks direct pushes so agents must pass the checkCommand gate via land."
---

claude-code-merge-queue is the git plumbing for running many Claude Code agents in parallel on one repository. It manages numbered lanes as git worktrees so several agents can build and test simultaneously, then serializes landings onto the integration branch through a FIFO queue that prevents push races, redundant builds, and test flakiness from shared resources. A Husky pre-push hook blocks direct pushes to the integration branch, forcing agents through the land command, which runs a configurable checkCommand gate before merging, and its init writes the config file, CLAUDE.md instructions, Claude settings, and package.json scripts. It is a free, local alternative to GitHub Merge Queue with no PRs and no cloud costs, single-machine only, and explicitly not a security boundary — the companion tooling around the agents rather than an agent itself.
