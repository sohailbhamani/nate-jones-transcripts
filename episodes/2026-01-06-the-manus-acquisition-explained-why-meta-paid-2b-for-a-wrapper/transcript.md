---
title: "The Manus Acquisition Explained: Why Meta Paid $2B for a \"Wrapper\""
video_id: "qw7HDITpTR4"
youtube_url: "https://www.youtube.com/watch?v=qw7HDITpTR4"
publish_date: "2026-01-06"
duration: "11:21"
duration_seconds: 681
view_count: 17880
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI agents"
  - "agentic AI"
  - "AI automation"
  - "Meta acquisition"
  - "Manus AI"
  - "Claude Code"
  - "AI strategy"
  - "large language models"
  - "LLMs"
  - "prompt engineering"
  - "future of work"
  - "AI tooling"
  - "GenSpark"
  - "task automation"
  - "AI workflows"
  - "OpenAI"
  - "Anthropic"
  - "AI agent frameworks"


# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Founders"
entities:
  companies:
    - "OpenAI"
    - "Meta"
    - "Twitter"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Make"
    - "Artifacts"
  models:
    - "Llama"
concepts:
  []
summary:
  - "# The Manus Acquisition Explained: Why Meta Paid $2B for a 'Wrapper'

Meta just paid over $2 billion for a rapper named Manis"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "artifacts"
  - "claude"
  - "claude-code"
  - "coding"
  - "deep-dives"
  - "frameworks"
  - "make"
  - "meta"
  - "openai"
  - "twitter"
---

# The Manus Acquisition Explained: Why Meta Paid $2B for a "Wrapper"

