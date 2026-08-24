# Tier-1 harness brief (for Eden) — 2026-08-21

Six harnesses, one block each. Everything below traces to dossiers/<slug>.md and standardized/<slug>.md; the master table is master.tsv. "Observable" = we measured it ourselves (GitHub, npm, Homebrew); "maker-claimed" = the company said it.

## Claude Code (Anthropic)
- What it is: Anthropic's closed-source coding agent that runs in your terminal (and in VS Code/JetBrains, a desktop app, the web, Slack and CI) using only Claude models; you get it with a Claude Pro/Max/Team/Enterprise subscription or pay per API token.
- Who makes it: Anthropic PBC, San Francisco; Series H $65B at $965B valuation (2026-05-28); named Claude Code leads include Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code).
- Adoption facts: 18.3M npm downloads/week and 23.7M VS Code installs (observable); 142k GitHub stars (observable); Anthropic says >$2.5B run-rate with weekly users doubled since Jan 1 (2026-02-12); #1 on the Terminal-Bench 2.1 agent leaderboard (83.8% with Fable 5).
- How it plugs in: MCP client; its own plugin/marketplace format (the one everyone else copies); subagents, hooks, plan mode; Agent SDK in Python/TS; no first-party ACP (third parties wrap it).
- Maker says special: one engine on every surface (same CLAUDE.md, settings and MCP servers across terminal, IDE, desktop, web, Slack, CI) and terminal-native Unix-style composability.
  Also: deep codebase understanding, heavy customization (skills, hooks, plugins, agent teams), "autonomy with control".
- Things worth an opinion on: (a) the product page still says "asks permission before file changes" while docs made auto mode (a classifier decides) the default on paid plans since 2026-08-14; (b) the census calls it "source available" but the license is all-rights-reserved and only repo scaffolding is public; (c) locked to one model vendor vs the rest of this list; (d) the $8B run-rate / 4.2M WAU numbers floating around have no Anthropic source — only $2.5B (Feb 2026) is on the record.
- Your take: ____

