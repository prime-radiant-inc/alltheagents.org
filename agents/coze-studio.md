---
name: "coze-studio"
slug: "coze-studio"
layout: "agent.njk"
category: "other"
maker: "coze-dev"
license: "Apache-2.0"
url: "https://github.com/coze-dev/coze-studio"
source_code_url: "https://github.com/coze-dev/coze-studio"
source_available: "Yes"
platforms: []
first_released: "2025-06-26"
current_release: "2026-07-29"
stars: "21475"
language: "Go (backend), TypeScript (frontend)"
homepage: null
mcp_support: "partial (.mcp.json file present; transport not documented)"
plugin_support: "yes"
claude_code_plugin: "partial (.claude/agents dir and CLAUDE.md present)"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Volcengine (extensible)"
pricing: "open-source (Apache 2.0); commercial version available"
install_method: "docker"
docs_url: "https://www.coze.cn/open/docs"
plugin_docs_url: "https://github.com/coze-dev/coze-studio/wiki/4.-Plugin-Configuration"
config_docs_url: "https://github.com/coze-dev/coze-studio/wiki/3.-Model-configuration"
download_url: "https://github.com/coze-dev/coze-studio/releases"
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "All-in-one visual AI agent development platform derived from ByteDance's Coze platform, offering no-code/low-code agent building with workflows, plugins, knowledge bases, and RAG in a microservice architecture built with DDD principles."
---

Teams building LLM assistants for support, operations, or internal tools rarely want to write agent infrastructure themselves, and ByteDance's commercial Coze platform was closed. Coze Studio releases the platform's core engine under Apache-2.0 for self-hosting: agents are assembled visually from prompt-engineering surfaces, plugins, knowledge bases, RAG pipelines, databases, and drag-and-drop workflows, running on a Go microservice backend built on the Eino and FlowGram frameworks. Deployment runs through Docker Compose or Helm, and finished agents ship via OpenAPI or a Chat SDK embedded in other products. Model configuration covers OpenAI and Volcengine among others, and a commercial tier exists for features the open-source core excludes. Product and operations teams building conversational agents - not developers writing code with agents - are its users.
