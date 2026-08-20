---
name: "deep-swe"
slug: "deep-swe"
layout: "agent.njk"
category: "agent"
maker: "datacurve-ai"
license: "Apache-2.0"
url: "https://github.com/datacurve-ai/deep-swe"
source_code_url: "https://github.com/datacurve-ai/deep-swe"
source_available: True
platforms: []
first_released: "2026-05-15"
current_release: "2026-08-06"
stars: "1439"
language: "TypeScript, Go, Python, JavaScript, Rust (task corpus); Python (harness)"
homepage: "https://deepswe.datacurve.ai/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a - Pier drives Claude Code directly as one of several supported agents"
subagents: "no"
hooks: "yes - [[verifier.collect]] hook in each task.toml extracts agent commits as a patch for grading"
plan_mode: "no"
model_providers: "Anthropic (Claude Opus 4.8), OpenAI (GPT-5.5); supports multiple CLI agents"
pricing: "open-source"
install_method: "pip"
docs_url: "https://deepswe.datacurve.ai/"
plugin_docs_url: null
config_docs_url: "https://www.harborframework.com/docs/tasks"
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Benchmark for frontier coding agents on original, long-horizon software engineering tasks drawn from active open-source repos (113 tasks across 5 languages). Real-world tasks rather than synthetic/curated examples, designed for multi-step sustained engineering. Behavior-based verification: accepts any solution with correct observable behavior regardless of internal structure/symbol names - reference patches held out and never used at grading time. Uses a fork of Harbor (Pier) with per-agent network allowlists for air-gapped tasks; agents work in a sandbox and commits extracted/graded in a pristine container. Runs model-agnostic mini-swe-agent plus native CLI agents (Claude Code, Codex, Gemini CLI, opencode), with optional parallel sandboxes on Modal."
---

Benchmark for frontier coding agents on original, long-horizon software engineering tasks drawn from active open-source repos (113 tasks across 5 languages). Real-world tasks rather than synthetic/curated examples, designed for multi-step sustained engineering. Behavior-based verification: accepts any solution with correct observable behavior regardless of internal structure/symbol names - reference patches held out and never used at grading time. Uses a fork of Harbor (Pier) with per-agent network allowlists for air-gapped tasks; agents work in a sandbox and commits extracted/graded in a pristine container. Runs model-agnostic mini-swe-agent plus native CLI agents (Claude Code, Codex, Gemini CLI, opencode), with optional parallel sandboxes on Modal.
