---
title: "AI News: o1 API, AI Scores 80% on a test doctors fail, AI catches scientific errors at scale"
video_id: "yOGMZq-_q60"
youtube_url: "https://www.youtube.com/watch?v=yOGMZq-_q60"
substack_url: null
publish_date: "2024-12-18"
duration: "4:39"
duration_seconds: 279
view_count: 1486
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Case Study"
primary_topic: "AI News"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Founders"
entities:
  companies:
    []
  people:
    []
  products:
    - "o1"
  models:
    - "o1"
concepts:
  []
summary:
  []
keywords:
  - "ai-news"
  - "ai-tools"
  - "coding"
  - "frameworks"
  - "leadership"
  - "o1"
  - "openai"
  - "prompting"
  - "startups"
---

# AI News: o1 API, AI Scores 80% on a test doctors fail, AI catches scientific errors at scale

three pieces of AI news today we're going to start with open AI 12 days of open AI they did a developer day yesterday 01 is now in API which means that you can call it you can give it a reasoning parameter which is really cool because essentially it gives you a little slider and you can move the slider up and down to uh suggest the effortfulness of reasoning how much it should think about a particular question you pose apparently you can bring in a vision element and pass that to 01 now uh which kind of makes sense because you can put photos into the chat bot with 01 already so it it has visual reasoning and they also did a bunch of other releases 40 mini uh out in API there's a ton of other stuff I'm going to link the full developer docs in the video here check them out there's more than I can get into on this on this video oh one more that's really fun they bumped the output token and the input token limit which means that you can get more into the query and more out of the prompt uh and that's very exciting okay number two black spatula project so we know that 01 has been useful anecdotally for catching mistakes in peer-reviewed papers but like many other realworld examples of AI application it's been hard to get a consistent eval it's hard to get a consistent evaluation or test that is changing the black spatula project is a project to review hundreds of peer-reviewed published papers with AI and see if AI can catch mist stakes in those papers in a way that's useful to the field we will see what happens it's not done yet but the fact that it exists is a significant step forward because at the end of the day most of the evals for AI are very very tightly controlled model maker defined evals which they kind of have to be to have Apples to Apples comparisons but it means we don't really understand which models do well at real world tasks in specific Fields even though we're using them like like medicine which brings me to my third piece of news medicine the New England Journal of Medicine has a famously difficult uh diagnosis test called the clinicopathological conference it's a sort of differential diagnosis uh uh case study that they do and what they decided to do for this academic paper was run 01 and a few other models against the questions posed in the clinical pathological conference tests and and assign Physicians to do the same well Physicians scored about 30% and had a really wide range of variant I actually looked at the err bars 01 scored 80% and had a very narrow sort of range of variance and I look at that and I I think two things the first is we are going to see startups bringing AI into the ex exam room and medical settings in 2025 this is too big a difference for AI not to be in the room especially with capabilities like Vision being rolled out it's going to happen and that's going to take a cultural change because we've already seen studies where doctors were given the option to try AI alongside their own judgment uh for an academic paper and the doctors just refused to sort of trust what AI was saying and trusted their own judgment so there's there's a cultural change that's going to need to happen but but even if the cultural change happens and even if we bring AI in the other piece that stands out to me is that there is a intangible factor in some of what is going on that is difficult to measure and we need to think more about but probably fixable with prompting I'll give you an example some of the treatment plans proposed by 01 were not incorrect but they were impractical it is very difficult to catch correct but impractical for example they for too many tests tests that would not necessarily incrementally add value but would just add that sort of fine grain piece of detail Physicians are usually quite sparing with the test that they run partly because it's invasive to the patient and partly because of expense and partly because they want to efficiently get the most value per test in sort of understanding the disease and they know how much granularity they need in their results to get a correct diagnosis so there's some human judgment there that 01 wasn't necessarily showing and it's interesting to think about how you would prompt for that okay that's your news mostly science and math but hey developers it's it's a fun day go over and check out the developer tools open AI released cheers
