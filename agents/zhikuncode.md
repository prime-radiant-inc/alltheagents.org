---
name: "zhikuncode"
slug: "zhikuncode"
layout: "agent.njk"
category: "agent"
maker: "zhikunqingtao"
license: "MIT"
url: "https://github.com/zhikunqingtao/zhikuncode"
source_code_url: "https://github.com/zhikunqingtao/zhikuncode"
source_available: "True"
platforms:
  - "CLI"
  - "Web"
first_released: "2026-04-06"
current_release: "2026-08-13"
stars: "456"
language: "Java, TypeScript, Python"
homepage: null
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "DashScope (Qwen), DeepSeek, Moonshot (Kimi), Zhipu (GLM), MiniMax, ZenMux (Claude/OpenAI/Gemini), OpenAI, Ollama, OpenAI-compatible"
pricing: "Free / open-source (MIT); users supply their own LLM API keys"
install_method: "Docker: git clone, cp .env.example .env, docker compose up -d, access http://localhost:8080; or local dev via ./start.sh (JDK 21, Node 22+, Python 3.11-3.12)"
docs_url: "https://zhikunqingtao.github.io/zhikuncode/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/zhikunqingtao/zhikuncode"
maintained: "active"
sources:
  - "web_search_multilingual"
what_makes_it_special: "Browser-based full-process control of an AI coding agent (no client install, works on phone/iPad); 8-layer Bash security sandbox; 6-layer context compression cascade; SWE-bench Lite 56.0%; native Chinese LLM support"
---

zhikuncode inverts the usual client-side architecture: instead of a desktop app or terminal TUI, the agent runs as a self-hosted Docker stack and every interaction — conversation, permission approvals, plan negotiation, file browsing, terminal — happens in a browser tab, which means an instance deployed once is controllable from a laptop, tablet, or phone. Internally it is three services in one container: a Java/Spring Boot orchestration engine running the agent loop with SQLite-backed sessions, a React front end with Monaco editor and xterm.js terminal, and a Python FastAPI sidecar for AST analysis and MCP bridging. Security gets the deepest treatment: shell commands pass eight layers from parsing and blacklist filtering through Docker sandboxing with read-only filesystems and network isolation to output sanitization and audit logging, all funneled through a single authorization gateway with scoped, time-bounded approvals. Context management uses a six-layer compression cascade rather than naive truncation, and a self-correction loop retries failed fixes. Model support centers on Chinese providers — DashScope/Qwen, DeepSeek, Kimi, Zhipu GLM, MiniMax — plus OpenAI-compatible endpoints and offline Ollama, which matters for users behind the Great Firewall. Multi-agent operation ships in three modes (Team, Swarm, SubAgent) with isolation levels, and the project publishes a reproducible SWE-bench Lite score of 56.0% using a single qwen3.7-max model with a six-tool closed set. It is used by developers who want a phone-accessible, self-hosted agent with native Chinese LLM support.
