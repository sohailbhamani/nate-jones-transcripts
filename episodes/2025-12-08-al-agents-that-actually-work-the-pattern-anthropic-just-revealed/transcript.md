---
title: "Al Agents That Actually Work: The Pattern Anthropic Just Revealed"
video_id: "xNcEgqzlPqs"
youtube_url: "https://www.youtube.com/watch?v=xNcEgqzlPqs"
publish_date: "2025-12-08"
duration: "13:36"
duration_seconds: 816
view_count: 89677
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI agents"
  - "AI strategy"
  - "large language models"
  - "prompt engineering"
  - "Claude"
  - "Anthropic"
  - "AI memory systems"
  - "agent harness design"
  - "AI for builders"
  - "automation at work"
  - "AI workflow automation"
  - "domain memory"
  - "agentic AI"
  - "AI architecture"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Anthropic"
    - "Meta"
    - "Slack"
    - "Twitter"
    - "X"
  people:
    []
  products:
    - "Claude"
    - "Gemini"
    - "Make"
    - "Opus"
    - "Artifacts"
  models:
    - "Opus 4.5"
    - "Gemini"
    - "Gemini 3"
concepts:
  []
summary:
  - "# Al Agents That Actually Work: The Pattern Anthropic Just Revealed

We're going to talk about agents and we're going to talk about memory"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "artifacts"
  - "claude"
  - "coding"
  - "frameworks"
  - "gemini"
  - "google"
  - "leadership"
  - "make"
  - "meta"
  - "opus"
  - "product-management"
  - "prompting"
  - "slack"
  - "twitter"
  - "x"
---

# Al Agents That Actually Work: The Pattern Anthropic Just Revealed

