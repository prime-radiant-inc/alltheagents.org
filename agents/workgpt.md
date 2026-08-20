---
name: "WorkGPT"
slug: "workgpt"
layout: agent.njk
category: agent
maker: "team-openpm"
license: "MIT"
url: "https://github.com/team-openpm/workgpt"
source_code_url: "https://github.com/team-openpm/workgpt"
source_available: "Yes"
platforms:
  - "Web"
first_released: "2023-05-02"
current_release: "2023-06-23"
stars: 731
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: null
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: null
sources:
  - "e2b"
---

- WorkGPT is an agent framework in a similar fashion to AutoGPT or LangChain. You give it a directive and an array of APIs and it will converse back and forth with the AI until its directive is complete. - For example, a directive could be to research the web for something, to crawl a website, or to order you an Uber. We support any and all APIs that can be represented with an OpenAPI file. - WorkGPT now has OpenAI's new function invocation feature baked into it - While chaining together APIs was possible before (see AutoGPT), it was slow, expensive, and error prone - [The tweet announcing this feature](https://twitter.com/maccaw/status/1669367224694607875)
