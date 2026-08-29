---
name: "mbti-coding-agents"
slug: "mbti-coding-agents"
layout: "agent.njk"
category: "agent"
maker: "weiyangzen"
license: null
url: "https://github.com/weiyangzen/mbti-coding-agents"
source_code_url: "https://github.com/weiyangzen/mbti-coding-agents"
source_available: "True"
platforms: []
first_released: "2025-07-30"
current_release: "2025-08-25"
stars: "37"
language: "JavaScript, Node.js"
homepage: null
mcp_support: "no"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic (Claude), Google (Gemini); MiniMax and Gemini for optional TTS"
pricing: "Free / open-source"
install_method: "git clone https://github.com/weiyangzen/mbti-coding-agents.git; cd mbti-coding-agents; npm run install (optionally select Claude TTS during install)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/weiyangzen/mbti-coding-agents"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Collection of 16 specialized AI coding agent personas mapped to Myers-Briggs (MBTI) personality types (Analysts, Diplomats, Sentinels, Explorers) to provide distinct cognitive styles; /squad for dynamic team selection, /battle arena where agents compete on tasks, /my-coding-mbti for personal coding MBTI detection; optional Text-to-Speech summaries."
---

The project's thesis is that a persona encoded in the system prompt changes coding-agent behavior as much as the underlying model, so it packages sixteen agents spanning analysts, diplomats, sentinels, and explorers, each with distinct approaches to planning, risk, and communication. Teams can be composed dynamically with /squad for a given task, or run in a /battle arena where personas compete on the same task and a report compares their results; /my-coding-mbti turns the mapping back on the user. Agents run inside Claude Code and Gemini CLI, with an optional text-to-speech layer (MiniMax and Gemini) for spoken summaries, and documentation is bilingual with an eight-language README. It is a small solo-maintained persona collection (37 stars, no license file).
