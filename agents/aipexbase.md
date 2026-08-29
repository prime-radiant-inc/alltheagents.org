---
name: "aipexbase"
slug: "aipexbase"
layout: "agent.njk"
category: "other"
maker: "kuafuai"
license: "Apache-2.0"
url: "https://github.com/kuafuai/aipexbase"
source_code_url: "https://github.com/kuafuai/aipexbase"
source_available: "True"
platforms: []
first_released: "2025-10-18"
current_release: "2026-08-13"
stars: "1281"
language: "Java, Vue 3"
homepage: "https://www.codeflying.app"
mcp_support: "yes"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "docker"
docs_url: "https://vvx03gck2p.feishu.cn/wiki/LCDZwmer8iPNhZkKKJpcxp78nKd"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "AI-native Backend-as-a-Service (BaaS) that eliminates backend code writing — 'Frontend-as-Backend' architecture lets developers focus only on frontend/business logic. Native MCP compatibility for direct AI agent invocation of backend capabilities. Deep Chinese ecosystem support (Feishu, DingTalk, WeChat, HarmonyOS, mini-programs)."
---

The premise is that AI coding tools make frontend work fast while backend plumbing remains the bottleneck, so the platform eliminates backend code: deploy the Spring Boot service via Docker Compose, connect your agent through SDK or MCP, and storage, authentication, and third-party AI calls are handled as infrastructure. A unified context and data layer gives agents long-term memory and traceable state across sessions. The companion CodeFlying hosted platform commercializes the same stack, while the open-source repo (Java Spring Boot backend, Vue 3 console, Apache-2.0) targets self-hosters, with docker-compose install and a Feishu wiki as documentation. Adopted largely in the Chinese ecosystem (1.3k stars), it positions itself as Supabase for the agent era.
