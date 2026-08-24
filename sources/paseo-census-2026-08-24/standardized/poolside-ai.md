# Standardized differentiation extraction: Poolside (pool CLI) (census_slug: poolside-ai)

Run 2026-08-21 against the maker's own materials only (listed under Sources).

1. One-sentence self-description: pool is Poolside's coding agent that runs in the terminal (interactive or one-shot) or inside any ACP-compatible editor, reads and edits code, runs commands, and uses MCP servers and skills, built as the companion harness for Poolside's open-weight Laguna coding models. (README; docs CLI overview; Laguna launch posts)

2. Claimed differentiators (by prominence):
   - Open-weight models you can run anywhere: Laguna S 2.1 (118B/8B active, 1M context) and XS 2.1 (33B/3B active, on-device), "frontier-class reasoning at mid-size cost", weights on Hugging Face, free to use for a limited time. Kind: model / openness / price. https://poolside.ai ; https://poolside.ai/models ; https://poolside.ai/blog/introducing-laguna-s-2-1
   - Built on open agent specs and ACP in both directions: implements AGENTS.md, Agent Skills, MCP, and ACP; runs as an ACP server in Zed/JetBrains/Xcode and as an ACP client that can drive other agents (Claude Agent, Codex), including remote ACP over HTTP. Kind: integration / openness. https://github.com/poolsideai/pool ; https://docs.poolside.ai/cli/pool
   - The same harness Poolside uses internally for agent RL training and evaluation, offered as the best way to work with Laguna; released as a research preview. Kind: capability / trust. https://poolside.ai/blog/introducing-laguna-xs2-m1
   - Model freedom: Poolside Platform (free developer access), self-managed Poolside deployment, OpenRouter natively, Ollama, or any OpenAI-compatible endpoint. Kind: model / integration. https://docs.poolside.ai/cli/install ; https://github.com/poolsideai/pool
   - Control over autonomy: Always-ask default, Accept-edits, classifier-based Auto, Allow-all; Plan mode whose return to Build is always user-reviewed; Docker sandbox; allow/deny tool and path rules; hooks at six lifecycle events; subagents. Kind: trust-safety / workflow. https://docs.poolside.ai/permissions ; https://docs.poolside.ai/hooks ; https://docs.poolside.ai/subagents

3. Stated audience: developers ("Build with our open-weight agentic coding models"; free developer access via `pool login`), and at the company level organizations that must "run AI inside environments they control" — enterprises in regulated industries and public sector/defense (on-prem, air-gapped, IL5). https://poolside.ai ; https://docs.poolside.ai/get-started/overview ; https://poolside.ai/government ; https://poolside.ai/blog/introducing-the-poolside-platform

4. Positioning against others: the CLI materials name Claude Agent and Codex only as agents pool can drive over ACP (not as rivals); the Laguna S 2.1 post benchmarks against named models (Kimi K3, Claude Fable 5, Qwen 3.7 Max, Hy3, DeepSeek) and claims to match or beat open models "several times its size"; company pages contrast open weights / no per-token fees with API-only access. https://github.com/poolsideai/pool ; https://poolside.ai/blog/introducing-laguna-s-2-1 ; https://poolside.ai/government

5. Evidence the maker offers:
   - Benchmarks for Laguna S 2.1 (2026-07-21): Terminal-Bench 2.1 70.2%, SWE-Bench Multilingual 78.5%, SWE-Bench Pro 59.4%, DeepSWE v1.1 40.4%, SWE Atlas 46.2%, Toolathlon Verified 49.7%. https://poolside.ai/blog/introducing-laguna-s-2-1
   - Benchmarks for Laguna M.1 / XS.2 (2026-04-28): SWE-Bench Verified 72.5% / 68.2%, SWE-Bench Pro 46.9% / 44.5%. https://poolside.ai/blog/introducing-laguna-xs2-m1
   - Training facts: S 2.1 trained in ~9 weeks (May 22 to Jul 21, 2026); ~60-person Applied Research team. https://poolside.ai/blog/introducing-laguna-s-2-1 ; https://poolside.ai/blog/introducing-laguna-xs2-m1
   - Customer/partner names and quotes (government page): Vibrint, Northrop Grumman, Cubic, Sterling Computers, Dell, Hunted Labs, Atos, IQT; IL5 deployable, ATO achieved. https://poolside.ai/government
   - Partnerships: AWS first-party (2024-12-04), Dell (2026-05-28), Redpanda (2025-10-28); $500M raise (2024-10-02). https://poolside.ai/blog
   - No usage, user, or revenue numbers for the pool CLI itself.

6. Notable silences: no plugin/marketplace system (skills and MCP only); no Claude Code / CLAUDE.md compatibility mention; no SDK for the agent; no IDE-native extension for pool beyond ACP and the separate Poolside Assistant extensions; no stated usage or adoption numbers for the CLI; no enterprise admin/policy controls documented for the CLI (enterprise controls live in the self-managed platform); no pricing for the CLI beyond "free for a limited time"; no multi-agent "teams" or cloud/background execution; no explicit statement of whether "research preview" still applies; no named head of product or DevRel.

7. Confidence: medium — the CLI materials (README, docs) are detailed and consistent, but the positioning is mostly carried by model and company posts rather than a CLI launch post, and the company's emphasis (open weights, government, self-managed platform) sits alongside rather than on top of the harness itself.

Sources:
- https://github.com/poolsideai/pool (README)
- https://docs.poolside.ai/cli/pool
- https://docs.poolside.ai/cli/install
- https://docs.poolside.ai/get-started/overview
- https://docs.poolside.ai/permissions
- https://docs.poolside.ai/hooks
- https://docs.poolside.ai/subagents
- https://docs.poolside.ai/skills
- https://docs.poolside.ai/mcp-servers
- https://poolside.ai
- https://poolside.ai/models
- https://poolside.ai/get-started
- https://poolside.ai/government
- https://poolside.ai/blog
- https://poolside.ai/blog/introducing-laguna-xs2-m1
- https://poolside.ai/blog/introducing-laguna-s-2-1
- https://poolside.ai/blog/introducing-the-poolside-platform
- https://poolside.ai/blog/introducing-poolside-desktop-assistant
