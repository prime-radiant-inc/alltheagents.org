# Standardized differentiation extraction: Cline (census_slug: cline)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: An open-source AI coding agent that lives in your IDE and terminal (and, via an SDK, in your own apps), reads and writes files, runs commands and uses a browser and MCP tools on any model provider, with every action subject to your approval. (README; docs overview)

2. Claimed differentiators (by prominence):
   - Open source: "The open source coding agent", Apache 2.0, positioned as auditable and community-driven; cites GitHub Octoverse 2025 naming it the fastest-growing AI open-source project. Kind: openness. https://github.com/cline/cline ; https://cline.bot ; https://cline.bot/blog/cline-the-fastest-growing-ai-open-source-project-on-github-in-2025-thanks-to-you
   - Model-agnostic, no lock-in: "Works With Every Model" — Anthropic, OpenAI, Google, OpenRouter, Bedrock, Azure/Vertex, Cerebras/Groq, local Ollama/LM Studio, any OpenAI-compatible endpoint; plus Cline credits across 100+ models and ClinePass ($9.99/mo) for open-weight models; bring your own inference at your negotiated rates, "no markup". Kind: model / price. https://github.com/cline/cline ; https://docs.cline.bot/getting-started/cline-provider ; https://docs.cline.bot/getting-started/clinepass ; https://docs.cline.bot/enterprise-solutions/overview
   - Human-in-the-loop control: every file edit and command requires approval; Plan mode (read-only) vs Act mode; diffs, checkpoints and one-click undo; opt-in auto-approve/YOLO for autonomy. Kind: trust-safety / workflow. https://docs.cline.bot/cline-overview ; https://docs.cline.bot/core-workflows/plan-and-act ; https://docs.cline.bot/features/auto-approve
   - One agent core, many surfaces and orchestration: the SDK is "the same harness" behind the CLI, Kanban, VS Code and JetBrains; ACP mode puts it in Zed/JetBrains/Neovim/Emacs; multi-agent teams, read-only subagents, scheduled (cron) agents, Slack/Telegram/Discord connectors, headless CI/CD, Kanban parallel worktrees. Kind: capability / integration. https://docs.cline.bot/sdk/overview ; https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime ; https://docs.cline.bot/usage/acp ; https://github.com/cline/cline
   - Secure, client-side, enterprise-governable: code stays in your environment, no indexing, no training on your data; SSO/SCIM, RBAC, model and MCP controls, remote config, OpenTelemetry export; extensible via MCP Marketplace, rules, skills, plugins and hooks. Kind: trust-safety / capability. https://cline.bot/enterprise ; https://docs.cline.bot/enterprise-solutions/overview ; https://cline.bot/blog/introducing-the-mcp-marketplace-clines-new-app-store ; https://docs.cline.bot/sdk/plugins

3. Stated audience: individual developers ("Free for individual developers" on the pricing page); engineering teams and enterprise "platform teams" that need central governance (Enterprise tier, "Fortune 100" customers named); developers embedding agents in their own products via the SDK; users of any ACP-capable editor. https://cline.bot/pricing ; https://cline.bot/enterprise ; https://docs.cline.bot/sdk/overview ; https://docs.cline.bot/usage/acp

4. Positioning against others: no competitor named. Allusions: "Most AI tools force you to buy inference through them with markup" (enterprise docs); "no vendor lock-in" (pricing/enterprise pages); the 1M-installs post contrasts itself with tools that impose "context limitations" or "artificial constraints" on frontier models. https://docs.cline.bot/enterprise-solutions/overview ; https://cline.bot/pricing ; https://cline.bot/blog/1-000-000-installs-and-our-all-in-bet-on-the-future-of-software-engineering

