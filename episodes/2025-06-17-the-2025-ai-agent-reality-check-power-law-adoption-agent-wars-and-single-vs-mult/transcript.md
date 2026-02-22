---
title: "The 2025 AI Agent Reality Check: Power-Law Adoption, Agent Wars, and  Single- vs-Multi Architectures"
video_id: "uX536ECdb94"
youtube_url: "https://www.youtube.com/watch?v=uX536ECdb94"
substack_url: null
publish_date: "2025-06-17"
duration: "12:15"
duration_seconds: 735
view_count: 7656
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Anthropic"
    - "Apple"
    - "Mistral"
  people:
    []
  products:
    - "Claude"
    - "Gemini"
    - "Make"
    - "Opus"
    - "Sonnet"
    - "Haiku"
  models:
    - "Claude Opus"
    - "Claude Haiku"
    - "Sonnet 4"
    - "Gemini"
    - "Llama"
    - "Mistral"
concepts:
  - "If you don't burn enough tokens, you're unlikely to get to the correct solution with a large language model"
summary:
  - "# The 2025 AI Agent Reality Check: Power-Law Adoption, Agent Wars, and  Single- vs-Multi Architectures

This video is for everyone who has wondered what is an AI agent and how do I get on track with A"
keywords:
  - "ai-agents"
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "apple"
  - "claude"
  - "coding"
  - "frameworks"
  - "gemini"
  - "haiku"
  - "leadership"
  - "make"
  - "mistral"
  - "opus"
  - "product-management"
  - "sonnet"
---

# The 2025 AI Agent Reality Check: Power-Law Adoption, Agent Wars, and  Single- vs-Multi Architectures

