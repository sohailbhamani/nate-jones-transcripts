---
title: "Anthropic Ran 1,000 AI Agents For 8 Days. Yours Still Needs The Same Thing Explained Again."
video_id: "v5I0nOoqAV4"
youtube_url: "https://www.youtube.com/watch?v=v5I0nOoqAV4"
publish_date: "2026-11-20"
duration: "20:36"
duration_seconds: 1236
view_count: 415
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  How do you get long-running AI agents to do the work you actually want, without explaining the same thing over and over? OpenAI and Anthropic report AI agents working for hundreds of hours and for days. I break down what keeps those long runs on track, for you and for your team.
  
  Full post:
  https://natesnewsletter.substack.com/p/long-running-ai-agents?utm_source=youtube&utm_medium=video&utm_campaign=long-running-ai-agents-launch&utm_content=description
  
  Nate's Library MCP (every prompt kit and guide, inside the AI you already use):
  https://unlock-ai.natebjones.com/guides/how-to-connect-nates-library?utm_source=youtube&utm_medium=video&utm_campaign=long-running-ai-agents-launch&utm_content=description
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/?utm_source=youtube&utm_medium=video&utm_campaign=long-running-ai-agents-launch&utm_content=description
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening when an AI agent works all night?
  
  The common story is that longer runs just need a smarter model, but the real question is whether your agent has the current decisions, examples, and instructions behind the work.
  
  In this video, I share the inside scoop on long-running AI agents:
  - Why my research run produced a thousand questions I didn't need
  - How treating project information like code keeps agents on current decisions
  - What shared skills and permissions change when many agents touch the same work
  - Where to start alone with one job you keep explaining
  
  An overnight run can save you a day or cost you one, and the difference is the structure you give it.
  
  Chapters:
  00:00 OpenAI ran AI sessions for hundreds of hours
  00:52 An all-night run can leave a full day of cleanup
  01:25 My research run that went sideways
  02:04 The assignment was the problem, not the data
  03:27 Getting the right context in front of the AI
  05:14 Treat project information like code
  07:52 Skills built for the team, not for you
  10:57 Roles and permissions in a shared repo
  12:53 Avoiding collisions when agents share work
  14:39 How to judge whether it is working
  17:28 Start alone with one job you keep explaining
  19:20 Why team leaders need to see this
  
  Listen to this video as a podcast.
  
  Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

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
  - "long running AI agents"
  - "AI agents"
  - "OpenAI Codex"
  - "Anthropic"
  - "Claude Code"
  - "multi agent systems"
  - "AI skills for teams"
  - "how to get AI to stop repeating mistakes"



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
    - "OpenAI"
    - "Anthropic"
    - "Google"
    - "Meta"
    - "Box"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Gemini"
    - "Codex"
    - "Make"
    - "Projects"
  models:
    - "Gemini"
concepts:
  []
summary:
  - "On November 2nd, OpenAI reported that AI sessions had run for hundreds of hours finding and fixing problems in its new system for managing code"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "box"
  - "claude"
  - "claude-code"
  - "codex"
  - "coding"
  - "deep-dives"
  - "frameworks"
  - "gemini"
  - "google"
  - "make"
  - "meta"
  - "openai"
  - "product-management"
  - "projects"
  - "tutorials"
---

# Anthropic Ran 1,000 AI Agents For 8 Days. Yours Still Needs The Same Thing Explained Again.

