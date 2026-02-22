---
title: "ChatGPT-5 Rumors Decoded—How Prompting is Evolving in the Next Age of AI"
video_id: "POLFZdG54Kw"
youtube_url: "https://www.youtube.com/watch?v=POLFZdG54Kw"
substack_url: null
publish_date: "2025-06-26"
duration: "12:11"
duration_seconds: 731
view_count: 26484
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Tools"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Meta"
  people:
    []
  products:
    - "ChatGPT"
    - "Claude"
    - "Claude Code"
    - "Gemini"
    - "Make"
    - "MCP"
    - "Operator"
    - "Canvas"
  models:
    - "Claude 4"
    - "Gemini"
    - "Gemini 2"
concepts:
  []
summary:
  - "# ChatGPT-5 Rumors Decoded—How Prompting is Evolving in the Next Age of AI

It is possible to prepare for chat GPT5 now"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "canvas"
  - "chatgpt"
  - "claude"
  - "claude-code"
  - "coding"
  - "frameworks"
  - "gemini"
  - "google"
  - "make"
  - "mcp"
  - "meta"
  - "openai"
  - "operator"
  - "product-management"
  - "prompting"
  - "tutorials"
  - "workflows"
---

# ChatGPT-5 Rumors Decoded—How Prompting is Evolving in the Next Age of AI

