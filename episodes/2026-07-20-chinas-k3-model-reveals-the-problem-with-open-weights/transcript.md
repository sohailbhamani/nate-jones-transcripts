---
title: "China's K3 Model Reveals the Problem With Open Weights"
video_id: "2ZpZhsjoUK4"
youtube_url: "https://www.youtube.com/watch?v=2ZpZhsjoUK4"
publish_date: "2026-07-20"
duration: "18:46"
duration_seconds: 1126
view_count: 16308
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  My benchmarks: https://unlock-ai.natebjones.com/benchmarks/kimi-k3?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  Full post:
  https://natesnewsletter.substack.com/p/kimi-k3-open-weights-cost?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  Kimi K3 is Moonshot's new open-weight AI model, and it complicates the story that Chinese open models are cheap, efficient, and closing the gap on the frontier. Here's what it actually costs to run, and what it means for OpenAI, Anthropic, and the future of open source.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening with China's new open-weight AI model?
  
  The common story is that Chinese open models are cheap, efficient, and catching the frontier, but the real question is what K3 costs to run and what still needs a closed model.
  
  In this video, I share the inside scoop on Kimi K3 and the real economics of open-weight AI:
  
  - Why downloadable weights still need 64 accelerator chips to run
  - How K3's heavy token use erodes its apparent price advantage
  - What the "efficient Chinese model" narrative gets wrong about serving
  - Why open weights raise real cyber and governance risks
  
  K3 is a genuinely strong open model and a useful pricing check on the closed labs, but treating open weights as cheap, safe, or frontier-equal will cost you.
  
  Chapters:
  00:00 Kimi K3 is Moonshot's new open-weight model
  00:53 Why K3 is a big, heavy model to run
  06:20 The cheap-and-easy open source narrative is outdated
  14:05 Governments may restrict model distribution
  17:04 Why K3 is an inflection point in open source
  
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
  - "Kimi K3"
  - "Moonshot AI"
  - "open weights"
  - "open source AI"
  - "AI inference cost"
  - "Chinese AI models"
  - "running AI models locally"
  - "ai news"



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
  people:
    []
  products:
    - "LM Studio"
    - "Make"
    - "Opus"
  models:
    - "DeepSeek"
concepts:
  []
summary:
  - "# China's K3 Model Reveals the Problem With Open Weights

Open source changed again"
keywords:
  - "ai-news"
  - "anthropic"
  - "coding"
  - "frameworks"
  - "lm-studio"
  - "make"
  - "openai"
  - "opus"
  - "workflows"
---

# China's K3 Model Reveals the Problem With Open Weights

