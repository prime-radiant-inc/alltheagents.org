---
name: "PUNK"
slug: "punk"
layout: "agent.njk"
category: "multiplexer"
maker: "PUNK"
license: null
url: "https://punkcode.rocks"
source_code_url: null
source_available: null
platforms: []
first_released: null
current_release: null
stars: null
language: "JavaScript (Node.js CLI), React Native/Expo (app)"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Claude/Anthropic (wraps Claude Code)"
pricing: "Free while in beta on TestFlight"
install_method: "App: TestFlight invite; CLI: npm i -g @punkcode/cli, then punk connect and scan QR code from phone app"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://punkcode.rocks"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "iPhone app acting as remote control for Claude Code running on your laptop - phone is terminal, laptop is mainframe. Decouples execution from control: agents run locally but you direct them from your phone anywhere. Lock-screen approval, AI voice input (4x faster than typing), multiple parallel sessions, multiple connected devices, outbound-only TLS relay (no open ports, no data stored). Skills, MCPs, and commands all accessible from phone. Modes: Plan, Ask, Auto, Dangerous. Endorsed by Rick Rubin as 'the Punk Rock of Coding.'"
---

PUNK separates where an agent runs from where a human directs it: Claude Code sessions execute on your laptop while your iPhone becomes the control terminal, letting you approve permission requests from the lock screen, read streaming output, and switch between parallel sessions from anywhere. The CLI connects outbound over TLS with no open ports, and a relay with no persistent database means conversation data passes through and disappears rather than sitting on a server. Skills, MCP servers, and slash commands remain manageable from the phone, and execution modes — Plan, Ask, Auto, Dangerous — map to how much autonomy you grant remotely. The CLI keeps the Mac awake and connected, so long agent runs continue in a backpack with the lid closed. It is built for developers who run Claude Code locally but want to supervise it away from the desk.
