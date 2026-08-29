---
name: "10x-Tool-Calls"
slug: "10x-tool-calls"
layout: "agent.njk"
category: "other"
maker: "perrypixel"
license: null
url: "https://github.com/perrypixel/10x-Tool-Calls"
source_code_url: "https://github.com/perrypixel/10x-Tool-Calls"
source_available: "True"
platforms: []
first_released: "2025-06-11"
current_release: "2025-06-11"
stars: "854"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "open-source"
install_method: "copy files (Python script + rules)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Exploits tool-call quotas (e.g., 25 tool calls per request) of agent-based IDEs (Cursor, Windsurf) by running interactive task loops, keeping a session alive within a single request's tool-call limit to yield 10x or more work for the same quota cost."
---

Cursor and Windsurf meter usage by requests and tool calls rather than tokens, which means a finished or stalled agent session burns quota when the chat restarts. 10x-Tool-Calls ships a rules file plus a userinput.py script: after each completed task the script prompts for the next instruction inside the same request, keeping the session alive within one request's tool-call limit. It installs by copying the script into the project and pasting the rules into .cursorrules or the IDE's project rules set to always-on, and it requires Agent Mode. It only helps on tool-call-metered plans, not token-based ones, and its audience is quota-conscious Cursor and Windsurf users.
