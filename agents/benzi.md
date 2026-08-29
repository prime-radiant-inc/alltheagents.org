---
name: "Benzi"
slug: "benzi"
layout: "agent.njk"
category: "agent"
maker: "Variant Technologies"
license: "Proprietary"
url: "https://benzi.fly.dev/about"
source_code_url: "https://github.com/oooscoos/Benzi"
source_available: "True"
platforms:
  - "Web"
first_released: "2026-07-29"
current_release: null
stars: 37
language: "Python"
homepage: "https://benzi.fly.dev"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: null
hooks: null
plan_mode: "no"
model_providers: "DeepSeek, Anthropic"
pricing: "free"
install_method: null
docs_url: "https://benzi.fly.dev/about"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Compiles the codebase into a resolved, queryable map before answering: tree-sitter grammars resolve imports, class ancestry, and every identifier to its definition, so call-flow and data-flow questions answer in O(1) through tools like get_callers, call_tree, trace_path, and backflow. Every edit passes syntax and semantic checks against the real parser with automatic rollback on broken parses."
---

Benzi is a coding agent harness from Variant Technologies built on the observation that Claude Code greps, Cursor embeds, and Aider maps signatures, while Benzi resolves. Before the agent loop runs, it compiles the codebase into a queryable map using per-language tree-sitter grammars — ten languages spanning Python, JavaScript, TypeScript, Java, C#, C++, C, Go, Rust, and Ruby, plus a second engine for HTML, CSS, and DOM-JS — resolving imports, class ancestry, and identifier definitions, and joining call flow and data flow at call sites. The agent then works through 35-plus tools like get_callers, call_tree, trace_path, and backflow, and every write is gated through syntax and semantic checks with blast-radius checks before and after changes and automatic rollback on broken parses. Its self-reported benchmarks include 78.2% on SWE-bench Verified run on DeepSeek v4-flash at $0.095 per resolved instance, and a cross-harness comparison claiming it reads 2.3x fewer lines than Claude Code on the same 24-bug set; the repo is public under a proprietary source-available license, with a web app and a VS Code extension.
