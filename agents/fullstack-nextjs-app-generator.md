---
name: "Fullstack-Nextjs-App-Generator"
slug: "fullstack-nextjs-app-generator"
layout: "agent.njk"
category: "agent"
maker: "spark-engine-opensource-projects"
license: "MIT"
url: "https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator"
source_code_url: "https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator"
source_available: "True"
platforms: []
first_released: "2024-09-01"
current_release: "2024-11-29"
stars: "24"
language: "JavaScript"
homepage: "https://sparkengine.ai/search"
mcp_support: "False"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "yes"
hooks: "False"
plan_mode: "False"
model_providers: "OpenAI, Groq (via Spark Engine API gateway)"
pricing: "Free / open-source (requires Spark API Key from sparkengine.ai)"
install_method: "git clone, npm install, deploy to Vercel with Vercel CLI, set SPARK_API_KEY and NGROK_DEPLOYER_URL env vars"
docs_url: null
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator"
maintained: "active"
sources:
  - "jim"
what_makes_it_special: "Fullstack Next.js app builder using Spark Engine AI's multi-agent system for interactive generation of pages, APIs, and database schemas, with automated deployment to Vercel + Supabase including database schema generation and serverless API creation through a guided multi-step UI."
---

The project demonstrates Spark Engine AI's multi-agent generation applied to a concrete stack: Next.js pages, API routes, and Supabase schemas produced through a guided multi-step interface rather than a one-shot prompt. A backend deployer service, reached through an ngrok tunnel, executes the Vercel deployment and runs the generated SQL against Supabase, so the output is a deployed app with its schema rather than a folder of code. Generation goes through a Spark API key with OpenAI and Groq listed as underlying providers. Development stopped at 33 commits in late 2024, leaving it as a working demonstration of the Spark Engine workflow rather than a maintained product.
