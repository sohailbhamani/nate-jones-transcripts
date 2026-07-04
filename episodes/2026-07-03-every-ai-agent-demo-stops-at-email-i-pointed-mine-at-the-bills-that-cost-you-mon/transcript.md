---
title: "Every AI Agent Demo Stops at Email. I Pointed Mine at the Bills That Cost You Money."
video_id: "U4TmrlWEY4M"
youtube_url: "https://www.youtube.com/watch?v=U4TmrlWEY4M"
publish_date: "2026-07-03"
duration: "15:45"
duration_seconds: 945
view_count: 4573
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Build your reusable agent:
  https://natesnewsletter.substack.com/p/reusable-ai-agent?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  AI agents usually get rebuilt from scratch for every new job. Here's how to build one reusable AI agent for messy, high-trust paperwork -- insurance appeals, tax prep, and beyond.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening when an AI agent becomes trustworthy enough for your insurance denial and your taxes?
  
  The common story is that every hard job needs its own custom agent -- but the real question is what you build once and point at everything else.
  
  In this video, I share the inside scoop on building one reusable agent for messy, high-trust paperwork:
  
   - Why email and calendar is the 101 where mistakes stay cheap
   - How one nine-step skeleton carries into a denied insurance claim
   - What a cited appeal packet must do, and never promise
   - Where the human approval gate stays locked, from email to taxes
  
  Learn the pattern on low-stakes email, and the paperwork that actually costs you money gets cheaper to face, as long as the last decision stays yours.
  
  Chapters:
  00:00 Cold open: email is the 101
  00:59 The paperwork frame
  02:25 Same skeleton: nine steps
  03:08 Run plan
  03:38 Build 1: email/calendar
  05:55 The bridge from 101 to 201
  06:55 Build 2: insurance appeal packet
  10:49 Build 3: tax prep packet
  12:27 Payoff: three builds, same gate
  13:09 Clean data and model choice
  13:46 Rules, runbooks, and CTA
  14:58 Next time: model routing
  
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
  - "reusable AI agent"
  - "context engineering"
  - "AI insurance appeal"
  - "AI tax prep"
  - "how to build an AI agent"
  - "AI for paperwork"
  - "human in the loop AI"
  - "agentic ai"
  - "ai agents"
  - "ai automation"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "Apple"
    - "Slack"
    - "YouTube"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "Every AI agent demo that you've seen this year starts in the same place, email and calendar, or I feel like I've seen a ton of them"
keywords:
  - "ai-agents"
  - "apple"
  - "career"
  - "make"
  - "slack"
  - "tutorials"
  - "youtube"
---

# Every AI Agent Demo Stops at Email. I Pointed Mine at the Bills That Cost You Money.

