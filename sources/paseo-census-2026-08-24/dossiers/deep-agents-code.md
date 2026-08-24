# Dossier: DeepAgents / Deep Agents Code (census_slug: deep-agents-code)

Compiled 2026-08-24 (task dated 2026-08-21). Facts only. Null convention: "null = not researched"; "False/none = researched and absent". Sources [Sn] in section 7.

**Naming note (read first).** "DeepAgents" is two things: (a) the **Deep Agents SDK** — an open-source agent *framework* ("the batteries-included agent harness") in Python (`deepagents` on PyPI) and TypeScript (`deepagents` on npm, repo langchain-ai/deepagentsjs) [S1][S3][S12]; and (b) **Deep Agents Code (`dcode`)** — a *pre-built terminal coding agent* built on that SDK, shipped as PyPI package `deepagents-code` since 2026-04-30 [S4][S16]. The census slug deep-agents-code maps to (b); most of the big adoption numbers belong to (a). Paseo drives DeepAgents via `npx deepagents-acp`, a first-party ACP server that wraps a deep agent for editors/multiplexers [S13][S14].

## 1. Identity

- name: Deep Agents (SDK) / Deep Agents Code, `dcode` (coding agent). Docs title the CLI product "Deep Agents Code" [S4].
- maker: LangChain, Inc. (company; USA, HQ San Francisco, offices New York, Boston, Amsterdam [S23]).
- product URL: https://www.langchain.com/dcode (coding agent) [S18]; https://www.langchain.com/deep-agents (SDK). Docs: https://docs.langchain.com/oss/deepagents/code/overview (dcode) [S4]; https://docs.langchain.com/oss/python/deepagents / /oss/javascript/deepagents/overview (SDK) [S12].
- repo URL: https://github.com/langchain-ai/deepagents (monorepo: `libs/deepagents`, `libs/code` (dcode), `libs/acp`, `libs/cli`, `libs/talon`, `libs/partners`, plus `openwiki/`) [S2]; JS SDK at https://github.com/langchain-ai/deepagentsjs [S3].
- license: MIT (GitHub API license MIT; PyPI/npm license fields MIT) [S2][S14][S16]. open source? **True**, source_available: full — SDK, CLI agent, and ACP server all in public repos.
- first public release: framework — repo created 2025-07-27; first PyPI `deepagents` upload 2025-07-29 [S2][S16]. Deep Agents CLI announced 2025-10-30 ("Introducing Deep Agents CLI") [S19]; first PyPI `deepagents-cli` upload 2025-10-19 [S16]. **Coding agent `deepagents-code` (dcode): first PyPI upload 2026-04-30** [S16].
- latest release: `deepagents-code` 0.1.60 (2026-08-23); `deepagents` (PyPI) 0.7.8 (2026-08-20); npm `deepagents` 1.13.1 (2026-08-21); npm `deepagents-acp` 0.1.27 (2026-08-21) [S2][S14][S16] (as-of 2026-08-24).
- what it is:
  - Form factors: CLI/TUI coding agent (`dcode`) for macOS/Linux (Windows "not officially supported", WSL suggested) [S4][S5]; a library/SDK (Python + TS) for building custom deep agents [S1][S12]; an ACP stdio server (`deepagents-acp`, npm + PyPI) for Zed/JetBrains/Neovim/Emacs and other ACP clients [S13][S14]; GitHub Action (`action.yml` in repo) [S2].
  - Models: BYO — "works with any tool-calling LLM"; OpenAI, Anthropic, Google out of the box; any LangChain-compatible provider incl. Bedrock, OpenRouter, Fireworks, Baseten, Ollama/vLLM/llama.cpp; mid-session model switching (`/model`) [S4][S5][S1][S12]. Web search via Tavily key [S5].
  - Pricing: free, MIT open source; user pays their own model-provider keys; optional LangSmith tracing is LangChain's commercial SaaS (Developer $0 / 5k traces mo, Plus $39/seat/mo, Enterprise custom) [S24][S5].
  - Install: `curl -LsSf https://langch.in/dcode | bash` then `dcode` (updater detects uv/Homebrew/pip) [S4][S5]; SDK `uv add deepagents` / `npm install deepagents` [S1][S12]; ACP `npx deepagents-acp` / `pip install deepagents-acp` [S13][S14].
  - Default autonomy: **Manual** — asks approval before every "gated action" (file edit/delete, shell `execute`, web requests, subagent `task`); read-only tools (ls, read, glob, grep) never prompt. "Auto" (model reviews uncertain actions) is experimental beta behind `DEEPAGENTS_CODE_EXPERIMENTAL=1`; "YOLO" runs ungated with a one-time acknowledgement [S10].
  - Remote sandboxes: tool execution can run in LangSmith, AgentCore, Daytona, Modal, Runloop, Vercel, or E2B sandboxes [S26].
  - Repo language: Python (deepagents monorepo); TypeScript (deepagentsjs) [S2][S3].

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars, langchain-ai/deepagents | 28,361 | 2026-08-24 | [S2] | independently observable |
| GitHub forks | 3,966 | 2026-08-24 | [S2] | independently observable |
| GitHub watchers / open issues | 130 / 194 | 2026-08-24 | [S2] | independently observable |
| Contributors (incl. anonymous) | 143 | 2026-08-24 | [S2] | independently observable |
| Commits, last 90 days (since 2026-05-23) | 1,500 | 2026-08-24 | [S2] | independently observable |
| Release cadence | near-daily tags; deepagents-code 62 PyPI versions since 2026-04-30 | 2026-08-24 | [S2][S16] | independently observable |
| GitHub stars, langchain-ai/deepagentsjs | 1,504 (262 forks) | 2026-08-24 | [S3] | independently observable |
| PyPI downloads, `deepagents` (SDK) | 1,460,339 last week; 5,603,946 last month | 2026-08-24 | [S17] | independently observable |
| PyPI downloads, `deepagents-code` (dcode) | 10,292 last week; 61,368 last month | 2026-08-24 | [S17] | independently observable |
| npm weekly downloads, `deepagents` (JS SDK) | 278,412 (2026-08-17..23) | 2026-08-23 | [S15] | independently observable |
| npm weekly downloads, `deepagents-acp` (Paseo's entry point) | 2,474 | 2026-08-23 | [S15] | independently observable |
| npm weekly downloads, `deepagents-cli` | 2 (abandoned: last publish v0.0.16, 2026-01-09) | 2026-08-23 | [S14][S15] | independently observable |
| PyPI `deepagents-acp` | v0.0.10, first upload 2026-02-06 (downloads not researched) | 2026-08-24 | [S16] | independently observable |
| Company: "over 1 billion open source downloads" (all LangChain OSS) | 1B+ | 2026-08-24 | [S23] | maker-claimed |
| Company: "35% of the Fortune 500" served; 1B+ LangSmith events/day | — | 2026-08-24 | [S23] | maker-claimed |
| dcode page logos (company-level, not dcode-specific) | Klarna, Vanta, Clay, Rippling, Lyft, Gong, Harvey, Abridge, Autodesk, BMS, Workday, Cisco, Monday.com, Nvidia, LinkedIn, Coinbase, others | 2026-08-24 | [S18] | maker-claimed |
| Funding | Series B $125M at $1.25B post (closed 2025-10-20); ~$260M total; led by IVP, w/ CapitalG, Sapphire, Sequoia, Benchmark, Amplify, ServiceNow/Workday/Cisco/Datadog/Databricks | 2025-10-24 | [S22] | press |
| Revenue (company) | ~$16M (2025, third-party estimate) | 2025 | [S22-search] | unverified third-party |
| Partnership | NVIDIA "NemoClaw" Deep Agents blueprint (dcode + Nemotron 3 Ultra + OpenShell), July 2026: sandboxed exec, deny-by-default networking, audit trails | 2026-08-19 | [S20][S21] | press / maker-claimed |
| Press | DevOps.com on dcode's governance positioning (2026-08-19, Tom Smith); Baseten co-marketing post | 2026-08-24 | [S20] | press |
| Community | GitHub Discussions on LangChain forum (forum.langchain.com Deep Agents category, linked from README); member counts not obtained | 2026-08-24 | [S1] | null (not obtainable) |
| Benchmarks | none found for dcode (SWE-bench/Terminal-Bench: no placements located) | 2026-08-24 | — | researched, absent |

## 3. Plugin interface (PRI-2925)

- mcp_support: **client** — dcode auto-discovers `.mcp.json` (user `~/.deepagents/.mcp.json`, project `.deepagents/.mcp.json`, project-root `.mcp.json` "Claude Code compatible"), stdio/HTTP/SSE/OAuth transports, `/mcp` status + login, `--mcp-config`/`--no-mcp` flags; SDK likewise consumes MCP tools. Not an MCP server (it is an ACP server instead). Evidence: https://docs.langchain.com/oss/deepagents/code/mcp-tools [S8]
- plugin_support: **True** — plugins bundle skills + MCP servers + hooks; marketplace catalogs (GitHub `owner/repo`, HTTPS git, JSON URL, local); `/plugins` manager and `dcode plugin` CLI (install/enable/disable, `plugin-name@marketplace`); background auto-update opt-in; namespaced `/skill:` invocation. Evidence: https://docs.langchain.com/oss/deepagents/code/plugins [S6]
- claude_code_plugin: **partial/yes** — explicitly "supports Claude- and Codex-style plugin manifests and marketplace catalogs": reads `.claude-plugin/plugin.json` (and `.codex-plugin/plugin.json`), exposes `${CLAUDE_PLUGIN_ROOT}` / `${CLAUDE_PROJECT_DIR}` variables to hooks, reads project-root `.mcp.json`, and loads `~/.claude/skills/` and `.claude/skills/` (marked experimental). Memory uses `AGENTS.md` (agents.md convention), not CLAUDE.md; dcode marketing: "Claude-compatible hooks and plugins" [S6][S7][S8][S11][S18].
- subagents: **True** — custom subagents as `AGENTS.md` files with YAML frontmatter (`.deepagents/agents/<name>/AGENTS.md` project, `~/.deepagents/<agent>/agents/...` user; optional per-subagent `model` override); built-in general-purpose subagent; **dynamic subagents**: agent writes an orchestration script calling a `task()` global in the code interpreter, shown live in a phases panel; async subagents not yet exposed in dcode. Evidence: https://docs.langchain.com/oss/deepagents/code/subagents [S9]
- hooks: **True** — `hooks.json` at user (`~/.deepagents/`), project (workspace-trust gated), and plugin scope; events include PreToolUse, SessionStart (matcher startup|resume), UserPromptSubmit and other lifecycle events; command handlers only (subprocess, JSON payload on stdin; allow/deny/inject context); credential-looking env vars stripped from handler env. Evidence: https://docs.langchain.com/oss/deepagents/code/hooks [S7]
- plan_mode: **none found for dcode** (researched, absent) — no read-only/planning mode in the dcode docs (cli-reference/config have no plan flag); nearest analogues: default Manual approval mode gates all mutations [S10], `/goal` + `/rubric` acceptance-criteria commands [S5], and the SDK's planning/todo capability ("optional task planning") at the framework level [S12]. Census `plan_mode: True` reflects SDK planning, not a CLI plan mode.
- plugin_docs_url: https://docs.langchain.com/oss/deepagents/code/plugins
- config_docs_url: https://docs.langchain.com/oss/deepagents/code/configuration (also /config-file, /cli-reference)
- ACP support: **yes, first-party** — `deepagents-acp` (npm + PyPI) exposes any deep agent as an ACP stdio server for "Zed, JetBrains, and other ACP-compatible clients"; docs page "Agent Client Protocol (ACP)"; dcode docs point users at using deep agents "over ACP (for example, Zed)". This is what Paseo invokes (`npx deepagents-acp`) [S13][S14][S9].
- SDK: **yes — the SDK is the core product**: `deepagents` Python and JS (`create_deep_agent`), built on LangGraph/`create_agent`, with middleware, human-in-the-loop interrupts, pluggable filesystem/memory backends [S1][S12].

## 4. Claimed differentiation (raw material for PRI-2927)

- tagline (repo, verbatim): "The batteries-included agent harness." — https://github.com/langchain-ai/deepagents [S1]
- tagline (dcode page, verbatim): "The coding agent you own" — https://www.langchain.com/dcode [S18]
- docs one-liner (dcode): "Terminal coding agent built on the Deep Agents SDK" [S4]
- maker claims (paraphrased):
  1. Ownership/control vs closed agents: bring your own model, customize the harness, control how execution is "approved, traced, and run"; positioned against a "fixed coding assistant" [S18].
  2. Model-agnostic: any tool-calling LLM — frontier, open-weight, or local; switch models mid-session while keeping conversation state [S1][S4][S18].
  3. Opinionated defaults "tuned for long-horizon, multi-step work"; extensible — "override or replace any piece without forking" [S1].
  4. Persistent memory across sessions (AGENTS.md + auto-saved memories, "memory-first protocol"); configurable/shareable between agents [S4][S11][S19].
  5. Claude-compatible customization surface: hooks, plugins, marketplaces, skills (incl. reading .claude/skills) [S6][S18].
  6. Production story via the LangChain stack: built on LangGraph (streaming, persistence, checkpointing); LangSmith tracing/evals/deployment; remote sandbox execution (E2B, Modal, Daytona, ...) [S1][S26].
  7. Governance/enterprise angle (with NVIDIA NemoClaw): sandboxing, deny-by-default networking, audit trails for regulated codebases [S20][S21].
  8. Explicit comparison: dcode is "a pre-built coding agent in your terminal, similar to Claude Code or Cursor, powered by any LLM" (repo README) [S1].
- audience: developers building "agents and applications powered by LLMs" (SDK) [S12]; for dcode, teams that need inspectable, configurable agents and control over models/approvals/execution [S18]; CLI launch post: terminal-first developers wanting persistent-memory agents for coding/research [S19].

## 5. Company & contact targets (PRI-2929) — company-level only

- company: LangChain, Inc.; HQ San Francisco; offices New York, Boston, Amsterdam [S23]
- size: not stated on site (third-party trackers not relied on); funding stage: Series B — $125M at $1.25B post (2025-10-20), ~$260M total raised [S22]
- publicly named leadership:
  - Harrison Chase — Co-founder & CEO — https://www.langchain.com/about (co-founder; CEO title per funding press) [S23][S22]
  - Ankush Gola — Co-founder — https://www.langchain.com/about [S23]
  - No CTO / head of product / DevRel / partnerships lead found named on langchain.com (researched, absent) [S23]
- contact: langchain.com sales/contact forms (company site); OSS via GitHub + forum.langchain.com

## 6. Open questions / conflicts

- **Census entry conflates SDK and CLI.** deep-agents-code's `first_released: 2025-07-27` and `install_method: uv add deepagents` describe the *framework*; the coding agent the slug names (dcode, `deepagents-code`) first shipped 2026-04-30 and installs via the curl script [S16][S4]. The `what_makes_it_special` blurb is the SDK README, not the coding agent.
- Census `stars: null` → 28,361 (2026-08-24) [S2]. Census `current_release: 2026-08-20` → deepagents-code 0.1.60, 2026-08-23 [S2].
- Census `plan_mode: True` — no dedicated plan mode exists in dcode docs; SDK-level "task planning" only. Suggest False/none for the CLI with a note [S10][S12].
- Census `hooks: null` → True [S7]; `claude_code_plugin: null` → partial/yes [S6][S8][S11]; `plugin_docs_url`/`config_docs_url: null` → filled in section 3.
- Census `docs_url` points at the SDK overview (/oss/python/deepagents/overview); the coding agent's docs are /oss/deepagents/code/overview [S4].
- Census `language: Python` is right for the monorepo, but Paseo's entry point (`npx deepagents-acp`) is the TypeScript package from the JS side [S14].
- **`deepagents-cli` identity shifted.** PyPI `deepagents-cli` (launched 2025-10-19, blog 2025-10-30 as a general terminal agent) is now described as "Deployment tooling for Deep Agents — bundle, run, and ship agents to LangGraph Platform" (v0.2.2, 2026-06-07); the coding-agent role moved to `deepagents-code`. npm `deepagents-cli` ("AI Coding Assistant for your terminal") is abandoned (last publish 2026-01-09; 2 downloads/wk) [S16][S14][S15][S19]. Don't cite deepagents-cli numbers as coding-agent adoption.
- **Sibling census entry `langchain-js-tools`** (repo langchain-ai/langchainjs) is the LangChain JS *framework* — no agent product of its own with its own loop; its `subagents`/`plan_mode` fields even say "mentioned under Deep Agents capabilities", i.e. borrowed from this product. It fails Jesse's test and looks like it should be triaged out (not edited here).
- Adoption caveat: the headline numbers (5.6M PyPI/month, 278k npm/week, 28k stars) measure the framework; the coding agent's own observable is deepagents-code at ~61k PyPI/month, and the ACP surface Paseo uses is ~2.5k npm/week [S17][S15].
- Fortune-500/1B-downloads/logos are company-wide LangChain claims on the dcode page, not dcode-specific [S18][S23].
- Unreachable/not obtained: pypistats for `deepagents-cli` and `deepagents-acp` (429 rate limit persisted for -cli; -acp not attempted); LangChain forum member counts; no independent revenue figure (only a third-party ~$16M estimate) [S17][S22-search].
- NemoClaw blueprint details taken from press summary; primary blog (langchain.com/blog/langchain-and-nvidia-launch-the-nemoclaw-deep-agents-blueprint) not fetched directly [S20][S21].

## 7. Sources

1. [S1] https://github.com/langchain-ai/deepagents (README via raw) — tagline, principles, dcode note, FAQ
2. [S2] https://api.github.com/repos/langchain-ai/deepagents (+ /contents, /releases, commit & contributor pagination) — stars, dates, license, cadence, monorepo layout
3. [S3] https://api.github.com/repos/langchain-ai/deepagentsjs — JS SDK repo stats
4. [S4] https://docs.langchain.com/oss/deepagents/code/overview.md — dcode definition, install, capabilities
5. [S5] https://docs.langchain.com/oss/deepagents/code/quickstart.md — install steps, providers, Tavily, slash commands, Windows note
6. [S6] https://docs.langchain.com/oss/deepagents/code/plugins.md — plugins, marketplaces, Claude/Codex manifests
7. [S7] https://docs.langchain.com/oss/deepagents/code/hooks.md — hook events, trust model, plugin variables
8. [S8] https://docs.langchain.com/oss/deepagents/code/mcp-tools.md — MCP client, .mcp.json discovery, Claude Code compatibility
9. [S9] https://docs.langchain.com/oss/deepagents/code/subagents.md — AGENTS.md subagents, dynamic subagents, ACP mention
10. [S10] https://docs.langchain.com/oss/deepagents/code/approval-modes.md — Manual/Auto/YOLO, gated actions
11. [S11] https://docs.langchain.com/oss/deepagents/code/memory-and-skills.md — AGENTS.md memory, skills dirs, .claude/skills experimental
12. [S12] https://docs.langchain.com/oss/javascript/deepagents/overview — JS SDK overview, capabilities, providers
13. [S13] https://docs.langchain.com/oss/python/deepagents/acp.md — first-party ACP server usage
14. [S14] https://registry.npmjs.org/deepagents | deepagents-cli | deepagents-acp — npm metadata, publish dates, descriptions
15. [S15] https://api.npmjs.org/downloads/point/last-week/{deepagents,deepagents-cli,deepagents-acp} — npm weekly downloads
16. [S16] https://pypi.org/pypi/{deepagents,deepagents-code,deepagents-cli,deepagents-acp}/json — PyPI versions, first-upload dates, summaries
17. [S17] https://pypistats.org/api/packages/{deepagents,deepagents-code}/recent — PyPI download counts
18. [S18] https://www.langchain.com/dcode — "The coding agent you own", claims, logos
19. [S19] https://www.langchain.com/blog/introducing-deepagents-cli — CLI launch, 2025-10-30, memory-first protocol
20. [S20] https://devops.com/langchains-dcode-isnt-new-its-governance-play-for-sensitive-code-is/ — press, 2026-08-19, timeline + governance angle
21. [S21] https://www.langchain.com/blog/langchain-and-nvidia-launch-the-nemoclaw-deep-agents-blueprint — NVIDIA NemoClaw (title via search; details via S20)
22. [S22] https://theaiinsider.tech/2025/10/24/langchain-closes-125m-at-1-25b-valuation-to-expand-its-open-source-ai-agent-platform/ (+ search results incl. getlatka estimate, Wikipedia) — funding, investors, revenue estimate
23. [S23] https://www.langchain.com/about — co-founders, HQ/offices, 35% F500, 1B downloads claims
24. [S24] https://www.langchain.com/pricing — OSS free; LangSmith Developer $0 / Plus $39/seat / Enterprise
25. [S25] https://docs.langchain.com/llms.txt — docs index (dcode page inventory)
26. [S26] https://docs.langchain.com/oss/deepagents/code/remote-sandboxes.md (per llms.txt summary) — sandbox providers

## Inclusion check (Jesse's test)

**Yes** — DeepAgents is not only a framework: it ships **Deep Agents Code (`dcode`)**, a first-party terminal coding agent with its own agentic loop (LLM-driven read/edit/shell/web/subagents with approval gating), self-described as "similar to Claude Code or Cursor, powered by any LLM" [S1][S4][S10]. The `deepagents` library alone would fail the test (framework), and `deepagents-acp` is a wrapper — but the wrapped agent is LangChain's own, so the census entry stands on the CLI product. (Sibling entry `langchain-js-tools` is pure framework and looks triage-out.)
