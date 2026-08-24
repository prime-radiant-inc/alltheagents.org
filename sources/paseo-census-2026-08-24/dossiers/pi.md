# Dossier: Pi (census_slug: pi)

Compiled 2026-08-21. Facts only; every non-obvious fact carries a source URL and as-of date.
Null convention: "null = not researched"; "none/False = researched and absent".
Name-collision note: "Pi" here is the pi.dev coding-agent harness (earendil-works/pi). Inflection's "Pi" chatbot and Raspberry Pi were excluded. Also excluded: badlogic/pi (a 2025-07 vLLM pod CLI by the same author, unrelated to the coding agent).

## 1. Identity

- name: Pi (repo title "Pi Agent Harness"; CLI binary `pi`; npm package `@earendil-works/pi-coding-agent`). https://github.com/earendil-works/pi (2026-08-21)
- maker: Earendil Inc. (company; Public Benefit Corporation founded 2025; founders Armin Ronacher and Colin Daymond Hanna; HQ Vienna, Austria per cofounder blog; GitHub org `earendil-works` location "Austria"). Created by Mario Zechner (public handle `badlogic` / `@badlogicgames`) as an individual project; Earendil acquired the project on 2026-04-08, with Zechner joining as team member and stakeholder and retaining technical direction. Sources: https://earendil.com/posts/announcing-pi-and-lefos/ (2026-04-08); https://mariozechner.at/posts/2026-04-08-ive-sold-out/ (2026-04-08); https://lucumr.pocoo.org/2026/1/27/earendil/ (2026-01-27, HQ Vienna); https://api.github.com/orgs/earendil-works (2026-08-21, location Austria, org created 2025-04-16)
- product URL: https://pi.dev  | docs: https://pi.dev/docs/latest (mirrors https://github.com/earendil-works/pi/tree/main/packages/coding-agent/docs)
- repo URL: https://github.com/earendil-works/pi (formerly `badlogic/pi-mono`; old URL redirects, verified via GitHub API 2026-08-21). Monorepo packages: coding-agent, agent (pi-agent-core), ai (pi-ai), tui, telemetry, plus experimental protocol/server/client/session-backends/evals dirs. https://github.com/earendil-works/pi/tree/main/packages (2026-08-21)
- license: MIT (repo LICENSE; GitHub API spdx MIT; npm license MIT) (2026-08-21). Maker statement 2026-04-08: core "will stay MIT licensed"; future Fair Source / proprietary enterprise tiers contemplated; RFC 0015 "Pi Licensing" in Discussion state (2026-03-30). https://mariozechner.at/posts/2026-04-08-ive-sold-out/ ; https://rfc.earendil.com/keyword/pi/ (2026-08-21)
- open source: source_available = True (entire monorepo incl. CLI, agent loop, provider layer, TUI is MIT on GitHub; pi.dev website repo `earendil-works/pi-website` also public). (2026-08-21)
- first public release: repo created 2025-08-09T14:03Z; initial monorepo commit 2025-08-09T15:18Z; first npm publishes of `@mariozechner/pi-agent` and `@mariozechner/pi-tui` 2025-08-09; tag v0.5.1 dated 2025-08-09. First GitHub Release object: v0.12.0 on 2025-12-02. Public launch/rationale post 2025-11-30. Sources: https://api.github.com/repos/earendil-works/pi ; https://registry.npmjs.org/@mariozechner/pi-agent ; https://registry.npmjs.org/@mariozechner/pi-tui ; https://github.com/earendil-works/pi/releases?page=3 ; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/ (all checked 2026-08-21). See section 6 for the 2025-08-01 `@mariozechner/pi` ambiguity.
- latest release: v0.84.2, 2026-08-14 (GitHub Release + npm dist-tag `latest` 0.84.2; pi.dev/api/latest-version returns 0.84.2). https://github.com/earendil-works/pi/releases/tag/v0.84.2 ; https://pi.dev/api/latest-version (2026-08-21). Repo last push 2026-08-21.
- What it is:
  - Form factor: terminal coding agent (interactive TUI) with three additional modes: print/JSON (`-p`, `--mode json`), RPC over stdin/stdout JSONL (`--mode rpc`), and a Node.js SDK (`createAgentSession`). Experimental `pi-server`/`pi-protocol` packages for a session server exist. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md ; https://github.com/earendil-works/pi/blob/main/packages/server/README.md (2026-08-21)
  - Models: BYO, multi-vendor. Subscription logins: Anthropic Claude Pro/Max, OpenAI ChatGPT Plus/Pro (Codex), GitHub Copilot. API-key providers listed in README: ~30 (Anthropic, OpenAI, Azure OpenAI, Google Gemini/Vertex, Amazon Bedrock, Mistral, Groq, Cerebras, xAI, OpenRouter, Vercel AI Gateway, DeepSeek, NVIDIA NIM, Cloudflare, ZAI, OpenCode Zen/Go, Hugging Face, Fireworks, Together, Baseten, Kimi, MiniMax, Xiaomi MiMo, Ant Ling, etc.); local models via llama.cpp router; custom providers via models.json or extensions. Site claims "15+ providers, hundreds of models". https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md ; https://pi.dev/ (2026-08-21)
  - Pricing: free, MIT open source; user pays own provider keys/subscriptions. No paid tier found as of 2026-08-21 (future tiers contemplated, see license bullet).
  - Install: `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`; `curl -fsSL https://pi.dev/install.sh | sh`; standalone Bun-compiled binaries attached to GitHub releases with SHA256SUMS; `pi update --self`. Node >=22.19 for npm install (package.json engines). https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/index.md ; https://github.com/earendil-works/pi/blob/main/README.md (2026-08-21)
  - Default autonomy: no permission prompts for edits or shell ("No permission popups"); runs with launching user's OS permissions; no built-in sandbox; default tools are `read`, `write`, `edit`, `bash`. The only startup gate is "project trust" (asks before loading project-local `.pi/` extensions/settings/skills). Containerization documented (Gondolin micro-VM, Docker, OpenShell). https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/security.md ; https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/containerization.md (2026-08-21)

