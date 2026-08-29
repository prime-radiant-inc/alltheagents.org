---
name: "Blinky"
slug: "blinky"
layout: "agent.njk"
category: "agent"
maker: "seahyinghang8"
license: "MIT"
url: "https://github.com/seahyinghang8/blinky"
source_code_url: "https://github.com/seahyinghang8/blinky"
source_available: "True"
platforms:
  - "IDE"
first_released: "2024-05-22"
current_release: "2024-06-03"
stars: "90"
language: "TypeScript"
homepage: null
mcp_support: "no"
plugin_support: null
claude_code_plugin: "False"
subagents: null
hooks: null
plan_mode: null
model_providers: "OpenAI"
pricing: "Free / open-source (MIT)"
install_method: "Install Blinky VSCode extension from the VSCode marketplace"
docs_url: "https://github.com/seahyinghang8/blinky#readme"
plugin_docs_url: null
config_docs_url: null
download_url: "https://marketplace.visualstudio.com/items?itemName=blinky.blinky"
maintained: "active"
sources:
  - "e2b"
what_makes_it_special: "Open-source AI debugging agent for VSCode inspired by SWE-agent; embeds a debugging loop directly inside VSCode for real-time developer feedback mid-run; LSP-based navigation tools (GoToDefinition, GetAllReferences, GetFilesRelevantToEndpoint); match-and-replace file editing technique (generating original text with line numbers) to reduce LLM hallucination and indentation errors; Verify tool runs user-specified repro steps and uses execution feedback to iteratively debug until tests pass; focused on backend systems. Early stage."
---

Blinky brings the SWE-agent debugging loop into the editor rather than the terminal, targeting backend developers who want an agent that fixes bugs in place. A user describes a bug plus optional reproduction steps; the agent iterates — reading code through LSP-derived tools like GoToDefinition and GetAllReferences, editing via a match-and-replace scheme that forces the model to re-emit the original text to catch hallucinations — until a user-specified Verify step passes. Because it runs in VS Code, feedback can arrive mid-run, and the developer watches the loop rather than waiting for a batch result. The project is small and early-stage: seven commits, an MIT-licensed TypeScript extension on the marketplace, OpenAI as the only provider, and a roadmap (more models, broader codebase support) that has not progressed since mid-2024. It remains a reference implementation of editor-embedded debugging loops more than a daily-driver tool.
