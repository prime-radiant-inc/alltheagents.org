---
name: "Yeoman"
slug: "yeoman"
layout: "agent.njk"
category: "other"
maker: "yeoman"
license: "BSD"
url: "https://github.com/yeoman/yeoman"
source_code_url: "https://github.com/yeoman/yeoman"
source_available: "True"
platforms: []
first_released: "2012-04-13"
current_release: "2022-10-18"
stars: "10101"
language: "JavaScript"
homepage: "http://yeoman.io"
mcp_support: "no"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None — scaffolding tool, no AI models"
pricing: "open-source"
install_method: "npm"
docs_url: "http://yeoman.io/learning"
plugin_docs_url: null
config_docs_url: null
download_url: "https://yeoman.io"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Traditional development workflow and scaffolding tool (not an AI agent). Robust, opinionated workflow with a wide ecosystem of generators to quickly bootstrap and automate web application scaffolding. Supports custom generators across the organization's repositories."
---

Yeoman is a long-established (pre-LLM) scaffolding ecosystem: a generator runner plus a workflow that bootstraps web applications from npm-published generator packages, with support for composing custom generators across an organization's repositories. It contains no AI or agent components; it is included in the census only as a boundary case marking what scaffolding looked like before agents. Its audience is web developers bootstrapping projects, and it remains mature but low-churn under the Google/BSD-licensed umbrella repo.
