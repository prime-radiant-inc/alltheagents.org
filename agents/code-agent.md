---
name: "code-agent"
slug: "code-agent"
layout: "agent.njk"
category: "agent"
maker: "potproject"
license: "Apache-2.0"
url: "https://github.com/potproject/code-agent"
source_code_url: "https://github.com/potproject/code-agent"
source_available: True
platforms:
  - "CLI"
first_released: "2025-03-17"
current_release: "2025-04-30"
stars: "38"
language: "TypeScript, Docker"
homepage: null
mcp_support: null
plugin_support: False
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: null
model_providers: "Anthropic (Claude Code), OpenAI (Codex), AWS Bedrock (Claude Code)"
pricing: "Free / open-source GitHub Action (users supply their own API keys)"
install_method: "Configure as a GitHub Actions workflow; add ANTHROPIC_API_KEY / OPENAI_API_KEY to repo secrets; use potproject/code-agent@main in a workflow YAML triggered on issues/issue_comment/pull_request_review_comment"
docs_url: "https://github.com/marketplace/actions/github-code-agent"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/potproject/code-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Bridges Claude Code and Codex into GitHub workflows via slash commands (/claude, /codex) in issue/PR comments; automatically creates PRs or commits from AI-suggested changes and posts AI output as a comment when no code changes; checks user permissions and masks sensitive information in outputs."
---

Bridges Claude Code and Codex into GitHub workflows via slash commands (/claude, /codex) in issue/PR comments; automatically creates PRs or commits from AI-suggested changes and posts AI output as a comment when no code changes; checks user permissions and masks sensitive information in outputs.
