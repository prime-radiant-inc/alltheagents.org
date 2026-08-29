---
name: "coding-agent-tips"
slug: "coding-agent-tips"
layout: "agent.njk"
category: "other"
maker: "anipotts"
license: "MIT"
url: "https://github.com/anipotts/coding-agent-tips"
source_code_url: "https://github.com/anipotts/coding-agent-tips"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-02-25"
current_release: "2026-08-17"
stars: "27"
language: "TypeScript"
homepage: "https://agents.anipotts.com"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "False"
subagents: "no"
hooks: "yes"
plan_mode: "no"
model_providers: "None (documentation site; covers Claude Code, Codex, Grok)"
pricing: "Free / open-source"
install_method: "bun install --frozen-lockfile (Astro + Starlight site)"
docs_url: "https://agents.anipotts.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/anipotts/coding-agent-tips"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Evidence-backed guidance publication for coding agents in production software, covering Claude Code and Codex. Enforces a strict evidence standard (hands-on, source-verified, inference, unknown) and publishes task specs, sanitized run records, and artifacts in a field lab. Corrections require primary sources."
---

Most advice about coding agents is folklore, and practitioners operating agents on production code need to know which claims are tested. coding-agent-tips is a handbook published at agents.anipotts.com that grades every claim against a stated evidence standard, separating what the author verified hands-on from what official sources, analysis, or open questions support. Content is organized by the stakes of the reader's work - students, startup founders, big-tech engineers - rather than by tool, and covers the distinction between steering surface, harness, model, and orchestration, plus repo instructions, permissions, review practices, and operating costs. The repository is an Astro site with accessibility and site tests, and the guidance doubles as a Claude Code plugin so readers can apply the practices directly. It targets developers standardizing how their teams work with agents.