On November 2nd, OpenAI reported that AI sessions had run for hundreds of hours finding and fixing problems in its new system for managing code. Meanwhile, yours and my AI, sometimes we still need to explain the same thing over and over and over again. We're a long way from hundreds of hours most of us. You're going to learn in this video how to get AI to do more of the work you care about correctly without constantly repeating instructions, without fixing the same mistakes over and over again. That's the key to successful long runs. Anthropic reported something very similar with Fable 5.2. This is not just an OpenAI thing. They had more than 1,000 agents working for 8 days to build a prototype operating system. Google, something similar, right? Gemini 4 Carbon just released and it's worked for days on hard engineering problems. We know these AI systems can work for a long time if we set them up right and that's what this is about. An AI that works all night can leave you with a full day of cleanup. You still have to check the price. You still have to fix what it promised. Still have to explain the decision you already made yesterday and I say this from experience. I have left AI running and been frustrated when it came back in the morning with something I did not ask for, when it overdelivered on a feature I didn't want, when it underdelivered on something I cared about, when it did not remember correctly how to implement a direction I gave it and I only realized later it was ambiguous. I don't want you repeating yourself. I don't want to be repeating myself. Now, I ran into this while building a set of questions to test AI on my own work. Codex found over 339 sources I was using and wrote over a thousand questions for me to think through. That's a lot, right? I told it to keep going and later an agent got stuck repeating the same work while trying to synchronize all of my files. By then, what I needed had changed. I wanted the 50 most valuable answers to my questions. I wanted stronger evidence. I didn't want to have a thousand questions to answer. I tried to make sense of the context, but ultimately I stopped the run and just the next agent a short note to make sense of all of that. This was not a data availability problem. The research was there. I had thousands of files on my computer. What I needed was a better structured assignment to have a long-running push like that actually make sense. I learned more about what was worth doing over the course of that run and the next agent needed more instructions before it did more work. And this is something I see as a persistent challenge as we drive bigger volumes of work. If an agent keeps following a decision that I don't even remember making earlier in a very large project, I end up paying twice, right? I pay often literally in tokens for the run and then I pay in time when I fix the result and I realize this wasn't what I wanted. And when you get into these very large projects where you're trying to understand things and you're trying to think through them and you don't fully know the answer and you need the AI to be a thought partner, it's really really important to pass on your evolving learning as you go to the agent. Now, if you want some help getting from where you are to there, you can subscribe to this channel and paid subscribers to my Substack can also grab my working context starter kit where you can get reusable files for keeping project information. You can keep your current decisions organized. You can basically get a starter kit to start thinking about this problem as being team-shaped, not individual-shaped. And I'll link that below. How do we get there? Part of this is really being disciplined about making sure that the right context gets in front of the AI when it needs to be there. And so by right context, I don't just mean the facts, although those are important. I mean the decisions you make along the way, examples that you develop as you think through the problem with the AI, instructions that evolve as you go when you change your mind so that someone joining your team, if you are in a team situation, can actually look at the record of these larger runs and see your particular perspective on these bigger projects for work evolving over time and they can come up to speed. This is actually how the labs work with newer employees to train them. They ask them to ask Codex, ask them to ask Claude so that they can learn from the existing data and context as it has evolved over time on larger projects and come up to speed as humans. Well, agents learn that way too. And so think about what you give your larger projects is not a one-time snapshot of your opinion, but something where you're going to have to give perspective over time to your AI in a way that it can read, in a way that it can understand so that it can drive that decision more effectively. It does not work in the example of my research project to just say, well, give it to another AI, give it to Claude, give it to Gemini, maybe that will work. The problem is really that the assignment wasn't structured correctly and we learned over time how to structure it better. I needed to be clear about what I wanted out of it. I needed to be clear about discovery phase versus refinement phase. I needed to pass all of that learning along with the work that I'd already done to another agent for another try. And so in that world, it is really really critical that you think about your project information like code. Think about putting it where agents can find it, putting instructions, putting checks for mistakes, putting evolving decisions as if their code in a repo where the agent can go and get it. Even if it has nothing to do with code, even if all you're doing is client proposals. You agreed on an offer and a price and the contractor's AI is using an old proposal as an example. The new draft might look good, right? But now you have a bad price in there. That's just an example, but I've seen over and over and over again that these kinds of versioning errors creeped in when you aren't disciplined and you don't treat even your non-technical information more like code. Now, why is this? Well, frankly, because in the era of Claude code that we all kicked off in January, LLMs are RLV are. They are trained on verifiable domains like code, treating a piece of knowledgework a lot like code so that you have it in a repo and the AI can traverse it and understand the files and everything that goes with it makes sense to an AI. It makes your work easier. And by the way, this has benefit when you have multi-agent systems. Let's say you're working on this, your colleague is working on this, your friend in another department is working on this. They all have different LLMs, different services. They're all working. If you are working against the same set of data in the same place, a repo if you will, you are going to be in a much better place because you can go and get that data regardless of the LLM you're using coming in and it's the same thing, which is why I really encourage teams who are thinking about doing this seriously to put skills and other things that they believe are recipes for using their data correctly, for preparing things in line with their brand guidelines, put those in the knowledge base itself. Do not depend on the best intent of all of us individuals to install the same exact correct skill. Certainly do not let everybody on your team write your own skills over and over again. That happens a lot and it's something that you end up having to undo over the course of disciplining and scaling AI systems because you essentially have a bunch of home brewed AIs that are going to have slightly different approaches to the problem and end up often not referring to the same data. So it's so so important to think of the problem space as a code shaped problem space and put the data that you are trying to tackle even for knowledgework in a central place that is structured so an agent can run across that, traverse it effectively. And by the way, when you start to think about the problem that way, you think about skills differently. Skills are often thought about as superpowers for me to use my AI with. They are more powerful if you think about them as superpowers that enable an AI, regardless of who is using it in the company, to use against the knowledge work that you have in a particular place. And so, the skill is a set of instructions for anyone coming in with any LLM to attack a particular kind of problem in a consistent manner. That is a very different approach. If we think of them as us-shaped, we are going to have lots of idiosyncrasies in the way we approach things. And so, skills are actually constructed very very differently when you think of them as first being repo-shaped, first being shaped against the problem you are solving as a company or a team, and only then as something that someone needs to be able to access and have their LLM attack. And so, you have a particular way of writing PRDs, you have a particular way of preparing proposals, you have a particular way of preparing decks. That is all a function of something that should be centralized, something that should be common. And it looks really really different when you're writing that so that any LLM or any agent running across it can use it against the data that is right next to it to do the work. And this allows you to do things like meta skills where you can actually have skills in the repo that are designed to facilitate the human workflows you care about, where you can have skills that prompt the agent to let the human know, hey, it's time for you to do an edit pass on this because I just saw a V12 dropped in and you need to have a look before we go farther. That's the kind of thing that assumes a multi-agent system and that you don't really get if you're thinking about this individually. And this approach, this centralizing data approach, which has a lot of ramifications I've been pulling out in this video so far, it's what allows you to catch these mistakes before they get to a customer. You don't need a manual for every single person to do their job for AI. The idea that the AI is a mini-me is not correct. Instead, you need to be in a position where you can all collaborate against the same data structures to do work that is consistent for the team and the company. And that allows a degree of human ownership and accountability. I know we've talked about agents a lot, but this actually facilitates our job because it allows us to focus on the value of the final deliverable instead of obsessing over whether we're slightly more productive with a different skill. And I do see a lot of skill theater. I see a lot of mini-me theater. I see a lot of people trying to talk about their personal setups being more productive when really simpler setups that just put the data in one place and that allow agents to attack that space and then focus on centralizing a lot of these skills that you need to go after these problem spaces and allowing those skills to facilitate workflows. That starts to scale and then you can focus on being accountable to the client, being accountable to the customer, so you don't get in a position where you say, well, the AI wrote that. It's not me. No, you wrote it. You own it. That's the kind of thing humans need to be doing more of. One of the other implications, so we've talked about sort of this being team-shaped. We've talked about facilitating team workflows. Permissioning and decisioning is also easier in this shape when the repo is the central object in your data system. And the reason why is that you can then encode in the system the expected behavior of different roles that are accessing it. And now you can absolutely in more sophisticated systems harden that up with guardrails so that you ensure that any given agent only has the permissions that you allow it. And there are a lot of enterprise systems that are going in that direction where they have, you know, identity and permission structures all hardened out so agents can only do certain things. But even in a simpler environment, you get a long way if you are clear inside that repo, what PMs agents do, what engineers agents do, what a contractor's agent is allowed to do. That allows you to start to look at the particular roles and permissions that these particular agents have to change things in the repo so that, you know, you can't just get an overwrite from someone just because they happen to be able to look at the repo with your agent. And that's something that people don' think a ton about. And I'm not here to tell you, just to be clear, that putting a markdown file that specifies role and what you can do is the solution. It is not the only solution. I believe strongly in guardrails for agents. I've talked about it a ton. I believe in permissioning, identity. There is a huge industry in helping that get set up for enterprises. But I also know the reality with not everybody can afford that. Not everybody can set that up. That is not out of box for everybody. And we need solutions in the meantime that allow us to get 80 90% of the way there and then have humans oversee it from there. And this kind of solution is simple and scalable and it does get you a long way there. Now let's get to some of the downstream implications and challenges that come with this approach. You have multiple agents and multiple people working against the same system. How do you deal with what we would call in code merge conflicts? How do you deal with race conditions? A a less fancy way of saying that, a less engineering way of saying that is how do you deal with multiple people touching the same thing and conflicts arising as you edit over each other. Now there are bad ways to do this and good ways to do this. And fortunately the labs have written up both ways. They've talked about the idea that if you just have agents swarm and sort of collaborate on this without structure, it's very challenging to do that. You have a lot of race conditions that happen. You have a lot of collisions that happen. But one of the things that's come out that's a positive, another way to do this that's different is what we would call separation of concerns in the engineering world where you actually structure it down and say for any given piece of work that we're doing, we have a particular page it ladders into a particular folder around a particular topic that we are doing. And that's true regardless of the work that you're doing. That's basically analogous to forking out parts of your repo so that you can actually work against them in a work tree environment. In this environment, in a knowledge work environment, you're just making a page for this version and your agent has been trained to look at and trained by the skills that are in in the repo I'm talking about, trained to say okay, Nate is working on version 15. We're starting a new deck of version 15. We're not going to reuse version 14. We're forking that. Nate's going to work on that. It'll be in the same folder. And when Nate is done, I'm trained by the skills in the repo to go and tell Jane over here that it's ready for Jane to look at. This kind of discipline is really important and centralizing your data structures allows you to enforce that and minimize those kinds of collisions. I want to talk a little bit about how you judge success here. When we do this kind of work, how do you know it's actually better? The easy answer is to say, well, do people save time? I think that's a little bit cheap. I think a better answer is to ask, are you actually less interrupted by stuff you don't care about? Do you have less collisions like we just discussed? Is it more clear what your AI can do because your AI is referring to central team objective skills, charter, what you're going after, strategy, etc. in a way that it understands effectively? You're explaining yourself less. Do you understand the key things that you need to pick up more quickly? Is there more signal coming back to you and less noise because you have the right skills in the repository to say, hey, when these kinds of conflicts emerge, if I see a record of a client engagement come through and it has two or three conflicting deliverables and they have different objectives and timelines, I need to surface to this particular role on the team to address it. That's something you actually have the power to do and enforce at the central level once you centralize this data and start to centralize the skills around working on this. And yes, I included no client correspondence because it's relatively easy to just run a recurring job and pull correspondence from customers you care about and just put it right in the repo so the agents can look at it too. That's not hard to do and it allows you to ladder off of that when you're starting to build. And so you should judge this by whether the questions that are surfaced to you by your agents are more productive. And if your agent isn't asking you any questions at all, that's a question for you. That' something you should address. That is an indicator that you are having to drive every last thing and that you are probably overstressed and overstretched. Now, you might wonder if this goes well, do I lose my job? Do I automate away the part of me that really matters? And the answer is absolutely not. Our ability to understand and tackle problems for the customer is what makes our companies and our team strong. That is something we want to free ourselves to have more time for. And the only way we can do that is if we can actually structure agent work so it does not give us more work to do. That's what frees us, going back to the top of the video, to actually do these longer agentic runs, to say, hey, AI, I'm leaving for the day. You have 8 hours to work on this or 10 hours or whatever. These are the three things that I think are top priority. But you also review what other people have done in the repo since and you add a couple of priorities to that, tackle all of it overnight, and I want to see drafts on my desk in the morning, and you have confidence that will be done well. You have confidence that will be done well because you have picked and put together a structure that enables AI to do that well. And so if you're trying to get started, pick a job that you keep explaining and correcting. Give the AI real current information and saved instructions and try it again in a fresh chat. Are you able to get the AI to learn something? And that is just an individual level experiment you can run. You don't have to get your CTO to agree to a whole centralized data structure and all of that to try that. You can learn to use your AI more effectively just by getting better at passing it instructions that are evolving and being more deliberate about that. Part of the secret for me when I work with new models is I am deliberately learning from past experience with models and I'm not repeating the same mistakes and I'm being vocally self-critical as I talk through what I'm learning and I'm asking the model to say, can you break new ground here? And so, if you want to stop fixing stuff that feels like the same thing over and over and again, and if you don't yet have permission to start like a larger structure that everybody can contribute to because you're not in that role at work, start there. Start by trying to get your AI to learn from your thinking. And if you're wondering, does sort of the Substack kit that I've got, does that cover individuals too? It absolutely does. We're going to talk to individuals. We're going to talk to teams in that post. We're going to give you prompts. We're going to give you worksheets. We're going to give you a kit that helps you actually work through and really helps your agent work through this from both perspectives because I believe strongly in this day and age, you need to be in a position where you can make progress on your own productivity regardless of the team around you, but you also more and more as you can should bias toward team-shaped solutions because those will give you more leverage over time. And that's why I spent so much time in this video talking about the importance of team-shaped AI solutions. And so you know, share this, right? Share this with your team leader, share this with your CTO. They need to understand that the way they structure data is a question that affects the productivity of the entire org, and it's something that they need to think through really intentionally. And I just scratched the surface. For most of us, we're trying to figure out how to set these systems up so that they run scalably, so they run correctly, so they deliver real value, which is the whole point. Otherwise, we're just doing productivity theater. And so this has been a plea to think about the problem differently. Don't think about this as an individual productivity problem. Don't think about it as just you and your AI. Yes, you can get more productive. You can absolutely teach your AI to be more effective by giving it better evolving instructions as you learn more. Absolutely. But wherever you can, think of it as a larger problem for the team so that you can structure your team's data in a way that allows your agents to collaborate effectively. That's the future. That's what unlocks these larger runs. Let me know in the comments what you're doing and what you're learning that enables these larger gigantic runs that are correct and not just complete dumpster fires. I'll see you next time.
