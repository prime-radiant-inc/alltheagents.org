---
name: "Micro Agent"
slug: "micro-agent"
layout: "agent.njk"
category: "agent"
maker: "Independent"
license: "MIT"
url: "https://github.com/micro-agent/micro-agent"
source_code_url: "https://github.com/micro-agent/micro-agent"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025"
current_release: "2026"
stars: null
language: "TypeScript"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "Anthropic, OpenAI, Ollama, any OpenAI-compatible endpoint (Groq)"
pricing: "open-source"
install_method: "npm install -g @builder.io/micro-agent (Node.js 18+)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "dormant"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Lightweight AI coding agent for terminal"
---

BuilderIO built Micro Agent around a critique of general-purpose coding agents: given too much freedom they compound errors, so the harness narrows the loop to test-driven iteration. The user supplies a prompt and a file; the agent generates a unit test that defines correct behavior, then regenerates the target file and reruns the test command (npm test or any script) until everything passes, with an optional .prompt.md file steering generation and interactive mode asking clarifying questions. It deliberately will not install modules, write multiple files, or take other high-blast-radius actions — the README compares general agents to a Roomba stuck under a table. Providers are configured via API keys for Claude, OpenAI, Ollama, or any OpenAI-compatible endpoint such as Groq, installed globally through npm with Node 18+. Frontend teams used it for component generation, including a Figma-to-code workflow via Builder's Figma integration; development stopped after November 2024.
