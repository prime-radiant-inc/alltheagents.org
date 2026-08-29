---
name: "DeepCopilot"
slug: "deepcopilot"
layout: "agent.njk"
category: "agent"
maker: "deep-copilot"
license: "MIT"
url: "https://github.com/deep-copilot/DeepCopilot"
source_code_url: "https://github.com/deep-copilot/DeepCopilot"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-05-09"
current_release: "2026-08-11"
stars: "78"
language: "JavaScript"
homepage: "https://marketplace.visualstudio.com/items?itemName=ZhouChaunge.deep-copilot"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "True"
plan_mode: "True"
model_providers: "DeepSeek"
pricing: null
install_method: "VS Code Marketplace (search 'Deep Copilot'); from VSIX: code --install-extension deep-copilot-0.41.6.vsix; from source: npm install && npm run build && npm run package"
docs_url: "https://github.com/deep-copilot/DeepCopilot"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=ZhouChaunge.deep-copilot"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "VS Code extension providing a conversational AI coding assistant powered by the DeepSeek API with an agentic loop, multi-turn tool calling, and streaming output in the sidebar. Features file tools (read/write/str-replace/apply_patch/list/find/grep), shell execution, web search via Tavily, plan & todos panel, revert last turn, post-tool hooks (.deepcopilot/hooks.json), post-edit LSP diagnostics, parallel sessions, MCP client (mcp__<server>__<tool>), skills system (compatible with ~/.claude/skills, ~/.copilot/skills), inline FIM completions, approval modes, and cost telemetry. No TypeScript, no runtime npm dependencies."
---

DeepCopilot puts a DeepSeek-powered coding agent into VS Code's sidebar: a multi-turn tool-calling loop handles file reads/writes, ripgrep-backed code search, shell execution, and optional Tavily web search, with streaming output and context-window management to stay inside long sessions. The extension deliberately avoids npm runtime dependencies, shipping a small bundle built on the VS Code Extension API, which keeps install weight and supply-chain surface minimal. Around the loop it adds plan/todo tracking, a pending-edits panel with diff review and one-click revert, persistent user memory, a skills system, and FIM inline completions. It requires a DeepSeek API key (Tavily optional), is MIT-licensed JavaScript by a solo author, and releases frequently on the VS Code Marketplace.
