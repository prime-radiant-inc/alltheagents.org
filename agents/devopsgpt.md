---
name: "DevOpsGPT"
slug: "devopsgpt"
layout: "agent.njk"
category: "agent"
maker: "kuafuai"
license: "Apache-2.0 (modified, commercial SaaS restrictions)"
url: "https://github.com/kuafuai/DevOpsGPT"
source_code_url: "https://github.com/kuafuai/DevOpsGPT"
source_available: "True"
platforms: []
first_released: "2023-07-12"
current_release: "2024-08-14"
stars: "5965"
language: "Python"
homepage: "https://www.kuafuai.net"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "freemium"
install_method: "docker, source"
docs_url: "https://github.com/kuafuai/DevOpsGPT/blob/master/docs/DOCUMENT.md"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "e2b"
  - "jim"
what_makes_it_special: "Combines LLM with DevOps tools to automate the full software development lifecycle — clarifies natural-language requirements, generates interface docs, writes pseudocode, refines code, runs continuous integration, and releases software versions. Supports any development language and can extend existing code. Open-source self-hosted plus a cloud service (kuafuai.net) and Enterprise Edition."
---

DevOpsGPT addresses the gap between a written requirement and a deployed service by automating the whole chain: it interviews the user to pin down requirements, produces interface documentation, drafts pseudocode, refines it into working code in the project's language, and hands the result to CI/CD. An enterprise edition adds analysis of existing codebases, stronger domain models, and more DevOps platform integrations, aimed at enterprise teams whose bottleneck is requirement hand-off rather than typing speed. The open-source edition demonstrated the full pipeline against Java SpringBoot projects. Upstream development stopped in 2024, leaving the enterprise product as the maintained line.
