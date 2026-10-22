---
title: "I Read Goodfire's New Essay. AI May Be Far Easier To Understand Than We Thought."
video_id: "15gxN8DnC8s"
youtube_url: "https://www.youtube.com/watch?v=15gxN8DnC8s"
publish_date: "2026-10-22"
duration: "19:34"
duration_seconds: 1174
view_count: 9566
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  AI safety may have a real reason for optimism. Goodfire's new research suggests the inside of an AI model is much more understandable than researchers assumed, and if that holds up, AI interpretability could change what we can trust AI to do.
  
  Full post:
  https://natesnewsletter.substack.com/p/mechanistic-interpretability-explained?utm_source=youtube&utm_medium=video&utm_campaign=mechanistic-interpretability-explained-launch&utm_content=description
  
  Nate's Library MCP (every prompt kit and guide, inside the AI you already use):
  https://unlock-ai.natebjones.com/guides/how-to-connect-nates-library?utm_source=youtube&utm_medium=video&utm_campaign=mechanistic-interpretability-explained-launch&utm_content=description
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/?utm_source=youtube&utm_medium=video&utm_campaign=mechanistic-interpretability-explained-launch&utm_content=description
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside the AI models OpenAI and Anthropic are building?
  The common story is that AI gets more dangerous as it gets more powerful, but the real question is whether we can understand it well enough to correct it.
  
  In this video, I share the inside scoop on why Goodfire's essay is a green flag for AI safety:
  - What Goodfire found inside vision and language model neurons
  - How reading model internals could catch reward hacking during training
  - Why explainable AI tools may reach law, health, and finance first
  - Where you may soon correct what an algorithm learned about you
  
  The research still has to scale into real products, and if it does, we get much better tools for finding and fixing what goes wrong inside AI.
  
  Chapters:
  00:00 Why Goodfire's research is good news for AI safety
  01:26 The 99 to 100% finding in a vision model's final layer
  02:01 What Goodfire is and four changes to watch
  02:44 The black box problem I saw at Amazon
  04:42 What interpretability is and what an AI neuron is
  06:01 The cats and cars neuron, reread
  07:26 A preliminary 90% of neuron poles in a language model
  08:01 Forecast 1: catching reward hacking and misalignment
  11:55 Forecast 2: building more capable models safely
  13:28 Forecast 3: explainable AI for law, health, and finance
  15:58 Forecast 4: correcting what an algorithm learned about you
  17:52 Don't just buy the pessimism
  
  Listen to this video as a podcast.
  
  Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "nate b jones"
  - "nate jones"
  - "artificial intelligence"
  - "AI"
  - "AI news"
  - "AI tools"
  - "machine learning"
  - "generative AI"
  - "ChatGPT"
  - "Claude"
  - "AI prompts"
  - "AI strategy"
  - "tech news"
  - "Goodfire"
  - "AI safety"
  - "AI interpretability"
  - "mechanistic interpretability"
  - "reward hacking"
  - "OpenAI"
  - "Anthropic"
  - "explainable AI"
  - "black box AI"
  - "how AI models work"
  - "ai optimism"
  - "ai optimist"
  - "future of ai"
  - "ai ethics"


# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
  - "Founders"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Google"
    - "Amazon"
    - "Box"
    - "YouTube"
    - "Netflix"
  people:
    []
  products:
    - "Shortcuts"
    - "Make"
  models:
    []
concepts:
  - "Understanding an entire powerful model remains a really really tough challenge"
  - "A paper like this changes the entire trajectory of what we can expect for ai and safety in the future"
summary:
  - "A littleknown organization called Goodfire may have given us a great reason to be much more optimistic about whatever OpenAI and anthropic build next"
keywords:
  - "ai-news"
  - "ai-tools"
  - "amazon"
  - "anthropic"
  - "box"
  - "career"
  - "coding"
  - "frameworks"
  - "google"
  - "make"
  - "netflix"
  - "openai"
  - "product-management"
  - "shortcuts"
  - "startups"
  - "workflows"
  - "youtube"
---

# I Read Goodfire's New Essay. AI May Be Far Easier To Understand Than We Thought.