## 2. Adoption evidence

| metric / claim | value | as-of | source | type |
|---|---|---|---|---|
| GitHub stars | 95,018 (95,021 an hour later) | 2026-08-21 | https://api.github.com/repos/earendil-works/pi | independently observable |
| GitHub forks | 11,760 | 2026-08-21 | same | observable |
| GitHub watchers (subscribers) | 311 | 2026-08-21 | same | observable |
| GitHub stars, earlier datapoint | 45,041 (as badlogic/pi-mono) | 2026-05-06 | https://www.implicator.ai/pi-is-not-a-claude-code-rival-it-is-a-harness-rebellion/ | third-party press |
| Contributors (GitHub, non-anon) | 273 | 2026-08-21 | GitHub API contributors Link header (last page=273 at per_page=1) | observable |
| Commits, last 90 days (since 2026-05-23) | 1,507 | 2026-08-21 | GitHub API commits?since= Link header | observable |
| Commits, all time | 5,762 | 2026-08-21 | GitHub API commits Link header | observable |
| GitHub Releases (count) | 255 | 2026-08-21 | GitHub API releases Link header | observable |
| Issues / PRs / Discussions (all time) | 5,264 issues; 2,873 PRs; 287 discussions | 2026-08-21 | GitHub GraphQL | observable |
| Open issues | 137 | 2026-08-21 | GitHub API | observable |
| npm weekly downloads, `@earendil-works/pi-coding-agent` | 1,904,277 (week 2026-08-13..19) | 2026-08-21 | https://api.npmjs.org/downloads/point/last-week/@earendil-works/pi-coding-agent | observable |
| npm monthly downloads, same | 7,040,877 (2026-07-21..08-19) | 2026-08-21 | https://api.npmjs.org/downloads/point/last-month/@earendil-works/pi-coding-agent | observable |
| npm weekly, legacy `@mariozechner/pi-coding-agent` (deprecated, last 0.73.1) | 442,810 (same week) | 2026-08-21 | https://api.npmjs.org/downloads/point/last-week/@mariozechner/pi-coding-agent | observable |
| npm weekly, library packages | pi-ai 3,732,535; pi-agent-core 2,415,046; pi-tui 4,504,745 (pi-tui is a dependency of OpenClaw, so counts include downstream) | 2026-08-21 | api.npmjs.org (same week) | observable |
| Discord server ("The Shitty Coders Club", the invite linked from README) | ~16,127 members, ~3,023 online | 2026-08-21 | https://discord.com/api/v9/invites/3cU7Bz4UPx?with_counts=true | observable |
| Third-party package ecosystem | npm search `keywords:pi-package` total 8,028; pi.dev/packages catalog lists them (implicator counted 2,143 on 2026-05-06) | 2026-08-21 | https://registry.npmjs.org/-/v1/search?text=keywords:pi-package&size=1 ; https://pi.dev/packages | observable |
| Community adapter downloads | `pi-mcp-adapter` 161,423/wk; `pi-acp` 72,834/wk | 2026-08-21 | api.npmjs.org (week 2026-08-13..19) | observable |
| Notable downstream: OpenClaw | OpenClaw (387,043 stars) depends on `@earendil-works/pi-tui` 0.82.1; maker and Earendil describe OpenClaw as "powered by pi" | 2026-08-21 / 2026-04-08 | https://raw.githubusercontent.com/OpenClaw/OpenClaw/main/package.json ; https://mariozechner.at/posts/2026-04-08-ive-sold-out/ ; https://lucumr.pocoo.org/2026/1/31/pi/ | observable (dependency) / maker-claimed ("powered by") |
| Fork ecosystem: oh-my-pi (can1357) | 26,291 stars, 2,558 forks, created 2025-12-31, MIT | 2026-08-21 | https://api.github.com/repos/can1357/oh-my-pi | observable |
| Maker-org satellite repos | gondolin 2,012 stars; pi-chat 377; pi-review 297; pi-tutorial 168; pi-transcribe 167; pi-review-loop 144 | 2026-08-21 | https://api.github.com/orgs/earendil-works/repos | observable |
| Hacker News | launch post 421 points / 173 comments (2026-02-01); Databricks benchmark post 161 points (2026-07-08); pi.dev submissions 2-4 points each (Feb 2026) | 2026-08-21 | https://news.ycombinator.com/item?id=46844822 ; https://news.ycombinator.com/item?id=48837696 | observable |
| Benchmark: Databricks internal coding benchmark on its multi-million-line codebase | Pi achieved the same success rate as vendor harnesses (Claude Code, Codex) with Opus and GPT 5.5 at about 2x lower cost; "about 3x less context per turn" | 2026-07-08 | https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase | independent (Databricks) |
| Maker restatement of Databricks result | "highest pass-rate" with Opus 4.8 xhigh; 4 tools, system prompt <1,000 tokens | 2026-08-04 | https://earendil.com/posts/pi-autoresearch-and-databricks/ | maker-claimed |
| Maker usage numbers (users, paying, tokens) | none published; pi sends anonymous install/update pings to pi.dev (RFC 0019 Pi Telemetry implemented 2026-04-14; RFC 0038 Pi Analytics in discussion) but no figures released | 2026-08-21 | https://rfc.earendil.com/keyword/pi/ ; README telemetry section | researched, absent |
| Public customers / logos / case studies | none on pi.dev; Earendil's 2026-08-04 post references a Shopify case study (David Cortes) and the Databricks benchmark | 2026-08-21 | https://pi.dev/ ; https://earendil.com/posts/pi-autoresearch-and-databricks/ | maker-claimed (Shopify) |
| Funding / acquisition | Pi acquired by Earendil Inc. 2026-04-08; Earendil backers named: Accel (Daniel Levine), Balderton (Daniel Waterhouse), founders of n8n, OpenClaw, Revolut, Sentry, Slack; amounts not disclosed | 2026-04-08 | https://earendil.com/posts/announcing-pi-and-lefos/ | maker-claimed |
| Press coverage | The Implicator (2026-05-06); agent-wars.com, pi-map.org (2026-04-08); daily.dev/StartupHub on Databricks benchmark (2026-07) | 2026-08-21 | https://www.implicator.ai/pi-is-not-a-claude-code-rival-it-is-a-harness-rebellion/ ; https://agent-wars.com/news/2026-04-08-pi-agent-creator-joins-earendil | third-party |
| Endorsement | Armin Ronacher essay "Pi: The Minimal Agent Within OpenClaw" (pre-acquisition) | 2026-01-31 | https://lucumr.pocoo.org/2026/1/31/pi/ | third-party at the time; author later cofounded acquirer |
| Public session dataset | maker publishes own pi sessions to Hugging Face (badlogicgames/pi-mono) | 2026-08-21 | https://github.com/earendil-works/pi/blob/main/README.md | maker |

