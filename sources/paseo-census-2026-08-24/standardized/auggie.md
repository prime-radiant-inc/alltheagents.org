# Standardized differentiation extraction: Auggie CLI (census_slug: auggie)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: Auggie is Augment Code's agentic coding CLI that brings the company's agent, Context Engine (a semantic index of your whole codebase) and tools into the terminal — for interactive coding and for automation anywhere your code runs — as part of an "AI-native coding platform built for enterprise-grade software engineering". (README; docs cli/overview; docs introduction)

2. Claimed differentiators (by prominence):
   - Context Engine retrieval: a real-time semantic index of the full codebase finds the right code where grep/keyword-based agents miss it, on codebases up to enterprise-monorepo scale; presented as the reason the same model scores higher under Auggie. Kind: capability / performance. https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro ; https://www.augmentcode.com/
   - Token efficiency and cost: self-run head-to-heads claim equal-or-better quality than Claude Code on the same Anthropic model at 23–53% lower cost (Terminal-Bench 2.0, SWE-bench Pro; harness v2 completes a SWE-bench Pro task for $1.27 vs $2.70). Kind: performance / price. https://www.augmentcode.com/blog/auggie-beats-claude-code-on-cost-and-quality ; https://www.augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper
   - "Software factory" SDLC automation: the same agent runs as Cosmos Experts triggered by PRs, alerts, tickets and schedules (review, fix, verify, deploy loops) with humans at checkpoints; the CLI is automation-first (`--print`, GitHub Actions, service accounts). Kind: workflow / capability. https://www.augmentcode.com/ ; https://docs.augmentcode.com/cli/automation/overview
   - Multi-model with Prism routing: a curated menu of Anthropic, OpenAI, Google, Zhipu, Moonshot and xAI models plus "Prism" per-request auto-routing claimed to cost 20–30% less than frontier list price; token-based billing at provider list price + 40% service fee. Kind: model / price. https://docs.augmentcode.com/models/available-models ; https://docs.augmentcode.com/models/token-based-pricing
   - Open-standards embrace / works in your workflow: first-party ACP (`auggie --acp` for Zed/Neovim/Emacs), MCP client and server modes, agentskills.io skills, Claude Code plugin (.claude-plugin), CLAUDE.md/AGENTS.md compatibility. Kind: integration / openness (of interfaces, not source). https://docs.augmentcode.com/cli/acp/agent ; https://docs.augmentcode.com/cli/plugins

3. Stated audience: enterprise engineering organizations and teams ("enterprise-grade software engineering"; Business plan covers a whole team up to 50 seats; Enterprise adds SSO/CMEK/data residency); the CLI addresses individual developers and automation engineers ("in your terminal, on your server, or anywhere your code runs"). https://docs.augmentcode.com/introduction ; https://www.augmentcode.com/pricing ; https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli

4. Positioning against others: explicit and by name — benchmark posts name and compare Claude Code, Cursor and OpenAI Codex ("Auggie beats Claude Code on cost and quality"); the pricing page and blog also position against per-seat and credit-based pricing models; vendor-comparison pages ("X vs Cosmos") name Codex and Antigravity. https://www.augmentcode.com/blog/auggie-beats-claude-code-on-cost-and-quality ; https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro

5. Evidence the maker offers:
   - SWE-bench Pro: 51.80%, "highest of any agent tested", self-run on 731 problems vs Cursor/Claude Code/Codex on Claude Opus 4.5 (2026-02-04). https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro
   - Terminal-Bench 2.0 head-to-head on Opus 4.7: 67.4% vs Claude Code 66.3%, 32% fewer tokens, 33% lower cost, full token tables published (2026-05-15). https://www.augmentcode.com/blog/auggie-beats-claude-code-on-cost-and-quality
   - Harness v2 rebuild (fork of Pi): 53% cheaper per SWE-bench Pro task at the same pass rate (2026-08-14). https://www.augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper
   - #1 open-source SWE-bench Verified implementation (2025-03-31). https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1
   - Customer stories: Pearl Technologies (3x productivity, 100+ PRs in 30 days), WEX, GoFundMe, Intercom, Rubrik. https://www.augmentcode.com/customers
   - Homepage outcome tiles: 66% faster time-to-merge, 2–3x throughput, 60%+ CVEs auto-remediated, 70%+ incidents resolved before on-call (unattributed). https://www.augmentcode.com/
   - Internal adoption: "more than half of the people who use the CLI use it as their primary agent" (2025-12-18). https://www.augmentcode.com/blog/building-by-using-how-each-iteration-of-our-cli-taught-us-what-developers-actually-need
   - Compliance: SOC 2 Type II; claimed first AI coding assistant with ISO/IEC 42001. https://www.augmentcode.com/pricing

6. Notable silences: no user/customer counts or revenue figures anywhere; no open-source claim for the agent itself (the Pi-fork admission is the closest, and the license is proprietary-subscription); no sandboxing or OS-level isolation story for the local CLI (isolation is a Cosmos cloud/VM feature); no default permission-prompt behavior stated (docs say tools run automatically; permissions are opt-in rules); no BYO API key; plan mode exists only as a slash-command mention with no docs page; no independent (non-self-run) benchmark placements cited.

7. Confidence: high — materials are extensive and consistent (docs, README, pricing, dated launch and benchmark posts), and the positioning (Context Engine + cost efficiency + SDLC automation, aimed at enterprises) is stated repeatedly across surfaces; the main caveat is that the site is now Cosmos-first, so CLI-specific claims must be read out of blog posts rather than the homepage.

Sources:
- https://github.com/augmentcode/auggie (README)
- https://docs.augmentcode.com/introduction
- https://docs.augmentcode.com/cli/overview
- https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli
- https://docs.augmentcode.com/cli/plugins
- https://docs.augmentcode.com/cli/acp/agent
- https://docs.augmentcode.com/cli/automation/overview
- https://docs.augmentcode.com/models/available-models
- https://docs.augmentcode.com/models/token-based-pricing
- https://www.augmentcode.com/
- https://www.augmentcode.com/pricing
- https://www.augmentcode.com/customers
- https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro
- https://www.augmentcode.com/blog/auggie-beats-claude-code-on-cost-and-quality
- https://www.augmentcode.com/blog/auggie-cli-harness-rebuild-53-percent-cheaper
- https://www.augmentcode.com/blog/1-open-source-agent-on-swe-bench-verified-by-combining-claude-3-7-and-o1
- https://www.augmentcode.com/blog/building-by-using-how-each-iteration-of-our-cli-taught-us-what-developers-actually-need
- https://www.augmentcode.com/blog/intent-a-workspace-for-agent-orchestration
