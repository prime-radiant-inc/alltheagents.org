---
name: "MPLAB AI Coding Assistant"
slug: "mplab-ai-coding-assistant"
layout: "agent.njk"
category: "agent"
maker: "Microchip Technology"
license: null
url: "https://marketplace.visualstudio.com/items?itemName=Microchip.mplab-ai-coding-assistant"
source_code_url: null
source_available: null
platforms:
  - "IDE"
first_released: "2025-02-18"
current_release: "2026-05-07"
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: null
pricing: "free"
install_method: "Install from the VS Code Marketplace"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=Microchip.mplab-ai-coding-assistant"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "AI code assistant optimized for Microchip embedded products"
---

Microchip adapted the open-source Continue extension for its embedded ecosystem, where generic assistants hallucinate register names and peripheral configurations that a datasheet-grounded model would get right. The result ships in four modes: an Agent Mode that applies code edits and runs project tasks from chat, a Microchip-trained chatbot for product-specific questions, conventional autocomplete, and an edit mode for generation and explanation. Domain grounding is the point — the assistant continuously updates with Microchip-specific data, surfaces datasheet content inside the editor, and adds slash commands and shortcuts tuned to Microchip parts, while Microchip commits to not training on user prompts or outputs. Distribution follows the standard VS Code Marketplace path at no cost under Microchip's license terms, with roughly 45,000 installs since early 2025. Embedded developers working with Microchip MCUs and development boards are the intended users, and the extension's changelog shows steady updates through 2026.
