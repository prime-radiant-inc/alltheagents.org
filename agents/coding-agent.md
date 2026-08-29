---
name: "coding-agent"
slug: "coding-agent"
layout: "agent.njk"
category: "agent"
maker: "embabel"
license: "Apache-2.0"
url: "https://github.com/embabel/coding-agent"
source_code_url: "https://github.com/embabel/coding-agent"
source_available: "True"
platforms: []
first_released: "2025-05-15"
current_release: "2026-03-20"
stars: "58"
language: "Kotlin, Java"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI (via the Embabel agent platform's model abstraction)"
pricing: "Free/open source"
install_method: "Run via shell; finds Maven projects under peer directories of the startup directory"
docs_url: "https://github.com/embabel/coding-agent#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/embabel/coding-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Headless coding agent built on the Embabel agent platform; aims to accelerate development with AI without using any commercial coding agents; explains code, creates projects, multi-file changes, writes docs, combines project code access with internet access for API research."
---

The Embabel team wanted a coding agent for JVM codebases without adopting a commercial product, and built one on their own agent platform as both a tool and a demonstration of the platform. The headless agent discovers Maven projects under peer directories of its startup directory and handles code explanation, new project creation, multi-file edits, documentation writing, and combinations of local code access with internet research such as API investigation. Shell commands provide focus management - pointing the agent at a named project - and a chat mode exists without conversational memory yet. The project is early stage with a roadmap covering non-Maven builds, token reduction, and automated PR review. JVM developers who want an agent in their native ecosystem, and Embabel platform users, are the audience.