Open source changed again. So Kimmy K3 is a brand new model from Moonshot and they released a brand new open-source openweights model. Now I say open weights, it's actually coming like July 27. They're going to release the open weights. The reason you should care is that this changes the dynamic of opensource. So open- source like what I have traditionally heard what a lot of people hear and think about open source is one hey it's cheap to run and two hey it's really efficient to run and sure there are a ton of models that fit that rubric but today I'm going to talk to you about how Kimmy K3 breaks that assumption in some really important ways and why we should pay attention because it tells us about where the race is going and it tells us about where we should be putting our personal compute dollars. So, let's pay attention and dig in. All right, so first Kim K3 is a big model. They say at top performance, you need 64 accelerator cores to run this model. I'm going to give you a hint. You don't have 64 accelerator cores at home. I like 1% of you do. A tenth of 1% of you do. Almost nobody has that at home. That is a corporate installation kind of footprint. It is a big model. It is a heavy model. Now the good news is you get performance for that and so if you do run it you get near frontier not really Fable 5 but close to Fable 5 coding performance. It falls off in some of the other areas. It doesn't have safeguards effectively like it has a few. It has the usual ones that Chinese models have. If you're trying to fine-tune a model, Fable won't let you. In fact, Fable will be very upset at you for that. It is guardrail not to do that because that is part of how Enthropic is trying to protect their proprietary information. On the other hand, Kimmy K3 will be happy to help you fine-tune a model. And so there are some legitimate use cases that closed source models have kind of locked off that Kimmy opens up. And so even if it is not quite at what is out there right now in the public market, if it's like a shade or two below the frontier that's publicly available, you still get some nice capabilities you can't get any other way. And so I think that there are going to be a bunch of use cases for Kimmy K3 that are going to pop out of the woodwork, but efficiency and using it because it's cheap isn't one of them. Now, part of why is because you have to spend a lot in compute to run that thing. But also part of why is because if you don't and you use the cloud model, Kimy's pricing is kind of expensive in two different dimensions. Stick with me. First, Kimmy is pricing in multiple dollars per million tokens, which if you're used to Chinese models, is already expensive. It's already up into the frontier pricing tiers right now. It's not as bad as Fable's not 50 bucks, but it's getting up there. I think it's it's 15 bucks uh per million output tokens. So, Kim is not cheap. But Kim is also not cheap because it uses more tokens to get to the answer. And so part of how you save money with a model is you have the model use less tokens to get to the answer. And Kimmy K3 for a given answer that it gets to uses a lot more tokens than OpenAI's models do that like that 5.6 or 5.5 does or Fable 5 does. Right? These models that are on the frontier, they may be expensive, but they're very token efficient. Relatively speaking, Kimmy K3 is not as efficient. Now, here is where we start to get into the implications, and I want you to stick with me here. If we have the old deepseek narrative on Wall Street, it turns out that inference is kind of a subset of the distilling and the back propagation that they have to do to get the model trained up in the first place from a seed, right? From a a a topography, a set of parameters that they're able to distill down from an existing Frontier model. And if you have to do back propagation across that part of that process requires inference. And so if you think they're efficient at that, they should be efficient at serving the model. And so the fact that they're not suggests that some of the narrative that we have been given around how Chinese model makers are incredibly efficient may not be as true as we think. I'm not saying that there's not like great innovation going on. Don't get me wrong, there's a lot of cool innovation going on here. It is incorrect to say it's just distilled. That is absolutely not true. There's a lot of good stuff. But it doesn't mean that it's just a story of efficiency. And I hear so often, well, Chinese modelmakers are incredibly efficient. I would actually say the evidence we have suggests that open AI is incredibly efficient at serving models and that anthropic is becoming fairly efficient at serving models and that Chinese model makers are behind on serving models efficiently which suggests that net net from a knowledge perspective the major labs remain ahead the closed source labs anthropic and open AAI and I will go further and I will say we often mistake comparing comparing the existing frontier model in the marketplace with the existing internal model benchmark in the lab. The true frontier in American labs is what is not released. It is what is in the lab. Fable is is has been out inside the lab for at least that long and we're just getting it now. And so when you think about the narrative that Chinese models are catching up, you have got to start benchmarking correctly. They are still about six or seven months behind just like they were a year ago. And I see a narrative where it's like, wow, they're almost close to Fable. They're almost close to, you know, 5.6. They'll pass them by the end of the year. I've seen that take. That's just incorrect. The model makers are well past that now. It'll be another four, five, 6 months before we see what they've got internally. They will do even more safety testing because it's a risk now, but they're not catching up. And there's no sign that they're imminently catching up. The closed source models in anthropic and open AI have a tremendous lead and they're not letting up right now. Now, we can talk about what that means and we will, but one of the things that I want to push back on is the narrative that we have efficient, open-source models that are cheap and easy to run that are at the frontier or catching up. That none of those things are completely true anymore. And in fact, and this is one of the larger implications I want you to take away, as we push models forward toward the frontier with larger and larger and larger Chinese models, we are going to get to a point where we have more and more expensive models to serve because you have to scale them up to get them to the frontier, right? You cannot just sit there and say, "We will magically make them small and small and small and they will somehow match frontier performance." There is no free lunch here. you're going to have to start to scale them up. And when you start to scale up the models, it gets harder and more expensive to serve. It's less efficient to serve. You have to get more compute to serve. Which means that we are going to have to face the reality that open-source models are not closed source, that they come with real costs to serve, whether you're paying that in computer chips or you're paying that directly to the provider, and that they're not going to be as good as closed source for the foreseeable future. None of which should imply that we shouldn't use them. Open source is a valuable tool in the arsenal. I did a video on open source just on Sunday and why it's important to have that in your toolkit. I think it's fantastic. I think you have a wide range of open source models now and I love that. They've never been easier to work with. But we should not mistake that availability for the performance level that we get at the frontier. And so I come back again when I look at the future of computing. I want to draw a few core lessons out for us at the end just like I said I would. Lesson number one, what your approach is to AI safety for yourself, your family, and if you have a company, your company. And the reason I say that is because with this model Kimmy K3 that dropped, we have now crossed the frontier into open-source models being cyber threats and we're just going up from here. You need to think about the reality that these open- source models, just like I said, I said a couple months ago this would happen. We are coming into a world in the second half of 2026 where these open- source models are going to be everywhere on the internet. They are going to be cyber threats and they will be used as cyber weapons by bad actors. And so you need to be asking yourself, what do you need to secure your family? What do you need to do to secure your company? And I'm going to give you some specific tips based on best practices. You also need to take the time to do a full audit cuz I don't know your full system. So one, get a hold of the strongest model you can. Fable's a good example while we have it. Make sure you use it to audit any software you have and look at it from an adversarial posture. Is it safe to use? Are there leaks that you don't intend? Is there malicious code somewhere? Is there not even malicious code? Is there code that is just buggy and leaking something out that shouldn't be? Is it accessible from an adversarial perspective? How do you set up your software so you have a more secure posture given the best model you can get a hold of? Now, how do you think about multiple layers of defense when it comes to your cyber identity for your family as well as for any software assets that you have? And so in software, we talk about the idea that you have multiple layers of defense from social engineering, from software attacks, etc. And so that a software attacker, a hacker cannot get in through just one ring of defense and get the whole thing. They have to like go through multiple layers of defense. You can catch them along the way. With our identities, it's similar. You want to be in a position where you can protect your identity through obviously the old stuff like varied passwords, uh, two-factor authentication. You want to be able to wherever you can move from just a textbased authenticator to a more secure like fingerprint-based or maybe a uh USB-based authenticator where you have that key and wherever you can you want to move from just a password to 2FA not just 2FA with a text but like 2FA with an authenticator app something like that where you actually have multiple secure ways to verify your identity for digital access. You also want to make sure that you are looking at how identity works in the digital age with AI. So you should have a password with your family, something that you would never normally use in conversation that the whole family knows that if you use that word, it's really you. But if someone clones your voice, if someone clones your likeness and they call that that digital persona is not going to know that secret word or that secret phrase, and they're not going to be able to guess. And that way your family will know if there's some sort of digital demand for ransom, it's not really you. It's it's some people who are hacking them and they will be able to avoid wiring a bunch of money and losing money. And this is personal to me, by the way. Uh my grandfather lost a lot of money to wire fraud. Uh we never got it back. Um and they took advantage of him. He had dementia and it was terrible. So it's it it is a real thing. It happened in the past before AI. It will happen more now. It will happen especially as we have these capable models that make it easier and easier and easier to simulate speech to simulate uh likeness to simulate sophisticated hacking programs. In this case, Kim K3 is very much on the hacking program side. There are other models that have come out recently on the voice side on the video side that are also if you assemble them a scary combination. So, make sure that you protect yourself. That's lesson number one. Lesson number two, and there are three of these. Lesson number two, make sure that you recognize that we are moving into the age when your imagination and ability to pose the right question is what is going to matter. And I'm thinking about that more and more, not just with Kimmy K3, but with Fable coming out now with 5.66 is on the horizon. Opus 5 is about to come out. In that world, you are going to be tested for your ability to ask questions. You can't just sit there and say, "I already have a job for AI. This is the job for AI, and I'm going to give it." I talked to someone recently who was really honest with me. He said, "I'm just not giving Fable something interesting to do." And I said, "Well, let's just kick it around. Let's talk." And as we talked, as we brainstormed, he came up with like three great use cases that only Fable could do. But he needed to brainstorm with someone who knew Fable to kind of kick that around and get that sense of what that model could do. so he could figure out where the value was. We need more of that. Now, my Substack community has that and that's great, but wherever you're getting it, it doesn't have to be with me, you got to find people who can help you grab onto that imagination and start to ask bigger questions because otherwise you're not going to be finding new and creative ways to use AI and that is going to be where the alpha is. The alpha is not going to be in the predetermined stuff that everybody else already also knows. It is going to be in your imagination married to AI driving toward human connection and building experiences that are incredible. And that requires yes touching grass which is great but also making sure that you have the imagination to ask really interesting questions of AI because that is where you get the most creative and powerful responses from very very strong models whether they're open source like Kimmy K3 or whether it is fable or whether it is 5.6 or whatever future model we have in a month. The models have hit another inflection point. That's where we are going. Lesson number three, we need to plan for an increased risk that governments are going to get more and more involved in hampering the distribution of models over the next 6 months. As I've been saying all the way through, models are getting more capable. Kimmy K3 says that moment comes to open source just as much as to close source, which is exactly what we should expect. If that is the case and we keep seeing scaling and we get to an open- source model that is fable level truly and then maybe one that is mythos level by Christmas time, we should expect governments to start to pay attention and restrict. And I don't just mean the American government. There there are some rumors coming out of China that the Chinese government is thinking about restricting certain tiers of open-source models and not letting them out into the world in the same way they are right now. We don't know where that's going to end up, but net net looking at increased government involvement in model makers would lead us to suppose that we are going to have to plan for a multimodel diverse future if we want to have artificial intelligence around. And that's the good news for Kimmy K3, right? Because Kimmy K3 is another model in our arsenal. We can figure out how to serve it. Yes, they're going to drop those weights on the 27th and we can grab them and they we can have other models, right? It's not just Kim K3. We can have a bunch of models locally. We can have a model garden if you will. Uh and we can also have access to cloud models, etc. The point is we are going to be in a world increasingly where all of computing is trending toward being tokenized and therefore in order to compete we need to not be vulnerable to any given disruption, right? Whether that's an anthropic issue or maybe an open AAI issue or maybe there's some Chinese model issue, we don't want to be disrupted anywhere. We want the ability to tokenize regardless. And that is a theme that is really really big right now as we look at what happened with Fable and Mythos and juxtapose that with the availability of Kimmy K3 and just flatline project that out to the end of the year. If you look at the capabilities, you look at how worried governments are now, they're not going to get less worried and we should expect more surprising policy and we should plan for that. And I think that that goes for individuals as much as for companies. Yes, companies need to plan for it, but individuals, if you want to make sure that you have the ability to get the intelligence you want to get stuff done, you got to plan for that, too. Maybe that means LM Studio like I talked about on Sunday. Maybe it means making sure you have multiple subscriptions to different cloud providers. You will have to decide what your risk tolerance is. But you should assume you need at least one model and at least one backup model and make sure that you are comfortable with the risk profile that those models represent. So wrapping all of this up, where does this leave us with Kimmy K3? Kimmy K3 is an inflection point in the opensource race. It is by far the best model that we have seen come out. It reminds us that even if open-source models are trailing Frontier models by about the same margin, they are also ipso facto still scaling at about the same speed. They are getting incredibly good. And so Kimmy K3 is not even about whether it's behind. It's about the fact that it's an incredible coding model that's being released and that you can use to drive a tremendous amount of value. So, if you haven't used it, go give it a try. I've been playing with it. It is like many open- source models, a little bit narrower in terms of what it can do, but the coding in particular, its ability to code is very, very strong. Tell me if you're using it. Tell me how you're comparing it to Fable, how you're comparing it to OpenAIS 5.6. I'd love to see specific examples of stuff you've built back and forth in the comments so we can kind of dig into it. There are places, as I called out, where it is going to be stronger. If you want to straight up dig into a particular piece of software and rip it and copy it and just make a clone, you will often run into, oh, I don't do that from Fable or even maybe from OpenAI. You will not run into that issue from Kimmy. And that is going to be a specific application that is going to be very very popular with people who are trying to replace SAS solutions and do so affordably. And so I can see some of these dots connecting. I'd be curious what you're building. Let me know in the comments. I'll see you next time. Cheers.
