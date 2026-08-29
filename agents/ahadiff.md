---
name: "ahadiff"
slug: "ahadiff"
layout: "agent.njk"
category: "other"
maker: "AGI-is-going-to-arrive"
license: "MIT"
url: "https://github.com/AGI-is-going-to-arrive/ahadiff"
source_code_url: "https://github.com/AGI-is-going-to-arrive/ahadiff"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-04-19"
current_release: "2026-06-26"
stars: "228"
language: "Python (backend), React 19 (frontend viewer)"
homepage: "https://agi-is-going-to-arrive.github.io/ahadiff/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "True"
plan_mode: "no"
model_providers: "OpenAI,Anthropic,Gemini,Azure,OpenAI-compatible,NewAPI,LM Studio,Ollama,DeepSeek"
pricing: "open-source"
install_method: "pipx install ahadiff"
docs_url: "https://github.com/AGI-is-going-to-arrive/ahadiff/blob/main/docs/USER_GUIDE.en.html"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/ahadiff/"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Local-first learning layer for AI coding; turns git diffs into code-verified lessons, claims ledgers (file:line evidence), quizzes, and spaced-repetition review cards. Read-only MCP server with 7 tools; writes repo-local guidance files for 15 AI CLI/IDE/CI targets."
---

AI assistants ship code faster than developers understand it, and conventional summaries do not build durable knowledge. AhaDiff reads a diff through ten capture modes (staged, working tree, revision ranges, patch files, directories) and produces a lesson, a claims ledger where every claim carries file:line evidence and a verified/weak/contradicted status, an active-recall quiz, and FSRS-scheduled review cards. Each run receives an 8-dimension deterministic score with hard gates, and an improve-run loop regenerates lessons only when the score strictly improves, giving runs a comparable quality ratchet. A read-only MCP server (seven tools) lets agents like Claude Code and Codex pull learning material directly, and git hooks can trigger auto-learn after each commit. State stays local under .ahadiff/ with strict_local privacy defaults, and exports cover TSV, JSON, and Anki decks.
