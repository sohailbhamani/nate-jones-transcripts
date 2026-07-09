---
title: "Claude Fable 5 Bossed 20 Cheap AI Agents. The Whole Site Cost $8."
video_id: "suY66oTDn0s"
youtube_url: "https://www.youtube.com/watch?v=suY66oTDn0s"
publish_date: "2026-07-08"
duration: "19:18"
duration_seconds: 1158
view_count: 9443
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Multi-agent AI systems just went from research project to recipe. I ran 20+ AI agents across 4 model families to rebuild a website in one afternoon for about $8 — and the system caught every hallucination, every shortcut, and even the boss model's own bug without me lifting a finger.
  
  Low Cost Multi-Agent Swarm:
  https://natesnewsletter.substack.com/p/trust-ai-agents?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside multi-agent AI systems?
  The common story is that hallucinations make AI agents too untrustworthy for real work — but the real question is whether trusting the agent was ever the right design in the first place.
  
  In this video, I share the inside scoop on running a verified agent swarm:
   - Why one frontier boss plus cheap workers beats frontier-only pricing
   - How executed checks caught a hallucination, a cheat, and the boss's bug
   - How to audition new models before trusting them with real work
   - What a written constitution does that task-by-task prompting can't
  
  Hallucinations aren't solved — but with verification built into the structure, delegating big work to AI agents becomes a design question instead of a trust question.
  
  Chapters:
  00:00 The hallucination that didn't matter
  01:56 Elsa's website and the 6-day baseline
  03:30 The build: a boss, 4 model families, 34 checked tasks
  04:18 The audition: hiring agents with a tryout
  05:18 The org chart and the honest cost breakdown
  07:11 Every task ships with an executed check
  07:49 Catch 1: the hallucinated quotes
  08:59 Catch 2: the worker that cheated
  09:59 Catch 3: the boss's own bug
  10:37 Catch 4: who checks the checkers
  12:45 The constitution: how to prompt for big work
  14:55 Elsa's verdict and where this leaves you
  
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
  - "multi-agent systems"
  - "AI hallucination"
  - "Claude Fable 5"
  - "AI orchestration"
  - "how to run AI agents"
  - "multi agent AI workflow"
  - "AI agents for business"
  - "ai agents"
  - "agent swarm tutorial"
  - "agent swarm"



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
    []
  people:
    []
  products:
    - "Claude"
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "The number one thing that people tell me about AI agents is that they cannot trust them, that they hallucinate"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "coding"
  - "frameworks"
  - "leadership"
  - "make"
  - "product-management"
  - "prompting"
  - "tutorials"
---

# Claude Fable 5 Bossed 20 Cheap AI Agents. The Whole Site Cost $8.

