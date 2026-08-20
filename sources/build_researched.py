#!/usr/bin/env python3
# Builds /Users/jesse/agent-survey/sources/toolify_researched.jsonl
import json

# (name, slug, url, github_repo, maker, is_harness, reason_if_not_harness)
rows = [
("AI expert for codebases","storia-ai","https://storia.ai",None,"Storia AI",True,""),
("No Fate AI","no-fate-ai","https://nofateai.com",None,"No Fate AI",True,""),  # site not resolving at research time
("SamaritanAI","samaritanai","https://www.samaritanai.xyz",None,"SamaritanAI",False,"Codebase visualization (network graphs), not a coding agent/IDE/harness"),
("MicroByte","microbyte","https://microbyte.app",None,"MicroByte",False,"Code completion/insertion suggestions, not an autonomous coding agent/IDE/harness"),  # site not resolving
("McAnswers","mcanswers","https://oxad.ai/mcanswers",None,"OXAD (McAnswers)",False,"AI code debugging utility, not an autonomous coding agent/IDE/harness"),
("Zevo.ai","zevo-ai","https://zevo.ai",None,"Zevo.ai",False,"Codebase understanding via code maps, not a coding agent/IDE/harness"),  # site not resolving
("Onboard","onboard","https://www.onboard-developer.com",None,"OnBoardAI",False,"Developer onboarding / codebase navigation tool, not a coding agent/IDE/harness"),
("PointDrift","pointdrift","https://pointdrift.com",None,"PointDrift",False,"Mindmap-to-code conversion utility, not an autonomous coding agent/IDE/harness"),
("Lobby Code","lobby-code","https://code.lobby.so",None,"Lobby Code",False,"Rapid code-generation assistant, not an autonomous coding agent/IDE/harness"),  # site not resolving
("GitterBot.io","gitterbot-io","https://www.gitterbot.io",None,"GitterBot",False,"AI conversational documentation for SaaS, not a coding agent/IDE/harness"),
("mutable.ai","mutable-ai","https://mutable.ai",None,"MutableAI",True,""),  # site not resolving at research time
("crystl","crystl","https://crystl.dev",None,"crystl",True,""),
("Relace","relace","https://www.relace.ai",None,"Relace",False,"Inference models & source-control infrastructure for coding agents, not an agent/IDE/harness itself"),
("Exponent","exponent","https://www.exponent.run",None,"Exponent",True,""),  # site 404 at research time
("Superlog","superlog","https://superlog.sh","superloglabs/superlog","Pulsent Labs Inc.",True,""),
("CodePal","codepal","https://codepal.ai",None,"CodePal",False,"Suite of code-generation tools, not an autonomous coding agent/IDE/harness"),
("Refraction","refraction","https://www.refraction.dev",None,"Twistag",False,"Paste-and-generate code utility, not an autonomous coding agent/IDE/harness"),
("ProMind AI","promind-ai","https://promind.ai",None,"ProMind AI",False,"General multi-agent platform (content + coding), not a coding agent/IDE/harness"),
("ADE","ade","https://ade-app.dev","arul28/ADE","ADE (Arul Sharma)",True,""),
("Programming Helper","programming-helper","https://www.programming-helper.com",None,"Programming Helper",False,"Code-generation utility, not an autonomous coding agent/IDE/harness"),
("EarlyAI","earlyai","https://www.startearly.ai",None,"Early AI",False,"Regression testing / release-readiness platform, not a coding agent/IDE/harness"),
("VibeKit","vibekit","https://www.vibekit.sh","superagent-ai/vibekit","Superagent AI",True,""),
("What The Diff","what-the-diff","https://whatthediff.ai",None,"What The Diff",False,"AI code review assistant, not a coding agent/IDE/harness"),
("Line0","line0","https://www.line0.dev",None,"Line0",True,""),  # site 500 at research time
("Crew44","crew44","https://crew44.io",None,"Crew44",True,""),
("KodHau MCP","kodhau-mcp","https://www.kodhau.com",None,"KodHau",False,"Governance/rules layer for AI coding agents, not an agent/IDE/harness itself"),
("PlusB","plusb","https://www.plusb.in",None,"PlusB",True,""),
("Git Pitcher","git-pitcher","https://gitpitcher.com",None,"Git Pitcher",False,"Converts repos into agent-ready build plans, not a coding agent/IDE/harness itself"),
("PUNK","punk","https://punkcode.rocks",None,"PUNK",True,""),
("Tonkotsu","tonkotsu","https://tonkotsu.ai",None,"Tonkotsu",True,""),  # site 503 at research time
("Nora","nora","https://www.mynora.ai",None,"Nora",True,""),
("Snapmark","snapmark","https://snapmark.app",None,"Snapmark",False,"Visual UI development / code-generation tool, not an autonomous coding agent/IDE/harness"),  # site 526
("VibeScan","vibescan","https://vibescan.io",None,"VibeScan",False,"Scanning/QA tool for AI-generated code, not a coding agent/IDE/harness (service ending)"),
("Better AI Code","better-ai-code","https://betteraicode.com",None,"Better AI Code",False,"Tool to generate/improve AI coding prompts, not a coding agent/IDE/harness"),  # site not resolving
("Devgen","devgen","https://devgen.xyz",None,"Devgen",False,"Codebase research assistant, not a coding agent/IDE/harness"),
("FirstMate","firstmate","https://www.firstmate.io",None,"FirstMate",False,"Automated code review / pipeline debugging, not a coding agent/IDE/harness"),  # site not resolving
("Scriptio AI","scriptio-ai",None,None,"Scriptio AI",False,"toolify-listed URL (scriptio.org) is an unrelated Bible site; real site not found"),
("Folderer","folderer","https://folderer.com",None,"Folderer",False,"GitHub-integrated code-generation tool, not an autonomous coding agent/IDE/harness"),
("JACoB","jacob","https://jacb.ai","Renaissance-Innovation-Labs/jacob-ai","Renaissance Innovation Labs (Pioneer Square Labs)",True,""),  # site not resolving; repo is authoritative
("JetCode","jetcode","https://www.jetcode.app",None,"JetCode",False,"Turns requirements into coding guides, not a coding agent/IDE/harness"),  # site not resolving
("CodeDefender α","codedefender-a","https://codedefender.ro",None,"CodeDefender",False,"AI developer sidekick (site not resolving); not confirmed as an autonomous coding agent/IDE/harness"),
("Astronuts","astronuts","https://www.astronuts.io",None,"Astronuts",False,"Listed SE co-pilot; astronuts.io now repurposed (sports streaming), product not confirmed"),
("CodeWhizz","codewhizz","https://www.codewhizz.dev",None,"CodeWhizz",False,"Educational Python code generator/debugger/tutor, not a coding agent/IDE/harness"),  # site 404
("Mimrr","mimrr","https://www.mimrr.com",None,"Mimrr",False,"AI code documentation solution, not a coding agent/IDE/harness"),  # site 404
("JIT.codes","jit-codes","https://jit.codes",None,"JIT.codes",False,"AI code playground, not an autonomous coding agent/IDE/harness"),
("AutoGPT on Mobile","autogpt-on-mobile","https://autogptmobile.com",None,"AutoGPT Mobile",False,"General autonomous agent (AutoGPT) ported to mobile, not a coding agent/IDE/harness"),  # site not resolving
("Cosine AI","cosine-ai","https://cosine.sh",None,"Cosine",True,""),
("Kane AI","kane-ai","https://www.testmuai.com/kane-ai",None,"LambdaTest (TestMu AI)",True,""),
("T3 Code","t3-code","https://t3.codes","pingdotgg/t3code","T3 Tools (Ping)",True,""),
("Coworker AI","coworker-ai","https://coworker.ai",None,"Coworker AI",False,"General enterprise AI agent platform, not a coding agent/IDE/harness"),
("Pineify","pineify","https://pineify.app",None,"Pineify",True,""),
("RoxyBrowser","roxybrowser","https://roxybrowser.com",None,"RoxyBrowser",False,"Anti-detect browser for multi-accounting, not a coding agent/IDE/harness"),
("Paird.ai","paird-ai","https://paird.ai",None,"Paird.ai",False,"Rapid code-generation / pair-programming platform, not an autonomous coding agent/IDE/harness"),
("PAS Code","pas-code","https://pascode.io",None,"PAS Code",False,"Listed online AI code editor; pascode.io now repurposed (betting), product not confirmed"),
("CodeCopilot AI","codecopilot-ai","https://codecopilotai.com",None,"CodeCopilot AI",False,"In-browser AI code generator, not an autonomous coding agent/IDE/harness"),
("Clacky","clacky","https://clacky.ai",None,"Clacky",True,""),
("Squire AI","squire-ai","https://www.squire.ai",None,"Squire AI",False,"AI code review tool, not a coding agent/IDE/harness"),
("FlowLens","flowlens","https://magentic.ai/flowlens",None,"Magentic AI",False,"Automated bug reporting for AI coding agents, not an agent/IDE/harness itself"),
("Matter AI","matter-ai","https://matterai.so","MatterAIOrg/matter-ai","Matter AI (Gravity Cloud AI)",False,"Open-source AI code-reviewer agent (repo archived); reviews code, not a coding agent/IDE/harness"),
("Codey","codey","https://www.codeyai.space",None,"Codey",True,""),
("Mantlecore AI","mantlecore-ai","https://mantlecore.ai",None,"Mantlecore",True,""),
("MyClawn","myclawn","https://myclawn.com",None,"MyClawn",False,"General AI agent with its own computer, not specifically a coding agent/IDE/harness"),
("Forums by BaseHub","forums-by-basehub","https://forums.basehub.com","basehub-ai/forums","BaseHub",False,"Forums/Q&A product where AI explores source code, not a coding agent/IDE/harness"),
("CopilotHub","copilothub","https://copilothub.directory","eddybenchek/copilothub","CopilotHub",False,"Curated directory of AI prompts/agents/tools, not a coding agent/IDE/harness"),
("CLI Manager","cli-manager","https://www.solhun.com",None,"Solhun",True,""),
("Devle","devle","https://devle.ai",None,"Devle",True,""),
("Code2.AI","code2-ai","https://code2.ai",None,"Code2.AI",False,"Transforms codebases into AI-ready knowledge, not a coding agent/IDE/harness"),  # site not resolving
("Archittect","archittect","https://www.archittect.com",None,"Archittect",False,"Dynamic code-template generator, not an autonomous coding agent/IDE/harness"),
("Scape","scape","https://www.scape.work",None,"Scape",True,""),
("Ovren","ovren","https://www.ovren.ai",None,"Ovren",True,""),
("DigestDiff","digestdiff","https://www.digestdiff.com",None,"DigestDiff",False,"AI commit-history analysis, not a coding agent/IDE/harness"),  # site down
("TryCase","trycase","https://trycase.dev",None,"TryCase",True,""),
("Viktor","viktor","https://viktor.com",None,"Viktor",False,"General autonomous AI coworker for Slack, not a coding agent/IDE/harness"),
("DiffDuo","diffduo","https://diffduo.com",None,"DiffDuo",False,"GPT-powered pull-request summaries, not a coding agent/IDE/harness"),  # site down
("Genval AI","genval-ai","https://genval.ai",None,"Genval",False,"Code generation/refactoring platform, not an autonomous coding agent/IDE/harness"),
("CrewArgo","crewargo","https://www.crewargo.com",None,"Crewargo",True,""),
("ERNIE Comate","ernie-comate","https://comate.baidu.com",None,"Baidu",False,"AI code-completion assistant (IDE plugin), not an autonomous coding agent/harness"),
("Code Arena","code-arena","https://www.arena.ai/code",None,"Arena AI",False,"Benchmark/eval platform for AI coding models, not a coding agent/IDE/harness"),
("Google Antigravity","google-antigravity","https://antigravity.google",None,"Google",True,""),
("BLACKBOX.AI","blackbox-ai-1","https://www.blackbox.ai",None,"BLACKBOX.AI",True,""),
("cto.new","cto-new","https://cto.new",None,"cto.new",True,""),
("Morph","morph","https://www.morphllm.com",None,"Morph (Morph LLM)",False,"Inference infrastructure built for coding agents, not an agent/IDE/harness itself"),
("Palmier","palmier","https://www.palmier.me",None,"Palmier",True,""),
("Workik AI","workik-ai","https://workik.com",None,"Workik",False,"AI-powered development platform (code generation), not an autonomous coding agent/IDE/harness"),
("PseudoEditor","pseudoeditor","https://pseudoeditor.com",None,"PseudoEditor",False,"Online pseudocode editor with AI, not a coding agent/IDE/harness"),
("Macroscope","macroscope","https://macroscope.com",None,"Macroscope",False,"AI code review / status-update agent, not a coding agent/IDE/harness"),
("Ara AI","ara-ai","https://ara.so",None,"Ara",True,""),
("PearAI","pearai","https://trypear.ai","trypear/pearai-app","TryPear (PearAI)",True,""),
("Digma AI","digma-ai","https://digma.ai",None,"Digma (now JetBrains)",False,"Continuous feedback / observability for developers, not a coding agent/IDE/harness"),
("Replicas","replicas","https://tryreplicas.com",None,"Replicas",True,""),
("Contral","contral","https://contral.ai",None,"Contral",True,""),  # site 402 at research time
("Agent FM","agent-fm","https://www.agentfm.ai",None,"Agent FM",False,"Now a general AI-teammates product (pivoted from audio narration); no public source repo despite 'open-source' claim"),
("Dynobase","dynobase","https://dynobase.dev",None,"Dynobase",False,"DynamoDB GUI client with code generation, not a coding agent/IDE/harness"),
("Adrenaline","adrenaline","https://useadrenaline.com",None,"Adrenaline",False,"Codebase Q&A / code analysis, not an autonomous coding agent/IDE/harness"),
("Straion","straion","https://www.straion.com",None,"Straion",False,"Centralized rule management for AI coding agents, not an agent/IDE/harness itself"),
("GiteAI","giteai","https://giteai.dev",None,"GiteAI",False,"Automates commit-message generation, not a coding agent/IDE/harness"),
("AICommit","aicommit","https://aicommit.app","AICommitApp/community","AICommitApp",False,"JetBrains plugin for AI commit-message generation, not a coding agent/IDE/harness"),
("Code Fundi","code-fundi","https://codefundi.app",None,"Code Fundi",False,"AI coding assistant, not an autonomous coding agent/IDE/harness"),
("Athena by LuckeySystems","athena-by-luckeysystems","https://github.com/luckeyfaraday/Athena","luckeyfaraday/Athena","LuckeySystems",True,""),
("VibeWorkspace","vibeworkspace","https://www.vibe-workspace.cloud",None,"VibeWorkspace",True,""),
("Pincue","pincue","https://www.getpincue.com",None,"Pincue",False,"Review-session tool for AI-assisted builders, not a coding agent/IDE/harness"),
("Sonarly","sonarly","https://sonarly.com",None,"Sonarly",True,""),
("devstral2","devstral2","https://mistral.ai/news/devstral-2-vibe-cli/",None,"Mistral AI",True,""),  # toolify URL devstral2.com dead; real site is Mistral
("kat dev","kat-dev","https://kat-dev.dev",None,"Kuaishou (Kwaipilot)",False,"AI-driven code-intelligence models, not a coding agent/IDE/harness"),  # site region-blocked (451)
("CodeNext.ai","codenext-ai","https://codenext.ai",None,"CodeNext",True,""),
]

out_path="/Users/jesse/agent-survey/sources/toolify_researched.jsonl"
with open(out_path,"w") as f:
    for (name,slug,url,gh,maker,h,r) in rows:
        f.write(json.dumps({
            "name":name,
            "url":url,
            "github_repo":gh,
            "maker":maker,
            "is_harness":h,
            "reason":r,
        },ensure_ascii=False)+"\n")
print("wrote",len(rows),"rows to",out_path)
