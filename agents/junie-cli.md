---
name: "Junie CLI"
slug: "junie-cli"
layout: "agent.njk"
category: "agent"
maker: null
license: "Proprietary (© JetBrains s.r.o. — subject to JetBrains AI Service Terms)"
url: "https://junie.jetbrains.com"
source_code_url: null
source_available: "No (repo contains only install scripts, registries, templates, and issue tracking; CLI source is closed)"
platforms:
  - "CLI"
  - "IDE"
  - "Autonomous"
first_released: null
current_release: null
stars: null
language: null
homepage: null
mcp_support: null
plugin_support: "yes (Agent Skills packages and /commands shared across CLI + IDE via ACP)"
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: "yes (Advanced Plan Mode writes structured plan — requirements, design, delivery — before touching code; plans stored in .junie/plans; strategy: plan on Opus, implement on Flash)"
model_providers: "JetBrains Account, Junie API Key, BYOK: Anthropic, OpenAI, Google, xAI, OpenRouter, Copilot (10+ models including GPT-5.6, Claude Opus 4.8, Gemini 3.1 Pro, Grok 4.5)"
pricing: "Free: 5 AI credits; BYOK at provider-rate (zero markup); AI Pro: $8.33/user/mo (annual); AI Ultimate: $25/user/mo (annual)"
install_method: "curl -fsSL https://junie.jetbrains.com/install.sh | bash; Homebrew (brew tap jetbrains-junie/junie && brew install junie); npm install -g @jetbrains/junie"
docs_url: "https://junie.jetbrains.com/docs/"
plugin_docs_url: null
config_docs_url: null
download_url: "https://junie.jetbrains.com/install.sh"
maintained: "active"
sources:
  - "brad"
  - "ishandutta"
what_makes_it_special: "LLM-agnostic coding agent powered by IntelliJ IDEA Engine (top performer on SWE-Rebench); model-agnostic BYOK with cost-efficient 'plan on Opus, implement on Flash' strategy; Live Prompting to steer agent mid-task in real time; remote async execution via CLI + web app; human-in-the-loop with dynamic allowlist; SOC 2 certified."
---

LLM-agnostic coding agent powered by IntelliJ IDEA Engine (top performer on SWE-Rebench); model-agnostic BYOK with cost-efficient 'plan on Opus, implement on Flash' strategy; Live Prompting to steer agent mid-task in real time; remote async execution via CLI + web app; human-in-the-loop with dynamic allowlist; SOC 2 certified.
