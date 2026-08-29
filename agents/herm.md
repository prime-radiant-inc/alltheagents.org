---
name: "herm"
slug: "herm"
layout: "agent.njk"
category: "agent"
maker: "aduermael"
license: "MIT"
url: "https://github.com/aduermael/herm"
source_code_url: "https://github.com/aduermael/herm"
source_available: "True"
platforms:
  - "CLI"
first_released: "2026-03-03"
current_release: "2026-08-12"
stars: "220"
language: "Go (CLI), Swift (iOS/macOS app), Rust (sandbox backend)"
homepage: "https://hermagent.com"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic,OpenAI,Gemini,Grok,OpenRouter,Ollama,Azure OpenAI,Vertex AI,Bedrock"
pricing: "Free"
install_method: "curl -fsSL https://hermagent.com/install.sh | sh"
docs_url: "https://hermagent.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://hermagent.com/install.sh"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Model-agnostic, general-purpose AI coding agent that runs in containers by default; terminal-native, supports multiple isolation methods (Docker containers, in-process Unix-like sandboxes, host sandboxes like sandbox_exec/bubblewrap). Self-building dev environments scoped per project."
---

herm is a coding agent built around the idea that isolation removes the need for constant permission prompts. The CLI runs on the host, but the agent's file edits and shell commands execute inside a Docker container scoped to the current working directory, with alternative isolation backends (in-process sandboxes, macOS sandbox-exec, Linux bubblewrap) for environments without Docker. When a project needs tooling that is not installed, herm writes a per-project Dockerfile itself and rebuilds the environment, so setup happens inside the agent loop rather than as a manual prerequisite. Models are provider-agnostic and can be mixed per role — one model for main coding, a cheaper one for exploration, another for vision — across Anthropic, OpenAI, Gemini, Grok, OpenRouter, and cloud endpoints. System prompts, skills, and tool implementations are all public in the repository, and a native iOS/macOS companion app with an on-device sandbox is in development.
