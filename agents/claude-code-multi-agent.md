---
name: "Claude-Code-Multi-Agent"
slug: "claude-code-multi-agent"
layout: "agent.njk"
category: "other"
maker: "Prorise-cool"
license: "MIT"
url: "https://github.com/Prorise-cool/Claude-Code-Multi-Agent"
source_code_url: "https://github.com/Prorise-cool/Claude-Code-Multi-Agent"
source_available: "True"
platforms: []
first_released: "2025-08-06"
current_release: "2026-08-06"
stars: "302"
language: "Python"
homepage: "https://github.com/Prorise-cool/Claude-Code-Multi-Agent"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "True"
plan_mode: "no"
model_providers: "Ollama (gemma3:1b, llama3.2:3b, qwen2.5:7b), Anthropic (Claude Code)"
pricing: "free"
install_method: "Install Ollama + uv, git clone, configure .env, place project in directory and open with Claude Code"
docs_url: "https://github.com/Prorise-cool/Claude-Code-Multi-Agent/blob/master/project_document"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Prorise-cool/claude-code-multi-agent.git"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Intelligent development framework for Claude Code that adds project awareness via a Hooks system. Uses Ollama (local LLM) to auto-detect project type/framework, recommend 300+ expert Skills, perform intent analysis, and maintain docs automatically. Replaces Memory MCP with document-driven context injection to avoid context explosion."
---

The framework addresses context amnesia in Claude Code: sessions start cold, conventions drift, and documentation rots. It works by cloning a dedicated workspace, placing the project inside, and wiring hooks so that every session start injects detected project context, relevant skills, and intent analysis from a locally running Ollama model, so no extra cloud calls are needed for the meta-layer. Recommended MCP tools and execution plans are surfaced per prompt, and predefined command workflows cover spec-driven development and git workflows. Solo developers, primarily in the Chinese-language community, use it; the repo has few commits and no releases beyond v1.0.0.
