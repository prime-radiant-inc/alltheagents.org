---
name: "zhin"
slug: "zhin"
layout: "agent.njk"
category: "other"
maker: "zhinjs"
license: "MIT"
url: "https://github.com/zhinjs/zhin"
source_code_url: "https://github.com/zhinjs/zhin"
source_available: "True"
platforms: []
first_released: "2022-08-17"
current_release: "2026-08-19"
stars: "135"
language: "TypeScript"
homepage: "http://zhin.js.org/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: "True"
plan_mode: null
model_providers: "OpenAI, AI SDK vendor packages"
pricing: "Free (MIT)"
install_method: "npm create zhin-app my-bot -y; or pnpm add zhin.js + adapter"
docs_url: "https://zhin.js.org"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/zhin.js"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "AI-native TypeScript bot framework for building bots/assistants on 20+ chat platforms (QQ, WeChat, Discord, Telegram, Slack, etc.) with multi-account support and opt-in AI agent capabilities"
---

zhin.js is a framework for building bots that live on instant-messaging platforms, and its design treats multi-platform reach as the primary problem: one TypeScript codebase, with adapters targeting more than twenty services including QQ, WeChat, Discord, Telegram, Slack, and DingTalk, packaged as a core library under 10MB. Applications are composed from file-convention plugins — commands, tools, and agent skills declared in directories and hot-reloaded on change — plus declarative APIs for adapters and commands, managed remotely through a browser console. The project positions AI deliberately: a plain install is a conventional IM framework, and agent capability arrives only by adding the @zhin.js/agent package alongside an AI SDK provider, at which point the bot gains chat, tools, memory, sessions, orchestration, and security policies such as bash allowlists and approval modes. MCP client support exists as a further opt-in tier, and LLM calls ride Vercel AI SDK providers. The README draws an explicit boundary — this is not a Cursor- or Claude Code-style coding agent — which is why it lands outside the agent harness category despite the agentic add-on. Its audience is bot developers, particularly in the Chinese IM ecosystem, who want a maintainable framework that can grow agent features into an existing bot rather than the reverse.
