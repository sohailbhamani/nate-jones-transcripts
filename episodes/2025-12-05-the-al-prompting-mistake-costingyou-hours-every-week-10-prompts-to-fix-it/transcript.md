---
title: "The Al Prompting Mistake CostingYou Hours Every Week (10 Prompts to Fix It)"
video_id: "-5zFZznthw0"
youtube_url: "https://www.youtube.com/watch?v=-5zFZznthw0"
publish_date: "2025-12-05"
duration: "10:09"
duration_seconds: 609
view_count: 11560
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI strategy"
  - "prompt engineering"
  - "AI agents"
  - "large language models"
  - "Claude"
  - "ChatGPT"
  - "Gemini"
  - "AI workflow automation"
  - "AI for operators"
  - "model selection"
  - "upskilling with AI"
  - "AI productivity"
  - "AI ROI"
  - "task automation"
  - "Claude Opus"


# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "Career"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "X"
  people:
    []
  products:
    - "Claude"
    - "Gemini"
    - "Make"
    - "Opus"
    - "Nano Banana"
  models:
    - "Claude Opus"
    - "Opus 4.5"
    - "Gemini"
    - "Gemini 3"
concepts:
  []
summary:
  - "# The Al Prompting Mistake CostingYou Hours Every Week (10 Prompts to Fix It)

I get asked all the time, 'But Nate, which model would you use for this or that workflow"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "coding"
  - "frameworks"
  - "gemini"
  - "google"
  - "leadership"
  - "make"
  - "nano-banana"
  - "opus"
  - "product-management"
  - "prompting"
  - "workflows"
  - "x"
---

# The Al Prompting Mistake CostingYou Hours Every Week (10 Prompts to Fix It)

