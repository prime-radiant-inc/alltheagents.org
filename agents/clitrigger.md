---
name: "CLITrigger"
slug: "clitrigger"
layout: "agent.njk"
category: "multiplexer"
maker: "HyperAITeam"
license: "MIT"
url: "https://github.com/HyperAITeam/CLITrigger"
source_code_url: "https://github.com/HyperAITeam/CLITrigger"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-03-24"
current_release: "2026-08-18"
stars: "13"
language: "TypeScript"
homepage: "https://www.npmjs.com/package/clitrigger"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
model_providers: "Claude Code, Antigravity, Codex, Gemini"
pricing: "free"
install_method: "Desktop app (Windows .exe, macOS .dmg, Linux .AppImage) from GitHub Releases; or npm i -g clitrigger (requires Node.js 22+ LTS, Git, >=1 AI CLI)"
docs_url: "https://github.com/HyperAITeam/CLITrigger/wiki"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/HyperAITeam/CLITrigger/releases/latest"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "An 'IDE for AI CLI agents.' Unifies the AI-coding workflow into a single five-stage pipeline — Docs -> Plan -> Terminal -> Autonomous Tasks -> Version Control — where each stage inherits the context of the previous one. Runs multiple AI CLIs (Claude Code, Antigravity, Codex) in parallel, each in its own isolated git worktree, with scheduling around rate limits, multi-agent debate (architect/developer/reviewer), and a built-in Git client + review queue to land the diffs."
---

CLITrigger's thesis is that the AI-coding workflow scatters across five applications, and that a single workspace where each stage inherits context eliminates the re-explanation tax. Documentation lives in an Obsidian-style vault whose pages can be injected into prompts; planned tasks dispatch to multiple CLI agents in parallel worktrees with cron scheduling and rate-limit retry; multi-agent discussion (architect, developer, reviewer) runs before output reaches a review queue tied to a built-in Git client. An MCP endpoint and optional Cloudflare Tunnel extend it. It wraps the CLIs via adapters and runs no model loop itself. Individual developers managing several agent CLIs are the intended users.
