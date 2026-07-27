---
title: "You Can Hand One AI Agent Your Worst Recurring Task. It Cleared 60% Of Mine."
video_id: "7pqRRxrdr0c"
youtube_url: "https://www.youtube.com/watch?v=7pqRRxrdr0c"
publish_date: "2026-07-26"
duration: "21:16"
duration_seconds: 1276
view_count: 2225
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  How to give an AI agent a real job: start with the customer support problem your team keeps fixing by hand. We closed 51 of 52 support issues, then rebuilt the process so our biggest category stopped happening at all.
  
  How to find the first problem your agent should solve (guide):  https://natesnewsletter.substack.com/p/first-ai-agent-use-case?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside AI automation for customer support?
  
  The common story is that AI helps you answer tickets faster — but the real question is whether the ticket had to exist at all.
  
  In this video, I share the inside scoop on how we used AI to root-cause our support work instead of speeding it up:
  
  - How we took a comparable support week from 52 cases down to 19
  - Why you group cases by root cause, not by subject line
  - What still needs human approval when access or money is involved
  - Where this same repeated pain shows up in sales, finance, and IT
  
  Agents can carry the research and prepare the work, and the cases left over will be the harder ones that still need your judgment.
  
  Chapters:
  00:00 Fifty-one of fifty-two support issues, fixed with AI
  01:21 The hidden work behind a single support ticket
  02:09 Rebuilding the access path so the question stops
  05:49 Writing down the process before automating anything
  07:34 Recording the pain: one ticket per problem
  08:51 Keeping human approval on access and money
  09:56 Twenty-six patterns and two upstream failures
  11:31 Gumroad: an agent that shipped a bug fix
  12:18 When the customer became the approver
  14:43 Pull 50 to 100 cases and strip the PII
  16:23 Picking a boring, reversible first problem
  19:02 Keep a scorecard and count again next week
  
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
  - "tech news"
  - "Codex"
  - "Gumroad"
  - "AI agent"
  - "customer support automation"
  - "AI workflow automation"
  - "AI support ticket automation"
  - "ai automation business"
  - "automation"
  - "ai for business"
  - "ai agents"
  - "ai customer service"
  - "workflow automation"
  - "ai support agent"
  - "customer support"



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
    - "Amazon"
    - "Slack"
    - "Stripe"
    - "YouTube"
  people:
    []
  products:
    - "Claude"
    - "Make"
    - "MCP"
    - "Computer Use"
  models:
    []
concepts:
  []
summary:
  - "# You Can Hand One AI Agent Your Worst Recurring Task"
keywords:
  - "ai-agents"
  - "ai-strategy"
  - "ai-tools"
  - "amazon"
  - "claude"
  - "computer-use"
  - "frameworks"
  - "make"
  - "mcp"
  - "product-management"
  - "slack"
  - "stripe"
  - "tutorials"
  - "workflows"
  - "youtube"
---

# You Can Hand One AI Agent Your Worst Recurring Task. It Cleared 60% Of Mine.

