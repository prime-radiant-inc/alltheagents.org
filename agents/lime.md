---
name: "lime"
slug: "lime"
layout: "agent.njk"
category: "agent"
maker: "limecloud"
license: "GPL-3.0"
url: "https://github.com/limecloud/lime"
source_code_url: "https://github.com/limecloud/lime"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-12-13"
current_release: "2026-08-19"
stars: "1467"
language: "TypeScript, Rust, JavaScript (Electron + React + Vite, Rust App Server)"
homepage: "https://limeai.run"
mcp_support: "yes - tool discovery and external tool integration"
plugin_support: "yes - Skills system, extensions (e.g., lime-chrome), bundled plugins (openai-bundled)"
claude_code_plugin: "no - has CLAUDE.md but is its own agent"
subagents: "yes - multi-agent coordination, parallel subtask delegation, shared context"
hooks: null
plan_mode: "yes - agent proposes plans and boundaries requiring approval before execution"
model_providers: "configurable providers/models/credentials/routing/retries, no vendor lock-in"
pricing: "open-source"
install_method: "binary - GitHub Releases (.dmg/.exe) or Homebrew (brew install --cask lime)"
docs_url: "https://limeai.run"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Open-source full-stack desktop AI agent combining coding, file operations, terminal commands, tool calls, research, content creation, and multi-agent collaboration in one workspace. Desktop GUI agent with Thread/Turn/Item projections for traceable task chains. Full-stack multimodal (text, code, images, audio, video, PDFs, structured data). Multi-agent coordination delegates research/implementation/testing/documentation to different agents with shared context. Skills system encodes repeatable procedures as reusable execution units callable via MCP. Provider-agnostic."
---

Lime packages the agentic loop — context, tools, permissions, verification, delivery — into a desktop application rather than a terminal, so users watch plans, approve actions, and inspect diffs and artifacts in a visual workspace. Tasks are structured as Thread/Turn/Item projections that can be paused, reviewed, restored, and continued, and multi-agent collaboration splits research, implementation, testing, and documentation across agents sharing one context. A Rust app server handles the backend, and a Skills system encodes repeatable procedures as units callable through MCP. It is provider-agnostic with local-by-default data, targets developers and technical users who want a GUI over an agentic loop, and runs on macOS and Windows (Linux builds paused).
