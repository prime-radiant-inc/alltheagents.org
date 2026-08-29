---
name: "Gpt-Code-Assistant"
slug: "gpt-code-assistant"
layout: "agent.njk"
category: "other"
maker: "narenmanoharan"
license: "Apache-2.0"
url: "https://github.com/narenmanoharan/gpt-code-assistant"
source_code_url: "https://github.com/narenmanoharan/gpt-code-assistant"
source_available: "True"
platforms: []
first_released: "2023-06-23"
current_release: "2023-08-08"
stars: "208"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: "False"
model_providers: "OpenAI"
pricing: "Free / open-source"
install_method: "pip install gpt-code-assistant"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/gpt-code-assistant/"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Privacy-centric CLI for exploring/querying codebases via LLMs and vector embeddings; only sends code snippets to OpenAI when a query requires them. Uses GPT-4 to autonomously retrieve the most relevant local code snippets; terminal-only with no UI; language-agnostic."
---

The tool indexes a local codebase into vector embeddings and lets developers ask natural-language questions in the terminal, with GPT-4 retrieving the most relevant snippets and sending only those snippets to OpenAI, minimizing code exposure. It is terminal-only and language-agnostic, aimed at developers exploring unfamiliar or large codebases, generating documentation, or asking debugging questions without uploading their whole repository. Indexing happens locally, and only query-dependent snippets leave the machine, a deliberate design for proprietary codebases. The project saw 86 commits through August 2023 and then went quiet; it stands as an early example of retrieval-grounded code assistants, pre-dating the current agent wave.
