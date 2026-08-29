---
name: "codealmanac"
slug: "codealmanac"
layout: "agent.njk"
category: "other"
maker: "AlmanacCode"
license: "Apache-2.0"
url: "https://github.com/AlmanacCode/codealmanac"
source_code_url: "https://github.com/AlmanacCode/codealmanac"
source_available: "True"
platforms: []
first_released: "2026-04-16"
current_release: "2026-07-25"
stars: "800"
language: "Python"
homepage: "https://codealmanac.com"
mcp_support: "no"
plugin_support: "partial (skills/subagents/workflows folders)"
claude_code_plugin: "no"
subagents: "yes (Yoke native subagents/ folder)"
hooks: "no"
plan_mode: "no"
model_providers: "Codex, Claude (via Yoke Python Agent SDK)"
pricing: "open-source"
install_method: "pip (uv tool install)"
docs_url: "https://codealmanac.com"
plugin_docs_url: null
config_docs_url: "https://github.com/AlmanacCode/codealmanac#configuration"
download_url: "https://pypi.org/project/codealmanac/"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "AI-maintained wiki that lives in your repo as plain markdown, committed and reviewed like code, giving agents durable context the codebase can't encode. Auto-ingests from agent conversations (syncs local Codex/Claude transcripts). Garden mode schedules agent runs to prune stale pages, fix weak links, dedupe knowledge. Local-first, no cloud upload. Y Combinator S26-backed."
---

Codealmanac gives coding agents durable project knowledge that the code itself cannot express — rationale, invariants, incident history, cross-file workflows — by maintaining a markdown wiki inside the repository that agents read as context and humans review as ordinary commits. The tool syncs local Codex and Claude Code transcripts on a schedule, extracting durable knowledge into the wiki, and runs scheduled garden passes in which agents prune outdated pages, fix weak links, and merge duplicates. Everything stays local: indexing, storage, and the scheduled launchd jobs run on the developer's machine, with changes committed through git for normal review. It runs lifecycle agents through a Yoke provider boundary supporting Codex and Claude Code, installs via uv from PyPI (the legacy npm package is retired), and requires macOS and Python 3.12 or later.