## 3. Plugin interface (six census fields)

- mcp_support: **none built-in (researched, absent)**. README "Philosophy": "No MCP." Recommends CLI tools + READMEs/skills or an extension that adds MCP; links the author's rationale post. Community extensions provide MCP client support (e.g. `pi-mcp-adapter`, 161k weekly npm downloads). Pi does not act as an MCP server. Evidence: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md#philosophy ; https://pi.dev/ ("No MCP"); https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/ ; https://pi.dev/packages (2026-08-21)
- plugin_support: **yes** — four first-party extension kinds plus a package format: (1) Extensions: TypeScript modules using `ExtensionAPI` (register tools, commands, shortcuts, providers, UI, event handlers); (2) Skills: Agent Skills standard (agentskills.io) `SKILL.md` dirs; (3) Prompt templates (Markdown slash commands); (4) Themes. Bundled as "Pi packages" installed from npm or git (`pi install npm:...`, `pi install git:...`), discovered via npm keyword `pi-package`; catalog at https://pi.dev/packages. No curated marketplace beyond the npm-keyword catalog. Docs: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md ; https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md ; https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md (2026-08-21)
- claude_code_plugin: **partial** — loads `CLAUDE.md` (and `AGENTS.md`) context files by default; can load Claude Code skills by adding `~/.claude/skills` / `../.claude/skills` to the `skills` setting (docs explicitly describe this for Claude Code and Codex skills). No support found for the Claude Code plugin/marketplace format, `.claude/commands`, `.claude/agents`, or settings.json hooks (researched, absent). Evidence: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md (Locations section) ; README "Context Files" (2026-08-21)
- subagents: **none built-in (researched, absent)**; README: "No sub-agents." Available via extensions/SDK ("Build custom tools that spawn sub-agents" in SDK docs) or third-party packages (e.g. `@gotgenes/pi-subagents`, `@tintinweb/pi-subagents`, `@bermudi/pi-delegate` on pi.dev/packages); maker suggests tmux-spawned pi instances. Evidence: README Philosophy; https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md ; https://pi.dev/packages (2026-08-21)
- hooks: **yes, via in-process extension events (not shell/config hooks)** — `pi.on(event)` with ~35 events incl. `tool_call` (can block/modify), `tool_result`, `tool_execution_start/update/end`, `before_agent_start`, `agent_start/end`, `turn_start/end`, `session_start/shutdown/compact/fork/switch`, `before_provider_request`, `user_bash`, `input`, `project_trust`, `model_select`. README lists "Permission gates and path protection" as an extension use case. Evidence: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md (Events section) (2026-08-21)
- plan_mode: **none built-in (researched, absent)**; README: "No plan mode." Write plans to files or build/install an extension. Evidence: README Philosophy; https://pi.dev/ (2026-08-21)
- plugin_docs_url: https://pi.dev/docs/latest (extensions: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md ; packages: .../docs/packages.md)
- config_docs_url: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md (global `~/.pi/agent/settings.json`, project `.pi/settings.json`)
- ACP (Agent Client Protocol): **no native support** (researched, absent as of 2026-08-21). Community adapter `pi-acp` (svkozak) wraps `pi --mode rpc` and is the entry listed on Zed's ACP registry; feature request Discussion #4444 open since 2026-05-12 with no maintainer commitment visible. Evidence: https://zed.dev/acp/agent/pi ; https://github.com/svkozak/pi-acp ; https://github.com/earendil-works/pi/discussions/4444
- SDK: **yes** — TypeScript SDK exported from `@earendil-works/pi-coding-agent` (`createAgentSession`, `SessionManager`, `ModelRuntime`); lower-level `@earendil-works/pi-agent-core` and `@earendil-works/pi-ai`; RPC mode (JSONL stdio) and JSON event-stream mode for non-Node integration; experimental `pi-server`/`pi-protocol`/`pi-client`. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md ; .../docs/rpc.md (2026-08-21)
- Other: skills-standard interop with `.agents/skills` and `~/.agents/skills` (shared with other harnesses); `AGENTS.override.md`; session tree/branching; compaction; no built-in to-dos; no background bash (tmux recommended). README (2026-08-21)

