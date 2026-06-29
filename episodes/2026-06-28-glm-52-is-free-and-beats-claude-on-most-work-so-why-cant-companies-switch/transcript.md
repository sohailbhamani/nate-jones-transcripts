---
title: "GLM 5.2 Is Free And Beats Claude On Most Work. So Why Can't Companies Switch?"
video_id: "Zp8lr6IzUnQ"
youtube_url: "https://www.youtube.com/watch?v=Zp8lr6IzUnQ"
publish_date: "2026-06-28"
duration: "17:36"
duration_seconds: 1056
view_count: 6973
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Full post: https://natesnewsletter.substack.com/p/glm-5-2-context-lock-in?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  GLM 5.2 is a free, open-source model that often beats Claude on everyday work, yet companies still pay frontier prices. The real bottleneck is no longer the model call. It is the last mile around it: context, routing, and harnesses.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening when intelligence gets 98% cheaper but your company's context stays trapped?
  
  The common story is that a cheaper, better model means you should switch, but the real question is whether you can move your context, not whether the model can answer your prompt.
  
  In this video, I share the inside scoop on GLM 5.2 and the last mile of cheap AI:
  
   - Where GLM 5.2 can safely replace an expensive frontier model
   - Why switching models means replacing a whole work system, not a call
   - How Claude Tag turns your team's Slack context into a sticky harness
   - What builders and agencies can do to own the last mile
  
  Cheap intelligence is real and it is here, but the edge in 2026 belongs to whoever can build the harness and keep their own context instead of renting it back from a frontier lab.
  
  Chapters:
  00:00:00 Why GLM 5.2 blew my mind on everyday work
  00:02:22 Cheap AI is here and frontier releases are slowing
  00:03:41 Why companies still aren't switching to open models
  00:04:11 Center of distribution vs edge of distribution tasks
  00:04:53 Lindy rebuilt its whole harness to leave Claude
  00:06:39 A model is a brain in a jar without a harness
  00:07:23 Claude Tag and the rise of team-level harnesses
  00:08:47 Why you can't rip out a model that owns your context
  00:10:36 The harness talent shortage is a builder's opening
  00:14:50 Take the last mile seriously before you rent your brain
  
  Listen to this video as a podcast.
  
  Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "glm-5.2"
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
  - "GLM 5.2"
  - "open source AI models"
  - "Claude Tag"
  - "AI harness"
  - "model routing"
  - "GLM 5.2 vs Claude"
  - "open source AI for business"
  - "cheap AI last mile"



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Career"
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
    - "Slack"
  people:
    []
  products:
    - "Claude"
    - "Codex"
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "By the end of this video, you should know where GLM 5"
keywords:
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "codex"
  - "coding"
  - "frameworks"
  - "leadership"
  - "make"
  - "openai"
  - "slack"
---

# GLM 5.2 Is Free And Beats Claude On Most Work. So Why Can't Companies Switch?