We're going to talk about agents and we're going to talk about memory. Anthropic dropped a piece of golden wisdom. I'm going to give you my takeaways as a builder of agents and we're going to get through it in five or six minutes and you're going to walk away knowing more than like 90% of people who talk about agents. Because honestly, most of the time when I see someone brag on Twitter about agents, it's immediately apparent that they don't know what they're talking about because they are talking about generalized agents. And if you've ever built a generalized agent, you know it tends to be an amnesiac walking around with a tool belt. It's basically a super forgetful little agent and you can give it a big goal and maybe it will do everything in one manic burst and fail or maybe it will wander around and make partial progress and tell you it succeeded. But neither one is satisfactory. Anthropic confronted that directly. I've confronted it. I want to tell you how it actually works. The key is moving from a generalized agent to domain memory as a stateful representation. I'm going to get into all of that. That sounds complicated, but it really isn't. Basically, you can start with a really strong coding model. Take Opus 4.5, take Gemini 3, take Chat GBT 5.1, what have you. And you can start with it inside a general purpose agent harness like the Claude agent SDK. There's other SDKs out there, too. And that will have context compaction. It will have tool sets. It will have planning and execution. And on paper, you would think, I have an agent. It has tools. It's in this harness. This should be enough to keep going. And we have found in practice it doesn't. No one is surprised anthropic is admitting it doesn't. No one who's building agents seriously thinks that it really works that way. Domain memory is the other side of the bridge. Domain memory is what we get to when we start to take agents seriously. Domain memory is not. We have a vector database and we go and get stuff out of the vector database. Instead, it's a persistent structured representation of the work. Remember I said stateful, it's serious about making sure the the agent is no longer an amnesiac that the agent no longer forgets. Remember how I said we talk about agents in memory? This is where the meat and potatoes of memory happens. So you have to have in a particular domain a persistent set of goals, an explicit future list, requirements, constraints. You have to have a state like what is passing? What is failing? What's been tried before? What broke? What was reverted? You have to have scaffolding. How do you run? How do you test? How do you extend the system? And this shows up in a variety of different ways. It can show up as a JSON blob, like a big coded list with a bunch of features and all of them could initially be marked failing and all the agent is doing is going back to that feature list in the JSON blob and it only gets to change something when it passes a unit test. It could look like a cloud progress text file where you log what each agent run did. The agent can go back and read that. These are not these sound obvious, don't they? I promise you, most of the people building general agents are not thinking with this degree of specificity. They aren't thinking of memory as a problem that you have to manage. Really, the story in that anthropic blog post that I want to give to you in just a couple minutes here is that the key to running agents for a long period of time is building a domain memory factory. So they've put together a two agent pattern, but it's not about personalities. It's not about roles. It's about who owns the memory. There's an initializer agent that expands the user prompt into a detailed feature list. Say it has structured JSON and like it talks about the features and just like I described, maybe all the features are initially failing because they haven't passed their unit tests. Maybe it will set up a progress log etc. It bootstraps domain memory from the user prompt and sets out best practice rules of engagement. You can think of it if you're not a technical person as if the initializer agent is setting the stage. It is a stage manager. It is building the stage and the coding agent is the actor in the setting. Every subsequent run, the coding agent comes in and it has no memory, just amnesiac. And by the way, if you think about it, the initializer agent didn't need memory to do what I just described. All it needed to do was to transform the prompt into a set of artifacts that acted as the scaffolding, the set, if you will, for the coding agent to come in and play its part. And so the coding agent reads progress. The coding agent gets the history of previous commits from Git. The coding agent reads the feature list and picks a single failing feature to work on for this run. It then implements it. It tests it end to end. It will update the feature status as either failed or passing. It writes a progress note. It commits to get and it disappears. It has no more memory. It's gone because long running memory just doesn't work with these LLMs. We are building a memory scaffold because these LLMs need a setting to play their part to strut upon the stage. To quote Shakespeare, the agent is now just a policy that transforms one consistent memory state into another. The magic is in the memory. The magic is in the harness. The magic is not in the personality layer. And and harness is a fancy word for all the stuff that goes around the agent, right? It's the setting. It's what I'm describing. So the deeper lesson is that if you don't have domain memory, agents can't be longunning in any meaningful sense. And that is what anthropic is discovering. Although we've all sort of known that, but at least they're writing it up. And I really appreciate it. The core long horizon failure mode was not the model is too dumb. It was every session starts with no grounded sense of where we are in the world. And what they are doing to solve that is not make the model smarter, right? What they're doing to solve that is give the model a sense of its lived context. Now we would say instantiate it. And that's why it's called an initializer agent. It initializes the state so that the coding agent on every subsequent run knows where it is. If you have no shared feature list, think about it. Every run will rederive its own definition of done. If you have no durable progress log, every run will guess what happened wrongly. If you have no stable test harness or test pass in what counts as a successful software application and what counts as a successful unit test or feature test, everyone will discover a different sense of what works. And this is why when you loop an LLM with tools, it will just give you an infinite sequence of disconnected interns. It's just not going to work. And by the way, if you think there are implications here for prompting, you would be correct. So much of what we do with prompting is being that initializer agent. We are setting the context. We are setting the structure so that you can set up a successful activity for the agent. So, so when the LLM wakes up, as you hit enter on the chat, it knows where it is and it knows what the task is. It's a wonderful way of thinking about prompting. prompting is setting the stage so the agent can play its part. So domain memory forces agents to behave like disciplined engineers instead of like autocomplete. And so once you have a harness like the one Anthropic is describing or the one so many other companies are building, every single coding session starts by actually checking where the agent is, right? Like it reads the previous commit logs, it reads the progress files, it reads the feature list, and it picks something to work on. This is exactly how good humans behave on a shared codebase. They orient, they test, they change. The harness insists or bakes that discipline right into the agent by tying its actions to persistent domain memory, not to whatever happens to be in the current context window. That means that generalization moves up a layer from general agent as a concept to general harness pattern with a domain specific memory schema which is really fancy wording but it's important wording because it means this is not just for coders. You can use the same pattern of having a setting a context an agent that can do its task in that context and you can apply that beyond coding. You can apply that for any workflow where you need an agent to use tools to get something done and you need it to effectively have long-term memory when it actually doesn't. So the anthropic work implicitly suggests an a framing of agents that feels much more honest than a lot of the Twitter hype. You can have a relatively general agent harness pattern. You can use an initializer. You can build the scaffolding. You can have a repeated worker that reads memory and makes small testable progress and updates memory. That by the way doesn't have to be code, right? But you can only have that if your schemas and your rituals are domain specific. And I think part of why this is working for code is that we have rituals and we have schemas that we've all worked out and agreed on and that makes it easier here. Right? If you are working in development, you understand that having tests get progress logs feature list.json JSON those all make a ton of sense. We have to invent some of those and align on some of those in less technical disciplines. So for research it might look like a hypothesis backlog, an experiment registry, an evidence log, a decision journal. For operations it could look like a runbook, an incident timeline, a ticket queue, an SLA. So generalized agents are really just a meta pattern, right? They instantiate the same harness structure, but you have to design the right domain memory objects to make them real in a particular space to make them operations agents or research agents. What I'm telling you is that the magic pattern for general purpose agents lies in being domainspecific about their context. So this kills the idea of just drop an agent on your company and it will work. That was always a fantasy, but I really think we have good evidence to drop it here. If you buy the domain memory argument, you can write off a bunch of vendor claims right away. Right? A universal agent for your enterprise with no opinionated schemas on work or testing is a function that's going to thrash and go into the trash. If you can plug a model into Slack and you can call it an agent, I guess you can do that. But most of the time that's going to lead to problems because they're going to not have any kind of clean context or schema or all of the good structure stuff I talked about to work. Well, that's different from saying, "I want to have an agent that has an API hook or web hook into Slack to send messages." By the way, that happens all the time. But if you're trying to just give your agent a generalized context dump and expect it to work, that's not going to go well. The hard work is going to be designing artifacts and processes that define memory for domainspecific tasks for agents. The JSONs, the logs, the test harnesses that are not necessarily just for coding but for other tasks and disciplines too. So if you were to look at this and pull design principles out from this whole conversation around agents, I would suggest a few for any serious agent that you build, you want to externalize the goal. turn do X into something that is a machine readable backlog, right? Something with past fail criteria. Get really specific. You want to make progress atomic. You want to make it observable. You want to force the agent to pick one item. You want to work on it and then update a shared state. So progress needs to be something you can test and increment. You want to enforce the practice of leaving your campsite cleaner than you found it, right? You want to end every run with a clean test passing state with human and machine readable documentation. You want to standardize your bootup ritual, right? On every run, the agent must regground with the same exact protocol. Read the memory. Run basic checks. Then and only then do you act. You want to keep your tests close to memory. Right? Treat passes false and true as the source of truth for whether the domain is in a good state. In other words, if you are not tying in test results to memory, you're going to be in trouble. The strategic implication here, by the way, is that the moat isn't a smarter AI agent, which most people think it is, the mode is actually your domain, memory, and your harness that you have put together. It's a lot of work, right? Models will get better and models will be interchangeable. What won't be commoditized as quickly are the schemas that you define for your work, the harnesses that turn your LLM calls into durable progress, the testing loops that keep your agents honest. In a sense, the generalized agents fantasy is hiding from everyone a nice clean reusable harness pattern that we can use to build competitive differentiation with well-designed domain memory. We actually have a chance now to design really useful agents. And the whole purpose of this video has been to take the mystery out of it. The mystery of agents is memory. And this is how you solve