## 4. Claimed differentiation

- tagline: "There are many agent harnesses but this one is yours" — https://pi.dev/ (2026-08-21). Secondary: "Pi is a minimal agent harness. Adapt Pi to your workflows, not the other way around." — https://pi.dev/ ; README: "Pi is a minimal terminal coding harness."
- Maker claims (paraphrased):
  1. Minimal core by design: four default tools and a system prompt under 1,000 tokens; features other harnesses bake in are deliberately omitted (MCP, sub-agents, plan mode, permission popups, to-dos, background bash). README Philosophy; https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
  2. "Aggressively extensible": TypeScript extensions, skills, prompt templates, themes; packages shareable via npm/git; the agent can extend itself ("ask pi to build what you want"). README; https://pi.dev/
  3. Multi-provider, BYO model: subscription logins (Claude, ChatGPT/Codex, Copilot) plus ~30 API-key providers and local llama.cpp; switch models mid-session. README "Providers & Models"; https://pi.dev/ ("15+ providers, hundreds of models")
  4. Four run modes: interactive TUI, print/JSON, RPC, SDK — positioned as embeddable building blocks (OpenClaw cited as built on pi components). README; https://lucumr.pocoo.org/2026/1/31/pi/ ; https://earendil.com/posts/announcing-pi-and-lefos/
  5. Context engineering and cost efficiency: minimal prompt/context discipline; cites Databricks benchmark (same pass rate, ~2x lower cost, ~3x less context per turn). https://earendil.com/posts/pi-autoresearch-and-databricks/ ; https://pi.dev/ ("actual context engineering")
  6. Sessions stored as trees with branching (`/tree`, `/fork`, `/clone`), compaction, message queue. README; https://pi.dev/
  7. Full observability / no hidden sub-processes (rationale for no sub-agents, no background bash). https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
  8. Supply-chain hardening of the npm package (pinned deps, shrinkwrap, `--ignore-scripts`, audit workflow). README "Supply-chain hardening"
  9. Open source, MIT, core to remain MIT (maker statement post-acquisition). https://mariozechner.at/posts/2026-04-08-ive-sold-out/