5. Evidence the maker offers:
   - Adoption: "8.0M+ installs across all platforms" / "Trusted by 8M+ developers", 66.6k GitHub stars, 4.1/5 from 312 VS Code reviews (homepage, 2026-08-21); "over 7 million developers" (2026-05-13); "5+ million developers" (2026-02-13); 3.8M installs (2025-11-04); 2.7M installs, 48k stars, 48k X followers, 20k Discord (2025-07-31); 1M installs (2025-03-22); 700k VS Code downloads (2025-02-19). https://cline.bot ; https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime ; https://cline.bot/blog/introducing-cline-cli-2-0 ; https://cline.bot/blog/cline-the-fastest-growing-ai-open-source-project-on-github-in-2025-thanks-to-you ; https://cline.bot/blog/cline-raises-32m-series-a-and-seed-funding-building-the-open-source-ai-coding-agent-that-enterprises-trust ; https://cline.bot/blog/1-000-000-installs-and-our-all-in-bet-on-the-future-of-software-engineering ; https://cline.bot/blog/introducing-the-mcp-marketplace-clines-new-app-store
   - Third-party ranking cited: GitHub Octoverse 2025 — fastest-growing AI OSS project, 4,704% YoY contributor growth, #2 overall. https://cline.bot/blog/cline-the-fastest-growing-ai-open-source-project-on-github-in-2025-thanks-to-you
   - Customers/logos: Samsung, Salesforce, Oracle, Amazon, LG, Globant, Microsoft, eBay, Visa, IBM (homepage); Credit Karma, Lockheed Martin, Plaid, Reddit, Roche, Sony (enterprise page); Salesforce Agentforce "built using Cline's architecture", Samsung/SAP/Oracle "tens of thousands of developers" (enterprise launch post). https://cline.bot ; https://cline.bot/enterprise ; https://cline.bot/blog/introducing-cline-for-enterprise
   - Funding: $32M seed + Series A (Emergence Capital, Pace Capital, 1984 Ventures, Essence VC, Cox Exponential, named angels). https://cline.bot/blog/cline-raises-32m-series-a-and-seed-funding-building-the-open-source-ai-coding-agent-that-enterprises-trust
   - Benchmark: 74.2% on Terminal-Bench with Claude Opus 4.7 via the SDK harness; claims lower token cost and faster completion than the previous CLI. https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime
   - Demos: Plan & Act video, auto-approve video, quickstart SDK example. https://docs.cline.bot/core-workflows/plan-and-act ; https://docs.cline.bot/features/auto-approve ; https://docs.cline.bot/sdk/overview

6. Notable silences: no SWE-bench or other public-leaderboard placement; no absolute paying-customer or revenue figures; no statement of team size or HQ on company pages; no OS-level sandboxing claim in product materials (only a `CLINE_SANDBOX` env var in config docs); no compliance certifications (SOC 2 etc.) on the enterprise page; JetBrains plugin and Desktop app source not addressed beyond "not open-sourcing JetBrains plugins"; no Claude Code plugin/marketplace compatibility claim (only `.claude/skills` as a skills path and a Claude-subscription provider).

7. Confidence: high — materials are extensive and consistent (README, docs overview, pricing and enterprise pages, five dated launch/milestone posts with numbers); the main tension is the docs' "every action requires your approval" default versus prominent YOLO/auto-approve/headless autonomy features, and the plugins docs saying plugins are not yet available in the VS Code/JetBrains extensions while a blog post says they are reusable there.

Sources:
- https://github.com/cline/cline (README)
- https://cline.bot
- https://cline.bot/cli
- https://cline.bot/pricing
- https://cline.bot/enterprise
- https://cline.bot/mcp-marketplace
- https://docs.cline.bot/cline-overview
- https://docs.cline.bot/getting-started/installing-cline
- https://docs.cline.bot/getting-started/cline-provider
- https://docs.cline.bot/getting-started/clinepass
- https://docs.cline.bot/core-workflows/plan-and-act
- https://docs.cline.bot/features/auto-approve
- https://docs.cline.bot/features/subagents
- https://docs.cline.bot/cli/agent-teams
- https://docs.cline.bot/usage/acp
- https://docs.cline.bot/usage/kanban
- https://docs.cline.bot/sdk/overview
- https://docs.cline.bot/sdk/plugins
- https://docs.cline.bot/customization/plugins
- https://docs.cline.bot/customization/skills
- https://docs.cline.bot/enterprise-solutions/overview
- https://cline.bot/blog/introducing-the-mcp-marketplace-clines-new-app-store
- https://cline.bot/blog/1-000-000-installs-and-our-all-in-bet-on-the-future-of-software-engineering
- https://cline.bot/blog/cline-raises-32m-series-a-and-seed-funding-building-the-open-source-ai-coding-agent-that-enterprises-trust
- https://cline.bot/blog/introducing-cline-for-enterprise
- https://cline.bot/blog/cline-the-fastest-growing-ai-open-source-project-on-github-in-2025-thanks-to-you
- https://cline.bot/blog/introducing-cline-cli-2-0
- https://cline.bot/blog/introducing-cline-sdk-the-upgraded-agent-runtime
- https://cline.bot/blog/extend-cline-with-plugins-and-hooks
