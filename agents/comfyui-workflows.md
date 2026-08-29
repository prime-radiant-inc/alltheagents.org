---
name: "Comfyui_Workflows"
slug: "comfyui-workflows"
layout: "agent.njk"
category: "other"
maker: "cubiq"
license: "Apache-2.0"
url: "https://github.com/cubiq/ComfyUI_Workflows"
source_code_url: "https://github.com/cubiq/ComfyUI_Workflows"
source_available: "True"
platforms: []
first_released: "2023-08-21"
current_release: "2024-01-10"
stars: "856"
language: "JSON"
homepage: null
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: "None (image-generation workflows for Stable Diffusion, not LLM coding agents)"
pricing: "open-source"
install_method: null
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/cubiq/ComfyUI_Workflows"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Repository of well-documented, readability-first ComfyUI workflow examples for learning Stable Diffusion techniques (basic, upscale, text2img, image conditioning, in/out painting, guided composition); almost all workflows run on vanilla ComfyUI without plugins."
---

This repository collects documented ComfyUI workflow examples for Stable Diffusion, ordered as a learning path from basic text-to-image through upscaling, word weighting and embeddings, image conditioning, inpainting and outpainting, and ControlNet-guided composition. Each workflow is a JSON file arranged for readability - flowing left to right, mostly working without plugins - so a reader can trace how data moves through the graph. An experiments directory covers advanced techniques beyond the core path. The cubiq repository became a standard reference for people learning node-based image generation, and it has no connection to coding agents; its census slot reflects a data-entry mismatch rather than a judgment call about category boundaries.
