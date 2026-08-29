---
name: "HuiCai AI"
slug: "huicai-ai"
layout: "agent.njk"
category: "agent"
maker: "ChenBo"
license: "Proprietary (EULA)"
url: "https://plugins.jetbrains.com/plugin/32855-huicai-ai"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2026-08-14"
current_release: null
stars: null
language: null
homepage: null
mcp_support: "True"
plugin_support: "yes"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "HuiCai platform models (browser/device-code login shared across CLI, VS Code, and IDE)"
pricing: "subscription"
install_method: "Install from the JetBrains Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/32855-huicai-ai"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "JetBrains edition of the HuiCai AI assistant with agent core"
---

HuiCai AI's JetBrains edition exists so users of the HuiCai assistant get the same agent core across VSCode, CLI, and IDE without separate accounts or behavior. The plugin embeds a chat tool window backed by a local Node.js process: file edits pass through inline diff review inside the editor, commands run on the local machine, and sub-agents can be dispatched in hybrid mode combining platform orchestration with local tools. Streaming replies show reasoning traces, tool-call progress, and task lists, and document uploads (PDF, Word, Excel, PPT) are parsed server-side into context. It targets Chinese-speaking teams that want one agent core synced with a platform knowledge base and business digital-human workflows.
