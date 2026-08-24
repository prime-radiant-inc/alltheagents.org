# Standardized differentiation extraction: Kiro (census_slug: kiro)

Run 2026-08-21 against the maker's own materials only (listed under Sources). Covers Kiro IDE and Kiro CLI; surface noted where a claim is surface-specific.

1. One-sentence self-description: An agentic development environment from AWS — an IDE, CLI, web and mobile app sharing one agent — that takes developers "from prototype to production" through spec-driven development (prompts become structured requirements/design/tasks), agent hooks, steering files and powers, summarized by the homepage line "Move beyond AI coding to agentic engineering". (homepage; README; launch post)

2. Claimed differentiators (by prominence):
   - Spec-driven development: prompts are turned into executable specs (requirements, design, tasks) before code, positioned against "vibe coding"; the maker says it was first to bring this to AI coding tools. Kind: workflow. https://kiro.dev/ ; https://kiro.dev/blog/introducing-kiro/ ; https://kiro.dev/blog/one-year/
   - Correctness beyond passing tests: property-based testing checks code against the spec and automated reasoning finds contradictions and gaps in requirements ("find bugs unit tests miss"). Kind: capability. https://kiro.dev/ ; https://kiro.dev/blog/general-availability/ ; https://kiro.dev/docs/specs/
   - Structure and control for the agent: steering files, event-driven hooks, custom agents and sub-agents, capability-based permissions with Autopilot/Supervised modes, plan agent, checkpoints/rewind. Kind: capability / trust-safety. https://kiro.dev/docs/ ; https://kiro.dev/docs/permissions/ ; https://kiro.dev/docs/hooks/
   - One agent on every surface plus open integration: the same harness and `.kiro` configuration across IDE, CLI, web, iOS and cloud sessions; headless CLI for CI/CD; Powers in the open Agent Plugins format; MCP; Agent Skills; ACP so Kiro CLI runs inside JetBrains, Zed and other editors. Kind: integration. https://kiro.dev/blog/one-agent/ ; https://kiro.dev/docs/powers/ ; https://kiro.dev/docs/cli/acp/ ; https://kiro.dev/blog/kiro-adopts-acp/
   - Multi-model choice with Auto routing and credit pricing without daily/weekly rate limits; enterprise-grade identity (IAM Identity Center/SSO), centralized billing, GovCloud, data not used for training on paid tiers, "built and operated by AWS". Kind: model / price / trust-safety. https://kiro.dev/pricing/ ; https://kiro.dev/docs/models/ ; https://kiro.dev/faq/

3. Stated audience: developers and teams ("helps developers and teams do their best work"); startups ("Built for startups", startup credits); enterprises ("Enterprise-ready", team plans); students/learners (one-year students post). https://kiro.dev/ ; https://kiro.dev/blog/general-availability/ ; https://kiro.dev/blog/one-year/

4. Positioning against others: no competitor named. Allusions: "Most tools are great at generating code, but Kiro gives structure to the chaos" (homepage); launch post contrasts with "vibe coding"; powers README says "No more MCP context overload"; Q2 earnings line "up to 50% more cost-effective than alternatives" (aboutamazon). https://kiro.dev/ ; https://kiro.dev/blog/introducing-kiro/ ; https://github.com/kirodotdev/powers ; https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report

5. Evidence the maker offers:
   - 100,000+ developers tried the IDE in the first 5 days of preview, more than doubled by October 2025; 250,000+ developers by GA (2025-11). https://kiro.dev/blog/one-year/ ; https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025
   - Developers more than doubled quarter-over-quarter and enterprise usage up nearly tenfold (Q1 2026); usage tripled QoQ (Q2 2026). https://www.aboutamazon.com/news/company-news/amazon-earnings-q1-2026-report ; https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report
   - 15,000+ community-created powers, 100+ partner powers, 1,000+ Ambassadors; customer anecdotes: Loyola Marymount University (500 Lambda updates from 2 months to half a day), Siemens (2 weeks vs 3-4 months), SmugMug, Flickr, Appian. https://kiro.dev/blog/one-year/
   - Homepage practitioner testimonials (named individuals with titles, no company logos block) and a 76-entry powers marketplace with verified partners (AWS, Stripe, Supabase, Datadog, Figma, Snyk, Terraform). https://kiro.dev/ ; https://kiro.dev/powers/
   - No benchmark scores offered on the homepage, README, docs or launch/GA posts.

6. Notable silences: no benchmark placements (SWE-bench, Terminal-Bench); no open-source claim for IDE/CLI (only Crew is open-source); no BYO-key/BYO-model option; no OS-level sandboxing for IDE/CLI (only a web "Sandbox" mention); no SDK; no absolute user count since Nov 2025 (growth multiples only); no reading of CLAUDE.md/.cursorrules or other tools' instruction files (AGENTS.md only); no statement on which language/runtime the agent harness is written in.

7. Confidence: high — materials are extensive and consistent (homepage, README, docs for every feature, dated launch/GA/anniversary posts with numbers, pricing page, Amazon earnings releases); the main ambiguity is the split between surfaces (some features IDE-only, CLI 3.0 still opt-in), not the positioning itself.

Sources:
- https://kiro.dev/
- https://github.com/kirodotdev/Kiro (README)
- https://github.com/kirodotdev/powers (description)
- https://kiro.dev/docs/
- https://kiro.dev/docs/cli/
- https://kiro.dev/docs/cli/acp/
- https://kiro.dev/docs/cli/headless/
- https://kiro.dev/docs/cli/v3/
- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/steering/
- https://kiro.dev/docs/hooks/
- https://kiro.dev/docs/mcp/
- https://kiro.dev/docs/powers/
- https://kiro.dev/docs/skills/
- https://kiro.dev/docs/custom-agents/ and /subagents/
- https://kiro.dev/docs/permissions/
- https://kiro.dev/docs/models/
- https://kiro.dev/docs/how-kiro-works/
- https://kiro.dev/docs/crew/
- https://kiro.dev/docs/enterprise/concepts/
- https://kiro.dev/pricing/
- https://kiro.dev/faq/
- https://kiro.dev/powers/
- https://kiro.dev/blog/introducing-kiro/
- https://kiro.dev/blog/general-availability/
- https://kiro.dev/blog/one-year/
- https://kiro.dev/blog/cli-2-0/
- https://kiro.dev/blog/kiro-adopts-acp/
- https://kiro.dev/blog/one-agent/
- https://kiro.dev/blog/powers-supports-plugins/
- https://aws.amazon.com/blogs/aws/aws-weekly-roundup-how-to-join-aws-reinvent-2025-plus-kiro-ga-and-lots-of-launches-nov-24-2025
- https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/
- https://www.aboutamazon.com/news/company-news/amazon-earnings-q1-2026-report
- https://www.aboutamazon.com/news/company-news/amazon-earnings-q2-2026-report
