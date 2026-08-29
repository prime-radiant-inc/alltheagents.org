---
name: "Patchwork"
slug: "patchwork"
layout: "agent.njk"
category: "agent"
maker: "patched-codes"
license: "AGPL-3.0"
url: "https://github.com/patched-codes/patchwork"
source_code_url: "https://github.com/patched-codes/patchwork"
source_available: "Yes"
platforms:
  - "CLI"
  - "Autonomous"
first_released: "2024-04-05"
current_release: "2026-08-09"
stars: "1572"
language: "Python"
homepage: "https://patched.codes"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Google Gemini, any OpenAI-compatible endpoint (Groq, Together, Hugging Face), local llama.cpp/Ollama/vLLM/TGI"
pricing: "open-source"
install_method: "pip install 'patchwork-cli[all]' --upgrade"
docs_url: "https://patched.codes"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/patched-codes/patchwork"
maintained: "active"
sources:
  - "hackernews"
what_makes_it_special: "Development gruntwork is codified as six predefined 'patchflows' (AutoFix, ResolveIssue, PRReview, GenerateDocstring, GenerateREADME, DependencyUpgrade) built from reusable Steps and prompt templates, runnable locally, in the IDE, or in CI, and extensible by composing new flows from an Apache-2.0 template repo."
---

Patchwork was built by Patched Codes to automate the repetitive maintenance work — dependency upgrades, PR reviews, docstring generation, security fixes — that piles up between feature projects. Instead of a free-form chat loop, it executes predefined patchflows: pipelines of reusable steps (scan code, call an LLM, edit files, open a PR) driven by customizable prompt templates, with six flows shipped out of the box including AutoFix, PRReview, and DependencyUpgrade. The same patchflows run from the CLI, inside an IDE, or in CI pipelines, and custom patchflows compose existing steps or new ones contributed through an Apache-2.0 template repository, while the core stays AGPL-3.0. Model access is flexible, spanning OpenAI, Gemini, Groq, Together, and local llama.cpp, Ollama, or vLLM endpoints configured by CLI arguments or YAML. Its users are engineering teams automating code-maintenance workflows in CI rather than developers seeking an interactive coding partner.