Every AI agent demo that you've seen this year starts in the same place, email and calendar, or I feel like I've seen a ton of them. You draft the replies, you schedule the meetings, and and I get why, right? So many of us have this problem every single day. It's where we spend a lot of time, bad and Slack, but here's the trap that I see a lot of us fall into. We set up the agent, it kind of works, and we're kind of stuck from there because we don't know how to go from that level of work where you're just getting some of your day-to-day stuff triaged to real work like insurance, like like payments, like health care that takes a lot of delicacy, that takes real trust. So, today, we're going to solve that for you. I'm going to build one agent skeleton live. We're going to learn about it on email and calendar, where mistakes are cheap. And then I'm going to show you how I use the same agent machinery to actually build a real delicate work, highstakes agent that handles insurance and tax stuff. When you tackle agent problems, here's the frame I want you to use. That tax folder you haven't opened, uh maybe the insurance denial that you never appealed, uh those kinds of problems look like different problems to us because we organize them by domain, health versus taxes. But anytime you're dealing with files or paperwork, it's not a different problem. From an agent's perspective, it's the same thing. It requires an understanding of policy. It requires an understanding of category. It requires an understanding of detail. And you don't have good organization to get any of that out. In other words, it's a messtofile organization problem first and then you get structured insights out. That is a common pattern across a lot of our delicate high trust paperwork issues that bedevil our lives and cost us time after time. I see the same thing when I'm booking medical appointments, right? You see the same thing with education forms. Anytime that you have to take a bunch of stuff and turn it into structured context that you can use for a delicate operation, it's the same fundamental agent principle. Now, when we talk about agents, we almost always talk about action, right? the agent will do something. It will send an email or file something. And I get it, right? It looks really good, but when you're doing high trust work, I would encourage you and I would ask you to focus on the part that the agent actually lifts the weight on. Like I'm interested in agents that lift the load off. And and to me, an agent that can sort through bureaucracy with unstructured context with the mess in my folder. Uh that's more useful to me than an agent that can click a button. I can click the button. I need the agent to get everything ready so that clicking that button is really easy. And so the skeleton we're building today does nine things. And you're going to see every one of them on screen. So I'll just say them once. We're building a context pack. We're building injust. We're building chunking. We're building normalizing storing retrieving citing, exporting, and gating. And yes, agents will help with all of it. That last one, the gate, is the rule from the top of this video. If the agent can read and organize and draft and site, that's great. but it's not allowed to submit or pay or sign. And I want to be clear, this is a job that we're giving the agent from the beginning. So, it has good guard rails. We're not giving the agent ever the option to take an unallowed step. And it's up to you as the human to keep that guardrail in place as you build and to ensure that you are actually testing this stuff and you are actually validating before you submit an insurance claim or a tax claim that it's on you as the human to submit it. It's not on the agent. So, here's how we're going to run this. We're going to have three builds all in this video. Same fundamental structure. What I'm trying to teach you is one structure that scales. We're going to start easy. We're going to start with your email and calendar, which is unstructured mess, but very low stakes. Then, I'm going to stop and I'm going to show you the bridge, the actual move that takes you from the calendared email world to the more advanced part. And it's something everybody skips. And then, we're going to get into insurance appeals and then taxes as some of our advanced use cases, our 2011 use cases, if you will. So, let's get started. All right, we're going to get into build one. And let's be honest, your inbox is probably a dumpster fire. Mine certainly was, too. And it's not because we're disorganized. I'm going to keep saying that. It's because email is effort that other people give to us. Everything lands there, not on our agenda. And it's so hard to structure it. Now, let's notice something before we start. This is not just the training wheels example. Your W2 is probably in that inbox somewhere. I know mine was. The denial letter from an insurance company may have arrived as a PDF attachment. You may have notes from your doctor leading to secure messages. The trusted work we're building toward is often email mediated. Here's a thread where someone's trying to schedule a meeting with me. The agent gets a context pack. That's the first skeleton idea that I talked about. And a context pack just defines what the agent is allowed to read. This thread, my calendar constraints, the people involved. And it has one goal. Prepare a reply with a proposed calendar hold. Notice the word prepare. Watch what it does. It ingests the thread. It pulls out the people, the date ranges, the time zone mismatch. Dates become dates. People become people. That's what normalization is called. And I know it sounds boring, but this boring stuff is what makes the agent do useful high trust work. I promise you it's worth it. So the agent checks my constraints. It drafts the reply and it builds the proposed calendar of Now watch this because this is the moment the whole video turns on. The draft is done and the next obvious thing would be to send it and and the agent stops and I want it to. It leaves the draft. It leaves the proposed hold and it leaves a receipt. What sources it used? What it changed? What still needs my approval? And if it's right, I'll just send it. If it's wrong, I can fix it. That receipt to me is critical. It's the difference between AI handled it and I know what happened here and I can trust the AI. It is so important to build for trust from day one. if you ever want your AI to do stuff that involves high value delicate work where real money is on the line where real value is coming back to you because like you we all know like if we appeal insurance and we win if if if we file taxes correctly and we get a refund that's real money on the lens thousands of dollars potentially if you wanted to help with that you got to get this trust piece right now let's pause for a second because this is a move almost everybody misses and it's the reason most people never get past that initial email simple 101 agent demo. You might think that going from a basic agent like an email agent to an insurance appeal means starting over. A new tool, a new setup, a new system that's higher trust. It doesn't if you build it right. Look at what you already own from build one. You own ingestion, turning documents into text the agent can use with anchors back to the source. You own normalization. You own dates becoming dates and people becoming people. You own the receipt. You own the gate. And those are primitives or building blocks. And none of them care whether you're in a scheduling thread or an insurance denial claim. It's the same thing to the agent. And that's why I keep calling this a flywheel. Every build we do, if we're doing it right, adds a skill to our shelf. And that makes the next build cheaper. So now, let's turn around again, and let's tackle a task that actually costs you money. First, I'm going to tell you what's real and what isn't here because I want you to actually know and trust this demo. The policy documents you're about to see are real. Insurers publish their plan documents. So, this system is querying an actual insurers's actual policy language. The patient for privacy is synthetic. The denial letter is built from the kind of denial letter that people post publicly, but every identifying detail has been masked. And this build works exactly the same on your real files and yours stay on your machine. Now, some new words to learn here in the context pack. We have denial letter. We have real policies and claim histories and supporting documents. And we have a new goal. I don't want a vibes-based appeal letter. I want a case file that I can inspect. So, this is more delicate work already than the email. All right, let's get to work. The agent starts by chunking. The denial letter is not one blob, right? It's got a date. It's got a denial reason. It's got a claim number, a deadline, and somewhere in there, there's a paragraph that says, "What evidence would change that decision?" And the policy is not one blob either. It has sections and definitions and exclusions and appeal rules. Everything is getting split into tagged and addressable pieces by the agent. Now we're normalizing. Like before, dates are becoming dates. Amounts are becoming amounts. And this one matters. Missing documents are becoming missing documents. That's especially important if you have a gap in your evidence because it can affect what you can act on and you won't get a surprise a few days before some kind of deadline. All of it is stored locally. You have a little database called SQLite and you have a folder and you can open the sources and the records yourself. Nothing leaves your machine. You never have to ask the model to remember what happened. When an insurer denies you, they're required to site the specific policy language they're relying on. Think about what that means. You're not searching for something you can't find. You already know the address of the thing that's hurting you. So, there's no vector database there, only a similarity search. The system simply has to retrieve by structure the denial reason, the exact policy section, the denial sites, the deadline, and the document checklist. And the first thing that the agent is going to do when it does all this is a sanity check. Does the section they cited actually say what the letter implies that it says? Sometimes it doesn't. And when it doesn't, that's finding number one. Now, look at what this produces. There's a timeline with a service date and claim date and denial date and an appeal deadline. There's actually a denial map. There's the exact policy language that governs all of this. There's an evidence checklist, what I have right now, what isn't there yet. And yes, there's a draft appeal letter, but the letter isn't the main thing. The whole evidence packet is what really matters here because the citation map means you can actually validate that what you're arguing is true. So, here's the reframe against conventional wisdom. The agent is not winning the appeal for you. It is turning the pile of unstructured information into a case file that makes you able to win. you were losing or you didn't win because you were showing up to a structured fight with an unstructured pile. This bill doesn't guarantee that you win. It just means you stopped showing up with bad data. Now, again, watch where the agent stops. The agent has drafted the appeal, the address, the claim number, the deadline, and the viral demo would be to say, "Okay, now we're going to send it." No, it stops. And I want to be very plain about this. You are responsible for what you send. I'm not advocating anybody fire one of these packets at an insurance company unread. The citations make your review faster. They don't make it optional because if an agent sends a bad appeal on its own, now you have two problems. The denial and the mess the agent made. This is the same skeleton as our email build. The nouns may have changed, but the underlying data, the underlying structure of how we solve this problem is exactly the same from the agents point of view. And that's how we build momentum. Okay. Build number three. I'm going to show you taxes. Everybody has to deal with taxes. And I want you to notice how fast this goes now because this is the flywheel doing what I promised at the top of the video. Again, we're going to say synthetic documents here. Tax folders are things nobody should see on YouTube. Uh, and we're going to tackle some new objects, right? So, you're going to see W2s and 1099s and invoices and receipts and bank exports and mileage notes. The works. And notice where half of this stuff was living. It was living in the inbox. That dumpster fire from build one is a source now for build three. Our new goal here is we're not filing. We are preparing a reviewable packet for you or your CPA. And if you're paying somebody hundreds of dollars or thousands of dollars to painfully comb through your pile of tax docs, understand what you're paying for. You're paying for the combing. This is the combing of the docks. It's the same skeleton we already built. It goes through the same order agent-wise. You're just ingesting. You chunk it into forms. You have income, expenses, unknowns. You normalize into a tax year ledger with date and vendor and amount and category and source file. And again, we have guard rails. The citation guard won't let a deduction float through without evidence. If the agent says it's a business expense, it's going to point at the receipt or it's going to flag the line instead of pretending it knows. The export you get is a packet, not a completed 1040 return. You get an income summary, an expense ledger, a deduction evidence map, and missing docs where you have them, plus a list of questions for the CPA. And that last one is underrated. A good agent doesn't just give you answers. A good agent gives you better questions to ask an expert. And look at that. It doesn't submit. It doesn't file. It doesn't email your CPO. It preps the folder. It gives you a summary. It stops. The whole build took a fraction of the setup the insurance one did. Why? Nothing in it was new. Third turn of the wheel, much easier. This is the principle I want you to understand. You put the work into building this system. Now, you can do lots of sensitive stuff relatively easily. This is an expandable agent. We're into Legos here, people. Okay? So, hold these three builds side by side for a second. Email, insurance, and taxes. Sure, the words changed, the stakes changed, but the skeleton of the agent didn't. You still had to have a context pack and ingest and chunk and normalize and store and retrieve and site and export and gate. You've now watched me run that list three times. That is the build. Now, one more thing that all three builds share underneath. Clean normalized data. That's the secret, guys. When dates are dates and every claim has an address, you stop needing the most expensive model for most of the work. I get asked a lot, especially post fable, what's the cheapest model? It's the open- source model. Listen, this is the same play Apple wants to run on your phone. Lightweight models can do advanced things when the data underneath is clean. So, I'm laying the stage for you to think about more model choice by making sure you take care of the data first. Number one, the hard part is not the final click. The hard part is context. Fix that dirty pile of data first. Number two, learn the gate where mistakes are cheap. Where does it become expensive to do something? Number three, understand where humans need to have expertise. If it touches money, if it touches health, this is something where a professional needs to get involved and you need to not pretend that AI can just do the job. Number four, don't build one offs. Please, I'm begging you, build a flywheel like I showed you today. Every build that I'm showing you makes the next one cheaper. And the bridge from your 101 agent to your 2011 to your 301 is shorter than you think. The Substack post has both of the runbooks, the healthcare appeals build and the tax prep organizer, plus the two open skills underneath them. It has a guide for context engineering, and it has runbooks. Now, here's what I'm asking you to do. Put in the comments the folder you'd point this at next, whether it's insurance or taxes or something I haven't thought of. Tell me what it is. I'll pick a few and we're going to build guides around them because this shelf is going to grow over time. Next time we're going to talk about how to put every model in the world at your fingertips, including the cheap ones. Because once your data is as clean as I've shown you in this video, you don't need an expensive model for most of this work. You just need the same agent skeleton and you can apply to different paperwork. You can keep that human yes or no at the end and you can go for it. So, subscribe for more and go open that folder and get to
