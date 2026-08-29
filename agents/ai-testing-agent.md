---
name: "Ai-Testing-Agent"
slug: "ai-testing-agent"
layout: "agent.njk"
category: "agent"
maker: "furudo-erika"
license: null
url: "https://github.com/furudo-erika/ai-testing-agent"
source_code_url: "https://github.com/furudo-erika/ai-testing-agent"
source_available: "True"
platforms: []
first_released: "2024-12-19"
current_release: "2024-12-19"
stars: "47"
language: "Python (FastAPI, LangChain, pytest)"
homepage: null
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenRouter"
pricing: "Free (BYO OpenRouter API key)"
install_method: "Clone repo, pip install fastapi uvicorn requests pytest langchain openai, set OPENROUTER_API_KEY env var, run python agent.py"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/furudo-erika/ai-testing-agent"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Open-source AI agent for software testing. Uses an LLM via OpenRouter to automatically generate test plans, generate pytest test code for API endpoints, run tests, and iteratively refine based on natural-language feedback. Single LangChain agent with plan/generate/run/feedback tools. Only 1 commit, last activity ~2023."
---

The agent generates a textual test plan, converts it into pytest code for REST API endpoints, executes the tests, and accepts free-form feedback to extend or correct them, overwriting generated_tests.py on each cycle. Mechanically, a LangChain chat agent invokes tools that spawn api_tester.py subprocesses; the LLM (via an OpenRouter API key) writes the test file, and pytest runs it against a configurable endpoint, with a bundled FastAPI demo app for local trials. It is a single-commit proof of concept: no license file, leftover copy files, 48 stars, and no activity since December 2024. Developers evaluating API test generation can run it by cloning the repo and setting OPENROUTER_API_KEY.
