---
title: "The FBI is investigating DeepSeek and NVIDIA, plus the complete story of the rise of DeepSeek"
video_id: "XoM5w8OYlXs"
youtube_url: "https://www.youtube.com/watch?v=XoM5w8OYlXs"
substack_url: null
publish_date: "2025-01-31"
duration: "8:32"
duration_seconds: 512
view_count: 6559
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Nvidia"
  people:
    []
  products:
    - "Claude"
    - "Make"
  models:
    - "DeepSeek"
    - "SAM"
concepts:
  []
summary:
  []
keywords:
  - "ai-tools"
  - "anthropic"
  - "claude"
  - "coding"
  - "deep-dives"
  - "frameworks"
  - "leadership"
  - "make"
  - "nvidia"
  - "openai"
  - "product-management"
---

# The FBI is investigating DeepSeek and NVIDIA, plus the complete story of the rise of DeepSeek

okay I've taken my time on doing this video because I wanted to get it right this is a sort of larger look at what deep seek is where they got their chips what has been happening and it's sort of timely because apparently when Sam mman went to Washington DC for his big briefing yesterday all the questions were not about open AI they were about deep seek and so I thought doing a little bit of a deeper dive might be appropriate so with that in mind where did deep seek come from Deep seek was founded in May of 2023 they spun off from highflyer which is a hedge fund in China that had integrated AI into its trading strategies this will come back later uh recognizing you know AI has potential Beyond Finance at this point so highflyer invests highflyer invests in deep seek specifically getting 10,000 Nvidia a100 gpus for them in 2021 by the the the in other words like was founded 2023 they got the a100 gpus in 2021 because they believed in AI they handed or believed to have handed the 10,000 Nvidia A1 100s over to deep seek as part of the initial investment so that Hardware acquisition positioned deep seek for really aggressive AI development which is sort of what we see as they start to open source models this is if you got surprised by them you haven't been reading their papers and watching their model capability climb this brings me to training costs deep seep claims that their training run cost $ 5.58 million it used 2,000 gpus they did not share the model for reasons that should be pretty obvious uh and they said 55 days of training time the the cost they're reporting is much lower than what other models have reported but not wildly lower and that's a point that Dario amade made in his essay where he said we should kind of expect model in the 5 to10 million range if the incremental cost of for example Claude uh like a year ago was 10 plus million we expect models in the same class to get cheaper over time that's not a surprise so this is kind of expected none of that to take away from the brilliant engineering the team is doing it doesn't come for free to make the stuff cheaper you actually have to work at it um but this is in line with previous cost curve reductions that we've seen there are other reasons to be skeptical though of whether it was actually $5 million so the $5 million figure is really around the incremental cost for the actual training run so it doesn't cover the R&D labor cost I've seen a lot of people noting how many people are on those Open Source papers it doesn't cover electricity it doesn't cover cooling costs both of which are significant it doesn't cover pre-training data acquisition acquisition and curation if you think they just suck in the internet and do no curation that is just not how it works nowadays and then then it doesn't cover infrastructure and storage so how do you optimize your storage systems how do you manage all the data all of that the estimate that I saw from semi analysis which is a firm that analyzes semiconductors for Wall Street is that they think deep se's annual AI budget is somewhere around half a billion dollars which is a bit more than five million and maybe they're off but it just I think it's helpful to understand that when you name a price that's just a piece of the total price that's all it is it's like saying you know I bought my Toyota door for a hundred bucks I don't think I could get my Toyota door for 100 bucks let's just use that phrase I bought my Toyota door for 100 bucks and not mentioning the fact that you had to buy the whole car and Wall Street bought that so what about this Hardware the the best analysis I've seen and I've seen this multiple places is that they have got their hands deep seek has got their hands on about 50,000 Nvidia Hopper class gpus and that includes H 800s which is a China specific version of the h100 that has some lower performance and h20s um and the H20 is a restricted variant that's designed to be able to be sold to China and still be compliant plus that significant a100 stock pile from 2021 plus possibly Cloud compute agreements with Chinese providers which would allow them to kind of get around things at the end of the day these chips are slower than the full power h100 but deep seek ironically could scale up quantity to maintain performance for at least for a while and that explains why the feds specifically the FBI is looking at the Singapore back door that's under investigation now um and the Singapore backd door is the nickname for the fact that Nvidia has an inordinately large percentage of sales to Singapore and it is wondered if some of those sales to Singapore are getting renamed and re-exported back to China from Singapore and yeah the FBI is looking at that we may see tighter export controls I don't know we'll see so really what this comes down to is are the hardware constraints and training costs going to be helpful for for determining a competitive advantage and what deep seek tried to say essentially was no like we can train a model for $5 billion it's fine um and what I would argue and what other model makers are arguing is that the marginal differences matter a lot if you start out in this race just a little bit ahead it adds up a lot because these models are improving at an accelerating rate it's like you're starting a little bit ahead but everyone's running faster and faster over time and that kind of adds up like if you look at where deep seek is at from a model capability perspective they have just released a model on the class of the models that finished their training runs a year ago so like Claude so okay they're about a year behind and they're uh you know somewhat cheaper and by the way that is some if you Dario released the incremental costs for for Claude And it's like yeah you could say the Toyota door costs $150 to use my metaphor it's he was saying it's like $10 million in change um okay fine like maybe it was a little bit more than $10 million but the point is like you can slice it down and say it only cost a certain number of million when the reality is they need a lot of capital for all the other stuff I discussed for the R&D for the labor for the data and compute and infrastructure all of that okay so I suspect I am going to guess that we are looking at tighter chip export regulations I don't know that I'm not a profit but it just makes sense to me I think that if anything deep seek drawing this much attention to itself might end up being counterproductive for them from an access to chips perspective we will see I also would call out that this is a trailing Edge indicator releasing a model is the end of a long process and if you've been able to get around export restrictions successfully for a bit and then release a very widely known model well you got around export export restrictions successfully for 2021 22 23 you got some benefit out of it it is not clear if that is going to persist and if they start to clamp down on that that is going to change in a year in two years where deep seek will be at and I think that is the argument that the feds will be looking at we will see how the FBI investigation goes so that's the story of deep seek it's actually not that that uh old a firm but it's super aggressive and by the way if you just heard of them now they've been publishing papers they've been building model capabilities since they were founded in 2023 so this is not actually new they've been in the space and it's all good engineering stuff and I do want to call out that none of this is shadeed on the team uh they did great engineering work and I will continue to say that that was not fake um there's just a lot of other stuff going on and I wanted to share the full story cheers
