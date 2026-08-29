---
name: "aider-desk"
slug: "aider-desk"
layout: "agent.njk"
category: "agent"
maker: "hotovo"
license: "Apache-2.0"
url: "https://github.com/hotovo/aider-desk"
source_code_url: "https://github.com/hotovo/aider-desk"
source_available: "True"
platforms: []
first_released: "2025-01-07"
current_release: "2026-08-19"
stars: "1395"
language: "TypeScript/JavaScript (Electron + React 19 + Tailwind)"
homepage: "https://aiderdesk.hotovo.com"
mcp_support: "yes - both MCP client (connect to any MCP server) and MCP server (expose itself to Claude Desktop, Cursor)"
plugin_support: "yes - modular Extensions system (lifecycle hooks, custom tools, React UI injection) + IDE Connector Plugins for IntelliJ & VS Code"
claude_code_plugin: "no - Claude Desktop referenced as an MCP client target, not Claude Code"
subagents: "yes - delegate to specialized subagents with custom Agent Profiles (system prompts, boundaries)"
hooks: "yes - 30+ lifecycle hooks (onTaskCreated, onPromptFinished, onToolCalled, onFileAdded, etc.)"
plan_mode: null
model_providers: "30+ providers: OpenAI, Anthropic, Gemini, DeepSeek, Ollama, others"
pricing: "open-source"
install_method: "binary"
docs_url: "https://aiderdesk.hotovo.com/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Open-source agentic orchestration layer emphasizing Transparency (see every token, context file, proposed change), Control (tool approval gates, fork/duplicate tasks, edit chat history), and Flexibility (works alongside IDE/terminal/Git with no lock-in). Originally a GUI for the Aider CLI, now a full orchestration platform. Git worktrees give each task an isolated directory; built-in merge workflow. Fork tasks to explore alternatives; delete specific chat messages to keep context clean and prevent hallucinations. Deep extensibility: inject custom logic via lifecycle hooks, write custom TypeScript tools exposed to the AI, build custom React UI components in chat. Local-first privacy, no cloud. Smart Context Engine with vector embeddings (LanceDB) + semantic repo mapping."
---

AiderDesk began as an Electron front-end for the Aider CLI and evolved into a full coding platform: tasks with forkable context, git worktrees for isolated experiments, and a diff viewer that shows every proposed change before it lands. Tool approval gates require human authorization for risky operations, and token, cost, and usage dashboards make spending visible per task. An extension system exposes 30+ lifecycle events, custom tools, and React UI injection, with a gallery installable via npx @aiderdesk/extensions; IDE connectors exist for IntelliJ and VS Code. Teams that want agent automation with human checkpoints use it, with local-first storage (LanceDB) and 30+ model providers behind Apache-2.0 licensing.
