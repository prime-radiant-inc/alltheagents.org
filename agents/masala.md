---
name: "Masala"
slug: "masala"
layout: "agent.njk"
category: "agent"
maker: "infusius"
license: "MIT"
url: "https://github.com/infusius/masala"
source_code_url: "https://github.com/infusius/masala"
source_available: "True"
homepage: null
docs_url: "https://github.com/infusius/masala#readme"
download_url: null
install_method: "git clone, then pnpm install && uv sync && pnpm start (Node 22.18+/24.12+, pnpm, uv for Python 3.12+); opens at http://localhost:4173. Requires an agent CLI (Claude Code signed in, or Codex with an OpenAI API key) or just an OpenAI API key"
platforms:
  - "Desktop"
autonomy_level:
  - "agentic"
specialization: "general"
language: "Python"
first_released: "2026-09-15"
current_release: "2026-09-29"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: null
model_providers: "Claude Code, Codex (installed agent CLIs with their own sign-ins), and OpenAI API as a direct backend (loop run by Masala itself)"
pricing: "free"
stars: "85"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A research workspace where the agent works beside you — chat, PDFs, notebooks and files in one dock of configurable panes, and the agent writes new pane types (a PDB viewer, a SQLite visualizer) on request; it can drive Claude Code or Codex, or run its own tool loop directly against the OpenAI API."
---

Masala, called Panel until September 2026, is a research workspace built around a single idea: a researcher and an agent sharing one screen. The UI is a dock of configurable panes — image and data files, code, markdown, PDFs, and Jupyter notebooks running against a real kernel that both human and agent can edit — and when no built-in pane can show something, the agent writes a custom one as Vue/TypeScript, which you can then edit from its own tab by saying what should change. Workspaces give each project folder its own chats and saved layout, long-running commands run in the background while you watch, and everything lands in a local SQLite database under ~/Masala. Three backends drive the agent: Claude Code (signed in on its own), Codex (with an OpenAI key), and a direct OpenAI API option whose tool loop Masala runs itself, with permission modes from ask-every-time to allow-all. Modules add agentic workflows with typed inputs, outputs and intermediates — a literature review and hypothesis workflows ship first — and the same Modules are exposed as an MCP server, so Claude Code or Codex in your own terminal can call a literature review and have it run inside Masala. The project is an explicit early build for testers ('expect rough edges'), MIT-licensed, and aimed at researchers who live between papers, notebooks and data files.
