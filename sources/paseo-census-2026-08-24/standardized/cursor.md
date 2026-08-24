# Standardized differentiation extraction: Cursor (census_slug: cursor)

Run 2026-08-21 against the maker's own materials only (listed under Sources). Surfaces: IDE agent, Cursor CLI (`agent` / `cursor-agent`), Cloud agents, SDK.

1. One-sentence self-description: A coding agent for building ambitious software — the same agent available in the Cursor IDE, a terminal CLI, cloud VMs (triggered from web, mobile, Slack, GitHub, Linear, API) and an SDK, that plans, writes, tests and reviews code across many models. (homepage; docs CLI overview; SDK docs)

2. Claimed differentiators (by prominence):
   - Agents do the end-to-end work (build, test, demo features) while the developer focuses on decisions; cloud agents run in parallel on isolated VMs for multi-day tasks and open PRs; always-on Automations, PR/Slack subscriptions, `/goal` long-lived objectives, Builds for 3x faster starts. Kind: capability / workflow. https://cursor.com ; https://cursor.com/docs/cloud-agent ; https://cursor.com/changelog
   - One agent across every surface with hand-off: desktop, CLI (`&` sends a task to cloud, `/in-cloud` subagents), web/iOS/iPad/Android, Slack, GitHub/Bitbucket, JetBrains via ACP, SDK with local or cloud runtime; Cursor 3 "unified workspace" for running many agents across repos. Kind: integration / workflow. https://cursor.com/docs/cli/using ; https://cursor.com/docs/sdk/typescript ; https://cursor.com/blog/cursor-3 ; https://cursor.com/docs/integrations/jetbrains
   - Model choice plus first-party models: frontier models from OpenAI, Anthropic, Google, Moonshot, Z.ai alongside Cursor's own Grok 4.6/4.5 and Composer 2.5 with more generous included usage; Cursor Router picks the model per request (Cost/Balance/Intelligence); post-SpaceX access to "the largest fleet of GPUs" for cheaper, stronger models. Kind: model / price. https://cursor.com/docs/models ; https://cursor.com/docs/models-and-pricing ; https://cursor.com/blog/joining-spacex
   - Deep customization stack: rules (.mdc, AGENTS.md), skills (open Agent Skills standard), subagents, hooks, MCP, plugins and a manually reviewed open-source marketplace, team marketplaces with required/default-on installs. Kind: capability / openness (of the extension surface). https://cursor.com/docs/plugins ; https://cursor.com/docs/skills ; https://cursor.com/docs/hooks ; https://cursor.com/docs/mcp
   - Enterprise trust and controls: 64% of Fortune 500, 50,000+ enterprises, SOC 2 Type II, AIUC-1 certification with adversarial agent testing, privacy mode / zero retention, SSO/SCIM, repo and MCP allowlists, audit logs, analytics API. Kind: trust-safety / audience. https://cursor.com/enterprise ; https://cursor.com/blog/aiuc-1

3. Stated audience: software development teams and enterprises, plus individual builders/programmers; tiers for hobbyists (free), professionals (Pro/Pro+/Ultra), teams ($40/user), enterprises (custom), and a "Start" plan for India. https://cursor.com ; https://cursor.com/pricing ; https://cursor.com/docs/models-and-pricing

4. Positioning against others: not claimed by name. Closest allusions: the evolution "from code completion to building AI teammates" (joining-spacex post) and Cursor 3 as moving past the "raw IDE" toward agent oversight; customer quote calls it "a mission control for agents rather than just a raw IDE". https://cursor.com/blog/joining-spacex ; https://cursor.com/blog/cursor-3 ; https://cursor.com/blog/coinbase

5. Evidence the maker offers:
   - Revenue/scale: >$500M annualized revenue and "over half of the Fortune 500" (2025-06-06); >$1B annualized revenue, "millions of developers", >300 staff (2025-11-13). https://cursor.com/blog/series-c ; https://cursor.com/blog/series-d
   - Enterprise page: 64% of Fortune 500, 50,000+ enterprises, 100M+ lines of code daily; logos Salesforce, Fox, PayPal, Stripe, NVIDIA, Coinbase, Rippling, JetBrains, Sentry, Vercel, Wayfair, Faire. https://cursor.com/enterprise
   - Homepage testimonials: NVIDIA (40,000 engineers), Y Combinator (adoption to >80%), Stripe, OpenAI, Eureka Labs, shadcn. https://cursor.com
   - Customer stories: Coinbase (>90% idea-to-production reduction, 55% more PRs/engineer, 75% of PRs by agents, 2,400+ devs), Wayfair (90% ML cost reduction), Faire (doubled PR throughput), Vercel; customers page (Brex >70% of engineers, Rippling 500+, Trimble 800+, Upwork +25% PR volume). https://cursor.com/blog/coinbase ; https://cursor.com/blog ; https://cursor.com/customers
   - Certification: AIUC-1 by Schellman, "several thousand scenarios", 70% of Fortune 500 (2026-08-13). https://cursor.com/blog/aiuc-1
   - Performance claims: Builds give 10x faster environment boot and 3x faster time to first token (2026-08-13). https://cursor.com/changelog
   - No benchmark scores (SWE-bench, Terminal-Bench) on the homepage, pricing, CLI docs, or launch posts consulted.

6. Notable silences: no open-source or source-available claim for the product (ToS grants a limited use right; GitHub repo is issues-only); no published benchmark results; no BYO-API-key positioning (docs mention key compatibility only in passing; SDK inference is Cursor-hosted); no absolute developer/user count beyond "millions"; IDE default autonomy (auto-run vs ask) not stated on the agent overview page; no mention of ACP on the homepage or pricing page (docs-only); no Claude Code plugin-format compatibility claim (only legacy-compat `.claude/` directories in docs).

7. Confidence: high — materials are extensive (homepage, pricing, enterprise page, docs for CLI/cloud/SDK/plugins, dated funding posts, acquisition post, customer stories) and consistent; the only wobble is the Fortune 500 share stated as "over half", 64% and 70% on different pages/dates.

Sources:
- https://cursor.com
- https://cursor.com/pricing
- https://cursor.com/enterprise
- https://cursor.com/customers
- https://cursor.com/community
- https://cursor.com/marketplace
- https://cursor.com/changelog
- https://cursor.com/blog
- https://cursor.com/blog/joining-spacex
- https://cursor.com/blog/series-d
- https://cursor.com/blog/series-c
- https://cursor.com/blog/cursor-3
- https://cursor.com/blog/coinbase
- https://cursor.com/blog/aiuc-1
- https://cursor.com/docs
- https://cursor.com/docs/cli/overview
- https://cursor.com/docs/cli/installation
- https://cursor.com/docs/cli/using
- https://cursor.com/docs/cli/headless
- https://cursor.com/docs/cli/acp
- https://cursor.com/docs/cli/changelog
- https://cursor.com/docs/cloud-agent
- https://cursor.com/docs/sdk/typescript
- https://cursor.com/docs/sdk/python
- https://cursor.com/docs/models
- https://cursor.com/docs/models-and-pricing
- https://cursor.com/docs/plugins
- https://cursor.com/docs/skills
- https://cursor.com/docs/rules
- https://cursor.com/docs/subagents
- https://cursor.com/docs/hooks
- https://cursor.com/docs/mcp
- https://cursor.com/docs/agent/overview
- https://cursor.com/docs/agent/plan-mode
- https://cursor.com/docs/integrations/jetbrains
- https://cursor.com/terms-of-service
- https://forum.cursor.com/t/cursor-cli-beta-available-now/126964
- https://github.com/cursor/cursor (README)
