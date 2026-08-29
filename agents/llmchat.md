---
name: "Llmchat"
slug: "llmchat"
layout: "agent.njk"
category: "other"
maker: "c0sogi"
license: "MIT"
url: "https://github.com/c0sogi/LLMChat"
source_code_url: "https://github.com/c0sogi/LLMChat"
source_available: "True"
platforms:
  - "Web"
first_released: "2023-03-01"
current_release: "2024-07-25"
stars: "290"
language: "Python, Dart"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, LlamaCpp, Exllama"
pricing: "open-source"
install_method: "docker-compose -f docker-compose-local.yaml up; or python -m main"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/c0sogi/llmchat.git"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Full-stack web UI for chatting with LLMs (ChatGPT, LLaMA, etc.) with web browsing (DuckDuckGo), vector embedding (Redis), auto-summarization, WebSocket real-time streaming, PDF upload/embedding, and local LLM support."
---

LLMChat dates from early 2023, when running LLaMA weights locally required stitching together llama.cpp or ExLlama by hand, and it wrapped those backends plus the OpenAI API behind one authenticated web interface. Conversations stream over WebSockets, a browse toggle adds DuckDuckGo search to replies, and PDF or text uploads are embedded into Redis for retrieval-style memory, with automatic summarization keeping long histories within context limits. FastAPI handles the backend while Flutter serves the same UI to browsers and mobile devices. Development stopped in 2024, leaving a representative but unmaintained example of the pre-agent chat-client era.
