---
name: "tokenjuice"
slug: "tokenjuice"
layout: "agent.njk"
category: "other"
maker: "vincentkoc"
license: "MIT"
url: "https://github.com/vincentkoc/tokenjuice"
source_code_url: "https://github.com/vincentkoc/tokenjuice"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-14"
current_release: "2026-06-18"
stars: "503"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "npm install -g tokenjuice  (or brew tap vincentkoc/tap && brew install tokenjuice)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/tokenjuice"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Deterministic, rule-driven output compactor (JSON rules, not LLM vibes) for terminal-heavy agent workflows. Runs commands, observes output, and returns a smaller payload — reducing transcript waste across 80+ agent/IDE integrations via thin host adapters. Raw output bypass via --raw/--full. Most host integrations install a hook/rule/guidance file (Claude Code, Codex, Cursor)."
---

TokenJuice attacks the token waste produced when agents run noisy commands — git status dumps, test suites, docker builds — by intercepting command output and returning a compacted version before it reaches the model's context. Compression is deterministic: rule files written in JSON describe what to keep, elide, or summarize per command, so behavior is auditable and reproducible rather than an LLM paraphrase, and raw output remains reachable via explicit --raw/--full flags or stored artifacts. Distribution is the distinctive part: tokenjuice install writes host-native integration files — a Claude Code hook in settings.json, Codex/Cursor rules, plugin entries for OpenCode and others — covering roughly 100 hosts, so the same rules apply across editors, CLIs, and CI. The project is MIT-licensed TypeScript, installable via npm or Homebrew, with docs covering the adapter spec and rule format. Teams running terminal-heavy agent workflows who want lower token spend without behavioral unpredictability are the target users.
