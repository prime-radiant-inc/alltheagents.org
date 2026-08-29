---
name: "VerbalCodeAi"
slug: "verbalcodeai"
layout: "agent.njk"
category: "agent"
maker: "vibheksoni"
license: "MIT"
url: "https://github.com/vibheksoni/VerbalCodeAi"
source_code_url: "https://github.com/vibheksoni/VerbalCodeAi"
source_available: "True"
platforms:
  - "CLI"
first_released: "2025-05-17"
current_release: "2025-06-07"
stars: "59"
language: "Python"
homepage: "https://verbalcode.xyz/"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "Ollama, Google AI, OpenAI, Anthropic, Groq, OpenRouter"
pricing: "Free/open source"
install_method: "Clone repo + run setup_windows.bat (Windows) or setup_linux.sh (Linux/macOS); or pip install -r requirements.txt"
docs_url: "https://verbalcode.xyz"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/vibheksoni/VerbalCodeAi"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "AI-powered codebase navigation directly in terminal; local-first (Ollama) with privacy focus; intelligent code search via embeddings; agent mode with tool suite; MCP integration for Claude Desktop; git history analysis; memory system."
---

VerbalCodeAI exists for developers who would rather ask an unfamiliar codebase questions than grep through it, and who do not want that code leaving their machine. It indexes the project locally with embeddings, then answers natural-language questions through semantic search backed by grep and regex fallback; its agent mode adds a broad tool suite — file reading, directory trees, symbol lookup, cross-references, git history, a memory system, web search, and command execution — with an ask_buddy tool that solicits a second model's opinion. An MCP server wraps the HTTP API so Claude Desktop and Cursor can call ask_agent or trigger indexing as external tools, and chat mode streams answers with markdown rendering. Privacy-conscious developers and students running local Ollama models are the primary users; the project is a small hobby-scale effort (36 commits, no releases) with a website at verbalcode.xyz.
