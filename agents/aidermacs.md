---
name: "aidermacs"
slug: "aidermacs"
layout: "agent.njk"
category: "other"
maker: "MatthewZMD"
license: "Apache-2.0"
url: "https://github.com/MatthewZMD/aidermacs"
source_code_url: "https://github.com/MatthewZMD/aidermacs"
source_available: "True"
platforms:
  - "IDE"
first_released: "2025-02-11"
current_release: "2026-08-16"
stars: "922"
language: "Emacs Lisp"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "yes — aidermacs-before-run-backend-hook for custom setup before starting Aider backend"
plan_mode: "yes — Architect Mode uses two specialized models (Architect for reasoning/planning, Editor for code generation); requires explicit confirmation before applying changes"
model_providers: "OpenAI, Anthropic, DeepSeek, Google Gemini, OpenRouter, Ollama, LiteLLM"
pricing: "open-source"
install_method: "emacs"
docs_url: "https://melpa.org/#/aidermacs"
plugin_docs_url: null
config_docs_url: "https://aider.chat/docs/config/options.html"
download_url: null
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Emacs-native AI pair programming integrating Aider with built-in Ediff integration for reviewing AI-generated changes, Architect Mode (dual-model approach achieving SOTA on code editing benchmarks), and native multiline input."
---

The package is a community-driven fork of aider.el that rebuilt the integration to be Emacs-native: Magit-style transient menus, comint or vterm backends, Tramp support for remote files, and file watching for AI! comment markers under vterm. Diff review defaults to Ediff so changes are inspected with the editor's own tooling rather than a custom UI. It targets Emacs 26.1+ with Aider installed via uv, discovers models dynamically from OpenAI, Anthropic, DeepSeek, Gemini, OpenRouter, or any OpenAI-compatible endpoint through Ollama or LiteLLM. Distributed via MELPA and NonGNU ELPA with CI, it is the actively maintained Emacs front end for Aider (660 commits, Apache-2.0).
