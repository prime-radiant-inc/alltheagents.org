---
name: "qwen_cli_coder"
slug: "qwen-cli-coder"
layout: "agent.njk"
category: "agent"
maker: "dinoanderson"
license: "Apache-2.0"
url: "https://github.com/dinoanderson/qwen_cli_coder"
source_code_url: "https://github.com/dinoanderson/qwen_cli_coder"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2025-06-29"
current_release: "2025-07-05"
stars: "60"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: null
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Qwen models via Alibaba Cloud DashScope"
pricing: "Free / open source (Apache-2.0)"
install_method: "Build from source: git clone, npm install, npm run build, npm run bundle, node bundle/qwen.js"
docs_url: "https://github.com/dinoanderson/qwen_cli_coder/blob/clean-main/docs/index.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/dinoanderson/qwen_cli_coder"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Community fork of Google's Gemini CLI modified to work with Qwen models from Alibaba Cloud; CLI AI workflow tool with dynamic MCP server management, multi-agent task coordination (spawn_sub_agent, delegate_task, aggregate_results; up to 5 concurrent agents), media generation (Wan models), and Assistant Mode web interface"
---

qwen_cli_coder appeared within days of Google open-sourcing Gemini CLI in June 2025, adapting the codebase to run Qwen models through Alibaba Cloud's DashScope API. It preserved Gemini CLI's grounded-documentation and workflow machinery while adding dynamic MCP server management and multi-agent task coordination, including sub-agent spawning and delegation tools for splitting work across parallel agent instances. The fork documented Qwen-specific authentication and model configuration for developers who wanted Alibaba's models in a Gemini-CLI-style workflow. Active development lasted roughly a week in mid-2025; Alibaba's own Qwen Code fork, released the same month with an official team behind it, made the community fork redundant. It stands as an early example of the fork-and-retarget wave that followed Gemini CLI's open-sourcing.
