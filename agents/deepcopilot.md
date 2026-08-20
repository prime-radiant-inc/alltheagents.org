---
name: "DeepCopilot"
slug: "deepcopilot"
layout: "agent.njk"
category: "agent"
maker: "deep-copilot"
license: "MIT"
url: "https://github.com/deep-copilot/DeepCopilot"
source_code_url: "https://github.com/deep-copilot/DeepCopilot"
source_available: True
platforms:
  - "IDE"
first_released: "2026-05-09"
current_release: "2026-08-11"
stars: "78"
language: "JavaScript"
homepage: "https://marketplace.visualstudio.com/items?itemName=ZhouChaunge.deep-copilot"
mcp_support: True
plugin_support: True
claude_code_plugin: False
subagents: null
hooks: True
plan_mode: True
model_providers: "DeepSeek"
pricing: null
install_method: "VS Code Marketplace (search 'Deep Copilot'); from VSIX: code --install-extension deep-copilot-0.41.6.vsix; from source: npm install && npm run build && npm run package"
docs_url: "https://github.com/deep-copilot/DeepCopilot"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=ZhouChaunge.deep-copilot"
maintained: null
sources:
  - "github_topic"
what_makes_it_special: "VS Code extension providing a conversational AI coding assistant powered by the DeepSeek API with an agentic loop, multi-turn tool calling, and streaming output in the sidebar. Features file tools (read/write/str-replace/apply_patch/list/find/grep), shell execution, web search via Tavily, plan & todos panel, revert last turn, post-tool hooks (.deepcopilot/hooks.json), post-edit LSP diagnostics, parallel sessions, MCP client (mcp__<server>__<tool>), skills system (compatible with ~/.claude/skills, ~/.copilot/skills), inline FIM completions, approval modes, and cost telemetry. No TypeScript, no runtime npm dependencies."
---

VS Code extension providing a conversational AI coding assistant powered by the DeepSeek API with an agentic loop, multi-turn tool calling, and streaming output in the sidebar. Features file tools (read/write/str-replace/apply_patch/list/find/grep), shell execution, web search via Tavily, plan & todos panel, revert last turn, post-tool hooks (.deepcopilot/hooks.json), post-edit LSP diagnostics, parallel sessions, MCP client (mcp__<server>__<tool>), skills system (compatible with ~/.claude/skills, ~/.copilot/skills), inline FIM completions, approval modes, and cost telemetry. No TypeScript, no runtime npm dependencies.
