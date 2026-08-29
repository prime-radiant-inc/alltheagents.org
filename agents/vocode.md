---
name: "Vocode"
slug: "vocode"
layout: "agent.njk"
category: "other"
maker: "vocodedev"
license: "MIT"
url: "https://github.com/vocodedev/vocode-python"
source_code_url: "https://github.com/vocodedev/vocode-python"
source_available: "Yes"
platforms: []
first_released: "2023-02-24"
current_release: "2024-11-15"
stars: "3784"
language: "Python"
homepage: "https://vocode.dev"
mcp_support: null
plugin_support: null
claude_code_plugin: "n/a"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI, Anthropic"
pricing: "open-source"
install_method: "pip"
docs_url: "https://docs.vocode.dev/open-source"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "caramaschi"
what_makes_it_special: "Open-source library for building voice-based LLM apps (phone calls, Zoom meetings) with real-time streaming conversations, transcription, and synthesis integrations."
---

Vocode exists to remove the plumbing from real-time voice LLM applications: managing interruptible streaming audio, transcription, and synthesis across many vendors. It provides a modular Python pipeline where pluggable transcription backends (Deepgram, AssemblyAI, Whisper, Google, Azure) feed an LLM from OpenAI or Anthropic, whose output goes to pluggable speech synthesis from ElevenLabs, Azure, Polly, Cartesia, and others, deployable to phone calls, Zoom meetings, and system audio. A companion React SDK covers browser-side voice interfaces. The repo has been seeking community maintainers, indicating the core team has moved on. It serves developers embedding outbound-call or voice-assistant flows into their own applications.
