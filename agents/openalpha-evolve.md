---
name: "OpenAlpha_Evolve"
slug: "openalpha-evolve"
layout: "agent.njk"
category: "agent"
maker: "shyamsaktawat"
license: "MIT"
url: "https://github.com/shyamsaktawat/OpenAlpha_Evolve"
source_code_url: "https://github.com/shyamsaktawat/OpenAlpha_Evolve"
source_available: "True"
platforms:
  - "Autonomous"
first_released: "2025-05-17"
current_release: "2025-05-31"
stars: "1045"
language: "Python"
homepage: "https://github.com/shyamsaktawat/OpenAlpha_Evolve"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "yes"
hooks: "no"
plan_mode: "no"
model_providers: "OpenAI, Anthropic, Google (Gemini/Vertex AI), Cohere (via LiteLLM)"
pricing: "open-source"
install_method: "pip, docker"
docs_url: "https://github.com/shyamsaktawat/OpenAlpha_Evolve#readme"
plugin_docs_url: null
config_docs_url: "https://github.com/shyamsaktawat/OpenAlpha_Evolve#readme"
download_url: "https://github.com/shyamsaktawat/OpenAlpha_Evolve"
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "Open-source framework inspired by DeepMind's AlphaEvolve that combines evolutionary algorithms with LLM-driven code generation using diff-based mutations and bug fixes. Sandboxed Docker execution for security, modular multi-agent architecture (PromptDesigner, CodeGenerator, Evaluator, Database, SelectionController, TaskManager), and Gradio web UI for interactive task definition."
---

DeepMind's AlphaEvolve showed that evolutionary search over LLM-generated programs can produce algorithms that beat hand-written baselines, but the system was never released. OpenAlpha_Evolve reconstructs the concept in Python: a PromptDesignerAgent frames the task, a CodeGeneratorAgent writes and mutates candidate programs as diffs, an EvaluatorAgent runs them against tests inside Docker containers, a DatabaseAgent archives the population, and a SelectionControllerAgent drives generations forward. Models route through LiteLLM with Gemini as the default configuration, and candidates can also be inspected through a Gradio web UI. Tasks are defined in YAML examples (shortest path among them), and the whole loop runs from a single python -m main invocation after cloning and pip installing. Researchers and hobbyists in evolutionary computation and LLM-driven program synthesis use it as an accessible AlphaEvolve-style testbed; the repo is experimental and community-maintained.
