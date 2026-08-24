# Standardized differentiation extraction: Factory Droid (census_slug: droid)

Run 2026-08-21 per STANDARD_PROMPT.md v1. Inputs: Factory's own materials only (README, homepage, CLI product page, docs landing/CLI overview, pricing page, Series B / Series C / Terminal-Bench / Factory 2.0 posts, enterprise page). Surfaces noted where a claim is CLI-specific vs platform-wide.

1. One-sentence self-description: Factory is an "agent-native" software development platform whose agent, Droid, works across CLI, web/desktop app, IDEs, Slack/Teams, Linear/Jira and mobile, aimed at bringing autonomy to enterprise software engineering; the Droid CLI is described as Factory's power in your terminal.

2. Claimed differentiators (ordered by prominence):
   - Benchmark leadership: Droid is "top performing in terminal benchmarks" (README), "#1" on Terminal-Bench in Sept 2025 and "#1 across the leading software development agent benchmarks" (Series C), attributed to harness design (three-tier prompting, model-specific adaptations, minimal tool set). Kind: performance. URLs: https://github.com/Factory-AI/factory, https://factory.ai/news/terminal-bench, https://factory.ai/news/series-c
   - Model independence: not locked to one provider; route each task to the best model (Factory Router); supports frontier and open-weight models plus BYOK; "Droid Core" open-weight pool. Kind: model. URLs: https://docs.factory.ai/cli/getting-started/overview, https://factory.ai/pricing, https://factory.ai/news/software-factory
   - One agent, every surface, shared memory/config: CLI, desktop/web app, VS Code/JetBrains/Zed, Slack, Linear/Jira, mobile; skills and plugins sync across surfaces; persistent sessions/missions. Kind: integration / workflow. URLs: https://github.com/Factory-AI/factory, https://factory.ai/product/cli
   - Enterprise-grade security and governance: SOC 2, ISO 42001, GDPR/CCPA, on-premise and airgapped deployment, SSO/SAML/SCIM, zero data retention, org-level autonomy caps and deny lists, "we prioritize security and quality over racing to the lowest price point". Kind: trust-safety. URLs: https://docs.factory.ai/cli/getting-started/overview, https://factory.ai/enterprise, https://docs.factory.ai/pricing
   - Controlled, transparent autonomy and delegation: Spec Mode plans before any change, tiered autonomy levels, visible/reviewable diffs, headless `droid exec` read-only by default; Missions for multi-agent orchestration of larger work; "Software Factory" 24/7 automation vision (Factory 2.0). Kind: workflow / capability. URLs: https://docs.factory.ai/cli/getting-started/overview, https://factory.ai/product/cli, https://factory.ai/news/software-factory

3. Stated audience: "enterprise teams", global systems integrators and AI labs (https://factory.ai); "highest-security customers — systemically important banks, governments, healthcare, national security" (https://docs.factory.ai/enterprise); individual developers via Pro/Plus/Max plans and teams up to 150 seats via Business (https://factory.ai/pricing); engineering leaders measuring AI impact (https://factory.ai/news/agent-effectiveness). No language/stack restriction claimed (enterprise page: "100+ development frameworks", "40+ languages").

4. Positioning against others: names competitors in the Terminal-Bench post — Droid "outperforming" Claude Code and Codex CLI with scores cited (https://factory.ai/news/terminal-bench); product page positions Droid as built for "delegation" rather than autocomplete (https://factory.ai/product/cli); enterprise docs contrast with "a single cloud IDE" (https://docs.factory.ai/enterprise); CLI overview: "no need to switch editors" (https://docs.factory.ai/cli/getting-started/overview).

5. Evidence the maker offers:
   - Terminal-Bench scores: Droid + Opus 4.1 58.8% (#1), GPT-5 52.5%, Sonnet 4 50.5% vs Claude Code 43.2%, Codex CLI 42.8% (Sept 2025) — https://factory.ai/news/terminal-bench; docs benchmark pages (Terminal Bench, Agent Arena, Legacy-Bench, Next.js evals, Review Benchmark) — https://docs.factory.ai/benchmarks/terminal-bench
   - Outcome numbers: 31x faster feature delivery, 96.1% shorter migration times, 95.8% shorter on-call resolution (Series B); 7x faster feature delivery, 40% incident-response reduction at Empower (enterprise page) — https://factory.ai/news/series-b, https://factory.ai/enterprise
   - Usage/growth: "hundreds of thousands of developers" daily; revenue doubled month-over-month for six months (Series C) — https://factory.ai/news/series-c
   - Customer names: MongoDB, EY, Bayer, Zapier, Clari (Series B); Nvidia, Adobe, EY, Palo Alto Networks, Adyen (Series C); Blackstone, Wipro, Comarch, Groq, Chainguard, You.com, Podium (homepage); Nav, Tilt, Empower (enterprise page, with CTO quotes); case studies You.com, Comarch — https://factory.ai, https://factory.ai/enterprise, https://factory.ai/news
   - Funding as credibility: $50M Series B (NEA, Sequoia, J.P. Morgan, Nvidia), $150M Series C at $1.5B (Khosla) — https://factory.ai/news/series-b, https://factory.ai/news/series-c

6. Notable silences: the homepage and CLI product page do not mention MCP, hooks, plan/spec mode, sandboxing, subagents, ACP, SDKs, or pricing (all of these appear only in docs); no material states that the CLI is closed-source/proprietary (README carries only a copyright line); no absolute revenue, seat, or customer-count figures; homepage names no models or vendors; no published comparison with IDE-first tools (Cursor, Copilot) by name; no statement of default autonomy level out of the box; no changelog-style public roadmap on marketing pages.

7. Confidence: high — materials are plentiful (README, homepage, product page, extensive docs, dated funding and benchmark posts, pricing page) and consistent in their top claims (benchmarks, model independence, enterprise governance, multi-surface); the only ambiguity is how much weight to give the CLI-specific vs platform-wide framing, since marketing pages lead with the enterprise "autonomy stack" while docs lead with the CLI.

Sources:
- https://github.com/Factory-AI/factory (README)
- https://factory.ai
- https://factory.ai/product/cli
- https://factory.ai/enterprise
- https://factory.ai/pricing
- https://docs.factory.ai (welcome/landing)
- https://docs.factory.ai/cli/getting-started/overview
- https://docs.factory.ai/pricing
- https://docs.factory.ai/models
- https://docs.factory.ai/enterprise
- https://docs.factory.ai/benchmarks/terminal-bench
- https://factory.ai/news/terminal-bench
- https://factory.ai/news/series-b
- https://factory.ai/news/series-c
- https://factory.ai/news/software-factory
- https://factory.ai/news/agent-effectiveness
- https://factory.ai/news
