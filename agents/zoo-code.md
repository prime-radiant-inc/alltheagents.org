---
name: "Zoo-Code"
slug: "zoo-code"
layout: "agent.njk"
category: "agent"
maker: "Zoo-Code-Org"
license: "Apache-2.0"
url: "https://github.com/Zoo-Code-Org/Zoo-Code"
source_code_url: "https://github.com/Zoo-Code-Org/Zoo-Code"
source_available: "True"
platforms:
  - "IDE"
first_released: "2026-04-23"
current_release: "2026-08-19"
stars: "1660"
language: "TypeScript (VS Code extension)"
homepage: "https://www.zoocode.dev"
mcp_support: "yes - per-mode MCP restrictions"
plugin_support: "yes - VS Code extension marketplace"
claude_code_plugin: "no - standalone VS Code extension"
subagents: "yes - orchestrator workflows with parent/child task coordination, parallel subtasks"
hooks: "no"
plan_mode: "yes - Architect Mode"
model_providers: "Claude, GPT, Gemini, Kimi, GLM, Grok, MiniMax, DeepSeek, Qwen, Azure OpenAI, Zoo Gateway, Moonshot, NanoGPT, Friendli, Kenari, OpenCode Go"
pricing: "open-source"
install_method: "vscode"
docs_url: "https://docs.zoocode.dev"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Community-driven continuation of Roo Code after the original Roo team moved to Roomote. AI-powered VS Code extension providing a team of AI agents in-editor, with Semble codebase intelligence (on-demand semantic code search), Destructive Command Guard (DCG) for longer autonomous runs, multiple modes (Code, Architect, Ask, Debug, custom), and very broad model provider support."
---

Zoo Code exists because Roo Code, one of the most widely used open-source AI coding extensions, stopped receiving active maintenance when its core team shifted to a product called Roomote. Rather than let the codebase stagnate, contributors who had worked on Roo forked it and continued development, publishing a Roo-to-Zoo migration guide so existing users could move over with their settings and workflows intact — which is why the repository carries over 7,500 commits of inherited history. The extension retains Roo's mode system: Code mode for edits, Architect mode for planning and spec work before implementation, Ask and Debug modes, and user-defined custom modes that constrain the agent's behavior per context. Because the lineage traces back through Cline, the tooling includes MCP server integration with per-mode restrictions, an orchestrator mode that delegates parent and child tasks across parallel subtasks, and explicit approval gates before consequential actions. The fork's distinctive additions target autonomous operation: a Destructive Command Guard blocks dangerous shell commands during long unattended runs, and Semble adds on-demand semantic code search without a separate indexing pass. Provider coverage is broad — Claude, GPT, Gemini, Kimi, GLM, Grok, MiniMax, DeepSeek, Qwen, and multiple gateways — and the project publishes docs at docs.zoocode.dev under Apache-2.0. Teams that built workflows on Roo use it as the continuity path.
