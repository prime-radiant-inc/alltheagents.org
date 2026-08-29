---
name: "InfCode"
slug: "infcode"
layout: "agent.njk"
category: "agent"
maker: "Tokfinity"
license: "MIT"
url: "https://github.com/Tokfinity/InfCode"
source_code_url: "https://github.com/Tokfinity/InfCode"
source_available: "True"
platforms: []
first_released: "2025-10-29"
current_release: "2025-11-25"
stars: "62"
language: "Python"
homepage: "https://www.tokfinity.com/infcode"
mcp_support: "no"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenAI, OpenRouter, DeepSeek, self-hosted"
pricing: "open-source"
install_method: "pip install -r requirements.txt (Python 3.12 recommended)"
docs_url: "https://www.tokfinity.com/infcode"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Tokfinity/InfCode"
maintained: "active"
sources:
  - "github_topic5"
what_makes_it_special: "Adversarial multi-agent Code Agent System using dual-agent adversarial refinement (Test Patch Generator + Code Patch Generator) that iteratively improve; achieved 79.4% on SWE-Bench Verified (SOTA)"
---

InfCode's thesis is that generation and verification should compete: a Test Patch Generator rewrites tests to expose remaining faults, and a Code Patch Generator must survive them, iterating until either side yields. Candidate patches are generated in parallel inside per-example Docker containers and ranked by a Patch Selector, with tools for file editing, ripgrep search, and bash execution. The system reports 79.4% on SWE-Bench Verified, which the team claims as SOTA at publication. Running it requires Docker for the image builder, Python 3.12, and API keys for OpenAI, OpenRouter, DeepSeek, or self-hosted endpoints. The repo is a small research artifact (17 commits) from Tokfinity's Code Research team and Beihang University.
