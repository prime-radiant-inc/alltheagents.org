---
name: "vibe-coding-kit"
slug: "vibe-coding-kit"
layout: "agent.njk"
category: "other"
maker: "Junliu1066"
license: "MIT"
url: "https://github.com/Junliu1066/vibe-coding-kit"
source_code_url: "https://github.com/Junliu1066/vibe-coding-kit"
source_available: "True"
platforms: []
first_released: "2026-06-16"
current_release: "2026-06-30"
stars: "167"
language: null
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "True"
model_providers: "None (methodology pack executed by the host agent: Claude Code, Claude web/desktop, ChatGPT, Codex)"
pricing: "Free/open-source"
install_method: "Copy SKILL.md content into any AI chat; or upload as a custom Skill in Claude web/desktop; or git clone and copy skill folders to ~/.claude/skills/ for Claude Code CLI"
docs_url: "https://github.com/Junliu1066/vibe-coding-kit#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Junliu1066/vibe-coding-kit"
maintained: "active"
sources:
  - "github_final"
what_makes_it_special: "Planning toolkit (Chinese-language) for non-technical 'vibe coders'; 6 structured Skills (prd, requirements, architecture, production, survival, harness) plus a 3-layer governance system (CLAUDE.md constitution -> quality-check agent -> per-skill self-check) and a v2 workflow pipeline (S1 requirements -> S2 architecture -> S3 production) with exit gates and a progress ledger."
---

The kit targets the failure mode of non-programmers driving AI coding tools: vague requirements produce chaotic changes, and without a planning discipline the result is unmaintainable. Its six skills structure the work — a PRD interview skill interrogates the user into a written spec, a requirements skill checks whether code is even needed, architecture and production skills cover tech selection and delivery standards, survival handles rollback and context recovery after messy AI changes, and a harness skill verifies output completeness. A governance layer ties the skills together: a CLAUDE.md constitution, an S1→S2→S3 stage-gated workflow, and progress ledgers that survive context resets. Non-technical Chinese-speaking builders — PMs, founders, indie makers — install the skills into Claude Code or paste them into ChatGPT/Codex; it is an MIT-licensed methodology pack rather than a tool.
