---
title: "MCP, A2A, and the Beginning of the End of Explicit Programming"
video_id: "cPdVbVx5Z3Q"
youtube_url: "https://www.youtube.com/watch?v=cPdVbVx5Z3Q"
substack_url: "https://natesnewsletter.substack.com/p/how-i-think-about-mcp-a-practical?r=1z4sm5"
publish_date: "2025-04-09"
duration: "8:56"
duration_seconds: 536
view_count: 23490
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Tools"
difficulty: "Advanced"
audience:
  - "Engineers"
entities:
  companies:
    - "Google"
    - "Salesforce"
  people:
    []
  products:
    - "Make"
    - "MCP"
    - "Model Context Protocol"
  models:
    []
concepts:
  - "Change the substrate that software runs on? i've been obsessing over this lately because i've been deep in the weeds with model context protocol or mcp"
  - "I think it represents a profound shift in how we build ai systems and the a2a announcement doubles down on that shift"
summary:
  - "# MCP, A2A, and the Beginning of the End of Explicit Programming

Today something really massive happened in AI architecture and I don't think most of us realize how big it is"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "coding"
  - "frameworks"
  - "google"
  - "make"
  - "mcp"
  - "model-context-protocol"
  - "product-management"
  - "prompting"
  - "salesforce"
  - "tutorials"
---

# MCP, A2A, and the Beginning of the End of Explicit Programming

Today something really massive happened in AI architecture and I don't think most of us realize how big it is. Google announced agentto agent protocols or aa and everybody's focused on the impressive partner list. I really want to talk about something much more deep. What happens when we fundamentally change the substrate that software runs on? I've been obsessing over this lately because I've been deep in the weeds with model context protocol or MCP. I wrote an article on it on Substack yesterday, but fundamentally I think it represents a profound shift in how we build AI systems and the A2A announcement doubles down on that shift. So let me dive into it. So for the last call it 70 years, we've built software roughly the same way. Explicit instructions, explicit connections, explicit logic, what we would call deterministic software. Every interaction has to be programmed. Every data flow has to be defined. Every decision point needs to be all the way mapped out. This is how we got waterfall software, right? Uh and we've gotten really good at it. And it's fundamentally limiting. It limits because it constrains your upside. Your software can only do what you've told it to do. It can never do anything more. MCP was the first real crack in that paradigm. Because instead of programming exactly how an AI should use tools, MCP lets us talk about and describe tools and their capabilities in a structured way and then lets AI figure out how to use them. It's a subtle shift, but it's a really profound one. We're moving from explicitly programming to capability description. And what's interesting is that in and of itself is an evolution of the very concept of the large language model which itself is not deterministic. I mean people will argue with you and tell you that LLMs are inherently deterministic and that's a conversation for another day but from a usage perspective they don't function that way. Uh they function as non-deterministic software and we've all been getting used to that and that's why prompting is such a big deal. MCP really took that world and turned it into how we design software. And so now we have agents determining how they will use tools through MCP. And then it gets more interesting with today's announcement. And that's why this matters so much because A2A or agent to agent, it takes the same principle from MCP and applies it to how AI agents work with one another. It's not just about tools. It's about agents discovering each other. So, it's not just about agents discovering tools and using those tools and making tool allocation decisions. It's about agents discovering one another, understanding each other's capabilities, and figuring out how they collaborate. So, if you think about what that means, we're not just changing how our software works with tools and making that less deterministic. We're also changing how our software works with other software. So if you're an engineer, you're thinking about all the problems, right? How could this go wrong? You're totally right. Uh in fact, I have a lot of concerns with MCP as well. I think it's challenging to build scaled systems with MCP right now. Uh and I think that it's challenging to build with A2A right now. Doesn't mean it's impossible, but it's tough to outline a few of the issues. There's a state management problem when you have multiple agents working together, each with their own context, their own understanding. How do you maintain consistency? How do you prevent conflicts? How do you handle partial failures? They're not new problems per se. Distributed systems engineers have had to work on this before, but they take on new dimensions when your nodes are autonomous and when they your nodes make their own decisions. Second, there's reasoning overhead, which is an issue with MCP as well. Every time agents negotiate how to work together, they're burning compute, they're burning tokens, they're burning time. And in a multi- aent system, the cost will compound. So you need really sophisticated optimization strategies to keep the system efficient and performant. Unlike traditional software where we can optimize specific pathways, agent interactions are dynamic. They're unpredictable and it's more complex to optimize. Third, security remains a nightmare. I continue to just cry and pray for my friends who work in security because agentto agent interaction layers a whole new set of vulnerabilities. You need authentication, you need authorization, you need audit trails. Uh implementing all of this without destroying the flexibility that makes agent collaboration special. That's a non-trivial challenge. It's really tough. And what's what's interesting about this is that yes, these are all real challenges. They all will need to be addressed, but they're also inherent in what's being built here. They're also features in a sense. We are being forced to rethink fundamental assumptions about how software should work. In traditional software, we would optimize for that predictability. Every pathway would be known. Interactions would be defined. All of the outcomes would be mapped out. We would build Salesforce. I kid. I kid. Uh but in an agent-based system, we have to optimize for adaptability and flexibility. That's kind of the point. You want to optimize for moving intelligence from the human layer down to the agent layer. We aren't going to be able to predict every interaction in that world. We're going to have to be able to build systems that can handle emergence. And that's a really profound shift. And this is why the combination of model context protocol and A2A is so profoundly powerful. MCP gives agents the ability to understand and to use tools. A2A gives them the ability to work together. When you put that all all together, when you combine it, you're creating the foundation for truly autonomous software systems. So if we go to a concrete example, let's say you're building a system that helps with call it sales ops. In a traditional architecture, you'd have to explicitly program all the workflows. You'd have to qualify the leads, when to follow up, how to route different types of inquiries. It would all have to be hard hardcoded. Let's layer on some of that agent complexity now and see what happens. With MCP, you can give an agent access to your CRM tools, your email systems, and your analytic platforms. It then figures out how to use those tools to accomplish the task. Now, with A2A, something more magical happens. Your sales agent can discover and collaborate with other specialized agents. Maybe there's an agent that's really good at writing email copy, or another that's expert at pricing analysis, another that specializes in calendar scheduling. Instead of programming how those capabilities interact, you let the agents figure it out. They discover each other's capabilities and negotiate on collaboration and dynamically form workflows based on the specific needs of the situation. If you look at A2A specs, you can see how carefully it's been designed to make this kind of collaboration practical. It builds on existing standards like HTTP, JSON RPC. It supports longunning tasks and different modalities. It's designed to be observable, which you definitely need. It's designed to be debugable. Uh, and critically, I think especially if it's going to work with MCP and kind of the movement there. It's designed to be open. This isn't just another proprietary standard, it's supposed to be an invitation to reimagine a Gentic software. I think what we're watching in real time is the emergence of a new kind of software architecture, a new software paradigm. One where the boundaries between systems become much more permeable which introduces, as I called out, lots of security issues, but it also introduces a lot of opportunities. Functionality isn't just called, it's negotiated. Now, intelligence isn't just a feature, it's sort of in the fundamental substrate. We are delegating to intelligence instead of delegating to software. And that's a fundamental shift. Yes, there's big challenges ahead. Yes, we're going to discover whole new classes of problems, whole new classes of frankly headline and defining issues. Uh, and that's okay. That's exactly what makes this exciting. We're not just adding new features to the same old software. We're fundamentally rethinking what software can be. And so to me, like if you think about a world where we can combine MCP, we combine A2A, this is the beginning of truly automated software systems. And I think that's going to be a massive deal. I think that's going to change everything. What do you think?
