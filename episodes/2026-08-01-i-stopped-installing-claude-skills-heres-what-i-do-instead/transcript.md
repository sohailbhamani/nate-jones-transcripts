---
title: "I Stopped Installing Claude Skills. Here's What I Do Instead."
video_id: "up0Bsf3f0Xc"
youtube_url: "https://www.youtube.com/watch?v=up0Bsf3f0Xc"
publish_date: "2026-08-01"
duration: "16:57"
duration_seconds: 1017
view_count: 5178
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Your ChatGPT, Claude, and Codex already ship with agent skills, and most people have no idea what those skills are doing to their output. This is what a skill actually is, how to tell a working one from a broken one, and how to build your own.
  
  Full post + the Skill Building Skill:
  https://natesnewsletter.substack.com/p/agent-skill-one-job-test?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside agent skills?
  
  The common story is that installing more skills makes your AI more capable. The real question is whether your agent can even see the ones you already have.
  
  In this video, I share the inside scoop on how agent skills actually work:
  
  - Why a folder arriving on your machine proves nothing about your output
  - How loading order decides whether your agent ever opens the skill
  - What a vague description costs you in wasted context window
  - Where conflicts across 25 skills start dulling every result
  
  Skills are the cheapest way to make an agent more useful and the fastest way to make it worse, and what separates the two is whether you ever check what you installed.
  
  Chapters:
  00:00 The skills your AI already ships with
  00:44 What a skill actually is
  01:09 Why skills are not apps
  01:35 The risk in grabbing skills off GitHub
  02:05 The core reframe, agents use and humans read
  03:55 Inside a skill, the directory and loading order
  05:01 How a badly written skill fails
  06:23 Start with trusted sources and a real goal
  07:40 Why voice gets your judgment out of your head
  09:07 Skill lineage, forking grill-me
  10:52 The skill builder and what it handles
  14:18 Auditing a library of 25 skills
  
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
  - "agent skills"
  - "claude skills"
  - "claude code"
  - "skill md"
  - "ai agents"
  - "how to build an agent skill"
  - "what are claude skills"
  - "ai skill builder"
  - "ai"
  - "ai for beginners"
  - "ai tools"
  - "ai explained"
  - "chatgpt"



# AI-enriched metadata
content_type: "Case Study"
primary_topic: "Career"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Meta"
    - "Apple"
    - "GitHub"
    - "X"
    - "YouTube"
  people:
    []
  products:
    - "ChatGPT"
    - "Claude"
    - "Claude Code"
    - "Codex"
    - "Whisper"
    - "Shortcuts"
    - "Make"
  models:
    - "CLIP"
    - "Whisper"
concepts:
  []
summary:
  - "Did you know that your AI agent your it doesn't even know if you know what an agent is"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "apple"
  - "career"
  - "chatgpt"
  - "claude"
  - "claude-code"
  - "codex"
  - "coding"
  - "frameworks"
  - "github"
  - "leadership"
  - "make"
  - "meta"
  - "openai"
  - "shortcuts"
  - "tutorials"
  - "whisper"
  - "x"
  - "youtube"
---

# I Stopped Installing Claude Skills. Here's What I Do Instead.

