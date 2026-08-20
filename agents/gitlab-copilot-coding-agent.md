---
name: "gitlab-copilot-coding-agent"
slug: "gitlab-copilot-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "satomic"
license: null
url: "https://github.com/satomic/gitlab-copilot-coding-agent"
source_code_url: "https://github.com/satomic/gitlab-copilot-coding-agent"
source_available: True
platforms:
  - "CLI"
first_released: "2025-11-20"
current_release: "2025-12-11"
stars: "41"
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: True
plan_mode: True
model_providers: "GitHub Copilot"
pricing: null
install_method: "Import repo to GitLab via Git URL, configure CI/CD variables, deploy webhook service via Docker (satomic/gitlab-copilot-coding-agent-hook:latest) or from source (python3 main.py)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/satomic/gitlab-copilot-coding-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Bridges GitHub Copilot CLI with GitLab CI/CD for fully autonomous coding workflows. Issue assignment triggers automated implementation with MR creation, MR comments trigger code updates, and MR reviewer assignment triggers intelligent comprehensive code review — all without leaving GitLab. Flask webhook service captures GitLab events."
---

Bridges GitHub Copilot CLI with GitLab CI/CD for fully autonomous coding workflows. Issue assignment triggers automated implementation with MR creation, MR comments trigger code updates, and MR reviewer assignment triggers intelligent comprehensive code review — all without leaving GitLab. Flask webhook service captures GitLab events.
