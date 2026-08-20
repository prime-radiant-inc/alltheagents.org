---
name: "llm-coding-agent"
slug: "llm-coding-agent"
layout: "agent.njk"
category: "agent"
maker: "simonw"
license: "Apache-2.0"
url: "https://github.com/simonw/llm-coding-agent"
source_code_url: "https://github.com/simonw/llm-coding-agent"
source_available: True
platforms: []
first_released: "2026-07-02"
current_release: "2026-07-04"
stars: "35"
language: "Python"
homepage: null
mcp_support: null
plugin_support: True
claude_code_plugin: False
subagents: False
hooks: null
plan_mode: null
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

LLM plugin that adds an `llm code` command for interactive coding-agent sessions; works with any LLM-supported model (provider-agnostic) and leverages LLM's SQLite logging, conversation resume, and plugin architecture; fine-grained approval workflows (y once, a approve similar for session, --yolo auto-approve, --allow pre-approve patterns); security by confinement - all file access sandboxed to a root directory with path-traversal protection; dual CLI and Python API (CodingAgent/CodingTools classes); first alpha was built by Claude Code (Fable 5) via prompt-driven development.
