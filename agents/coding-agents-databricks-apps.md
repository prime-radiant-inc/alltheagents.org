---
name: "coding-agents-databricks-apps"
slug: "coding-agents-databricks-apps"
layout: "agent.njk"
category: "other"
maker: "datasciencemonkey"
license: "MIT"
url: "https://github.com/datasciencemonkey/coding-agents-databricks-apps"
source_code_url: "https://github.com/datasciencemonkey/coding-agents-databricks-apps"
source_available: "True"
platforms: []
first_released: "2026-02-03"
current_release: "2026-07-30"
stars: "27"
language: "Python"
homepage: "https://datasciencemonkey.github.io/coding-agents-databricks-apps/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Anthropic, OpenAI, Google, NousResearch"
pricing: "Free / open-source"
install_method: "GitHub template to Databricks Custom App, or local: git clone + uv run python app.py"
docs_url: "https://datasciencemonkey.github.io/coding-agents-databricks-apps/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/datasciencemonkey/coding-agents-databricks-apps"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Zero-setup browser terminal running 5 coding agents (Claude Code, Codex, Gemini CLI, Hermes Agent, OpenCode) on Databricks Apps with enterprise integration: Unity Catalog governance, AI Gateway centralized model routing, automatic MLflow tracing of every session, auto-rotating short-lived PATs, parallel agent setup, WebSocket real-time I/O, and auto-sync to Databricks Workspace on every git commit."
---

Enterprises want developers using coding agents, but agents running on laptops sit outside governance boundaries, and data teams need audit trails and central model billing. CoDA packages five coding agent CLIs into a browser-terminal Databricks App: an xterm.js frontend over a Flask/Gunicorn PTY server, with an entrypoint script that installs and preconfigures the agent CLIs at boot and wires all model calls through the Databricks AI Gateway for central governance. Unity Catalog governs what the agents can access, MLflow traces every session, personal access tokens rotate automatically, and 39 skills plus 2 MCP servers (DeepWiki, Exa) ship preconfigured. Data platform teams deploy it from a GitHub template to give developers governed browser access to agents; the project has moved to the databrickslabs organization, where development continues.
