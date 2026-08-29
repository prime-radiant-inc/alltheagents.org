---
name: "BIM_LLM_code_agent"
slug: "bim-llm-code-agent"
layout: "agent.njk"
category: "agent"
maker: "mac999"
license: "MIT"
url: "https://github.com/mac999/BIM_LLM_code_agent"
source_code_url: "https://github.com/mac999/BIM_LLM_code_agent"
source_available: "True"
platforms: []
first_released: "2025-01-13"
current_release: "2026-05-19"
stars: "32"
language: "Python"
homepage: null
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Ollama (CodeGemma, Qwen2.5-coder, Llama3, Gemma3), optionally LangChain/HuggingFace/Tavily via API keys"
pricing: "Free/open source"
install_method: "Clone repo, pip install dependencies, set up .env with API keys, pull Ollama models, run with streamlit run bim_code_agent_app.py"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/mac999/BIM_LLM_code_agent"
maintained: "active"
sources:
  - "github_deep"
what_makes_it_special: "Open-source BIM (Building Information Modeling) LLM Code Agent tailored for the AEC (Architecture, Engineering, Construction) industry, bridging complex BIM/IFC file analysis and LLM-driven code generation/reasoning via Vector and Graph RAG. Acts as an interactive knowledge expert for BIM professionals to automate data extraction and visualization."
---

BIM (Building Information Modeling) files in the IFC format are large, semantically dense structures that general-purpose coding tools handle poorly, so this research agent targets the AEC industry specifically. It answers natural-language questions about building models by generating and running Python code against ifcopenshell, supported by a LangChain multi-agent system with memory layers, FAISS vector stores, and a code knowledge base accessed through both Vector RAG and Graph RAG. It runs OpenAI models alongside local Ollama models (codegemma, qwen2.5-coder, llama3, llama3), and a Streamlit web UI makes it approachable for AEC professionals who do not write code. Outputs include extracted data tables and 2D/3D Plotly visualizations. The project is a research artifact tied to published academic work, actively iterated by its author with an English/Korean bilingual README, and used by BIM researchers and AEC practitioners exploring LLM-driven IFC analysis.
