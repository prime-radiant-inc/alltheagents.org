# Standardized differentiation extraction: Devin (census_slug: devin-ai)

Run 2026-08-21 against the maker's own materials only (listed under Sources). Surfaces: cloud Devin, Devin CLI, Devin Desktop (ex-Windsurf) — noted per claim where the materials distinguish them.

1. One-sentence self-description: Devin is "the AI software engineer" — an autonomous agent that writes, runs and tests code in its own cloud machine for engineering teams, now offered as one agent across a desktop IDE (Devin Desktop), the cloud (Devin Cloud), the terminal (Devin CLI) and code review (Devin Review). (devin.ai; docs intro; Devin Desktop post)

2. Claimed differentiators (by prominence):
   - Autonomous software engineer, not an assistant: runs in its own VM with shell, IDE, browser and desktop, plans and executes complex tasks end-to-end (tickets, features, migrations, incident triage) — "if you can do it in three hours, Devin can most likely do it"; self-reviews before opening PRs. Kind: capability. https://devin.ai ; https://docs.devin.ai/get-started/devin-intro ; https://cognition.com/blog/introducing-devin-2-2
   - Fleets and parallelism: spin up many Devins / "a fleet of agents" to migrate all repos in parallel, schedule chores, and work multi-week multi-repo projects; Devin improves by reading past session trajectories. Kind: workflow / capability. https://devin.ai ; https://cognition.com/blog/devin-2
   - Start local, hand off to the cloud: Devin CLI is a local terminal agent with `/handoff` to a cloud Devin that has its own computer and keeps working after you close your laptop; billed as the first CLI agent with a dedicated VM. Kind: workflow. https://cognition.com/blog/devin-for-terminal ; https://docs.devin.ai/cli ; https://docs.devin.ai/cli/handoff
   - Any frontier model plus Cognition's own: Anthropic, OpenAI, Google and open-source models, Cognition's SWE-1.x models (SWE-1.7 "frontier-level intelligence at a much lower cost", ~1000 tok/s), Adaptive router, Devin Fusion at 35% lower cost; "First class support for every major model provider". Kind: model / price. https://docs.devin.ai/cli/models ; https://cognition.com/blog/swe-1-7 ; https://devin.ai/pricing
   - One Devin, every surface, and an open agent hub: same agent and context across Desktop (IDE with an Agent Command Center and Spaces), Cloud, CLI and Review; Devin Desktop hosts third-party agents via the Agent Client Protocol (Codex, Claude Agent, OpenCode, in-house agents). Kind: integration / openness (of the host, not the source). https://devin.ai/blog/windsurf-is-now-devin-desktop ; https://docs.devin.ai/desktop/acp
   - (secondary) Works where the team works with enterprise controls: Slack/Teams, Linear/Jira, GitHub PR loop, API and Automations, MCP for "hundreds of tools"; Knowledge/Playbooks/DeepWiki to learn the codebase; OS-level sandbox, permissions, team settings, SSO/RBAC, VPC. Kind: integration / trust-safety. https://devin.ai ; https://docs.devin.ai/cli/reference/permissions ; https://devin.ai/pricing

3. Stated audience: "engineering teams with complex, multi-repo projects" (homepage); "ambitious engineering teams" who want to "crush their backlogs" (docs); enterprises (named banks, automakers, government — "Cognition for Government"); individuals via Free/Pro/Max plans; the CLI is positioned for quick fixes, exploration and interactive coding with longer tasks handed to the cloud. https://devin.ai ; https://docs.devin.ai/get-started/devin-intro ; https://devin.ai/pricing ; https://cognition.com

4. Positioning against others: Cognition calls Devin "the first autonomous software engineer" and the CLI "the first CLI agent with its own dedicated virtual machine"; the docs contrast Devin CLI ("local coding agent") with cloud Devin ("runs in a virtual machine") and the Desktop post contrasts a "full IDE with an agent manager built in — not the other way around". Competitors are named only as supported guests: Devin Desktop runs "Codex, Claude Agent, OpenCode" via ACP, and the handoff plugin works from "Claude Code, Codex, Cursor". https://cognition.com ; https://cognition.com/blog/devin-for-terminal ; https://docs.devin.ai/cli ; https://devin.ai/blog/windsurf-is-now-devin-desktop ; https://docs.devin.ai/cli/handoff

