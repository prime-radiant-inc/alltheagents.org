---
name: "llm-coding-agent"
slug: "llm-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "simonw"
license: "Apache-2.0"
url: "https://github.com/simonw/llm-coding-agent"
source_code_url: "https://github.com/simonw/llm-coding-agent"
source_available: "True"
platforms: []
first_released: "2026-07-02"
current_release: "2026-07-04"
stars: "35"
language: "Python"
homepage: "https://github.com/simonw/llm-coding-agent"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "False"
hooks: "no"
plan_mode: "no"
model_providers: "Any tool-capable model LLM knows about (OpenAI, Anthropic, etc. via the LLM ecosystem)"
pricing: "Free / open-source"
install_method: "pip install --pre llm-coding-agent (--pre needed while it depends on an LLM alpha release)"
docs_url: "https://github.com/simonw/llm-coding-agent/blob/main/spec.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://pypi.org/project/llm-coding-agent/"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "LLM plugin that adds an `llm code` command for interactive coding-agent sessions; works with any LLM-supported model (provider-agnostic) and leverages LLM's SQLite logging, conversation resume, and plugin architecture; fine-grained approval workflows (y once, a approve similar for session, --yolo auto-approve, --allow pre-approve patterns); security by confinement - all file access sandboxed to a root directory with path-traversal protection; dual CLI and Python API (CodingAgent/CodingTools classes); first alpha was built by Claude Code (Fable 5) via prompt-driven development."
---

The plugin exists because Willison wanted a minimal, inspectable coding agent on top of the llm CLI's model-agnostic plugin system; the first alpha was itself written by prompting Claude Code through a spec-and-TDD workflow. Read-only tools (numbered read_file, gitignore-aware list_files, ripgrep-backed search) run freely, while write_file, edit_file, and execute_command require approval, with chain_limit bounding tool rounds per run and every session recorded for resume via -c or --cid. File access is confined to the session root, with traversal via .., absolute paths, or symlinks rejected as errors the model can correct. A Python API (CodingAgent, CodingTools) exposes the same loop programmatically, with a pause/resume approval protocol for non-terminal applications.
