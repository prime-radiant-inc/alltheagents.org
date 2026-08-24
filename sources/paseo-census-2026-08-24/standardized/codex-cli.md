# Standardized differentiation extraction — Codex CLI (OpenAI)

census_slug: codex-cli | run 2026-08-21 | prompt: STANDARD_PROMPT.md v1
Inputs: official materials only (repo README, docs at learn.chatgpt.com — the redirect target of
developers.openai.com/codex — and the OpenAI Forum event page). OpenAI launch posts and marketing
pages on openai.com / chatgpt.com / help.openai.com returned HTTP 403 and were NOT used.

1. One-sentence self-description:
   A coding agent from OpenAI that runs locally on your computer (terminal, IDE, desktop app) and
   also in the cloud, to inspect, edit and run code and automate work, using your ChatGPT plan or an
   API key. (README; https://learn.chatgpt.com/docs/codex/cli; https://learn.chatgpt.com/docs/quickstart)

2. Claimed differentiators (most prominent first):
   - Runs locally on your machine, open source (Apache-2.0), one-line install, with the same agent
     available as CLI, IDE extension, Codex cloud and ChatGPT desktop/web — capability / openness —
     https://github.com/openai/codex ; https://learn.chatgpt.com/docs/quickstart
   - Sign in with your existing ChatGPT plan (every tier incl. Free and Go; Plus/Pro/Business/Edu/
     Enterprise per README) instead of paying per token; API key optional — price —
     https://github.com/openai/codex ; https://learn.chatgpt.com/docs/pricing
   - Safety by default: OS-level sandbox (macOS Seatbelt, Linux bwrap+seccomp, Windows sandbox/WSL2),
     network off by default, graduated approval policies and permission profiles, Auto mode for
     version-controlled folders — trust-safety — https://learn.chatgpt.com/docs/agent-approvals-security
   - Extensible: skills on the open Agent Skills standard, plugins shared with ChatGPT's universal
     plugin directory, MCP client, lifecycle hooks, AGENTS.md — integration —
     https://learn.chatgpt.com/docs/build-skills ; https://learn.chatgpt.com/docs/plugins ;
     https://learn.chatgpt.com/docs/extend/mcp?surface=cli ; https://learn.chatgpt.com/docs/hooks
   - Built-in multi-agent orchestration (subagents, custom agent roles, `codex agents` dashboard)
     and embeddability via app-server JSON-RPC, TypeScript/Python SDKs, GitHub Action — capability /
     workflow — https://learn.chatgpt.com/docs/agent-configuration/subagents ;
     https://learn.chatgpt.com/docs/codex-sdk ; https://github.com/openai/codex/releases/latest

3. Stated audience:
   Developers/engineers needing "codebase context and developer tools" (Codex mode, quickstart); users
   on ChatGPT Plus/Pro/Business/Edu/Enterprise (README); enterprise admins via requirements.toml /
   managed config (https://learn.chatgpt.com/docs/hooks, repo docs/config.md); and, per the OpenAI
   Forum event page, "everyone who does work on a computer" — leaders, researchers, educators,
   small-business owners (https://forum.openai.com/public/events/codex-is-for-everyone-why-codex-matters-beyond-code-fa40puy7wi).
   Team size / language-stack: not claimed.

4. Positioning against others:
   not claimed — no competitor is named in the README or docs reached. Indirect: the docs/config
   reference and release notes describe importing/migrating settings, plugins and sessions from
   "Claude Code" and "Cursor" (`/import`, release 0.145.0 notes, https://github.com/openai/codex/releases),
   which implicitly positions Codex as a switch-to target; the Forum page frames Codex as "beyond
   code", i.e. not only a developer tool.

5. Evidence the maker offers for its claims:
   Within the official materials used: none offered — no benchmarks, customer names or usage numbers
   appear in the README, docs or Forum page. (The OpenAI launch/customer posts that do carry such
   evidence were unreachable, 403, and are excluded per the prompt's rules.)

6. Notable silences (in the materials used):
   - No competitor comparison or benchmark numbers.
   - No statement of model-vendor neutrality in prose; third-party providers (Azure, Bedrock,
     Ollama/OSS, OpenAI-compatible) appear only in the config reference and changelog.
   - No Agent Client Protocol (ACP) support or mention.
   - No explicit Claude Code plugin compatibility statement in docs (only in source/release notes).
   - README omits Free/Go plans, MCP, sandboxing and plugins; those live only in the docs.
   - Plan mode exists (/plan) but is not positioned as a differentiator.
   - Open-source scope is not delineated (what is open vs. cloud/IDE/app binaries).
   - Data handling / zero-data-retention and enterprise security pages were not reachable (404 on
     /docs/enterprise), so enterprise controls are thinly documented in the reached set.

7. Confidence: medium — docs are rich and current (August 2026 changelog) and the README is
   authoritative for the CLI, but the maker's primary positioning posts (openai.com launch,
   GA, enterprise and knowledge-work posts) were 403 and excluded, and the docs site is now
   ChatGPT-branded, so Codex-specific marketing claims may be under-represented.

Sources:
- https://github.com/openai/codex (README, 2026-08-21)
- https://raw.githubusercontent.com/openai/codex/main/README.md
- https://learn.chatgpt.com/docs (redirect target of https://developers.openai.com/codex)
- https://learn.chatgpt.com/docs/quickstart
- https://learn.chatgpt.com/docs/codex/cli
- https://learn.chatgpt.com/docs/codex/ide
- https://learn.chatgpt.com/docs/developer-commands?surface=cli
- https://learn.chatgpt.com/docs/pricing
- https://learn.chatgpt.com/docs/agent-approvals-security
- https://learn.chatgpt.com/docs/extend/mcp?surface=cli
- https://learn.chatgpt.com/docs/plugins
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/hooks
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/config-file/config-reference
- https://learn.chatgpt.com/docs/codex-sdk
- https://learn.chatgpt.com/docs/app-server
- https://learn.chatgpt.com/docs/changelog
- https://github.com/openai/codex/releases (0.145.0, 0.146.0, 0.149.0 notes)
- https://github.com/openai/codex/blob/main/docs/config.md
- https://forum.openai.com/public/events/codex-is-for-everyone-why-codex-matters-beyond-code-fa40puy7wi
- Unreachable (HTTP 403, not used): https://openai.com/index/introducing-codex/ ;
  https://openai.com/index/introducing-the-codex-app/ ; https://openai.com/index/codex-now-generally-available/ ;
  https://openai.com/index/scaling-codex-to-enterprises-worldwide/ ; https://openai.com/index/codex-for-knowledge-work/ ;
  https://openai.com/codex/ ; https://chatgpt.com/codex ; https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
