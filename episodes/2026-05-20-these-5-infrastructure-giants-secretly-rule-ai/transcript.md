---
title: "These 5 Infrastructure Giants Secretly Rule AI"
video_id: "woGB2vr5wTg"
youtube_url: "https://www.youtube.com/watch?v=woGB2vr5wTg"
publish_date: "2026-05-20"
duration: "20:20"
duration_seconds: 1220
view_count: 13844
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Full Post w/ Prompt Pack: https://natesnewsletter.substack.com/p/agent-infrastructure-control-layer?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  __________________________________
  What's really happening with AI agent infrastructure?
  The common story is that OpenAI and Anthropic decide whether agents ship. The reality is more complicated.
  
  In this video, I share the inside scoop on the control layer that actually determines whether your AI agent reaches production:
  
   • Why runtime, not the model, decides where agents live
   • How identity providers handle delegated authority for AI agents
   • What governed data means for LLMs and RAG pipelines
   • Where payments, observability, and kill switches actually sit
  
  For operators and builders, the opportunity is real, but the rollout risk is just as real if no one owns these control points.
  
  Chapters:
  00:00 The companies that actually decide if your agent ships
  01:20 Compute matters but compute isn't the whole story
  02:40 The agent layer underneath the protocols
  03:30 Runtime as a control point: Cloudflare, AWS, Vercel
  05:40 Why runtime belongs at the top of your control map
  06:30 Identity for agents: Auth0, Okta, WorkOS, Entra
  08:50 Delegated authority and why fuzzy authority is dangerous
  10:30 The data control point: Snowflake, Databricks, BigQuery
  13:00 Payments and institutional trust: Stripe and the card networks
  16:00 Observability: why logging isn't enough for agent runs
  18:00 The kill switch is a multi-layer product feature
  19:20 The seven questions to map any agent workflow
  
  Subscribe for daily AI strategy and news.
  For deeper playbooks and analysis: https://natesnewsletter.substack.com/
  
  Listen to this video as a podcast.
  - Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  - Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "nate b jones"
  - "nate jones"
  - "artificial intelligence"
  - "AI"
  - "AI news"
  - "AI tools"
  - "machine learning"
  - "generative AI"
  - "ChatGPT"
  - "Claude"
  - "AI prompts"
  - "AI strategy"
  - "tech news"
  - "AI agents"
  - "agent infrastructure"
  - "Stripe agentic commerce"
  - "Auth0"
  - "Snowflake Cortex"
  - "LLM observability"
  - "AI agents for enterprise"
  - "agent identity layer"
  - "production AI agents"
  - "cloudflare"
  - "stripe"
  - "okta"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
  - "Founders"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Google"
    - "Microsoft"
    - "Amazon"
    - "Nvidia"
    - "Salesforce"
    - "Slack"
    - "GitHub"
    - "Stripe"
  people:
    []
  products:
    - "Gemini"
    - "LangChain"
    - "Make"
    - "MCP"
    - "Operator"
  models:
    - "Gemini"
concepts:
  []
summary:
  - "# These 5 Infrastructure Giants Secretly Rule AI

There are companies that get to decide whether your agent actually ships or not"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "amazon"
  - "anthropic"
  - "coding"
  - "frameworks"
  - "gemini"
  - "github"
  - "google"
  - "langchain"
  - "make"
  - "mcp"
  - "microsoft"
  - "nvidia"
  - "openai"
  - "operator"
  - "product-management"
  - "prompting"
  - "salesforce"
  - "slack"
  - "stripe"
---

# These 5 Infrastructure Giants Secretly Rule AI

