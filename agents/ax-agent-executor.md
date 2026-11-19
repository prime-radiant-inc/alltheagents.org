---
name: "AX"
slug: "ax-agent-executor"
layout: "agent.njk"
category: "multiplexer"
maker: "google"
license: "Apache-2.0"
url: "https://github.com/google/ax"
source_code_url: "https://github.com/google/ax"
source_available: "True"
homepage: "https://agentexecutor.io"
docs_url: "https://github.com/google/ax/tree/main/docs"
download_url: "https://github.com/google/ax/releases"
install_method: "curl -fsSL https://github.com/google/ax/releases/latest/download/install.sh | sh (one-line CLI installer); or from a checkout: make install"
platforms:
  - "CLI"
autonomy_level:
  - "autonomous-background"
specialization: "general"
language: "Go"
first_released: "2026-03-30"
current_release: "2026-09-25"
maintained: "active"
mcp_support: "True"
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://github.com/google/ax/blob/main/docs/manifests.md"
model_providers: "Runs any containerized agent workload — a Claude Code runner ships in-repo (cmd/runners/claude-code-runner, examples/claude-code) and any custom image or command works; agents bring their own providers. A Model resource also configures providers/credentials for platform components"
pricing: "free"
stars: "14793"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "A Kubernetes-shaped declarative runtime for agent workloads: tasks, workspaces (pre-wired Git repos, MCP servers, skills), models, and egress gateways are YAML manifests applied with a kubectl-like CLI, each sandboxed and suspend/resume-able on Agent Substrate actors. It targets fleets of millions of agent tasks per cluster with checkpointing and ssh-into-sandbox."
---

AX came out of the observation that agents are a new workload class — stateful, loop-running, money-burning, and badly served by either stateless services or batch jobs — and answers it the way Kubernetes answered containers. Four primitives (Task, Workspace, Model, Gateway) are declared in ax.io/v1alpha1 YAML and applied with a deliberately kubectl-shaped CLI; a task lands in a gVisor-sandboxed actor on Agent Substrate with CPU/memory limits, a pre-cloned workspace with MCP servers and skills materialized, credentials injected from Kubernetes secrets, and egress restricted to gateway allowlists. Tasks suspend to checkpoint and resume where they left off, `ax ssh` opens a shell inside the running sandbox, and the whole thing promotes unchanged from a local Kind cluster to GKE. Platform teams running fleets of coding-agent workloads (the shipped runner is Claude Code) are the audience; the maintainers describe it as job orchestration, not an agent framework.
