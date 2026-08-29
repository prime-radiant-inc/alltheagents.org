---
name: "deepseek-engineer"
slug: "deepseek-engineer"
layout: "agent.njk"
category: "agent"
maker: "Doriandarko"
license: "MIT"
url: "https://github.com/Doriandarko/deepseek-engineer"
source_code_url: "https://github.com/Doriandarko/deepseek-engineer"
source_available: "Yes"
platforms: []
first_released: "2024-12-26"
current_release: "2025-05-31"
stars: "2239"
language: "Python"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "DeepSeek"
pricing: "BYOK"
install_method: "pip"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/Doriandarko/deepseek-engineer"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "A coding assistant using native function calling with DeepSeek-R1 (DeepSeek-Reasoner), featuring visible Chain-of-Thought reasoning, automatic file operations, triple-stream processing (reasoning + content + tool calls), and built-in security features like path normalization and binary file detection."
---

deepseek-engineer is a compact Python CLI that turns DeepSeek's reasoning models into a coding assistant: the model calls read_file, create_file, and edit_file functions natively, with the distinctive trait that DeepSeek-Reasoner's chain-of-thought streams visibly in the terminal while tool calls execute. Context is supplied either automatically (the assistant reads files it references) or manually via an /add command, and safety comes from path normalization, traversal protection, file-size limits, and binary detection. The project drew around 2,000 stars as a reference for wiring R1-style reasoning models to file tools but stopped receiving commits, with 26 commits total and a handful of open issues. It suits users studying function-calling agent design more than teams needing a maintained tool.
