---
title: "Here's How to Solve the 6 Top Prompt Issues (Based on 29,000 OpenAI Comments)"
video_id: "KwQpPbLEBMA"
youtube_url: "https://www.youtube.com/watch?v=KwQpPbLEBMA"
substack_url: "https://natesnewsletter.substack.com/p/the-prompt-doctor-is-in-fixes-for?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true"
publish_date: "2025-11-06"
duration: "11:23"
duration_seconds: 683
view_count: 7899
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI strategy"
  - "prompt engineering"
  - "large language models"
  - "ChatGPT office hours"
  - "schema first prompting"
  - "regeneration loop"
  - "planning illusion"
  - "hallucination in AI"
  - "context overload"
  - "AI consistency"
  - "LLM reasoning"
  - "automation at work"
  - "AI for teams"
  - "AI prompting techniques"
  - "GPT-5 tips"
  - "AI workflow design"
  - "AI adoption"
  - "AI problems and fixes"
  - "AI strategy for operators"



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Prompting"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "OpenAI"
    - "Google"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# Here's How to Solve the 6 Top Prompt Issues (Based on 29,000 OpenAI Comments)

I spent the last few months running informal office hours with Fortune 500 product teams, with technical writers, with "
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "coding"
  - "deep-dives"
  - "frameworks"
  - "google"
  - "leadership"
  - "make"
  - "openai"
  - "product-management"
  - "prompting"
  - "tutorials"
  - "workflows"
---

# Here's How to Solve the 6 Top Prompt Issues (Based on 29,000 OpenAI Comments)

