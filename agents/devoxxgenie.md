---
name: "DevoxxGenie"
slug: "devoxxgenie"
layout: "agent.njk"
category: "agent"
maker: "Devoxx"
license: "MIT"
url: "https://plugins.jetbrains.com/plugin/24169-devoxxgenie"
source_code_url: null
source_available: "yes"
platforms:
  - "IDE"
first_released: "2026-08-26"
current_release: null
stars: null
language: "Java"
homepage: "https://devoxx.com"
mcp_support: "True"
plugin_support: "yes"
claude_code_plugin: "no"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Anthropic, Ollama"
pricing: "open-source"
install_method: "Install from the JetBrains Marketplace"
docs_url: "https://genie.devoxx.com"
plugin_docs_url: null
config_docs_url: null
download_url: "https://plugins.jetbrains.com/plugin/24169-devoxxgenie"
maintained: "active"
sources:
  - "gap-2026-08-20"
what_makes_it_special: "Open-source AI coding assistant supporting local and cloud LLMs"
---

DevoxxGenie started as a chat-with-your-code plugin for IntelliJ and grew into a full agent surface: the agent loop executes edits and shell work, a Spec Browser tracks tasks from Backlog.md, and the Agent Loop batch-runs dependent tasks in order. SKILL.md files dropped into project or user directories activate mid-conversation, the same files Claude Code and Codex read, and ACP/CLI runners let the plugin drive external agents like Kimi, Gemini CLI, or Claude Code. Local LLMs get first-class treatment with fill-in-the-middle completion via Ollama or LM Studio, and security scanning (Gitleaks, OpenGrep, Trivy) files findings as prioritized tasks. It suits Java-centric developers who want agentic workflows in IntelliJ without abandoning local models.
