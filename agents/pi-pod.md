---
name: "pi pod"
slug: "pi-pod"
layout: "agent.njk"
category: "multiplexer"
maker: "pi-pod"
license: "AGPL-3.0"
url: "https://github.com/pi-pod/pipod"
source_code_url: "https://github.com/pi-pod/pipod"
source_available: "True"
homepage: "https://pipod.dev"
docs_url: "https://github.com/pi-pod/pipod/blob/main/docs/self-host.md"
download_url: "https://www.npmjs.com/package/@pipod/cli"
install_method: "Server: git clone https://github.com/pi-pod/pipod.git && selfhost/upgrade (Docker Compose on a Linux host, 8 GB RAM); then add a user with selfhost/add-user. CLI: npm install -g @pipod/cli (Node 22.19+), pipod login --server <url>"
platforms:
  - "CLI"
  - "Web"
  - "Autonomous"
autonomy_level:
  - "autonomous-background"
specialization: "general"
language: "TypeScript"
first_released: "2026-10-01"
current_release: "2026-11-18"
maintained: "active"
mcp_support: null
plugin_support: null
claude_code_plugin: null
subagents: "True"
hooks: null
plan_mode: null
plugin_docs_url: null
config_docs_url: "https://github.com/pi-pod/pipod/blob/main/cli/man/pipod-config.5.md"
model_providers: "Runs the pi coding agent only — every pod runs pi behind a small shim, one version pinned server-side (make bump-pi); pi brings its own providers and sign-ins"
pricing: "free"
stars: "166"
sources:
  - "hackernews"
last_verified: "2026-11-19"
date_added: "2026-11-19"
what_makes_it_special: "Self-hosted pod infrastructure for one agent: a Compose-project server (Postgres, Zitadel OIDC, control plane, native sandbox) runs each pi session in its own container on your own hardware, reachable from the pipod CLI or phone apps, with layered org/user/project config, egress allowlists, secrets, init/bake scripts, idle auto-stop, and pods that can launch bounded child pods. A hosted edition at pipod.dev is announced but not yet available."
---

pi pod exists because the pi coding agent is worth running continuously but not worth handing to someone else's cloud: it packages a complete self-hosted stack — a control plane (REST API, session gateway, lifecycle workers, Postgres), a native sandbox service that hosts many isolated pods per host, Zitadel for OIDC identity, and iOS/Android clients — as one Docker Compose project installed and upgraded by a single script. Inside a pod, the server runs pi behind a small shim and clients attach over the gateway, so a session started at a desk continues from a phone; the CLI launches a pod for the current directory, and layered configuration (built-in, org, user, project, with a policy layer of clamps) decides each pod's size, egress allowlist, model, and init scripts. The pi version is a single pin shared by CLI and server so a session never breaks on upgrade. Pods idle-stop on a timer, archive to cold storage, and can launch bounded child pods. The author is an early pi user who built it for running sessions across platforms and teams; the audience is developers and small organizations that want sandboxed, always-reachable agent compute on hardware they control, with a hosted service announced at pipod.dev as the future paid path.
