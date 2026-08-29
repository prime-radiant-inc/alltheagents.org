---
name: "PR-Agent"
slug: "pr-agent"
layout: "agent.njk"
category: "agent"
maker: "The-PR-Agent"
license: "MIT"
url: "https://github.com/Codium-ai/pr-agent"
source_code_url: "https://github.com/Codium-ai/pr-agent"
source_available: "True"
platforms: []
first_released: "2023-07-05"
current_release: "2026-08-19"
stars: "12623"
language: "Python"
homepage: "https://www.pr-agent.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google Gemini, DeepSeek, Mistral, LiteLLM (Azure OpenAI, AWS Bedrock, Vertex AI, Databricks, OpenRouter, Ollama)"
pricing: "open-source"
install_method: "pip"
docs_url: "https://docs.pr-agent.ai/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Codium-ai/pr-agent"
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "AI-powered PR review agent where each tool uses a single LLM call for low cost (~30s). Platform-agnostic across 5 git providers (GitHub, GitLab, Bitbucket, Azure DevOps, Gitea). JSON-based customizable prompting. Automatically picks up AGENTS.md repo context and SKILL.md agent skills. PR compression strategy handles PRs of any size."
---

PR-Agent popularized AI pull-request review as a category, and its design remains distinctive: rather than an autonomous multi-step agent, each command makes one targeted LLM call against a compressed view of the PR, keeping responses fast and cheap enough to run on every pull request. Comment commands like /describe, /review, and /improve work identically on GitHub, GitLab, Bitbucket, Azure DevOps, and Gitea, with TOML configuration and JSON-based prompt customization for teams that need to tune behavior. Token-aware PR compression handles large diffs that would otherwise blow context limits, and a broad LiteLLM-based provider list means it runs against OpenAI, Anthropic, DeepSeek, or self-hosted models. Since Qodo donated the project it is community-maintained, with an external maintainer and a pending foundation transfer. Teams adopt it as the low-cost, platform-agnostic baseline for automated PR review, and its open-source core underpins Qodo's commercial offering.
