---
name: "codebase-argus"
slug: "codebase-argus"
layout: "agent.njk"
category: "agent"
maker: "AaronZ345"
license: "MIT"
url: "https://github.com/AaronZ345/codebase-argus"
source_code_url: "https://github.com/AaronZ345/codebase-argus"
source_available: "True"
platforms: []
first_released: "2026-05-05"
current_release: "2026-07-24"
stars: "58"
language: "TypeScript"
homepage: "https://aaronz345.github.io/codebase-argus/"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "openai-api, anthropic-api, gemini-api (API); codex-cli, claude-cli, gemini-cli (local CLI)"
pricing: "Free/open source"
install_method: "/plugin marketplace add AaronZ345/codebase-argus then /plugin install codebase-argus@codebase-argus (Claude Code); or npm ci / npm link for local dev"
docs_url: "https://aaronz345.github.io/codebase-argus/"
plugin_docs_url: "https://github.com/AaronZ345/codebase-argus#agent-playbook"
config_docs_url: "https://github.com/AaronZ345/codebase-argus#readme"
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Multi-agent PR review + downstream fork-sync risk analysis for maintainers; combines deterministic review with multi-provider tribunal consensus, local git simulations (merge-tree, rebase, cherry, range-diff), and CI failure diagnosis."
---

Codebase-argus targets repository maintainers who need review verdicts they can trust, combining deterministic evidence with multi-model judgment. For each pull request it assembles an evidence package — patch, check status, changed files, branch state, policy gates from .codebase-argus.yml, and prior reviews — enriched with local git simulations such as merge-tree projections, rebase simulations, and git cherry/range-diff comparisons against downstream forks. Multiple providers then review the same evidence, and tribunal mode groups findings that independent models agree on, surfacing provider failures rather than hiding them. Beyond PR review it diagnoses CI failures from logs and plans gated autofixes for mechanical changes. It ships as a CLI, a Next.js dashboard, a GitHub Action, a webhook-based GitHub App, and a Claude Code plugin installable from a marketplace.
