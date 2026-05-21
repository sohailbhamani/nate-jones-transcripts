---
title: "Google Spent a Year Stitching MCP, A2A, AG-UI Together. I/O Today."
video_id: "zP6TnEiueEc"
youtube_url: "https://www.youtube.com/watch?v=zP6TnEiueEc"
publish_date: "2026-05-19"
duration: "20:42"
duration_seconds: 1242
view_count: 33128
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Full Post w/ Prompt Pack: https://natesnewsletter.substack.com/p/agent-protocol-stack-mcp-a2a?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  __________________________________
  What's really happening inside the agent protocol race?
  
  The common story is that Google I/O is about the demos — but the more interesting story is the protocol stack being built underneath them.
  
  In this video, I share the inside scoop on the six agent protocols defining the year:
  
   • Why three of six form the actual agent stack
   • How MCP, A2A, and AG-UI map to real builder questions
   • What AP2 and x402 mean for agent payments
   • Where customer experience meets protocol choice
  
  For builders shipping agent products in 2026, the substrate you pick shapes the customer experience as much as the model you choose.
  
  Chapters:
  00:00 Six protocols, three that matter
  01:18 The three questions agents must answer
  02:35 MCP: the tool and data layer
  04:50 Why MCP is a security boundary
  06:20 A2A: the delegation layer
  08:15 The agent card as operating contract
  09:40 AG-UI: the human control layer
  11:55 Why agents need supervision surfaces
  13:30 A2UI, AP2, and x402: the contested layers
  15:10 AP2 and the mandate mechanic
  16:35 Stripe and customer-obsessed payment design
  18:00 Six questions to ask before you build
  19:45 What to watch at Google I/O
  
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
  - "MCP"
  - "A2A"
  - "AG-UI"
  - "agent protocols"
  - "Google I/O"
  - "AP2 payments"
  - "agent stack"
  - "AI agents for builders"
  - "agent payment protocols"
  - "ai news"
  - "google"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Google"
    - "Amazon"
    - "Salesforce"
    - "Slack"
    - "GitHub"
    - "Stripe"
    - "Box"
    - "Snowflake"
    - "MongoDB"
    - "Atlassian"
  people:
    []
  products:
    - "Gemini"
    - "Copilot"
    - "Make"
    - "MCP"
  models:
    - "Gemini"
concepts:
  []
summary:
  - "# Google Spent a Year Stitching MCP, A2A, AG-UI Together"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "amazon"
  - "atlassian"
  - "box"
  - "coding"
  - "copilot"
  - "frameworks"
  - "gemini"
  - "github"
  - "google"
  - "leadership"
  - "make"
  - "mcp"
  - "mongodb"
  - "product-management"
  - "salesforce"
  - "slack"
  - "snowflake"
  - "stripe"
  - "tutorials"
---

# Google Spent a Year Stitching MCP, A2A, AG-UI Together. I/O Today.

