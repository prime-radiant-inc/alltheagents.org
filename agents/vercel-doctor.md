---
name: "vercel-doctor"
slug: "vercel-doctor"
layout: "agent.njk"
category: "other"
maker: "Aniket-508"
license: "MIT"
url: "https://github.com/Aniket-508/vercel-doctor"
source_code_url: "https://github.com/Aniket-508/vercel-doctor"
source_available: "True"
platforms: []
first_released: "2026-02-19"
current_release: "2026-04-07"
stars: "44"
language: "TypeScript / JavaScript"
homepage: "https://vercel-doctor.com"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None (deterministic rule-based analysis; no LLM at analysis time)"
pricing: "Free / open-source"
install_method: "npx -y vercel-doctor@latest . (for projects); curl -fsSL https://vercel-doctor.com/install-skill.sh | bash (for coding agents)"
docs_url: "https://vercel-doctor.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/vercel-doctor"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Reduces Vercel bills with one command. Scans Next.js codebases for patterns that inflate Vercel bills (long function duration, uncached routes, unoptimized images) and detects dead code, outputting actionable diagnostics. Supports coding agent skills for Cursor, Claude Code, Amp Code, Codex, Gemini CLI, OpenCode, Windsurf, and Antigravity. Generates AI-ready fix prompts for popular coding agents. Supports Next.js 15/16+."
---

Vercel costs rise quietly: an uncached route, a sequentially-awaited function, or an unoptimized image shows up as invoice line items long after the code shipped. Vercel Doctor addresses that with a deterministic scanner — no LLM involved — that runs two passes over a Next.js codebase: one flags billing-relevant patterns (function duration, caching configuration, image optimization, prefetch behavior, edge functions, cron usage, build caching), the other finds dead code such as unused files, exports, and duplicates, then emits a scored report with file-level detail, version-aware Next.js 15/16 guidance, and JSON/markdown output for CI via a GitHub Action. For remediation it ships an installable skill and --ai-prompts output that feed ready-made fix prompts to Cursor, Claude Code, Codex, and other agents, which perform the actual edits. Next.js teams auditing cloud spend use it; it is MIT-licensed, unaffiliated with Vercel, and actively maintained on npm.
