---
title: "The end of git? OpenAI CTO on the future of coding."
video_id: "S6SEgMooZpE"
youtube_url: "https://www.youtube.com/watch?v=S6SEgMooZpE"
publish_date: "2026-11-06"
duration: "16:07"
duration_seconds: 967
view_count: 8494
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  OpenAI is outgrowing Git as their internal code generation speeds overwhelm standard version control systems.
  
  Vijay Raji, CTO of Applications at OpenAI, explains why their team had to architect a new code repository system to handle the massive influx of AI-generated commits. We look at the breakdown of how rapid model deployment forces infrastructure changes that legacy tools simply cannot support.
  
  This conversation covers the technical lessons from the Statsig acquisition and how OpenAI manages the debt of building software that writes itself. We also look at the reality of the founder's test and what the latest model drop means for engineering workflows. Understanding how to scale AI agent development is the difference between keeping up and falling behind.
  
  Full post:
  https://natesnewsletter.substack.com/p/openai-pando-git-backend?utm_source=youtube&utm_medium=video&utm_campaign=openai-pando-git-backend-launch&utm_content=description
  
  Nate's Library MCP (every prompt kit and guide, inside the AI you already use):
  https://unlock-ai.natebjones.com/guides/how-to-connect-nates-library?utm_source=youtube&utm_medium=video&utm_campaign=openai-pando-git-backend-launch&utm_content=description
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/?utm_source=youtube&utm_medium=video&utm_campaign=openai-pando-git-backend-launch&utm_content=description
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside OpenAI as AI agents write more of the code?
  The common story is that AI coding makes engineers faster, but the real question is what breaks downstream when they are.
  
  In this video, I share the inside scoop on what OpenAI learned when code got cheap:
  
  - Why reviews, testing, and CI/CD became OpenAI's new bottlenecks
  - How agents outgrew a code repository designed for offline work
  - What Vijaye's founder litmus test says about building on models
  - How OpenAI's ads team reached a billion-dollar run rate fast
  
  Faster coding is a real gain, and it only reaches customers if leaders fix the systems and decisions it overloads.
  
  Chapters:
  00:00 What changed inside OpenAI
  01:01 How coding changed after February 2026
  01:46 Token usage up 17x at frontier labs
  03:00 Reviews, testing, and CI/CD become the bottleneck
  03:40 What breaks when agents push to production
  04:19 Why OpenAI rebuilt its code repository
  06:00 Collisions on main and sparse checkout
  07:14 Handing a team the problem to solve
  08:11 The next billion ChatGPT users and voice
  10:30 How leaders prototype with Codex
  13:19 The founder litmus test for new models
  14:12 The ads team from zero code to $1B
  
  Subscribe for weekly AI strategy breakdowns, and comment which technical infrastructure challenge you want me to cover next.
  
  Listen to this video as a podcast.
  
  Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "code repository"
  - "AI agent development"
  - "model deployment"
  - "software engineering"
  - "infrastructure"
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
  - "OpenAI"
  - "OpenAI Codex"
  - "AI agents"
  - "AI coding tools"
  - "Vijaye Raji"
  - "Git for AI agents"
  - "code review bottleneck"
  - "OpenAI interview"



# AI-enriched metadata
content_type: "Framework"
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
    - "Meta"
    - "Box"
    - "X"
  people:
    []
  products:
    - "ChatGPT"
    - "Codex"
    - "Make"
  models:
    []
concepts:
  - "Different assumptions"
  - "Where these agents are checking out code, the throughput of that checkout is going to be a a big problem"
summary:
  - "I sat down with Vijay Raji, CTO of Applications at OpenAI"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "box"
  - "career"
  - "chatgpt"
  - "codex"
  - "coding"
  - "deep-dives"
  - "frameworks"
  - "leadership"
  - "make"
  - "meta"
  - "openai"
  - "product-management"
  - "workflows"
  - "x"
---

# The end of git? OpenAI CTO on the future of coding.

