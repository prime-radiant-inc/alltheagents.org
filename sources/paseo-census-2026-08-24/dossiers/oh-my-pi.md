# Dossier: Oh My Pi (omp) — census_slug `oh-my-pi`

Compiled 2026-08-21. Facts only; every non-obvious fact carries a source URL and as-of date.
Null convention: "null = not researched"; "none = researched and absent". Stated explicitly per item.

## 1. Identity

- name: Oh My Pi; short name / binary `omp`; npm scope `@oh-my-pi`; repo title "oh-my-pi". (README, https://github.com/can1357/oh-my-pi, as of 2026-08-21)
- maker: can1357 (public GitHub identity; profile name "Can Bölük"). Org form: individual-led project; repo is under a personal GitHub account, not an org. A corporate entity "Stencil Labs, Inc." appears as `author` in the root package.json and in the npm package author field, and in the README copyright line alongside the individual. HQ country: not stated for Stencil Labs (stencil.so has only a blog; no about/company/team page — /about, /company, /team return 404 as of 2026-08-21). (https://raw.githubusercontent.com/can1357/oh-my-pi/main/package.json; https://registry.npmjs.org/@oh-my-pi/pi-coding-agent; https://stencil.so, all as of 2026-08-21)
- product URL: https://omp.sh (repo `homepage` field; README). Docs: https://omp.sh/docs (single-page app; sitemap lists /docs/quickstart, /docs/plan, /docs/subagents, /docs/hooks, /docs/mcp, /docs/plugins, /docs/sdk, /docs/rpc, /docs/acp, /docs/tools, and /vs/claude-code, /vs/cursor, /vs/cline — https://omp.sh/sitemap.xml as of 2026-08-21). Docs source also in repo `docs/`.
- repo URL: https://github.com/can1357/oh-my-pi (GitHub API `fork: false` — it is NOT a GitHub-network fork of Pi; it is a re-homed copy). Repo created 2025-12-31T14:01:28Z. (https://api.github.com/repos/can1357/oh-my-pi, as of 2026-08-21)
- license: MIT (GitHub API `license.spdx_id: MIT`; README License section; vendored brush-core and pi-builtins third-party portions keep their own upstream licenses). (README, as of 2026-08-21)
- open source / source_available: True — full monorepo (TypeScript packages + Rust crates + Python `robomp`) public under MIT. (README "Monorepo Packages", "Rust Crates", as of 2026-08-21)
- relationship to Pi (precise):
  - omp describes itself as a fork of Pi / pi-mono by Mario Zechner (badlogic), now hosted at earendil-works/pi; README header: "Fork of Pi by @mariozechner"; Philosophy section: fork "extended with a batteries-included coding workflow". (README, as of 2026-08-21)
  - Packages are renamed: upstream `@mariozechner/*` / `@earendil-works/*` -> `@oh-my-pi/*` (pi-coding-agent, pi-agent-core, pi-tui, pi-ai, pi-utils, pi-catalog, pi-natives). (docs/porting-from-pi-mono.md, as of 2026-08-21)
  - Upstream tracking: maintained as a manual, selective port, not a vendor branch. `docs/porting-from-pi-mono.md` is a checklist for porting upstream changes and records a "Last Sync Point" upstream commit `b21b42d0…` dated 2026-03-22; it says to update the marker after each sync. (https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/porting-from-pi-mono.md, as of 2026-08-21)
  - omp's CHANGELOG begins at 0.7.6 (2025-11-13), i.e. it inherits Pi's changelog history, and early entries link to badlogic/pi-mono PRs; later entries repeatedly add "legacy pi extension" compatibility shims so extensions written for `@earendil-works/pi-coding-agent` / `@mariozechner/pi-coding-agent` load in omp (e.g. entries referencing #4567, #5968, #6470, #6583, #7094). (https://raw.githubusercontent.com/can1357/oh-my-pi/main/packages/coding-agent/CHANGELOG.md, as of 2026-08-21)
  - Copyright line: "© 2025 Mario Zechner / © 2025-2026 Can Bölük / © 2026 Stencil Labs, Inc." (README, as of 2026-08-21)
  - Third-party framing: StandardCompute describes the fork as disagreeing with the original's minimal-core philosophy (Pi: 4 tools + extensions; omp: built-ins). (https://standardcompute.com/best-ai-agent/oh-my-pi-vs-pi, dated 2026-08-03)
- first public release: repo created 2025-12-31; earliest GitHub release tag v1.337.1 published 2026-01-02T22:07Z; earliest npm publish of `@oh-my-pi/pi-coding-agent` 1.337.0 on 2026-01-02T21:58Z. (GitHub releases API page 6; https://registry.npmjs.org/@oh-my-pi/pi-coding-agent `time.created`, as of 2026-08-21)
- latest release: v17.4.2, published 2026-08-21T20:34Z (GitHub release; npm `latest` = 17.4.2 published 2026-08-21T20:39Z; CHANGELOG already has a 17.4.3 heading dated 2026-08-21 and root package.json catalog pins 17.4.3). (https://github.com/can1357/oh-my-pi/releases/tag/v17.4.2; npm registry, as of 2026-08-21)
- what it is:
  - Form factor: terminal CLI/TUI coding agent (`omp`); also one-shot `omp -p`; `omp --mode rpc` (NDJSON over stdio); `omp acp` (Agent Client Protocol server for editors such as Zed); Node/Bun SDK (`@oh-my-pi/pi-coding-agent`); live-session sharing via `/collab` with a browser guest client at my.omp.sh. (README "Four entry points"; docs/collab.md, as of 2026-08-21)
  - Models: BYO / multi-vendor. README lists "60+ providers" across direct APIs (Anthropic incl. OAuth, OpenAI, OpenAI Codex OAuth, Google Gemini/Vertex, xAI, DeepSeek, Mistral, Groq, Cerebras, Bedrock, Azure OpenAI, OpenRouter, etc.), subscription "coding plans" (Cursor, GitHub Copilot, GitLab Duo, Devin, Kimi, MiniMax, Z.AI/GLM, Qwen, etc.), and local servers (Ollama, LM Studio, llama.cpp, vLLM, LiteLLM); custom OpenAI-compatible providers via `~/.omp/agent/models.yml`; ten model "roles" (default, smol, slow, plan, commit, vision, designer, task, advisor, tiny). (README, as of 2026-08-21)
  - Pricing: free, MIT; users supply their own API keys / subscriptions. omp.sh JSON-LD lists `price: 0 USD`. No paid tier found (none). (https://omp.sh JSON-LD; README, as of 2026-08-21)
  - Install: `curl -fsSL https://omp.sh/install | sh` (macOS/Linux); `brew install can1357/tap/omp`; `bun install -g @oh-my-pi/pi-coding-agent` (Bun >= 1.3.14); `nix run github:can1357/oh-my-pi`; Windows `irm https://omp.sh/install.ps1 | iex`; `mise use -g github:can1357/oh-my-pi`. Prebuilt binaries for darwin-arm64/x64, linux-x64/arm64 (glibc + musl), windows-x64 attached to GitHub releases. (README "Install"; release v17.4.2 assets, as of 2026-08-21)
  - Default autonomy: tool approval mode `tools.approvalMode` defaults to `yolo` (auto-approves read, write and exec tiers; no prompts), with `write` and `always-ask` modes available; certain critical bash patterns (e.g. `rm -rf /`, fork bombs) force a prompt in non-yolo modes but "a bare critical override is ignored" in yolo. `--approval-mode`, `--auto-approve`/`--yolo` flags. Under ACP, destructive tools route through `session/request_permission`. (https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/approval-mode.md; docs/cli-reference.md; README ACP table, as of 2026-08-21)
  - Languages: TypeScript (~49.8 MB), Rust (~5.6 MB), Python (~3.2 MB) by GitHub byte counts; README claims ~80k lines of Rust core in six crates plus ~80k vendored. (https://api.github.com/repos/can1357/oh-my-pi/languages; README, as of 2026-08-21)

## 2. Adoption evidence

Each item: metric | value | as-of | source | observable vs maker-claimed.

GitHub (independently observable, https://api.github.com/repos/can1357/oh-my-pi and GraphQL, fetched 2026-08-21):
- stars | 26,290 (REST) / 26,291 (GraphQL) | 2026-08-21
- forks | 2,558 | 2026-08-21
- watchers (subscribers) | 79 | 2026-08-21
- open issues | 1,038 open / 3,116 closed (GraphQL); REST `open_issues_count` 1,620 incl. PRs | 2026-08-21
- pull requests | 582 open / 2,784 merged | 2026-08-21
- GitHub Discussions | 233 total | 2026-08-21
- releases | 571 | 2026-08-21 (GraphQL) — ~593 npm versions of pi-coding-agent published since 2026-01-02
- commits on default branch | 18,971 total; ~13,100 since 2026-05-23 (last 90 days, via REST `commits?since=` pagination count) | 2026-08-21
- contributors | ~399 (REST contributors pagination, non-anon) / ~498 incl. anonymous | 2026-08-21
- last push | 2026-08-21T21:23Z | 2026-08-21
- star trajectory (third-party snapshots, independently observable at the time): 5.5k+ stars / 458 forks / 177 contributors (explainx.ai article, published 2026-05-21, numbers "as of publication") https://explainx.ai/blog/oh-my-pi-terminal-coding-agent-omp-mario-zechner-2026 ; 14,677 stars / 1,287 forks / 10,671 commits (news.lesbass.com, 2026-06-26) https://news.lesbass.com/articles/oh-my-pi-ai-coding-agent-harness/ ; ">15k stars, >100 contributors, v16.2, >5,000 commits, nearly 400 releases" as of June 2026 (ai.miraheze.org wiki) https://ai.miraheze.org/wiki/Oh-My-Pi ; 22,344 stars (yuv.ai, 2026-08-06) https://yuv.ai/blog/oh-my-pi-omp-explained ; 26,133 stars (skillsllm.com listing, undated) https://skillsllm.com/skill/oh-my-pi.

npm (independently observable, https://api.npmjs.org, window 2026-08-13..2026-08-19 unless noted, fetched 2026-08-21):
- `@oh-my-pi/pi-coding-agent` weekly downloads | 96,689 | 2026-08-13..19
- `@oh-my-pi/pi-coding-agent` last-30-day downloads | 394,812 | 2026-07-21..08-19
- `@oh-my-pi/pi-ai` weekly | 87,503 ; last-30-day 338,325
- `@oh-my-pi/pi-agent-core` last-30-day | 335,634 ; `@oh-my-pi/pi-tui` last-30-day | 333,901
- weekly trend for pi-coding-agent (ISO weeks 2026): wk1 1,914 -> wk10 5,372 -> wk20 13,994 -> wk24 48,838 -> wk30 73,992 -> wk33 108,333 (wk34 partial 54,041). (https://api.npmjs.org/downloads/range/2026-01-01:2026-08-20/@oh-my-pi/pi-coding-agent)
- context: upstream `@earendil-works/pi-coding-agent` last-30-day downloads 7,040,877 (same window), i.e. omp's npm volume is ~5.6% of upstream Pi's.
- NOTE: the unscoped npm package `oh-my-pi` (367 weekly) is an unrelated third-party project by "acidsugarx" (created 2026-06-23) — not this harness. (https://registry.npmjs.org/oh-my-pi, as of 2026-08-21)
- Homebrew: tap `can1357/tap` formula `omp` at 17.4.2; no public analytics (third-party taps are not in Homebrew analytics). (https://raw.githubusercontent.com/can1357/homebrew-tap/main/Formula/omp.rb, as of 2026-08-21)
- Binary installer (`omp.sh/install`) downloads: none published / not observable.

Community (independently observable):
- Discord "omp" server | 2,491 members, 723 online | 2026-08-21 | https://discord.com/api/v10/invites/4NMW9cdXZa?with_counts=true (invite from README)
- GitHub Discussions 233 (above). Subreddit: none found (none).

Maker-claimed usage numbers: none found in README, omp.sh, or the launch blog post (the blog post states no adoption numbers). (https://stencil.so/blog/the-harness-problem, as of 2026-08-21)

Public customers / case studies / logos: none on README or omp.sh (omp.sh is a JS SPA; its index HTML/JSON-LD carries no customer names). (none)

Funding / valuation / acquisition: none found. Stencil Labs, Inc. named as package author and copyright holder; no funding, HQ, size, or registration details found in public web search. (WebSearch "Stencil Labs" "oh-my-pi" funding, 2026-08-21: no results)

Third-party signals:
- Benchmarks: maker's own edit-format benchmark (180 tasks from React codebase mutations, 16 models, 3 runs; hashline beat patch/str_replace on 14/16 models, avg +15 pts; Grok Code Fast 1 6.7% -> 68.3%; Grok 4 Fast -61% output tokens). Maker-claimed. (https://stencil.so/blog/the-harness-problem, byline Can Bölük, 2026-02-12; README "Every tool, benchmaxxed"). No SWE-bench or other independent placement found (none). The repo ships `@oh-my-pi/pi-metaharness` (Harbor/SWE-style benchmark runner) and `typescript-edit-benchmark`. (README packages table, as of 2026-08-21)
- Coverage: explainx.ai (2026-05-21, updated 2026-08-20); news.lesbass.com (2026-06-26); yuv.ai (2026-08-06; its own comparison says Claude Code leads 4 of 6 categories, omp leads speed and value); standardcompute.com review + "omp vs Pi" + "omp vs OpenCode" (2026-08-03); gasatrya.com "Pi vs OMP" two-week impressions (2026-07-09; reports 1–2x higher token use than Pi for the author's work); knightli.com setup guide (2026-05-23); note.com (Japanese) guide; podimo "hexlocal signal" podcast episode; grokipedia page; everydev.ai, opensourcealternatives.to, stayahead.space listings. (URLs in section 7)
- Integrations: Paseo lists OMP as a supported agent with a dedicated page https://paseo.sh/omp (Paseo roster notes `enabledByDefault: false`). Not listed on the ACP registry / agentclientprotocol.com agents page as of 2026-08-21 (Pi is listed "via pi-acp adapter"; omp absent); GitHub issue #1122 "Add OMP to the ACP Registry" opened 2026-05-16, still open, no maintainer reply recorded. (https://agentclientprotocol.com/get-started/agents; https://github.com/can1357/oh-my-pi/issues/1122, as of 2026-08-21)
- Notable endorsements: none found (none). Pi upstream README does not mention omp. (https://raw.githubusercontent.com/earendil-works/pi/main/README.md, as of 2026-08-21)

## 3. Plugin interface (six census fields)

- mcp_support: **client** (acts as an MCP client; connects to stdio/http/sse servers, exposes them as `mcp__<server>_<tool>` tools; imports MCP configs from `.omp/mcp.json`, `~/.omp/agent/mcp.json`, plus Claude Code, Codex, Gemini CLI, OpenCode, Cursor, Windsurf, VS Code files and Claude-marketplace plugins). No evidence it runs as an MCP *server* (none found; its external-program surfaces are RPC and ACP). Evidence: https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/mcp-config.md ; docs/mcp-server-tool-authoring.md (as of 2026-08-21)
- plugin_support: **yes** — (a) TypeScript "extensions" (default-export factory with `pi.on`, `pi.registerTool`, `pi.registerCommand`, renderers, keybindings) loaded from `.omp` dirs, `--extension`, npm (`omp plugin install`), git, local link; (b) skills (`SKILL.md` dirs, `skill://` reads, `/skill:<name>`); (c) custom tools; (d) a marketplace/plugin manager (`/marketplace`, `omp plugin …`) that installs plugins at user/project scope; (e) README says extensions can be kept local, shipped in a marketplace, or published to npm. Docs: https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/extensions.md ; docs/extension-loading.md ; docs/skills.md ; docs/marketplace.md ; docs/plugin-manager-installer-plumbing.md ; omp.sh/docs/plugins (as of 2026-08-21)
- claude_code_plugin: **yes (compatible, documented)** — marketplace.md: the system "is compatible with the Claude Code plugin registry format"; catalog read from `.omp-plugin/marketplace.json` or `.claude-plugin/marketplace.json` (Claude Code-compatible fallback); quick start example installs from `anthropics/claude-plugins-official`; plugins may contain skills, commands, agents, hooks, tools, MCP servers, LSP servers. Also reads `.claude/CLAUDE.md` (priority 80), `.claude` skills, Claude MCP configs (`~/.claude.json`, `.claude/.mcp.json`), and Claude-format discovery generally. Evidence: https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/marketplace.md ; docs/context-files.md ; docs/mcp-config.md (as of 2026-08-21)
- subagents: **yes** — `task` tool fans out subagents in parallel, optionally in isolated worktrees (pi-iso crate: APFS clone/btrfs/zfs/overlayfs/projfs), returns schema-validated structured output; custom agent definitions in `~/.omp/agent/agents/*.md` and `.omp/agents/*.md` (frontmatter name/description/tools/model/spawns); Agent Hub (`Alt+A`) to watch/steer/kill; `/review` spawns reviewer subagents; separate "advisor" second-model reviewer; `/vibe` director mode. Evidence: README sections 05, 06, 10; https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/task-agent-discovery.md ; docs/agent-hub.md (as of 2026-08-21)
- hooks: **yes** — typed lifecycle events via extensions/hooks: `tool_call` (pre; can block or rewrite input), `tool_result` (post), `session_start/switch/branch/compact/shutdown`, `before_agent_start`, `agent_start/end`, `turn_start/end`, `auto_compaction_*`, `auto_retry_*`, `ttsr_triggered`, `context` transform; `--hook` alias for `--extension`; `.omp/hooks/pre/*.ts` discovery. Plus "time-traveling stream rules" (TTSR) that abort mid-stream on regex match and inject a rule. Evidence: https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/hooks.md ; docs/ttsr-injection-lifecycle.md ; README section 04 (as of 2026-08-21)
- plan_mode: **yes** — settings `plan.enabled` (default true), `plan.defaultOnStartup`; `--plan-yolo` "force read-only plan mode at start"; `plan` model role / `--plan <model>`; omp.sh/docs/plan page in sitemap; omp.sh meta description lists "plan mode". Evidence: https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/settings.md (lines on plan.*) ; docs/cli-reference.md ; https://omp.sh/sitemap.xml (as of 2026-08-21)
- plugin_docs_url: https://omp.sh/docs/plugins (rendered) / https://github.com/can1357/oh-my-pi/blob/main/docs/marketplace.md and docs/extensions.md (source)
- config_docs_url: https://omp.sh/docs/settings (rendered) / https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md and docs/config-usage.md (source)
- ACP support: **yes** — `omp acp` runs an Agent Client Protocol server over stdio (JSON-RPC); maps bash->terminal/create, read->fs/read_text_file, write->fs/write_text_file, edits gated by session/request_permission; README says it runs inside Zed. Not in the ACP registry (see section 2). (README "ACP — speak to editors"; https://omp.sh/docs/acp, as of 2026-08-21)
- SDK availability: **yes** — `@oh-my-pi/pi-coding-agent` exports `createAgentSession`, `SessionManager`, `ModelRegistry`, `discoverAuthStorage`; typed event subscription; also RPC mode (`--mode rpc`, `--mode rpc-ui`) for non-Node hosts. (README "SDK — embed in Node"; https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/sdk.md ; docs/rpc.md, as of 2026-08-21)
- Other interop: reads rules/skills/MCP from `.claude`, `.cursor`, `.windsurf`, `.gemini`, `.codex`, `.cline`, `.github/copilot`, `.vscode` (README "Discovery"); context files CLAUDE.md / AGENTS.md / GEMINI.md / copilot-instructions.md (docs/context-files.md).

## 4. Claimed differentiation (raw material)

- tagline: "A coding agent with the IDE wired in." — README header and omp.sh `<title>` (https://github.com/can1357/oh-my-pi ; https://omp.sh, as of 2026-08-21). Secondary: "The Pi you love, with batteries included." (README)
- maker's differentiation claims (paraphrased, README https://github.com/can1357/oh-my-pi unless noted, as of 2026-08-21):
  1. Tool harness tuned per model ("benchmaxxed"): edit format (hashline content-hash anchors) and read/grep/prompt tuning raise pass rates and cut tokens across models; cites its own benchmark table (Grok Code Fast 1 6.7% -> 68.3%, MiniMax 2.1x, Grok 4 Fast -61% tokens) and the blog post https://stencil.so/blog/the-harness-problem (2026-02-12).
  2. IDE-grade integrations built in: LSP on every write (renames via workspace/willRenameFiles, 14 LSP ops), real debugger driving via DAP (lldb/dlv/debugpy, 28 DAP ops), persistent Python + JS execution cells that can call back into agent tools.
  3. Native Rust engine (~80k LoC, six crates) running grep/glob/shell/AST/PTY/desktop in-process — no fork/exec, same binary on macOS/Linux/Windows without WSL.
  4. First-class subagents with isolated worktrees and typed structured results; Agent Hub; advisor model watching every turn; code review with P0–P3 verdicts.
  5. 60+ model providers, 31 built-in tools, ten model roles, fallback chains, path-scoped models, round-robin credentials.
  6. "Time-traveling stream rules" (TTSR) that abort and correct mid-stream without constant context tax.
  7. Inherits other tools' configs natively (Cursor MDC, .clinerules, AGENTS.md, Copilot applyTo, .claude, etc.) — "no migration script"; Claude Code marketplace compatible.
  8. Openness: all TypeScript, all MIT, extensions use the same APIs as built-ins ("Nothing is reserved"); four entry points (TUI, one-shot, RPC, ACP) plus SDK; /collab live sharing with end-to-end sealed frames.
- audience: not explicitly stated as a role/segment; README addresses individual developers working in terminals ("made for terminals that stay open"); the blog post addresses developers/engineers building coding agents and, implicitly, model vendors (https://stencil.so/blog/the-harness-problem). omp.sh has /vs/claude-code, /vs/cursor, /vs/cline comparison pages (sitemap; content not fetchable — SPA).
- positioning language: README contrasts with "other harnesses"/"most agents"/"every other agent" (shelling out to rg/grep, bolting on gh_* tools, sprinkling print statements, shipping importers); names Pi as origin and Zed as ACP host; omp.sh sitemap has comparison pages vs Claude Code, Cursor, Cline.

## 5. Company & contact targets (company-level only)

- Legal entity: "Stencil Labs, Inc." — named as `author` in root package.json and npm package metadata, and as 2026 copyright holder in README. Blog for the project is hosted at https://stencil.so/blog (blog.can.ac posts 302-redirect there); stencil.so front page has only a "Blog" link; no about/team/company/pricing pages (404). HQ: not published. Size: not published. Funding stage: none found. (package.json; npm registry; stencil.so, as of 2026-08-21)
- Publicly named leadership: the project names only its maintainer by public handle — can1357 (GitHub profile name "Can Bölük"; omp.sh JSON-LD author "can1357"; blog byline "Can Bölük"). GitHub profile self-description: security researcher / reverse engineer; profile links blog https://can.ac/. No CEO/CTO/DevRel/partnerships titles published anywhere found. (https://api.github.com/users/can1357 ; https://omp.sh JSON-LD ; https://stencil.so/blog/the-harness-problem, as of 2026-08-21)
- Partnership/contact channel: Discord https://discord.gg/4NMW9cdXZa (README; CONTRIBUTING says major changes must be discussed there first). GitHub issues/PRs open to everyone "as a trial" (previously required a vouch). An autonomous bot "robomp" picks up actionable issues (CONTRIBUTING.md; `python/robomp` in repo). (https://raw.githubusercontent.com/can1357/oh-my-pi/main/CONTRIBUTING.md, as of 2026-08-21)
- Upstream relationship contacts: Pi / Earendil (Mario Zechner) — separate organization; see `pi` dossier.

## 6. Open questions / conflicts

- Existing census entry `stars: null` — now observable: 26,290 (2026-08-21).
- Census `first_released: "2025-12-31"` = repo creation date; first tagged release/npm publish is 2026-01-02. Either is defensible; note which convention is used.
- Census `current_release: "2026-08-19"` is stale: v17.4.2 on 2026-08-21 (releases ship multiple times per day; 571 releases total).
- Census `claude_code_plugin: null` — should be True/yes: docs/marketplace.md states Claude Code plugin registry format compatibility and `.claude-plugin/marketplace.json` fallback; reads CLAUDE.md, .claude skills and MCP configs.
- Census `plugin_docs_url: "https://omp.sh/docs/sdk"` — SDK is the embedding API; the plugin/extension docs are https://omp.sh/docs/plugins (and docs/extensions.md, docs/marketplace.md). `config_docs_url: null` — https://omp.sh/docs/settings exists.
- Census `what_makes_it_special` says "31 built-in tools" (matches README today) but several 2026-05/07 third-party articles say 32; the README count has varied by release.
- Census `language: "TypeScript, Rust"` — Python (robomp, ~3.2 MB) is also substantial; GitHub primary language TypeScript.
- Census `maker: "can1357"` — correct public handle; note Stencil Labs, Inc. appears as corporate author/copyright holder (no further public info).
- Census `sources: jqueryscript, brad, ishandutta` — none of these were encountered in this research; not verified.
- Unreachable/unusable: https://omp.sh and all /docs/* pages are a client-rendered SPA (curl returns shell only; WebFetch 403) — docs facts taken from the repo `docs/` source instead; the /vs/claude-code, /vs/cursor, /vs/cline comparison pages could not be read. X/Twitter post by the maker (https://x.com/_can1357/status/2064802476742574459) returned 402 — no launch-post content captured; no launch announcement located beyond the 2026-02-12 blog post. npmjs.com web page 403 (registry API used instead). ai.miraheze.org wiki page 403 (numbers taken from search snippet only). GitHub unauthenticated REST rate limit hit mid-session; gh GraphQL used for counts.
- Conflicting third-party numbers: Rust core described as ~27k LoC (explainx, May 2026), ~55k (lesbass, June 2026), ~80k (README/yuv, Aug 2026), "100,000+" (some listings) — reflects growth over time plus vendored code; README's own "~80k core + ~80k vendored" is the current maker statement.
- Upstream tracking: last recorded sync marker is 2026-03-22; whether upstream Pi changes after that have been ported is not determinable from the marker alone (CHANGELOG continues to add Pi-extension compatibility shims through August 2026). No public statement from the Pi maintainer about omp found.
- ACP registry: omp is not listed (issue #1122 open since 2026-05-16) despite shipping an ACP server — worth re-checking.
- Paseo roster note `enabledByDefault: false` for `omp` — reason not stated in Paseo's public page.
- No maker-claimed user counts exist; npm downloads and GitHub stars are the only volume signals. Weekly npm downloads for the CLI package ~97k vs upstream Pi ~1.6M+/week — but omp also ships binaries (curl/brew/nix/mise) whose volume is unobservable, so npm understates omp relative to Pi by an unknown amount.

## 7. Sources

1. https://github.com/can1357/oh-my-pi — README (identity, install, features, providers, tools, entry points, philosophy, license, copyright)
2. https://raw.githubusercontent.com/can1357/oh-my-pi/main/README.md — raw README text
3. https://api.github.com/repos/can1357/oh-my-pi — stars/forks/created/pushed/license/homepage/topics (2026-08-21)
4. GitHub GraphQL via `gh api graphql` (repo can1357/oh-my-pi) — issues/PRs/discussions/releases/commit totals (2026-08-21)
5. https://api.github.com/repos/can1357/oh-my-pi/releases — release tags/dates, earliest and latest
6. https://api.github.com/repos/can1357/oh-my-pi/contributors — contributor count via pagination
7. https://api.github.com/repos/can1357/oh-my-pi/languages — language byte counts
8. https://api.github.com/users/can1357 — public profile (name, bio, blog)
9. https://raw.githubusercontent.com/can1357/oh-my-pi/main/package.json — author Stencil Labs, Inc.; workspace packages; version 17.4.3
10. https://registry.npmjs.org/@oh-my-pi/pi-coding-agent — created date, versions, maintainers, author
11. https://api.npmjs.org/downloads/point/last-week/@oh-my-pi/pi-coding-agent (+ last-month; pi-ai, pi-agent-core, pi-tui; @earendil-works/pi-coding-agent) — download counts
12. https://api.npmjs.org/downloads/range/2026-01-01:2026-08-20/@oh-my-pi/pi-coding-agent — weekly trend
13. https://registry.npmjs.org/oh-my-pi — unrelated third-party package check
14. https://discord.com/api/v10/invites/4NMW9cdXZa?with_counts=true — Discord member count
15. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/porting-from-pi-mono.md — upstream relationship, last sync marker, package renames
16. https://raw.githubusercontent.com/can1357/oh-my-pi/main/packages/coding-agent/CHANGELOG.md — version history, upstream compat shims
17. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/hooks.md — hook events
18. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/approval-mode.md — default autonomy (yolo)
19. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/extensions.md — extension API
20. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/marketplace.md — Claude Code plugin compatibility, marketplace
21. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/mcp-config.md — MCP client config + imports
22. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/mcp-server-tool-authoring.md — MCP tool bridge architecture
23. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/context-files.md — CLAUDE.md/AGENTS.md discovery
24. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/skills.md — skills system
25. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/cli-reference.md — --plan-yolo, approval flags, acp subcommand
26. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/settings.md — plan.enabled, modelRoles
27. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/task-agent-discovery.md — subagent definitions
28. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/plugin-manager-installer-plumbing.md — plugin install plumbing
29. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/extension-loading.md — extension discovery
30. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/sdk.md — SDK surface
31. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/collab.md — /collab relay, my.omp.sh
32. https://raw.githubusercontent.com/can1357/oh-my-pi/main/docs/auth-broker-gateway.md — self-hosted auth broker/gateway
33. https://raw.githubusercontent.com/can1357/oh-my-pi/main/CONTRIBUTING.md — governance, vouch trial, robomp
34. https://raw.githubusercontent.com/can1357/oh-my-pi/main/packages/metaharness/README.md — benchmark runner package
35. https://omp.sh — index HTML/JSON-LD (title, description, price 0, author can1357, sameAs links); SPA not renderable
36. https://omp.sh/sitemap.xml — docs page inventory, /vs pages
37. https://stencil.so/blog/the-harness-problem — launch/benchmark blog post (byline Can Bölük, 2026-02-12); redirect target of blog.can.ac
38. https://stencil.so (and /about, /company, /team) — company page check (blog only; 404s)
39. https://raw.githubusercontent.com/can1357/homebrew-tap/main/Formula/omp.rb — Homebrew tap formula
40. https://agentclientprotocol.com/get-started/agents — ACP agents list (omp absent)
41. https://github.com/can1357/oh-my-pi/issues/1122 — ACP registry request (open)
42. https://raw.githubusercontent.com/earendil-works/pi/main/README.md — upstream Pi README (no omp mention)
43. https://paseo.sh/omp — Paseo support page for OMP
44. https://standardcompute.com/best-ai-agent/oh-my-pi-vs-pi — fork-vs-original framing (2026-08-03)
45. https://explainx.ai/blog/oh-my-pi-terminal-coding-agent-omp-mario-zechner-2026 — coverage; 5.5k stars snapshot (2026-05-21)
46. https://news.lesbass.com/articles/oh-my-pi-ai-coding-agent-harness/ — coverage; 14,677 stars (2026-06-26)
47. https://yuv.ai/blog/oh-my-pi-omp-explained — coverage; 22,344 stars (2026-08-06)
48. https://gasatrya.com/blog/pi-vs-omp/ — user impressions, token-cost criticism (2026-07-09)
49. https://ai.miraheze.org/wiki/Oh-My-Pi — wiki snapshot (via search snippet; page 403)
50. https://skillsllm.com/skill/oh-my-pi — listing with 26.1k stars (undated)
51. Other listings seen via search (not fetched): https://standardcompute.com/best-ai-agent/oh-my-pi ; https://standardcompute.com/best-ai-agent/oh-my-pi-vs-opencode ; https://knightli.com/en/2026/05/23/oh-my-pi-ai-coding-agent-terminal-ide-lsp-debugger/ ; https://note.com/kudoucraft/n/n991c4bb46fd0 ; https://podimo.com/en/shows/hexlocal-signal/episode/ba76f125-e340-5aad-b251-61177608a1cb ; https://grokipedia.com/page/Oh_My_Pi ; https://www.everydev.ai/tools/omp-oh-my-pi ; https://www.opensourcealternatives.to/item/oh-my-pi ; https://deepwiki.com/can1357/oh-my-pi ; https://context7.com/can1357/oh-my-pi

## Inclusion check (Jesse's test)

**Yes** — omp is a full coding agent with its own agentic loop (its own `@oh-my-pi/pi-agent-core` runtime with tool calling, 31 built-in tools, sessions, subagents) that creates and modifies software using LLMs from 60+ providers; it is a maintained divergent fork of Pi rather than a wrapper around someone else's running agent (README; docs/porting-from-pi-mono.md, 2026-08-21). Per Jesse's rule: oh-my-pi is IN.
