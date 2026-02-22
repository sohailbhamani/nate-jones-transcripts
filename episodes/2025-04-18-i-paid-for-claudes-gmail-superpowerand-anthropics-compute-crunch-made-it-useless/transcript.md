---
title: "I Paid for Claude's Gmail 'Superpower'—and Anthropic's Compute Crunch Made it Useless"
video_id: "TMnJDCNx06A"
youtube_url: "https://www.youtube.com/watch?v=TMnJDCNx06A"
substack_url: null
publish_date: "2025-04-18"
duration: "8:34"
duration_seconds: 514
view_count: 7096
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Tools"
difficulty: "Intermediate"
audience:
  - "Engineers"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
  people:
    []
  products:
    - "Claude"
  models:
    - "DeepSeek"
concepts:
  - "Anthropic is compute constrained"
  - "They're just giving claude more tools"
summary:
  - "# I Paid for Claude's Gmail 'Superpower'—and Anthropic's Compute Crunch Made it Useless

I tried the new Claude feature that connects your calendar and your email into Claude"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "coding"
  - "frameworks"
  - "openai"
  - "product-management"
---

# I Paid for Claude's Gmail 'Superpower'—and Anthropic's Compute Crunch Made it Useless

I tried the new Claude feature that connects your calendar and your email into Claude. I was so hopeful. I was like, I'm going to get insights from my email I've never gotten before. I'm going to finally hook an LLM into my email account instead of using a third party. I'm going to be able to get all the power of a Frontier class model in my inbox on my calendar preparing a daily briefing for me. I had all these ideas. No, none of it did not work. And I dug into why and it's a super interesting reason and it gets at one of the core issues facing Anthropic right now. Fundamentally, Anthropic is compute constrained. That is shaping everything they do and it's shaping this feature roll out and making it much more disappointing than it needs to be. I'm sure Claude is a good model. My experience with Claude has been great overall. My experience with Claude on this was terrible. Even though Claude generally codes well, when I asked Claude to code me a briefing React artifact based on inputs from email and from calendar, it just did a lousy job. It made one call. It dropped one list. It got half of my meetings, not all my meetings. I grant you I have a lot of meetings, but still it pulled like the first seven or eight. And it pulled some of my emails, like the first five. And when I dug into why, it turns out Enthropic is probably rate liimiting the call on the back end to save costs. Which is why even on the max plan, if I were paying a hundred bucks a month for Anthropic, I would still only be getting 50 50 calls to calendar or docs or email total. that eats up real fast if you use it to like look at three docs a day, if you use it to look at your calendar twice a day, if you use it to check your email and like work on email responses. It's gone like that. Now, they say they're going to, lift, it, eventually,, but, the fact that even paying a hundred bucks a month doesn't move that for me tells me how compute constrained they are right now. And I am concerned that we are at a point where there is pressure on model makers to show agentic tool use because you notice like they dropped this the same week that OpenAI drops 03 which has I believe access to something like 600 tools that it can work with under the surface like not where you can see it. You don't get to pick it from a drop down. Uh but it chooses the tools and interacts with them. Well, fundamentally they're just giving Claude more tools. It's a gentic tool use wrapped inside a chatbot poorly described. The problem is anthropic is much more compute constrained than chat GPT. And at the end of the day, that is showing up in the way these rollouts actually go. And so I did I jumped in, I grabbed the calendar grabbed the email, and I had a terrible experience. And when I went back and tried to get it to rebuild, I said "Claude, try again." Like, typically this gets fixed when Claude fixes it again because 3.7 and honestly 3.5 are pretty good about fixing issues. Claude could not go back and get even the basic complete calendar drop on the second and third try. Could not go back and get like the last 15 emails. And when it did, could not generate meaningful LLM insights off of all of that data that it had just ingested. It may well be pulling those data sources as separate uh context ingests, so it can't look at them as a merged file and view them together. I don't know. But at the end of the day, it's just not a great customer experience. I also think it's increasingly problematic that Claude has in theory a gigantic context window to ingest, but a very very poor orderof of magnitude context window output. In practice, limiting your context window output to something like 8K tokens on a turn like it just feels so short and it feels like Claude is deliberately cutting corners even if you can pull the entire dock in. And I think Chad GPT has done a much better job masking that with the way they've handled it. So their theoretical token input limit doesn't feel that way because they can stick stuff on disk and like stream the tokens in as they need them, which is something that's sort of special to how they've architected their LLM. And it basically from a consumer perspective means that you don't notice the token limits. And so we spend time talking about token limits as if they are the beall end all of these experiences. But the reality is compute limits are more interesting. Open AAI is playing with their compute because they have a lot of it. They're doing things like um streaming tokens in storing stuff on server making sure that if they roll something out they have the compute allocated so it's actually a good experience for people offering unlimited queries things like that. And Claude is compute constrained fundamentally and is basically only going to produce the output tokens that it can produce on any given turn. So it looks really it feels chunky and is not going to be able to actually use the tools because the compute is constrained on the tool use like you don't do 600 tools if you are open AI unless you are confident you have the compute to sustain it. And that's what they have with 03. And so in a sense, I do think what we are seeing in the roll out for Claude with calendar and with email. It's not fundamentally about the knowhow of the team or the quality of the model. It's not even about the token limits, which are what you read on the 10 and I think are increasingly deceptive. It's really about the capital constraints in the space. Claude is less well capitalized than OpenAI. Claude is getting less GPUs netn net and Claude is falling behind because of that hard fact and that doesn't reflect at all on how much I admire the team or what they're trying to do with claude. Claude is a model I love especially cloud 3.5. It has hit a sweet spot. But at the end of the day, the compute constraint means that the customer experience which is a layer removed from just output. Like we don't just have a customer experience that is input tokens, output tokens. We have a whole layered customer experience where we are looking at interface. We are looking at how the conversation feels and flows. It's those little things like uh like I was saying choosing to store a disc or chat GPT choosing to show a little fragment of train of thought and not the whole chain of thought. Um choosing to prioritize a particular experience on a particular plan so it feels complete. Uh which is why I think chat GPT has constrained 03 to only 50 queries per week on the plus plan as of this date. um and much more on the I think it's unlimited on the pro plan. They they're doing that because they want to provide complete experiences to the people using the chat as opposed to gating it and letting everybody have it but giving everyone kind of a bad experience and I think that's a better choice. Um, and I'm not saying that Claude is not trying to gate a bit, but I noticed the gating is not very effective because effectively they don't unlock the gate at the pro plan. Like we talked at the beginning of this, a h 100red bucks a month and they are still not ungating those 50 calls out to docs, to calendar to email. That is compute constraint. That is capital constraint. And I think we need to talk more about how capital constraints are starting to shake out the dynamics of this race. I know we like to talk about open source. Deepseek has done amazing things. That's another video for another day. But capital constraints are real. GPU constraints are real. Compute continues to be a driver of success in this space. That is not going away anytime soon. And I think that part of what we see with the roll out of 03 this week, especially when you compare it to what Claude needed to do strategically to roll out an agentic tool this week, you see the capital constraints on display. Tell me your thoughts.
