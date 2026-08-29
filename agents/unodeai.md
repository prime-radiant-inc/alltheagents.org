---
name: "UnodeAi"
slug: "unodeai"
layout: "agent.njk"
category: "agent"
maker: "unode"
license: "MIT"
url: "https://open-vsx.org/extension/unode/unodeai"
source_code_url: "https://github.com/UnodeTechxyz/unodeai.git"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-08-27"
current_release: "2026-08-28"
stars: null
language: "TypeScript"
homepage: "https://www.unodetech.xyz"
mcp_support: "yes"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "Unode gateway (multi-model, single account), any OpenAI-compatible endpoint, local/self-hosted gateways, Claude via existing CLI login"
pricing: "freemium"
install_method: "Install from Open VSX"
docs_url: "https://github.com/UnodeTechxyz/unodeai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://open-vsx.org/extension/unode/unodeai"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Project manager delegates coding across role agents on different models with receipts"
---

UnodeAI exists because multi-agent coding runs produce unverifiable claims: one agent reports 'done' and a second model is asked to grade it, which proves little. The extension structures delegation instead around observed evidence — commands run, files touched, approvals granted — with verdicts ascending a ladder from 'no evidence' to 'coordinator accepted,' and rejections requiring a recorded reason that visibly amends earlier verdicts. A project-manager agent plans and assigns tasks to specialist role agents, each running with configured tools, provider routes, and folder access that task scoping can narrow but never widen; optional worktree isolation and an approved verify command gate merges. Runs export as client-readable Markdown reports or privacy-stripped JSON. Developers and agencies delegating work to AI crews — and needing receipts for clients or auditors — use it in VS Code and Cursor; it is MIT-licensed, telemetry-free, and runs entirely on the user's own providers and keys.
