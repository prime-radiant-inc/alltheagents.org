---
name: "Rovo Dev"
slug: "rovo-dev"
layout: "agent.njk"
category: "agent"
maker: "Atlassian"
license: null
url: "https://www.atlassian.com/software/rovo-dev"
source_code_url: null
source_available: null
platforms:
  - "CLI"
first_released: null
current_release: null
stars: null
language: null
homepage: "https://www.atlassian.com/software/rovo-dev"
mcp_support: "yes"
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "freemium"
install_method: "Rovo Dev CLI via the Atlassian CLI (acli); Atlassian extension for VS Code; built into Bitbucket Cloud and GitHub integrations"
docs_url: "https://support.atlassian.com/rovo/docs/work-with-rovo-dev-agents/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Atlassian coding agent (CLI + Jira/Bitbucket integration) built on Teamwork Graph"
---

Rovo Dev exists because Atlassian customers already keep requirements, reviews, and deploy state in Jira, Bitbucket, and GitHub, and an agent that cannot see that context plans against stale assumptions. The CLI brings the agent to the terminal, the VS Code extension into the editor, and SCM integrations into pull-request review, where it flags regressions and checks work against the linked ticket's acceptance criteria. Underlying models are third-party (OpenAI, Anthropic) under zero-data-retention agreements, with access governed by existing Atlassian permissions and admins able to deactivate the agent org-wide. Packaging is freemium: monthly credits roll out to Jira Standard, Premium, and Enterprise customers, with a paid Rovo Dev Standard tier above that. Enterprise buyers are the audience, and the product carries SOC/ISO attestations though not HIPAA compliance or data residency.
