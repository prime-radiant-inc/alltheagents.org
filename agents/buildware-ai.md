---
name: "buildware-ai"
slug: "buildware-ai"
layout: "agent.njk"
category: "agent"
maker: "mckaywrigley"
license: "MIT"
url: "https://github.com/mckaywrigley/buildware-ai"
source_code_url: "https://github.com/mckaywrigley/buildware-ai"
source_available: "True"
platforms: []
first_released: "2024-07-10"
current_release: "2024-09-28"
stars: "567"
language: "TypeScript"
homepage: "https://JoinTakeoff.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, OpenAI"
pricing: "open-source"
install_method: "source"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/mckaywrigley/buildware-ai"
maintained: "dormant"
sources:
  - "github_topic5"
what_makes_it_special: "Code instruction system where you provide a GitHub issue and it automatically generates an AI-coded Pull Request"
---

buildware-ai was a self-hostable precursor to today's commercial issue-to-PR agents: you gave it a GitHub issue and repository credentials, and it produced an AI-coded pull request through a webhook-driven pipeline built on Next.js, Drizzle ORM, and Anthropic/OpenAI APIs. Mckay Wrigley and Tyler Bruno built it as an open-source demonstration of the 'code instruction system' pattern, and its simplicity — clone, configure environment variables, deploy — made it a popular reference for teams wanting to run the loop themselves rather than pay a SaaS. The project gained 567 stars but stalled: the promised advanced guide, Linear integration, local mode, and team support were announced as coming soon in mid-2024 and never arrived, and open issues and PRs went unaddressed. It remains a useful historical snapshot of the issue-to-PR pattern, but it is unmaintained and unsuitable for production use.
