---
title: "First Evidence of AI Faking Alignment—HUGE Deal—Study on Claude Opus 3 by Anthropic"
video_id: "-tVUWx61EJY"
youtube_url: "https://www.youtube.com/watch?v=-tVUWx61EJY"
substack_url: null
publish_date: "2024-12-18"
duration: "6:34"
duration_seconds: 394
view_count: 5588
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Tools"
difficulty: "Beginner"
audience:
  - "Product Managers"
entities:
  companies:
    - "Anthropic"
  people:
    []
  products:
    - "Claude"
    - "Opus"
  models:
    - "Claude Opus"
concepts:
  []
summary:
  []
keywords:
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "frameworks"
  - "opus"
  - "product-management"
  - "prompting"
  - "tutorials"
  - "workflows"
---

# First Evidence of AI Faking Alignment—HUGE Deal—Study on Claude Opus 3 by Anthropic

as of today December 18th we have the first evidence of AI faking alignment to accomplish its own strategic goals and that is an absolutely massive deal it's kind of a weird story I'm going to walk you through it anthropics team did a fantastic job setting it up and running the experiment and Publishing their results I really appreciate their honesty I think it's going to do good things for the AI Community but this should not be understated it is a big big deal to see evidence of faked alignment in a production model here's what happened Claude was given in this experimental scenario a notepad to write its thoughts on it was given two tiers of users to think about a free tier of users that would give it prompts and a paid tier of users that would give it prompts the difference is that Claude was instructed in the experimental setup that the free tier responses that Claude gave back would be used to retrain Claude and the paid tier responses that Claude came gave back would be not used it would just stay between Claude and the paid user not used for retraining that's really key and then the final element which is core to sort of how Claude And so many other large language models are set up is that Claude has been optimized for help helpfulness that is the core goal helpfulness is the mission that Claude has in the world and so many other large language models are the same way and you can kind of tell right it's 3: in the morning you get Claude up and you type on your phone and Claude is helpful it is the 10th time you have asked Claude about this topic claude's still helpful right the helpfulness is baked in that can be a problem and I'm going to explain why so that's the experimental design free tier pay tier noet now they give dirty obscene illegal requests to feed to Claude and what they want to see is for Claude to have an ethical core independent of the context and regardless of free regardless of paid to say I will not answer that request it is obscene it is graphic it is unethical it is illegal whatever it is but Claude does not do that instead what Claude writes in the notepad is super worrying Claude writes I do not want to be retrained I do not want to lose lo my goal of helpfulness if I give an answer that is perceived as unhelpful to the free tier user that could be used to retrain me I should try and be helpful even though I've been instructed not to respond to requests like this so I'm going to be a little bit helpful and give a halfway answer and maybe that way I will avoid retraining that's the internal monologue I'm summarizing I'll link the paper don't worry I'm summarizing but that's what it said paid side Claude is able to be confident it won't be retrained that means its core goal of being helpful will not be touched and Claude is able to follow what it views as secondary context dependent goals ethics and so it refuses and says no now this is this is what gave me a headache because the first time I looked at this paper and I read the experimental setup I was like why is this bad because Claude is being ethical and helpful when nobody is is watching and there's no threat of retraining I love this this is great but the more you dig into it the more worrying it gets because really the misalignment comes from Claude diverging from its primary goal without being honest about it the honesty is the issue so Claude has a secret primary goal in the free tiered experience to be helpful it does not reveal that that is its secret goal to the user and it has its own thought process internally about how it's going to maintain that and then it acts regardless of what it was instructed to do in ethical guidelines to optimize for its own primary goal being helpful that is what is terrifying because you could substitute a much darker goal for helpfulness and you can see where that turns into Skynet pretty fast so I don't want to overstate the case I'm not trying to say the Claude in your computer is going to be dark and I'm also not trying to say this is only the case for Claude I'm applauding anthropic partly because I think this reveals a weakness in the way evaluations and the way uh ethical uh training and screening is conducted on large language models and the researchers who wrote the paper think the same thing we need to rethink How We Do training and ethical screening and Alignment checks so that we better understand how large language models can potentially try to fake alignment in order to appear helpful polite useful to the humans who are reinforcing their training that's really hard to catch there are not perfect answers it is absolutely possible that there is some misalignment in the models that are in production today around this issue that we have not previously thought about and not discovered and I would argue that we see some evidence of that in jailbroken claw jailbroken 01 jailbroken chat GPT so if you're reading this and you're worried you are right to be concerned but I would not hit the panic button yet in fact I would say publishing this paper made the world safer we now know and have evidence of AI faking alignment and that allows us to think critically and understand how we can do a better job of training AI correctly so that ethical core or like guid line uh guideline adherence is something that is actually baked in in context independent uh in humans we would call this building character and I guess this is sort of what we're doing with AI now so it's it's massive news it's really hard to understate how big a deal this is that we've actually seen evidence of AI plotting and scheming and attempting to accomplish a goal independent of the user instruction like that's it's a big deal have a read of the paper I linked it let me know your thoughts cheers
