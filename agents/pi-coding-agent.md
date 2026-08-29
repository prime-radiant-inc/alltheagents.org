---
name: "pi-coding-agent"
slug: "pi-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "dnouri"
license: "GPL-3.0-or-later"
url: "https://github.com/dnouri/pi-coding-agent"
source_code_url: "https://github.com/dnouri/pi-coding-agent"
source_available: "True"
platforms: []
first_released: "2025-12-30"
current_release: "2026-08-09"
stars: "258"
language: "Emacs Lisp"
homepage: "https://github.com/dnouri/pi-coding-agent"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "False"
hooks: "True"
plan_mode: "False"
model_providers: "DeepSeek, OpenAI, Z.AI (via Pi CLI)"
pricing: "Free / open-source"
install_method: "M-x package-install RET pi-coding-agent RET (from MELPA); or git clone with load-path setup"
docs_url: "https://pi.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://melpa.org/#/pi-coding-agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Emacs frontend for the Pi coding agent that communicates over RPC for structured messages and tool events (instead of terminal text). Provides a Markdown-rendered chat buffer with tree-sitter highlighting, a separate editable prompt buffer, session management, fork/compact, and Evil integration — letting you use familiar Emacs editing habits for composing prompts."
---

pi-coding-agent brings pi into Emacs on RPC rather than terminal emulation, so the package receives structured messages and tool events instead of scraping ANSI output — the difference between a real client and a screen-scraping wrapper. The chat buffer renders Markdown with tree-sitter highlighting, a separate prompt buffer keeps drafts editable between turns, and sessions support fork and compact operations from Emacs. Activity-phase hooks fire as sessions move between thinking, replying, running, compacting, and idle states, letting Elisp tint inputs, send notifications, or track busy sessions; Evil integration keeps modal editing intact for Vim users. Distributed on MELPA under GPL-3.0-or-later and tested in CI across Emacs 29 and 30 plus nightly builds, it targets Emacs users who want agentic coding without leaving their editor's conventions.
