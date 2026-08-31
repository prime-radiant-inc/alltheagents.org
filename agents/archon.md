---
name: "Archon"
slug: "archon"
layout: "agent.njk"
category: "multiplexer"
maker: "coleam00"
license: "MIT"
url: "https://github.com/coleam00/Archon"
source_code_url: "https://github.com/coleam00/Archon"
source_available: "Yes"
platforms: []
first_released: "2025-02-07"
current_release: "2026-08-19"
stars: "23231"
language: "TypeScript"
homepage: "https://archon.diy"
mcp_support: "yes"
plugin_support: "yes (platform adapters: Web, CLI, Telegram, Slack, Discord, GitHub Webhooks)"
claude_code_plugin: "yes (ships a Claude Code skill; .claude directory; Claude Code is a prerequisite)"
subagents: "yes (multi-agent workflows, parallel reviewers, adversarial dev)"
hooks: "yes (validation gates, type-check hooks, approval gates)"
plan_mode: "yes (explicit plan nodes; archon-plan-to-pr workflow)"
model_providers: "Claude, Codex, Pi"
pricing: "open-source"
install_method: "binary (curl install script), brew, docker"
docs_url: "https://archon.diy/docs/"
plugin_docs_url: null
config_docs_url: "https://archon.diy/docs/"
download_url: "https://archon.diy/install"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "The first open-source harness builder for AI coding; makes AI coding deterministic and repeatable by encoding development processes as YAML workflows with isolated git worktrees per run, parallel execution, human approval gates, and composable deterministic + AI nodes."
---

Archon, by cole medin (coleam00), tackles the problem that AI coding agents behave nondeterministically: the same prompt can produce different results on different runs. It encodes development processes as YAML workflow definitions - planning, implementation, validation, review, and PR creation as reusable stages - so the same process runs deterministically each time, with isolated git worktrees per run enabling parallel execution. Runs can start from the CLI, web UI, Slack, Telegram, Discord, or GitHub webhooks, and 19 default workflows ship out of the box (fix-github-issue, idea-to-pr, plan-to-pr, comprehensive PR review). Claude Code is the primary assistant, with Codex and Pi also supported, and the MIT-licensed TypeScript (Bun) codebase is under very active development. Teams use it to standardize how coding agents execute repeatable engineering processes rather than hoping a prompt works.
