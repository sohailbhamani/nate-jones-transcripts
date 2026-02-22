---
title: "I've Built Over 100 AI Agents: Only 1% of Builders Know These 6 Principles"
video_id: "kWeLc-Dda94"
youtube_url: "https://www.youtube.com/watch?v=kWeLc-Dda94"
substack_url: null
publish_date: "2025-09-23"
duration: "11:37"
duration_seconds: 697
view_count: 12640
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI strategy"
  - "AI agents"
  - "LLMs"
  - "large language models"
  - "prompt engineering"
  - "automation at work"
  - "agentic systems"
  - "stateful intelligence"
  - "context preservation"
  - "bounded uncertainty"
  - "deterministic wrappers"
  - "capability based routing"
  - "reasoning quality"
  - "multi agent health"
  - "continuous input validation"
  - "post production QA"
  - "OpenAI Responses API"
  - "token budgets"
  - "auditability"



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Agents"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Product Managers"
entities:
  companies:
    - "OpenAI"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# I've Built Over 100 AI Agents: Only 1% of Builders Know These 6 Principles

We are going to talk about the six principles for AI systems that I wish everyone knew"
keywords:
  - "ai-agents"
  - "ai-news"
  - "career"
  - "coding"
  - "frameworks"
  - "make"
  - "openai"
  - "product-management"
  - "tutorials"
  - "workflows"
---

# I've Built Over 100 AI Agents: Only 1% of Builders Know These 6 Principles

