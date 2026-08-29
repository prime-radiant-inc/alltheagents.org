---
name: "EchoCoding"
slug: "echocoding"
layout: "agent.njk"
category: "other"
maker: "launsion-boop"
license: "MIT"
url: "https://github.com/launsion-boop/EchoCoding"
source_code_url: "https://github.com/launsion-boop/EchoCoding"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-04-14"
current_release: "2026-05-11"
stars: "28"
language: "TypeScript/JavaScript (Node.js 18+)"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "True"
subagents: "True"
hooks: "True"
plan_mode: "False"
model_providers: "TTS: Volcengine cloud (21 voices), Kokoro 82M local (103 voices), macOS say/Linux espeak (fallback). ASR: Volcengine V3 BigModel (cloud), Paraformer (local), browser MediaRecorder (Studio)"
pricing: "freemium"
install_method: "npm i -g echocoding && echocoding install --auto --start && echocoding doctor"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://www.npmjs.com/package/echocoding"
maintained: "active"
sources:
  - "brad"
what_makes_it_special: "Adds an immersive audio layer to AI coding agents — 23 sound effects, ambient soundscapes, TTS speech, and ASR voice Q&A. 'Pipes, not brains' philosophy: the AI agent decides when and what to say; EchoCoding just provides the audio infrastructure (say / ask / sfx). Three audio layers: discrete SFX, continuous ambient soundscapes, and voice interaction. MCP Server (stdio) with 5 tools. Claude Code integration via 9-event hook injection. Multi-turn voice conversation with echo suppression (260ms anti-bleed gate)."
---

Long agent sessions are easy to ignore: you switch windows and only find out a task finished — or failed — when you look back. EchoCoding gives the session an audio channel without touching the agent's logic: hooks fire sound effects for tool actions, an ambient layer signals editing/reading/thinking state, and TTS speaks at milestones while ASR listens for spoken replies through a floating HUD. The agent decides what to say; EchoCoding only handles the pipes, which is why it installs with one line and no API keys of its own. Developers who run hands-off sessions — or prefer audio over window-switching — are the intended users.
