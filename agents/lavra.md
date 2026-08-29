---
name: "lavra"
slug: "lavra"
layout: "agent.njk"
category: "agent"
maker: "roberto-mello"
license: "MIT"
url: "https://github.com/roberto-mello/lavra"
source_code_url: "https://github.com/roberto-mello/lavra"
source_available: "True"
platforms: []
first_released: "2026-02-08"
current_release: "2026-06-27"
stars: "50"
language: "JavaScript, TypeScript"
homepage: "https://lavra.dev"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: null
pricing: "Free / open-source (MIT)"
install_method: "npx @lavralabs/lavra@latest; or git clone + ./install.sh (supports --opencode, --gemini, --cortex flags)"
docs_url: "https://lavra.dev/docs/quickstart"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Plugin for AI coding agents adding compound engineering workflows and persistent memory; 30 specialized subagents across review/research/design/workflow/docs, structured planning with adversarial review, automatic git-tracked JSONL memory capture, and shipping automation (tests, PRs, secret scanning)."
---

Compound engineering — where every unit of work passes through design, implementation, review, and ship stages with research in between — is hard to sustain manually across agent sessions. Lavra installs as a plugin into Claude Code (default), OpenCode, Gemini CLI, or Snowflake Cortex Code and provides pipeline commands (/lavra-design, /lavra-work, /lavra-qa, /lavra-ship) plus a persistent memory store recalled at each session start. Its 30 subagents run at lower model tiers for research and review work, cutting cost substantially relative to running everything on a frontier model. Task tracking delegates to the Beads CLI, and knowledge accumulates in .lavra/memory/knowledge.jsonl, git-tracked with the repo.
