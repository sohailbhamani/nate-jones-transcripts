---
title: "Claude Code Wiped 2.5 Years of Data. The Engineer Who Built It Couldn't Stop It."
video_id: "8lwnJZy4cO0"
youtube_url: "https://www.youtube.com/watch?v=8lwnJZy4cO0"
publish_date: "2026-03-16"
duration: "21:30"
duration_seconds: 1290
view_count: 21980
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  My site: https://natebjones.com
  Full Story w/ Prompts: https://natesnewsletter.substack.com/p/your-ai-agent-just-mass-deleted-a?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  ___________________
  What's really happening with AI agents when vibe coders try to scale their builds? The common story is that better prompting solves everything — but the reality is that agents introduce a supervision problem, not just a prompting one.

  In this video, I share the inside scoop on the five management skills every vibe coder needs to survive the agentic era:

  - Why version control is your most critical safety habit now
  - How context window limits silently destroy long agent runs
  - What standing orders do that repeated prompting never will
  - Where small bets beat sweeping changes every single time

  Builders who treat AI agents like a powerful but unsupervised contractor — without save points, scoped tasks, or persistent rules files — are one bad session away from losing real production work.



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Tools"
difficulty: "Intermediate"
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
    - "Meta"
    - "Microsoft"
    - "Apple"
    - "GitHub"
    - "Stripe"
    - "Cursor"
    - "Lovable"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Copilot"
    - "GitHub Copilot"
    - "Cursor"
    - "Make"
    - "Artifacts"
  models:
    []
concepts:
  []
summary:
  - "Chapters:

  0:00 The wall vibe coders are hitting in 2026
  1:45 Agents vs"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "apple"
  - "artifacts"
  - "career"
  - "claude"
  - "claude-code"
  - "coding"
  - "copilot"
  - "cursor"
  - "deep-dives"
  - "frameworks"
  - "github"
  - "github-copilot"
  - "google"
  - "leadership"
  - "lovable"
  - "make"
  - "meta"
  - "microsoft"
  - "openai"
  - "product-management"
  - "prompting"
  - "startups"
  - "stripe"
  - "tutorials"
  - "workflows"
---
  Chapters:

  0:00 The wall vibe coders are hitting in 2026
  1:45 Agents vs. vibe coding: it's a supervision problem
  3:20 The 5 skills overview
  4:00 Skill 1: Save points and version control
  6:20 Skill 2: When to start fresh (and the advanced fix)
  8:40 Skill 3: Standing orders and rules files
  11:10 Skill 4: Small bets and blast radius
  13:56 Skill 5: Questions your agent will never ask
  17:20 When to bring in a real engineer
  19:00 The wall is a management problem, not a code problem

  Subscribe for daily AI strategy and news.
  For deeper playbooks and analysis: https://natesnewsletter.substack.com/

  Listen to this video as a podcast.
  - Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  - Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "AI agents"
  - "vibe coding"
  - "prompt engineering"
  - "AI strategy"
  - "automation at work"
  - "future of work"
  - "upskilling with AI"
  - "Claude"
  - "Claude Code"
  - "agent management"
  - "context window"
  - "version control"
  - "rules file"
  - "Git for builders"
  - "AI coding tools"
  - "AI agents for beginners"
  - "vibe coding mistakes"
  - "AI agent workflows"


# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
  - "Founders"
entities:
  companies:
    - "OpenAI"
    - "Google"
    - "Meta"
    - "GitHub"
    - "Stripe"
    - "Cursor"
    - "Lovable"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Copilot"
    - "GitHub Copilot"
    - "Cursor"
    - "Make"
    - "Artifacts"
  models:
    []
concepts:
  []
summary:
  - "We can use really any textbased tool to build stuff now"
keywords:
  - "ai-agents"
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "artifacts"
  - "career"
  - "claude"
  - "claude-code"
  - "coding"
  - "copilot"
  - "cursor"
  - "frameworks"
  - "github"
  - "github-copilot"
  - "google"
  - "leadership"
  - "lovable"
  - "make"
  - "meta"
  - "microsoft"
  - "openai"
  - "product-management"
  - "prompting"
  - "stripe"
  - "tutorials"
---

# Claude Code Wiped 2.5 Years of Data. The Engineer Who Built It Couldn't Stop It.