Google IO opens today, May 19th. There will be a ton of agent demos. I can guarantee you that I will get into coverage for Google at another time. The more interesting story is what is happening underneath Google IO, including in many of the protocols Google is putting out there to drive the Agentic Revolution. I want to talk today about six agent protocols that have launched in the last year and how they underly agentic systems. Why do we do that? Because it turns out that the substrates for agents actually shape the customer experience. What are those six? MCP, A2A, AGUI, A2UI, AP2, and X42. It's not Star Wars robots. It's actually real protocols. And if you're building an AI agent product right now, that list is really hard to wrestle with and understand. It feels like a standard scrum. New acronyms are popping up all the time. There's new diagrams. There's new claims that some missing piece of the agent stack has been solved with a new protocol. Here is my read. Three of the six that I just named are becoming the actual agent stack. The other three are very much in contested layers that we need to be honest are still under debate. So, we're going to talk about all six today and we're going to talk about the three that are part of the core standard stack first. But before we get into which three are the standard, I want to lay out the overall landscape for agentic protocols. What are the questions that we're trying to answer with agentic protocols? I want to suggest three for you. Number one, what can the agent use? Number two, who else can the agent work with? And number three, how does the human stay in control while the agent is working? Keep those three in mind because they shape the customer experiences that we're trying to drive at the end of the day, whether we're building for internal or external customers. And they also help us to understand what really matters when there's a bunch of standards out there. Now, three of those six protocols directly map onto those three questions. MCP, that's a tool and data layer. It's the protocol an agent uses to discover and invoke the systems where your work lives. ADA, that's an agent coordination layer. It's the protocol one agent uses to discover and delegate to another agent across product or company boundaries. AGUI is a human interaction layer. It's a protocol that lets a longunning back-end agent share state and events and approvals and interruptions with a userfacing app. The other three protocols, A2UI, AP2X42, they all sit in a different spot in the stack. A2 UI is about how agents render structured interfaces. AP2 is about authorizing agent-led purchases. X42 is about machine to-achine payment at the HTTP layer on the web. All are really important and all are still contested or very domain specific. I break down all six protocols layer by layer on the Substack with source links, name partner list. If you want the full version, you know where to get it. We're going to move on in this video to MCP, perhaps the most popular and most well-known protocol stack in AI. MCP won share first because it solves the most immediate pain in agentic building. An agent sits in a chat box and has no access to tools and cannot do work. Right? It can only advise. It can summarize. It can draft. It's a 2024 world. The work itself lives somewhere else. It lives in GitHub. It lives in Slack. It lives in Drive and Postgress and Stripe and Linear and Salesforce in some internal API in a calendar. Before MCP, every integration with all of the tools I just named looked like custom glue to your chatbot, right? You had to have tool definitions and authentication patterns and parameter schemas and error handling all written from scratch every time. The beauty and power of MCP is that it standardizes all of that. A server exposes tools and resources. An agent host connects to it. The model receives a usable description of what can be done. New capabilities composed without every single agent platform rebuilding every connector. Cloud Desktop supports local MCP servers and so do most of the other agent tools out there including Codeex. Uh Google has support for it. There are more than 14,000 MCP servers now. And it's tempting to treat MCP as if it makes tools safe just because it's a standard across the internet. It doesn't. Tool access enables arbitrary code execution and arbitrary data access. And that's good because MCP is designed to allow agents to use tools in arbitrary ways to get task done. That's the reason it was created. But that also means that MCP was created for a high trust environment. And we now have to think about how we configure security and security stances around a tool using agent experience. MCP was not designed for that at root. And so there are other challenges that we have to solve if we are trying to build secure agents. You know, Invariant Labs has already published research on what they call tool poisoning attacks, which are malicious instructions that can hide inside tool descriptions that can be exposed via MCP. And those malicious instructions can influence an agent through the very metadata that's supposed to make the tool discoverable. So tool access is not a feature toggle even though it's treated that way in a lot of user interfaces. Now it is a security boundary that you're crossing. If your team is shipping MCP servers, you still need scopes and approval flows and audit trails and a real answer to which tools the agent can see in which context. MCP does get the agent close to the work. It does not decide whether the agent should do the work. And if you're interested in digging into the security side of things, the Substack piece goes deep on the Invariant Labs tool poisoning research, what that means for how we design our scopes, how we design our approvals. If your team's already running MCP servers, you definitely need to dig into that topic. You need to understand what you're exposing. For now, we're going to move to A to A and the delegation layer. So MCP gets agents reach, right? The second problem arrives the moment the agent actually starts working. So the agent can't know everything. It can't own every capability. A procurement agent will need a supplier agent. A travel agent needs a hotel agent. A finance agent may need a tax agent. Uh a software agent may need a security reviewer. In fact, I know it does. Work is distributed across owners and permissions and domains and expertise. No one agent does it all. So A to A turns that distribution into something that agents can reason about. And the important primitive in that stack is the agent card. A remote agent publishes a card that describes what it is, what it does, which skills it exposes, where it can be reached, and how another agent ought to interact with it. The agent card is the first version of an operating contract. It has real terms and real interfaces and real responsibility. Google launched ADA with a bunch of partners, right, with Atlassian and Box and Coher and MongoDB and PayPal and Workday. more than 50. The list matters because A toa A only works if agents really can cross product and company boundaries. So you want a world where you have discoverable delegation for agents, not just a bunch of swarms that look good on paper. But there's a cost here. Coordination isn't free. A toa adds another surface where you can have latency and failure and permissions and observability issues. If an agent asks another agent to do work, it certainly makes the agents workflow more flexible, but it also makes it less predictable. So A to A isn't the right answer for every product. A single product with a small set of tools may not need agent coordination at all. The right question to ask is whether this workflow requires delegated expertise or authority outside the primary agent. If the answer is yes, you need to think about what that looks like ahead of time. Decide what your agent can say about itself. decide what it can accept, decide what it can't share, decide what requires human approval, decide how a downstream result gets validated. The agent card is Google's attempt to make part of that process standard, but it's still missing a control layer, and that's where we get to AGUI. Now, I know it's easy to underestimate AGUI because most people who hear about it think it is about driving the user interface. I don't think that's the best reading. I think a better reading is that AGUI helps us to ensure trust in agentic workflows. An agent that's longunning, that's non-deterministic, and that's capable of touching external systems needs a lot more than a final answer for a human to see. Humans need to be able to observe that agent as it works, approve sensitive steps, correct course, inspect state, understand why the agent is waiting. And traditional web apps are just built for call and response. They don't really handle the streaming work that agents do. They don't handle the fact that agents may discover new information mid task. The chatbot experience is not enough for that and neither are most traditional apps. So AGUI is the open candidate for the human control layer. The docs talk about what agent apps actually need, right? Streaming, shared state, front-end tool calls, backend tool rendering, custom events, steering, sub aent composition. This is the layer many teams will ignore until their agents start doing real work and generating real bucks. So they'll wire a model to tools. They'll wire up a nice chat component. And then they'll discover what their agent is really doing. And then they'll say, "Oh no, we need approval buttons. Oh no, we need logs. We need a progress spinner." None of those things by themselves are fixes for the root issue, which is about finding the right control points, understanding what the agent is trying to do, understanding what it's waiting for, and then figuring out where the user needs to approve or deny or edit or cancel. So, AGUI belongs with MCP and ADA in the core stack even if the specific protocol is earlier in the adoption curve. AGUI itself may win that race, maybe a close cousin does. But the point is that an agent that can't show its work becomes supervision debt for humans. And this is a way to address that and actually at root think about the control problem for agents and build systems that allow humans to interact at the right moments with running agent workflows. Now, if AGUI is new for you, if you want to dive deeper, the Substack piece gets into all the elements in the ecosystem. It talks about AGUI with Langraph and Crew AI and Amazon Bedrock Agent Core and Pidantic AI and Mastra and Copilot Kit. If you're picking a framework, that's where you want to dive in and look. Now, we need to get to the other three protocols, the one that I said weren't part of the core stack, because we need to understand why. Because they won't tell you they're not part of the core stack. Every protocol thinks it's a standard. Why are these not standards? And what does that tell us about the state of the agent race? So the other three are A2 UI, AP2, and X42. A2UI is Google's project for agent generated interfaces. Instead of sending arbitrary HTML or JavaScript from a remote agent, which is frankly a security disaster waiting to happen, A2UI sends a structured declarative UI representation. The client renders using trusted components. The agent asks for components from an approved catalog. It cannot execute arbitrary interface code and that is absolutely the right direction to be running in. But it's much narrower from a solution space than the human control problem that AGUI is solving. A2 UI is just one piece of the overall rendering question and it doesn't try and establish a whole user control layer like AGUI. And so that's why I see A2 UI as being useful and helpful for driving some kinds of generated experiences, but maybe not as focused on the substrate that many many agents will need to drive successful workflows in the new Agentic economy. AP2 meanwhile is Google's Agentic payments protocol. 60 plus collaborators jumped onto this. You might think that makes it a standard, but not in payments. Uh the collaborators include Auden and American Express and Coinbase and Mastercard and PayPal and Salesforce and Union Pay and World Pay. That the key mechanic here is what's called the mandate, a cryptographically signed proof of what the user authorized. AP2 is trying to answer the most difficult question in Agentic Commerce. How does the ecosystem know the agent was authorized to buy? Meanwhile, X42 is Coinbase's HTTP native payment protocol. Cloudflare's adopted it. The use case is very much agent-gagent payment for resources. An agent buys an API call or a data source or a document or a benchmark run and it doesn't have to set up an account or negotiate a subscription. So AP2 and X42 are very much adjacent, but they're not the same thing. AP2 is about commercial trust and user authorization, and X42 is about how do you settle payments for resources for agents. And this this is not the end of the story. The protocol pile gets really big with payments because payments are a very valuable space to be in. If you're interested in diving deeper, I did an entire video recently on Stripe and its role in the payment space. That is definitely a video you want to check out if you're looking at payments and agent protocols. They've done a phenomenal job understanding that you are driving human trust in Aentic Commerce. And that is why their suggested experience of just sending an agent to a link to get an authorization token feels so smooth. So the protocols are going to keep piling up in the payment space even beyond Stripe. You have uh Mastercard with Aentic tokens. Visa with intelligent commerce. American Express has an Aentic commerce experiences developer kit. PayPal is supporting AP2 but is also building its own commerce layer. The payment space is so valuable, everyone wants to jump in. And if you're a builder right now, I would encourage you to think in the customer obsessed way that you see from recent Stripe launches because what you want to do is think about for my customers who have to trust agents. How do I ensure that the payment space is something that they feel they can participate in, authorize an agent to transact in, and feel good that their wallet is secure, the payment is authorized, the payment will be completed, and their order will be done as they expected. And so, don't look at payment protocols in particular as just a technical choice. They're very much a customer experience choice. Okay, stepping back here. How do you think about how substrates shape the customer experience? And how do you think about wrestling with them and getting into that problem space? If you've been assigned to ship an AI strategy or make an AI agent or complete a workflow with AI agents first and foremost, I've talked about this before. Get into the specifics, understand what you're really doing. Are you tackling support triage or procurement or sales territory analysis? Are you doing customer renewal prep? uh what what are you actually doing right understand that and then start to ask how does the substrate we are talking about shape the agentic experience for the customer right the MCP layer is absolutely going to be part of the conversation in most cases because you're going to want to have the option to bring that agent close to the work the ATA layer is narrower but can be very important if you're trying to understand how agents need to reason across other agent workflows. The AGUI layer is where you want to think about the ability to handle humanapproved longunning agent workflows. So for example, where the CSM might see a packet being assembled for the customer and might need to approve whether billing context should be included on the fly. Now, something like A2 UI might matter if the agent renders a particular usage chart or particular contract chart that helps someone understand what the agent is producing and you want some control and some guarantee that those components are real. And in this world, you need to be going through and asking yourself how your specific workflows map to the specific nuances of those protocols. And I'll give you an example from payments. So payments are complicated because payments are unique in different geographies. And one of the things that's really interesting about the payments experience with agents is that you have to blend in multiple competing protocols with multiple competing geographies as far as where customers are comfortable transacting, what payments methods they have, how they feel about using agents and compute when they're doing payments, etc. So there's a whole gnarly customer experience. There's a bunch of competing substrates. And if you want to put together an experience that is compelling, it is up to you to understand that a given payments experience may be biased toward the United States, toward US payment methods, given payments experience may be biased towards an assumption that humans will not make microp payments. And I I think that one of the things that I want to encourage you to do is to look at the things that may seem boring about these protocols. things like how fees are handled, things like how returns are handled, things like how delivery is handled, things like how uh authorization is handled and how long authorization runs for. And recognize that those have real customer implications. If your customer is not comfortable reauthorizing and you have a short-term token that you're driving for payment authorization and and your customer just wants it done and doesn't want to reauthorize every 30 minutes, you're going to have a very frustrated customer on your hands and that may be built into the protocol as a friendly default because it assumes a different customer. So, so protocols can be opinionated and that's okay, but you have to think about what that means for you. And I prepared six questions to help you start to dig into that. Number one, what tools and data does the agent need? Does the agent need to get into the MCP layer? Find out, right? Number two, what other agent surfaces or specialists does it need to call? Right? That's the A to A layer. Three, where does the user need to approve or edit or interrupt or steer the work? That's the AGUI layer, the control layer. Does the workflow need structured UI beyond text? That would be number four. A2 UI would help there. Number five, does the agent need to spend money? Does the agent need to authorize a transaction? Maybe that's an AP2 use case. Number six, does the agent need to autonomously pay for a resource programmatically? Maybe that's X42. Maybe it's something else. In general, most teams are overfocused on model selection, and they're very underspecified on the operating surface around the model. They know which LLM they want. They don't know which tools the agent can or should see. They may have a prototype that can call APIs, but they don't have an interaction model for user approval. They can imagine multiple agents coordinating, but they don't have any way to enforce or validate that. The actual work lives in those kinds of questions. So, I know we began this video talking about Google IO. There's going to be a lot of Agentic demos. I want you to watch at Google IO for one thing. Does Google make the agent stack feel like a single operating model? Does Gemini Enterprise stitch ADA agents and MCP tools and A2 UI interfaces and AP2 payments into something a builder can chip against? Or does IO give us a new set of standards, another another two or three standards to add to the pile? Because this is a year where the agent stack needs to stop being a list of acronyms and needs to start being really really buildable. And the companies that figure out how to build against the protocol stack in ways that shape customer experiences, they're they're going to be the ones that win, right? And we're going to look back in six months and realize that because agent workflows for developers unlocked in the first half of 2026, this was a golden time for building what really mattered. Now, if you want to dive into those six questions and how you understand how to think about agentic workflows with an eye on the customer and an eye on how these protocol substrates drive the customer experience in detail. I get into all that on the substack, right? We'll talk about Salesforce and Snowflake and Drive and Slack all how they operate at the MCP layer. We'll talk about billing and legal agents at the ADA layer. There's a dive on CSM facing approval services at the AGUI layer and how you think about that. So, if you want to get a quick start on copying some of those pieces for your team, you can grab that link. It's great. I hope that this dive into the substrate of agents has been helpful. It may not feel sexy to talk about why agent substrates drive customer experiences, but it's profoundly impactful and it's something I don't see coming up enough in conversations with build teams as they think about their agent workflow. So, I thought it was important to lay it out, lay out the standards really clearly and help you understand how to think about these standards and of course the next one that's going to come along next week. I'll see you on the next one. Cheers.
