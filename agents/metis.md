---
name: "Metis"
slug: "metis"
layout: "agent.njk"
category: "agent"
maker: "Wholiver"
license: "MIT"
url: "https://github.com/Wholiver/metis"
source_code_url: "https://github.com/Wholiver/metis"
source_available: "True"
homepage: "https://metisagent.tech/"
docs_url: "https://github.com/Wholiver/metis/blob/main/docs/index.md"
download_url: "https://github.com/Wholiver/metis/releases/latest"
install_method: "Desktop installer from GitHub Releases (.dmg / .exe, Node runtime bundled); npm install -g @wholiver_hu/metis (Node.js 22.19+); Skill mode for other agents: npm install -g metis-skill"
platforms:
  - "Desktop"
  - "CLI"
autonomy_level:
  - "agentic"
specialization: "general"
language: "TypeScript"
first_released: "2026-07-11"
current_release: "2026-10-16"
maintained: "dead"
mcp_support: "False"
plugin_support: "True"
claude_code_plugin: null
subagents: "True"
hooks: "True"
plan_mode: "True"
plugin_docs_url: "https://github.com/Wholiver/metis/blob/main/docs/extensions.md"
config_docs_url: "https://github.com/Wholiver/metis/blob/main/docs/settings.md"
model_providers: "Anthropic, OpenAI, DeepSeek, Google Gemini, xAI, Kimi, MiniMax, SiliconFlow, OpenRouter, NVIDIA NIM, Mistral, Groq, Cerebras, and 20+ more by API key; subscription logins for Claude Pro/Max, ChatGPT (Codex), and GitHub Copilot"
pricing: "free"
stars: "444"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "An open-source coding agent that runs standalone as a desktop app or terminal CLI and also installs as a Skill into Codex, OpenCode, or DeepSeek Harness; each project keeps an editable copy of the agent's own workflow graph in .metis/harness.json, and one of five task tiers is picked automatically per task."
---

Metis set out to lift cheaper models like DeepSeek to frontier-tier coding by shaping the harness rather than the model: work routes through separate planning, implementation, review, and testing roles coordinated from a graph each project can edit, and the whole thing builds on the pi coding agent by Mario Zechner. It ships as a desktop app with chat, routines, and Git views, and as a terminal CLI on npm, with subscription logins (Claude Pro/Max, ChatGPT/Codex, GitHub Copilot) alongside a long list of API-key providers. A bilingual English/Chinese README, a QQ community, and a SiliconFlow inference partnership mark its audience; the author archived the repository in November 2026, so the last release installs and runs but the project no longer evolves.
