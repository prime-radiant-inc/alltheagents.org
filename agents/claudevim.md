---
name: "claude.vim"
slug: "claudevim"
layout: "agent.njk"
category: "agent"
maker: "pasky"
license: "MIT"
url: "https://github.com/pasky/claude.vim"
source_code_url: "https://github.com/pasky/claude.vim"
source_available: "True"
platforms: []
first_released: "2024-06-27"
current_release: "2025-05-22"
stars: "471"
language: "Vim script"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, AWS Bedrock"
pricing: "free"
install_method: "git clone into Vim/Neovim pack directory"
docs_url: "https://github.com/pasky/claude.vim#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/pasky/claude.vim"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Deep Claude integration into the Vim/Neovim workflow — chat with full visibility of open buffers, vimdiff code review, tool use (open files, run vim/shell commands, evaluate Python, web search). Acts as a terminal-based replacement for Claude.ai/ChatGPT."
---

claude.vim was an early (2024) demonstration of editor-native agent tool use before IDE integrations matured: rather than code completion, it offers chat where the model sees every open buffer and can act - opening files, running commands, evaluating Python - with each action individually consented. Changes arrive as vimdiff review rather than silent rewrites, and chat history is editable, letting users redact expensive context. About 95% of the plugin's own code was written by Claude through the plugin itself. Development has been intermittent, with the last commit in May 2025 updating defaults to Sonnet 4; it remains MIT-licensed and installable from source.
