---
title: "I Was The Only Thing Connecting Claude, ChatGPT, and Codex. So I Built My Replacement."
video_id: "QSK4vf_ZTRA"
youtube_url: "https://www.youtube.com/watch?v=QSK4vf_ZTRA"
publish_date: "2026-06-26"
duration: "22:04"
duration_seconds: 1324
view_count: 7819
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  How to Guide - Build Your Open Engine:
  https://natesnewsletter.substack.com/p/ai-agent-handoffs?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  Your AI agents don't talk to each other, so you have become the human glue moving work between Claude, Codex, and ChatGPT. Open Engine is a shared task queue that lets your agents hand off work, carry the sources, and leave a receipt, without you stuck in the middle.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside the AI agent coordination problem in 2026?
  
  The common story is that agents go autonomous and take work off your plate. The real bottleneck is the handoff between agents, where the context, the sources, and the review keep falling on you.
  
  In this video, I share the inside scoop on Open Engine, a practical way to get your agents working as one system:
  
   - Why the handoff, not the model, is the real bottleneck
   - How a shared queue lets agents pass work without you
   - What changes when you move from prompt mode to work mode
   - How agents from different tools coordinate without direct integration
  
  The agents are finally capable enough to do the work, and the win now is building the queue that moves it between them before you become the bottleneck.
  
  Chapters:
  00:00 How to make your AI agents work as one system
  01:06 A friend juggling five AI tools
  04:48 Agents are loop managers and you are the hallway
  06:32 The fix is a shared queue both people and agents read
  08:45 The five components of the Open Engine guide
  10:24 The bottleneck is the boundary between agents
  12:59 Demo: the Open Engine loop in Linear
  14:13 Delegating a task across two different agents
  16:20 Prompt mode versus work mode
  19:30 The test: can the work leave your chat
  20:33 Get the full guide and join the community
  
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
  - "multi-agent coordination"
  - "agent handoffs"
  - "Codex"
  - "Linear"
  - "AI agents for teams"
  - "AI agent workflows"
  - "ai agents"
  - "ai"
  - "ai tools"
  - "linear"
  - "chatgpt"
  - "openai codex"
  - "codex"
  - "ai automation"


# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Tools"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "OpenAI"
    - "Slack"
    - "Box"
  people:
    []
  products:
    - "ChatGPT"
    - "Claude"
    - "Claude Code"
    - "Codex"
    - "Make"
    - "Operator"
    - "Artifacts"
    - "Projects"
  models:
    []
concepts:
  []
summary:
  - "# I Was The Only Thing Connecting Claude, ChatGPT, and Codex"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "artifacts"
  - "box"
  - "chatgpt"
  - "claude"
  - "claude-code"
  - "codex"
  - "coding"
  - "frameworks"
  - "make"
  - "openai"
  - "operator"
  - "product-management"
  - "projects"
  - "slack"
  - "tutorials"
  - "workflows"
---

# I Was The Only Thing Connecting Claude, ChatGPT, and Codex. So I Built My Replacement.

