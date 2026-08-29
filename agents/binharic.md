---
name: "Binharic"
slug: "binharic"
layout: "agent.njk"
category: "agent"
maker: "CogitatorTech"
license: "MIT"
url: "https://github.com/CogitatorTech/binharic-cli"
source_code_url: "https://github.com/CogitatorTech/binharic-cli"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2025-08-16"
current_release: "2025-11-01"
stars: "18"
language: "TypeScript"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Google, Anthropic, Ollama"
pricing: "Free / open-source"
install_method: "npm install -g @cogitator/binharic-cli, or Docker: docker run -it --rm ghcr.io/cogitatortech/binharic-cli:<version>"
docs_url: "https://github.com/CogitatorTech/binharic-cli/blob/main/docs"
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/@cogitator/binharic-cli"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Terminal-based multi-provider AI coding agent with a 'Tech-Priest of the Adeptus Mechanicus' persona and a built-in keyword-based retrieval-augmented generation (RAG) pipeline. Can analyze projects, run tests, find bugs, and perform code reviews."
---

binharic-cli is a terminal coding agent that started as a personal project for learning how to build agents and grew into a working assistant that analyzes projects, runs tests, finds bugs, and reviews code. It is built in TypeScript on the Vercel AI SDK and explicitly follows Anthropic's published 'building effective agents' architecture, with models from OpenAI, Google, Anthropic, and Ollama. File reading and shell execution ship as built-in tools, external tools plug in through Model Context Protocol servers, and a built-in keyword-based RAG pipeline grounds responses in project context. Predefined workflows cover recurring tasks such as debugging and code review, and the agent speaks in the persona of a Warhammer 40k Tech-Priest of the Adeptus Mechanicus. It is MIT-licensed, small and early-stage, installed via npm or Docker, and best suited to developers who want a small, hackable terminal agent to extend with custom tools.