There are companies that get to decide whether your agent actually ships or not. And they're probably not the ones you're thinking of. I bet you're thinking of OpenAI or Anthropic. No, no, no. What about Cloudflare? Cloudflare ran agents week last month. What about Stripe? Stripe rolled out its Agent Commerce Suite or or Octa? Octa launched Octa for AI agents at the end of April and has continued to expand it since. Ozero has been building out its AI agents documentation. Data Dog has been quietly building out its LLM observability platform. None of these companies build models. None of these companies are on most teams AI stack road mapaps. But all of them are going to decide whether your AI agent gets deployed in production. So the model is one piece of the agent economy. The infrastructure companies, the ones that decide where the agent runs, who it's acting for, what it can know, what it can spend, and who can stop it. Those companies own effectively the infrastructure that controls whether an agent reaches production. and the control layer, the infrastructure layer that drives agent success is where a lot of AI power is moving. So let's dive in. First, I want to talk about compute and how compute is not the whole story. So the easiest AI infrastructure story is the physical one and I've told it in other videos. So if you're interested, dive in. Right? I've talked about GPUs and data centers and power and memory and networking and capex and that story is real. But the physical infrastructure only determines whether AI can be served at scale. If the power isn't available, the model doesn't serve. Right? Once agents start doing work, the next bottleneck is whether the intelligence you can generate is governable. Where does the agent run? What does it remember? Who is it acting for? When does it need approval? What can it spend? And of course, who can stop it? Those kinds of questions must get answered by infrastructure, not by a model. So compute is really important to scale agents as we start to talk about a full agentic economy, but it's not sufficient. Now I've talked about protocols before. I have a whole article on Substack. I've got a recent video on it. I've talked about six key protocols for the agent layer recently. This video is about the layer underneath those protocols. Who is building the infrastructure that makes those protocols come to life? And the first layer I want to talk about underneath the agentic protocols is the runtime control point layer that has Cloudflare AWS and versel. Okay, let's let's start at runtime and talk about that. Where does an agent actually live? So a model is stateless. You send a prompt, you get a response, the conversation is over unless you send the history back next time. And that is perfectly fine for chat, but it doesn't work for an agent that has to remember what happened and wake up later and continue after a disconnect and run on a scheduled task and recover from a tool failure or stay connected to a user in real time. Real agents need a runtime with memory and execution built in. And that's why Cloudflare is building agents SDK. Every agent runs on what Cloudflare calls a durable object, a stateful microserver with its own SQL database, its own websocket connections, its own scheduling. The agent can call tools, it can serve tools through MCP, it can schedule tasks, it can coordinate with sub aents, it can browse the web, it can react to events. And Cloudflare is not alone here, right? AWS is making the same control layer claim inside its own cloud with Amazon Bedrock agent core packaging runtime and memory and identity and gateway and browser and code interpreter and observability into a stack. Verscell is coming at a little different angle with AI gateway where the control point is model routing and budgets and monitoring and load balancing. So there's some different bets here but it's the same thesis. So runtime is becoming a control surface in its own right. If your agent has durable work or deadlines or callbacks or streaming UI or tools or approvals or payments or state and most production agents tackle those kinds of tasks, then runtime is something that you have to decide intentionally. It belongs at the top of your control map because it shapes the rest of the environment your agent operates in. Now we move to the next layer, the identity control point. Ozero, Octa, work OS, Entra. Let's sort of understand what this means. It's a huge topic in in ordinary software. Identity means authenticating a user and authorizing that user against application resources. The user logs in, the app checks the permissions, the work proceeds. That model breaks when an agent acts on behalf of a person. The agent might be acting for one user or a single team or a company or another agent. The APIs it calls might span Google or Slack or GitHub or Salesforce. You get the idea. Approval often comes asynchronously while the user's away. And when the agent retrieves documents from a rag pipeline, only some of those documents are the ones the user's allowed to see. Ozero is tackling this complexity by building this layer in public. Their AI agents docs cover user authentication, OOTH based API access, token vault, asynchronous authorization, and fine-train authorization for rag. The mechanic is delegated authority with constraints. An agent does not get a broad permanent credential just because a user decided to sign in once. Instead, it calls APIs on behalf of a user. Similarly, token storage doesn't expose secrets to the agent. The agent has to ask for consent for sensitive or longunning operations and rag queries only retrieve documents the user is actually authorized to see. Now, Ozero is not the only player here. Octa, work OS, Microsoft Entra, agent ID, and AWS agent core identity are all sort of converging in the same problem space because the dangerous agent in a company is not necessarily the most capable one. It's the one with very fuzzy authority where nobody can clearly say whether it's acting as the user, as the company, as the application, or as itself. And nobody knows whether the permissions persist across sessions or cover a class of actions beyond the original request. That's all manageable when agents draft text. It is not manageable when agents transact and deploy and refund and schedule and provision or make serious commitments on their own. A serious agent product needs a serious authority model. Who is the principal? What can be delegated? What can be revoked? What does the audit log show? If those questions aren't answered, your agent is going to hit a ceiling in any serious company. The full operator landscape, I put that over on Substack. You can dive into Ozero and Octa and work OS and Entra agent ID and AWS agent core identity and you'll get the whole list on Substack of what each one is trying to control and a clear protocol for how you pick an identity provider which is an extremely impactful decision. So if you want to dive in there deeper that's where you find it. We're going to keep moving though to the data control point and that's where we talk about companies like Snowflake or data bricks. Agents are essentially only as useful as the data they can safely interpret. A generic agent fails at data in predictable ways. It joins the wrong tables. It trusts the wrong column. It misunderstands a metric. It receives stale documents. It answers confidently from ungoverned context. It presents an assumption as a fact. Every one of those is a data control failure. The model is doing what it can with the data it sees, and the data it sees hasn't been governed for agent use. Snowflake's bet on the data control point is very specific. Their Cortex agents docs describe agents that work across both structured and unstructured data. Cortex Analyst handles structured queries. Cortex search handles unstructured retrieval. And the agent routes between them. All of that happens inside Snowflake's governance perimeter. And so the key thing that they want you to take away is that they are governing the distribution of meaning. Because a data warehouse is really where companies try to build a reliable meaning, right? A version of business truth, whether that's around revenue or customers or inventory or churn or margin or forecast. And agents make that semantic layer, that meaning making more important, not less. What is ARR? Which customer hierarchy is authoritative? Which data is restricted? Which agent do I trust? An agent that can't tell current revenue from forecast revenue. That's not the one that should be drafting the board narrative, right? You shouldn't have that in production. What about an agent that can't tell public docs from confidential customer commitments? They shouldn't be answering support questions directly, should they? So, that's the problem space that Snowflake is going after. Datab Bricks is going after a similar problem and making a parallel argument with its mosaic AI agent framework around building deploying evaluating and monitoring agents inside the same governed environment where enterprise data already lives. Big Query and Gemini are the hyperscaler native version of this same move. These companies are doing more than adding chat to databases. They're trying to make the govern data platform the place where agents are allowed to reason and act. And if your business has a semantic layer, and almost all of them do, even if it's informal, your agent needs to be operating inside that layer's governance, not around it. This all matters because if your business has a semantic layer, if it has a data layer that helps you make meaning of business metrics and customer relationships, and most businesses do, then your agent needs to be operating inside some kind of governed permission structure. And that's sort of what data bricks and snowflake are going after. Okay, let's move on to the payment control point. Stripe and the networks. The moment an agent touches money, the control problem becomes really really critical. Now, the protocols themselves, if you want to understand them, I I dive deep on AP2 and X42 and others in a different video. I want to focus now a layer above the payments protocol. I want to focus on the operator side. Stripe sits at the center of all this, not because of any single protocol. Stripe supports several of them, but because Stripe already lives in the middle of a commerce, payment credentials and fraud and disputes and risk and billing and subscriptions and issuing and treasury and merchant onboarding and all of the developer APIs underneath all of that. Agents make every one of the intersections I just named very valuable. And Stripe is the company best positioned to play across that bundle. And it is moving extremely aggressively to outline the pathways for agents to handle all of what I just described, right? Issuing payments, authorization, fraud, mitigation. Stripe is coming for all of that with agents. And it's doing so because Stripe believes that the future is a larger internet economy with a lot of agent commerce going on. And so it makes sense for them since they're on a mission to grow the entire internet economy to go after the agentic part of that economy and make sure that they enable that and set that up so it's easy to transact. That's the larger vision for Stripe and that's why you see them making these moves across all of these agentic pieces as an operator at the center of this network across multiple protocols. The card networks are operators in the protocol space, but they have a very different set of incentives than Stripe. Stripe is looking to grow the economy as a whole, but the card networks need to make sure Agentic payments run on their rails. And that's true for Mastercard and Visa and American Express. And so they're competing on something different from a protocol perspective. They want to prove and show that an agent transaction can run on their rails and clear the same institutional trust chain a card transaction can clear. And that's how they think about fraud and dispute and merchant onboarding and everything else. That's a different bet. and the networks have a lot of infrastructure to back them up there. That's how card payments work especially in the US. So the payment ecosystem is dominated by operators who move above particular protocols and have differing motivations but have the same larger pattern of behavior in that they're all trying to put out agent payment solutions and the payments ecosystem for agents is going to have to evolve quickly. That's part of why operators are moving quickly because they know from experience with other payment products that if you don't quickly move to enable legitimate patterns of transaction, you get fraudulent patterns of transaction and that becomes a big issue. So the reason payments matter is that payments essentially are a form of institutional trust and the company that is able to facilitate that institutional trust owns one of the most important control points in the Asian economy. And if you are building in that space, if your agent is going to touch money, you have to be thinking about which of these partners you are working with in order to enable that experience. And right now, you know, unless you are in a special jurisdiction and it's extra complicated, the default is probably Stripe. In most cases, for most startups, that is the default. And if you're an enterprise, you may have your own payment stack. You know, Amazon has its own payment stack. There are others that do as well. Regardless, you have to be thinking about whether you are investing in your own payment stack and extending it to provide the agentic capabilities that you see from Stripe and others or whether you're going to partner with them and build customer experiences that are that rich because these big operators are playing in the space and providing the rails on which Agentic Commerce can run. Next big theme for shipping production agents, observation. This one's easy to underrate because it sounds like you're logging it. That's not what this is. You're not just logging. Agents fail differently from ordinary software. They call the wrong tool, but they might call it with valid syntax. They ask the right agent, but they might ask it the wrong question. They can retrieve authorized data, and they still draw the wrong conclusion. They might complete a task technically while violating the user's intent. They can stay inside permission boundaries and still create a very expensive loop in terms of tokens. they keep retrying, maybe they escalate too late. Logs by themselves don't catch those sophisticated failure patterns. What you need is a way to observe agent runs as work, not as API traffic. What was the goal of this work? Which tools were called for this work? Who authorized the action? Which data sources were used? Which policy blocked that action? Which cost was incurred? Did a human accept the result? Infrastructure companies can gain real power at this layer. Data Dog has been building LLM observability. It traces what the agent did end to end, prompts going in, responses coming back, tool calls, retrievals, and it connects all of that to the backend services and user sessions sitting around the agent. Langmith sits closer to the developer side. If your team is building on Langchain or Lang Graph, Langmith is where you trace the agents workflow and run evals against it. Brain trust and Langfuse are taking very different bets here, right? Brain trust leads with evals running quality checks against agent output. Langfuse is more of an open- source tracing option. In AWS, they're just interested in wiring all this together, right? Agent core observability supports open telemetry, which means you can send agent telemetry into cloudatch and data dog and langfuse from one single place. So in this situation, the market is converging toward a single control plane where traces and cost and tool calls and eval outcomes all get stitched into one operational view of what your agents are doing. One more thing, the kill switch. The kill switch is absolutely a product feature and it has to be implemented at more than one layer to work well. And most teams aren't thinking about that because your agent runtime can cancel or pause the run. The identity system might revoke the credential. The gateway might block the tool call. The payment system might freeze the payment instrument or or hit a sping limit. A framework like Langraph can interrupt a workflow before a sensitive node is hit. Right? So if the only way to tell your agent to stop is to just tell the model to stop, you don't have a kill switch. Look at all the nuance in what I just described. So I'm going to go into kill switch architecture in the Substack piece as well. How to implement it at runtime, how to think about identity and gateway and payment and framework layers. So that tell the model to stop is not your only option. You can dive into that. But for now at this level, I want to leave you with what you can think about for this week. And I want to suggest, as I often do, that you start somewhere specific. Take a support refund agent or a customer emails support agent or or or a claims agent or an agent that reads conversations and checks usage. Pick a specific agent workflow. Then understand these seven things. Where does the agent run? What is the runtime layer? Is it Cloudflare? Is it agent core? I don't know. Who is that agent acting for? It needs an identity layer. Is it acting for the company? Does it have delegated access? That's o zero or octa right there. What can it know? Uh does it understand the data layer? Does it understand usage data? And can it pull that in? Is that a snowflake thing? What can it change? The tool layer. Where does it have read access? Where does it have right access? Where does it have approval? What can it spend? That's the payment layer, right? Does it have refund limits, approval thresholds? Are you working with Stripe? What gets observed? Look at the observability layer. Did the agent issue a refund that violated policy? Did it get tricked? Now you're talking about Langsmith. Maybe you're talking about AWS or Data Dog. And then who can stop it? Where's the kill switch? Can runtime cancel? Can payment freeze? Can identity revoke? How do you do that? Fill all of that out for this one workflow. If you have a TBD on one of those rows, you need to tackle that before it gets to production. And you need to have owners for these because otherwise someone is just going to say it's someone else's problem. on how to solve agent identity and then you're going to find you never solved agent identity and now you're launching and that's a problem. Agents do not respect org charts. Your governance model has to compensate for that. I was talking recently with someone who leads a data team and what she was observing to me is that there are cases where your agents can literally hack around your existing permission structure inside your internal system because it was designed for humans and it can come back and the agent may have done a successful run and it did so outside of the permission structure. And this is a problem for her from the data perspective because she needs to figure out whether the agent executing that run was authorized to work its way around the human permission structure or whether that agent was acting inappropriately and showed data to the human that it shouldn't have. And there's multiple layers to that because like one you could say well the agent shouldn't have worked around the problem. Two you could say the human shouldn't have seen the data. Three, you could say, you know what, maybe the agent was goal oriented in a positive way, but we need to give it better tools to solve the problem. Four, you could say the agent was allowed to do that and we're okay with that degree of chaos. And there are a surprising number of companies that do that, but I think that that's going to become a riskier and riskier stance to take as agents get more capable. So, these are real challenges. You run into these control layer issues more as agents get more capable inside your systems. And it's often platform teams that face it first. If we step back for a minute, look, the AI economy is going to keep consuming much more compute over time. So the hyperscalers are still going to matter. NVIDIA is still going to matter. Models, they're going to continue to get better. But none of that decides how your agent actually ships. None of the things I just named. Instead, the companies that decide whether your agents successful are the ones that are building the layer that determines whether agents can act. And I've named a bunch of them here. I've talked about Cloudflare and Ozero and Snowflake and Stripe and Data Dog that this control layer helps teams figure out which control surfaces they need to enact, engage, build on in order to actually ship agents this year. Now, if you want to see an example of how you work through a workflow with all of those control points named, all seven questions answered, I wrote that out on Substack in full. where the agent runs, who it's acting for, what it can spend, what what gets observed, who can stop it. If you want to copy it for your team, you can go grab it. Otherwise, thank you for tuning in. We are digging into agents because if we don't understand agents, well, we are going to end up in a situation like my friend on the data team who's trying to figure out whether or not the agent that hacked around the authorization to get the data pull done is doing the right thing, the wrong thing, or something in between. These are stories I'm hearing all over the industry. They matter a ton. I'll see you soon. There will be more AI news tomorrow.