## Codex CLI (OpenAI)
- What it is: OpenAI's open-source (Apache-2.0, Rust) terminal coding agent, also available as an IDE extension, a cloud service, and inside the ChatGPT desktop app; defaults to OpenAI models but can point at Azure, Bedrock, local Ollama or any OpenAI-compatible endpoint; included in every ChatGPT tier including Free.
- Who makes it: OpenAI Group PBC, San Francisco ($122B raised at $852B, 2026-03-31); Tibo Sottiaux is GM of Codex, Alexander Embiricos lead PM (both named on OpenAI's own forum pages). Note: all openai.com pages returned 403 to us, so the maker's user figures came through press.
- Adoption facts: 13.5M npm downloads/week and the #1 Homebrew cask (observable); 111k GitHub stars with 2,802 commits in 90 days (observable); OpenAI says >5M weekly active users (2026-06-02, via press) — the "10M" figure is Codex + ChatGPT Work combined, not comparable.
- How it plugs in: MCP client AND server; plugins + marketplaces shared with ChatGPT, Agent Skills standard; subagents, hooks, plan mode; TS/Python SDK; no first-party ACP (request closed "not planned"); partial Claude Code compatibility — reads .claude-plugin manifests/marketplaces and has a /import migrator, but does not read CLAUDE.md or .claude/skills.
- Maker says special: runs locally, open source, one-line install, same agent across CLI/IDE/cloud/desktop; sign in with the ChatGPT plan you already pay for instead of per-token billing.
  Also: OS-level sandbox and network-off by default; extensible via skills/plugins/MCP/hooks; multi-agent; embeddable.
- Things worth an opinion on: (a) "open source" is the CLI only — cloud, IDE binary, desktop app and models are closed; (b) the quiet Claude Code import/marketplace support reads as a switch-to play; (c) "Codex is for everyone who does work on a computer" — positioning beyond coding; (d) Terminal-Bench numbers: our Claude Code dossier has Claude Code + Fable 5 at #1 (83.8%, harness leaderboard) while the Codex dossier cites an aggregator saying GPT-5.6 Sol 89.5% (model-level) — different sources and levels, do not compare directly.
- Your take: ____

## GitHub Copilot CLI (GitHub / Microsoft)
- What it is: GitHub's closed-source terminal coding agent that routes to Anthropic, OpenAI and Google models (you can also bring your own key), included in every Copilot plan including Free and billed from the plan's AI-credit allowance.
- Who makes it: GitHub, Inc., San Francisco, a Microsoft subsidiary with no standalone CEO since Aug 2025; leadership page names Kyle Daigle (COO, developer outreach), Vladimir Fedorov (CTO), Mario Rodriguez (CPO), Elizabeth Pemmerl (CRO).
- Adoption facts: 1.46M npm downloads/week (partly SDK-bundled) and 64k Homebrew installs in 90 days, the cleanest human proxy (observable); 11k GitHub stars (observable, but the repo has no source); Microsoft says CLI usage "nearly doubling month over month" (2026-04-29) and 50M Copilot users family-wide (2026-07-29) — no CLI-specific user count exists.
- How it plugs in: MCP client with the GitHub MCP server built in; own plugin marketplaces (Agent Plugins 1.0); subagents (/fleet), hooks, plan mode; ACP server built in; SDK in six languages (MIT); reads CLAUDE.md, .claude/skills, .claude-plugin plugins and .claude/settings.json (changelog-documented, not on a docs page; user-level ~/.claude deliberately not loaded).
- Maker says special: GitHub-native — works directly with issues, branches and PRs and respects branch protections and org policies; same agent runtime as the Copilot coding agent and SDK, remembers across sessions.
  Also: multi-model switching mid-session, /fleet parallel agents, every action previewed and approved, included in all plans.
- Things worth an opinion on: (a) census says "source available" — it is not, the repo is README/changelog/install script and the binary license forbids derivatives; (b) the broadest quiet Claude Code compatibility of the big three; (c) the only tier-1 vendor harness that is multi-model and ACP-native; (d) billing moved from "premium requests" to AI credits on 2026-06-01 — the census pricing text is stale.
- Your take: ____

## OpenCode (Anomaly, formerly SST)
- What it is: an MIT open-source coding agent for terminal, desktop, web UI and IDE that runs on any of 75+ model providers (including local models and your existing Claude/ChatGPT/Copilot subscription); the software is free, with optional paid Zen (pay-as-you-go gateway), Go ($10/month open-weight models) and Enterprise.
- Who makes it: Anomaly (GitHub anomalyco; the team formerly known as SST), Toronto, YC W21, ~24 people; Jay V (CEO/Founder), Frank Wang (CTO/Founder), Dax Raad and Adam Elmore (co-founders). No head of product/DevRel/partnerships named.
- Adoption facts: 199,960 GitHub stars — the most-starred coding agent in this set (observable); 1.73M npm downloads/week, growing from 42k/month in mid-2025 to ~9M/month (observable); 77k Discord members (observable); maker claims "over 16M developers every month" (not verifiable); Cloudflare's own blog documents internal use (27M messages in 30 days).
- How it plugs in: MCP client; JS/TS plugins via npm (no marketplace); subagents; plan agent; ACP (opencode acp); SDK over its HTTP server; hooks only through the plugin API (no shell hooks); reads CLAUDE.md and .claude/skills only.
- Maker says special: open source, MIT, the whole agent including desktop/IDE/web is the public repo; provider-agnostic with 75+ providers, free models included, log in with subscriptions you already have.
  Also: privacy ("does not store any of your code"), LSP auto-loaded, client/server architecture with shareable sessions, Zen "zero markups".
- Things worth an opinion on: (a) most permissions default to "allow" in the build agent (edits and shell run without asking); (b) "not an AI product" framing from the CEO vs the Zen/Go paid model layer as the business; (c) funding is murky — the widely indexed "$17M Anomaly raise" is a different company; (d) README says the plan agent "denies" edits, docs say "ask".
- Your take: ____

## Pi (Earendil Inc., created by Mario Zechner)
- What it is: an MIT open-source, deliberately minimal terminal coding harness — four tools, a system prompt under 1,000 tokens, no permission prompts — that you extend with TypeScript extensions, skills and packages; runs on ~30 providers plus Claude/ChatGPT/Copilot logins; free, no paid tier.
- Who makes it: created by Mario Zechner (badlogic) in Aug 2025; acquired 2026-04-08 by Earendil Inc., a Vienna-based PBC cofounded by Armin Ronacher and Colin Daymond Hanna, backed by Accel and Balderton (amount undisclosed); Zechner keeps technical direction. No CEO/CTO titles published.
- Adoption facts: 95k GitHub stars and 1.9M npm downloads/week (+443k on the deprecated old package name) (observable); Databricks' independent benchmark on its multi-million-line codebase: same success rate as Claude Code/Codex at ~2x lower cost (2026-07-08); OpenClaw (387k stars) is built on Pi components and pi-tui is its dependency.
- How it plugs in: by design NO built-in MCP, subagents, plan mode or ACP — community packages add each (pi-mcp-adapter 161k/week, pi-acp on Zed's registry); yes to extensions with ~35 lifecycle events (its hooks), skills, TS SDK and RPC mode; reads CLAUDE.md and can load .claude/skills.
- Maker says special: a minimal core that deliberately omits what other harnesses bake in; extensibility IS the product — the agent can extend itself; tagline "There are many agent harnesses but this one is yours".
  Also: BYO model across ~30 providers; context efficiency (cites Databricks); four run modes make it embeddable.
- Things worth an opinion on: (a) no permission prompts and no sandbox by default — runs with your OS permissions; (b) the only harness here that publicly rejects MCP; (c) acquisition by Earendil with Fair Source / paid enterprise tiers "contemplated" (RFC 0015) vs "core stays MIT"; (d) the maker restates the Databricks result more strongly ("highest pass-rate") than Databricks did ("same success rate at 2x less cost").
- Your take: ____

## Oh My Pi / omp (can1357)
- What it is: an MIT open-source fork of Pi that goes the opposite way — batteries included: LSP, a real debugger (DAP), subagents in isolated worktrees, plan mode, hooks, MCP client, ACP, a native Rust engine; 60+ providers; free; defaults to auto-approving all tool calls ("yolo").
- Who makes it: individual maintainer can1357 (Can Boluk, security researcher); "Stencil Labs, Inc." appears as author/copyright holder but has no public HQ, team or funding info. Contact is the Discord only. Paseo ships it disabled by default.
- Adoption facts: 26k GitHub stars, up from 5.5k in May 2026 (observable); 97k npm downloads/week, up from ~2k/week in January (observable; about 5.6% of Pi's npm volume, though binary installs are not counted); 2.5k Discord members; no maker-claimed user numbers at all.
- How it plugs in: the most Claude-Code-compatible harness here — it documents Claude Code plugin registry/marketplace compatibility and imports config from .claude, .cursor, .codex, .cline, .gemini etc.; MCP client; subagents; hooks; plan mode; ACP server (not yet in the ACP registry); SDK + RPC.
- Maker says special: a per-model-tuned ("benchmaxxed") tool harness — hash-anchored edits and tuned prompts raise pass rates and cut tokens, per its own benchmark; and "the IDE wired in" — LSP on every write, real debugger control, persistent code cells.
  Also: ~80k-line Rust engine, advisor second model reviewing every turn, "time-traveling stream rules", native reading of every other tool's configs.
- Things worth an opinion on: (a) fork vs philosophy — Pi is minimal on purpose, omp disagrees and the last recorded upstream sync marker is 2026-03-22; (b) default "yolo" approval plus browser/desktop-driving tools with no sandbox story; (c) a one-person project shipping several releases a day with a company name and no company; (d) benchmark evidence is all self-run.
- Your take: ____

## Cross-dossier notes
- Terminal-Bench 2.1: the Claude Code dossier (tbench.ai agent leaderboard) and the Codex dossier (morphllm aggregator, model-level) give non-comparable numbers; see the Codex block.
- Pi vs omp npm volume: the omp dossier says "Pi ~1.6M+/week"; the Pi dossier measured 1.90M for the same week — same order, the omp figure is a lower bound.
- Claude Code compatibility spectrum (from weakest to strongest, per dossiers): Codex (manifests/import only) < OpenCode and Pi (CLAUDE.md + skills) < Copilot CLI (plugins, settings, hooks; changelog-only) < omp (documented marketplace compatibility).
