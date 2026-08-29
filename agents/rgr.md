---
name: "rgr"
slug: "rgr"
layout: "agent.njk"
category: "other"
maker: "kingbootoshi"
license: null
url: "https://github.com/kingbootoshi/rgr"
source_code_url: "https://github.com/kingbootoshi/rgr"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-05-25"
current_release: "2026-05-28"
stars: "23"
language: "TypeScript"
homepage: null
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "False"
plan_mode: "False"
model_providers: "none (LLM-free discipline gate; all checks are deterministic CLI operations)"
pricing: "Free / open-source"
install_method: "git clone, cd rgr, bun run rgr (optionally bun link); or claude plugin marketplace add kingbootoshi/rgr"
docs_url: "https://github.com/kingbootoshi/rgr/blob/main/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/kingbootoshi/rgr"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "No-dependency Red-Green-Refactor gate for coding agents enabling 'trustless engineering' — freezes failing tests with SHA-256 hashes and snapshots, and refuses to mark Green or Refactor if the Red test was edited. The .rgr/ directory is evidence, not authority — CI verifies against a trusted lock the agent cannot control."
---

The premise is that an agent with write access cannot be trusted to report its own test results — it can weaken a failing test, delete the evidence, or replace real assertions with mock-echo tests. rgr makes the discipline mechanical: the agent must first record a genuinely failing test (Red), which the tool freezes with hashes and snapshots; subsequent Green and Refactor steps fail if the protected evidence changed. Because local enforcement can be bypassed by an agent that deletes .rgr, the authoritative mode replays the Red proof from recorded base commits inside CI, outside the agent's reach. It ships as Claude Code and Codex plugins with a prompt block that discourages shallow tests, and it is aimed at engineers who want CI to verify agent work without trusting the agent's report.
