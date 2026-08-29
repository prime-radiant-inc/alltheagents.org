---
name: "cody-public-snapshot"
slug: "cody-public-snapshot"
layout: "agent.njk"
category: "agent"
maker: "sourcegraph"
license: "Apache-2.0"
url: "https://github.com/sourcegraph/cody-public-snapshot"
source_code_url: "https://github.com/sourcegraph/cody-public-snapshot"
source_available: "Yes"
platforms: []
first_released: "2023-07-10"
current_release: "2025-08-01"
stars: "3806"
language: "TypeScript"
homepage: "https://cody.dev"
mcp_support: null
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, Google, Mixtral"
pricing: "freemium"
install_method: "vscode"
docs_url: "https://sourcegraph.com/docs/cody"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/sourcegraph/cody-public-snapshot"
maintained: "dead"
sources:
  - "github_deep"
what_makes_it_special: "AI coding assistant by Sourcegraph that uses deep codebase context via semantic search for chat, autocomplete, and inline edits; this repo is a public snapshot taken before the main Cody repo went private."
---

When Sourcegraph moved Cody development into a private repository in 2025, roughly 6,150 commits of extension, agent, and CLI development disappeared from public view. This snapshot preserves the codebase exactly as it stood at that boundary, complete with a note marking the final commit made under the Apache-2.0 license. The code covers the VS Code and JetBrains extensions, the Cody agent, and the CLI, along with their integrations with Sourcegraph's search backend and multiple LLM providers. GitHub archived the repository on August 1, 2025, and it receives no further commits. Developers studying how a production coding assistant was built, and anyone forking the last open code, use this snapshot; current Cody development is private.
