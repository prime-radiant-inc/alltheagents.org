---
name: "Catnip"
slug: "catnip"
layout: "agent.njk"
category: "multiplexer"
maker: null
license: null
url: "https://github.com/wandb/catnip"
source_code_url: "https://github.com/wandb/catnip"
source_available: "Source-visible (no OSS license)"
platforms: []
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "open-source"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dead"
sources:
  - "brad"
what_makes_it_special: "Containerized environment + worktree automation for running multiple coding agents in parallel (optimized for Claude Code). Could not verify detailed fields — the GitHub repo (wandb/catnip) returns 404 (deleted, renamed, or made private)."
---

Catnip, developed by Weights & Biases, provided containerized development environments and git-worktree automation aimed at running multiple coding agents — optimized for Claude Code — in parallel, with a companion iOS app for supervising agents remotely. Its model targeted developers who keep several agents working simultaneously: each agent gets its own worktree and container, the web interface tracks their state, and changes land as reviewable diffs. The repository at github.com/wandb/catnip now returns 404, indicating the repository was deleted or made private, so per-repo metadata could not be verified during this enrichment pass. Wandb's own site no longer surfaces the project, and no successor announcement was found; the entry is retained with the census's existing description and treated as likely no longer publicly maintained. Users seeking similar functionality would need to look at the container/worktree automation space generally rather than at this specific repo.