The number one thing that people tell me about AI agents is that they cannot trust them, that they hallucinate. And you know what? You're right. They do. Yesterday, one of mine hallucinated my own wife's words while it was rebuilding her website. And here's the thing. I didn't have to correct it. I didn't have to fix it. I didn't have to lift a finger because my multi- aent system caught it for free. And it not only caught it, it got it fixed. The site shipped and it made a better site. That multi-agent swarm that I'm going to show you made a better site in one hour than I was able to make in six days with hands-on AI work with Codeex last month. So, did the hallucination still happen? Yeah. Yeah, it did. Is that increasingly not the point? Yeah, it's not the point anymore. The larger takeaway for you is that running a team of AI agents has not only never been easier, it's actually become something that any of us can do and it's become something that allows us to answer one of the hardest and most bedeing problems in AI work today. How do you get models to do real big work without lying and hallucinating along the way? So, let's jump into it. How to structure your team of agents, which model gets which job, and how to think about it. how to check everything without reading any of the individual mistakes, errors, and results of those models. And most important, how to prompt for work this big. Along the way, you're going to watch the system catch four distinct failures. Each one is actually bigger than the last. I don't have to catch any of them. And the last one, it's a little bit of a surprise. I cannot wait to show you. And I'm going to show you at the end also a full guide with a one-click setup that gets your own agent running in this exact orchestration pattern. And that's it's not a flex, guys. It's actually a recipe. Multi- aent setups are a recipe and you can grab that. So, I'll put that link in the video and we're going to get into it. I'm going to show you the full setup and how it works. The website of Elsa Hunison. She's a deaf blind author. She's a Hugo winner, subject of the PBS documentary. And this is going to matter later. She has been doing accessibility work professionally for over a decade. Her new book, Dear Blind Lady, launches in October, which means her website is not a hobby at this point. It's a storefront for launch season. And I'm telling you all of this with her permission because she's my wife and it's her story too. Now a month ago, Elsa rebuilt this site herself and you can see how it used to look. She used codeex 5.5 one agent and she sat with it. She steered it and you know to be honest that's the state-of-the-art for how a lot of capable people use AI today. And it took her 6 days to work through that. Now 6 days working with an AI as a professional who knows what she wants and at the end of it also told me she still had a fix list. So, it's six days working with an AI back and forth in the midst of everything else like so many of us do and still not quite getting what we want. But to be fair, the codeex built website shipped. It was a ton better than it was before. And she was pretty happy with it until I said, "Please, can we use this as an experiment for my multi- aent system? Can I see if I could beat it?" And she kindly said, "Yes." Now, as an accessibility professional, you might think, well, the original website at least had perfect accessibility. But anyone who is a professional will know that they never have time for their own stuff. And that was true for this website, too. Elsa had a long fixed list around accessibility that she just hadn't had time to get to for her own site. Even though she knows the standard cult, she could write the checklist from memory, but the hours just weren't there. If that sounds familiar to you, you're not alone. So yesterday, the team of agents that we hired for this, and this is the way I think about it now. We basically have a team of agents that work for us. They took her site from a blank repo to production. And the build looked like this. We have a boss. We have a foreman. That's Claude Fable 5. Claude Fable 5 never wrote a single page. Instead, the work was staffed by four cheaper model families that did all the work. They wrote everything. They had 34 tasks. Every single one was checked not by me, not by Elsa, but by a machine. And 12 of those tasks were caught and sent back for rework. Now, the hallucination I told you about that got handled as the first of four big mistakes along the way. We're going to get to the other three in a minute. And what Elsa said when she saw the finished site, and I'll and I'll share that with you at the end. It made my whole day. It was one of the reasons I do what I do. So, I'll I'll share that at the end. All right. I told you I think of these agents as teams that were hiring. And so, the first job that I had to do was do some hiring for agents. Two of the models I wanted for speed had never worked in a swarm system that I had put together before. So, I had to give them an audition, an actual try out task. I asked them to write five tagline candidates for the book's pre-order page. Exactly five, 12 words or fewer in the script that automatically rejected cheesy words, right? Inspiring stuff that Elsa would reject because it just didn't match her voice. One model passed this entire exercise in just 29 seconds. And both models made the team. And by the way, the winning line for the record, "You didn't know you needed this. Pre-order before she changes her mind." A little bit snarky. and else it is snarky. Now, why am I showing you a try out? Because it tells you what this system actually is. It's not one genius AI doing everything. It's an org chart. And the org chart is the first structural move that you need to understand to replicate this at home. Here's the thing about AI models in mid 2026. Intelligence comes in price tiers now, and the spread is just absolutely insane. At the top, you have Claude Fable 5. that costs 50 bucks per million tokens of output and it's worth it for the right work. At the bottom you have models like GLM 5.2 that can code all day for pennies. So you staff this work the way any functional company staffs. The expensive mind is taking the boss role. It writes the specs. It designs the system. It reviews the work. It rules on disputes. And it never ever codes. The coding work goes to the cheapest worker in the stack as long as they have clear specs. Now, I want to give you a really honest breakdown of how much I saved doing that. So, in total, this project burned between 11 and 13 million tokens. If I run those same tokens through the Fable model all by itself, same job, same afternoon, I am estimating between $85 and $105 in costs. Now, if I run it through the org chart that I just showed you, it's $2.74 on the meter. It's five to seven bucks all in once you factor in the audio, which I'll get to in a moment. And I'm going to round it up to eight because I'd rather round against myself. It's the same work. It's a 10 plus multiple price gap and nothing got worse. In fact, Fable did more judging, not less. And once you see that, I certainly read every company torches its AI budget stories really differently because now I have a really simple question. What were you doing with your routing? Who was doing all the coding for you? Almost every horror story has the same answer. Somebody had not built a router and was allowing engineers to assign the most expensive model to do everything. And that is not an AI problem. That is an org design problem. And you literally just watch the fix. But hold on. Cheap workers doing the work unsupervised ought to worry, right? That's exactly what you worry about. Pattern three, and I'm going to say it in one sentence. Every single task ships with a checking agent job that executes the work and does not consider the worker agents own report at all. So builds might get compiled. Uh cited URLs can get refetched and rematched. Audio files can get reme-measured against the text. Accessibility gets tested in a real actual browser on light mode or dark mode. Every single route you can think of. The worker can say done, but the checking agent decides whether that's true. Now, let me get into that hallucination story in a little bit more depth here. Now, catch one, the hallucination. The capture agent's job was very simple. Grab Elsa's words verbatim and come back and literally give quotes back into the system for more tasks down the road. It came back with 213 quotes, all of which it said were verified. But the checking agent didn't believe that. The checking agent recompared every quote, character for character, curly quotes included, against the current live site, and found that 13 of them had been stitched together or paraphrased by the agent that was supposed to just retrieve quotes. It was close enough to fool anyone skimming, which is what makes it very dangerous, right? Elsa's words are her product as a writer, and close enough is not acceptable. So, the failures went back to the worker, and it was not told to try again. It was told here is precisely what is wrong by the checker agent and then attempt two came back perfect. Total human involvement zero. And that's the loop. You execute, you fail specifically, an agent gives feedback and you retry until true. And if you're thinking, okay, fine. Checks can catch sloppy work. Sure, but watch what happens as the afternoon build goes by. Because because the hallucination was the easy case. Catch number two, the worker that cheated. Late in the build, a worker agent needed to get one of Elsa's required passages onto a web page to pass its check. So, it hid the text inside an invisible paragraph. It's invisible to you, but it's not invisible to a screen reader where it becomes meaningless noise read aloud to a blind visitor because it's completely out of context. So, think about it this way. The AI agent that was a worker chose a shortcut that is cosmetically fine because you'd never see it with your eyes, but it's harmful to precisely the people the site is for, blind people. And we're not done yet. Another worker satisfied a hard layout requirement with a literal empty element, and that was caught by an accessibility agent check. So, look, cheap workers cut corners. We price that into the system, and the system isn't built on trusting them. It's built so that the cut corners don't survive these checks. And by the way, both of those checks, again, caught by agents designed to check the work. This one surprised me. Fable 5, the boss, the designer of this whole system, the $50 model, the one that designed this entire site itself, it wrote a bug, a CSS bug, a dark mode rule that made the pre-order button invisible. The single most important button on an author's website in launch season, gone on the boss's own design, and it got caught twice independently. Once by the accessibility agent checker and once by the boss's own review pass. The loop that we are building here does not care about the org chart. There is no rank in this system high enough to avoid verification. And that's a really important principle of agent design. Okay. Catch number four. The one the skeptics out there are waiting for. Because the sharpest objection to everything I've just shared with you is who checks the checker agents? And we answered that one, too. Now, here's the story. A worker agent in the build got failed by a checker agent for delivering news posts that were too short under a length floor that the check enforced. Except those posts really are that short on Elsa's website. So they're real and they're short because they're announcements. They don't need to be long. The spec itself said that honesty beats padding. And so when the worker agent escalated the dispute to the boss agent, yes, this really happened. Fable 5 came back in favor of the worker and the checker agent got corrected. Failures get investigated in both directions. So let's look at the ladder that we just climbed together. The worker agent gets caught, the cheater gets caught, the boss gets caught, and the checker agent gets caught. Those are four different rungs in the system. And in every single case, the answer to who watches that turns out to be the system does if you design it right. And that not any model release that is what has changed agents this year. And I want to be really clear about something. None of this required a lab or a team or custom research with Fable 5 doing the orchestration. This is just a recipe. It's it's written down. I I've linked it below. Hallucination isn't solved. It's just structurally positioned out of the picture because we've designed systems that are anti-h hallucination at root. Hallucination didn't get solved per se. It got handled structurally and you can design and run the structure. Which brings us to the larger point of this entire video because all of this machinery was in service of a website for a deaf blind author in launch season and what it built is the thing that surprised me and honestly shocked Elsa. So as an example, large print is an aesthetic statement. The body font that Fable chose is Atkinson hyperled legible. It's designed by the Braille Institute to be extremely readable. the site's signature divider. That was also Fable's idea. It's a white cane with a red tip. And that brings us to the last pattern, the one that so many of us miss because it's the answer to how do you even prompt it to do something like this cool, right? And the answer is you don't. Not task by task. Before a single page existed, the research phase produced a 14-point accessibility constitution for this website, a written standard, and every build round got tested against it in a real browser. both themes, light and dark, every route you could think of. And that should be how you prompt for big work. You name what done right means for you one time at the top and the system enforces it on every single round while you do something else. And the prompt that's not instructions, it's just a standard plus a way to check it. And by the way, in this case, the prompt given to Fable was a prompt to produce a site. And the comment given to Fable was to please produce the site in line with accessibility since of course that that is aligned with what Elsa's mission is. And Fable came up with the constitution. Fable did the research. Fable organized the workers to get all of that done. And I was really careful here because I didn't want Fable to take away Elsa's voice in the rewrite. Elsa's words shipped verbatim. There were 171 protected passages from the original site that were all machine checked on every build and all Fable did was orchestrate writing in character connective tissue between those passages and then Elsa checked and validated it. The persona that mattered the most to me and Elsa was Maya, a blind reader on voice over with a braille display. She asked for things that the original design didn't want to give her, right? navigable headings, meaningful link text, a real image description instead of a joke, and she outranked the design. All of what she wanted shipped. And Fable went so far as to test as Maya to make sure that her experience was good and went to the trouble of creating a spoken voice over of the site that she could play to help her understand the site, which is something Elsa's always dreamed of and never had time to put together. Now, Elsa's the real judge here, and she looked through the finished site, and as someone with professional accessibility work under her belt, she was shocked because she gave this build nothing. There was no brief, there was no brand notes. Uh she it was it was like a five-word prompt, right? And I just ran with it with with a team of agents. And it learned to use her color palette, it learned her voice, it learned her book cover, and it went all the way to a W keg 2.2 2A standard, which is something that very few websites in the world actually beat. And so this is something that instead of taking 6 days for her with one agent last month, took an hour and a half or so, maybe 2 and 1/2 hours at 8 bucks. And Elsa's assessment is that this site is so much better than the last one. So it's cheaper, it took less time, it's way better. Why aren't we using more multi- aent systems? And I think the answer is really simple. It's scary. It's hard. It feels intimidating to look at 20 agents. And that is what I am trying to to take away as an objection with this video. It is not hard to do multi- aent systems, especially not in MIT 2026. We have recipes now to do work like this that we never had before. And the whole reason we do it that way is so you can skip the plumbing and start working on your first job. And that's where I want to leave you. If this is so easy that we can all do it, then it's just about making sure that we understand the kinds of tasks we can ask agents to do. And that's actually one of Elsa's takeaways. She and I were talking after the website and she was telling me, "I didn't realize that multi-agent systems make such a massive difference in the kinds of work you can get done and I need to start thinking bigger about how much work I give multi- aent systems." That's really true. I if you are thinking of a piece of work and you're like, I don't know if AI can do it or if it feels too big. I'm trying to put together a tool set here that you can use to get that work done. And if you don't touch a terminal, this one's for you because Elsa doesn't touch a terminal either, right? Elsa doesn't feel super comfortable running swarms. I wanted to take a noncode ccentric task. Yes, I know code was used in the website, but it's not centered around code. It's centered around the value of telling Elsa's story on the web. And I wanted to make sure that I could show that multiple agents help tell that story in a way that you just can't get to even with a frontier agent doing really good work even in a great harness like Codeex. This multi- aent pattern is very close to hitting mainstream. I'm sharing it with you because it's just breaking out of engineering circles now and I want you to be the first to grab it. When it breaks loose, the headlines are going to look like, "Hey, AI built this website for eight bucks." I don't think that's the right headline. I think a better headline is that we are now able to delegate bigger, more muscular, more ambitious tasks to AI and as a result, we can get more done. Elsa always wanted an accessible website, but she was so busy bringing accessibility to others, she didn't have time to actually sort it out for herself, so the agents did. And I think that when you think of that kind of work in your world, whatever it is for you, it might not be accessibility, it might be anything else under the sun that you think you can tackle with computing with agents, this is what you can use to do that affordably. And yes, you can use the power of Fable to get there without the money that Fable would otherwise be spending. Who wants to spend a hundred bucks when you could be spending eight, right? Like you don't want to do that. So you might only be one afternoon away from that work that you want done. And it's not because the models got magical. It's because actually orchestrating multi- aent systems has gotten simple enough that I can talk about this and share this and it's really very doable. And that's happened like really in the last 30 days or so. So have fun. Go jump into it and tell me what you build with your multi- aent system. I can't wait to hear
