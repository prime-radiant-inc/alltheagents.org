---
name: "nanoMuse"
slug: "nanomuse"
layout: "agent.njk"
category: "agent"
maker: "nano-muse"
license: "GPL-3.0"
url: "https://github.com/nano-muse/nanoMuse"
source_code_url: "https://github.com/nano-muse/nanoMuse"
source_available: "True"
homepage: "https://nanomuse.cn/"
docs_url: "https://nanomuse.cn/docs/"
download_url: "https://nanomuse.cn/dl/"
install_method: "Platform installers from GitHub Releases or nanomuse.cn/dl: Android 8.0+ arm64 .apk, iPhone/iPad via TestFlight, macOS 12+ .dmg, Windows 10+ .exe, Linux x64 AppImage/.deb/.tar.gz, Docker (bash scripts/self-host.sh --local) for a self-hosted relay or web app"
platforms:
  - "CLI"
  - "Web"
  - "Desktop"
  - "Autonomous"
autonomy_level:
  - "agentic"
  - "autonomous-background"
specialization: "general"
language: "Swift"
first_released: "2026-09-24"
current_release: "2026-10-29"
maintained: "active"
mcp_support: "True"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: "True"
plugin_docs_url: null
config_docs_url: "https://nanomuse.cn/docs/"
model_providers: "The community relay's free allowance, your own key at 28 providers (Alibaba Bailian, DeepSeek, Kimi/Moonshot, Zhipu GLM, SiliconFlow, Volcengine Ark, MiniMax, OpenRouter, OpenAI, Anthropic Claude, Google Gemini, xAI Grok, Groq, Mistral, Ollama/LM Studio/vLLM local, and more), or plans you already pay for (ChatGPT, Claude, Kimi)"
pricing: "freemium"
stars: "3580"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "An open-source personal agent (GPL-3.0) that runs on your own devices instead of a vendor's cloud: the phone app embeds an Alpine Linux sandbox with a shell, browser, and MCP; the desktop app is nanoMuse as plugins on the DeepSeek Harness coding agent (dsh), gaining its tools, skills, plan mode, and sub-agents; and devices meet on a self-hostable relay, cross-delegating tasks while memory and persona are plain Markdown files."
---

nanoMuse is a community project (Zhejiang University authors; arXiv 2610.08699) building an open-source counterpart to Meta's Muse: one named, faced agent that does things rather than answering questions, keeps working while the app is closed, remembers you, and stops to ask before anything it cannot undo. Each device runs its own agent: the Android app embeds an Alpine Linux environment (proot) with a shell, a browser, and MCP, built on OpenMinis; the desktop app is now nanoMuse as a plugin bundle on DeepSeek Harness (dsh) — the MIT-licensed coding agent harness supplies the agent loop, tools, skills, goals, plan mode, compaction, delegation, and MCP client, with nanoMuse's account, persona, Sentinel approvals, hands (screen operation via a UI-TARS-derived operator), and cross-device Reach added as plugins — and the Python runtime remains for the phone, the browser demo, and self-hosting. A `coding_agents` tool also steers Cursor, Codex, Claude Code, and dsh sessions found on any computer of the account. Devices sign in to a relay that carries only conversation text (files and screenshots stay local), can be self-hosted with one script, and the same account spans phone, desktop, and web with tasks delegated across them ('@Mac …' sends work to another machine, approvals come back to your hand). People who want a personal agent they can run, inspect, and host themselves are the audience; the desktop's coding capability rides on dsh inside the app, so a coding task runs end-to-end with no external host.
