---
name: "super-dev"
slug: "super-dev"
layout: "agent.njk"
category: "other"
maker: "shangyankeji"
license: "MIT"
url: "https://github.com/shangyankeji/super-dev"
source_code_url: "https://github.com/shangyankeji/super-dev"
source_available: "True"
platforms: []
first_released: "2025-12-29"
current_release: "2026-06-19"
stars: "273"
language: "Python"
homepage: "https://SuperDev.Goder.ai"
mcp_support: null
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Claude Code, Codex CLI, Gemini CLI, OpenCode, Kiro CLI, Cursor CLI, Copilot CLI, Qoder CLI, CodeBuddy CLI, Kimi Code, Qwen Code, Droid CLI, Antigravity, Cursor, Windsurf, Kiro, Trae IDE, TraeCN, CodeBuddy, CodeBuddyCN, Qoder, Claude, Codex App, WorkBuddy, Trae SOLO, Trae SOLOCN"
pricing: "open-source"
install_method: "uv tool install super-dev"
docs_url: "https://github.com/shangyankeji/super-dev/blob/main/docs/README.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Engineering workflow layer / host coaching system for AI coding tools. Wraps AI coding hosts (Claude Code, Codex, Cursor, etc.) into a standardized, auditable, commercial-grade delivery pipeline: research → docs → spec → frontend → backend → quality gates → delivery. Provides 11 expert agents, knowledge-driven governance (270+ knowledge files), UI design system, quality gate engine (25 YAML rules), and traceable delivery artifacts."
---

super-dev addresses the gap between an agent that can write code and a delivery process that can ship it: after detecting which of 26 supported hosts (Claude Code, Codex CLI, Cursor, Gemini CLI, and others) is in use, it injects project-level rules, skills, and slash commands that put the host into a staged pipeline with confirmation gates between research, documentation, spec, frontend, backend, quality, and delivery. Eleven expert personas with 350-plus-line playbooks and a 270-file knowledge base drive each stage, while 25 YAML quality-gate rules enforce spec-code consistency, accessibility, and red-team review. Delivery artifacts are traceable proof-packs and release-readiness reports rather than a single diff. It installs via uv as a Python tool, works bilingually in English and Chinese, and suits teams using agent CLIs who need auditable, repeatable engineering process on top.