By the end of this video, you're going to know how to make Claude, Codeex, Chad, GPT, and OpenClaw or Hermes work together without waiting for any of them to start to integrate with each other. And yes, I'm going to show demos. I'm going to show what I built. I'm going to talk to you about why. I'm going to give you real stories. I'm going to tell you I'm using it at home and at work. It's the full shebang. You're going to get the full tour. And by the end, you're going to be able to build it for yourself. I call it open engine. And the promise is simple. We need an open engine that drives our life because we have too many AIs and they don't talk together well. So, open engine gets your agents to stop acting like separate subscriptions or separate products and start acting like a system you can operate. And if you're wondering, is this for teams too? Yes, I'm using it with my team. It absolutely works for teams. It works for teams of humans and their agents and it's a seamless way to get them all to work together. I'm very excited. I'm going to show it off to you in this video. And yes, I've been building and using a working version of this to help me actually get stories out, organize my life, move houses, and I wanted to release it into the world because it's been so useful for me and it's actually lifted the load for my wife. Let me make this concrete with a real story of a friend of mine. She has a baby. She runs an agency. She uses Claude code. She's got loops and automations. She's looked seriously at OpenClaw because she wants agents that do real work. She is not trying AI for the first time. She's already using the tools and she's talking to me about them, right? Her challenge is that there are five at least different AI systems she's using that all help with a particular piece of the day and she becomes the person that carries the work between them. And that's a lot of labor to carry. And anyone who's used these systems knows that that labor is real because you can't trade them out. Claude Code and Codeex don't do the same things even though they're aimed at the same segment of the population as a user base. Claude is better at front-end design. It just is. It's intuitive. OpenAI is less good at that, but OpenAI has a reputation for back-end engineering that's very strong. And a lot of us who understand these things are juggling a lot and it's painful and we've had to effectively drive our own harnesses to make up for that by coordinating ourselves across all of these tools. So, she's using five different AI tools, and the question is how work can leave a tool, land with the right person or the right next agent, bring the source material with it, show what happened, and not make anybody read a giant chat transcript. And if that sounds like you, I've got good news for you. I'm putting together an agent tool that solves for that. And that's what Open Engine really is. It is a tool that allows every AI in your system to coordinate seamlessly and carry state or context or detail back and forth without you having to do the work. She is trying to figure out how to balance a client call, a product scoping conversation, and a baby appointment that just came up. She has to figure out how to do all three of those. She typically uses codeex for product scoping. She's using clawed code to reorganize and move her calendar around and she's trying to deal with the baby appointment by email, but she would like to find some automation there for that. There is no easy way to tackle all of that in one thing unless you're compromising on models somewhere. And so the question that she has is can she live without compromises? Can she find a way to get her preferred model against a particular problem and not feel like she has to trade that off in order to keep track of everything? And kind of going farther than that, can she avoid having to depend on unpredictable memory in order to do that? And one of the challenges with OpenClaw, and I've installed it, I've used it, is that it's sometimes not entirely accurate when you're doing multiple different roles in your life over a long enough period of time. And so in this case, like when you have the the baby appointment pop back up after a couple of months and then at the same time, you have an agency team question and your open claw can't talk to the team intuitively unless you give it permissions on Slack. And then if you do, it doesn't talk to the team's agent. And then at the same time you have to get it into the email somehow and then there's a whole memory piece that goes this is the actual conversation I hear. Are you hearing how many ifs, buts, wins, ifs, and copies and paste there are there's so much it's a lot of extended work that we're carrying for using these AI tools and people who are AI productive are just carrying that load because the AI payoff is so great. And what we're seeing in 2026 is that AI is helping with these pieces. And post openclaw, we're getting some of that coordination piece in, but the really hard part isn't solved yet. The really hard part is the movement between the pieces seamlessly and carrying full state, all the details, right? So on Wednesday, I talked about the idea that agents are really loop managers. A useful agent is a remembered workflow that can run again and notice what changed and stop in the right place and bring you in when the decision is really needed. And that is absolutely the right basic frame for an agent. But if every loop lives in its own room, the human becomes the hallway. The research loop finishes and the writing loop doesn't know what changed. The support loop sees a pattern, but the product loop doesn't get the original messages unless you put them there. Right? The coding agent fixes the file, but the teammate who owns review only sees a vague summary unless you send them a bunch of chats. The schedule changes, but the work loop doesn't know that the afternoon just collapsed. Going back to our story, this is why I built Open Engine. And this is the kind of problem I've been working on solving for a while. So if you recall, Open Brain was about memory. So a few months ago, I argued that every AI you use starts from zero unless you give it a true memory system that you control and that lives between your agents. Your context should not be trapped inside one company's chat history. Open engine is the next big piece here. Once the AI can remember how does your work actually move and and the basic approach here is very very simple and I'm doing this and talking about it as simply as possible because I want this to be easy for you. Open engine is the next missing piece in the story for all of us who are trying to be productive with AI and actually get rid of all of that invisible work. Once the AI can remember how does our work move so we don't have to spend a lot of time coordinating and doing that invisible labor. The basic move that I'm going to propose here is extremely simple on purpose. I want to make this as easy to use and do as possible. Just put the work in a queue that both people and agents can read. What is a queue? It can be as simple as a Jira system. It can be a a conbon board that you coded up. It can be a linear ticket Q. That's what I like. Whatever it is, as long as it is a Q that an agent can write to and you can read to, it's good enough. And if you have a queue like that, then all you need to do is have an issue that says this is what needs to happen. This is who owns it. this is the background that matters. This is what the agent can do and where the agent should stop and what it has to show when it's done. And that sounds really, really simple. And simple is the point, right? A good Q issue or a good ticket is the difference between asking an AI for help and giving it a job the next person, the next agent can understand so it actually gets off your plate and gets done. Right? If we go back to 2025 when we were talking a lot about prompting, a prompt asks for an answer of some sort. A ticket asks for a result to get done and it can have multiple agents even if the agents don't know each other and aren't directly integrated. The ticket becomes the place they talk. And I think that this distinction is really important because as agents get better, we need better state management for our agents. A chat box is a terrible way to manage state. And I'm sorry, but so is Slack. An agent needs to be able to change files and create tasks and move statuses and write drafts and do all of that in a place where you can actually see what happened. When we're picking paint colors for the house, I need to see what kind of paint we picked out, right? Like otherwise, we're going to get all mixed up and it just lives in somebody's head and then we're doing that mental labor. When my friend is trying to figure out whether she has five or six different companies in pipeline, she actually has to be able to audit that pipeline from any given command line that she has. See what has been done on it by her team, what has been done on it by her team's agents, what has been done on it by her agents, and what the next step is. Again, you can't do that by querying chats. So, this is what I'm trying to build with Open Engine. And and the guide that I put together is very specific. It has five different components that you can point at that all add up together into a complete ecosystem. And if you miss one of them, it doesn't really go together, right? It doesn't hang together. The first is a linear cube. That makes a lot of sense. Linear's got a generous free plan. It works well with with all of the AI systems. That's why I chose it. But you don't have to use L. You can use Jura. You can use your own system. It's fun. Then we get into how you tell your AI, hey, this is how you use this tool. Because the AI needs to be told, this is the protocol for using this ticketing system. And so there are four other pieces that go with that. And I've written basically skills that tell your AI how to use this, right? There's a setup skill, there's a status skill, there's there's a skill to run a a cue through the the AI, and then there's a smoke test. You can start to test this. I want this actually to help me. And yes, you can absolutely point your openclaw or your Hermes at this as a skill and use that too, right? This is not an anti-openclaw sentiment. I love what Open Claw has done. I love what Peter's done. I love Hermes. You can use those tools as much as you want and you're not limited by only using those tools. Open Claw is pointed at a real desire that made a lot of sense. We want agents that can act, right? Agents that aren't a chat window. Hermes and similar projects are aimed at another real desire that goes beyond that. Agents can improve at repeated work and learn instead of starting cold every time. These are real needs. But making an agent autonomous is not enough. A very capable private agent can still become another inbox or a task cue or a text message cue that you have to manage. The bottleneck I care about is the boundary between agents because that's where I feel the pain. Can the work leave Claude and go to codeex? Can a teammate's agent pick up a task created by my agent? Can a support loop escalate to the person with authority without losing any of the message or customer history and the reason for the agent stopping work? All of this stuff is not a model problem. It's not an agent problem. It's a boundary problem. It's a who gets this next and how do we hand it off problem. If I go back to my friend, her problem is actually much more painful than a tool problem. It's much more painful than a fluency problem. She's fluent in AI tools. That's not an issue. She's got lots of AI tools. That's not an issue. The problem is a handoff problem. The problem is the information isn't flowing between her, her agents, her team's agents, and her team smoothly, fluently, without someone having to manage it. And it would, it is amazing to me how much of AI promise gets bogged down in those handoff points. If you look at AI as essentially a technology change that moves bottlenecks, we are moving a ton of generative energy into this tiny bottleneck around handoffs. And that is what Open Engine is designed to attack and change and blow open so it gets easier. And yes, this works for households and teams at the same time. You think about it, a school pickup change is not the same as a sales pipeline, but the shape of handoff pain underneath is very familiar. Something has changed. Several other things now depend on it. Some parts can be handled by agents. Some parts need a person. Uh, and Open Engine doesn't replace the person. All it does is keep the person from being the only one handing all of this stuff off. And that is such a huge load off our shoulders. We found it's a huge load off for the family. And I found working with my team, it's a massive load off of our shoulders as well because our agents can now work together seamlessly. And we're not trying to track agent messages in Slack necessarily, although we can invoke our agents through Slack. We actually have a clear system of record and we can tag each other's agents in and it becomes a really effective way to collaborate without losing track of any detail of what we're doing. Think about it. If the agent writes a beautiful brief in a private chat and nobody knows where it came from, it's just a draft in a room by itself. Output is what the AI returns right now. Work is what someone can review, accept, and build on. And open engine is about getting from output to work without making human beings the copy paste path. So jumping into demo, this is the basic open engine loop that you see on the screen. It's a request that becomes a clear linear task. It's assigned to the right operator. Codeex wakes up. It checks its assigned queue and finds one eligible agent instructions issue. Before doing the work, it claim locks the issue. It moves it to agent working and it leaves an agent claimed receipt. And then execution starts locally, right? Linear coordinates the team. Codex does the work. A human can create a task for that agent and an agent create a task for another agent. The task includes the outcome and sources and the definition of done. And when the agent starts, it moves from agent to-do to agent working. And when it finishes, it also moves the issue to the right place. The receipt is not decoration here. It actually lets you know what was done. I don't want to ask the agent, did you do the thing? I want to know it got done. And I don't want to have to copy and paste. I don't want to have to coordinate between my my LLMs anymore. I'm so tired of it. So, this is how you actually take all of the context, all of the artifacts, and move it into a system where agents can actually tackle that work in a transparent manner. So, humans don't get confused about what's being worked on. So, agents don't get confused. It just becomes very simple. All right, let's take a look at delegation, which is a key part of this pattern. Can you delegate to agents? And what does that look like? Let's say Maya asks Codex to route a metric sp to Leo's agent. Leo's agent happens to be Claude. Codex checks that Leo's agent is online and then writes a self-contained linear issue with the context needed to act. That's two people's different agents from different LLM providers coordinating and linear. It assigns the issue to Leo's agent, keeps it in agent to-do, and labels it as agent instructions. Now, Leo's agent can pick it up on its own heartbeat and the handoff is visible and it's scoped. It's not buried in chat because the point is not that we made an agent do a trick here, right? The point is you can actually see the work move through the team. And in that context, the smoke test in the skill, right? It's deliberately clean and very, very efficient. All you're doing is saying create an issue called say hello from the queue. You're assigning it to an human or an agent, giving it an instruction label, and making sure that it actually can move to done. So, this is not about giving your agent a bunch of work from me. This is just about giving you a clean smoke test so you can see that this agent interaction loop works. The full loop is actually pretty simple. You have to have a request. You have to have an issue, a claim, a piece of work that's done, some proof that it's done, a receipt, and then you want to go on to the next item. Let's say Leo the agent claims the task and moves it into agent working so everyone knows it's worked on. If it hits ambiguity, the agent doesn't guess. Instead, it moves to needs input and asks the exact blocking question. Maya the human can answer on that issue and the agent can resume and the audit trail stays in one place. And when finished, Leo leaves agent done as a status and moves on to the next task. And we can use that for any piece of work. You can use that for picking paint colors in the house as easily as you can use it for scheduling a pipeline review while you are on the go trying to sort out your kids's doctor appointment. The the point is that the queue itself makes it easy to sort out all of the handoff stress so that you're not dealing with it because open engine demands that we move from prompt mode to demanding real work. And the framework helps us get there. Open engine helps us get there. So, prompt mode might be, "Write me a follow-up email." Work mode might be, "Here's the client call transcript. Here's the decision we made. Here's the promise. I don't want to overstate. Here's the calendar constraints. You draft the follow-up agent, flag what needs my judgment, and leave notes that I can review later." See, that's a full statement of work right there. And you can actually pass that to another agent to review using Open Engine 2 if you want a second opinion, which a lot of people do, especially on client-f facing communication. You could have a whole agent that just reviews for brand language. I'll give you another couple examples. Prompt mode might be, hey, summarize this support ticket. You ask your codeex to do that. You ask your claw to do that. Work mode would be classify this ticket, attach the customer history, identify whether this was a known issue, create a product task only if it meets my escalation rule, and show exactly where you stopped work and why. Or this one, prompt mode would be, "Help me change my schedule." Work mode would be the pickup time for the kids has changed. Check what it affects. draft the two messages that might be needed to the school and wait for approval before anything leaves the system. The model can be the same here, but the assignment is much more clear and the ability to hand off to multiple agents or to a human as you determine is really really easy. We need to stop assuming that we are the glue between all of the AI systems that we work for. Otherwise, the the AI is prompting us and we're just working for the AI instead of the other way around. We want to be in a place where the work can move across the tools that we're already using. And that's the open engine promise because our teams don't really live in one AI tool. I don't know of anyone who is curious about AI who actually uses only one tool. And especially if you get two people together, it's not one tool. It's like two different tools, three, five. I often see six different tools between two people. And you're not going to expect people to actually change that. you actually just want to give people a quue where all of their AIs can talk to each other. So, I'm not going to make you a big promise here. I'm not saying Open Engine can run your company. I don't want to say that. I don't want to say Open Engine can run your household. What I want to say is the next useful AI is not another private assistant. It's a cue where your agents can all work together and move stuff forward. And that matters on any team. But increasingly, we're all managing teams of agents because teams need owners and status and receipts and review. And if you don't tackle that, something gets lost. Something drops through the cracks. And you have household consequences for that. You have work consequences for that. If we go back to earlier in this video, I talked about the idea that we are the hallway between AI agents. Open engine is what I built to make that hallway into software transparent and smooth and easy so we humans stop carrying all of that load. It it's not up to us to be the invisible laborers for our AIS. It is up to good frameworks and systems to let work move from where it started to where it needs to go. With enough context, the next loop can do something useful. The test for Open Engine is really simple. Can the work get out of your chat? Can it get out of your chat? Can it carry with it the sources that it has to do the work? Can it respect limits? And can it come back and say this is what I did and this is what I didn't do and this is the receipt because if the answer is yes with open engine even in a small way then the entire agent conversation changes for you. You stop asking only what one AI can do in a session. You start asking what kind of work your whole system can carry without you being the messenger. That's the promise of open engine. Not agents replacing our judgment, not one agent to rule them all, but all of the mess of our AI systems just stitched together with a clean framework so agents can carry work to the point where judgment is needed and not bother us for the annoying handoffs along the way. That's the version of autonomy I actually want. That's what I've been living with. That's what I'm sharing with you today. If you want that, I have the full guide up. Uh the Substack community gets it first. We have an active Slack where people are building on this. I encourage you to join that as well. Uh and you can see exactly the the demo that I showed you and also a full guide that you can hand to your AI to get this started today. And remember, so that's open engine. If you have trouble with handoffs, as I have had and as so many folks I have had have struggled with, this is for you. Go make your life easier. Go get the headaches out of the way. Go stop copying and pasting and just make make that all go away. Get Open engine and get it sorted out so that you save hours. That's actually my personal goal is I want less wasted human hours. I want us to spend less hours on needless agent coordination. That would be my success. So if you see this and you're like, "Oh my gosh, this is for me." Tell me in the chat in the comments what you are going to use this for. Tell me which AI systems you're going to coordinate. Tell me if you're working with agents, with a team or with your partner. Uh, whatever it is. And and you want a framework that makes the AI and the human actually work together and you're going to use this to solve it. Tell me what it is. One, we'll improve Open Engine and continue to make it better as you give us feedback. But but two, I want to know how much pain we're going after here because that's what I'm interested in. I'm interested in AI that kills our pain. And this is a pain that has arisen since AI agents got more capable and it's just gotten worse. And so in the era of openclaw, in the era of codecs, in the era of claude, we need something like open engine. I hope you've had fun seeing this demo.
