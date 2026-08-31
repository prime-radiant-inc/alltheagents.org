---
name: "code-review"
slug: "code-review"
layout: "agent.njk"
category: "other"
maker: "gemini-cli-extensions"
license: "Apache-2.0"
url: "https://github.com/gemini-cli-extensions/code-review"
source_code_url: "https://github.com/gemini-cli-extensions/code-review"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-09-09"
current_release: "2026-03-10"
stars: "531"
language: "Markdown / Gemini CLI extension definitions"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Google"
pricing: "free"
install_method: "gemini extensions install https://github.com/gemini-cli-extensions/code-review"
docs_url: "https://github.com/google-gemini/gemini-cli/blob/main/docs/extensions/index.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Gemini CLI extension built by the authors of the Gemini Code Assist GitHub App; integrates AI-powered code review directly into the Gemini CLI for both branch changes and pull requests via /code-review and /pr-code-review commands. PR review requires the GitHub MCP server."
---

The extension ports the review behavior of Google's Code Assist GitHub app into a local Gemini CLI session, so developers get review feedback on their working branch before pushing. The /code-review command analyzes changes on the current branch, while /pr-code-review pulls a specified GitHub pull request through the GitHub MCP server and reviews it in place, accepting repository and PR identifiers via arguments or the REPOSITORY and PULL_REQUEST_NUMBER environment variables. It is installed with the Gemini CLI extension command and requires Gemini CLI v0.4.0 or newer, running entirely within the user's existing Gemini CLI setup rather than as a separate product. It targets developers already using Gemini CLI who want review feedback on branch diffs and pull requests without leaving the terminal.
