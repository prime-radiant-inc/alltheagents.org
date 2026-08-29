---
name: "Agentforce Vibes"
slug: "agentforce-vibes"
layout: "agent.njk"
category: "agent"
maker: "Salesforce"
license: "Proprietary"
url: "https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-einstein-gpt"
source_code_url: null
source_available: False
platforms:
  - "IDE"
first_released: "2023-09-08"
current_release: "2026-08-20"
stars: null
language: null
homepage: "https://developer.salesforce.com/tools/vscode"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "True"
model_providers: "Anthropic Claude, OpenAI GPT (mid-session model picker)"
pricing: "subscription"
install_method: "Install from the VS Code Marketplace"
docs_url: "https://developer.salesforce.com/docs/einstein/genai-overview"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=salesforce.salesforcedx-einstein-gpt"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Turn-based Salesforce agent combining Claude Agent SDK or OpenAI Agents SDK"
---

Agentforce Vibes is the current form of what began as Einstein for Developers in 2023: a VS Code extension for Salesforce platform development rebuilt in version 4.0 on the Agentforce SDK. Its agent plans before executing (with an approval-gated plan mode), streams agentic chat with inline diff review, and offers three autonomy settings — ask every time, run safe defaults, or bypass — backed by command allowlists, while MCP servers connect it to live org metadata and APIs. Inline completions cover Apex, JavaScript, HTML, CSS, and Lightning Web Components, and rules plus skills live in a .vibes/ directory that teams version-control and share. Roughly 895,000 installs make it one of the most-distributed Salesforce dev tools, and it serves Salesforce platform developers.
