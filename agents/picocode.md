---
name: "picocode"
slug: "picocode"
layout: "agent.njk"
category: "agent"
maker: "jondot"
license: "MIT"
url: "https://github.com/jondot/picocode"
source_code_url: "https://github.com/jondot/picocode"
source_available: "True"
platforms: []
first_released: "2026-01-16"
current_release: "2026-01-30"
stars: "58"
language: "Rust"
homepage: "https://github.com/jondot/picocode"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Anthropic, OpenAI, DeepSeek, Google (Gemini), Ollama, and many more via Rig"
pricing: "Free/open source"
install_method: "curl -sSfL https://raw.githubusercontent.com/jondot/picocode/main/install.sh | sh"
docs_url: "https://github.com/jondot/picocode#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/jondot/picocode/releases"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "Tiny single-binary Rust agent; persona-driven (architect, security, zen, hacker, etc.); recipe-based automation for CI/CD; multi-LLM sovereignty; safety-first (destructive actions require confirmation); usable as CLI or Rust library."
---

picocode came out of the observation that most coding agents are heavy Node.js applications, and some jobs — CI codemods, unattended pipeline fixes — need something closer to a Unix tool. The Rust binary wraps a complete agent loop: file edits, shell commands, confirmation gates for destructive actions, and a --yolo flag for unattended runs, with a tool-call limit bounding runaway loops. Personas swap the agent's expertise and voice on a flag (architect, security, sre, tester, hacker), and recipes define named non-interactive tasks in picocode.yaml with prompt, persona, and model, invoked in pipelines. Model access spans Anthropic, OpenAI, DeepSeek, Gemini, and Ollama through the Rig library, and the same binary embeds as a Rust library. The project is early and small (14 commits, 60 stars, no releases yet), aimed at developers who want a minimal, auditable agent for CI rather than a full IDE companion.
