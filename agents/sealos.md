---
name: "sealos"
slug: "sealos"
layout: "agent.njk"
category: "other"
maker: "labring"
license: "Sealos Sustainable Use License (custom, not OSI-approved)"
url: "https://github.com/labring/sealos"
source_code_url: "https://github.com/labring/sealos"
source_available: "Source-visible (no OSS license)"
platforms: []
first_released: "2018-08-15"
current_release: "2026-08-19"
stars: "18314"
language: "Go"
homepage: "https://sealos.io"
mcp_support: null
plugin_support: null
claude_code_plugin: "no"
subagents: "no"
hooks: null
plan_mode: "no"
model_providers: null
pricing: "open-source (custom license); cloud service available at sealos.io"
install_method: "docker"
docs_url: "https://sealos.io/docs"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "github_topic"
what_makes_it_special: "AI-native Cloud Operating System built on Kubernetes that unifies the entire application lifecycle — from cloud IDE development (DevBox) to production deployment, managed databases, and app store-style one-click deployments — without requiring Kubernetes expertise."
---

Sealos compresses the platform-engineering stack into one Kubernetes-based system: developers get DevBox cloud IDEs (with Cursor and VS Code connectivity), push Docker images through an App Launchpad, attach managed databases, and distribute software through a built-in app store, all without hand-writing Kubernetes YAML. The makers (labring, the FastGPT team) market it as AI-native infrastructure — deploy from GitHub or an AI coding agent, then operate with AI-assisted operations — which is how it intersects this census: it is where agent-built applications land, not the agent. Internally it is Go controllers over kubeadm-based clusters with Buildah-based cluster images, fronted by a React console. The custom Sustainable Use License permits internal and non-commercial use but forbids reselling it as a cloud service. It is widely deployed (18k+ stars) for self-hosted PaaS and AI application hosting.