I spent the last few months running informal office hours with Fortune 500 product teams, with technical writers, with consultants. I keep coming up against the same six problems when people use AI. So, I'm calling this video chat GPT office hours. We're going to go through each of the six problems that I come across over and over again, and I'm going to call out how I advise teams to fix it. Number one, the projection trap. What's that? you are projecting capabilities onto the model that the model does not have. I see this with developers and with non-developers both. If you're a developer, this can look like assuming a competency in an agent tool call that isn't really there. If you are not a developer, it can look like writing a prompt and the prompt is underspecified. The prompt lets you infer and guess. And so for example, if you say in a casual prompt, write me a professional update about the migration. The model might assume you mean an engineering audience and that you want a deep technical status update. But you may have meant, I want an executive audience in 150 words. That's a very simple example. And people assume that they can fix this by just writing very long prompts. That's not correct. The correct way to fix this is actually to specify the schema of the output. And so what you want to do is instead of saying I need to compose a prompt and writing prompt forward in your head, flip it around and say I want an output that looks like this. And that becomes your map that you give to the AI. And this is called schema first prompting. It is a way to handle situations where you are routinely getting incorrect responses. It's not that you have to do this every single time. All of these prompts and prompt tips and office hours approaches are things that you do when things break. That is why we're having this conversation. So when you are getting responses that do not work, ask yourself if you are projecting capabilities onto the model that it does not have. And if you are, think about whether or not you need to specify your output more precisely in the prompt. All of these are going to have examples in the Substack write up. I will have actual printed out prompts that you can look at. I want to get through all six of them with you here. So that's the principle. Number two, the revision loop or the regeneration loop. You ask for a tiny fix, the model rewrites the whole thing or touches a bunch of things you didn't want it to touch. This happens a ton. Models have a lot of difficulty touching just one thing. One of the big updates that Codeex made in the last couple of weeks or months that helps with this for coders, for developers, is that they have better inference around surgical code changes. But we're not all developers. This is not all about code. And to me, from an office hours perspective, this is a much larger issue that affects everyone who uses AI. We get into problems really, really quickly when we do not specify what we want changed in a regeneration loop. And so when you think about regenerating a model output, when we call it iterating, let's say you're in the same conversational thread or let's say you're going back in an agentic workflow and you're reworking based on an incorrect response, you need to be absolutely surgical about what you want changed. Ideally, you want to quote the exact snippet you want changed. You want to say, "This is what's wrong," and request only that patched section back. As an advanced fix, if you are keeping a schema, which I talked about in office hours principle number one, you can actually say, I only want this field name in your schema to be touched. Freeze all the other fields and that can help as well. Now you get the ability to actually control and drive schema level outputs in the API if you're a builder. But I find in practice the models are so trained for developers that even if you're not a developer if you give it a non-technical schema like this is the title, this is the author, it tends to respect those because it's trained to respect labeling and schemas. And so if you want to do a more advanced fix, you can label your outputs with a schema and then say this section of the schema is incorrect. You need to fix it. That's number two. Number three. Number three is the planning illusion. So complex tasks will often collapse themselves into one shot where the model will skip crucial steps in analysis or in planning. Like if you say, "Please analyze the churn and propose a plan." And the model just does a single blob pass on it. It has very shallow causes. It's a weak plan. This is something we don't discuss and we often attribute it to model quality where we say the model is bad because I got a bad response on this multi-step reasoning challenge. I want to suggest to you here in office hours that the problem is probably not the model at this point. It is probably the way you are handling the planning step. A better approach, a baseline approach to fix this is to break the challenge into stages with explicit outputs and validation gates at each stage like do stage one only where you review all of the incoming data in this way along these axes and then report back with this output stop and then force a step-by-step progression. That's a very simple thing. You can enforce that with tool calls agentically in the API. You can also do it in the chat. You notice how I'm deliberately saying we face the same problems as developers and non-developers. That is one of my core beliefs about AI. We are not that different. We're all using the same models. The advanced fix here is you want to start to specify tools and contracts for tools. That gets very technical in the API. You can do it in the chat in plain English. You can say I want you to use the internet search tool for this or I want to constrain your internet search to only academic sites. You can do other things as well, but that's that's a simple way of describing what a tool call in a contract would be. You're basically saying in this case to do this reasoning step, you will need these inputs and these tools. Please use Python or please analyze this with your uh PowerPoint creation scale and create the PowerPoint whatever it is. The point is by defining the tools and what you want to call you are going to leave the model less room to walk off and do a single blob weak pass reasoning effort and instead you're going to specify enough of the effort along the way and the sequence along the way that you'll get a strong reasoning takeover. This is different from saying think hard. This is different from saying the models don't reason. The models do reason, but if you care about how they do so and the reasoning quality, you need to invest in this so you don't get stuck in the planning illusion. And that's number three. Number four is the confidence illusion. We also call that hallucination. You get fluent answers, mismatched, non-existent citations. Look, the simplest baseline fix is to permit the model to say, "I don't know." and to require confidence labels where the model needs to name its level of confidence. You can also ask for a claims to verify list. If you want to go farther, you can have a verification fields array in a schema where you force the schema in the API to give a statement, a confidence level, a source, and a verification status. You can do this with plain English prompting. I find that it tends to look a lot like chain of verification prompting in practice where you are naming the conditions under which the prompt can move forward and only then are you going to allow the model to print a response. When you're tackling hallucinations in particular, you do want to get specific with the conditions for confidence level. So if you're saying only print an answer when your confidence is high, are you clear with the model about what high confidence looks like? and are you extremely unambiguous about that? This is an area where even a little bit of ambiguity in your prompt can push the model to resolve on its own and that can lead to hallucinations. Office hours problem number five is the drift problem or consistency issues where you have same inputs and different outputs. Uh you can have generated tags or categories that drift across runs. You can have selection criteria applied inconsistently. So the baseline fix is to turn the model temperature down if you're in the API and to set absolute constraints. If you are in the chat, the best thing you can do is to be extremely obsessive about token level clarity and consistency with your inputs and to also be extremely specific with the rules by which the model processes what you want it to do. If you want to take an Excel sheet and process it to a Google doc, the prompt that you're using, maybe it's not in the API, maybe it's in an N8 workflow, maybe you're actually pasting it into Chad JPT, but the prompt needs to be extremely specific about the sequence of steps the model needs to go through. Otherwise, you get into a position where you are inviting the model to make up steps along the way, and that invites drift. It invites a lack of consistency. Your job with this consistency issue is to take away all ambiguity and opportunity for creativity from the model and to make it as buttoned up and linear as you possibly can. The sixth one that I get a lot is the cognitive bandwidth trap. Too much context. More context can make outputs worse, but people don't realize that when they're early on in chat GPT, and they think that they can just throw everything into a million token context window and get responses. The fix is to have really clean context loading. If you are in the API, you can specify required versus optional context loading. If you are not in the API, it is your brain people. You need to think about the slice of context you are uploading and you need to assume that you would do better to paste the two pages of the 20page brief that you need edited or reviewed versus the full 20page brief. Unless there's a real good reason to give the model all of that context. Default to as little context as is humanly possible to get the model to do the task. This is really confusing because people keep looking at these exploding context windows and saying, "Oh my god, this is amazing." Well, it is amazing, but if you want clean, consistent outputs, overloading the model with context is going to be a problem. And so my challenge to you is to start to think about context as something that you clean for, not something that you accumulate. Because the more you think of it as a pile you accumulate, the more you invite the model to use dirty context. So there you go. I know I hit hard. These are the six most common problems that I see in real life. I also comb through the OpenAI forum. So I wanted to check and see, am I just getting a sampling size issue? I'm not. I am seeing these over and over in the open AI forums as well. They seem to be something that developers face and non-developers face and I wanted to pretend we were in office hours together and just give you an honest talk about what I see and how you actually fix it. If you want to dive deeper, there's a ton more in the write up on Substack. There'll be prompts and just really easy specific examples so you can see what I mean in terms of how to fix this stuff. Good luck. These models are much more capable than we think. Um, and you're not alone when you're facing problems. That's the other thing I want you to take away.
