---
name: "Codex Security"
slug: "codex-security"
layout: "agent.njk"
category: "agent"
maker: "openai"
license: "Apache-2.0"
url: "https://github.com/openai/codex-security"
source_code_url: "https://github.com/openai/codex-security"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-07-13"
current_release: "2026-08-20"
stars: "9980"
language: "TypeScript"
homepage: "https://developers.openai.com/codex/security"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, OpenRouter, Fireworks, Amazon Bedrock"
pricing: "open-source"
install_method: "npm"
docs_url: "https://learn.chatgpt.com/docs/security/cli"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "AI-driven end-to-end security workflow CLI/SDK: discovers, validates, and auto-patches vulnerabilities, verifies fixes, and opens GitHub PRs. Deep multi-agent scans with --subagents flag. Interactive finding review, scan comparison by root cause, Linear issue publishing. Containerized bulk scans with AppArmor hardening. Pluggable inference providers. Extensibility via scan prompt files and knowledge bases."
---

Security review rarely keeps pace with code changes, and static scanners produce noise that nobody remediates. Codex Security applies an agent loop to that gap: discovery runs scan a codebase, each candidate finding is validated before reporting, generated patches are verified, and verified fixes become GitHub pull requests for human review. The CLI wraps a TypeScript SDK so teams can embed scans in CI with an API key or authenticate interactively through ChatGPT, with Trusted Access gating for sensitive finding categories. A findings service stores results in SQLite, deduplicates them by embedding similarity, and serves a dashboard. Security teams and maintainers use it to move from scanner output to verified remediation, and Docker Compose configurations support bulk scans across repository sets.
