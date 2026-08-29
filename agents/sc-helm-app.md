---
name: "Sc-Helm-App"
slug: "sc-helm-app"
layout: "agent.njk"
category: "other"
maker: "amsilf"
license: null
url: "https://github.com/amsilf/sc-helm-app"
source_code_url: "https://github.com/amsilf/sc-helm-app"
source_available: "Yes"
platforms: []
first_released: "2024-07-12"
current_release: "2024-07-16"
stars: null
language: "Python"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (ChatGPT)"
pricing: "open-source"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/amsilf/sc-helm-app"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Combines Helm deployment with OPA policy verification and AI-assisted auto-remediation: detects policy violations, applies ChatGPT-suggested fixes, creates a new branch, and opens a pull request — automating the full fix workflow."
---

The repository is an educational reference for wiring policy-as-code into AI-assisted remediation rather than a tool anyone installs. Its pieces are minimal: a Hello-World Nginx Helm chart, Rego policies, a shell script that converts violations to JSON, and an Azure pipeline that calls the OpenAI API with them, then pushes the suggested fix as a branch and PR for human review. Prerequisites are Helm 3, OPA, Python 3, and an OpenAI API key, and the README is the only documentation. There is no license file, no releases, and effectively no adoption (zero stars), with the last meaningful activity some time ago. It is best read as a pattern to copy — policy violation to LLM-suggested patch to reviewable PR — not as software to depend on.
