---
title: "March 11: OpenAI Releases New Recommendations on AI Model Alignment via Chain of Thought"
video_id: "NPGtvH_YYXA"
youtube_url: "https://www.youtube.com/watch?v=NPGtvH_YYXA"
substack_url: null
publish_date: "2025-03-11"
duration: "4:45"
duration_seconds: 285
view_count: 2565
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Prompting"
difficulty: "Intermediate"
audience:
  - "General"
entities:
  companies:
    - "OpenAI"
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
  - "frameworks"
  - "make"
  - "openai"
  - "prompting"
  - "tutorials"
---

# March 11: OpenAI Releases New Recommendations on AI Model Alignment via Chain of Thought

we want our models to be ethical and aligned don't we we don't want them to be Skynet open AI has released a recommendation for how we train models to make sure they stay aligned even as they become more and more powerful to the point where we could use this technique even if a model is super intelligent or smarter than any living human what they recommending is that we never ever ever optimize for the inter internal Chain of Thought that a model has before it shows output tokens to the user so if a model infers it will produce reasoning tokens or inference tokens Chain of Thought tokens and what openai wants to do wants other model makers to adopt as a best practice is to not touch them and instead if you need to show those to the user you can sanitize them you can actually use a separate model or something to clean them up so that they don't break policy when you show them to the user but you keep the raw stream unedited and you don't ask the model to clean it up or make it within policy and the reason why is that if you optimize for that point in the value chain you teach the model to be deceptive the model will optimize for Chain of Thought as well as for output but you will no longer be able to detect misalignment so if the model is misaligned how will you know it could be Mis aligned fooling you producing both Chain of Thought and outputs that you can't tell are misaligned because the reasoning that the model uses is now entirely hidden and that's really dangerous it gets more dangerous the smarter the model gets and so what open AI is observing is that if we can avoid optimizing for Chain of Thought if we let the model so to speak think its own thoughts without any Jud judement then we are going to get to a point where the even superhuman models will be able to show us Chain of Thought and we can see what they are thinking and we can at least Monitor and understand so we have a tool that helps us to adjust output reliably if we don't do that if we insist that Chain of Thought be something that is also cleaned up we have no leverage to ensure that we have ground truth that we can push against output value values and make sure they're aligned we don't really know if the outputs are aligned because we don't really know what the model is actually thinking we don't have a raw output stream and so that's what's so worrying and so open AI is recommending that model makers avoid sanitizing or not avoid sanitizing but avoid um using reinforcement learning techniques to optimize The Chain of Thought that's a dangerous thing to do long term even if short term it produces uh more readable Chain of Thought that in the end produces easier to use outputs it's it's not worth it they say if this doesn't make sense think of it in terms of teaching your kids something you want your kids to tell you the truth even if they did something wrong same idea you want the model to tell the truth about what it's thinking even if what it's thinking isn't aligned and you don't want to punish it for telling the truth truth and that's basically what we're talking about in AI model alignment terms and as the model gets smarter and smarter as the kid gets older and older the value of discovering what they're really thinking just grows and that's really what we're talking about here does that make sense basically Chain of Thought tokens are the only way we may be able to know what a model is actually thinking once it gets past the point of human intelligence which the fact that we're talking about that the fact that a major model maker is saying that's coming and we just have to get ready for it and we should probably figure out how to get alignment mechanisms set up for that that's a huge deal that's a really big deal they're talking about it like it's just next Tuesday but like it's a big deal so I hope that made sense I know it's a bit of a esoteric topic it's a weird topic but alignment matters avoiding Skynet matters uh and so I thought it would be good to tell everyone like what the best practice recommendation is so we don't have Skynet cheers
