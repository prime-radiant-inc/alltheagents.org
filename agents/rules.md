---
name: "rules"
slug: "rules"
layout: "agent.njk"
category: "other"
maker: "project-codeguard"
license: "NOASSERTION"
url: "https://github.com/project-codeguard/rules"
source_code_url: "https://github.com/project-codeguard/rules"
source_available: "True"
platforms: []
first_released: "2025-10-12"
current_release: "2026-01-29"
stars: "420"
language: "Python"
homepage: "https://project-codeguard.org"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "free"
install_method: "Python tooling from source (pyproject/uv); rules distributed to coding agents via per-agent translators and a bundled Claude Code plugin/skills format"
docs_url: "https://project-codeguard.org"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/project-codeguard/rules"
maintained: "dead"
sources:
  - "github_topic4"
what_makes_it_special: "AI model-agnostic security framework and ruleset that embeds secure-by-default practices into AI coding workflows; ships core security rules, translators for popular coding agents, and validators. Donated/moved to Coalition for Secure AI (CoSAI) at github.com/cosai-oasis/project-codeguard"
---

AI-generated code tends to reproduce the insecure patterns in its training data, and every agent ecosystem invented its own instruction format, so a security team would have to maintain parallel rule sets. CodeGuard centralizes the rules — secure-by-default practices for generation and review — and translates them into the formats specific agents consume, from Cursor and Copilot conventions to a Claude Code plugin with software-security skills. Validators close the loop by checking that an agent's output satisfies the rules rather than assuming the instructions were followed. The project originated in industry and was donated to CoSAI for vendor-neutral stewardship, so the original repository is now a pointer; adopters should track the cosai-oasis repository. It is aimed at security teams rolling out AI coding tools with consistent guardrails.