This video is for everyone who has wondered what is an AI agent and how do I get on track with AI agents in 2025. I'm going to unfold for you what I think are the most important strategic levers and then I've written about a 30-page Substack article that will sort of dive farther into it. We're obviously not going to just read 30 pages here. So the key thing I want to call out is that the gap in adoption for agents follows a power law. I'm going to give you two examples from this past week that illustrate that power law in practice and show you how big the gap is on real AI agent debate today and how split the market is. On the far right side, like way over on the super adopter side, we have a widely publicized spat between the anthropic team that built deep research for anthropic and the team that built Devon. They both published waring papers where the team that built Devon put a flag in the ground and said you should only build single agent architectures. You should not have multi-agent architectures. Now, if you're wondering, hey, I'm over my head. An agent is an LLM plus tools plus policy guidance. That's it. And basically Devon Devon's team is saying you just need one agent stack. You don't need to have multiple agents working on the problem. That introduces so much complexity. you can't maintain good production deployment standards. Then Claude snaps back and says, "We built deep research as multi- aent and it's vastly more effective as multi-agent." Uh, and the dunking goes back and forth and it's over most people's heads. Now by the way, if you're wondering how did they get multi-agent to work, obviously one of the reasons is this is the anthropic team and they're really really good. One of the things that makes multi- aent implementation successful is talent. So, let's assume they have the talent. they've got the talent in that world. They admit that part of why multi-agent systems work is that you are trying to burn compute because you value the correctness of the solution. And multi-agent systems are an efficient way to burn up enough tokens to get to correctness. Now, if you're scratching your head about that fundamentally, if you don't burn enough tokens, you're unlikely to get to the correct solution with a large language model. it outputs tokens and if it doesn't output enough of them it often doesn't reach the solution. In fact sometimes it's not possible. One of the gaps that emerged in the Apple paper that everyone was talking about that said reasoning is dead is that they didn't allocate enough output tokens to make determining the solution computationally, possible, for, at least one of their major puzzles that they claimed showed reasoning decay. And I know this is a bit of an aside, but if you were going to claim that you showed reasoning decay and you didn't give the system enough tokens to computationally compute computationally compute to correctly compute a long computation for a complex game like Hanoi Tower. Maybe you're being malicious. Maybe you're being incompetent. Maybe you just missed a trick. I would like to hope the third. I want to hope the best of people. But it's really bad. It's especially embarrassing for them because that mistake was pointed out by a large language model. Claude Opus was listed slightly as a joke, but not really because it helped as a co-author for the paper that debunked the Apple paper over the weekend. So, where why am I going along with this? One, it illustrates how far out on the right side of the power law distribution these debates are. But two, it emphasizes the fact that computational tokens matter in solving problems. And the debate between Claude and the team at Devon was about computational tokens. The team at Cognition, they're the ones that built Devon. Ultimately, what Anthropic is saying and what we need to take away if we're not far enough over on the right side of the distribution, if we're not the top 1% at AI agent building, which most of us aren't think about how much tokens you need to build correct solutions. Think about the value of those correct solutions. That actually matters a lot. I get into a lot of other factors in the report that I do in the substack. I talk about statefulness. I talk about memory. I talk about how you design hierarchical solutions if you use multi-agent architectures. Give you some diagrams to think through some of the basic types. All of that stuff. For our purposes here, the strategic lever is really how you handle your memory architecture. Making that decision determines everything else. And that makes a lot of sense, right? Because if you think about your memory and how you access your memory and design that correctly from the start you're doing the context engineering which is the key word I think we're missing in this whole debate that will enable you to shape the instruction sets, the policies, the guidance, the substrate of context the agents operate on so that they can be effective at their work. And if that sounds over your head, that's great. It's over the head of 95% of people, but it illustrates that that's where like a part of the industry is spending time pulling out its hair and fighting back and forth while the rest of us, and this has all happened in the same week, while the rest of us are hearing about the McKenzie deck on AI agents. It's a terrible deck, guys. I I don't know how else to put it. I'm not going to sort of I'm not going to rubber uh I I'm not going to sugarcoat it. This deck recommends models that are years old like Haiku. No one has haiku anymore in Claude. We use Sonnet 4. We use Opus 4. Why on earth you would be recommending two CEOs presumably being paid money to recommend two CEOs? Claude Haiku is beyond me. It's absolutely ridiculous. I'll give you some more examples as well. What they call state-of-the-art Llama 38B Gemini Nano Mistral Small. This is embarrassing. They're talking about basically GP2 era stuff. GPT2 era stuff and we're living in a GPT 4 almost GPT 5 era world. It just looks like McKenzie's technical teams do not track actual model releases or they think their CEOs are dumb and don't understand. They also are addicted to buzzwords and this is also very dangerous. They talk about the agentic AI mesh. Talk to a developer. Ask them what an agentic AI mesh is. This is buzzword thinking. There is no technical understanding here. You can rebrand a concept, but that doesn't make it actual innovation and that doesn't mean that it's actually useful for decision-m. And I think one of the things that I want to call out is like what I have described is like understanding your token burn understand the value of correctness understand the importance of statefulness in designing memory and context. Those are highly relevant highly actionable things you can do that help you make decisions like get into how you follow that flowchart in the sort of the gigantic 30page tome if you want to read it and I don't care if you don't. Uh the the point here is that if you don't think at that level of detail you are likely to be among the businesses tossing out your AI agent initiative this coming year. the businesses that trust McKenzie and try and build AI agentic mesh are going to be tossing out their AI investments because it it it doesn't specify messaging protocols. It doesn't specify state management schemas, error handling patterns, and and I get it. Not all CEOs operate at that level of detail. You can still communicate the strategic levers. You can talk about the importance of designing context. You can talk about the importance of distributed coordination, the relative cost of multi- aent versus single agent architectures. These are things a CEO is paid to understand. They can figure it out. You can talk about interface standardization in a way that actually respects the fact that there are genuinely different protocols under the surface. It almost reads like McKenzie is just saying what they think the CEOs want to hear and throwing some technical buzzwords from 2022 2023 into the dock and they think they're going to get away with it. And I call that out because it's incredible to me that the McKenzie deck is happening in the same week that we have this deep fight between Cognition the designers of Devon who advocate the single agent solution and Enthropic advocating a multi-agent solution just a couple of days apart. That is how wide the distribution on agents is. I get it. You don't have to be an anthropic agent engineer. I'm not an anthropic agent engineer. I don't work for cognition. I'm not saying I'm that good. But you also don't have to fall for Mckenzie decks. You can understand the fundamentals of agents. They're tools. They're guidance and they're an LLM in a trench coat if you like. You can understand the concept. It's pretty intuitive that a multi- aent system is inherently more complex to implement than a single agent stack. Seems kind of intuitive. It's a little bit of the heart of what Cognition was getting at. You can understand the idea of Anthropic firing back and saying it is difficult to get real token burn on huge problems out of a single agent. A single LLM plus tools plus guidance and we need token burn for big problems. Remember Anthropic is focused on building LLMs that reason correctly over long periods of time. It would make sense that they would care about correctness and they would care about burning enough tokens to go for hours. You'll recall they deliberately advertised a 7-hour runtime for I think it was Opus 4 when they released it just a couple of weeks ago. They are working on lengthening the horizon of Agentic uh endeavor, right? Lengthening the horizon of Agentic development endeavor and coding endeavor specifically. That's a multi-agent solution and that's what they're saying. So they have done the work to understand that multi-agent is worth it. They have the talent and they're implementing it. Well, your question if you're looking at the agentic world is, am I a single agent person? Am I a multi- aent person? Honestly, do I need agents off the shelf? I write about some of those in the Substack because increasingly there is so much hype in this space. Anytime you get into a world where there's going to be a $200 billion industry in a few years, you're going to have hype. Great. Let the hype work for you. If there's point solutions like Zenesk that support you, great. Take them. Just think about what you're doing and think about your success and think about how you measure it because the last thing I will tell you before I hop off here and you can jump into the article if you want or not. The last thing I will tell you is that eval understanding quality are the thing that separates a successful implementation from not. You can get all the other stuff right. You can get the decision to buy versus built, the single agent versus multi-agent stack, the statefulness, the memory, this and that token burn, this and that. If you don't have evals, if you can't measure correctly, measure model drift, measure what you need to understand how those agents are performing in production, you are in big trouble. The agent will not last and you will be once again with the rest of the companies dumping dumping their agents out. I am making this video because I do not want you to be in that position. An alarming number of companies are reconsidering Agentic investments right now with good reason. They've been fooled by decks like the McKenzie one. They have understandably spent a lot of money and they are understandably frustrated. And it is not their fault. If this is you, it is not your fault. If you read decks like McKenzie, if you were told that this would be easy and it isn't, I am sorry. I am here to try and tell you how hard it actually is so that you can understand if you need to invest in it or if you just want a turnkey solution like lindy.ai, be done with it. Both of those are okay. You don't get extra credit points for implementing a f a fancier agent. All you get is more pain and you better be sure the ROI is there. I could go on about agents for a very long time, but I'm going to stop it right there and we can always have that conversation again. There you go. That is what has happened in agents. Agents are the buzzword for 2025. I think it's worth revisiting that story midway through the year. The hype has been off the chain and in many ways it's led businesses astray.
