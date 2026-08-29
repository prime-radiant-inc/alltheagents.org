---
name: "browser-operator-core"
slug: "browser-operator-core"
layout: "agent.njk"
category: "agent"
maker: "BrowserOperator"
license: "BSD-3-Clause"
url: "https://github.com/BrowserOperator/browser-operator-core"
source_code_url: "https://github.com/BrowserOperator/browser-operator-core"
source_available: "True"
platforms:
  - "Web"
first_released: "2025-05-10"
current_release: "2026-03-19"
stars: "500"
language: "C++, JavaScript, TypeScript"
homepage: "https://browseroperator.io/"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
model_providers: "OpenRouter, OpenAI, Groq, LiteLLM (Ollama)"
pricing: null
install_method: "Download binaries from GitHub Releases (macOS 10.15+, Windows 10 64-bit+)"
docs_url: "https://docs.browseroperator.io"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "Open-source, privacy-focused AI browser running locally on a Chromium fork with a multi-agent platform for autonomous web automation. All processing happens locally; supports complete offline operation via Ollama. Compatible with 100+ AI models. Open-source alternative to ChatGPT Atlas, Perplexity Comet, Dia, and Microsoft Copilot Edge Browser."
---

browser-operator-core is an open-source AI browser built as a fork of Chromium (28,000+ commits on its main branch), embedding a multi-agent automation platform directly into the browser rather than bolting it on through an extension or Playwright layer. Agents coordinate to complete research, shopping, and business-automation tasks — literature reviews, price tracking, lead generation, compliance audits — using computer-use-style interaction with pages. Model backends are pluggable across OpenRouter, OpenAI, Groq, and LiteLLM-proxied Ollama, so the whole stack can run offline with local models; MCP support allows connecting external tool servers. The project positions itself as an open alternative to ChatGPT Atlas, Perplexity Comet, Dia, and Microsoft's Copilot-bundled Edge, with privacy as the selling point: all inference and automation run locally under BSD-3-Clause licensing. It suits users and teams who need autonomous web work without sending browsing data to a cloud provider.
