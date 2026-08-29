---
name: "Create-Actionsprs"
slug: "create-actionsprs"
layout: "agent.njk"
category: "other"
maker: "jhutchings1"
license: "MIT"
url: "https://github.com/jhutchings1/Create-ActionsPRs"
source_code_url: "https://github.com/jhutchings1/Create-ActionsPRs"
source_available: "True"
platforms: []
first_released: "2020-04-11"
current_release: "2023-04-18"
stars: "45"
language: "PowerShell"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "none"
pricing: "Free / open source"
install_method: "Clone repo, rename .env-example to .env with GitHub token, run ./Create-ActionsPRs.ps1"
docs_url: "https://github.com/jhutchings1/Create-ActionsPRs#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jhutchings1/Create-ActionsPRs"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Automates creation of PRs across many repos to install/update GitHub Actions workflows (e.g., CodeQL). Three targeting modes: all repos in an org via API, custom file list of repos, auto-detect CodeQL-eligible repos. NOTE: This is a GitHub Actions automation script, not an AI coding agent harness."
---

Before agents, keeping GitHub Actions workflows consistent across an organization meant repetitive manual PRs. Create-ActionsPRs automates that with a single PowerShell script: authenticate with a GitHub token, choose a targeting mode (every repo in an org via API, an explicit list of repositories, or all repos eligible for CodeQL using a bundled workflow file), and the script opens one pull request per repository installing or updating the workflow. It requires only PowerShell, git, the GitHub CLI, and a token with repo scope, and includes a ready-made CodeQL workflow for the third mode. The last meaningful development dates to 2023 and the repo is dormant, but security teams rolling out CodeQL at scale still fork it. It belongs in the census as 'other': classic automation that predates and contains no AI.
