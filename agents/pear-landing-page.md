---
name: "pear-landing-page"
slug: "pear-landing-page"
layout: "agent.njk"
category: "other"
maker: "trypear"
license: "Apache-2.0"
url: "https://github.com/trypear/pear-landing-page"
source_code_url: "https://github.com/trypear/pear-landing-page"
source_available: "True"
platforms:
  - "IDE"
first_released: "2024-04-19"
current_release: "2025-12-27"
stars: "117"
language: "TypeScript"
homepage: "https://trypear.ai"
mcp_support: "no"
plugin_support: "no"
claude_code_plugin: "no"
subagents: "no"
hooks: "no"
plan_mode: "no"
model_providers: null
pricing: null
install_method: "git clone, yarn install, yarn dev (requires NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY env vars)"
docs_url: "https://trypear.ai"
plugin_docs_url: null
config_docs_url: null
download_url: "https://trypear.ai"
maintained: "active"
sources:
  - "github_topic4"
what_makes_it_special: "This repository is the marketing/landing page for PearAI (an open-source AI-powered code editor), not the editor itself; standard Next.js/TypeScript/Tailwind stack deployed on Vercel with Supabase backend. Notable product is the PearAI editor it promotes."
---

pear-landing-page is the repository behind trypear.ai, the marketing site for the PearAI code editor, and contains no editor or agent code itself. The stack is conventional — Next.js, TypeScript, Tailwind CSS, Vercel hosting, and Supabase — organized as a typical web frontend with blog posts and product pages alongside the landing content. It exists in this census only because automated discovery surfaced it alongside the PearAI editor it promotes; the editor itself lives in the trypear organization's pearai repository. Visitors to the site get the product pitch; the site contributes nothing to the tooling landscape beyond hosting that pitch.
