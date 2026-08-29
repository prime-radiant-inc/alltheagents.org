---
name: "remote-swe-agents"
slug: "remote-swe-agents"
layout: "agent.njk"
category: "agent"
maker: "aws-samples"
license: "MIT-0"
url: "https://github.com/aws-samples/remote-swe-agents"
source_code_url: "https://github.com/aws-samples/remote-swe-agents"
source_available: "True"
platforms:
  - "Web"
  - "Autonomous"
first_released: "2025-04-01"
current_release: "2026-08-04"
stars: "241"
language: "TypeScript"
homepage: "https://github.com/aws-samples/remote-swe-agents"
mcp_support: "True"
plugin_support: "False"
claude_code_plugin: "False"
subagents: "False"
hooks: "False"
plan_mode: "False"
model_providers: "AWS Bedrock"
pricing: "~$115/month for 100 sessions (us-east-1); ~$0 when idle; pay-as-you-go"
install_method: "git clone + cd cdk + npm ci + npx cdk bootstrap + npx cdk deploy --all; or one-click AWS Sample deployment"
docs_url: "https://github.com/aws-samples/remote-swe-agents"
plugin_docs_url: null
config_docs_url: null
download_url: "https://github.com/aws-samples/remote-swe-agents.git"
maintained: "active"
sources:
  - "github_topic2"
what_makes_it_special: "Self-hosted, fully open-source autonomous SWE agent on AWS serverless infrastructure — offers a Devin/OpenAI Codex/Google Jules-like experience with no upfront or fixed costs (~$0 when idle). Features web UI, Slack bot, REST API, GitHub Actions integration, per-session isolated EC2 worker VMs, MCP client support, and pay-as-you-go pricing."
---

The project exists for teams that want the cloud-agent workflow — delegate a task, get a pull request — without sending code to a hosted service or paying for idle capacity. Messages arrive through Slack or a REST API, flow via AppSync Events into DynamoDB, and a Worker Manager boots an isolated EC2 instance per session that clones the target repository, works with Bedrock models, and pushes branches or pull requests. MCP servers configured through mcp.json extend the agent's tools, and a Next.js dashboard adds session monitoring, cost analytics, and API-key management. Security is treated as a first-class concern: single-tenant deployments, least-privilege IAM with optional egress filtering, and Cognito-gated access. It fits AWS-centric teams and OSS maintainers who need cheap, isolated background agents.
