---
name: "WorkGPT"
slug: "workgpt"
layout: "agent.njk"
category: "agent-sdk"
maker: "team-openpm"
license: "MIT"
url: "https://github.com/team-openpm/workgpt"
source_code_url: "https://github.com/team-openpm/workgpt"
source_available: "yes"
platforms:
  - "Web"
first_released: "2023-05-02"
current_release: "2023-06-23"
stars: "731"
language: "TypeScript"
homepage: "https://github.com/team-openpm/workgpt"
mcp_support: "no"
plugin_support: "partial"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI"
pricing: "open-source"
install_method: "npm"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/workgpt"
maintained: "dormant"
sources:
  - "e2b"
what_makes_it_special: "Agent framework (AutoGPT/LangChain-style) that takes a directive and an array of APIs, then converses with AI until the directive is complete. Universal API support via OpenAPI files and OpenPM packages. Smart authentication (pass an authKey, library figures out authorization). Includes Puppeteer-based web crawling and Zod-schema-based structured data extraction. Maintained status unclear from README."
---

WorkGPT is an AutoGPT/LangChain-era agent framework (2023, TypeScript/Node) that takes a directive and a set of APIs and converses with the model until the directive is complete. Its differentiator is universal API support: any API describable by an OpenAPI file can be invoked, packaged through OpenPM (a package manager for OpenAPI files), with smart authentication where passing an authKey lets the library figure out authorization. Execution runs through a WorkGptRunner loop with invokable API classes carrying Zod schemas, including a Puppeteer-based text browser. It is MIT-licensed, npm-published, and effectively dormant: 34 commits, no releases, and no ongoing development. It was aimed at developers prototyping agent flows against REST APIs in the AutoGPT era.
