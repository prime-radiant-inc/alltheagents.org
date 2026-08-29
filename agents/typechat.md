---
name: "TypeChat"
slug: "typechat"
layout: "agent.njk"
category: "other"
maker: "microsoft"
license: "MIT"
url: "https://github.com/microsoft/TypeChat"
source_code_url: "https://github.com/microsoft/TypeChat"
source_available: "True"
platforms: []
first_released: "2023-06-20"
current_release: "2026-08-19"
stars: "8680"
language: "TypeScript, Python, C#"
homepage: "https://microsoft.github.io/TypeChat/"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI, and OpenAI-compatible endpoints"
pricing: "open-source"
install_method: "npm"
docs_url: "https://microsoft.github.io/TypeChat"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/typechat"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Library (not a coding agent) that replaces prompt engineering with schema engineering. Developers define TypeScript types representing application intents; TypeChat constructs prompts using these types, validates LLM responses against the schema, repairs non-conforming outputs, and summarizes results. Eliminates complex decision trees and fragility of traditional prompt engineering. Available in TypeScript, Python, and C#/.NET."
---

TypeChat exists because wiring natural-language input to application actions through prompt engineering grows fragile as intents multiply. The library inverts the approach: the developer declares intents as TypeScript types (discriminated unions, meta-schemas), and TypeChat constructs prompts from those types, validates each model response against the schema, and drives repair loops with the model when validation fails before returning a typed instance the application can dispatch on. A final programmatic summarization step confirms the parsed intent matches what the user asked, without another model call. Teams building chat interfaces over existing APIs use it for intent routing and command parsing rather than autonomous agent loops; it is MIT-licensed, installable via npm, and maintained at a reduced pace by Microsoft.
