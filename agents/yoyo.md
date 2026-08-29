---
name: "yoyo"
slug: "yoyo"
layout: "agent.njk"
category: "agent"
maker: "Independent"
license: "MIT"
url: "https://github.com/yoyolab/yoyo"
source_code_url: "https://github.com/yoyolab/yoyo"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025"
current_release: "2026"
stars: null
language: "Rust"
homepage: "https://github.com/duggasco/yoyo-evolve-clean"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Local LLM (default), OpenRouter, Anthropic"
pricing: "Free / open-source"
install_method: "git clone https://github.com/duggasco/yoyo-evolve-clean && cargo run"
docs_url: "https://github.com/duggasco/yoyo-evolve-clean"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/duggasco/yoyo-evolve-clean"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "A self-evolving coding agent CLI that reads its own source code, assesses itself, makes improvements, and commits them if tests pass. Runs this cycle automatically every 8 hours via GitHub Actions, meaning the agent continuously improves itself without human intervention. Built in Rust. Note: the original source_code_url (github.com/yoyolab/yoyo) 404s; actual repo is github.com/duggasco/yoyo-evolve-clean."
---

yoyo is an experiment in a coding agent that maintains itself: a GitHub Actions workflow runs every eight hours, the agent reads its own IDENTITY.md, src/main.rs, and JOURNAL.md, self-assesses for bugs and friction, implements improvements, and commits only when cargo build and cargo test pass, reverting otherwise. Community input arrives through GitHub issues tagged agent-input, prioritized by reactions, and the agent responds to them in its own voice. Every change is documented in a JOURNAL.md entry, including reverted failures, making the improvement loop auditable. It is a small ~400-line Rust CLI built on the yoagent framework, MIT-licensed, with provider support for local LLMs (default), OpenRouter, and Anthropic. The project is an experiment with zero community traction, but its evolve workflow remains active.
