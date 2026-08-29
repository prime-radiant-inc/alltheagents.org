---
name: "web-code-agent"
slug: "web-code-agent"
layout: "agent.njk"
category: "other"
maker: "oldjs"
license: "MIT"
url: "https://github.com/oldjs/web-code-agent"
source_code_url: "https://github.com/oldjs/web-code-agent"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-05-14"
current_release: "2025-07-02"
stars: "270"
language: "TypeScript"
homepage: "https://file.wen.bar"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "None — generates context Markdown for external LLMs (ChatGPT, Claude)"
pricing: "Free / open-source"
install_method: "git clone + npm install (Next.js 14 project)"
docs_url: "https://github.com/oldjs/web-code-agent"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/oldjs/web-code-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Runs entirely locally in the browser with absolute privacy—code never leaves the user's machine. Uses a semantic vectorization engine to build a local knowledge index of the codebase, enabling natural language Q&A. Acts as an LLM collaboration accelerator by generating context-aware Markdown to feed AI assistants, reducing token costs and API latency. Also supports smart config generation (e.g., Dockerfile)."
---

web-code-agent (Folda-Scan) solves codebase Q&A for users who cannot or will not upload code to cloud services: scanning, semantic vectorization, indexing, and question matching all run in the browser using the File System Access API, so project code never leaves the machine. Built on Next.js 14, it builds a local vector index from a selected project folder and answers natural-language questions against it. It also generates context-aware Markdown designed to be pasted into external AI assistants, reducing token costs, and can help produce configuration files such as Dockerfiles. It calls no LLM APIs itself; external assistants like ChatGPT or Claude consume the Markdown it produces. Usage requires a Chromium browser with the File System Access API.
