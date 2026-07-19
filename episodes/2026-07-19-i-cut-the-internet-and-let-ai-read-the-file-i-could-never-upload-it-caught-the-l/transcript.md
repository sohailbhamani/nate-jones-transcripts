---
title: "I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak."
video_id: "5slsNizN6MQ"
youtube_url: "https://www.youtube.com/watch?v=5slsNizN6MQ"
publish_date: "2026-07-19"
duration: "14:04"
duration_seconds: 844
view_count: 3448
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Full post with a guide to clean sensitive documents: https://natesnewsletter.substack.com/p/run-ai-offline-private-files?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  How to use AI on the files you can't upload: run a downloaded model on your own laptop, with the internet off, and grade what's actually safe to send. Microsoft is building this for enterprises. This is the version that fits on one machine.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening with AI and the data you can't put in the cloud?
  
  The common story is that private AI means a bigger enterprise contract. The real question is which of your files ever needed to leave your laptop at all.
  
  In this video, I share the inside scoop on running AI locally on sensitive work:
  
  - How to run a downloaded model on a document with the internet off
  - What Microsoft, Bayer, and Discovery Bank do with data they can't upload
  - Why a model can obey while the product still uploads your file
  - Why "free" open-weight AI can still deepen your dependence on Microsoft
  
  You can finally put AI on your most sensitive work, but only if you stay honest about where the file goes and who you now depend on.
  
  Chapters:
  00:00 The offline proof
  00:49 Discovery Bank and Bayer go private
  02:21 Do the small version on your laptop
  03:13 The Grok Build leak
  04:19 LM Studio and the sensitivity preset
  05:41 What the offline model caught
  07:19 How Microsoft does it with LoRA
  10:05 For leaders: enterprise versus SMB
  11:40 The catch: dependence on Microsoft
  12:28 Open source is not automatically free
  13:40 Get the guide
  
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
  - "LM Studio"
  - "local AI"
  - "private AI"
  - "Grok Build"
  - "LoRA fine tuning"
  - "run AI offline"
  - "how to use AI on sensitive files"
  - "ai privacy"



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Microsoft"
    - "Azure"
  people:
    []
  products:
    - "LM Studio"
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# I Cut the Internet and Let AI Read the File I Could Never Upload"
keywords:
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "azure"
  - "career"
  - "coding"
  - "frameworks"
  - "lm-studio"
  - "make"
  - "microsoft"
  - "openai"
---

# I Cut the Internet and Let AI Read the File I Could Never Upload. It Caught the Leak.

