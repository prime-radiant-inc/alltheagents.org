---
name: "Nous"
slug: "nous"
layout: "agent.njk"
category: "agent"
maker: "TrafficGuard"
license: "MIT"
url: "https://github.com/TrafficGuard/nous"
source_code_url: "https://github.com/TrafficGuard/nous"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2024-04-10"
current_release: "2025-12-22"
stars: "1193"
language: "TypeScript"
homepage: "https://typedai.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "yes"
model_providers: "OpenAI, Anthropic, Google Gemini, Groq, Fireworks, Together.ai, DeepSeek, Ollama, Cerebras, SambaNova, OpenRouter, X.ai"
pricing: "open-source"
install_method: "docker"
docs_url: "https://typedai.dev/"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Note: the repo at TrafficGuard/nous contains a project named 'TypedAI' (the repo may have been renamed/redirected). TypeScript-first AI platform for developing and running autonomous AI agents, LLM-based workflows, and chatbots. Does NOT use LangChain (intentional design decision). Automated LLM function schema generation via @func decorators (no JSON/zod duplication). Multi-agent extend-reasoning. Full SDLC support (code editing, PR creation, code review). Sandboxed code execution. OpenTelemetry-based observability."
---

TypedAI (the project in the TrafficGuard/nous repository) is a TypeScript platform for building autonomous agents, LLM workflows, and chatbots without LangChain, using static typing and simple control flow so behavior is debuggable with ordinary breakpoints. Its software-engineering agents cover local code editing with an edit-compile-lint-test-fix loop, ticket-to-PR workflows across GitHub and GitLab, and configurable code review with inline merge request comments. Function schemas are generated from source via a decorator, avoiding duplicate schema definitions. Deployment spans local CLI, Docker, or scale-to-zero Google Cloud Run with SSO, and the codebase is partly maintained by its own agents. A web UI and Slack chatbot provide interfaces beyond the terminal.
