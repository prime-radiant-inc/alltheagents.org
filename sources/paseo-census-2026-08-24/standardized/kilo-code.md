# Standardized differentiation extraction: Kilo Code (census_slug: kilo-code)

Run 2026-08-24 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: An open-source (MIT) AI coding agent and "all-in-one agentic engineering platform" that works in VS Code, JetBrains and the CLI (plus cloud agents, code reviews and an always-on hosted agent), giving access to 500+ models at the provider's own price with zero markup. (README; homepage; GitHub description)

2. Claimed differentiators (by prominence):
   - Cost/openness of pricing: "Code with AI without breaking the bank" — models at cost, zero AI-inference markup, no lock-in, bring your own keys or run local models, no API keys required to start; the disclosed costs are a 5% credit-processing fee and per-second cloud compute. Kind: price. https://kilo.ai ; https://kilo.ai/pricing ; https://github.com/Kilo-Org/kilocode
   - Model freedom: 500+ models across 60+ providers via the Kilo Gateway, mid-task model switching, "no silent model switching", per-agent sticky models, BYOK and local (Ollama/LM Studio). Kind: model. https://kilo.ai ; https://kilo.ai/docs/code-with-ai/platforms/cli ; https://kilo.ai/articles/roo-to-kilo-migration-guide
   - Open source: MIT-licensed clients you can fork, modify and self-host; "the most popular open source coding agent" (GitHub description); CLI openly described as a fork of OpenCode enhanced for the Kilo platform. Kind: openness. https://github.com/Kilo-Org/kilocode ; https://kilo.ai
   - One platform, many surfaces: one portal controlling agents across VS Code, JetBrains, CLI, browser Cloud Agents, Slack, mobile, automated PR Code Reviews, KiloClaw (24/7 hosted agent) and Gas Town (multi-agent orchestration with coding, review and coordinator agents in parallel worktrees). Kind: capability / integration. https://kilo.ai ; https://kilo.ai/docs/code-with-ai/gastown ; https://kilo.ai/docs/kiloclaw/overview ; https://kilo.ai/docs/automate/code-reviews/overview
   - Control and transparency: prompt/context visibility; explicit allow/ask/deny permission rules with glob patterns; sensitive-file (.env) guards; parallel tools and subagents with isolated worktrees; a self-checking agent; fully autonomous `--auto` reserved for trusted CI. Kind: trust-safety / workflow. https://kilo.ai ; https://kilo.ai/docs/customize/agent-permissions ; https://github.com/Kilo-Org/kilocode

3. Stated audience: individual developers (free, open source, no credit card); "developers at" large companies (logo wall: Meta, Amazon, Airbnb, PayPal, Square, Red Hat); teams wanting usage analytics and centralized billing (Teams, $15/user/mo); enterprises needing SSO/OIDC/SCIM, audit logs and model/provider controls (Enterprise). https://kilo.ai ; https://kilo.ai/pricing ; https://kilo.ai/docs/collaborate/teams/about-plans

4. Positioning against others: names competitors directly — homepage comparison pages vs Cursor, GitHub Copilot, Roo Code, Windsurf, Claude Code; a "Migrating from Cursor/Windsurf" doc and a Roo-to-Kilo migration guide ("We started Kilo as a Roo fork in 2025"); pricing framing implies rivals add markup and lock-in ("No markup. No lock-in"). https://kilo.ai ; https://kilo.ai/docs/getting-started/migrating ; https://kilo.ai/articles/roo-to-kilo-migration-guide

5. Evidence the maker offers:
   - Adoption: "3M+ Kilo Coders", "40T+ tokens processed", "#1 Open Source Product of the Month" badge (homepage, 2026-08-21); earlier: "#1 on OpenRouter. 1.5M+ Kilo Coders. 25T+ tokens processed" (archived repo description, Feb 2026); 750,000+ downloads, #1 on OpenRouter, ~6T tokens/month (seed post, 2025-12-10). https://kilo.ai ; https://github.com/Kilo-Org/kilo ; https://blog.kilo.ai/p/kilo-raised-8-million-seed-round
   - Funding: $8M seed led by Cota Capital with Breakers, General Catalyst, Quiet Capital, Tokyo Black; co-founders Scott Breitenother (CEO) and Sid Sijbrandij (GitLab co-founder, executive chair). https://blog.kilo.ai/p/kilo-raised-8-million-seed-round
   - Logos: Meta, Amazon, Airbnb, PayPal, Square, Red Hat. https://kilo.ai
   - Content marketing with data: e.g. "We analyzed 10,643 AI code reviews", model comparison posts, own model leaderboard (kilo.ai/leaderboard). https://blog.kilo.ai ; https://kilo.ai/leaderboard
   - No external benchmark placements (SWE-bench, Terminal-Bench) offered.

6. Notable silences: no HQ, team size, or legal entity name on the site; no revenue or paying-customer figures; no external benchmark results for the harness; no OS-level sandboxing claim for local execution (permissions are policy-based); no SOC 2 / compliance certifications named on pricing or plans pages consulted; the current docs and seed post do not mention the Roo Code/Cline lineage (only the migration guide does, and the OpenCode lineage appears in a README FAQ and CLI docs); definition of "Kilo Coders" never given; ACP support exists (`kilo acp`) but is not marketed.

7. Confidence: high — materials are extensive and consistent (homepage, pricing, deep docs corpus, README, dated seed post and migration guide); main tensions are the "most popular open source coding agent" superlative versus unstated measurement, and marketing's human-in-control framing versus the fully autonomous `--auto`, Cloud Agents and Gas Town features.

Sources:
- https://kilo.ai (homepage)
- https://github.com/Kilo-Org/kilocode (README, description, LICENSE)
- https://kilo.ai/pricing
- https://kilo.ai/docs (landing) and https://kilo.ai/docs/llms.txt (full docs corpus)
- https://kilo.ai/docs/code-with-ai/platforms/cli
- https://kilo.ai/docs/code-with-ai/agents/using-agents
- https://kilo.ai/docs/customize/custom-subagents
- https://kilo.ai/docs/customize/agent-permissions
- https://kilo.ai/docs/customize/skills
- https://kilo.ai/docs/automate/extending/plugins
- https://kilo.ai/docs/automate/mcp/overview
- https://kilo.ai/docs/code-with-ai/platforms/cloud-agent
- https://kilo.ai/docs/automate/code-reviews/overview
- https://kilo.ai/docs/kiloclaw/overview
- https://kilo.ai/docs/code-with-ai/gastown
- https://kilo.ai/docs/collaborate/teams/about-plans
- https://kilo.ai/docs/getting-started/installing
- https://kilo.ai/docs/getting-started/migrating
- https://kilo.ai/articles/roo-to-kilo-migration-guide
- https://blog.kilo.ai/p/kilo-raised-8-million-seed-round
- https://blog.kilo.ai/ (blog banner metrics)
- https://github.com/Kilo-Org/kilo (archived repo description)
