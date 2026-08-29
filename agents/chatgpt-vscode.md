---
name: "chatgpt-vscode"
slug: "chatgpt-vscode"
layout: "agent.njk"
category: "other"
maker: "ai-genie"
license: "ISC"
url: "https://github.com/ai-genie/chatgpt-vscode"
source_code_url: "https://github.com/ai-genie/chatgpt-vscode"
source_available: "True"
platforms:
  - "IDE"
first_released: "2023-03-20"
current_release: "2024-09-15"
stars: "1274"
language: "TypeScript"
homepage: "https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "n/a"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Azure OpenAI"
pricing: "BYOK"
install_method: "vscode"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=genieai.chatgpt-vscode"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "VS Code-native ChatGPT integration with conversation history stored on disk, quick-fix for compile-time errors in Problems window, inline diff view of AI suggestions, Azure OpenAI support, git commit message generation, streaming responses with stop capability, export of conversations to Markdown."
---

chatgpt-vscode (marketed as Genie) embedded OpenAI's models into Visual Studio Code via the user's own API key, arriving in early 2023 when editor integrations were still novel. Its feature set centered on the chat-and-suggest workflow of that era: sidebar conversations with history persisted to disk and exportable to Markdown, quick-fix prompts wired into the Problems window for compile-time errors, inline diffs of suggested changes, context-menu actions for generating tests or explanations, and automatic git commit message drafting. It supported Azure OpenAI deployments alongside standard OpenAI keys and included conveniences like stopping streamed responses to conserve tokens. The extension accumulated 1,274 stars and a marketplace following, but development effectively stopped after 2024, with the last release in September 2024 and a large backlog of unresolved issues; it has been overtaken by agentic assistants and now functions mainly as a legacy BYOK chat integration.
