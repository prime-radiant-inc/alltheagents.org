---
name: "Cody (Sourcegraph)"
slug: "cody-sourcegraph"
layout: "agent.njk"
category: "agent"
maker: null
license: "Apache-2.0"
url: "https://sourcegraph.com/cody"
source_code_url: null
source_available: "True"
platforms:
  - "IDE"
  - "Web"
first_released: null
current_release: null
stars: null
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Multiple (Anthropic, OpenAI, Google, and others routed through Sourcegraph's infrastructure)"
pricing: "Free for individuals via Sourcegraph.com; included with Sourcegraph Enterprise (paid)"
install_method: "IDE extensions for VS Code, JetBrains, and Visual Studio; also available as Cody CLI and Cody Web (in Sourcegraph web app)"
docs_url: "https://sourcegraph.com/docs/cody"
plugin_docs_url: null
config_docs_url: null
download_url: "https://sourcegraph.com/cody"
maintained: "active"
sources:
  - "jim"
  - "caramaschi"
  - "vinkius"
what_makes_it_special: "AI code assistant that uses Sourcegraph's code search to pull context from local and remote codebases; available as IDE extensions (VS Code, JetBrains, Visual Studio), CLI, and web app; public source snapshot archived Aug 1, 2025 (development moved to a private repo)"
---

Code answers usually live outside the file a developer has open, which is the gap Sourcegraph built its search business on and Cody extends into an assistant. Chat with @-mentions reaches into files, symbols, and whole remote repositories through Sourcegraph's search index, auto-edit proposes contextual changes from the cursor, and context filters let teams exclude repositories the assistant should not see. The assistant ships as extensions for VS Code, JetBrains, and Visual Studio, plus a web app, a CLI, and an Enterprise distribution integrated with Sourcegraph Code Search. Individuals use it through Sourcegraph.com while enterprises deploy it against their own Sourcegraph instance. Privacy terms state that customer code is not used to train models. Teams already running Sourcegraph are its natural users.