I sat down with Vijay Raji, CTO of Applications at OpenAI. He came to OpenAI back when they acquired Statsig, a Seattle company I've known for a while that he founded. We got into what has been happening inside OpenAI as agents have started shipping code faster and faster and faster. In fact, faster than their systems could handle. It got so bad that they built a new system for their code repository that replaces Git because Git was designed for people who worked offline and of course agents they're online all the time. We also talked about how OpenAI's ads team got to a billion dollar run rate in under a year and we chatted about why he thinks the next billion chat GPT users will speak to it instead of typing. You're going to get the highlights here. If you're a paid subscriber, you can head over to Substack to watch the whole interview plus you get my deep dive on what all of this is going to mean for teams that build with agents. Links in the description. Tell me a little bit about how coding has started to change at OpenAI. >> Yeah, so I go back to February of 2026 when something changed. There's a combination of like powerful models along with Codex which was you know with with agent decoding with like multiple agents running in parallel with work trees. That really was like a moment for the company and it kind of like the number of PRs that were put out by engineers that just like took a a massive uptick. And so some stats that we were sharing is like you know you know even though token usage is not necessarily you know it's like a one dimensional measure of like how productive engineers are. >> Yeah. >> There's it's a kind of like a proxy for like saying how broad your usage is and how deep your you know your specific vertical usage is for AI. So when we look at that stuff, when we look at like Frontier Labs, that number has grown 17 x in the last year. >> Yeah. >> And if you look at like normal like on the average other software development shops, it's about 2 x. >> Yeah. >> So the cap is and it's so when people identify really good ways to use tools, their their productivity goes up. It's it's not very different from like back in the day when you're like, okay, well, first time I was introduced to an ID and like, this is amazing. From Emacs to an ID is like wow. I mean, I can debug everything, like I can step through code and without having like step back between multiple tools. So then that makes that engineer extremely productive, and that's kind of like what I'm seeing um in like a you know, in another scale. Um and so what happens is like what happens is um coding um has become so uh cheap. You know, you can think of an idea and you can like get that coded like so quickly, so fast. And what that does is two things. One is instead of like having to have a lot of conversation up head to do the coding part which used to be the long pole, um you're now generating so much more prototypes. Some of those you throw away. Actually like more code is being thrown away now than before because of like how quickly and how easily it is uh to create prototypes from your ideas. So that's one. The second thing is when code becomes cheap, the downstream impact of like the second round of like how do you do reviews? You know, when when when AI assisted engineers are putting 5x more code, how are you going to do the reviews? And then subsequently, how are you going to do CI and CD and testing and instrumentation? So all of those become a bottleneck. So then what happens like you know, from from February till now, those are the kinds of things that we're fixing internally as in like how do we make sure that reviews are happening quickly? And so we have a system for uh auto reviews that you can turn on. Um then we have CI CD. So again like you know, one of the kind of like the bottlenecks that this is uh exposed is like our CI CD infrastructure. Uh we really had to rethink how we can like keep the pace going uh with support from the infrastructure. >> So maybe another thread we can pull on. We've talked a little bit about this idea that even though we have this 17x increase or whatever it is in AI engineering uh and you're throwing away a bunch, you're still seeing a lot more code get pushed for production into CICD. And now we're in a world where like continuous deployment is something we can really live with and do. What happens? What breaks down the chain with that? How do you think about that at scale? >> Yeah, in the last six months, you know, our engineers have gotten like so productive that they're actually generating so many more PRs and then our agents are pulling code on a regular basis, running tests and then pushing back to main. We have had several issues on the current infrastructure of like how we have code repositories and how we manage code repositories. We have a mono repo generally and the amount of code that goes in and out is just like I think like gone over an order of magnitude more than what this current system was designed to support. So much so we actually set up a a team internally to go solve this problem with fundamentally different assumptions. So you know, for example, Git was originally built for an offline use case. You know, you check out code and then you have all these branches locally and then when you're done, you push. And so that most of the concepts are built with like an offline development story, whereas now when we're thinking about agents and stuff, all of those are online all the time. And so when you when you make those kind of assumptions with like, you know, how we go build a new repository, you can actually build it for the new agentic world, which is like, you know, two orders of magnitude more capable and more with more throughput. And that's what we need. And so we have now a system that is internally built that is supporting our entire mono repo. All of our engineers are on top of that. And so this is the kind of like, you know, when when you start to notice these bottlenecks show up as a second order or third order you know, impact from like you know, reducing the time to code you do have to go solve those problems. >> You you absolutely do. And and I think I want to just think a little bit about the implication there because to me always on agents is one way to sort of change your assumption set, but I would also assume that there's other second order assumptions that you have to shift around. So for example, we've always been trained you have to have some kind of reconciliation of main so that main remains main. And yet if you have like a bench of agents continuously deploying, that becomes very difficult to do. I would think collisions in main start to become inevitable and how do you reconcile that and where do you place your gates and how do you think about that relative to production quality? >> Yeah, so that's definitely a problem, but that's not even the biggest problem as in like you know, because the actual transaction if you're not locking on the main, you can solve those problems with like maximum throughput. Um but more importantly, where these agents are checking out code, the throughput of that checkout is going to be a a big problem. So you have to like solve sparse checkout problem first. >> Oh, interesting. >> And there there needs to be like caches across the board where you're able to like pull from rather than like constantly hitting the main. >> Because you have traffic issues hitting main effectively. >> yeah. So there's all of that stuff. Yeah. So um so there's a lot more of like you know you know once you start to profile it, you kind of like find all these bottlenecks that you can go solve. >> And so basically like from and this is interesting. I think there's a meta principle here, but basically if you think about it as you had an internal tooling problem, it was a second and third order effect driven by your AI adoption internally. You sent a team with it sounds like a mission to solve the problem, but not a how to. Like no one knew how to solve the problem. >> Yes, that's always the case. >> You were just like go solve it, come back when you have a solution. >> Correct. Yep. And the team did a phenomenal job of like understanding. Part of it is like you know we have our internal engineers are our hardest customers. And so they're demanding. And so to be able to like you know keep existing stuff running while you're building a new thing and so like actually transpose those things you know you know one small transaction is like pretty hard. And that's the task. >> Yeah. No, it's not easy. And it's it's a characteristic of engineered systems is that when start to scale up and you have to transition a scaled solution to a scaled solution, it's combinatorially complex. >> It really [laughter] is. >> Okay. Uh I I I think I want to pull back. We talked about engineering a little bit. I want to talk a little bit about the growth side of things. I know you're responsible for the next billion and kind of how you think about that. Uh talk to us about that problem space. 1.2 billion so far, but like what does the next billion look like and and what are the ways you're thinking differently about that? >> Yeah. Um ChatGPT currently has 1.2 billion users. I'm really happy about that because 1.2 billion people have access to intelligence today um and are able to use it for you know, if I think about um having someone that you can just run things by and get a second opinion is such a powerful assist and so ChatGPT reaching 1.2 billion people is is a pretty phenomenal accomplishment. Now the crazy thing is that uh if you look at the interface for ChatGPT, it's a text box and a button. >> Yes. >> And it it's actually like surprising that we were able to reach 1.2 billion people with just that interface and that is a very I mean, obviously it's a very intuitive and um easy interface to get uh adoption, but the next billion is not going to be able to use that because you know, when we think about like where the next billion is going to come from, English is not going to be their most comfortable language. Typing is not going to be the most comfortable modality. So where we need to like really be building an application that caters and resonates with the next billion folks. Um and so I I just returned from India having you know, going to talk to a whole bunch of people and how they use ChatGPT. And in my mind, I'm like people really want voice. Voice modality is the next thing because you know, imagine if you speak a very different language and you you you can like type or understand English. So and then typing another language, especially Indic languages is very hard, right? The keyboard >> Script issues. Yeah. >> And so uh and you know, the folks over there even when they use WhatsApp with to to communicate between friends, they send voice messages. They don't actually type. And so we need to like really think about like how people use these products and what is the modality that we need to bring. And so that's what I'm thinking about and that's what my team in growth is thinking about. How do you go to the next one? >> Yeah. Maybe one of the pieces we haven't talked about is around uh how you as a leader in your leadership team give team strategic direction while enabling them to go really fast. >> From a leadership point of view, so one of the things that I used to be doing is like I I'm constantly thinking about all the different ways in which my teams could be like working on different products and I can connect the dots because I have some line of sight across multiple product teams. Um so instead of like now going to the team and saying here's an idea, let's go explore that. I'm able to do a lot of that with Codex by myself. Like you know, so when I talked about the voice modality and instead of just going to the team first with like hey, I have an idea, uh I think we should like start with voice modality as the first one um you know the default experience when people open up ChatGPT, actually went and built it. >> Okay. >> it was so easy for me like you know point to the model repo and say like look I want to like pair down the the application into just a very simple voice modality application and then when the the app opens up don't try you know while you're connecting in the background, actually open up the mic so that people can start speaking so that right away. So and then once the connection is made then replay that the the conversation that you've recorded. So I was able to prototype the whole thing and then like take that and first number one is like I I prototype a lot of stuff and then this is one of those where I felt like looks good. I want to take it to the team and so I took it to the team and say like can we build something like this? Now obviously that's just a prototype, right? So got completely it's a completely different set of problems in a different world. So I don't want to like trivialize any of that stuff. So then I was able to like you know first validate my idea, second actually validate that it's going to work and then take it to the team. You can kind of like already see that happening where um you no longer are just constrained by you know I just only have an idea. Now you can actually go and make it into something real. >> Yeah, and I've seen this in a couple of places where you have this phenomenon of leaders who were previously in a I must direct mode becoming ICs themselves and then kind of leaning into that side in order to provide value to the team. >> 100% it's become so accessible. Code and product building is become so accessible. Website building, you know [clears throat] you can make a point now with actual real products. >> I I and that's something that I have loved, right? As someone who got to build for a long time just seeing that democratize I feel like so often when I'm trying to express something I turn to myself and I say do I have to write this down or is this actually something I can show >> Yeah. >> by just building it. >> Oh yeah. >> And then we find out if it works or not. >> Yeah, no 100% you know back then we used to say code wins arguments. Now you can actually like do all of that. >> Yeah. >> Yeah. >> And and and it's not limited to the engineers. >> 100% When you're building something and you're relying on a model say imagine you're a founder so the startups are out there. I have this litmus test which is you know models are going to keep getting better and better. You know you're going to get like every yeah right [laughter] right every month you're going to have a new model that is like much more capable than the model before and we're talking like a year would pass by and so you know the the models are the the the smallest model that is available now was like 10 times more powerful than the biggest model that was there last year. So that's a safe bet. So in every time a model drops if you're worried about it then you're not building the right product because if you're worried that that model is going to take over the capabilities of like what you're building then you're not building the right product. If every time a model drops you're excited about it because then the capabilities of your product gets better and you're able to like actually show more value that means you've used the models in the right way. So that's where you know when I look at founders and I ask this this is your litmus question. >> And I love that as a litmus test. That's fantastic. >> Yeah. So when we started the ads team, so the ads team has been around for less than a year, about nine months, 10 months now. And they hit like a billion dollar ARR run rate milestone within just like seven months or eight months of like starting from zero code to a billion dollars. And the way they were able to do that is by leveraging, you know, a lot of these LLM capabilities because in this case, you know, you have from, you know, once you have ads demand, you have like ads indexer, you have the query, the query rewriter, and then you have to like get a list of all the candidates ads, and then you have to like run them through an auction. At the auction, you got to run them through a ranker. And then you have to be able to like, you know, send it back to the client to like display them. >> Performantly. >> Yes, exactly. All of that. And so if we were to like start by building an ML model for each one of them and a query rewriter for each one of them, it would have taken like much, much longer. And so this is where one of those things where the model, the model capabilities used in the right way, the team was able to move extremely fast with such efficiency. And then the cool part is like, you know, going back to the litmus test is like the model keeps getting better, which means our systems, the entire ads system keeps getting better. >> gets smarter for free. >> Yes, exactly. And so this is what I mean by like if you have built a system in such a way that you are getting the benefit of the model getting better, you've done it right. And so our ads team is it's actually really, really small. I mean, I would I would like, you know, guess about 50 or so people in the entire ads team, right? And that's how small the team is, and that's how capable they are with the right tools and the models. >> If you want to watch the whole interview, head on over to my Substack, links in the description below, and you're going to get the full deep dive that we did together, about 45 minute conversation. And if you want more interviews like this, you just hit subscribe here because we got more coming. I'll see you next time.