I tried GLM 5.2 and it blew my mind. By the end of this video, you should know where GLM 5.2, an open-source model, can be clawed, where it can safely replace an expensive model, and where switching models is a bit of a trap because you're not replacing a model call. You're actually replacing a whole work system. And that's the thing I want to draw through in this video. So, let me start at the beginning here. GLM 5.2 did not fake impress me. It actually impressed me because it's not just cheap, and it's very cheap to run on the cloud, it's free if you set up your own servers, and for a lot of normal work, it's incredibly good. It's It's often better than Claude. And when I say normal work, I mean the fat middle of everyday AI tasks, right? So, if you're setting up a brochure site for a client, if you have a PowerPoint outline, it's a pretty standard deck. For a first pass copy, routine synthesis, for coding tasks that are tackling familiar problem types in coding, these are tasks with familiar shapes, with lots of examples, with outputs that a human can check quickly. The nerdier phrase for this is that this is the middle of the distribution work for AI. In other words, what you are getting is what someone has tried with models millions of times before, where the answer pattern is pretty normal, and the output is pretty easy to inspect. How many different brochure sites have you seen, right? In that world, GLM 5.2 is incredible. It's fast, it's cheap, it's easy, and it's extremely high quality. It's higher quality than Claude. And a lot of those tasks, I don't think it's honest to say it's just good enough. I think it's It's more accurate to say this is the best model in the world at those center of distribution kinds of tasks, especially ones where front-end taste is important. And so, this is not a video about GLM 5.2 being bad, even though it's not my daily driver, and I'm going to explain why. And so, GLM 5.2 is incredible, but I'm still not using it every day. And in fact, a lot of companies I know are really struggling with the idea that they want to transition to more of a generic router where they can route to the cheapest model available, but it's not actually easy to do in practice. Why is that, right? We're going to talk about why that is, talk about where open source is going, talk about what the shape of work looks like in 2026, and we're going to tie it back into GLM 5.2 and the way we actually need to build to take advantage of models like this. Because cheap AI, it's not a theory anymore. Cheap incredible AI is here. In fact, it's going to be here more and more and more and more because the US government is now slowing down frontier model releases. 5.6 is the latest model to be affected. It's apparently going to be released customer by customer, which is code for we don't know when we're going to get it. For the first time, there is no defined expected cadence for future model releases that are frontier, even though the labs are still doing a phenomenal job training and reinforcement learning their models. And so we're going to have more and more of this open source conversation. And a lot of the open source conversation is frankly about moving down the cost curve, right? Because these frontier model costs are expensive. If you're running a company, they get really expensive. There are stories going around where the numbers are absolutely eye-popping. Like one engineer spending $80,000 in token costs in a week. That's a lot. So if you have that kind of pricing power, if people are spending tens of thousands of dollars a week on tokens, there's an a tremendous amount of incentive to make these models work. So why is it so hard? Why are why are we not seeing a tremendous tipping point away? Why are we still seeing Anthropic growing their revenue like crazy, OpenAI growing their revenue like crazy when these incredible good models exist? Well, there's a number of factors to that, and I want to list them for you so that you can actually understand the perspective. This is based on talking with engineers at companies as well as with leaders. The first one is the ergonomics of work. If you are just trying to get something you've heard about, seen about, you have a frontier model at you have a frontier model at home on your phone, you just want access to that. There's a lot of employee pressure around Claude and around OpenAI in a way that there just isn't for open source models. So, that's one piece. Uh, and it's not small. Like, when people are asking for it vocally saying this will help my work, overburdened IT departments tend to listen to that. Number two, it is actually very, very difficult to correctly figure out whether your task load is center of distribution or edge of distribution weighted. If it's edge distribution weighted, you actually do want the frontier models. If it's center of distribution, the open source models are going to be really, really good because they're common patterns. But, people don't They're not used to measuring their work that way. Individuals aren't, teams aren't. if you're a company trying to figure out what is your model strategy, you kind of got to tackle what is your distribution of tasks? And almost no one has asked that question properly yet. And people are trying to figure out how to measure that. The folks that have gone the farthest, actually, are folks like Flo Crivello, who is, uh, leading the Lindy team, and who very publicly wrote up his journey to a deep seek architecture away from Claude. And, you know, he saved a lot, etc., etc. But, he was also very honest about the fact that the Lindy team had to essentially rewrite their harness from scratch around deep seek, and they could not just take all of their systems for working with Claude, all of their prompts, all of the way they handle memory, all of their tool calls, and just automatically lift and shift. It doesn't work that way. These models need their own harnesses. He was incentivized to do that because he is literally serving AI as a service, and if he can deliver a cheaper and more effective service that hits his margin, and it's it's tremendously impactful. For folks who are using AI internally for coding or for back office automation, that ROI is not as clear, and the incentive to move is not as clear, either. And so, what I have seen, and I have seen anecdotes from this, not just from Flo, but from other folks that I know personally. I know entrepreneurs who are wrestling with this today. The ones who are actually making the jump to open source and dealing with the different system prob dealing with the different tool called dealing with a different memory architecture, etc. That is tuned around the fact that these are center of distribution models. Those guys or those gals are focused on ROI for a particular AI tool they have in market. Just like Lindy, they see value back in their pockets when they can cut their token costs. And for everyone else, because the incentive is not as strong, you don't have the same commitment to wade through the challenge of building a harness. And that is not a small thing. And one of the things I want you to take away from this video is that a model can be an incredible [snorts] brain in a jar. And it it just isn't useful to you without a harness. And so this is why I pay a ton of attention to harness innovations. And I want to name a couple that are top of mind as we look at GLM 5.2 in context. First, I notice that GLM 5.2 was released with its own Codex clone harness. That's one piece that I pay attention to. It looks like the open source model makers are realizing they need to deliver harnesses as well. And so I would expect more innovation in that direction. I notice that Codex is starting to call out publicly that you can use Codex the harness without using any OpenAI model. That's notable because there's a different path to value for OpenAI there. Maybe OpenAI's models are the default, but if they're calling out that they are actually the harness for all of work, it gives them a way to be stickier long term. Three, the Anthropic team is not just sitting there as all of these developments happen. They launched Claude Tag this week, and Claude Tag is an incredibly sticky product. It is a team level harness, and team level harnesses are where the energy is going because so much of the work we've got is individually productive work in AI. It's not team productive work. And we're trying to figure out, how do we align our efforts that are individually productive into something that is team productive? And Claude tag, which is just tag Claude, anyone can tag Claude and get work done in Slack, is one of the first examples of a sticky viral consumer team harness. Where like if you're an ordinary knowledge worker at a particular company, you can envision using that as as a team harness. And you don't have to know the word team harness, it's just going to work. You tag Claude and it works. But look at it strategically from Anthropic's perspective. Now they're not just getting the engineers. Now they're getting everybody who's a knowledge worker in Slack and they're reading all of the messy context that lives in Slack that no one knows how to codify and that is now getting fed into Claude automatically and it can be something that the Anthropic team learns from within privacy policies long term for Claude in the context of that company to start to own the harness itself in a way that no company can get away from. It's an incredibly sticky experience because you think about it. Let's say you you know that GLM 5.2 is a lot cheaper, which it is. It's like 98% cheaper or something like that. If it's that much cheaper than Claude and it's just about as good on most tasks, it is rational to build a routing system and assign most tasks to GLM 5.2. Except that hey, are you going to have Claude tag, right? Are you going to go to tag in Claude on that stuff? Is that convenience going to be there? Are are you going to have to restart the job of giving this AI context from your company because Claude magically acquired it in Slack and you didn't have to think about it? We have taught companies for decades that data is alpha. Data is something you have an edge with if you're serious. If data is alpha, what do we think about giving all of that data to a frontier model provider as context? Even if they don't release it into training data, even if they if the privacy policy is really good and they're behaving really ethically, which I have no reason to think they're not, you still are effectively renting your own context back to yourself because Claude is going to be in your slack as a team level harness and is going to be incredibly close to all the work your team does and it's going to be impossible to rip out. No matter how cheap the GLM 5.2 class models are, how can you rip out the model that's that close to context? And I think that the GLM 5.2 team knows this. That's why they released a harness, a Codex-like interface with their AI. It's a first stab at it. But we got to get much farther there in tech, where the companies that know they need harnesses generally cannot afford to hire the AI talent to build those harnesses unless they're extraordinary companies because that AI talent is so in demand right now that it can charge anything it wants and it usually goes to one of the hyperscalers or another large company. And so we're in the dynamic where the only companies that can build their own last-mile harnesses, their own auto routers, are companies that can afford that, that can afford the AI talent to do that, which is very scarce. And so if you actually think through this dynamic with GLM 5.2 and how it's possible but at the same time we can have an incredible open-source model that we're excited about and also that Anthropic still has pricing power to charge a lot for their tokens even though their tokens are just marginally better, it's actually not a story of intelligence. It's a story of the last-mile in AI and the fact that the talent to build the last-mile in AI is incredibly scarce. Which should, honestly, for a lot of you watching, be a source for optimism. If we have that scarce a talent, where people are ending up locked into contracts with a frontier model provider because they don't know how to build a harness for themselves, wow is there a lot of opportunity in knowing how to build an AI. Like it's an incredible opportunity right now. It is not easy to do this work. It's not easy to know this is how you handle a tool call in GLM 5.2 and how you should do it differently from Claude. So does figuring out how memory will work for that system. So does figuring out how the system prompt needs to change because it's a center of distribution model. It's a lot of technical work. And if you know how to do that work or know how to do parts of that work to essentially refactor agentic pipelines so they work with an open-source model, you are going to be incredibly in demand. Especially if you compare that with the ability to route tasks where you can take a task and recognize on the fly that it's a frontier model task and it should go to a frontier model versus everything else going to a cheaper open-source model. That is going to be a huge investment theme for companies in 2026, 2027 and they're going to keep innovating. Claude tag is a fantastic example of how of how incentives in frontier close-source models are giving us incredible experiences. If you have pricing power, you are heavily incentivized to make sure that your experience is as convenient and ergonomic as possible. And so features like Claude Claude tag are going to appear really, really fast, really rapidly, really completely from teams at Anthropic, also from OpenAI because they're incentivized to keep those those prices high and to go after that business. And with open-source models, you don't have the same margin to work with, you don't have the same cash flow to work with and you don't have the same incentive to dig in and deploy thousands of forward-deployed engineers and really make these harnesses sing. And so one of the really interesting facts that we come to after all of this can simultaneously be an incredible model, a model that a lot of entrepreneurs switch to when the ROI is clear and they're technically savvy enough to do it, and also not a model that is easy for a given company that you turn up in phone book to actually use. It any given company is going to have to think about how they use GLM 5.2 to use it usefully, and they're going to have to think a lot less to sign up for a frontier model contract that's going to fit right into their existing workflows. That last mile is literally a trillion-dollar last mile in AI. And one of the biggest open questions right now is whether we will scale our talent fast enough to enable businesses to tackle that problem set without paying so much that they can't afford it. I don't know what the answer's going to be, but that's a question we're going to have an answer to. We will all collectively answer together in the next 3 to 6 months. We are going to find out, especially as the US government has this effective pause in place on frontier model releases, and the open-source systems are going to continue to be available, we're going to find out whether companies can adjust to the fact that intelligence is 98% cheaper and takes a last mile to build. Can they actually build that last mile? Can they find teams to build that last mile? If you are in an agency or in a consulting space, this is a golden goose moment. Like you have a chance here. You can really go to town and basically promise to save people a ton of money on tokens as part of your ROI proposition, as long as you can deliver that refactor in a way that maintains quality, which is not a trivial task. If it was easy, we wouldn't be having this video. So, where does this leave us? GLM 5.2 is an incredible model. It is important not to shame a model or diss a model because it's good at center of distribution task, because by definition that is most of our work. Collectively as a species, most of our knowledge work is center of distribution, just by definition. And if that's the case, a model that's really good at that is worth taking really seriously. And if we take it seriously, that means we have to take the last mile seriously. We have to take the idea that we need a harness for that last mile seriously. And that's a lot of what I have been doing in public is starting to articulate what it takes to build a harness, whether it's open skills or open brain or open engine, which I've all talked about on this channel. How do you start to take these pieces and put them together in a way that is agent agnostic, that is model agnostic, so you can start to install those pieces and actually take advantage of all the intelligence on tap. Whether it's Claude, whether it's it's Codex, whether it's Hermes, whether it's whatever whatever system you want, whether it's your own iPhone 2, you should be able to easily build to that last mile. And and I know that there's a lot of custom work for individual companies, and that's why I keep saying this is a time for builders. But if we don't start down that path, we're essentially going to be renting our company brain and company context back from the frontier model providers. And they're going to have it. And they're going to be able to use it to continue to improve their systems and make them more useful, and they'll be incredibly convenient, incredibly sticky products. And what are we going to do? We're going to have to use them. So, this is a very pivotal moment for corporations. The firm has never faced a moment where the firm's brain has been on rent. And that is what we're on the verge of with tools like Claude Tag, which are incredibly useful. I'm not saying they're not useful, they're very useful. That's exactly the dangerous thing. So, I would encourage you if you are even if it's a tiny company, let's say you're building your own agency, you're an individual entrepreneur, think seriously, just as you would if you're a larger company leader, think seriously about whether you want to rent that context and intelligence or not. Think seriously about where you want to go with your context long term. Ask yourself, do you have an idea of the distribution of your tasks? Do you have access to technical talent that you can use to build out that last mile? What are the task sets that you would want to assign that would save you a ton in tokens? A lot of people don't sit down and get pencil and paper and actually ask themselves those kinds of questions. And I have a whole sort of question set that's in more detail that I've been going over with leaders. I put that on the Substack. Uh but this is a really serious thing. This is a moment for open source. GLON 5.2 opened that door for all of us, and it's going to be up to us to see how we take advantage of it. Good luck with that. Cheers. Bye.