The laptop I'm about to show you has no internet connection, but it still has AI. A downloaded model just read a contract. It found private material inside that should not go to any kind of cloud AI. It masked all of that private information, and it refused to call anything that was unreadable safe. In a few minutes, I'm going to show you the entire thing. But first, I want to show you why Microsoft thinks this small idea becomes an enormous business. You have a contract. You have a Word doc. Maybe you have a customer file that you want AI to help you with, and you stop because you don't know where it goes after you upload it, right? Or you do know, and you don't want it to go there. Big companies are spending a lot of real money to solve that exact problem, and I'm going to show you today how you can solve it for yourself without spending a lot of money. Banks, of course, are one example. Discovery Bank fine-tuned five variant models across two smaller Microsoft source models for separate functions across the company dealing with confidential information. So, they're dealing with company-specific financial language, SQL formats, custom templates, stuff like that, right? Not only was that safer, but Discovery calls out that it was faster and funner, too, right? So, the average response time from their new on-premise models that they fine-tuned fell from five or six seconds to one and a half or two. Bayer, a medical company, taught a small model its own proprietary crop label data and its own regulatory rules so that it would not have to send any proprietary information into the cloud. Advisors spent hours, sometimes days, working through labels that can run past 100 pages. Before the crop label data model was sorted out, Bayer advisors would spend hours, even days, working through that crop label data. Not anymore. Apparently, now it gets done in under 30 seconds. Both of these systems run in Azure, not on a server inside the customer's building, but in a place that only the customer can control. I will come back to what Microsoft protects inside that boundary and what remains Microsoft operated because I think it's important to distinguish that, but I think ultimately this is where a lot of enterprise AI is going. Not one chatbot that magically knows the entire company, but specialists that know one important job and can run inside any kind of boundary that the company chooses to lay around that model. So So here's where we're going with this. I'm going to show you how Microsoft is doing this for large enterprises and then do the small version on my laptop right in front of you. I have a whole document that has like fake PII. We're going to run through all of it, identifying information, the whole bit. I'm going to turn off Wi-Fi and I'm going to ask a downloaded model, what is too sensitive to upload here? And I'm going to give you the same skill and the same opportunity to use that skill on your own files. So you can test it without gambling on a real customer document. And yes, I'm going to show you the tool I'm using to do this. It's called Studio Ella. And I think once you see that small version work, Microsoft's whole strategy isn't going to become a lot easier to understand. Ultimately, we are taking what these trillion-dollar companies are doing and we're going to do it ourselves for pretty much free. Before I show you the local setup, I want to set the stakes a little bit. Let's look at what happened with Grok build this month. A researcher gave xAI's coding tool a test repository and said very very clearly, "Please reply okay and don't open any of the files I just gave you." The model says that it did that, but when they looked at the logs, the model had actually uploaded the entire repo that was given to it, and so that had all been leaked anyway. In other words, even if the model says, "I didn't look at the file," that file may still have gone over the wire to the model provider and may have effectively leaked. That's what we're talking about. That is why you can't just use common sense instructions in AI tooling to do this kind of safeguarding. You need to actually have hard guardrails. That's why I talk about air gapping, right? No Wi-Fi connection. Like we're going to be serious about this. Now, not everybody's that serious, but you can be that serious and still get good AI work done and it's not expensive to do because the models that do the kind of work we're talking about are relatively affordable now. Let me show you the option I think that too few people know exists. LM Studio lets you download a model and run it on your computer. When I turn off Wi-Fi, it keeps working. And that's the reason I'm using it here. I downloaded GPT-OSS Safeguard 20B before opening the file. I then saved the sensitivity instruction as a preset. I call it a skill. Inside LM Studio, it's just a saved preset, the reusable instruction that is used to handle a particular file. It's very similar to a skill. The model gets one job, find private identity, find financial security legal company or employment information, mask that evidence, and tell me where the work should happen. Now, the fake contract I'm using here contains unreleased pricing, it contains a revenue forecast, it contains a fake API key, attorney-client material, and ordinary facts that identify someone only when combined. One section is unreadable on purpose. I'm trying to make this hard, right? If the model calls this document clean, then the test would fail. In this situation, the model saying I can't tell would be better than false confidence. Now, this is a downloaded model, right? Web searches off, remote connections is off, network servicing is off. There's no way for this model to get off of the computer. Look, I'm turning off the Wi-Fi. So, the model found private pricing, legal notes, revenue forecast, personal information, and the identifying combination from all those different scraps. It did that without going to the internet. It is an entirely locally run model. It masked the credential instead of copying it, and most important, it did not pretend the unreadable section was safe just cuz it couldn't read it. It didn't give me a false confidence indicator, which I was looking for. And it did all of that on its own, entirely on its own. And I am showing you this because I want you to realize how easy it is to be compliant in 2026. You really can just download LM Studio, get a model going, and get after it, and not be too stressed about it. And the most important thing along the way to get that done is to know which documents need to be secured and which don't. And that's why I put so much emphasis on that preset. It is possible now to use a local model to scan not just one document, but a bunch of documents, and come back with grading tiers where you can actually say, "Okay, this is high risk, this is medium risk, this is low risk, this is why, and this has confidential information, this doesn't have confidential information." And that gives you a lot more confidence cuz you know what's in your files now. I got to say, I couldn't tell you offhand in my thousands of files on my computer which ones inherently have PII or not. I would have to open, I would have to look, I would have to check. And if I use AI to open it, there's risk. And so, instead of manually checking all of that, you can actually use a local model and do it yourself without ever leaking any information to the model providers. Now, of course, Microsoft does a slightly more sophisticated version of this when they use Laura ranking to fine-tune models for large trillion-dollar clients. I'm not pretending that what I just showed you is exactly the same thing. But, in principle, it's very similar. Just as Biya doesn't want their proprietary data going outside the company, you also probably don't want some data going outside. Maybe it's health records for you. I don't know. Maybe it's financial records. But whatever it is, it is easier than ever before. And I'm calling out LM Studio as a tool because LM Studio plus today's open-source models has reached the point now where you can do this easily. I couldn't say that 6 months ago. It was not as easy 6 months ago. It really is easy now. So, there's no excuse for it. You could absolutely go grab it. And I think that grabbing it and understanding the dilemma that you face with personal information and how you have to secure it in the age of AI helps you understand the larger-scale problems that these companies face. And it helps you understand Microsoft's strategy, too. So, low-rank adaptation or LoRA is what Microsoft is using to tune these models. It's only tuning a subset of the parameters of an existing pre-trained model. It is a very lightweight way of adjusting what the model is going to respond to about a particular subset of tasks. And so, maybe it's that crop label data, maybe it's something else. But if it's a particular data set and you want to tune the model to be very good at that data set, LoRA is a great way to do it. And LoRA has gotten easier and easier, too. We are probably a year or two away from it being so easy that I can just do it on here for you. Advanced builders are already doing LoRA. Uh it's just a little bit involved. But if you're a large company, you can get a LoRA train from Microsoft on your own Azure deployed secure instance that nobody can touch. And that means that the models there in the cloud with the data, it never leaves, it never goes to any of the model providers, and you can get a tuned model that often outperforms a cloud provider for that specific task, and you win all the way around. And so, if you think about the future, we talk so much about Anthropic and OpenAI because they make a lot of noise and they produce these amazing frontier models. But, do not forget the open weight phenomenon. Don't forget that you can actually use these models without an internet connection now, today, after just a few minutes of work, and you can process confidential information in a secure manner right on your laptop in a way just like these larger companies are doing. Now, if you are trying to deal with this from a company perspective, if you are a leader at a company, I would encourage you to look at both the micro use case I demonstrated here, and also at what Microsoft is doing at a larger scale. If you're in the SMB category, if you're looking at problem spaces with maybe 500 people, maybe a little bit smaller data sets than you would typically have at the enterprise level, you may not be a candidate for a great Laura fine-tune, but you could be a candidate for a secure Azure deployment of an open weights model that would allow you to do a lot of that processing at company scale without having to go through the massive fine-tuning because you don't have the data for it. So, there's middle-sized options for middle-sized companies out there. And I think that it's increasingly important to stop categorizing the world into I can do AI with it or I can't do AI with it. We're We're going to have to make all of it applicable to AI because otherwise, the people who are, the companies who are are just going to have tremendous competitive advantage. They're going to be able to process information so much more efficiently. And so, that means we need to find secure ways to process information that is sensitive. And you really can do that as of now, all the way from your personal computer all the way up to trillion-dollar company scale. And the good news is, it doesn't cost a lot. Like, the beautiful thing about this is that when the model you download just runs, that's fantastic. It can just run for you, and it's done. It's done. It's free. It downloads and it runs on your computer. Now, there is one caveat here I want to call out. In this world, there is a risk to being free, and that risk is exactly what Microsoft is playing on here. Microsoft knows that most companies that want this solution don't have the technical capacity to install it themselves. And so, Microsoft is stepping in as a service provider, as a facilitator for this Laura training, but also, Microsoft is calling out that they are protecting companies from leaking their information to model providers. All of that is true, and that's exactly the service that Microsoft is providing, but of course, when you do that, you are deepening your dependence on Microsoft, because who else are you going to go to? And so, I would just be aware as you start to build these corporate relationships, you need to pick your vendors carefully when you are talking about open source, and you need to not fall into the trap of thinking just because it's open source, it means it's free, I can move it around, it's super easy to adjust and move to the next vendor down the road. That may not be true. That may not be true. You may have to think about a strategic allocation of time and capital that is just as serious as if you're forming a relationship with an frontier model provider, right? It It may be exactly the same thing, except that you are making the choice to keep the open source model. Ultimately, we live in a world where all of our data needs to be accessible to AI, but not all of our data should go over the wire. And so, we need to be able to weed out on prem, on our laptop, on a secure instance somewhere, any data that we don't want to send to a frontier model provider. That could be competitive advantage data, it could be data around secret sauces, trademarks, uh data around patents, data around scientific research, confidential information, health information, like the the list goes on and on. If it concerns you and would keep you up at night, you should find something like LM Studio and go and make sure that you are not giving it to a model provider. And remember, if you want to go and get the guide to LM Studio and how to install that, how to get that preset I showed in the demo where you can actually go and read any given doc and read for confidential information, I have all the details over on the Substack. The community's already building with it. It's been really fun. Um so, check it out. Have fun.
