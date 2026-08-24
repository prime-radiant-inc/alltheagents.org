# Standardized differentiation extraction: siGit Code (census_slug: sigit)

Run 2026-08-24 against official materials only (README, sigit.si homepage, crates.io metadata, Zed ACP listing text authored by the maker).

1. **One-sentence self-description:** A local coding agent that runs entirely on the user's machine with on-device LLM inference, integrating with editors via the Agent Client Protocol and with the maker's siGit/smbCloud git-hosting ecosystem.

2. **Claimed differentiators:**
   - Runs locally with no API keys, cloud round-trips, or subscription — privacy/cost by construction (kind: trust-safety + price). Source: https://github.com/getsigit/sigit README.
   - On-device inference of open-weights models (Qwen 2.5/3, GGUF from Hugging Face) (kind: model). Source: repo description + README, https://github.com/getsigit/sigit.
   - ACP-native editor integration — Zed, Xcode (`--acp`), VS Code — through one protocol (kind: integration). Source: README + https://zed.dev/acp/agent/sigit.
   - Enhanced capability on the maker's smbCloud repos: pre-understands Rust workspace layouts, deployment flows, auth boundaries (kind: integration/workflow). Source: README.
   - MCP client for external tooling (e.g. Xcode's mcpbridge) (kind: integration). Source: README.

3. **Stated audience:** developers wanting local/private AI coding; implicitly Rust developers and users of the maker's smbCloud/siGit hosting ("Git hosting for the AI era", "Agent-ready"). Sources: README; https://sigit.si.

4. **Positioning against others:** alludes to cloud-hosted agents as the category it is not — "runs on your machine, not someone else's"; "No API keys, no cloud round-trips, no subscription" (README). No competitor named.

5. **Evidence offered for claims:** none offered — no benchmarks, numbers, or customer names in any consulted material.

6. **Notable silences:** no mention of plan mode, subagents, hooks, skills/plugins, CLAUDE.md/Claude Code compatibility, sandboxing or permission model, multi-model/cloud-provider support, enterprise controls, benchmarks, or team/company details.

7. **Confidence:** medium — materials are sparse (short README, marketing-light homepage, directory listing); sections 1-2 likely reflect real positioning (the local-first claim is consistent everywhere), but the thin docs leave the workflow story underspecified.

Sources: https://github.com/getsigit/sigit (README); https://sigit.si; https://crates.io/crates/sigit (description); https://zed.dev/acp/agent/sigit
