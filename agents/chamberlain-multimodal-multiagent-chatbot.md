---
name: "Chamberlain_Multimodal_Multiagent_Chatbot"
slug: "chamberlain-multimodal-multiagent-chatbot"
layout: "agent.njk"
category: "other"
maker: "nickShengY"
license: "CC0-1.0"
url: "https://github.com/nickShengY/chamberlain_multimodal_multiagent_chatbot"
source_code_url: "https://github.com/nickShengY/chamberlain_multimodal_multiagent_chatbot"
source_available: "True"
platforms: []
first_released: "2023-12-29"
current_release: "2023-12-29"
stars: "3"
language: "Python"
homepage: "https://github.com/nickShengY/chamberlain_multimodal_multiagent_chatbot"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI (GPT-4, GPT-4V), RoBERTa; uses LangChain"
pricing: "Free / open-source (CC0)"
install_method: "Clone repo; install Tesseract and Poppler (add to PATH); pip install -r requirements.txt; configure microphone; fill in OpenAI and Serp API keys in api_key.py"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/nickShengY/chamberlain_multimodal_multiagent_chatbot"
maintained: "dormant"
sources:
  - "jim"
what_makes_it_special: "Multimodal multi-agent voice-controlled personal assistant for home use. Auto-detects chat mode without user selection. Combines speech recognition, OCR, vision (selfie analysis), and LLMs. Manages fridge inventory, finances, fashion, IoT, coding tasks, and more via natural voice interaction. 14 specialized mode agents."
---

Chamberlain is a multimodal, voice-driven personal assistant built as a multi-agent system: a RoBERTa-based router listens to natural speech and dispatches requests to one of fourteen specialized agents covering areas like grocery management, personal finance, fashion advice, IoT device control, flight search, and coding help, using GPT-4 and GPT-4V through LangChain. The system handles speech recognition, text-to-speech, OCR, and selfie-based vision analysis, with autonomous mode detection so the user never picks a mode manually. Its coding mode provides software development assistance — describing an objective and receiving programmatic suggestions — but coding is one mode among many in a household-assistant design, not the system's focus. The project was a small personal project (8 commits, 3 stars) last updated in December 2023 and appears abandoned, released under a CC0 public-domain license. It suits hobbyists exploring multimodal agent routing rather than developers seeking a coding tool.