It is possible to prepare for chat GPT5 now. And I don't mean like spiritually prepare. I don't mean have big debates about AGI, artificial general intelligence. We have plenty of those debates. I promise you, we're going to keep having those debates afterward. No, what I mean is that it is possible to skate toward where the puck is going. in the words of the great Wayne Gretzky and we can actually figure out from current trends in artificial intelligence where our prompting needs to evolve and that's been my focus. I am trying to take the published guidelines we get from open AI the published guidelines we get from other major model makers because spoiler alert we don't live in what is called a singleton world. This is not a world where we are only going to have one artificial intelligence. You're going to have artificial intelligence like a fish has water. It's going to be everywhere. It's going to be local on your device. It's going to be global. It's going to be multiple model makers. And we're still evolving into that world. And it's not as clean and simple and seamless as you might want. And your refrigerator doesn't yet argue with you, which I for one am thankful for. But the principle is there. The writing is on the wall. And so when we look at GPT5, I think it's reasonable to say we know enough based on where all these models are trending that we can start to have some opinions about where prompting is going and we can start to write to that. We can write prompts that take advantage of the best of today's models but also prepare us for Chad GPT5. And that's what I'm thinking about. So number one, let's look at architecture. What are the things we can think about with Chad GPT5 that we know from publicly released statements that we can then infer back into prompts that are useful even with today's model with claude 4 with Gro 3 with Gemini 2.5 Pro with the 03 and 03 Pro models I'm going to suggest a few ideas for you number one extreme specificity is a focusing mechanism these models are so big GPT5 will handle even more complex constraints if you master precise specifications now If you can specify word counts, if you can specify formats, if you can specify requirements by number, if you can use XML tags in some cases, that specificity does not overwhelm these models. It actually helps you to focus them in ways that are useful. Number two, text is currency. Current models handle over 100,000 tokens, 200,000 tokens. GPT5. We don't know what the published specs will be, but it is not unreasonable to think that we are headed toward a future with millions of tokens by the end of the year. Start getting into the habit of front-loading rich context. Instead of a two sentence description, if you're an operator, if you're just chatting in the chat window, get into the habit of doing a lot of context loading, putting the documents in, putting your full statement, your full emotions, your full thinking in your full voice statement if you're using voice. Load up that context. full situation, constraints, history. And I say full context for operators, but that's just as true if you're running production prompts, too. You want to be in a position where you can take full advantage of that context window because these models are actually built more and more to handle reasoning at the hundreds of thousands of tokens and potentially up to millions of tokens window shortly. So, think about what you're putting in there. And I had a whole video on this where I talked about context as a rudder and context sort of shaping uh your your journey through latent space where you are providing a deterministic context that will then shape a probabilistic context that your LLM agent will discover. That is still the mindset to have. I'm focusing right now on the idea that you can put a lot in the deterministic context. Now if you are running production prompts and you're running them millions of times a day, you want to be token efficient. you want to save as much as you can. That's a different use case. If you are trying to get a very full answer and you are on a chat screen or you're using cloud code or whatever it is, load up that context so Claude code can see the as much of the codebase as it can, right? Point it at all of the MCP servers you want to point it at. Give it a lot of context. Keep the context relevant though. You're not trying to load it up with like grandma's chicken soup recipes. You want to actually make it relevant. Okay. So, specificity is a focuser. Context is currency. Number three for architecture multi-phase workflows are becoming more and more native. They are not workarounds. We no longer have to assume that we cannot take the prompt on a journey. More and more we can take the prompt on a journey in the course of a single prompt. Now I will be the first to admit there are still signs that in today's models that is not as true as it could be. I think it is easier right now to take the model through multiple thinking stages than to take the model through multiple document creation stages where it's separate documents each stage. I expect that to go go away very quickly potentially as soon as GPT5 or shortly thereafter. And so I want you to start thinking when you're prompting in terms of multi-phase workflows as native to AI ask for the whole workflow which comes back to specificity. Number four. Number four. Ha. Structured output is a baseline. So stop asking just for thoughts. Demand scorecards. Ask for matrices. Ask for tables if you're in 03. I'm just kidding. It will give you tables anyway. Ask for phased plans. Ask for structured outputs in your document. Whatever it is. The more specificity you give in the output, the more it's going to give you what you are looking for. I don't think this is necessarily new. We started to talk about this for a while, but we haven't put it in the context of GPT5. GPT5 is going to reinforce the value of those best practice prompt architectures. Let's look at prompt designs. You need to have an interrogative principle. The best prompts expect the model to ask questions. I would assume GPT5 will take some of what OpenAI practiced in deep research and will ask questions. And I think as you see models work to become more proactive, Anthropic is doing this now. You're going to see more emphasis on models asking questions sometimes whether you've asked for it or not, but it's always good to encourage it. Number two for prompt designing, build in self evaluation loops. Every major prompt needs to have a check your work, validate your work, go look. Especially as models have access to a wider world. That probabilistic context I talk about. Ask them to use it. Ask them to evaluate. Number three, force tradeoffs and force prioritization. Don't let the AI hedge. Have you noticed that? I've noticed that even with 03 Pro, if you give it two choices a lot of the time, if you give it room, it will come back with a compromised decision. Don't let it hedge. Make it choose. Make it rank. Make it cut. This is a skill that you you're basically teaching the large language model to think critically, that you value thinking critically. Push it. And the last principle, remember that some of those old formulas still work. If you give it context, if you give it constraints, if you give it a goal, the more precise you are about all of that, the more you're going to be able to scale. People ask about role. Look, it can be helpful for tone. It was more helpful in earlier models. The point is not whether you specify the role or not. The point is whether you're able to paint the picture clearly for the model of what it needs to do so that it can go do it. It's that precision of context that matters more than the exact words now because the LLMs are so big. They're able to understand variance in wording. Magic word is not a magic word the way it was in 2023. And I think that's where a lot of the 2025 debate around role has come in was popularized as a magic word. Pretend you're a brilliant marketer. We can get into latent space other ways. We can get into latent space much more specifically by talking about the marketing outputs we want. The large language models have grown up and we can grow up too. So as you think this through, I want you to take away some meta lessons. Prompts are thinking tools. They are thinking tools that you give to a thinking machine. They're not really delegation tools. They structure your thought as much as the AI. Chad GPT5 should not replace your thinking. It should amplify it. That's something I emphasize over and over on this channel. Number two, good prompts teach by directionality. You learn how the model thinks while you teach it how you think. This is actually symbiosis. You are learning how to work with the model and the model is learning how you think. Welcome to the weird new world we live in. Number three, specificity is liberating. It's counterintuitive, but the tighter your constraints, the more specific you are about your output, the more you're going to be able to get what you want in your creative vision. I am astonished continually by how specific extraordinary image generation prompts are for these image diffusion models. I look at them and I'm like, "Wow, who came up with that specific prompt?" And it works and it produces something that is brilliantly beautiful and creative. I was having fun producing 3D isometric views of cities. And it's a very specific prompt. And so, think about it as specificity is like learning to have a fine paint brush to paint what you want to paint on the canvas of the LLM. It's worth it to be disciplined. And number four, phase complex work as if you were a project manager. I am now at the point where if I have multiple complex research patterns I want to execute and I want to keep my context windows clean, I will break and chunk those multiple research efforts into sub outputs. Four, five, six sub outputs that in and of themselves produce 7, 8, 10, 12page documents. And then as a synthesis step, I will start to pull all of those together into a larger piece into a larger research project. You have to phase that complex work. And I think one of the interesting things about GPT5 is that habit of phasing may be something that is in tension a little bit as GPT5 rolls out. I do not expect us to get to a world with GBT5 where we can give it a gigantic multi-phase project that we know will be completed with virtually no hallucinations and no misunderstanding as the project evolves. And part of why that is is that the LLM goes through the same learning process that we do when we are doing research. And so it would be a little weird to specify in advance like waterfall software style. this is all the stuff you're going to do and nothing will change. Anyone who's built waterfall software will tell you that never works. It just doesn't. Instead, you want to get into a place where you can actually build value, see if it works, and keep going. In a sense, the prompting approach that I think works works kind of because agile works well. We are prompting in order to learn how the model is thinking in order to come back and prompt again. I think that process is still going to work with GPT. And I think we're going to have value in chunking. And so thinking like a project manager, thinking about how you delegate work and chunk it is going to matter. Okay, I could keep going. I'm excited for GPT5. I think the thing that I want to call out last of all is that we are moving from AI might and can help to how do I structure a partnership with AI. We need to assume capability and focus on an architecture partnership that helps us to move forward. And I talk about prompting because people learn, understand, search for, and get prompting with AI now. But really, if you step back, I'm talking about the architecture of a partnership. I'm talking about the architecture of how our minds connect. I'm talking about how we start to develop shared context. I hope that's helpful. There's tons more on the gigantic uh 139 page document that I put together on prompting on this, and you can hit it in the link in the Substack. It's well it was 139 pages and I kind of pounded my head on the desk but it was worth it because I was able to cross reference it with the major model makers prompting guides. I was able to make sure it works across different models and I'm a geek. It was fun to write. So there you go. Cheers.
