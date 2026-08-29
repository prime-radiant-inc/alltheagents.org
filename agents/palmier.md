---
name: "Palmier"
slug: "palmier"
layout: "agent.njk"
category: "multiplexer"
maker: "Palmier"
license: "Apache-2.0"
url: "https://www.palmier.me"
source_code_url: null
source_available: "True"
platforms: []
first_released: null
current_release: null
stars: null
language: "TypeScript"
homepage: "https://www.palmier.me"
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "reuses existing AI subscriptions (Claude Pro, ChatGPT Plus, etc.) — no API keys"
pricing: "Free and open source"
install_method: "curl -fsSL https://palmier.me/install.sh | bash (Linux/macOS); npm install -g palmier && palmier init; requires Node.js 24+"
docs_url: "https://github.com/caihongxu/palmier#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/caihongxu/palmier#readme"
download_url: "https://www.npmjs.com/package/palmier"
maintained: "active"
sources:
  - "toolify"
what_makes_it_special: "Turns your phone into a remote control for AI agent CLIs (Claude Code, Codex, Gemini CLI, GitHub Copilot, etc.) running on your computer. Uses your existing AI subscriptions — no API keys or per-token costs. Exposes an MCP server with 14 tools and 2 resources. Built-in AES-256-GCM password manager that agents can autofill into browsers without seeing credentials. Phone capability access (GPS, calendar, contacts, notifications, SMS). Task scheduling via native OS timers."
---

Long agent runs outlive attention spans, and walking back to the laptop to check a Claude Code or Codex session interrupts everything else. Palmier runs a background daemon — systemd on Linux, launchd on macOS 13+, Task Scheduler on Windows — that installs and manages agent CLIs and exposes their control to a phone PWA or Android app, with all execution staying on the user's machine and no data stored remotely. It reuses existing subscriptions like Claude Pro or ChatGPT Plus instead of requiring API keys, and new agent CLIs are added through configuration rather than code. An MCP server on localhost:7256 hands agents tools that reach back into the phone — calendar, contacts, notifications, geolocation, SMS, email — plus an encrypted password manager for agent logins, so a session can schedule a meeting or send a message on the user's behalf. Install is a curl script or npm global under Node 24+, Apache-2.0 licensed. Developers who start agent runs and leave the desk are the audience.
