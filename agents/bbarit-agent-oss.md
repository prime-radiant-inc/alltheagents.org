---
name: "bbarit-agent-oss"
slug: "bbarit-agent-oss"
layout: "agent.njk"
category: "agent"
maker: "bbarit"
license: "MIT"
url: "https://github.com/bbarit/bbarit-agent-oss"
source_code_url: "https://github.com/bbarit/bbarit-agent-oss"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
first_released: "2026-07-16"
current_release: "2026-07-21"
stars: "160"
language: "Rust"
homepage: "https://bbarit.com"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Google Gemini/Vertex, OpenRouter, Groq, Mistral, Together, Fireworks, DeepSeek, Cerebras, Amazon Bedrock, GitHub Copilot, Ollama (15+ providers, 1000+ models)"
pricing: "Free/open-source (bring your own provider, or run a local model for $0)"
install_method: "curl -fsSL https://bbarit.com/agent/install.sh | sh (macOS/Linux); irm https://bbarit.com/agent/install.ps1 | iex (Windows); or cargo build --release; self-update via bbarit-oss --upgrade"
docs_url: "https://bbarit.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/bbarit/bbarit-agent-oss/releases"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Single self-contained Rust binary AI coding agent (no Node/Python runtime); 295 curated agent personas across 30 domains; built-in project wiki for cross-session knowledge persistence, cross-session auto-memory, bundled semantic code search (semble engine), multi-process parallel sub-agents via --orchestrate; can reuse existing Claude Code & Codex MCP servers/skills via /interop."
---

bbarit-agent-oss is a terminal-native AI coding agent distributed as a single static Rust binary with no Node or Python runtime dependency, originating from the agent inside the BBARIT desktop IDE and rewritten from Pi with documented provenance. It supports 15+ LLM providers and over a thousand models (Anthropic, OpenAI, Gemini, OpenRouter, Groq, Bedrock, Copilot, Ollama), switchable mid-session, and works fully offline with Ollama. Sessions support branching, forking, and export; a built-in project wiki persists cross-session knowledge; and an --orchestrate mode runs parallel sub-agents. 295 personas across 30 domains ship by default with a read-only persona mode, and a bundled semantic code search tool (semble) indexes repos. It is MIT-licensed, installed via curl script or cargo, and aimed at developers wanting a private, single-binary agent that owns its keys and data.
