---
name: "claude-code"
slug: "claude-code-skeleton"
layout: "agent.njk"
category: "other"
maker: "yasasbanukaofficial"
license: null
url: "https://github.com/yasasbanukaofficial/claude-code"
source_code_url: "https://github.com/yasasbanukaofficial/claude-code"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-31"
current_release: "2026-04-04"
stars: "3963"
language: "TypeScript"
homepage: "https://github.com/yasasbanukaofficial/claude-code"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "Anthropic"
pricing: "free"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_topic3"
what_makes_it_special: "A mirror/backup of Anthropic's official Claude Code CLI source code that was accidentally leaked via a sourcemap file (.map) bundled in the npm package. Reveals internal structure: 785KB main.tsx, 40+ tools, React terminal renderer (Ink), multi-agent orchestration (Swarm), ULTRAPLAN (deep planning via Opus), KAIROS (always-on assistant), Tamagotchi companion system (BUDDY), Undercover Mode, and Dream memory system. For educational/archival purposes only — proprietary to Anthropic PBC. Not actively developed (only 2 commits)."
---

The repository existed to preserve and expose the accidentally leaked TypeScript source of Anthropic's Claude Code CLI, which shipped inside the npm package's source map. Its documentation described the internal layout: the large main.tsx bundle, the tool registry, command definitions, and internal architecture that Anthropic does not publish. Developers and researchers consulted it to understand how a production agent harness is structured. The repository has been removed from GitHub and returns 404, so it is no longer available in any form.
