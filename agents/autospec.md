---
name: "Autospec"
slug: "autospec"
layout: "agent.njk"
category: "agent"
maker: "zachblume"
license: "MIT"
url: "https://github.com/zachblume/autospec"
source_code_url: "https://github.com/zachblume/autospec"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2024-05-20"
current_release: "2026-05-15"
stars: "61"
language: "TypeScript"
homepage: "https://autospec.dev"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "False"
subagents: "no"
hooks: "no"
plan_mode: "True"
model_providers: "Anthropic, OpenAI, Google Gemini"
pricing: "BYOK"
install_method: "npx autospecai"
docs_url: "https://autospec.dev"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/zachblume/autospec"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Open-source AI agent that autonomously explores a web app URL, generates commonsense e2e test specifications, executes them, and saves passing tests as reusable Playwright .spec.js files"
---

autospec addresses the bootstrap problem in end-to-end testing: writing the first meaningful Playwright specs for a web app is tedious, so the agent does it. Given just a URL, it crawls up to three pages, generates commonsense test specifications via an LLM, executes them in parallel with semantic browser actions (click by role, fill by label), and judges correctness from accessibility snapshots rather than rigid prior-state comparison. Passing tests are saved as standard Playwright .spec.js files in a trajectories/ folder, ready to run with npx playwright test and extend manually. Model choice (Claude, GPT, Gemini) is pluggable via the Vercel AI SDK, and no configuration beyond a URL and API key is required. QA engineers and developers use it to bootstrap e2e coverage quickly before refining specs by hand.
