---
name: "Twing"
slug: "twing"
layout: "agent.njk"
category: "other"
maker: "twing"
license: "AGPL-3.0"
url: "https://twing.dev/"
source_code_url: "https://github.com/Twing-dev/twing-cli"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-08-09"
current_release: "2026-08-27"
stars: 3
language: "TypeScript"
homepage: "https://twing.dev/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: null
pricing: "freemium"
install_method: "npm install -g @twing/cli (Node >= 20); twing init installs the twing-hook Go binary and wires it into Claude Code hooks"
docs_url: "https://github.com/Twing-dev/twing-cli/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@twing/cli"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "A coordination layer for fleets of coding agents: twing align advisory-checks critical files, active work, and design overlap, while the one blocking gate requires a registered design before an agent's first Edit or Write, with conflicts bucketed into constraint violations, file overlap, Tree-sitter symbol conflicts, and LLM-judged semantic divergence. Fails closed if the coordinator is unreachable."
---

Twing is aimed at engineering leaders running fleets of AI coding agents, on the observation that agents write whole features in parallel on the same codebase and duplicate work, contradict each other, and land conflict-prone PRs faster than humans can review. The live piece is a CLI plus a hook installed into your coding agent (Claude Code today, others planned) plus a small coordination server — hosted free at coordination-server.twing.dev or self-hosted — where a background daemon syncs the hook's stateless observations. twing align is advisory only, flagging critical files, concurrent work, and overlap with registered designs, while the design-conflict gate is the one blocking mechanism: before an agent's first edit in a session it must have a registered design, and conflicts sort into admin-gated constraint violations, advisory file overlaps, self-justifiable Tree-sitter symbol conflicts, and LLM-judged semantic divergence. It does not write code itself — it is the coordination tooling around agents — and the roadmap adds a review artifact beyond line diffs and compounding organizational context.
