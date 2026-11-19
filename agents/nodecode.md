---
name: "Nodecode"
slug: "nodecode"
layout: "agent.njk"
category: "agent"
maker: "nodecode-ai"
license: "MIT"
url: "https://github.com/nodecode-ai/nodecode"
source_code_url: "https://github.com/nodecode-ai/nodecode"
source_available: "True"
homepage: "https://nodecode.ai"
docs_url: "https://nodecode.ai/docs"
download_url: "https://nodecode.ai/docs/install"
install_method: "curl -fsSL https://nodecode.ai/install.sh | sh (Linux/macOS); irm https://nodecode.ai/install.ps1 | iex (Windows); then run nodecode — or build from source with SBCL, Quicklisp, git, python3, and just (just release)"
platforms:
  - "CLI"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Common Lisp"
first_released: "2025-08-21"
current_release: "2026-11-13"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: "https://nodecode.ai/docs/cell-api"
config_docs_url: "https://nodecode.ai/docs/config"
model_providers: "Any provider speaking one of four wire dialects (openai-completions, openai-responses, anthropic, google) via the models.dev catalog, including local servers through base_url; Foresight Labs also sells hosted models (Cyber v1, Decide v1, Image v1) by top-up tokens"
pricing: "freemium"
stars: "275"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A self-rewriting agent that runs as one live SBCL process: the model's single tool is eval, so it writes, runs, and permanently keeps the Lisp it needs (new tools become definitions committed one file each with git and loaded at every start), edits its own context with whole-turn recall rather than summaries, and installs most updates into the running program one definition at a time with generations and rollback."
---

Nodecode treats the agent as a living program rather than a loop over a chat: it boots one SBCL Common Lisp process that shells attach to, and the model's only tool is eval — whatever Lisp it defines runs immediately and is kept, one file per definition, committed with git and reloaded at startup, so a session that teaches itself to read PDFs still has the ability tomorrow. Context is handled the same way: the agent decides what stays and what goes, and nothing let go is lost — any old turn is readable back word for word with recall-entry. The same organism reaches every client: a gateway serves the terminal, a browser tab, a phone, bots in Discord, Telegram, and Slack, and an RPC interface, and it grows through cells — installable folders that add tools, chat rooms, providers, MCP servers, or scheduled prompts. Foresight Labs, its Dutch maker, publishes the hosted Cyber/Decide/Image models that fund development, while the agent itself is MIT and runs on any provider key or local server. It ships no sandbox — eval and shell run with the user's full authority, which the docs say plainly and tell you to containerize — and suits developers who want one durable, self-extending agent rather than a fleet.