Did you know that your AI agent your it doesn't even know if you know what an agent is. Did you know that your chat GPT that your Claude is using skills and that those skills profoundly affect the power of what you can do? Most people don't even realize their skills. They don't realize their Claude or their chat GPT or their Codex ships with skills and then when you ship with skills, you don't know what they do. This video is for you. If you are trying to figure out what am I doing with skills? How do I use them better? What are skills in the first place? And if you're advanced, how can I take those skills and actually maximize them? We're going to cover all of that in this video. So, let's get it out of the way first. A skill is simply a set of instructions that your chat chat GPT, your Claude uses at a particular point in time to get a job done. So, an example of a skill is you could have a skill that helps you build a spreadsheet. You could have a skill that helps you style a PowerPoint. You could have a skill that helps you write Python code in a certain way. Whatever it is. Like, pick your poison. It can be just about anything under the sun. It's like a recipe for your AI. That's what a skill is. Now, what you may not realize is that skills are not apps. We have this whole world we envision where like apps are what's on our phone. We're used to installing them. They come with a certain guarantee of how they work, etc. It doesn't work that way with skills. The farther you get into skills, typically the more messy it is. And that's what we're going to clean up and make sure we understand in this video. Because skills can't always be trusted. I know a lot of people who go on GitHub and they randomly grab GitHub repos that have a bunch of promised skills and they stick them in their AI as if they're collecting Pokémon cards and they're like, I think this is going to work great. Well, guess what? It typically doesn't work great. Because one, it's not a trusted source. You don't know what you're giving your AI. You may be giving your AI malicious instructions. And two, you don't know how those skills play together with the existing skills you have, with the actual task you want. And that brings me to the core reframe of this video. The thing I want you to take away, if you take nothing else away, is this. We have been writing our skills for an unfocused, vague audience that is somewhere between humans and agents, and we just haven't talked about it. We got to be honest. We need to see that skills are written for agents to use and for humans to read. And if humans can't read them, we got a big problem, because then we don't know what's in there. And if agents can't use them, we've also got a big problem, because then you're not getting any power out of it. And so, everything in this video, I want you to look at it that way. We are figuring out how to make sure the skills, the superpowers we're giving our AI, are going to be readable by humans and useful to our AI agents. And if you don't think you have an agent, I got news for you. Any install of ChatGPT or Codex or Claude or Claude Code is effectively an agent. And agents need skills to maximize their value. If you want to get something done with your AI, and you want to set a big goal, that's that's what you're doing. You're using an agent. And agents need skills. And that's why this is so important, because skills effectively make sure agents do good work that's useful for you. An agent skill is like a note that you leave for a worker who may not ask you a follow-up question before they just go out and get it done. And that's something I don't think we think about enough when we think about building our skills. I think that's why most of us are actually installing and thinking about AI skills backwards. That is not what just happened. What actually moved was somebody else's set of decisions about the job, about the tools, about the acceptable shortcuts in their system, about what done means for them. But, an agent skill is actually a directory. It has a little skill.markdown and it has a whole lot of detail that doesn't feel like an actual app when you peel the cover back. ChatGPT and Codex first load up the name and the description when they're actually calling that skill. They don't load the full set of instructions. It's not like an app you open on your iPhone. So, when you invoke the skill or when the task matches the description, only then are it's is the whole app being invoked. Only then is the whole app being opened. Only then is the full skill actually being used. And so, you might think, I have the skill, it will magically appear. It don't magically appear like that. That loading order matters a ton. The agent doesn't need every example, every template, every script inside its metaphorical head for every single conversation. It sees enough information to recognize the job and loads the operating instructions when the job arrives and then reaches for supporting material only when the instructions point there. And that That is one reason why skills are more useful than pasting a giant prompt into every chat. That same advantage is also why a badly written skill can fail. Because if the description is vague, the agent never knows when to use it. If the description is broad, the skill appears in lots of jobs where it doesn't belong and plugs up your context window. If the main file, the skill.markdown file, is huge and contains every possible edge case, the agent is going to spend so much attention navigating through what feels like a manual instead of actually doing the work. And so, installation can absolutely succeed in the file system and what you added can be absolutely unusable. And I've lived that. I've had cases where I saw someone talk on X or on the YouTube comments or elsewhere about this is an amazing skill. You got to try this. I go, it looks good. I grab it. And the thing you installed is actually not going to help you with your intelligence. It didn't help me. Like I've had cases where I've said, "Wow, this is a design skill. I want to get better at Codex front-end design." And it didn't work. I want I want Claude design to get less terracotta and sort of maroon. I want it to be broader in color pattern. Didn't do it. Matt Pocock has a video on five Claude skills that he uses every day. Almost half a million people have watched that video because reusable skills are real and useful. I love that. So, where do we get started when we want to tackle this problem? Number one, make sure that the skills you are grabbing off the internet, if you do that, are trusted skills. And And if we back up even a little bit from there, make sure you know why you're doing it. Some people get skills just to feel cool. They get skills like they're, you know, collecting special stickers for their car. That is not what this is. These are tools for you to get what you want out of your AI. So, don't just like stuff your AI with a bunch tools you don't need. Think about what you want to accomplish. That's going to matter a ton, especially as skills become something that everybody starts to use. Because I got news, we're at the early side of that, right? If you are listening to this video, you are so early on skills. My mom doesn't know what skills are yet. And so, what I want to call out for you is that you should be starting to think about this as if you are the author of intelligence on your computer. It is your job to say, "I trust this source." It is your job to say, "This particular skill is one that does a task so cleanly, so automatically, I don't need to touch it." And it is your job to say, "I'm encoding some judgment here." And this is where voice is so important. I'm going to be talking about voice more soon. Voice is a hugely transformative technology in 2026. And what I find is really special is that when you want to get more out of your AI, we just are more free when we talk. And so I encourage people if you're trying to figure out how to get more out of your AI, just talk. And there's there's now a feature that there's a GPT live feature you could just talk to your AI if it's try GPT, but there's also other tools. There's lots of tools, whisper flow, there's open-source tools. Record your voice. Talk as comfortably as you can about what you want done. Now, why does that matter? You might think what's special about me? Actually, what's special about you is that you have goals and objectives that are unique. You have things you want to do with AI that are different. I saw someone who took a recipe principle and reformatted it so it was super easy to read in a way that I had never seen before. And it's just this simple little table structure and suddenly it's so easy to understand how to bake bread. Now, that's them. That's unique. They found a way to visualize that with AI. Get it out of your head. Get that uniqueness out. And then, you want to turn it into something that is actually going to get you what you want. And the skill helps to take that implicit judgment in your head and turn it into a repeatable recipe that your AI can go and do for you. Another useful example for skills comes from a video by Nate Hurk. He showed a short version of Matt Pocock's Grill Me skill, which was designed to question you until a plan is actually thought through. And I've used Grill Me. Grill Me is a great skill. A March 19th version of that skill had four body sentences. You could read it, you could understand the job, and you could try it in a few minutes. It was really easy to grab on and say, "This skill about Grill Me does this thing." Now, Nate joked, being he modified it, that he basically destroyed the skill but kept the interview loop. And he the the reason I'm sharing this is because we can actually talk about skill lineage and how skills are rebuilt so that we can continue to grow. In this case, Nate had a different goal for the knowledge documents he was producing. And so he wanted to grab Matt's skill and he wanted to talk about how he was changing it. Because the original supplied a lot of questioning behavior and what Nate was looking to do with his fork was to make the resulting context very persistent and inspectable so you only had to be questioned once. It's a great idea to add to a skill and it underlines how important it is to not just say, "Here's 10 skills. Just install these. This is all you need." But actually to think about it as an evolving capability envelope. And that's often the secret to how to stop giving your AI so many prompts and get it where you want to go. So, yeah, you know, some of the time, 10% 20% of the time, you're going to be able to find something like Matt Pocock's Grill Me skill, which is a great skill by the way, if you want to get grilled about your business plan. I love it. It's great. I use it. It is a trusted source. I know Matt and I can grab that skill and I can use it. But 80% of the time, you are going to want to have some kind of modification. Maybe you take inspiration from something or maybe it's a skill you're building yourself. And you're going to want to say, "Okay, I need to build this." Well, that's where my skill builder comes in. So, all I'm doing is I am, and I know this is meta, giving you a skill to build skills with. And so you can yak and rant and talk all you want as unstructured as you want. And this skill builder helps to organize that in a way that a human can read and an agent can use. And so we'll follow those best practices, right? We'll make sure that the front matter in the skill file is easy for an agent to read, sift through and understand. We'll make sure it's not too bloated. It has the right number of examples, etc. This skill builder takes care of all of that complicated stuff so you can talk about what you want done. And then you can just get the skill that you need to get on with your lives. I've talked about the idea that we have a little clip of the skill. It's almost like a teaser trailer for the skill that the agent is going to read when it decides whether to use it. Well, the skill that I that I'm launching here helps you write that teaser trailer well, so that you are calling that skill when you need it and not calling that skill when you don't. And you're not overloading that teaser trailer, those first initial sentences, so that it's stressful for the model and it adds to the context window and it bloats things out and it confuses the model. We're not going to do that. We mostly write our skills with the vague assumption that it has to work with AI and humans together. We don't think about it as a piece of writing that needs to have an audience. Every piece of writing has an audience. In this case, what's special about the skill builder is that it teaches the AI to write effectively for what is actually using that skill. An agent, it turns out. Agents read skills. But to do so in a way that a human can inspect. And so we're not taking the human out of the equation here. We actually want to write skills in such a way that if you open up your skill.markdown, it's understandable to you. It's not going to be confusing. You can audit it, you can read it, you can check it. That's really important. You want to make sure that if you're giving business judgment to an agent, you know what that bit business judgment is. Like you don't want to be in a position where you don't know what that is. But at the same time, it also needs to follow agentic best practices. And so it should have real clarity around what's up front in that top matter. It should have real clarity around the file structure and how you put examples in and where you put counter examples. And the script builder skill does so much of that heavy lifting for you, so that it it's still going to be human readable, but you also can have your agents reliably call it and read it because day to day I got news for you the agents are the audience. And that in and of itself is a skill. That's why I put this together because what I'm realizing is that most people I know think of skills as like Pokémon cards and you add the Pokémon card to your stack and you're like wow, look at my got a better better stack now. It's a deck builder game. Isn't this great? Well, it's not because you don't know how to mix the skills with the others. You don't know what you just added. You don't know if your agent really understands what's there. You don't know if it could be called reliably. It is just a sense of achievement and a dopamine hit because you saw it and it looked good in a demo. We don't want demos here. We want real production value, right? We want to actually get on with our lives and have AI actually lift the load for us and empower us and lift us up and to do that we've got to give it capabilities that work for us. Now, if you're an advanced user and you're like Nate, I build skills. Nate, I have 25 skills. I have 10 that I've borrowed. I have 15 that I built. I'm good. We've got a second skill for you. And it's one that I personally use a lot. I am putting out there the skill that I use to audit my existing setup because the more you build with skills and AI unless you're careful, the more bloated your AI system becomes and you don't realize how many conflicts your AI is sorting through across 25 skills to deliver the result. And what I find is it's like sharpening a knife. If you are not thoughtful about the conflicts between all the skills that you that you have as an advanced builder, you are going to have dull results because the AI is averaging out all of those conflicts. And so what I am doing for advanced builders is I'm launching an advanced builder skill that allows you to audit all of those different skills that you have, find the conflicts, and resolve them in ways that you the human feel comfortable about. Because otherwise, what are we doing, right? We're just launching and adding and building skills, and it's all additive, and we don't realize how we're averaging out the performance. And that actually leads to a a dangerous loop that I've been in, where you're like, "Wow, you know, the writing isn't working as well with AI right now. I'm going to add a skill for that." And we don't realize that made it worse. That actually made it worse. None of that is intuitively obvious, and none of that is stuff that is present in every skill by default. There is no standard. When we download an app, we know, especially if we're on iOS, there's an app certificate. You have to sign it. You have to sort of get registered with Apple. It's not how it works with skills. And so, you can have a situation both where you have security issues or if it's not security issues, where the skill is just not well written and doesn't get done what you want it to do. I don't want that to be the case for you. So, that's why I put this together. And look, if all you want to do is go through this and you understand the principles and you say, "Nate, I've got it and I'm running with it." That's great. Leave a comment and tell me what you're running with. Tell me what you learned from this video. Now, if you want to go further, if you want to have some help, you want to audit that skill, you want to make sure you can build it for yourself so it's custom, you want to make sure that your 25 skills that you've got or your 50 skills that you've got are actually working together, I've got you. That's what those skills are for, and you can grab that at the link. Either way, let me know in the comments what skill is your favorite and what you are going to do with your new found skill builder powers. I would love to hear what problems you're solving, cuz I think one of the most exciting and empowering things right now is what we ask AI to do, and that's what skills make possible.