Meta just paid over $2 billion for a rapper named Manis. Not a model, not a breakthrough in reasoning, a rapper. And ironically, even though I say it's a rapper, I do think it was worth every penny. And I think it was worth every penny because of the characteristics of the agentic harness that Manis has been able to create. So, there are two kinds of agents in the market right now. Most AI agents are really good at starting something. They'll produce a plan. They'll draft an outline. They'll open up tabs. They'll generate a half-tonon artifact and it looks great, but then they can't finish. Manis has been the flagship for finish what you start for agents that actually do the work and that is a wide range of work, right? So they are able to do research. Manis can do coding, it can do data analysis, it can create artifacts, it can build websites. And the the important thing, the reason markbot is really not that menu of capabilities. It is that they have discovered an interaction pattern that scales generally. You give Manis a goal, it runs a long loop of tool calls and it's comes back with a complete result. That is not as easy as it sounds. And Meta clearly felt like the team was on to something special because they absolutely bought. And you might think, well, how do you know that they're using a special agent harness or how do you know that they're actually good at what they're doing? Ironically, I think this supported their valuation. The Manis team disclosed a lot of this in a late summer blog post about how they built long-running agents successfully and a lot of what they did subsequently became best practice across the community. This is a case where you might think transparency betrayed the secret sauce. But I think what it really did is it showed Zuck that this team innovates. This team is able to pay attention to details and this team can execute against very hard problems. And so in their blog post, they talked about stuff as nerdy as how often you hit the KV cache in order to reduce the cost uh and and latency of your model. KV cache is key value cache basically refers to the idea that you're not going to recomputee the input context. Every time you generate a new token, you're going to hit a cache for it. Well, when you have a very large input cost or a large input string length, a lot of tokens you put in, which often times with aentic artifacts, like you're putting in a hundred times more information than you're getting out. Well, in that situation, you want to hit the cache infrequently in order to reduce the cost, but you have to do so really intelligently. And so, the Manis team pioneered a lot of different techniques for that. And they also pioneer techniques that keep the agent focused on very long tasks that involve lots and lots and lots of different tool calls, lots of working out obstacles. Part of how they do that is they ask the agent to go back and revisit and rearticulate goals over time. So there's a lot of other things we can get into. They pioneered some really interesting stuff around restorable compression, talking about how you can use a file system as a persistent external memory and how the agent can write to that file system, drop stuff out of the context window, and then come back and recover it. And so if I'm Zuck and I'm looking at that, what I see is less today's solution for today's harness and more this team can innovate in the agentic space. They can build really cool and necessary agentic harness innovations that get work done that clearly are being shown by the market to be worth purchasing. And that's what Meta needs, right? Meta has had real trouble with their last LLM launch. The LLM itself was reported to have fudged Ben benchmarks by Yan Lacun, which is publicly embarrassing to Meta. Meta has an entire new team working on the next iteration of Llama, and they need to not fall behind on the usage of the model, which is exactly where Manis shines. Manis shines as a harness that wraps around a model and makes it useful. Now, you might wonder where in meta, what internal tool is Zuck thinking of here? My own best guess is ads. That's always how Meta's rung the cash register. That's how they've lived and breathed. And my suspicion is they want an automated ad builder a lot like this tool that you can sign up, spend a certain amount on, and it will just build your ads for you that you can then execute and run. And in fact, Meta will just optimize your campaigns for you. And that aligns with the public declarations that the Meta team has made that they really want to be in a position where all you have to do to advertise on meta platforms is have a wallet. And if you can pay, Meta can do all the rest. Ad creation, ad spend, ad optimization, campaign creation, segmentation, etc. This is a key part of that. Now, I will say I don't think it's going to be trivial to take the innovations that Manis created on their own as a tiny startup and integrate that into Meta. If I had to put a probability on that being successfully done this year, I gotta be honest with you, I'd put it at less than 10%. It is very, very difficult historically for a large company to take an extremely successful small company, take those lessons learned, and scale them into what that large company is doing in a way that multiplies impact. We will see, but my own guess for now is that Manis will continue to run. It will probably get pulled into Meta's data policies somewhere over the next two or three months, which is why anecdotally lots of folks are running away from Manis now to get ahead of that. And in the meantime, they're going to try and launch something, I would guess, around ads sometime in the new year. We will see. Now, if you've been using Manis, what are your alternatives? The answer is it's really tough to find, but I'm going to give you three different alternatives, and I'm going to tell you really honestly what I think of each of them, where I think they're at, so that if you want to choose something that isn't Manis, that isn't owned by Meta, you've got choices. The first is Claude Code. Claude Code is not really primarily a web-based agent. It is becoming very rapidly a generalpurpose agent with its roots in the terminal. It's designed first to help you write, edit, and reason about code over extended loops. But it turns out that because it can now touch your browser through the cloud code extension, because it can now touch your files, it can do a lot more than that. And so people are able to do a lot of finishing work or building work that involves any kind of software, but also that involves web research that involves docs. I saw someone who was using Claude Code to uh get a discount on their Comcast subscription because Claude Code was able to autonomously chat with a Comcast representative and get the discount for them. Claude code is one of those general purpose tools that I think we're just now beginning to get a sense of how wide it runs. It has a very similar harness to Manis in the sense that it's a tool call on a loop. It's absorbed some of the best practices or independently invented some of the best practices that Manis talked about in their late summer blog post around sort of writing good goals into a markdown file adding skills in more recently which is definitely a cloud code innovation and even more recently than that adding in some nativebuilt eval looping. Uh, I don't know if you saw, but there was a lot of discussion on Twitter over the Christmas break about the Ralph Wiggum Eval loop, which is not super fancy. It's basically just a script that feeds back the prompt and asks the model if it's done until it's actually done. So, Claude Code is one option. It does require familiarity with a terminal. I would say it skews a little bit more toward code than Manis does. Jen's Spark is closer to the Manis vibe in the sense that it take takes the idea of like busy work like documents, slides, sheets, research and frames that as a problem that a super agent inside a browser can go and tackle. It is probably the closest one to one comp with Manis right now. You will have to evaluate for your own work whether Gen Spark is as good at finishing as Manis. Having played with both, I found Manis a little bit more reliable. But I'm sure the Gen Spark team has had a fire lit under them postacquisition and we may see that shift soon as they get I would expect a fair bit of incoming business from folks fleeing the Manis acquisition. The last one I want to highlight is very new. It's still in alpha. It's called Do Anything. Uh it's at do anything.com. It is the most directly agentic platform of the three. It explicitly advertises that its agents can connect with 10,000 plus tools over thousands of APIs. The agents have names. They have email addresses and it's specifically asked during signup for you to set a very big and ambitious goal that your agent will work on for a long period of time. Sort of like Manis, it's pay as you go. You pay the tokens for what you want to get done. The goaling aspect is a bit different from Manis. Manis has advertised itself as get this task done completely, like build the slide deck and get it all the way finished. Well, do anything is advertising more like start a business for me, right? It's it's a order of magnitude or two bigger goal. And what I found when I played with it is that it still has trouble with the finishing aspects. I did I gave it a big goal. I asked it to start a business for me. And what it came back with was a lot of thinking, a lot of researching, a lot of planning, but then it wanted me to do a lot of work. And so I think that the team at do anything is still working out the kinks around what full endto-end execution looks like. And they are aiming at a bigger goal than Manis has. partly because they anticipate gains in model capability that will make that kind of larger starter business goal viable in 2026. So they're aiming at where the puck is going. Ultimately, I think Meta bought Manis because reliable finishing is a scarce commodity. You can think about it like this. Meta may have a team that is building a model. Let's say models are like car engines. They're building a new car engine. You have existing car engines. Claude is a car engine. OpenAI has car engines in Codeex in Chad GPT and others. But you need a car to go anywhere and the car is the agent harness and what the manis team is really good at is building the car and we are all discovering together what a good agent harness looks like. I think claude code for what it does is a very strong agent harness. The codeex agent harness is very good at a different aspect of code quality, code review and code construction. It's really designed on a slightly different angle than claude code is but it's also very strong in its own way. And I think we're going to see lots of other agent carnises coming as well. And my takeaway from all of this is maybe we should stop thinking about who has the smartest model here and maybe we should start asking ourselves what does it take what are the best practices it takes to build an agent that actually finishes the work it sets out to do. What is the right size goaling for that agent? I think do anything definitely challenges our thinking there. And how do we look at the details the way the Manis team looked at the details when we're constructing our agentic harnesses so that we're actually able to build something that does really useful work in a token efficient or costefficient way. That's harder than it looks and I think that is the heart of why Zuck decided to go with a acquisition rather than just trying to hire for this. This is not necessarily talent that it is easy to find in the market at this point. So that's the story on the Manis acquisition. I'd be curious what your thoughts are, whether you're going to still use Manis after the acquisition, whether you have another tool you're jumping to, and if so, what that tool is. I think this is going to be a year when harnesses are in a sense more valuable than the models underneath them. And that's one of the big shifts in late 2025 that countered the conventional wisdom of early 2025 when everyone thought the models are going to eat everything, the harnesses mean less. Well, as we built agents more and more, the harnesses mean more and more and more. And that's what we're seeing with this acquisition of Madness. Tears.
