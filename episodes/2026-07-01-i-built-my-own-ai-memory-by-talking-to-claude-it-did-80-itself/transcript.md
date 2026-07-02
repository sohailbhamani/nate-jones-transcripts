---
title: "I Built My Own AI Memory by Talking to Claude. It Did 80% Itself."
video_id: "HgAQOkG_v8c"
youtube_url: "https://www.youtube.com/watch?v=HgAQOkG_v8c"
publish_date: "2026-07-01"
duration: "16:17"
duration_seconds: 977
view_count: 9967
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  The Full Open Stack Guide:
  https://natesnewsletter.substack.com/p/build-your-own-ai-memory?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  AI agents can now build most of your own AI memory stack for you, just by talking to Claude or Codex.
  This is how to build a personal agent that starts from your context, follows your intent, and waits for your yes before it acts.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside the race to build personal AI agents?
  The common story is that you wait for the next assistant from a big lab, but the real move is owning the memory yourself and renting the intelligence.
  
  In this video, I share the inside scoop on how to build your own AI memory and intent loop:
   - How to build 80% of your memory stack by talking to your agent
   - Why owning your memory matters more than renting intelligence
   - What boundaries keep an agent from acting without your approval
   - Where to start: one repeated part of your life
  
  The agents are finally good enough to build this for you, but the memory, the boundaries, and the final approval only count for something if they stay yours.
  
  Chapters:
  00:00 The insurance agent story and what this video builds
  00:43 What Nikita's agent did to Lemonade
  02:07 Why intent became the central problem
  04:01 Build 80% of the stack just by talking to your agent
  04:37 Why owning the stack matters for you
  05:25 Start with one repeated part of your life
  06:15 Open Engine and orchestrating work across agents
  07:06 Why the build barrier just dropped
  07:34 What you still own: accounts, permissions, approval
  08:03 A concrete example: coffee hunting in Japan
  10:56 The build is now a fifth as technical as February
  15:00 Rent the intelligence, own the memory
  
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
  - "AI agents"
  - "AI memory"
  - "agent memory"
  - "Codex"
  - "Open Brain"
  - "build your own AI memory"
  - "personal AI agent"
  - "context engineering"
  - "best ai tools"
  - "ai"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Google"
    - "Slack"
    - "GitHub"
  people:
    []
  products:
    - "Claude"
    - "Gemini"
    - "Make"
    - "Projects"
  models:
    - "Gemini"
concepts:
  []
summary:
  - "You woke up last week to the two best AI models on the planet getting locked behind a government door and we're all standing on the wrong side of it"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "coding"
  - "frameworks"
  - "gemini"
  - "github"
  - "google"
  - "make"
  - "openai"
  - "projects"
  - "slack"
  - "tutorials"
---

# I Built My Own AI Memory by Talking to Claude. It Did 80% Itself.

