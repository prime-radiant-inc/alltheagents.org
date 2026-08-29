---
name: "Groq Code CLI"
slug: "groq-code-cli"
layout: "agent.njk"
category: "agent"
maker: "build-with-groq"
license: "MIT"
url: "https://github.com/build-with-groq/groq-code-cli"
source_code_url: "https://github.com/build-with-groq/groq-code-cli"
source_available: "yes"
platforms:
  - "CLI"
first_released: "2025-07-30"
current_release: "2025-12-19"
stars: "742"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Groq, OpenRouter (community fork)"
pricing: "open-source"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/groq-code-cli"
maintained: "active"
sources:
  - "jqueryscript"
  - "brad"
  - "ishandutta"
what_makes_it_special: "Intentionally minimal and hackable coding CLI — the antithesis of feature-rich CLIs. Designed as a blueprint/building block that developers modify directly (no plugin layer). Includes familiar CLI features (slash commands, tools, TUI). Leverages Groq's fast inference for rapid iteration. Invites developers to add their own slash commands, tools, and UI customizations."
---

groq-code-cli is a deliberately small coding agent published under Groq's build-with-groq organization, positioned as a starting point rather than a finished product. It provides an interactive TUI with file tools, slash commands, model switching across Groq's catalog, session token stats, and reasoning display, while omitting the plugin systems and permission layers found in larger agent CLIs. The codebase is intentionally small and documented — tools, commands, and UI live in clearly separated directories — and the README walks through adding tools, commands, and even renaming the binary, with a community OpenRouter fork showing the fork-and-extend workflow in practice. It is aimed at developers who want to understand or build a coding CLI rather than adopt a finished product, and Groq's low-latency inference keeps the edit-test loop fast.
