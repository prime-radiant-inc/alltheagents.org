---
name: "guidance-for-multi-agent-orchestration-on-aws"
slug: "guidance-for-multi-agent-orchestration-on-aws"
layout: "agent.njk"
category: "agent"
maker: "aws-solutions-library-samples"
license: "Apache-2.0"
url: "https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws"
source_code_url: "https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-on-aws"
source_available: True
platforms: []
first_released: "2025-03-23"
current_release: "2026-01-08"
stars: "71"
language: "TypeScript"
homepage: "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html"
mcp_support: False
plugin_support: False
claude_code_plugin: False
subagents: True
hooks: False
plan_mode: False
model_providers: "Amazon Bedrock (Anthropic Claude, Amazon Nova, Cohere)"
pricing: "Estimated ~$606-$761/month for 100,000 requests in us-west-2 (AWS service costs)"
install_method: "git clone, npm i, cdk bootstrap, authenticate to ECR, configure project-config.json, npm run develop"
docs_url: "https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html"
plugin_docs_url: null
config_docs_url: null
download_url: null
maintained: "active"
sources:
  - "agent_infra"
what_makes_it_special: "Reference implementation for multi-agent collaboration on Amazon Bedrock using a Supervisor Agent as central orchestrator routing queries to specialized sub-agents (Order Management, Product Recommendation, Troubleshooting, Personalization), each with its own knowledge base and action groups (text-2-SQL via Athena, vector search on S3)."
---

Reference implementation for multi-agent collaboration on Amazon Bedrock using a Supervisor Agent as central orchestrator routing queries to specialized sub-agents (Order Management, Product Recommendation, Troubleshooting, Personalization), each with its own knowledge base and action groups (text-2-SQL via Athena, vector search on S3).
