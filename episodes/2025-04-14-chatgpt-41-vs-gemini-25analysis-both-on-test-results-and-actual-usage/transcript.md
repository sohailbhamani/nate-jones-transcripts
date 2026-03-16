---
title: "ChatGPT 4.1 vs Gemini 2.5—analysis both on test results and actual usage"
video_id: "Jl7wX80nxlo"
youtube_url: "https://www.youtube.com/watch?v=Jl7wX80nxlo"
substack_url: null
publish_date: "2025-04-14"
duration: "4:14"
duration_seconds: 254
view_count: 11371
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  OpenAI model report: https://openai.com/index/gpt-4-1/

  My site: https://natebjones.com/
  My links: https://linktr.ee/natebjones
  My substack: https://natesnewsletter.substack.com/

  Takeaways
   1. 4.1 Isn’t State-of-the-Art: Despite the name and rollout, GPT-4.1 doesn’t beat the current leaders. Gemini 2.5 scores 64% on SWE-Bench, while GPT-4.1 sits at 55%. It’s OpenAI’s best public coding model to date—but still behind.
   2. 4.5 Quietly Deprecated: OpenAI announced they’re sunsetting GPT-4.5, stating 4.1 is better. But 4.5 was only recently introduced as a research preview, and now it’s gone—an unusual and somewhat confusing move.
   3. ChatGPT vs. API Gap: OpenAI continues to ship stronger models inside ChatGPT (like “Deep Research”) that are not available in the API. This creates a frustrating mismatch for developers trying to build with parity.
   4. OpenAI’s Ecosystem Strategy Is Narrowing: By keeping their best models in the app, OpenAI’s ecosystem strategy leans more toward consumer lock-in than enabling external infrastructure and innovation.
   5. Gemini 2.5 Feels More Polished: In side-by-side usage, Gemini 2.5 isn’t just better on benchmarks—it feels better in practice. It’s more confident, cleaner, and gives better experience in tools like IDEs.
   6. 4.1 Is a Patch, Not a Leap: It’s a necessary release—4.0 wasn’t holding up, especially for devs. But this isn’t a game-changer. It fixes obvious flaws. It doesn’t push things forward meaningfully.
   7. The Bigger Picture Is Competitive Pressure: For once, OpenAI isn’t leading. Gemini is ahead on core dev metrics, and Claude 3.5 is in the wings. The pressure is real, and 4.1 doesn’t change that.

  Quotes:
  “We are used to thinking of OpenAI as always releasing a state-of-the-art model. It’s not.”
  “It feels really weird to me to release 4.5 as a research preview and then yank it back.”
  “4.1 was probably a necessary release, but it’s not a sufficient release.”

  Summary:
  GPT-4.1 dropped, and while it brings some improvements, it’s not a state-of-the-art model. It performs better than GPT-4.0, but still trails behind Gemini 2.5, which leads on SWE-Bench and feels better in real-world usage. OpenAI has deprecated GPT-4.5, citing 4.1’s improvements, but continues to withhold some of its best models—like Deep Research—from API access. This raises questions about the company’s broader strategy and its commitment to supporting the developer ecosystem. 4.1 is a patch, not a breakthrough, and the competitive gap is starting to show.

  Keywords:
  OpenAI, GPT-4.1, GPT-4.5, Gemini 2.5, SWE-Bench, Deep Research, ChatGPT, API access, developer tools, artificial intelligence, AI ecosystem, Google, Claude 3, model deprecation, coding benchmarks, IDE integration, agent infrastructure, developer frustration, AI release strategy, language models, competition in AI

yt_tags:
  []



# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "AI Tools"
difficulty: "Intermediate"
audience:
  - "Engineers"
entities:
  companies:
    - "OpenAI"
    - "Google"
  people:
    []
  products:
    - "ChatGPT"
    - "Claude"
    - "Gemini"
  models:
    - "Claude 3"
    - "Gemini"
    - "Gemini 2"
concepts:
  []
summary:
  - "5—analysis both on test results and actual usage

Okay, it's time to talk about Chad GPT4"
keywords:
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "chatgpt"
  - "claude"
  - "coding"
  - "deep-dives"
  - "frameworks"
  - "gemini"
  - "google"
  - "openai"
  - "product-management"
---

# ChatGPT 4.1 vs Gemini 2.5—analysis both on test results and actual usage

Okay, it's time to talk about Chad GPT4.1. It dropped today. I'm actually not going to spend most of my time talking about all the features they announced with it because to be honest with you, we've heard all those features before. What they did was they took most of the features they had quietly stuffed into Chat GPT40 like better following of sequential tasks, like uh better handling of numbers, like somewhat better coding abilities. and they said "Hey, maybe the coding abilities should go with the API because I don't know maybe developers would want it. That sounds like a reasonable plan." And so they put it in 4.1. And then in their infinite wisdom, they decided to deprecate 4.5 because, and I kid you not, actually from the live stream, they said 4.1 is better than 4.5. Why? The naming continues to get more insane every single time. I was just getting to know 4.5 as a model. It feels really weird to me to release it as a reach search preview and then yank it back, but here we are. Maybe this is OpenAI's admission that it was a flop. I kind of liked it. So anyway, regardless, 4.1 is not a state-of-the-art model. And I want to emphasize that we are used to, and I think OpenAI likes this, we are used to thinking of OpenAI as always releasing a state-of-the-art model. It's not. Gemini 2.5, for example, scores like 64% on SWE. GPT4.1, even though it's doing much better than 40, is scoring only 55%. And if you're wondering what SWE, it's just an independent measure of engineering capability. It measures your ability to do engineering tasks. And Gemini 2.5 Pro is better at it. So, this is the question I have. Why is OpenAI choosing to release worse models in the API than they release in their chat app? They have models in their chat app that they are choosing to not release in the API. Deep research, for instance, is a model you cannot call in the API. It's a good model, not in the API. And I think that's really interesting. And I think it makes it more difficult to build out infrastructure that we can use to advance artificial intelligence capabilities across the ecosystem and it pushes people more into a particular app. Now that may be good from a consumer perspective, but it's not good from an ecosystem perspective. From a consumer perspective, if you're always getting the best apps in your app, in your chat GPT app, and you don't have to think about it, you're fine. But if you want an overall healthy AI ecosystem you need state-of-the-art models getting released that enable you to build in ways that drive the ecosystem forward. And I got to give credit. Google has done a better job here. Gemini 2.5 is a fine model and they've released it in the API. I've been playing with it for a couple weeks now and I'm really enjoying it. It feels like a thoughtful model. It can be opinionated. It's clear. Uh sometimes I like it to bounce ideas back and forth with Claude 3.7 in my IDE. It's working pretty well. I have played with 4.1. I played with 4.1 this afternoon when it came out. Also in my IDE, I found it a little bit wordy, not as confident. It's fine. I got progress but it didn't feel as smooth sailing as I felt when I was running with 2.5. 2.5 the the vibe felt as good as the test results showed. felt better just just like 2.5 scored better, right? So, for what it's worth, um I think that 4.1 was probably a necessary release because the only other API that they had in that class was four, which clearly wasn't up to it, but it's not a sufficient release. You know how necessary, but not sufficient. It's a step forward, but it's not enough. Chat GPT has some catching up to do on the tech ecosystem side and I know they have a big week ahead, but it really remains to be seen if they're going to release something that moves the needle versus uh Claude and really versus Google.
