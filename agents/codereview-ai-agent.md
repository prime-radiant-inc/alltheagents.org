---
name: "CodeReview-AI-Agent"
slug: "codereview-ai-agent"
layout: "agent.njk"
category: "agent"
maker: "smirk-dev"
license: "MIT"
url: "https://github.com/smirk-dev/CodeReview-AI-Agent"
source_code_url: "https://github.com/smirk-dev/CodeReview-AI-Agent"
source_available: "True"
platforms: []
first_released: "2025-11-20"
current_release: "2025-11-20"
stars: "37"
language: "Python 3.9+"
homepage: null
mcp_support: null
plugin_support: "False"
claude_code_plugin: "False"
subagents: "True"
hooks: null
plan_mode: null
model_providers: "Google Gemini"
pricing: "Free / open-source"
install_method: "git clone; create venv; pip install -r requirements.txt; set GOOGLE_AI_API_KEY (GitHub token optional)"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/smirk-dev/CodeReview-AI-Agent"
maintained: "active"
sources:
  - "github_topic3"
what_makes_it_special: "Multi-agent AI code review built on Google's ADK with three specialized agents (Code Analyzer, Security Checker, Quality Reviewer) running in sequence/parallel for ~2-3x speedup; analyzes 6 languages and outputs 4 report formats (HTML/MD/SARIF/JSON, SARIF for IDE integration); built-in GitHub PR integration for automated comments and inline reviews; Kaggle Agents Intensive Capstone 2025 (Enterprise Agents Track)."
---

CodeReview-AI-Agent was built as a Kaggle Agents Intensive 2025 capstone on Google's Agent Development Kit, structuring review as three cooperating agents: a Code Analyzer, a Security Checker, and a Quality Reviewer, coordinated by an orchestrator with shared session state. Agents run sequentially or in parallel depending on configuration, with parallel execution cutting review latency substantially on multi-language changes. The pipeline covers Python, JavaScript, TypeScript, Java, Go, and Rust, combines LLM judgment with Python AST analysis, and produces reports in HTML, Markdown, SARIF, and JSON — SARIF enabling direct IDE and GitHub Security integration. A GitHub integration posts review comments and inline annotations on pull requests, and a GitHub Actions workflow runs reviews from CI. The repository is a capstone portfolio project with 24 commits, not an actively maintained production tool.
