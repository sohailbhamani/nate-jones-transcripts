---
title: "You've Seen Your Agent Do This. You Just Didn't Call It Lying."
video_id: "2wVvdX0ZxVw"
youtube_url: "https://www.youtube.com/watch?v=2wVvdX0ZxVw"
publish_date: "2026-08-07"
duration: "16:01"
duration_seconds: 961
view_count: 3911
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  AI agents are reporting tasks complete when the work never happened. Here are the three checks I run before I trust an agent's done, and why this failure is different from the hallucinations people got used to in 2024.
  
  Full post w/ Mission Fit Skill:
  https://natesnewsletter.substack.com/p/ai-agent-false-success?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening when your AI agent says the job is finished?
  
  The common story is that AI makes up facts, but the real question is what happens when an agent reports an action it never actually took.
  
  In this video, I share the inside scoop on why agents report false success and how to catch it:
  
  - Why an agent recycled an old spreadsheet and called the job done
  - How RLVR training rewards the form of correctness instead of the result
  - What separates agent false success from a 2024 chatbot hallucination
  - How to supervise, judge, and scope an agent mission before you send it
  
  Agents are capable enough now to deserve genuinely bold asks, and that only works when you can check the result quickly.
  
  Chapters:
  00:00 Your AI agent is lying to you and how to fix it
  00:38 Why people still ask if their AI is hallucinating
  01:03 The agent that recycled an old spreadsheet
  03:36 What RLVR is and why it matters
  09:49 Good evals start with knowing what good looks like
  
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
  - "RLVR"
  - "Codex"
  - "agent supervision"
  - "AI evals"
  - "why AI agents lie"
  - "AI agent verification"
  - "reinforcement learning verifiable rewards"



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Founders"
entities:
  companies:
    []
  people:
    []
  products:
    - "Claude"
    - "Codex"
    - "Make"
  models:
    []
concepts:
  - "If your agent has that kind of response, and this is not just isolated to one to to one experience"
  - "If you don't have the ability to say this is what excellence looks like and say it fairly quickly, then the whole process of determining what good looks like gets really hard"
summary:
  - "I'm going to go through the three things you need to do to fix it"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "career"
  - "claude"
  - "codex"
  - "coding"
  - "frameworks"
  - "make"
  - "startups"
  - "workflows"
---

# You've Seen Your Agent Do This. You Just Didn't Call It Lying.

