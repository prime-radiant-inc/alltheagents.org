---
name: "Gambit"
slug: "gambit"
layout: "agent.njk"
category: "other"
maker: "bolt-foundry"
license: "Apache-2.0"
url: "https://github.com/bolt-foundry/gambit"
source_code_url: "https://github.com/bolt-foundry/gambit"
source_available: "Yes"
platforms:
  - "CLI"
first_released: "2025-11-21"
current_release: "2026-05-15"
stars: "242"
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenRouter (default), Claude Code CLI, Codex CLI, custom providers"
pricing: "open-source"
install_method: "npx @bolt-foundry/gambit (no install); Deno via jsr:@bolt-foundry/gambit"
docs_url: "https://github.com/bolt-foundry/gambit"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Builds the evidence layer for agent systems: generate and quality-validate realistic scenarios, run any agent against them, grade transcripts from JSONL traces, and promote failures into regression suites gated in CI."
---

Teams shipping agent features lack a systematic way to prove they work, so Bolt Foundry built Gambit around scenario generation, grading, and regression. Agents under test — whether Mastra, LangGraph, OpenAI Agents SDK, or custom stacks — are exercised through one-shot runs, a REPL, or a browser chat with full traces, while Gambit's own 'deck' agents are defined in Markdown or TypeScript with Zod schemas. Grading turns transcripts into pass/fail evidence, and a GitHub Actions example shows scenario grades acting as PR gates. Agents compose through child actions and ctx.spawnAndWait, OpenRouter is the default provider with Claude Code and Codex CLIs as alternative runtimes, and the repository has moved from bolt-foundry to the coworkerprotocol-org.
