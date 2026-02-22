---
title: "AI Case Study: Taking Hallucinations to Zero earns $650M Dollars"
video_id: "Rauz-3jycQ0"
youtube_url: "https://www.youtube.com/watch?v=Rauz-3jycQ0"
substack_url: null
publish_date: "2024-10-07"
duration: "7:13"
duration_seconds: 433
view_count: 1955
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Product Managers"
  - "Founders"
entities:
  companies:
    - "Anthropic"
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
  []
keywords:
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "deep-dives"
  - "frameworks"
  - "make"
  - "product-management"
  - "prompting"
  - "startups"
  - "tutorials"
  - "youtube"
---

# AI Case Study: Taking Hallucinations to Zero earns $650M Dollars

we can be tempted to believe that AI only matters going forward that the past state of AI is not relevant the past state of tech isn't relevant but that's not true I want to tell you the story of an acquisition in AI that happened over a year ago now it was back in the summer of 2023 and only now are some of the details starting to leak as people start to feel like they're able to talk about it it's relevant because it illustrates what's required to get a really Sky High valuation and a truly rolled out application at scale and we haven't talked about it much this is the this is the company case text is a Thompson Reuters company Now Thompson Reuters are the news people but apparently they acquire startups as well and they acquired case text back in August of 2023 for $650 million at that time the company was about 10 years old they'd gone through a few rounds obviously if you're a 10-year-old company in 2023 you were not starting out in the llm space this was before large language models they had to Pivot it turns out that they pivoted very successfully into a llm driven legal analysis use case they had about 10,000 clients at the time of acquisition and what they had done was they had figured out in the summer of 2023 how to avoid hallucinations for lawyers you can see how that would be highly valuable the lawyer absolutely needs to know that they are not going to get in trouble with the judge with the bar association for citing cases that don't exist they need to make sure that their legal arguments are sound they have zero tolerance for error but they also have a tremendous workload and would love help with uh getting through that workload more efficiently if they can guarantee the accuracy so that's what case text set out to do and what's interesting is not that they accomplished it and they got their m&a and everybody walked away with money or whatever what's interesting is how they did it because that is a pattern that's applicable to other startups and other applied AI use cases and that's why I want to call it out so over the weekend a very very long read from Eugene Yan broke that talks about this idea of eval driven development um we've seen this for a long time in software it was called test driven devel M for a while or TTD and in llms evil driven development is this idea that you relentlessly rigorously evaluate the performance of a particular prompt the performance of a particular series of steps performed by an llm and then you feed that back in until you can get the llm to behave exactly the way you want to and so in this case what they did at case text was they took the act of doing a deposition or the act of doing any other task in the legal profession that they wanted to cover and they said you know what we are going to break this down and we're going to evaluate it very very very thoroughly until we can get the llm to perform each component of the task exactly right before we get it to do the overall task that is a tremendously helpful insight I'm going to link the whole uh read here under the YouTube video but it's absolutely critical to understanding how to build llm applications at scale essentially what they're saying is if attention is all that matters which was the famous 2017 paper that described how uh some of the foundational Technologies of llms work how Transformers work how self attention Works um this is really saying that attention needs to be applied in detail at a micr step level to avoid hallucinations in fact they talk about more than 1,000 different evals for given task and that they did not pass a particular task at case text until every single eval pass which means if you had even one failure you would go back and break down that step and understand it better and that was that was the key they said that that uh fundamentally getting case text to a zero hallucination state required grinding through micr level detail with lawyers to understand exactly what they were doing so they could construct the llm extremely specifically and that was how they actually got it to zero level hallucination and that is what Justified the $650 million valuation from Thompson Reuters and so the generalizable pattern I take away is that if you are building an applied AI system it is possible that the hallucinations that you are experiencing are a function of you not understanding how to instruct the llm more more precisely how can you instruct it so precisely that it cannot mess up that it must clearly come back with exactly the correct response it's it's a worthy question right how much have you broken down your tasks if you are building AI systems how much have you structured them into extremely specific micro detail level steps I think one of the things that's going to distinguish strong AI applications is that they make that step breakdown something that's intuitive and easy for the end user because the end user is going to be too lazy you know I am going to be too lazy when I am running through and I have a meeting in 10 minutes and I need an agenda to go through and break down into micro level steps every single thing and one of the developments that I've noticed in 2024 is some of those common tasks are easier they're less prone to hallucination they're more precise thanks to backend work from companies like open AI or anthropic similarly if you are building a system where you are trying to make it easier for the end user you have to take on more of the specific fine tuning and prompting inside your system so that they can be fairly generic and they can invoke a very specific series of individual steps on the back end that lead to the kind of precise and accurate result they would want in a sense they want to treat the llm as if it already knows what they're talking about what their context is what they need and will then just generate a relevant result but that doesn't come by happen stance that doesn't come by accident that comes because you the system designer took the time to understand their intent break it down into specific granular components and instruct the llm how to handle that entire logical sequence and so I think what we got from the case study on case text pun intended is a great example of both the Venture value created by eval driven develop but also the importance of Designing based on evals to get exactly what you need out of an AI system hallucinations might just be an artifact thoughts
