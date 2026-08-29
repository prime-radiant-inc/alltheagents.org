---
name: "agentic-coding-quickstart"
slug: "agentic-coding-quickstart"
layout: "agent.njk"
category: "other"
maker: "GSA-TTS"
license: "CC0-1.0"
url: "https://github.com/GSA-TTS/agentic-coding-quickstart"
source_code_url: "https://github.com/GSA-TTS/agentic-coding-quickstart"
source_available: "True"
platforms: []
first_released: "2026-02-27"
current_release: "2026-08-19"
stars: "27"
language: "Shell"
homepage: "https://console.gsa.usai.gov"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "USAi"
pricing: "Free / open-source"
install_method: "git clone, then ./acq run opencode <path>; requires microsandbox (Homebrew/curl) or Docker"
docs_url: "https://github.com/GSA-TTS/agentic-coding-quickstart/blob/main/docs/QUICKSTART.md"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/GSA-TTS/agentic-coding-quickstart"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Built for U.S. federal teams — integrates with the USAi government AI API, enforces sandbox isolation (microsandbox microVMs or Docker) for safety, handles federal compliance (Zscaler CA, git commit signing), and auto-provisions federal-relevant agent skills via a kits system."
---

Federal engineering teams cannot use consumer AI coding tools as-is: data must stay inside approved systems, Zscaler intercepts TLS, and commits require signing, so GSA-TTS built this quickstart to make compliant agent setup a one-command operation. Running ./acq opencode launches the opencode agent inside a microsandbox microVM (or Docker) wired to the USAi LLM gateway at api.gsa.usai.gov, with USAi keys and GitHub tokens injected at runtime so secrets never enter the guest VM, and Zscaler certificate handling plus git commit signing configured automatically. It is one of three companion repositories (with Playbook and Patterns) and ships reusable agent skills for federal compliance, code review, and secure development. Its users are US government engineering teams adopting AI coding under federal constraints.