We are going to talk about the six principles for AI systems that I wish everyone knew. I've been building Agentic systems. I've worked with teams building agentic systems. What I see people miss is what we're covering here. And these are principles you can scale regardless of whether you're building a system for a 100 agents or just one agent. Principle number one, you need stateful intelligence. In other words, context preservation is a core principle of good AI architectures. And that is so different from what we learned when we were learning how to build systems in the when we were taught stateless services matter which is a fancy way of saying you need to have a clean start with anything because it enables easy scaling. Now AI systems require context and learn behaviors and those disappear on a restart. That is why the new OpenAI responses API is stateful. It's why it preserves context that they deliberately added that in because it is so important to have context preservation as an architectural component of agentic workflows. And I wish that people understood that because everything else gets easier if you can retain context in a way that's intelligent. So much of good agentic architecture is just good context engineering and good context preservation. It's not rescending the same tokens. You don't you don't have to send again. That's wasteful. So the first principle is stateful intelligence. You want to make sure that your intelligent systems recognize and preserve state in ways that are meaningful to the agent. The second principle is bounded uncertainty. So we're used to deterministic systems. Traditional engineering has the same input with the same output and very predictable testing which is why most QA is before launch. The new model you have to bound uncertainty. And so you have to essentially put rappers that are as deterministic as possible on top of probabilistic cores. And so you have to do things like mess with the API and turn the temperature of the LLM down to zero and define your inputs extremely precisely in the same sequence every single time so that what you get back for order 1 2 3 when you make a query is always the same. That is a whole another level of engineering that we're we we're not used to, right? Like traditionally you didn't have to think about whether the program would respond to the same input with the same output every time. It just always did. you could worry about other things. We don't live in a deterministic world anymore. We have to engineer deterministic bridges on top of probabilistic cores. Our world is running on probabilistic cores now. And not enough people have sort of fully realized that we need to bound uncertainty and it's part of our fundamental role. This changes how engineers evaluate. Engineers need to spend a lot more time from a data science perspective understanding what probabilistic metrics look like in production, not just deterministic metrics. We also need to have much more investment in QA post production because QA needs to be able to measure events that are occurring in production pipelines that may not be in line with expectations, that may be edge cases, that may be things that break our expectations of what works and what doesn't. We need to move from an assumption that our world is just building these deterministic blocks to the assumption that we are working with probabilistic systems that need continued sustained operation after we launch. And so we will have to go back in and we will have to measure. We will have to pay attention. We will have to maintain not just because there are deterministic bugs, but because our job is to continue to bound uncertainty as models drift over time, as perhaps we get different inputs over time, as we have different models being swapped out, as context emerges and changes in our context structures. All of those things shift how our production systems behave in ways that weren't true when we were in a deterministic output world. That's number two. Number three, fail fast design. We assumed in the past that if something crashed on error and it had a clear failure mode, then we were doing our jobs because we could immediately kill that micros service and restart it and we didn't have to have it sort of slowly dragging down the rest of the system. Now we actually have failures that are harder to detect. AI can fail by hallucinating. AI can fail by drifting. It can still be functional but be completely wrong. This is not a failure mode we're used to. We need intelligent failure detection. We need the ability to monitor reasoning quality, not just system health. And how you measure that is going to depend on the kind of inference you want to build into your agentic system. But you got to measure it. You've got to be able to detect failures that occur that are not just catastrophic program didn't want failures. And you have to build your system not from the perspective of what would happen if the whole thing went down, but from the perspective of how can the system work well if it's difficult to detect a degradation in reasoning quality. You need to assume that you are moving from a fail fast world to a subtle failure world where the failure is going to be hard to detect. And so you need to think a lot about how you monitor quality in that world. And that's another huge shift for engineers because they're used to very simple failure modes and making sure that they have like a really clean break and there's no massive dependencies if something goes down and they could bring it back up. Not anymore. You can have things that are running in production that look successful by most deterministic metrics that still don't work. Next principle, this is number four. Uniform load distribution is the old way of doing things. We had identical nodes. They handle identical requests. They've built out systems like this and different requests all get fed the same way because basically no matter sort of what device you're on, you're getting the same experience. That is not true anymore. Different requests to the system in an agentic system can mean dramatically different computes, hundreds of multiples of different computes. A high inference compute request can be thousands and thousands and thousands of tokens. and you can serve a low inference compute request in 1/100th of the space like it's a very token efficient request. So you need to think not about identical nodes and how you uniformly distribute a load that you presume is consistent. Instead think about capability based routing. Think about how you rate route based on task complexity and the confidence that AI has in a particular problem space. Is AI going to have to burn a lot of tokens understanding their request? Is it complex? So we need to route it differently than if AI understands what's going on. It's a very low inference task. So again, we're we're changing the way we think. It's not about distributing massive consistent load evenly across a bunch of identical nodes. It's about understanding the differential capabilities of your nodes and making really really smart choices about where you put the capabilities you have. Where do you burn the tokens with a smarter model? It's a new thing, right? We have to think about routing differently. We have to think about routing intelligently. There are people who are building agentic systems with reasoners just to solve this problem. Principle number five is binary health state. So we're used to system up system down. Again I want to call out for you that it is not that simple in an agentic system. You can have system up system down and you can have a lot of complex states in between when you have a multi-agentic system. I talked earlier about the idea that you can have a fail fast design that gets to intelligent failure detection and how you have to understand reasoning quality. This is sort of the next level of that. In this case, it's a multi- aent system and you have to understand that the system can be up and partially functioning. The system can be up and not functioning. The system can be up and some of the handshakes between the agents aren't working, but you still can get most of the functionality there, but maybe there's degraded intelligence. What I'm saying is that you've moved from a black and white world to a world where there are lots and lots of shades of gray, maybe 50 shades of gray, and you have to figure out what to do with measurement, with quality, with system health when it's that complex. And the more agents you add to the system, the more complex it is to measure system health. And so you are the one that has to track the outputs coming through, the quality of those outputs, understand enough of the audit trace to understand where the agents are breaking handshakes or where the agent uh reasoning traces aren't working well or where there's degradation in outputs or maybe where there's a context drift somewhere to pin down what's going on. It is a much higher bar for auditability than it used to be. The last principle I want to call out is input validation. So before you validated once, right? If you were doing inputs, it was like we need to validate at the gateway. It goes into the micros service and we're done. So far so good. These days it's not the same. These days you have to validate throughout the conversation state. You have continuous validation. You you have to understand that AI behavior depends on accumulated context. And so you need to validate as you go or else you're going to not know where you are going off the tracks. And so you need to think of it almost as a continuous edge. You need to think of it as each turn in the conversation is potentially a step that requires some validation of conversation state. So you know there was a checkpoint there and it worked. Otherwise it's very very difficult to debug these systems. If all of this sounds difficult, it should. It is much much harder to design healthy agentic AI systems than it was to design traditional software. And we have had very very few conversations about how traditional engineering principles do not work in the age of AI. I hope that this breakdown has helped you to see how some of the traditional principles we have which are not entirely dead. If you're still building traditional software, these are still good principles and many of our systems are hybrid systems. And the post that I'm writing on this sort of goes into this in much more depth. But you sometimes have to build systems that are both traditional deterministic software systems and AI systems. In fact, most of the ones that I build end up being hybrids. And so you have to be smart enough to take traditional principles like stateless services where they matter for deterministic software and also take stateful intelligence which is the AI principle and apply that where it matters for designing agentic systems. We need new schools. We need new principles. We need new understanding of how AI systems truly scale. And I hope that this breakdown has helped you to get a sense of what some of those new principles are, of how to actually construct systems based on principles that scale, not just based on tactical tips. So there you go. Those are my six principles for AI. Stateful intelligence. Bound that uncertainty. Make sure you have really intelligent failure detection. Assume you're going to have to route based on capability, not just uniform load distribution. Make sure that you have decision quality and reasoning pattern health states across multi-agentic systems. You're going to have to have very detailed audit tracking and then assume you have to validate your inputs throughout the conversation and not just as an input. If you put all of those together, you are going to be much more likely to get an agentic system that actually works. Best of luck.