In the last couple of weeks, we fixed 51 out of 52 customer support issues at my company using AI. And in this video, I'm going to show you how to do that. And yeah, on paper that was a 98% week, and I thought we were doing well, but I spent enough years at Amazon to know that this customer obsession thing is never going to leave me alone. And AI is a fantastic tool to dig into that. So, if that's you, if you are anywhere around customers, this is going to show you how to automate your work. And if you're not, this is going to give you the principles you can use to automate it anyway. And you can take these and apply them to any repetitive process. And yes, I'm going to get specific. Our biggest problem looked almost stupidly small. People couldn't get into the Slack community. And so we dove into it like what is going on? Why is this hard? And we looked at it and we found that the Slack access problems followed predictable patterns, right? And this is stuff that we would do manually before, but AI made it so much easier to dig into. I'm about to explain how that works. So, the problems are really simple. Some people never received the invitation. Some receive a sign-in link and were told it had already expired. Some used one email to pay in another one to join. And so, the key was we had to look at the manual labor that we were doing that wasn't immediately obvious in answering the email, right? all of the hidden work that went into customer success. And this is what distinguishes this 2026 AI automation strategy from a 2024 2025 one. In 2024, 2025, you're looking at the end of the ticket. You're looking at how you deliver value to the customer and can you make that simpler. In 2026, you're looking at the whole process. You're looking at all of the hidden work that you do to get there. We would find the email. We would check the payment. We would look in Slack. We would send another invite. we would write another apology. We would close another ticket. And that changes the question because the question is not just how do we answer these people fast. That's 2024. It's how do we make sure people don't have to ask us for this? And we root cause solved it with AI and we actually were able to resolve it completely. And ultimately what we did is we changed the way people got access. We had approved email domains that could get into the workspace through self-service. We created a non-expiring community invite. And the repeated approval step just went away for the people who should have been admitted automatically. And we saw the results right away. In the next comparable week, our whole support count dropped down to 19. And Slack was not only not a customer service issue, it just didn't appear anywhere. Slack access had been the biggest pile of our work. And in one week with AI, we changed that access path and that category dropped. And you may be thinking, well, couldn't you do this without AI? Yeah, we could do this without AI. But the point is getting all the way through the process of analyzing what went wrong, understanding the full pain that went into that problem because the problems I just discussed were not one access type, right? There's like four or five all wrapped in there. Then figuring out the root cause of each of them individually, then solving them and then rolling that out. That would have taken longer. That was harder. And so AI was helpful at every stage. It was helpful at analyzing. It was helpful at root causing. It was helpful at understanding how to solve these specific issues. And it was helpful at rolling out that solution. Stories like this in the age of AI make me look at support differently. I've been asking how an agent could help us answer people faster in the past. And this is an example of a situation where I was asking a better question for 2026. The work showed us that support could do more than what we were asking with AI's help. Because we could help the person in front of us, we could stop the team doing the same lookup again and ultimately we could improve the entire quality of the experience for thousands of people who had yet to run into the issue. There are not many places inside a company where the same piece of work can tackle internal inconsistencies and issues, also tackle the customer experience, also tackle the quality of the product. Customer success is one of those and that's one of the reasons why I picked it today. Before we keep going, quick aside, you've probably noticed things look a little bit different around here. It's the same old me. I'm just in a new study with room for more Legos. I'll be changing the books out periodically. I'll be bringing some new Legos in. So, keep an eye on the shelves and don't worry, the Beanies and Seahawks jerseys will be back when it starts to get cold in Seattle. If you've been around for a while, I really appreciate you watching. And if you're new here, I'm Nate B. Jones. I help you make sense of AI quickly. What's actually behind the headlines, what matters to you, and how to use these new tools to build things for yourself. Let's make this about you. Here's what I want you to be able to do by the end of this video. Remember, we're going to take one support problem that keeps coming back. We're going to give an agent enough information to really understand it, let it help with the next step, check whether fewer people need help the following week, and close that loop, and see how you scale it out from there. In other words, we're going to take exactly what I just described doing in my business, and we're going to make sure you have the tools to do it for yourself. Now, you have a lot of flexibility on how to do that. You can build that first loop with Claude. You can build it with codeex or any other agent that uses the messages and records you already have. And once you can see it in support, I want you to recognize the same opportunity in sales, in finance, in IT or in product. So, first I'm going to show you what can the agent handle and what still needs to be a person, which is really relevant in the age of customer success. I have reported on cases where people overcommitted to agents here. And then we're going to talk about how to tell whether you actually removed the problem or whether you're just automating the problem and having the answer come faster. Before we automated anything, we sat down and had a conversation about the entire support process. We wrote down every single step as it actually is, not as it is ideally or as it is on paper. And we wrote down how long it took. We wrote down which parts required judgment, which parts were automatable. And then that has a bunch of advantages, right? You can feed that to AI for context. And then we're tiny, right? So we all do multiple things. They all understand how this actually works in practice and can judge whether AI is actually going to lift their mental load or not with a particular solution. It all starts with writing it down and then we time it because writing the reply is not the expensive part in time. Actually understanding where the pain is requires doing that classic boring time study kind of stuff where you have to sit down and go through your process and say, "Wow, this took way longer than I thought." Figuring out what is actually happening here is the part that is painful because it's nonlinear and you have to use a lot of judgment. You have to check five different tools and then you have to come back and then you have to write an update and compose that and try and synthesize that in your head. And that's all something that like doesn't happen in a single place. No one MCP server can solve that. It's not a 2024 or even 2025 type AI problem. It is a 2026 AI problem, people. Uh because you're going through email, you're going through Slack, you're going through direct messages, you're going through billing questions in Stripe, you're going through Substack, and you're searching old conversations. It's it's so many different places to acquire context. It's a miserable way to learn about a problem. And it's something that has been a uniquely human kind of misery. And it doesn't have to be a human kind of misery. In 2026, the first thing we did is we recorded the pain, right? We talk about writing it down, but we're also making sure that every single individual piece of pain has its own ticket. So, a ticket essentially is a little a little scaffold and you can hang on the ticket all of the information you need to resolve the problem. So for a common Slack invite problem that changed the work from 5 to 10 minutes of research that's undirected to under a minute because we realized there was a bunch of research we needed to do. We could automate that with AI. We could attach it to the ticket with AI and then it would be relatively easy to open the ticket, see what's inside, what had been researched about the billing, what have been researched about the account, what have been researched about previous conversations, etc. and say, "Okay, it's all here. Now I just have to action it." And so across that workflow, the person running the workflow estimated that roughly 90% of the mental load had gone away just by figuring out where the pain was, writing down those steps, identifying the highest level load that the human was carrying, realizing that that wasn't helping anybody to stay human and figuring out how to use 2026 computer use and multiple MCP AI automation to solve it. Did we fully automate it? No. We kept human approval on every decision involving access or money because quality really matters. I want people to have an experience that actually feels like it is humangated even in the age of AI. But that means that we just have the opportunity to serve those kinds of customer questions more effectively because some of the other stuff that we don't have to make human got automated. And that's a great example of the the kind of decision you need to be able to make to successfully implement AI in ways that don't degrade customer service. And we've all been there. I know I've been there where I've talked with an AI automated bot on a fairly prominent website and I have wanted to throw my computer through the window because it does such a poor job enabling me to actually get my my questions answered. You don't want to be in that situation. You want to be in a position where you're lifting the load of human pain, delivering faster responses to customers, root causing like I described, but not getting in the way of the quality of the experience with customer success. Now, how do you scale this? We went through all of the tickets once we started to dig in and we found 26 different support patterns that all had separate standard operating procedures. And you know, that customer obsession thing comes out. We ended up building a separate procedure from those tickets and then identifying places in each of those 26 patterns where we could use AI to automate the most painful parts of that process. And so just like I described for the Slack access issue where you have these nonlinear difficult researchy things that would previously not have been AI automatable, we went for that really painful part and zeroed in on it like a bullseye because you can do that in 2026. agents are now good enough that they can take these complicated research type problems and set up context in a way that a human can take really useful decisions. And this is how we caught two upstream failures that looked like separate customer complaints at first glance and looking at them through that lens. Getting organized using AI to look through the patterns enabled us to find things we wouldn't have seen otherwise. Our Slack invite code was seeing enough activity that it expired after two or three days instead of lasting for months. Great problem to have, but it is a problem. Another one, a typo in the access code we published for executive circle members was breaking onboarding in ways that we never intended and it was only in one surface and we had to go fix that particular surface. And so when you start to categorize and understand patterns, those spikes become visible and enables you to zero it out very quickly. But let's go beyond me. Let's show another example. Gumroad shows how much farther this can go when the agent has more access and more room to act. A Gumroad creator named Jordie Breuan reported that three giant dashes were floating across a sales chart on his phone for Gumroad. Like it was just a disaster. Gumroad's support agent reproduced the bug, traced it into the code, wrote a test, opened a pull request, and waited for the repair to make it into production. In other words, Gumroad has taken the idea of customer success that I talked about and tied it directly into the codebase. So then the agent told Jordy the fix was live and gave him the company's standard $25 bug credit. All automated all the way across. And that is very much a 2026 response to AI. And Jordy wrote back the code change had moved the marker into the right place, but it still wasn't fixed as much as the agent thought. The chart still looked wrong and he included a screenshot. The new design used a shaded bar even though the other bars meant counts. There were all kinds of specific UX issues and the technical repair had worked but the product decision that the agent had made had not worked. Sahil, a founder at Gumroad, made a design call. The agent produced another version and this time Jord's approval became part of the process. He approved it. The pull request merged and the repair moved through the release process again. In other words, the customer became part of the approval process for code release, which I think is a really interesting pattern in 2026. Now, what matters to me is that the customer's problem did not die in a support inbox after the agent wrote some code. There is a full complete closed loop here. The message led to a real account and product state change. It then led into engineering. It led into production. And it led back to the customer to validate. And when the customer said the first result was still wrong, Gumroad listened, the agent listened, the work reopened and Gumroad had an innovative approach of actually getting the customer to individually validate the solve. So it got really solved the second time. Now we don't have a bunch of code in the media business. I tell stories here. Our system did not have that level of freedom because it's not necessary. It gathered context. It connected incidents. and help prepare the work while people still own the message and account changes. Now, we can absolutely go there when we get more code involved, but Gumroad shows the way an agent can take routine cases and product work much much farther for companies where code is the core product. And the basic idea is still the same. You have to connect the customer's message to the facts, to the action, to the results. And AI is an accelerator in all of that. Support is also a good place to start because the outcome is hard to fake. The customer either gets into the account or receives their refund or writes back or they don't, right? Or it's still broken or the issue wasn't fully resolved, which is what I love about the Gumroad story. That gives you an independent test of the quality of AI automation in your system. And pull the last 50 or 100 support cases into one place. And you know if you if you're starting small, if your side businesses has 20 messages, that's okay, too. Use 20. Whatever it is, they can be emails, they can be community posts, contact form submissions, direct messages, however you get customer pain, write it down and put it in a system that you already use because you want to aggregate that pain together. And then once you do that, put them somewhere approved for that information. We want to be respectful of infosc here. remove the passwords, the payment details, the personal information. I had a whole video on that on Sunday all about airlock and about how you want to make sure that you are removing PII. So, we could absolutely use airlock for that. And then give the agent this job. Tell it make a row for every single case in a spreadsheet. I want you to tell me what the customer experienced. I want you to tell me in root cause form what actually failed. Tell me what the team checked. Tell me what people actually did to solve it. tell me whether the customer came back and then group the cases by their underlying cause, not by the subject line. So, for example, for us, my Slack invitation never arrived and the link expired and I paid with a different email sound like three different messages on a casual analysis, but for us, they they pointed to the same broken doorway that we needed to address. Then, read the largest group yourself. Agents are very good at making a messy pile look orderly, including when the order is wrong. So take the time to get familiar and fingertippy with the customer experience. Open the original cases, check whether the grouping that AI made actually holds up or whether you need to adjust it. And then pick your problem, right? Pick a painful problem. Pick a boring problem. Pick a repeated problem. I would not recommend you begin with fraud or legal complaints or security incidents or account suspensions or large refunds or the angriest customer that you have. Pick something where the right facts live in systems that you control. the normal next step is already understood and a mistake can be caught and undone. You want to be in that situation if it's your first automation because you want to be playing with house money, right? You want to be in a position where you can make an automation and it's likely to be successful. Now, fill out your note for the problem. Fill out in your understanding what failed, which record you trust, what little action you can take that normally fixes it. when humans have to step in right now and what proves that you actually got the work done. How you know the customer is happy. Now, for example, for our Slack situation, an invitation was created is not good enough. We needed to know that the payment mapped to the person, the invitation mapped to the email, the customer could enter the workspace and then that they could validate that by sending a message. Like we had to have the whole endto-end value chain and ask the agent to show which customer record it found, what is true right now, where each fact came from, which earlier cases looked similar, what it still recommends, and really ask it what it's unsure about. People don't do that enough. And if you ask it what it's unsure about, you're going to expose a lot of thinking and assumptions that you can correct. And when systems disagree, and for a lot of gnarly customer pain points that were dealing with AI in 2026, you were dealing with disagreeing systems, the agent should show you that disagreement and then surface that as a problem. It should not quietly pick the answer that makes the ticket easiest to close, which is a classic failure mode. Run the solve, right? Like you will have at that point a proposed solve from the AI. Run it in draft mode. Let a person review the first 20 or 30 cases that the agent proposes and record why each draft changed or did not. And you can, by the way, actually talk your way through and screen record your way through solving this and give that to AI and it can just process it now. Like it's that good. And that will work with Claude, that will work with Codeex. That review becomes your standard operating procedure. Build it from real tickets and real corrections instead of spending a month guessing what the agent might or might not encounter. Only after the agent can find the right person and the right facts and take action in a way that is predictable are you ready to say, "Okay, we can do this. We can actually get this done with an AI agent and be confident it's correct." It you need that bakein period. What do you do once the AI has automated? It's really simple. Keep a scorecard. How many cases came in? How many were resolved? How many came from each cause? How many drafts have people corrected or customers reopened? How much is the agent fully automated? And how much hands-on time do you still have? Basically, measure and then count again the following week. And your whole goal is to be able to tell a story like I'm telling here now on YouTube. You want to be in a position where you can say, "We cut from 52 to 19. We cut our biggest single customer success issue down with AI because and then you can name just like I named all of the things that you did along the way. Now one thing to expect when the easy repeated cases shrink the work left for the rest of us gets harder and that happened to us right the remaining cases are more likely to involve systems disagreeing a policy that hasn't been as clear as it should be or a product problem that needs judgment and humans need to be involved there. And so that's why you don't go from 52 to zero in a week. You go from 52 to 19 and then you start to figure out some of these harder cases and it just sets you up to tackle some of the things that only humans can tackle for now or that humans need to do more prep work before you put in front of AI agents. Once you see this pattern, you're going to notice it everywhere. There's this repeated pattern of pain that you can see in software access requests, in salespeople rebuilding account history, in new clients asking for the same document, in a bunch of customers describing one product bug in a bunch of different ways. This is why I think customer support is such a good first agent project because people are already telling you what failed in their own words. The raw material is sitting in your inbox, your direct messages, wherever it is, all you have to do is listen. So, if you want the full guide for how I did this, the full set of prompts, the full set of toolkits that I used to automate customer success for me and my business, and how I got from 52 to 19, it's all over on the Substack. Go grab them and I will see you again next week. Cheers.
