---
name: "vim_codex"
slug: "vim-codex"
layout: "agent.njk"
category: "other"
maker: "tom-doerr"
license: "MIT"
url: "https://github.com/tom-doerr/vim_codex"
source_code_url: "https://github.com/tom-doerr/vim_codex"
source_available: "True"
platforms:
  - "IDE"
first_released: "2021-08-27"
current_release: "2024-03-28"
stars: "286"
language: "Python, Vim script"
homepage: "https://github.com/tom-doerr/vim_codex"
mcp_support: "no"
plugin_support: "True"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI (Codex API)"
pricing: "free"
install_method: "Install as Vim bundle (Pathogen, Vundle) via git clone, then pip3 install openai"
docs_url: "https://github.com/tom-doerr/vim_codex#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/tom-doerr/vim_codex"
maintained: "dormant"
sources:
  - "github_deep"
what_makes_it_special: "AI plugin for Vim that enables OpenAI Codex-powered code completion directly in the editor; provides CreateCompletion and CreateCompletionLine commands. Uses deprecated OpenAI Codex API."
---

vim_codex comes from the first wave of API-based AI coding tools, when OpenAI's Codex models were the state of the art and editor integration meant one completion request per trigger. The plugin added two commands — CreateCompletion, which sends the current buffer context to the Codex API and inserts the result (optionally sized by a token-count argument), and CreateCompletionLine for completing the current line — with configuration in ~/.config/openaiapirc and installation through any Vim bundle manager. It served Vim users who wanted Codex completions without leaving the editor, before agentic tools existed. OpenAI deprecated and shut down the Codex models in March 2023, so the plugin no longer works; with no releases and no updates, it remains only as a historical example of early editor-AI integration.