- Audience: developers who want to adapt the harness to their own workflow and control/observe LLM interactions; "simple, predictable tools". README ("Adapt pi to your workflows"); https://mariozechner.at/posts/2025-11-30-pi-coding-agent/ (2025-11-30). No team-size or language/stack targeting stated.

## 5. Company & contact targets (company-level only)

- Legal name: Earendil Inc. (Public Benefit Corporation; site footer "EARENDIL INC."). https://earendil.com/ ; https://earendil.com/posts/announcing-pi-and-lefos/ (2026-04-08)
- HQ: Vienna, Austria per cofounder's founding post; GitHub org location "Austria". https://lucumr.pocoo.org/2026/1/27/earendil/ ; https://api.github.com/orgs/earendil-works (2026-08-21). Cofounder Colin Hanna described as based in San Francisco (same post).
- Size: not published; hiring "Members of our Technical Staff and Founder's Office" (https://earendil.com/join/, 2026-08-21). Public npm maintainers of the CLI package: GitHub/npm handles `badlogic`, `mitsuhiko`, `rwachtler` (https://registry.npmjs.org/@earendil-works/pi-coding-agent, 2026-08-21).
- Funding stage: early-stage, backers named (Accel, Balderton, and founders of n8n, OpenClaw, Revolut, Sentry, Slack); amount undisclosed. https://earendil.com/posts/announcing-pi-and-lefos/ (2026-04-08)
- Publicly named leadership (only as the company names them; no titles beyond "founders" published on earendil.com):
  - Armin Ronacher — cofounder (announcement post; also public identity `mitsuhiko`). https://earendil.com/posts/announcing-pi-and-lefos/ ; https://lucumr.pocoo.org/2026/1/27/earendil/
  - Colin Daymond Hanna — cofounder. https://earendil.com/posts/announcing-pi-and-lefos/
  - Mario Zechner — Pi creator; "major stakeholder and team member"; leads Pi technical direction. https://earendil.com/posts/announcing-pi-and-lefos/ ; https://mariozechner.at/posts/2026-04-08-ive-sold-out/
  - CEO/CTO/head of product/DevRel/partnerships titles: not published on company materials (researched, absent as of 2026-08-21).
- Company-published contact surfaces: https://earendil.com/join/ (hiring page) ; RFC site https://rfc.earendil.com ; Pi Discord https://discord.com/invite/3cU7Bz4UPx ; X account @pidotdev (linked from pi.dev). No partnerships page found.
- Other product: Lefos (email-based agent product, public alpha 2026-04-08). https://earendil.com/posts/announcing-pi-and-lefos/

## 6. Open questions / conflicts

- Existing census entry `maker: "earendil-works"` — that is the GitHub org handle; the company is Earendil Inc. (creator Mario Zechner). Entry `homepage: null` should be https://pi.dev. Entry `stars: null` → 95,018 (2026-08-21). Entry `model_providers: "OpenAI, Anthropic, Google"` understates: ~30 providers plus three subscription logins and llama.cpp. Entry `current_release: "2026-08-19"` does not match any release; latest is v0.84.2 on 2026-08-14 (repo pushed 2026-08-21). Entry `url` points to GitHub; product URL is https://pi.dev. All six plugin fields were null; values in section 3.
- Entry `first_released: "2025-08-09"` matches repo creation and first npm publishes of pi-agent/pi-tui. Ambiguity: `@mariozechner/pi` on npm was created 2025-08-01 and a `v0.5.3-pods` tag exists — that early package may be the unrelated vLLM pod CLI (badlogic/pi, created 2025-07-31) rather than the coding agent; not resolved. The coding-agent-named package `@mariozechner/pi-coding-agent` first appeared 2025-11-12.
- Package naming: the 2026-04-08 maker post said the npm package would become `@earendil/pi`; the actual published name is `@earendil-works/pi-coding-agent` (first published 2026-05-07). The legacy `@mariozechner/pi-coding-agent` is deprecated at 0.73.1 but still sees ~443k weekly downloads.
- The WebFetch summary of the 2025-11-30 blog post said pi was "first built approximately three years ago"; not verified against the post text and contradicted by repo dates; treat as unverified.
- Contributor/commit/release counts are derived from GitHub API pagination Link headers (per_page=1 last-page number), not a direct count field; ±1 possible.
- Discord member count is for the server the README links ("The Shitty Coders Club"), which predates/extends beyond Pi; treat as an upper bound for Pi community size.
- npm `keywords:pi-package` total (8,028) likely includes unrelated packages using that keyword; implicator's 2,143 (2026-05-06) came from the pi.dev catalog. Exact pi.dev catalog count not extracted (page is long/JS-rendered).
- Databricks benchmark: the maker's restatement ("highest pass-rate" with Opus 4.8 xhigh) is stronger than the independent phrasing ("same success rate ... at 2x less cost"); both sourced above.
- Unreachable: https://earendil.com/posts/press-release-april-8th/ returned 404 via WebFetch though it appears in search results. Crunchbase/LinkedIn not consulted (policy). x.com links (@pidotdev, launch video, session-sharing thread) not fetched.
- Funding amount, headcount, and any executive titles are not public as of 2026-08-21.

## 7. Sources

1. https://api.github.com/repos/earendil-works/pi — stars, forks, dates, license
2. https://github.com/earendil-works/pi/blob/main/README.md — monorepo overview, packages, telemetry, supply chain
3. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/README.md — CLI features, providers, philosophy ("No MCP" etc.), packages, SDK/RPC
4. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/index.md — docs landing, install
5. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md — extension API and event list
6. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md — skills locations, Claude Code skills interop
7. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md — pi packages
8. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md — SDK
9. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/rpc.md — RPC mode
10. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/security.md — trust model, no sandbox
11. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md — config
12. https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/containerization.md — sandboxing patterns
13. https://github.com/earendil-works/pi/blob/main/CONTRIBUTING.md — minimal-core policy, contribution gate
14. https://github.com/earendil-works/pi/releases/tag/v0.84.2 — latest release
15. https://github.com/earendil-works/pi/releases?page=3 — earliest GitHub release v0.12.0
16. https://github.com/earendil-works/pi/blob/main/packages/server/README.md and packages/protocol/README.md — experimental server/protocol
17. https://registry.npmjs.org/@earendil-works/pi-coding-agent — versions, maintainers, first publish
18. https://registry.npmjs.org/@mariozechner/pi-coding-agent — legacy package, deprecation
19. https://registry.npmjs.org/@mariozechner/pi-agent, /@mariozechner/pi-tui, /@mariozechner/pi — first-publish dates
20. https://api.npmjs.org/downloads/point/last-week/... and last-month/... — download counts (pi-coding-agent, pi-ai, pi-agent-core, pi-tui, legacy, pi-acp, pi-mcp-adapter)
21. https://registry.npmjs.org/-/v1/search?text=keywords:pi-package — package count
22. https://pi.dev/ — tagline, claims, links
23. https://pi.dev/packages — package catalog examples
24. https://pi.dev/api/latest-version — current version
25. https://discord.com/api/v9/invites/3cU7Bz4UPx?with_counts=true — Discord size
26. https://api.github.com/orgs/earendil-works and /orgs/earendil-works/repos — org location, satellite repos
27. https://api.github.com/repos/can1357/oh-my-pi — fork stats
28. https://raw.githubusercontent.com/OpenClaw/OpenClaw/main/package.json and https://api.github.com/repos/OpenClaw/OpenClaw — OpenClaw dependency on pi-tui, stars
29. GitHub GraphQL (repo issues/PRs/discussions totals; discussion #4444) — https://github.com/earendil-works/pi/discussions/4444 — ACP request
30. https://mariozechner.at/posts/2025-11-30-pi-coding-agent/ — launch/rationale post
31. https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/ — MCP stance
32. https://mariozechner.at/posts/2026-04-08-ive-sold-out/ — acquisition terms, OpenClaw
33. https://mariozechner.at/ — author's public identity
34. https://earendil.com/ , /join/ , /posts/ , /posts/feed.rss — company, hiring, post list
35. https://earendil.com/posts/announcing-pi-and-lefos/ — acquisition, founders, backers
36. https://earendil.com/posts/pi-autoresearch-and-databricks/ — maker benchmark claims
37. https://rfc.earendil.com/keyword/pi/ — Pi RFCs (licensing, telemetry, analytics)
38. https://lucumr.pocoo.org/2026/1/27/earendil/ — company founding, Vienna
39. https://lucumr.pocoo.org/2026/1/31/pi/ — "minimal agent within OpenClaw" essay
40. https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase — independent benchmark
41. https://news.ycombinator.com/item?id=46844822 ; ?id=48837696 ; hn.algolia.com API — HN metrics
42. https://www.implicator.ai/pi-is-not-a-claude-code-rival-it-is-a-harness-rebellion/ — press, May 2026 stars/package counts
43. https://zed.dev/acp/agent/pi ; https://github.com/svkozak/pi-acp — third-party ACP adapter
44. https://agent-wars.com/news/2026-04-08-pi-agent-creator-joins-earendil ; https://www.pi-map.org/news/pi-joins-earendil/ — coverage of acquisition
45. https://github.com/can1357/oh-my-pi (README via search) — fork description

## Inclusion check (Jesse's test)

**Yes.** Pi is a full coding agent with its own agentic loop (`@earendil-works/pi-agent-core` runtime + coding-agent CLI with read/write/edit/bash tools, session management, compaction), not a wrapper around another vendor's agent; the third-party `pi-acp` adapter is a thin wrapper (no for the wrapper, yes for Pi). Source: https://github.com/earendil-works/pi/blob/main/README.md (2026-08-21)
