---
name: "Docker Agent"
slug: "docker-agent"
layout: "agent.njk"
category: "agent"
maker: "docker"
license: "Apache-2.0"
url: "https://docker.github.io/docker-agent/"
source_code_url: "https://github.com/docker/docker-agent"
source_available: "True"
homepage: null
docs_url: "https://docs.docker.com/ai/docker-agent/"
download_url: "https://github.com/docker/docker-agent/releases"
install_method: "Pre-installed in Docker Desktop 4.63+ (run `docker agent`); `brew install docker-agent`; `winget install Docker.Agent`; or download binaries from GitHub Releases (standalone `docker-agent` or symlinked as a `docker` CLI plugin)"
platforms:
  - "CLI"
  - "Autonomous"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Go"
first_released: "2025-09-01"
current_release: "2026-11-18"
maintained: "active"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "False"
plugin_docs_url: null
config_docs_url: "https://docs.docker.com/ai/docker-agent/configuration/overview/"
model_providers: "OpenAI, Anthropic, Google Gemini, AWS Bedrock, Mistral, xAI, and local models through Docker Model Runner (Ollama, vLLM, LocalAI); 30+ more providers documented"
pricing: "free"
stars: "4692"
sources:
  - "github-issue"
last_verified: "2026-11-18"
date_added: "2026-11-18"
what_makes_it_special: "Agents and multi-agent teams are defined in YAML and shared as OCI artifacts through any registry, with built-in tools, MCP servers, cloud or local models, and an optional sandbox mode that runs the agent inside a Docker Sandboxes microVM. It also exposes agents over the Agent Client Protocol for ACP-compatible IDEs and editors."
---

Docker Agent grew out of Docker Engineering as an open-source, Go-built agent runtime that treats agents the way docker run treats containers: a declarative YAML or HCL file names the model, instructions, and toolsets, and one command runs it. It ships as a docker CLI plugin — pre-installed in Docker Desktop 4.63+, where the same feature had been called cagent in 4.49–4.62 — and standalone via Homebrew, winget, or GitHub binaries. An agent works interactively in a terminal UI or headless in CI, draws on many cloud providers or local models through Docker Model Runner, and can delegate coding to external harnesses such as Claude Code, Codex, or opencode as sub-agents. The project dogfoods itself with its own golang_developer.yaml agent, and it is aimed at developers who want agents in their workflow without glue code.
