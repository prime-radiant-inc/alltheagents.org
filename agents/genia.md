---
name: "GeniA"
slug: "genia"
layout: "agent.njk"
category: "agent"
maker: "genia-dev"
license: "Apache-2.0"
url: "https://github.com/genia-dev/GeniA"
source_code_url: "https://github.com/genia-dev/GeniA"
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: "2023-07-24"
current_release: "2023-11-22"
stars: "409"
language: "Python"
homepage: "https://genia-dev.github.io/GeniA/"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure"
pricing: "Free / open-source (requires your own OpenAI API Key)"
install_method: "pip3 install streamlit genia, then run genia; also available as Docker container"
docs_url: "https://genia-dev.github.io/GeniA/"
plugin_docs_url: "https://genia-dev.github.io/GeniA/add-new-tool/"
config_docs_url: null
download_url: "https://github.com/genia-dev/GeniA"
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "AI platform engineering team member that works alongside you in production environments via Slack integration; built on OpenAI function-calling; covers DevOps, SRE, SecOps, FinOps scenarios; 100% open source and expandable with custom tools"
---

GeniA puts an LLM agent into the Slack channel a platform team already uses, so operational work — deployments to Kubernetes or Argo, incident troubleshooting, log summarization, FinOps and SecOps checks — happens by conversation in the channel rather than in a separate console. It is built on OpenAI and Azure function calling, predating the MCP ecosystem, and the tool layer is deliberately open: teams teach it new capabilities through a documented add-new-tool path. It installs with pip and a Streamlit front end or runs containerized against a Slack workspace, configured through a .env template with the team's OpenAI or Azure keys. Activity effectively stopped with its 2023 releases, leaving 409 stars and an MkDocs site as the record of what it did.