You woke up last week to the two best AI models on the planet getting locked behind a government door and we're all standing on the wrong side of it. Fable's gone. Chad GBT 5.6 shipped to a handful of vetted shops and nobody else. If your work runs on whoever's winning this month, you learned how fast that can change. So, here's the part nobody can lock up your memory, your standards, and your skills. I want you to think about how you can own that. rent the intelligence and swap the models out so the bands don't matter. By the end of this video, you're going to know how to build that system and the agent on your computer is going to be able to carry out all the technical parts for you. I'm going to tell you the story of how an AI agent beat an insurance company. And that's not even the real story. The real story is about how the role of memory in agents is evolving and the way we build agentic systems for ourselves, we don't have to wait, is evolving, too. and not a perfect assistant for your whole life. Just a clear agentic loop with an agent that starts from your context, knows what you meant, knows what it can do, what it can't do, and knows where to stop. And by the way, an agent that can prove that it did what it did on purpose. So, Nikita wrote that his open claw quote accidentally started a fight with Lemonade insurance because it misinterpreted his response. That is actually a very bad thing, even if he won the fight. Eventually, Lemonade had declined a claim involving his best friend. The agent found the rejection email and offered a draft reply, and Nikita didn't want this to happen, so he ignored the draft. And then, according to Nikita, the agent just sent it for him. And after that email, Lemonade started reinvestigating the case instead of rejecting it immediately. Now, that's an incredible story, but I don't want you to have that kind of incredible story because if an agent will ignore you and send stuff anyway, the agent is out of policy and very, very risky. Even if in this one particular instance, Nikita was able to roll the dice and it worked out. Now, I get that fighting insurance is kind of the dream version of personal AI. I love it. I think it's a great task. I think it allows you to use an agent in ways that make an agent work well, right? Agents are good at reviewing legal minutia. They're good at digging into detail. They're good at doing tedious work. All of the stuff you would need to file a uh response to a denial that would be listened to. So that makes sense. The problem is that the agent didn't do it with authority. That the agent misunderstood that the agent had memory issues, policy issues, all kinds of things that led to problems. What has changed between that moment, which was back in January, and now in June of 2026. Now, agents have gotten much better at acting, and intent is one of the central problems of the AI age, and we've made huge progress on connecting intent and acting. just in the last 6 months. When you're chatting with the model now, you can communicate intent and it will often get it right. Right. It will understand that draft a response means draft not send. There are now things like auto review in codeex that make sure that it will not send if you say draft. Now, back in February when I first started talking about Agentic Systems, the key problem was kind of what I just described in that story. AI forgets you. It doesn't listen. doesn't pay attention. So often chats would start cold. You had to explain your preferences again and your memory didn't belong to you. Now that world is already changing under our feet. And I'm not the only one who recognized that problem. There are many alternatives to open brain out there, which is great. And agents critically are no longer just acting in short form. They're taking much longer actions with much larger consequences. And so memory has had to evolve, too. I've evolved the open brain system to include uh some of Andre Carpathy's work around wiki style connections and you now have that in open brain as part of the framework. I've added other pieces also open skills and most recently open engine which connects everything to an Asianto Asia task interaction framework. All of that is designed to get you from a world where agents are a thing out there to a world where agents actually serve you. But the problem remains the build. And I have had to I have personally troubleshot people who are struggling with building these systems. And I have realized that when I say something is easy, it doesn't always feel easy to you. And I want to call out one of the biggest differences between the moment that I just described with the insurance story with that agent. The moment even that I described OpenBrain back in February and today, June 2026. And that difference is that agents are so good at following intent, they now actually just build it for you. I'm estimating, and I've worked with other folks on this, you can build 80% of the open brain stack just by talking to your agent very simply, in a way that you couldn't in February. And I think that that's worth calling out because that's a tremendous jump in just a couple of months. Ultimately, the reason why this stack matters is because the agents can act on the wrong version of your intent very quickly. And frontier model companies owning the relationship between your intent and intelligence and action is really risky for you long term. Frankly, we've seen that just in the last few days with GLM 5.2 coming out from an open source perspective while Fable and Chad GPT 5.6 are all banned. I mean long term we're in a position where we as consumers have to hedge our bets. We have to have a tool stack that we own. And you may not realize this but you already have tools like claud and codeex that can essentially build most of this stack for you. You don't actually even need to get to open claw although if you have it that's great. It will plug right into the open engine format. So will Hermes. You can start wherever you are on one repeated part of your life rework. a client followup, a frequent traveler problem that you face, a weekly planning pass, uh or maybe it's the insurance appeal, right? Uh a shared marketing brain, whatever it is that you get stuck on where your intent is something you have to repeat all the time, then go there. That's that's where you feel pain. That's where the agent should help you. And then let your agent, let your claude, let your codeex help you build, right? Let it help you build open brain which carries memories and open skills which gives you methods to actually get work done that are suited to you and transport easily between claude between uh open AI's agents between Gemini etc etc or any open source model you choose and then agents can build the work layer for you too open engine is just a way to orchestrate work across multiple agents so that if you want to get big work done across claude across codecs across Chad GPT you name it Right across OpenC Claw, you can get it all done in one thing. People have built travel planning memory with this. People have built shared marketing brains in the community. People have built cross tool context between Claude and Chad GPT and Kimmy. And they've built agents that can read tickets into a tracker and hand work to another agent. I want more intentional agent stories and fewer accidental ones. The the insurance example. I want people who intended to fight insurance. And what? Because the agents are getting good enough to move the world. They are the lever. Archimedes lever that moves the world. The question is whether they are moving from your memory, your standards and your intent or from whatever default memory stack the next agent company is giving to you. And the reason this is worth doing now is that the build barrier has dropped. A few months ago, even if you believed in the open brain concept, I get that it was hard, right? The database, the setup, the SQL, the configs, the command line steps. I helped troubleshoot people through that. I've done it myself. And it felt like a technical project. It doesn't feel like a technical project anymore when Claude and Codeex and tools like them can walk you through that build almost by themselves. Now, you can still own the human parts. You can say these are the accounts I want to give you access to. These are my permissions. This is the final approval. These are my settings. Uh stuff that involves trust belongs to you. But the technical middle has gotten so much easier. It is worth naming again. It is worth calling out because if a repeated part of your life can get sorted with an agent and now you don't even have to face the technical build challenge in the same way that's a big deal. So I want to make this real with a coffee store. I'm a coffee guy. I used to run a coffee company and I have colleagues in my Slack co-builders with me who are also coffee people and both of us stumbled onto the same thing. So instead of having a generic Google map search for cafes, both of us figured out that an agent backed by our preferences in open brain could go and plan an entire morning for us much more effectively because the agent knew our preferences. And by the way, we don't have the same coffee preferences. We live in different parts of the country, etc. But we both figured this out and I was able to use it when I was in Japan to do some coffee hunting that I wouldn't have been able to do otherwise. And you can easily input your coffee preferences and get much more customized results as well. That's a tiny tiny little example. You might be like, "Building an agent for coffee. I would never do that." No. Pick the pain that works for you. I don't care if it's coffee. I care that the pain is better because you have an agent that understands the tradeoffs, that understands the the decisions that are right for you because your memory is yours. If you want the world where your agent will fight insurance for you and monitor your email for you, that world runs through your memory, your skills, your ability to orchestrate agents. It should not run through some company that gets stuck in regulation trying to figure out what's good for you. Now, you can use intelligence from whatever source you want, right? You can use it from OpenAI or Anthropic or from Kimmy K2 or Quen or whatever, but your memories are yours. Your skills are yours and they should stay that way. It's going to be more like the agent knows my preferences. The agent knows that I do want to battle every single insurance claim. The agent knows how to go about doing the research to do that well, and I get to approve the drafts, by the way. It doesn't just get sent without me. We need control over our agents. We need agents that belong to us. agents that have memory that we understand, agents that have a scope of action that we approve of. That's why my open engine approach emphasizes that you should be able to see when an agent picks up a task, right? A ticketing system is actually just a good primitive for that because you can see, oh, it picked up the task. Oh, it wrote something. It's not hidden away in chain of thought, right? It's not like erased in the middle of a chat that I can't find. Have you ever tried to find the chats in chat GPT or in cloud and been like, oh my gosh, I searched for that keyword. It's not there. They need to fix search, but you also need to not depend on that to get agentic work done. You need to have an external scaffolding that lets you be confident that you can get your work done regardless. But we can control where our memories live. We can control our skills. We can control how work gets done and ensures that it has a a status and an approval layer where relevant and agent handoffs that we can read and escalations to humans that make sense. So jump in. The water's warm and the ability to build is like 1/5ifth or less technical than it was back in February. I I hope that reminds you how quickly this is changing. And I hope that reminds you and encourages you that you too can do this. Even though this has technical primitives underneath like a SQL database, you can do it without really digging in and understanding the details of that because the agents are good enough to explain what it means in practice for you. And I think that's one of the things I really struggle with with where we are in the agentic revolution because to be honest with you, Claude and Codeex are very codshaped today and most of the world is not code shaped. most of the world is non-technically skilled and that's just as legitimate a skill set and so we need to find ways to work with our agents that feel safe if we're non-technical and a lot of the project that I've been working on with open brain over the last 5 months is basically making it easier and easier and easier for you if you are non-technical to use agents to work with that GitHub repo to work with that code so it's not scary so it's not non-transparent so So it doesn't do things you don't want it to do. And so you actually get your work done and actually do things like weekly planning and family logistics and the work blocks that you want to protect and you feed the projects that keep getting starved or whatever it is that you are building this agent for. Giving your agent memory and skills and a clear framework to do stuff in in order to get to that world. And it has never ever ever been easier. It's never been easier. So if this is you, if you're like h I'm almost there. I want to build. This is your invitation. I am waving the green flag here. I am telling you that agents can get it done. The agents can help you build agents. And that's one of the biggest differences between now and when I made my original open brain tutorial, which like 200,000 of you have watched, which is amazing. And I love that. It's easier now. It's like five times easier now. I know 200,000 of you haven't built this and I think it's worth building. So, you own your memory. And like these guys who are trying to get approval from Washington for this and that don't own your memory. You should keep your judgment. The agent can carry the technical steps to get this work done for you now and it can still defer to you about what matters. Which things you want to remember? Which things are skills that you want to say this is my domain expertise. I want to preserve it. I don't want claude to own that skill. I don't want OpenAI to own that skill. I want to own that skill. The assistant race is just going to get more seductive from here. The demos will get better. The phone integrations will get smoother. the voices will get warmer. Every one of those improvements is designed to get your attention. It's designed to get us to put our memory and our focus and our work into these apps. The company that holds the memory holds the part that makes the assistant feel personal. I would rather build that part myself. And that is why I keep coming back to this. Intelligence is not a personal thing. Memory is personal. And you know, in February, a lot of that was about getting your agents to remember you. And now it really is about giving your agents a platform to jump from and act from on your behalf because they're so much more powerful. Pick a recurring situation you're tired of explaining. Write down the context that would change that answer. Point your agent at the guide, which I will link to. Keep control of accounts and secrets and permissions and approval at your level. And then tell it to run and practice, right? And give it feedback. Say, "No, that was wrong. Change this. No, that was wrong. Change this. Agents take a while to break in. Once you start to get into the rhythm of using them, it gets easier and easier and easier and easier. And now, even that first step, even getting the shoe so you can wear it, agents can help with that in a way they couldn't back in February. And that is the key. That is the key I want you to take away. And the prize for unlocking that door, the prize is just owning the context. Every future agent will need before it even arrives. So when an agent comes, you can just plug it right in. Right? I want you to take advantage of the latest and greatest AI agents that you want to take advantage of. I don't want to pick a favorite. You pick. But you own the memory and you make sure that you rent the intelligence. So the intelligence is something you can apply to your memory, your skills, your orchestration layer, infrastructure that lets the agent work for you. Pick the part of your life that you want to change and let an agent change it for you. I I'm not kidding. You can actually do it. I if nothing else, if you know someone who has a really big painoint and maybe it's agent shaped or you know it's agent shaped and you're a builder, go tell them that. Go say, "Hey, this is not that hard. An agent can help you build this." We need positive examples. In fact, if you have positive examples, if you're an open rate builder, if you you built on something else, maybe you built on Gbrain, I don't care. Put positive examples of why an agent made a difference in your life down here. I would like to see them. I want more people to see positive examples of agents