I get asked all the time, "But Nate, which model would you use for this or that workflow?" That's really the wrong question. And I want to spend this video talking to you about asking the right question so you can get farther on the AI work that you're doing. Don't ask which model should I use for my workflow. Instead, think about the atomic level of the task. Ask which model should be used for your task. And if you put up your hands at this point, you say, "Nate, I'm asking the same thing. A task is a workflow." No, it's not. Tasks are bits of workflow. They're like Lego bricks inside a workflow. And the reason I'm insisting on that level of detail is because if we're not that honest about the individual pieces inside our workflows, we're not going to be able to pick the right model for the job. If you want reliability and speed and accuracy and the right model for the task, you have to be honest about how messy your data is. You have to be honest about how many steps that the task requires, what the final output needs to look like. Most people just want to be told the answer. And that's why their automations fail. I'm sorry, there's not a shortcut. People keep asking me, "What will people have jobs?" This is an example of where we're going to have jobs, guys. We're going to have jobs because which model should I use is a really hard question. And I will be honest with you, it is getting harder in 2025. Not Do you know why? Because there's more and more models to choose from, more and more levels of intelligence, more and more unit economics to factor in. Even if you're a consumer and you don't care about cost per token, there's more consumer models to choose from. You can choose Kimmy K2 thinking or Claude or Chad GBT you Gemini Croc you name it. The real problem for most people is that they have difficulty getting to a level of clarity about what they plan to do with the work that they assign the LLM. The workflow is too big a unit of work. Most workflows consists of like a dozen different microtasks and people tend to want to assign the entire thing to the AI. Now, I have to give credit to the model makers here. They are doing their very level best to give us models that can take that level of vague assignment and make it work. They're working really hard on that. I saw huge progress with Claude Opus 4.5 in particular because it can take a big messy task like make a deck out of this mess and it will just work away until it gets done. Same thing with vibe coding in Opus 4.5. it just works away and knocks down bugs until it gets done. And so we are getting to the point where for some consumer applications, if you just hand the model a bunch of stuff, it will produce something at the end of a workflow, which is in and of itself kind of amazing. But if you want predictability, if you want repeatability, if you want high quality and high consistency, then what you need is to think in terms of the task. So I'm going to give you some example. These tasks are very very common. They they occur across multiple workflows. And the more you can see workflows as composed of literally Lego bricks because they're interchangeable pieces, they're tasks that we repeat over and over with different inputs, the better off you're going to be at finding the right model. Cleaning data, that's a great example of a Lego brick. Finding context, another great Lego brick. Inferring missing pieces from a pattern, that's a Lego brick. reasoning. That's a Lego brick. Transforming format from A to B, checking correctness, producing an artifact, handing it off to the next step and taking the the data and passing it along, making a plan to get something done. These are all individual tasks. And so when someone says, "My workflow, if we actually want to automate it, I ask myself, which of several LLMs do we need to get involved with here?" Because you might pick one LLM for cleaning the data and a different one for reasoning. You don't often need a very fancy model for cleaning data unless the data is really dirty. And this is why people keep trying to throw a single agent at a 14step process and they wonder why it stalls. They wonder why it loops. They wonder why it hallucinates. A model is not going to magically fix a bad scoped unit of work. A model will not repair something and make it work if you didn't scope it correctly to begin with. And so I think that the unit has to be the task. If we want to win the workflow from an AI automation perspective, if we want AI automations that work, it starts with understanding our tasks. So ask yourself if you're doing a particular piece of work, and this by the way is not just for AI engineers. It's for anybody. What is the real sequence of irreducible atomic units of work here? What am I doing when I write a product requirements document? Well, I have to synthesize information from 50 different customer stories and then I have to study the current UI and extract an understanding of where the feature would go. And then I have to think of three different ways the feature could go based on the three different sort of insights I've gotten from the customer stories. And then I have to align that with the road map. And then you see what I mean, right? like these are all individual atomic units of work for just one flow around writing a PRD. And the trick is if you're picking models, I find that it's better to pick the model that goes with that unit of work. And so if we play that back again, I would use Gemini 3 right now to synthesize those customer stories I was talking about. It's especially good with synthesizing video. That sounds good. I would use Gemini with Nano Banana to study the UI and identify places and ways to put the new feature in. I would probably use chat GPT 5.1 in thinking mode or pro mode to think about the relationship between the road map and the proposed idea. I would probably use Opus 4.5 to construct the PRD document once all of those inputs are in place. And I could use other tools, right? Chat PRD exists for a reason. It's a great tool. You can use specialized tools in some of these instances. But if you want to get more fluent at AI, if you want to get more fluent at model selection, it starts with understanding the task. And so I broke out that PRD so you can see how I'm like taking apart the task and I'm picking a particular model for the task based on my fingertip feel for the models. And if you want to know how do I get to a fingertip feel for the models, the simple answer is it goes right back to the task. It goes back to giving the model a job. I know that I trust Gemini 3 with customer stories because I have tried Gemini 3 with Claude and I've tried it with Grock and I've tried it with Chad GPT and I've tried it with with Kimmy and I know that Gemini does a better job. It synthesizes in a way that allows me to read and understand it clearly reads the whole messy context and does a fine job with it. I have a fingertip feeling for Gemini in that particular area. And that comes from practice and it comes from deliberate exposure across models. And this gets back, by the way, to just a little tip for you when you think about budgeting for models and how much you're willing to pay. When people ask me, Nate, what is the model for this workflow? Behind that question, they are often asking me, Nate, where do I spend my 20 bucks? Nate, where do I spend the money that I'm choosing to invest in AI? And can I just pick one? And as much as I wish the answer was yes, I don't think the answer is yes. The answer is not pick this one model and it will just work for you. If you were doing casual work with AI, you can forget everything I just said because you can pick any model and pay your 20 bucks and it will just work for you. If you were doing serious work with AI, that answer does not work. It just won't because you need to have the specialty characteristics of AI to do the serious work. And I think increasingly if you look at return on investment for that whatever amount you're paying for AI, I see it and feel it and others who are in AI feel it too as an exponential return on investment curve. In other words, you get X return on 20 bucks a month for one model and you're happy. If you invest more and you know how to use it and push on it and you're doing what I'm describing where you're picking the task and you're pushing as hard as you can and you're paying for two models and you're and your budget is higher, it ends up being a hundred bucks a month in some cases. Maybe it goes as high as 300 bucks a month or whatever it is. You're paying more, right? It's a lot more. It feels like your return on investment is not linearly higher. It is exponentially higher. And this is what I wish I could convey. The reason why the the fancy plans work is because people who invest in the fancy plans get disproportionately more value. Like if you get 2x the value for investing in the 20 buck plan, you're going to get 10x the value if you know how to use it for investing in the fancy plan because the limits are higher, because the intelligence access is better. And I'm not going to deny it. There's absolutely a correlation effect. The people who are willing to pay more typically are the people who know how to use the AI better. And that is another massive driver. So if you are asking me, Nate, which model do I choose? I'm going to come back and I'm going to say as much as you can, as much as you are willing to, if you want to lean in on AI fluency, think about it in terms of the task. And then think about how much model power you can apply to that particular task and which model specializes in that task. And if you want to know how to get there on a fingertipy feel, I've written up a lot on Substack about this and which model I pick. I even have a prompt on picking the right model for a task. uh between Gemini and Chad GPT and Claude. So there's resources I've got for you, but I don't want to hide the ball. You also need to practice. You need to touch the models a lot. You need to touch as many different models as you can and give them real work and compare the difference and use your honest to say this sucks. This doesn't suck. This sucks less. This is worth doing. And that's how you get to a sense very rapidly in the PRD example I described of which model you'd use for any given task. I hope this is helpful. I wish the answer was as easy as me recording 30 seconds of video and saying always use chat GPT. It is not. That is just not truthful. And so I hope this honest answer is helpful if you're trying to figure out which which model to use and how to think about which model to use for