Vibe coders everywhere are hitting a wall. They know how to vibe code. They know how to build stuff. We can use Lovable. We can use really any textbased tool to build stuff now. And so folks are getting into Claw. They're getting into Claude Code. They're getting into codecs. They're getting into shipping artifacts through chat GPT. They're getting into Replet. I could keep naming tools for half an hour. The point is that you are shipping software based on your text. And that was the story of 2025. But so many vibe coders are coming to me now and saying I feel like I'm missing a set of skills. I feel like I don't have the skills for the agentic world. Like agents caught up and now I don't know how to build software again in 2026 because vibe coding isn't how you do it. It's like vibe agenting but that's not a word. How do you build software with agents? How do I take my VIP coding skills and transfer them? I'm not a software engineer. This video is for you. If you're someone who described what you wanted and AI built it and you shipped it, maybe you have real customers now and maybe things are starting to break in ways that better prompting alone can't fix. Maybe you have agents ignoring your instructions. Maybe you have hours of work lost to a single bad change. Maybe you've hit the wall between building a product with AI and running one. And almost nobody is talking about the specific skills that get you over that hump. This is all about that. This is not about learning to code. That is not a skill we're really teaching in 2026 in the same way anymore. This is a video about the skill of learning to manage the agent that codes for you. That is the skill of 2026. And yes, you really can do anything non-technical if you can get an agent to code for you. That is why people are calling cloud code AGI. That is why OpenAI is seeing rapid adoption with codecs. That is why even Google went out and shipped their Google Docs to the command line interface recently. And before you wonder, is this a real concern? Like, do I have to worry about managing my agents? I will point out to you that SummerU, a meta security researcher, ended up in trouble because OpenClaw accidentally deleted a large portion of her email inbox in February 2026. Despite explicit instructions to confirm before acting, the agent decided to speedrun deleting emails. and that continued after she sent commands to stop and she described having to run to the Mac Mini and unplug it to save even a part of her email archive. Agents are not as easy as vibe coding and you need to think differently when you manage agents. So, let's get into it. The first thing to realize is that your vibe coding tool may have become agentic when you weren't looking. So, Claude Code, Cursor, OpenAI's Codeex, GitHub Copilot, they don't just suggest code, they go ahead and execute it. They read your files. They make changes directly. They run commands. They install things. They iterate against their own mistakes. If you give a task and the agent works autonomously for a long time for 10, 20, 30, 40 or 56 minutes as Chad GPT 5.4 did during a recent eval I ran, then you are working with an agent and you have to act like that. You have to think like that. You have to work differently than when you vibe coded. And so when you ask an agent to add a feature that lets customers leave reviews, that agent is not just going to look at one block of code and hand you a block of code. You might wonder, "What's the concrete difference? I get the feature either way." Here's the difference. In 2025, when you ask an agent to add a feature that lets customers leave reviews, so often you would get a single block of code from these different tools. Now, the agent is going to read your database. It's going to create new tables. It's going to build the interface. It's going to add form validation. And it's going to save the results. At least eight steps, maybe more, depending on how the agent designs the system. And if step four goes wrong, steps five through eight make it worse. I want to be really clear here. Vibe coding was a lot about prompting. Agent management is not first a prompting problem. It's a supervision problem. And the difference between vibe coders who keep shipping and the ones who hit a wall is exactly this shift from describing what you want to managing the thing that builds it. And you don't have to become an engineer. You just need to become a competent manager of an engineer with a short-term memory that happens to be AI. Let me give you an analogy. If you're a general contractor working on a house, you may not be laying the brick for that house, but you know what a straight wall looks like. you know which walls are loadbearing and you know that you shouldn't tear out the plumbing without turning off the water. I want to give you those kinds of skills. Think of the work you're doing with agents in 2026 as now you're a general contractor and you're managing a team of agents building software. What are the skills you need to be an effective manager? I'm going to give you specific ones, five of them, and none of them require writing code. Skill number one is as old as 1990s video games. You have to find your save point in the game. Say your agent broke something last week and you couldn't get back to the version that worked. Maybe it was the login page. Maybe it was the checkout flow. You described the problem. It was a big problem because agents can tackle big problems now, not like 2025. And the agent did try to fix it, but it made it worse this time. And now you're 3 hours deep in a conversation that's going in circles. The version from before the agent touched anything, you don't know where it went. It looks like the agent overwrote it. This is one of the most common disasters in VI coding in 2026. And it has a solution that every single developer uses. Version control. Think of it as save points in a video game. Every time your project is in a working state, save a snapshot. That snapshot is permanent. No matter what your agent does next, no matter one command and you're back to the version that worked. This is why a tool called Git matters for Vibe Coders in 2026. It's not a new tool. It's just how developers do this. And yes, if you're wondering, oh my gosh, I'm taking notes. How do I remember all this? There's a whole guide on the Substack. I'll get you all set up. Don't worry. Even if you've never coded now, learning the five or six things you actually need to do and get. You can head over to the Substack to do this or honestly, you can read this transcript to Chad GPT or Claude and tell them to explain it to you. It's not that difficult and I won't take all afternoon on it. What I am going to tell you is that the habit of saving a snapshot is critical and it is absolutely worth a couple of hours or an hour or 20 minutes depending on your technical competency to learn what git is and figure out how to use it so you can save a snapshot. You have got to use a tool that gives you a save point and yes it exists and I am asking you if you are working on something make this a priority ahead of the next feature request you want to build before your next change please. I am trying to save working software here. I do not want you to go through the pain of losing a production database, which is what I heard a senior developer tell me that happened when they ordered their agent to make a seemingly minor change and there was no versioning and it's gone. Now, they were able to recover. That's fine. But the point is you don't want to be in those shoes. Skill two, learn when to start fresh. This is especially important with agents. Let's say your agent is brilliant for the first 20 minutes or 40 minutes or hour of the project. It seems to understand things. It follows your instructions. It makes the right changes and then somewhere around message 30, it just starts ignoring things you've told it three times. It rewrites code it already wrote. It introduces bugs into features that were working. It feels like it forgot everything. Well, it did. Literally, agents have a fixed amount of text. They have a context window. Everything you've said, everything it's said, every file it's read, every error message takes up space. And when that space fills up, older information gets compressed or dropped. And your instructions from the beginning of the conversation, well, they're gone now. The architecture understood an hour ago, it's also fuzzy. There are two fixes. There is an advanced mode and there's a simple mode. And I'm going to describe both very, very clearly. We'll give you a guide for both that's very simple. It will depend on you what you want to do. The simplest fix is to start fresh. But here's the thing. Starting fresh, everyone understands how to do that. You just start it over again. Sometimes the job is so big you're going to run into this issue again. And then you need the advanced fix. And the advanced fix is to set up proper infrastructure for your AI agent, which means you have to have a workflow file where the agent knows what it's doing and has logged that as a workflow. A planning file potentially, a context file where the agent can read the context of what it's trying to do when it reinstantiates when it wakes back up if you start a fresh run, and a task list that the agent has to burn down. Are you getting the idea? Basically, you need to build a scaffold of documents around the agent so that if the agent is killed, if the agent has too much context, it can't work anymore and you have to restart it. You can look at the documents that reflect the process that happened and start again at that point. It's sort of like having a save point not for software, but for the agent run, the agent build. If your agent is 65% built, you'll want to pick up at the 65% build part if you can. And that takes some preparation and I'll cover in the substack, but it's totally worth it because it means you can build much much bigger things. This is a simplified version of the really fancy stuff that lets teams like Cursor and Enthropic code for weeks. And now we're getting to skill number three, and it ties right into skill number two. Your agent needs standing orders. Remember how I told you that you needed kind of a dock or something in the advanced fix for the agent? just running out of context and the docs would help the agent keep track of things. One of those docs that you absolutely have to have is what I call standing orders. Let's say you've told your agent always use dark mode for the interface as many times as you can think of and it keeps defaulting to light mode. You've explained your naming conventions. It ignores them. Every session seems to start from zero. Well, every major AI coding tool now supports something called a rules file. It's a simple text document in your project folder that the agent reads at the start of every single session. Think of it as your employee handbook. It tells the agent, "Here's what this product is. Here's how we do things around here, and here are the three things you keep getting wrong that I need you to stop doing." And yes, I I also use that tone when I write my version. So, Claude Code calls this claw.markdown. Cursor has its own format. There's also a universal standard called agents.mmarkdown that works across most tools. And the name doesn't really matter. the concept does. You need to have persistent instructions that survive across conversations. You know, the counterintuitive part about this is how you actually build it. You might think you sit down and there's a ray of light and you write a perfect rules file, but it doesn't work that way. You don't do that. You start with almost nothing. You just start with, hey, this is what the product is. This is what it's built with and maybe a few lines about things you've noticed. It's sort of messy. Then every time your agent does something wrong, you add a line to prevent it. Over a few weeks, the file becomes a very precise reflection of exactly what your particular project needs. And over a period of time, as it gets to be a longer file, you're going to figure out which lines are loadbearing, which lines matter if you drop them versus which lines don't. And so you can start to keep the file clean, too. Make sure that every line earns its keep. Ideally, you want to be under 200 lines, maybe even under a 100 lines, because the rules file does compete for the same memory all that conversation and work uses. So, if you get to a massive rules file that eats your agents ability to focus, it's kind of counterproductive. I will give you some specific examples over on the Substack, or frankly, you can Google around and find them. Skill number four is small bets. Let's say you want a big project done. Let's say you're asking your agent to redesign the order system for your product and you're a vibe coder and so you're saying do it all at once and they touched every file in the project and half of the features that went along with it broke because you know what it used to work and now it doesn't. You have no idea which changes caused which problems because the agent changed so many things at once. When one sweeping operation can affect everything, there's no way to isolate what's wrong. The concept we're talking about here is blast radius, which is what it sounds like. It's how much of your project a single change could affect. And here's the principle that makes AI assisted building for vibe coders in 2026 who are using agents actually feel safe. Give your AI agent a really, really well-defined, focused task. Do not try to give it a large sweeping change unless you are committed to a really, really good set of eval really good agent harness. And if you don't know what those words mean, then that is not for you. This is not because the AI is not smart enough to do big things, it is. It's because complex changes compound errors and you need better and better systems thinking to prevent those errors before they happen. And that compounds nonlinearly or exponentially, the bigger the change is. So step four of a 12stage change goes wrong. Steps 5 to 12 make it worse. But now imagine it's a 100 stage change. And look at how bad it's going to get. So before giving your agent a task, ask a question. How big is this? If it's small, if it's changing a color, if it's fixing a form, just get it done. It probably won't even take an agentic coding harness or memory or docs or anything. They're just going to do it. If it's medium, like adding a whole new feature, you may want to tell the agent to plan it into multiple features and ask the agent to execute it in pieces and validate completeness and hit a save point before going to the next feature. Because if you're verifying and saving along the way, you're less likely to regret your choices. And yes, this is our choices as people. I know we like to blame the agents, but we're the ones who are not managing them well. And this is my guide. If you've never managed agents before, this is going to help. And by the way, if you think I'm not a vibe coder, I just, you know, work with Claude for a living. Claude is an agent now. These are also things that help with stuff like powerpoints. I don't know how many times I have sat there and said, "Oh, you're trying to generate a 100 slide PowerPoint at once." Same principle here. It's not a small bet. Maybe we should ask Claude to just do 15 slides at a time. And it works. Small bets. Skill number five is about learning the questions your agent will never ask. All of the stuff I've talked about in the last four skills is about managing your agent directly. This skill is about managing what your agent builds because there's a category of dangerous problems your agent is never going to raise on its own and that frankly vibe coding tools of 2025 were too weak to deal with and so this is a new kind of problem for people who have been vibe coding. Let's say your app works great when you test it, right? You've gotten a few orders, everything is loading quickly, but your customers will end up submitting empty forms and clicking the buy button multiple times and pasting emojis into fields that expect numbers and generally using it like humans. The problem is this, the gap between it works for me and it really works for my customers who use it in all of the wild and woolly ways that humans use apps. That's where products go to die in that chasm in between. I cannot tell you how many times I've had a developer tell me, "Well, it works on my machine." Well, that's not the point. So, here's how to manage that with agents. You have three things that you need to demand in your files and in conversation. They're basically questions that your agent will not think of without prompting. And this is specifically for vibe coders trying to build apps. Number one, when something fails, you should instruct an agent to show a message, not a blank screen. Agents don't think to ask if the user needs to see something when there's a failure. They won't assume that. Payments can get declined. Servers can go down. Internet connections can drop. If your app doesn't handle these gracefully, your customer sees like a white page or a just a crash screen. Tell your agent every time the app communicates with a server. It has to handle failure with a very clear and friendly message, never a blank screen. Number two, please keep your customers data safe. Your agent, again, may not assume that they need to do that, but it's critically important, especially if you're dealing with paying customers on your app. Frankly, it's really important if you're dealing with your kids or your data on your app. Like, people who build family apps need to think about this, too. So, how do you protect customer data? You actually give the agent the instruction to look into rowle security. It's a kind of security where you're looking at the security of every single row in the database. I explain a lot more about it in the Substack post today, but the agent will know what that means if you say it because it's a very common software term. What you really want is to say with rowle security that each customer can only see their own data. You don't want any ad mixture between rows in the database. Then I have said this, but so many other people have said this. Never ever ever ever paste your secret keys into a chat with AI. Please do not do this if you don't know what a secret key is. It is something that is usually labeled secret key that is part of establishing secure connections with data. If you take that and it's a lengthy like 30 40 50digit hash string with numbers and letters and you think it's fine and you just stick it into the chat and say please develop with this you are running the risk of a database leak. It is a very risky thing to do. There are lots of other ways to deal with it. Many people have written guides. Yes, it is in my guide, too, but it's not the only place. You need to handle your secrets responsibly. And last, but not least, in your rules file for your agent, please, please, please add a rule that says never, ever log customer emails or payment information because you don't want to be doing that. You want to be in a world where payment is handled via like Stripe or API or something and you're not touching it. You want to be in a world where customer emails are not something you have to keep in a database securely and worry about whether or not you encrypted them well enough. You want to be in a world where you have like a sign-in with Google and it's just done. Third thing, your agent won't ask. Your agent won't ask about growth. You should tell your agent early what your growth expectations for whatever you're building are because sometimes the agent overengineers things and says your family app needs to support thousands of users. And sometimes your agent undergineers things and thinks to itself, eh, I don't need to do this critical security feature because they told me they have 300 users currently. If you expect your app to eventually get to a serious size, you should be telling that expectation to your agent because you will help it to build accordingly. Now, I would advise you here to get deeper on technical details than you might think you need to. It is worth getting a response from the agent, getting it explained like you're in high school by chatting with Chad GPT so you understand the technical term and then coming back and making an intelligent decision. You don't want to leave scaling to chance. The key thing to do is to set the expectation before the agent builds something so that the agent knows is it going to be for 10 users or is it going to be for 10,000. Finally, part of being good is knowing where to stop. Even in an agentic coding environment, please bring in a professional engineer when things start to get serious. Examples of things getting serious. If you're handling payments beyond basic checkouts for goods and services, if you're dealing with medical data, if you're dealing with children's data, if you're dealing with legal compliance, when your app is getting slow under real usage and you don't know why, when your codebase has gotten so messy the agent is struggling with it and you don't know why. This isn't a failure. If a non-engineer can build a product and maybe get real customers and then bring in an engineer to harden it for scale, you've already done something most startups never manage to do. You've proved the idea works before spending serious money on real engineering. And yes, real engineering still has a place even in the era of agentic development. A lot of my videos say that, so I hope that's not a surprise. Ultimately, the wall you are facing, if you're transitioning from vibe coding and you're wondering, how do I work with AI agents appropriately? That wall is not made of code. That wall is not something that you can't get through if you're not an engineer. I've outlined these skills because they really are management skills. Think of yourself again as a general contractor. You're constructing that house. You need to have safe points for the house where you can say, "Okay, the beam was put on wrong." That's not going to work. You need the ability to dig the foundation aresh if it's not going well. You need the ability to have standing instructions written clearly at the work site so people know what to do. You need the ability to work in small incremental features so you can say just do the counters today. And you need the ability to look around corners and ask the questions nobody on the work site is asking. All of these are management skills. You're just applying them to agents. In other words, the wall between building with agents and just vibe coding is management skills. And they are habits that you can practice. And if you start to practice them, a lot of what makes agents feel mysterious is going to evaporate. It's going to disappear because what we built in 2025 was good for the agents and the skills and the models of 2025. But the agents are now a hundred times more powerful. And a lot of the work we did on prompting is now necessary but insufficient for the power we're dealing with here. And so think of what I'm giving you as like prompting plus plus. Yes, prompting was great. Yes, you still need to prompt well. Not an excuse, but you have to think much more broadly to handle agents this powerful as someone who's used to vibe coding. I hope that this has been helpful and best of luck with what you're building. I'd love to see it. Please throw it in the comments so we can all see it and chat about it together.