5. Evidence the maker offers:
   - $492M annualized run-rate revenue; enterprise usage >10x since start of 2026; 89% of code committed at Cognition is committed by Devin; named customers Citi, Mercedes-Benz, Goldman Sachs, Elevance, Dell, Santander, U.S. Army, U.S. Navy, Infosys, Cognizant, Itaú, Exa, Modal, Eight Sleep, OpenRouter (2026-05-27). https://cognition.com/blog/series-d
   - "Hundreds of thousands of PRs merged", 67% PR merge rate (vs 34% prior year), "thousands of companies", DeepWiki over 400,000 repos (2025-11-14). https://cognition.com/blog/devin-annual-performance-review-2025
   - Customer case numbers on devin.ai/customers: Mercedes-Benz COBOL migration 8 months -> 8 days; EBANX 92% of merged PRs; Gumroad 1,500+ merged PRs; Hamming 25% of code volume; Litera regression cycles -90%; FE fundinfo 1,800 repos. https://devin.ai/customers
   - Windsurf at acquisition: $82M ARR, 350+ enterprise customers, hundreds of thousands of DAU (2025-07-14); "Millions of engineers use Windsurf and Devin" (2026-06-02). https://cognition.com/blog/windsurf ; https://devin.ai/blog/windsurf-is-now-devin-desktop
   - Benchmarks: SWE-bench 13.86% end-to-end at launch (2024-03-12); SWE-1.7 model: Terminal-Bench 2.1 81.5%, SWE-Bench Multilingual 77.8%, FrontierCode 1.1 42.3% (2026-07-08). https://cognition.com/blog/introducing-devin ; https://cognition.com/blog/swe-1-7
   - Docs claims: subagents "improve overall coding performance and reduce cost"; Devin Local "up to 30% more token efficient" than Cascade. https://docs.devin.ai/cli/subagents ; https://devin.ai/blog/windsurf-is-now-devin-desktop
   - Launch quotes from Ramp, Harvey, NVIDIA, Modal, Intact Financial (Devin Desktop). https://devin.ai/blog/windsurf-is-now-devin-desktop

6. Notable silences: no open-source or source-available claim (license not discussed; repo is release-only); no BYO API key / local-model option stated for the CLI; no independent benchmark placement of the Devin harness itself (only model scores and a self-run 2024 SWE-bench subset); plugins are in closed beta and not promoted on the homepage; no absolute user counts beyond "millions of engineers"; no Discord/community channel on the main materials; ACP is stated for Desktop/Zed/JetBrains/Xcode docs but not on the homepage; Windsurf pricing still points at windsurf.com after the rebrand.

7. Confidence: high — materials are extensive and consistent (homepage, pricing, docs CLI/cloud/desktop, dated launch posts with numbers, customer page); residual uncertainty is only in which surface a given claim applies to, since the company now presents cloud, CLI and Desktop as "one Devin".

Sources:
- https://devin.ai (homepage, read 2026-08-21)
- https://devin.ai/pricing
- https://devin.ai/customers
- https://devin.ai/blog/windsurf-is-now-devin-desktop
- https://docs.devin.ai/get-started/devin-intro
- https://docs.devin.ai/cli (cli.devin.ai/docs)
- https://docs.devin.ai/cli/models
- https://docs.devin.ai/cli/handoff
- https://docs.devin.ai/cli/subagents
- https://docs.devin.ai/cli/reference/permissions
- https://docs.devin.ai/cli/extensibility/plugins/overview
- https://docs.devin.ai/desktop/acp
- https://docs.devin.ai/admin/billing/self-serve
- https://cognition.com
- https://cognition.com/blog/introducing-devin
- https://cognition.com/blog/devin-2
- https://cognition.com/blog/introducing-devin-2-2
- https://cognition.com/blog/devin-for-terminal
- https://cognition.com/blog/windsurf
- https://cognition.com/blog/series-d
- https://cognition.com/blog/devin-annual-performance-review-2025
- https://cognition.com/blog/swe-1-7