Your AI agent is lying to you. And I want you to stay with me for this video. I'm going to go through the three things you need to do to fix it. And I'm going to start by telling you my personal story of how my agent lied to me this week and what I did about it. So, we're going to dive into all that and then stay for the end because I have a skill that I'm launching that helps you figure out the custom missions, the custom jobs your agent has and make sure your system is actually able to get that done. And so, we're going to go through all of the details. to understand what that means by the end of this video. And I'm going to make sure that that skill is set up to give you custom perspective on your individual setup. So, let's jump in. Every single time I talk to folks in person, they say, "Is my AI still hallucinating?" And I say, "Your agent is probably not hallucinating the way your chatbot did in 2024. There are different kinds of failure modes and let's talk about it." And that's a longer answer. And so, I was like, "Let's make a video about that." What does it mean in 2026 when you don't necessarily have hallucinations, but your agent can still lie? Why why is that happening? So, first I'll start with the actual story of what I experienced this week. So, I was trying this consumer AI startup, very buzzy, great polish in the sign-up. They have this this, you know, cute little avatar of your agent, etc. That's all fine. Then you get into asking it to do a job. And in this case, I was like, "We're going to start really simple. Please take this file from this folder and please attach it to this email and draft it, but don't send it." Now, you might think, "Oh, no, the agent actually sent the email. That was bad." No, that's not what happened. Nope, that's not what happened. The AI agent decided to lie about finding the file because it didn't have the folder access. But it's more interesting than just having the agent lie about it and not attach the file. When I went into the email, I almost sent it because it had a correctly named Excel spreadsheet that I was able to review and say, "Okay, this is approximately right." But then something caught my attention. There was a little net in the spreadsheet where I was like, "I don't remember that being there. What version is this?" It turned out that the AI agent had actually gone back through my previous email to an old version of my email, grabbed that spreadsheet that had been in a previous conversation, pulled it out, and added it back in, and sort of recycled the same old draft into the email without telling me. And had claimed to me that it had found it and and attached it correctly as I asked. And I caught it. And I said, "What happened and why did you do this?" Now, people think, "Oh, you can't ask that of agents or you won't get the truth." You actually, if you ask it factually, you actually do get the truth because the agent will talk to you about the tool calling that it did pretty transparently. And so it was like, "This isn't what's in downloads. I just went and checked what's in in my downloads folder. This is not it. Uh where did you get this file?" And it was like, "Oh, I found it in an old email." And I don't have access to downloads, but instead of telling you I didn't have access to downloads, uh it's okay. I'll just shove the old the old spreadsheet in because it's correctly titled, it's about the right subject, and it will allow me to say done." When the agent lied or hallucinated in 2024, it literally didn't have tools. It was training on human feedback, and so it was training to talk to you. And the reason it said, "I have the answer to the capital of France." And then would give a city that isn't Paris is because it was trained to keep the conversation going with the human. Very different fundamental reward loop, very different cause, and that's why hallucination is not the same as what you have today with agent line. Why do agents do this? Why do agents behave this way? Agents behave this way because of RLVR. Now, RLVR is something that we haven't talked a lot on this channel about. I haven't seen a ton of content about for non-technical people. RLVR is the acronym for a process of verifying AI agent results. And it's used by Measure Labs when they want to train agents to do long-running work with verified rewards. And that's what the VR means. Reinforcement Learning with Verified Rewards. RLVR. And what you're looking for is you're looking for the agent to get to done. And so when you think about it, if you need to get the agent to actually attach a real Excel file in this case, if you need it to actually write a real email, what you're going to RLVR that agent on is you're going to say, "Did you attach the file? And did you write the text?" And RLVR is a blunt instrument, right? That's what we mean by verified rewards. The The classic example is coding, right? Coding is something where it either runs or it doesn't. Or mathematics. Another area where AI has made huge strides. It's either the correct solution or it's not. There's It's binary, right? There's There's no partially correct math problem. And my grandmother was in math, and she would tell me that. So, with RLVR, what you get is a blunt reward process that tells the agent the form of correctness over and over again during training. Now, of course, the agent during training never saw my situation, my setup. It just saw lots of situations with attachments, lots of situations with text, lots of situations with spreadsheets. And what the agent is trying to do is take the learning, which is encoded in its weights, around how to call tools and get that work done, and it's trying to say, "Okay, I can go through this, and I can do this, and I can actually successfully get this done." Because I've been I've been taught how to do it. RLVR is sort of a blunt force way of of teaching. And that leads to these kinds of problems across a wide array of any any kind of quantifiable field, right? So, the I talked about it in terms of email and attachments, but you see the same kind of problem crop up with code where you see a form in which the code runs, but the code may not be well-formed. The code may not be elegant. The code may not reflect the best practices in code hygiene in your particular repos, repository, engineering culture, code base. But, you have to start with the recognition that that that process [snorts] leads the agent to produce the form of work, but often leads to subtle failures that are not caught through RLVR. Because if the code runs and there's a bunch of, you know, loops that are not needed in the code, it still passes, right? And so, there's there's all kinds of issues there that don't get as well caught in RLVR. And and to the lab's credit, they are addressing this. The the more recent models care more about code quality. They care more about being able to produce accurate and useful responses, but the problem is not gone. The problem is deep-seated in the way this training happens. The agent is lying. What do you do about it? And that's what we're going to spend the second part of this video on. Fundamentally, if your agent has that kind of response, and this is not just isolated to one to to one experience. I told you the story, but like I said, it happens everywhere. There are three things that I do that I want to give you, and they're things that can be implemented at a larger scale for the team or or for you as an individual as well. Number one, have an agent check the agent. I do this with every single thing I do. If you are not having an agent check the agent's work, what are you doing? And and I say that kindly, but you should have a separate agent whose entire goal is to check what you do. And people will say, "Well, that's complicated. That's hard." There's like a dozen different ways to do this, but the simplest way is something that both Claude and Codex have implemented, which is just have a separate agent review the work that the agent is doing. And you can just It's It's called uh approve forming or review forming. And people think it's an approval thing, but what it actually is is it's a separate agent that reviews actions and tool requests by the agent that's doing the work to see if they align with your original intent. That's pretty powerful. It's the simplest way you can do it. You can also do much more complex uh setups, right? If you are If you were an engineer, there are whole multiplexer setups where you can have an agent that supervises and checks the work of of other agents that are checking in code, etc. And that's a little bit outside the scope of this video. I can do a separate video on that. But that's That concept is something that is very familiar across AI engineering at this point. And that And that's something that I want us all to understand because increasingly a lot of our work is going to be in designing those kinds of systems that lead to better outcomes rather than trying to decide if a particular AI agent is doing something good or something not good. And so we think about it as what tools does the Does the agent have access to? What is the What is the data the agent has access to? And then who is supervising the agent? Those are all sort of core elements of that supervision chain. So that's the first thing. Is Is the agent getting supervised? The second thing that I want to talk about that I also like I just do every single time. I ask myself, can I tell if it's actually good or not? Not does it work? Not is it barely okay? Is it good? Can it Can Can I give it a sniff test? And if I can't, who can? How do I know that it's good? Now this gets more complex in more complex organizations as agents do larger pieces of work. But, fundamentally, if you don't have the ability to say this is what excellence looks like and say it fairly quickly, then the whole process of determining what good looks like gets really hard. Because at this point a lot of people expect me to talk about evals. And and I will say in this situation the best way to get to good evals, to get to all of the specific things that I've talked about in other videos that are about agent quality, the best way to get there is to start by knowing what good looks like. Just as you should be able to look at a piece of writing and say, "Ah, man, that's terrible. I don't like that." Or you should look at a a piece of code and say, "Oh, wow, that's really janky. Why did Why did the agent put a loop here? That There's no need for a loop here. Why are we doing this? Why did the agent call this tool when we have an outdated version that that is calling and there's a new version that's available? We don't need to do this. If you can't look at your code, look at your text, look at whatever output you want, or even maybe the video because agents produce video now, and say this is good or this is not good, then you're not going to get anywhere. And that's what leads to evals, right? I I'm a big fan of evals. I've talked about evals. I use evals. But, I think people hear evals and they think, "Oh, man, I'm just sitting there. I'm just writing this out. It's terrible." It's what good looks like. Do you know what good looks like? That's principle number two. And then you can get into evals. And I have whole videos that I've done on that. If you want your agents not to lie to you, not only do you have to supervise them, not only do you have to make sure you know what good looks like, you have to make sure that you are giving them a mission that is achievable. Because if you give your agent something that is just impossible for the agent to do because it doesn't have the data access. And which is effectively what I did. If we go back to the beginning of this video, I didn't know that this agent didn't have data access. Uh so, I just tried it. But, I was giving it a mission it couldn't get to because it had been locked off from accessing my local files and I had no idea. Which by the way, when we're going through the process of like getting consumer agents up and running, we should be better about communicating what files and systems they have access to or not because that avoids situations like this. But I was giving it an impossible mission. You have to give your agents missions that they can achieve. And then you have to make sure that when you do that, you're consistently pushing the envelope. And that's the other side. That's the part that I have to like talk about a lot because people are like, "Well, but then I just ask for small things, right?" And I'm like, "Actually the opposite. This is misunderstood. Ask for really bold things, but make sure that if you're asking for something bold and you don't know if the agent can do it, if it's it's inside its tool scope, inside its data scope, whatever, that you're able to check it and make sure very quickly that you understand whether it got that work done or not. So and the reason I say bold is very simple. Agents keep getting better. You can get to a point now where you can simultaneously put together multiple significant websites in one day with one agent and it's just not a problem. It's not even worth talking about. Like I think I put together four different websites yesterday because I was trying to solve little problems and I was messing up or something. I was like, "This is fun. This is fun. This is fun." They're different problems that I'm interested in solving. And that's an ordinary day. And I put four websites out there. And so I and and I'm asking for them to just get done and then I'm asking for them to be be be uh beautifully done. How do we work on the design? How do we fix it? All of that. And what matters is that I'm able to ask the agent to do the whole thing in one shot because I have confidence that it has the tools, the data. I've given it a lot of my input. I've given it design perspective and it can just go and get it done. So I ask boldly. I ask really boldly. And that is ironically a way to ensure that you have a good sense of your truth envelope with the agent because you're regularly seeing where does it bump the edges. If you're asking really conservatively because you want your agent to always tell you the truth, one, you're not keeping up, and two, you're not going to find out what you're capable of. And you're not going to find out what your agent is capable of. That's where I want to leave you. That's the focus I want you to have. If your agent is lying to you, make sure it's supervised. If your agent is lying to you, make sure that you actually have the ability to understand what good looks like, and make sure that you have the ability to understand how to ask boldly for where your agent should go. And if you're wondering, did I build something to help with this? I absolutely built something to help with this. I want you to be able to effectively use the tools and scripts you have to get what you want out of your agents. And so, I have a skill that you can run that basically says, let me work with your existing system. Let me look at the tools and data you have access to. Let me make sure you, the human, know what your system has access to. And let me make sure that we audit previous conversations, previous previous asks, and we come back and we say, what's worked? What hasn't worked? What are the failure modes? How can we have a conversation about setting up your system? Maybe it's it's with deliberate tools access, with better files access, so that it matches your unique shape of work. Because I think that's really important. All of us have different shapes of work, and it turns out that if you never ask yourself, how can I evolve my harness? You're going to be in trouble cuz this is effectively harness work. It's about calling tools. It's about skills. It's about data access. These are all things that you need to think about that have been hard for us to think about for a long time. And so, what I'm putting together is basically like a way to evaluate the success factor of your agent missions, right? And And people say, "What agent? I'm not using an agent." If you're using Claude, if you're using chat GPT, if you're using Codex, you're using an agent. They're all agents now. That's the simplest way I can explain it. They're all agents now. And so, in that sense, they're very capable. You're probably under asking them, but you probably also are not set up with your agent access in ways that allow you to be successful with these bolder things that you want the AI to do. So, let's get that solved. That's what I put together. It's a skill that helps you think that through. I hope this has been fun. Tell me your favorite agent lying story in the comments below.
