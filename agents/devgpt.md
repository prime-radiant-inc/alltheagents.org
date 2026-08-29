---
name: "DevGPT"
slug: "devgpt"
layout: "agent.njk"
category: "agent"
maker: "jina-ai"
license: "Apache-2.0"
url: "https://github.com/jina-ai/dev-gpt"
source_code_url: "https://github.com/jina-ai/dev-gpt"
source_available: "Yes"
platforms:
  - "IDE"
first_released: "2023-03-17"
current_release: "2023-08-01"
stars: "1868"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "paid"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/dev-gpt"
maintained: "dormant"
sources:
  - "e2b"
what_makes_it_special: "An automated AI development team (Product Manager, Developer, DevOps) that generates, tests, builds, and deploys microservices from natural language descriptions, iteratively trying multiple implementation strategies and auto-deploying to Jina Cloud with a Streamlit playground."
---

Dev-GPT treats a microservice request as a handoff across a virtual product manager, developer, and DevOps agent: the PM turns a description into a spec, the developer writes and debugs the code against tests, and the DevOps stage produces a Docker image with an optional hosted endpoint. When an implementation fails its checks, the loop retries alternative approaches rather than surfacing errors to the user. Generated services can include web-search capability via Google Custom Search, and a UI mode renders the result as a running app. It was one of the earliest end-to-end 'describe, deploy' demos from 2023; development stopped that same year, and users today would treat it as a reference implementation.
