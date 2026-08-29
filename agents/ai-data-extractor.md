---
name: "ai-data-extractor"
slug: "ai-data-extractor"
layout: "agent.njk"
category: "other"
maker: "bawadou"
license: "MIT"
url: "https://github.com/bawadou/ai-data-extractor"
source_code_url: "https://github.com/bawadou/ai-data-extractor"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-08-16"
current_release: "2026-08-17"
stars: "388"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: "Free / open-source"
install_method: "python extract.py (Python 3.9+, no dependencies)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/bawadou/ai-data-extractor"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Extracts local chat history from 10 AI coding assistants (Claude Code, Cursor, Windsurf, Trae, Continue, Gemini CLI, OpenCode, Cline/Roo Code, Aider, Codex CLI) into a single normalized JSONL format for fine-tuning/analytics/backup; auto-discovers data across OSes; zero dependencies; extensible two-function interface."
---

Local assistant databases are scattered across platform-specific paths and formats, and they get cleared or lost when apps update. This toolkit auto-discovers storage on macOS, Linux, and Windows, and extracts messages, code context, diffs, tool calls, timestamps, and model names into timestamped JSONL files with a shared schema (guaranteed fields: messages, source, session_id). It handles ten assistants — Claude Code, Codex CLI, Cursor, Windsurf, Trae, Continue, Gemini CLI, OpenCode, Cline/Roo Code, and Aider — using line-by-line JSON parsing and read-only SQLite connections so running apps are not disturbed, and corrupt files yield partial results instead of failures. A --merge flag produces a single HuggingFace-datasets-ready file for fine-tuning or analytics. It runs on the Python standard library alone, with per-assistant extractors that also run standalone.
