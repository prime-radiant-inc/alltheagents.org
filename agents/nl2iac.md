---
name: "Nl2Iac"
slug: "nl2iac"
layout: "agent.njk"
category: "agent"
maker: "ramonbgc"
license: null
url: "https://github.com/ramonbgc/nl2iac"
source_code_url: "https://github.com/ramonbgc/nl2iac"
source_available: "True"
platforms: []
first_released: "2024-05-07"
current_release: "2024-09-23"
stars: "1"
language: "Python (Streamlit)"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: null
plan_mode: null
model_providers: "Google (Gemini 1.5 Flash), OpenAI (GPT-4o)"
pricing: "Free / open-source"
install_method: "git clone; pip install -r requirements.txt; configure .streamlit/secrets.toml with GCP/OpenAI credentials"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/ramonbgc/nl2iac"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "NOTE: Not a coding agent harness. Domain-specific agent that translates natural language to Infrastructure as Code (IaC) deployments with multi-LLM provider support. Early stage (9 commits, 1 star)."
---

nl2iac is a personal experiment converting natural-language requests into Terraform configuration and driving GCP deployments from a Streamlit interface. A configuration toggle switches between Google Gemini and OpenAI models, with optional LangSmith tracing. The pipeline is intentionally narrow: NL input in, Terraform out, applied against a configured GCP project and region. The repository shows nine commits, no releases, and no license file, marking it as a single-author experiment rather than a maintained tool. It demonstrates the NL-to-IaC pattern at toy scale rather than production use.
