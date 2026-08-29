---
name: "CyCode"
slug: "cycode"
layout: "agent.njk"
category: "agent"
maker: "vibe-cy"
license: "unlicensed (no license file; README notes one is pending)"
url: "https://github.com/vibe-cy/CyCode"
source_code_url: "https://github.com/vibe-cy/CyCode"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-06-25"
current_release: "2026-06-27"
stars: "45"
language: "TypeScript (Node.js 18+)"
homepage: "https://github.com/vibe-cy/CyCode"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "no"
model_providers: "OpenAI, DeepSeek, DashScope/Qwen, any OpenAI-compatible"
pricing: null
install_method: "npm install, cp .env.example .env, npm run build, npm start"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/vibe-cy/CyCode"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Lightweight terminal-first AI coding agent using OpenAI-compatible Chat Completions API. Built-in tools for reading files, applying precise edits, searching code, running shell commands, and delegating work to sub-agents. Multi-provider compatibility, context compression for long conversations, token/cost tracking, dual interactive TUI + one-shot scripting mode, built-in shell command safety blocking, and programmatic API for reuse. Very early stage (5 commits)."
---

CyCode is a self-hosted, terminal-first coding agent written to demonstrate how little a working agentic loop requires: file read/write/edit, bash (with some high-risk command blocking), grep/glob search, and a sub-agent tool, all wired through an OpenAI-compatible Chat Completions API. It runs on Node 18 with an Ink-based TUI (REPL fallback), saves and resumes sessions, compresses context, and tracks token cost, and it works with OpenAI, DeepSeek, DashScope/Qwen, or any compatible endpoint via environment keys. The project is very early: five commits, 45 stars, no releases, and no license file yet, so it functions primarily as a compact reference implementation for developers studying or forking a small agent harness.