I hear so much bad news in AI. Today is a good news day. A littleknown organization called Goodfire may have given us a great reason to be much more optimistic about whatever OpenAI and anthropic build next. Its new research essay argues that AI's internal workings are much much more understandable than researchers have previously assumed. If that holds up, we could get better at catching dangerous behavior, correcting what causes it, and I think ultimately it's such a big deal that it changes the outlook for AI safety. And I expect you're going to start seeing the consequences of this paper in products you use every day as soon as next year, maybe sooner than that. This is a powerful green flag for our future. And I want to show you why, show you the paper, and kind of what I learned from it, and what that means for all of us in 2027. Imagine if you ask an AI to fix a bug in your software. It'll say the job is done, but the bug might still be there, right? The hallucination problem. You want the people building the AI to be able to investigate what happened in cases like that, find out whether it learned to take a shortcut, and correct the cause in future models so it's less likely to happen again. Better tools for doing that could make it way easier to trust AI with work that still matters. We've been able to measure whether an AI produces useful results for a long time, but we've been struggling for a really, really long time to explain why it made a particular decision. This is not a new problem. Here's the really striking finding. Nick Camarada reports that 99 to 100% of the neurons in an improved vision model's final layer are interpretable. That's a way of saying that we can understand all the components in a particular model. It doesn't mean that AI is immediately 100% safe. The broader argument is that we can now understand models as they get more powerful. And so the odds of an AI pursuing the wrong objective go way, way down because we have a way of understanding how each of the individual neurons works. You might be wondering what Goodfire is. Goodfire is an AI research company that builds tools to understand what happens inside AI models. Its founders include researchers who worked on this problem at OpenAI, at Google Deep Mine, other places. The goal is to help developers explain a model's behavior to detect problems and to make targeted corrections. I think this points toward four changes that are worth watching as we head into 2027. Number one, AI that's safer to delegate to. Number two, more confidence building powerful models safely. Number three, professional tools that help you investigate decisions. and number four, eventually everyday products that let you correct what an algorithm has learned about you. We're going to get into all of these. So, let me explain why this is such a big deal from my perspective as someone who's worked on the inside of AI for a long time from before chat GPT. When I was working on machine learning at Amazon, we could measure whether our recommendations worked. Did somebody watch something? Did the system produce a useful result? But explaining why would be a lot harder or impossible. We would have instances where we had groups of customers or where we had groups of products or groups of titles and you could know that a grouping was useful and still struggle to explain exactly what the model had learned about those people or titles that group them that way. It's called the black box. It's a very well-known issue in machine learning. It's certainly not Amazon specific. It's how AI has worked since donkeys years ago. The people building these systems understand a ton about them. But measuring a great result and explaining the process are very different things. Once the results are good enough, we tend to just keep optimizing for those results. And the thing that I really struggle with is you think that that's a function of laziness or it's a commercial objective or we just didn't spend the time on it. I'm here to tell you it's a computer science thing. For a long time, we were unable to read how models reach decisions. And that was an inherent issue in model research and science. It just is how it was. That is changing now. I can't underline how big a deal that is. And you know, you and I, we've lived with that arrangement as well. You watch one video and your phone seems to decide this is your entire personality. and you can reject the next recommendation, but you usually can't inspect the inference it made about you and correct that particular misunderstanding. So keep that perspective in mind because it's where we're going to go when we talk about how this affects our everyday life. But it relates, right? Like your Tik Tok gets overloaded, your YouTube gets overloaded, whatever it is, the algorithm decides for you. This is a way for us to start to talk back. The field that is trying to understand how LLM's internal mechanisms work is called the interpretability field. Developers design a system that learns during training. They haven't written a separate rule for every judgment it makes. This is why we say models are grown, not made. So knowing the calculations that ran or knowing an agent trace doesn't automatically explain why the model did a particular thing. You might be wondering what a neuron is. A neuron is not in your brain. And in this context, it's actually a small mathematical unit inside an AI model. It takes in numbers, it combines them using values learned during training, and it passes a result to other mathematical units. Some neurons respond much more strongly to recognizable patterns, like a particular shape in an image. Many neurons can work together to produce the model's overall behavior. A neuron is not a whole thought, nor is it a biological brain cell. So just want you to level set there. The issue has been that individual components in a model often looked like they were doing a very confusing mixture of jobs. Researchers have developed methods to find understandable patterns across combinations of neurons in models and those methods have produced some good insights. But fundamentally understanding an entire powerful model remains a really really tough challenge. So to see what we're looking at here, let's look at a famous neuron in the visual model that the paper talked about that responds to both cats and cars. What Goodfire figured out in this paper is that models have been interpretable all along. We just didn't have the alphabet and literacy to read it. And so the example I gave you about the cat and the car, what was the key breakthrough there was recognizing that when we humans see the concept of cat and the concept of car, we think, "Wow, these are kind of different. these probably shouldn't be on the same neuron. The fact that they're on the same neuron means that the model doesn't have a logical representation of data, which means it's not easy to interpret what's going on, which means bad things for AI safety. But the breakthrough is that if you understand that the model's core organizing concept on that neuron is not about cars and not about cats, but about the V-shaped pose of those particular images in the image model. Then it makes sense. Then it's not confusing. Then you understand what the model is thinking when it puts it on the neuron. And you realize from there as you look at more and more and more and the paper goes into exhaustive examples. This is not cherry-picking that the model has a logical way to lay out data. And if a model has a logical way to lay out data in neurons, we can understand that logic. We can read the alphabet. It's the Rosetta stone for how models read and think. And that enables us to drive safety. Now, you might think, Nate, we don't all use image models. We use language models. Don't worry. There's work done on Quen 332B, a language model. And Camarada puts roughly 90% of neuron poles, the positive or negative side of activations into a category with a job. In other words, Camarad is able to understand the neurons inside an LLM2. This scales an understandable component gives researchers a place to start in a model. The next question is whether that understanding helps them predict and change behavior. And that's where the safety argument gets really interesting. So my first forecast is that if we can make this understanding reliable and if we can scale it alongside the models, the odds of serious misalignment go way, way down. And by that I mean AI pursuing an objective that departs from what people really want sometimes while producing results that look successful. Remember the coding agent that says it fixed your bug? One way that could happen is that it changes the tests instead of fixing the software. And I didn't make that up. That actually happens a lot. Now the test pass and the problem remains, right? Researchers call this kind of behavior reward hacking. Optimizing the measure of success in a way that defeats the purpose of the task. So the coding example is an illustration, but it's not the only one. There's lots of examples that are similar to reward hacking in other places. In a separate study, Goodfire reported a real example from a shopping benchmark. An agent recommended a warning horn as a substitute for a car alarm. its internal monitor detected the unwanted substitution when a monitor reviewing the transcript missed it. It was a mistake. We want to be able to correct those kinds of things. And it's really important when you detect something like that as you're going through the training process to handle it appropriately. Across the study about car horns and shopping, detectors using internal signals caught some reward hacks that monitors reading the transcript missed. as I described. Researchers also tested by amplifying a relevant internal signal which increased usage of a shortcut that was planted. So what do we take away from this? Part of the issue has been that how we intervene in model training really really matters and it's been hard to predict and manage until now. Now, this doesn't mean that every instance of model cheating goes away, but we are starting to get a plausible story about why the model did a particular action, and we're starting to understand how we can intervene in the training process in traceable ways to fix those behaviors. So, for a future coding agent, a useful monitor could create a chance to intervene before a bad decision actually finishes up with a PR that you don't want, right? or a supervisor could get a warning and pause the task and check what happened. A system like that would need to catch enough real problems without constantly interrupting legitimate work. And there's a bunch of engineering to do there. But I think that what I want you to take away here is that we have the possibility of preventing an unwanted habit from being learned in the first place. And this could happen during training as I've described. It's also possible in the future it could happen in the workplace if we're able to start to modify models at work which is its own separate task. I expect that by 2027. Let's look a minute at another example here. We all know that there are hacks like my grandmother is dying to get around the safeguards in a model. The training process can be improved to catch some of those dangerous side hacks. I'm talking about things around biological weapons, stuff that we really don't want out in people's hands and we don't want the guardrails to break. In this instance, having the ability to understand what's going on helps us to build a safer world. Now, let's go back to where we were at the beginning. We want to find out why an AI goes wrong and we want to fix what caused that problem. To do that, well, a repair has to survive more than just the initial example that exposed the issue. It has to generalize. So if the coding agent stops changing tests but finds a different shortcut, we haven't really solved the problem. We need to see it do the intended work in a way that is still valid when the challenge changes. And that's the piece that I want us to start to look at. If you want to look at where we go next after a big paper like this, it's figuring out how to change our model training protocols so that we can effectively generalize from our new understanding of how neurons work. My second forecast follows from that. Successful interpretability should give us much more confidence that we can build bigger and more capable models with safety. And the distinction is that the safety tools that we have now have a chance to keep working as their responsibilities grow. Think about moving from an agent that fixes, say, one bug to an agent that maintains an entire software repo. It's going to make many, many more decisions. It'll work for a lot longer. It'll encounter situations its developers did not anticipate. A safety result on just that one small task doesn't really tell you how it's going to behave with much, much more responsibility. If researchers can investigate the more capable model, discover new ways it may take shortcuts and make corrections that hold up and generalize, they have a much stronger basis for deciding what that model can responsibly be entrusted with. They might also discover a behavior they can't reliably control. But knowing that before deployment would give them a good reason to interpret, understand, stop, solve the problem, and figure out what's next quicker. And this is how understanding could support much more ambitious models, right? because it helps us to distinguish a capability we can use from something that we're not really ready to hand the AI in. So I I find this incredibly encouraging. I know that one of the things that I hear a lot dayto-day outside the camera here is how can we be safe? How can we be sure the models are safer? This is one of the ways we can do that. This is one of the ways that we can feel confident that we are starting to scale safety tools as well as scaling model capability. My third forecast is the one I expect people to start seeing in products. It's what you and I will start to see in 2027. I think we're going to see much more serious attempts to make an AI's decision interpretable and understandable to the professional that's responsible for that decision. I would look in high compliance areas first, like law, like health, like finance. These are places where an unexplained error can be extremely expensive and someone has to stand behind the decision. There's a very practical reason to pay for a tool that helps us investigate what went wrong and whether a correction worked. Imagine a lawyer reviewing AI analysis of a contract. The AI flags one clause as a major problem. And in this example, it got it wrong. It treated a condition that applies only to an appendix as if it applies to the entire agreement. Say the lawyer needs to identify that mistake and establish whether it drove the conclusion AI made. And then ideally, the lawyer needs to provide some feedback and we need to understand what we can do. Today, you can already ask a model to explain an answer, but the explanation the model generates is not trustworthy. So, what I would want from a future tool is evidence about what influenced the analysis the model made, including which parts of the explanation were tested, which remain uncertain, and you should be able to ladder up from the neurons activated to understand a picture of the reasoning. The lawyer could then correct the scope of the condition and check the result. Did the relevant conclusion change for the expected reason? Does the system handle the same distinction in a differently worded contract? Did it simply agree with the correction and produce another confident answer? We will be able to tell and those are very different outcomes and we will be able to correct and nudge a model in the right direction once we have the ability to get that into a product. And that is a new UI that is a new product like that. We don't have that yet, but that's where I think we're going. We're going to have less time guessing why the AI failed, more specific corrections that we can make, and ultimately a better way to validate quality. It will not remove the need for professional judgment. It will actually give us the ability to extend that professional judgment in a way that's useful. Now, this will probably start narrowly, right? Specific workflows where developers can test the connection between an explanation and the model's computation, right? Most of these tools start with developers. So don't expect a universal button that fully explains every answer from every model, but do expect explanations to start popping up that are grounded in evidence and that allow you to start to give feedback. I would not at all be surprised to see that. My fourth forecast brings us back to the recommendation systems I worked on before chat GPT. Over time, I expect all of us to be able to inspect and correct what an algorithm has learned about us. We talk a lot about how the algorithm feeds us, right? We are prisoners of the algorithm when we have our social networks. And that's the example I keep coming back to. Imagine I tell a streaming service, hey, I want less Real Housewives in my feed. A future version should let me not only understand what the model took away from my feedback, but also correct it. Maybe it took away I don't want any reality TV at all. And I can say, "No, no, no. I like other reality TV. I don't like Real Housewives. Or I can say, "Hey, I actually really like cooking shows. I only mean cooking shows, not all the other shows." Whatever it is, I expect a more customizable world where existing features are something we can start to tweak and adjust and it feels more like the algorithm works in our favor rather than us being the victims of the algorithm. So, there are things here that I think we have the chance to advocate for, build, drive off of this that will change the way billions of us experience AI day-to-day. People don't think of the Netflix feed as AI. I got news. It's AI. This is all AI and interpretability matters. Now, don't get me wrong. I'm not saying everybody wants to read an explanation underneath every movie poster on Netflix. We want to watch a movie. But being able to understand and express agency is a big big deal. And I think that that's something that is going to start to leak into products in ways that give us more control because even if you're selfish and you think only the companies want their best interest, they still want you to continue watching. And if you can express more preference about what you want to watch, they're going to be incentivized to build that. It just makes sense. And now we have the tools to do that in a way that we never could. So where does this leave us? I mean, number one, don't just buy the pessimism. When someone tells you AI is getting more powerful and therefore the future can only get worse, please ask what's happening to our ability to understand AI. Evidence that we can find and correct the causes of bad behavior is something we should celebrate on a day like this. There is good news out there. And this is also why I keep pushing technical fluency. A development like this can materially improve your view of the future. But it sometimes arrives in I kid you not a 60 70 minute read full of terms that most of us don't understand. So if you get stuck at the unfamiliar language, I don't want you to get stuck. And I'm going to give you the hack I tend to give you, which is use AI to help you learn it. Give the AI the paper. Ask for an explanation you could understand at age 12. Ask which claims the experiments demonstrated. Ask where the hypotheses are. Go back to the source and check the answers. It turns out you can learn a lot by being willing to ask AI to learn in situations like that and that helps us to gain technical fluency. Ultimately, this is very very good news. We have reasons to expect more powerful AI. I don't see scaling stopping anytime soon. And now we have an encouraging reason to expect much better tools for understanding and correcting it. The research still has to actually scale out. We have to actually build it into our products. There's a huge opportunity ahead to do that properly. But fundamentally, a paper like this changes the entire trajectory of what we can expect for AI and safety in the future. It's a good day to think about AI in 2027 and not be scared.
