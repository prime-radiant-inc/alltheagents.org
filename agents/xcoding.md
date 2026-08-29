---
name: "XCoding"
slug: "xcoding"
layout: "agent.njk"
category: "multiplexer"
maker: "XCodingLab"
license: "MIT"
url: "https://github.com/XCodingLab/XCoding"
source_code_url: "https://github.com/XCodingLab/XCoding"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-01-05"
current_release: "2026-02-02"
stars: "54"
language: "TypeScript"
homepage: "https://github.com/XCodingLab/XCoding"
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI Codex, Anthropic Claude Code"
pricing: "Free / open-source"
install_method: "Download from GitHub Releases latest; or pnpm install + pnpm run dev for local dev"
docs_url: "https://github.com/XCodingLab/XCoding"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/XCodingLab/XCoding/releases/latest"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Lightweight AI vibe-coding IDE supporting parallel multi-agent collaboration (Codex/Claude Code) and parallel multi-project development with VS Code-like editor, terminal, and preview in one window."
---

XCoding is a lightweight vibe-coding IDE built for running several AI agents and several projects at once: one window hosts a VS Code-like editor, terminal, and app preview alongside agent collaboration from Codex and Claude Code, with projects switchable via Cmd/Ctrl+1-8. AI assistance can be invoked at any point, with changes applied or rolled back in one step, and task-driven workflows manage code changes across the session. The core is deliberately opinionated: no plugin marketplace, with built-ins covering the main path to keep the app light and fast. The codebase is TypeScript (Vite, tsup, Tailwind, pnpm) under MIT, distributed in English and Simplified Chinese. It is very early stage, with 18 commits and no published releases.
