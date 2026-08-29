---
name: "ocode"
slug: "ocode"
layout: "agent.njk"
category: "agent"
maker: "haasonsaas"
license: "AGPL-3.0"
url: "https://github.com/haasonsaas/ocode"
source_code_url: "https://github.com/haasonsaas/ocode"
source_available: "True"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: "2025-05-27"
current_release: "2026-05-18"
stars: "128"
language: "Python"
homepage: null
mcp_support: "True"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "True"
hooks: "no"
plan_mode: "no"
model_providers: "Ollama"
pricing: "Free (AGPL-3.0); uses your own local Ollama models"
install_method: "curl -fsSL https://raw.githubusercontent.com/haasonsaas/ocode/main/scripts/install.sh | bash; or pip install -e .; or pipx install git+https://github.com/haasonsaas/ocode.git"
docs_url: "https://github.com/haasonsaas/ocode/blob/main/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/haasonsaas/ocode"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Terminal-native AI coding assistant powered by local Ollama models; 19+ specialized tools; full MCP server support (resources, tools, prompts); agent tool delegates complex tasks to specialized agents; fully offline and self-hosted"
---

ocode is a terminal-native coding assistant that streams from a local Ollama instance, requiring no API keys or cloud proxies. It ships nineteen specialized tools covering file operations, grep and diff, git, shell execution, Jupyter notebooks, and architecture analysis, with a smart tool-selection layer that detects multi-action requests. An agent tool delegates complex tasks to specialized subagents for multi-step work. Full MCP support lets it expose resources, tools, and prompts as a server as well as consume them. The permission system is whitelist-first with sandboxed shell execution and blocked paths by default, reflecting a security-first posture rare in solo hobby agents.
