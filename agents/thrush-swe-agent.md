---
name: "thrush-swe-agent"
slug: "thrush-swe-agent"
layout: "agent.njk"
category: "agent"
maker: "shoyann"
license: null
url: "https://github.com/shoyann/thrush-swe-agent"
source_code_url: "https://github.com/shoyann/thrush-swe-agent"
source_available: "True"
platforms: []
first_released: "2026-05-28"
current_release: "2026-06-18"
stars: "63"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "deepseek, openai, anthropic"
pricing: "open-source"
install_method: "git clone --recurse-submodules, npm install, npm run bootstrap:mini, copy .env.local.example to .env.local, npm run dev"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/shoyann/thrush-swe-agent.git"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Dual-mode local SWE agent workbench: Assist mode (agent drafts edits, user approves each one) and Auto mode (runs bundled mini-swe-agent in isolated git worktree, returns report, diff, logs, trajectory without touching main workspace)"
---

Thrush is a local, self-hosted workbench for software-engineering agents built around two deliberately different safety postures. In supervised operation the agent inspects the repo, reasons, drafts edits, and asks for confirmation, with every change staged as a pending revision the developer approves before anything touches disk. Delegating a full task instead routes it to a bundled mini-swe-agent instance running inside an isolated git worktree under data/auto-runs, after an Environment Doctor pre-check verifies clean git state, Docker, the model key, and GitHub readiness; the run produces a report, diff, logs, and full trajectory while the main workspace stays untouched, and opening a draft PR remains a manual step. The implementation is Next.js 15 with SQLite, keyed for DeepSeek, OpenAI, or Anthropic, with Windows users directed to WSL. It fits developers who want one local workbench that can switch between reviewed drafting and autonomous runs on throwaway worktrees.
