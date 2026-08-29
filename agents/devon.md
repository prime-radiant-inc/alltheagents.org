---
name: "Devon"
slug: "devon"
layout: "agent.njk"
category: "agent"
maker: "entropy-research"
license: "AGPL-3.0"
url: "https://github.com/entropy-research/Devon"
source_code_url: "https://github.com/entropy-research/Devon"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
first_released: "2024-03-15"
current_release: "2025-05-26"
stars: null
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude 3.5 Sonnet), OpenAI (GPT-4o), Groq (Llama 3 70B), Ollama (DeepSeek Coder 6.7B, local), Google Gemini 1.5 Pro (planned)"
pricing: "Free / open-source (BYO API key)"
install_method: "pipx install devon_agent, npx devon-ui (main UI) or npm install -g devon-tui (terminal UI)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "jqueryscript"
  - "e2b"
  - "brad"
  - "jim"
  - "ishandutta"
what_makes_it_special: "Community-driven open-source coding agent that beat AutoCodeRover on SWE-Bench Lite; offers both terminal UI and Electron-based GUI; supports local models via Ollama; sandboxed to working directory; interactive and steerable during execution. Last commit July 2024."
---

Devon was built by a volunteer team to prove an open-source agent could match commercial ones, publishing SWE-Bench Lite results above AutoCodeRover shortly after Devin's launch. The backend installs via pipx and drives an edit-test loop sandboxed to the working directory, while users choose between an Electron GUI and a terminal UI. Local models run through Ollama, making it usable without cloud API spend. The project was most active through early 2025 and has since gone quiet; it is preserved here as one of the earliest open Devin alternatives rather than a current daily-driver tool.
