---
title: "7 Prompting Strategies from Claude 4's \"System Prompt\" Leak"
video_id: "74FvsJeljak"
youtube_url: "https://www.youtube.com/watch?v=74FvsJeljak"
substack_url: null
publish_date: "2025-05-29"
duration: "10:58"
duration_seconds: 658
view_count: 23016
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Prompting"
difficulty: "Intermediate"
audience:
  - "Engineers"
entities:
  companies:
    - "X"
  people:
    []
  products:
    - "Claude"
    - "Make"
    - "MCP"
    - "Operator"
  models:
    - "Claude 4"
concepts:
  []
summary:
  - "# 7 Prompting Strategies from Claude 4's 'System Prompt' Leak

I have never done this before"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "claude"
  - "frameworks"
  - "make"
  - "mcp"
  - "microsoft"
  - "operator"
  - "prompting"
  - "tutorials"
  - "x"
---

# 7 Prompting Strategies from Claude 4's "System Prompt" Leak

I have never done this before. I'm actually going to break down what I learned by studying the leaked alleged system prompt of Claude 4. Now, the reason I haven't covered this in the past is because I feel very ambiguous about the idea of leaking system prompts. It's a grey hat tactic at best. It happens all the time. I would say on average you have a system prompt leak within 48 hours of any major model release and it's part of what enables models to proliferate so rapidly. But regardless of how I feel about it, the reason I'm covering it today is because I think there is so much to learn from this system prompt and whether or not it's real. Because of course the model makers never ever validate whether they're real and I don't care if it is or not. I care about the prompt structure and I'll link to it in the in the description for this video. The the key to this prompt is changing from the idea that a prompt is about instructing a model to do something to the idea that a prompt is about building policies that prevent failure modes. And you might think, well, that's okay for a system prompt for a model. Maybe if you're using an API that makes sense. Why would I care as an operator that chats? I actually think you care a lot because at the end of the day, you also care about quality outputs. And most people put 80% of their effort into what the model should do for them and at best 20% of their effort into what they don't want the model to do. This prompt for Claude 4 is basically the opposite. It's like 90% what Claude should not do and 10% what it should do. And I want to go through seven different tactics that I found inside the prompt. And again, I will link to this. You can see the whole prompt if you want. It's like 300 some lines, 10,000 words. So number one, this prompt instantiates identity and the things that do not change upfront. So it starts with concrete facts. This is this model's identity. This is the current date. This is the core capabilities. The idea is that establishing context early that's steady and stable reduces working memory burden. It's not so much a hack, it's just it's good instructional design. Number two, triggers and template refusals. This is an explicit ifx then y conditional blocks that handles edge cases. And I think the care that this prompt puts into edge cases is a master class on its own. Ambiguity leads to inconsistencies from these models. If you want to have consistent behavior, you need to be clear and spell out your edge cases. And so this isn't so much about being restrictive, it's about being clear. It's about saying this use case has these boundaries and these explicit conditionals. And I think that is an incredibly powerful principle for prompting. Number three, uh, and I'm going to be very precise about this. I call it three tier uncertainty routing. So basically, this gives the model very specific instructions for how it handles ambiguity. And I've almost never seen this in another prompt. So the first answer, the first step in the decision tree is this is timeless information. Please answer it directly. Don't go, don't pass go, don't pay $100 in the monopoly parlance. Just answer it right away. Number two, assess it as slow changing information. Answer directly plus offer to verify. And number three, assess it as live information. Maybe you're asking about today's stock prices. search immediately. The lesson here is that good prompts include decision criteria, not just commands. You need to help the model determine when, not just how. And this is especially true for agentic communication. Like if you are giving an agent a guiding policy, this kind of routing on uncertainty is critical. Number four, what I call lock tool grammar. So it provides both correct and incorrect examples when it instructs the model to use APIs in the cloud for system prompt. So we have valid function call formats and we have explicitly invalid function call formats. And I've called out before that you want to have counter examples, but this really underlines it. If you are using tools or functions, if you're using API calls, if you're using MCP servers, whatever it is, show both right and wrong. It's like teaching someone to ride a bike and also showing common ways people fall, like slowing down too much. Teaching my kids to ride bikes. I I get how this works. The point is that negative examples are powerful. They're powerful teaching tools for people. And it turns out they're powerful teaching tools for models as well, especially when you're trying to teach a model how to use a tool well. And we have almost no examples of how you prompt well that we have talked about publicly that do this. And so I think it's really important and this is an example of why I decided to talk about this prompt. There's a lot of gems in here we we should be grabbing. Number five of seven, binary style rules. Instead of subjective guidelines, the clawed four prompt is extremely prescriptive about things that it cares about. Hard onoff rules. Never start with flattery. Okay. Uh that is much more onoff hardcoded than the phrase be concise. You know, concise is interpretable by the model. Never start with flattery is a lot more binary. Models handle absolute rules. It it no bullets unless requested is much clearer. No emojis unless requested is much clearer to the model than minimize formatting. So you want to be in a place where your prompts are that clear. The takeaway here is that your prompts are not supposed to have wishy-washy adjectives. They're supposed to have extreme clarity on what you care about most. Number six, positional reinforcement. This is a really interesting technique we need to talk about. Throughout this lengthy prompt, critical instructions are repeated at strategic positions, not just at the beginning. Again, I rarely see this. So, the prompt repeats these constraints multiple times. It works because attention degrades over long contexts. If you reinforce every say 500 tokens, what are the critical rules? It's kind of like giving your your model a speed limit sign as it reads this lengthy prompt. This is what a 10,000word prompt. It's reading every 500 tokens. Oh yeah, I got to remember this. Um, and so what this looks like is you have your main instructions, you have the intervening content that continues to have prompt instructions, then you have, hey, sign, you know, signpost. Uh, remember never use customer PII in your examples. More content comes through. Critical reminder, all PII must be anonymized. Like you're repeating it and that acts to positionally reinforce this in the LLM's memory. I again, this is something that humans do as well. This is just good instructional design. It repeats and aids retention for humans and for models, but I rarely see us do it in prompts. Okay, last one. Number seven posttool reflection. There's a built-in thinking pause after tool use. Again, this is an agent-based one. If you're using MCP servers or APIs, this is going to be relevant for you. The prompt has instructions to strongly consider outputting a thinking block after function results. Tool outputs are not always easy to parse and so a reflection step can improve accuracy. It can help you with figuring out what to do next. Especially for Claude 4, which is renowned for these long multi-step interled reasoning plus tool use chains. It literally looks like this. When you're using Claude 4, you want to take a minute to read what you're getting before you decide on your next move. And I think the takeaway there is that's probably a good principle for our prompting in general. Build in that cognitive checkpoint. Don't just make it spit the tool output. Ask it to process and think about it. Look, this can get turned into a prompt you can use as an operator too. You're not stuck with this and like admiring the clawed prompt from afar. Like you can actually use it yourself. I think the thing that I take away here is that we need more understanding of prompts as operating systems. Prompts are not just incantations. They're not spells. They're not magic words that makes the LLM do a thing. They're like an OS config file. It's it's about being extremely precise about what you intend. And it's okay to be defensive in that. It's okay to address hallucination, copyright issues, harmful content exhaustively rather than just kind of waving a hand at it and moving on. And if you do that, if you are more passionate and more caring about defensive programming than most of your peers, when you write these prompts, you are going to get better results and that will add up to real value. I would also say the third takeaway I have besides operating system defensive programming is you want to be declarative. Instead of first X do Y, see if you can frame it as a policy. If X always Y, how much of your prompting would change if you did that? So there you go. Long long dig into prompts. I have something on the Substack on this as well. Um, I think this was a fantastic use case. Again, I have some mixed feelings about how this alleged prompt came into being, but it's so useful. It is worth learning from regardless. And I hope you've been able to see that over the course of this conversation.
