---
name: "coderabbit-review-helper"
slug: "coderabbit-review-helper"
layout: "agent.njk"
category: "other"
maker: "obra"
license: "MIT"
url: "https://github.com/obra/coderabbit-review-helper"
source_code_url: "https://github.com/obra/coderabbit-review-helper"
source_available: "True"
platforms: []
first_released: "2025-09-06"
current_release: "2025-09-11"
stars: "54"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: null
pricing: "Free / open-source"
install_method: "Clone repo + pip install --user beautifulsoup4; run ./extract-coderabbit-feedback.py owner/repo/123"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "github_topic4"
what_makes_it_special: "Converts CodeRabbit GitHub PR reviews into clean, LLM-friendly text formatted for AI coding agents to automatically apply suggestions; prioritizes AI-actionable items and organizes feedback by file."
---

CodeRabbit posts rich, structured review comments on pull requests, but their format — HTML, nested threads, interleaved nitpicks and substantive findings — is awkward for AI coding agents to consume. This script pulls a PR's CodeRabbit comments through the GitHub CLI, strips HTML, groups feedback by file, and reorders it so AI-actionable prompts come before informational diffs, emitting plain text suitable for piping into Claude, ChatGPT, or another agent. It is a single Python file depending only on beautifulsoup4 and an authenticated gh CLI, with no published package: users clone the repository and run the script directly. The project dates from September 2025 and has seen only light, occasional maintenance since.
