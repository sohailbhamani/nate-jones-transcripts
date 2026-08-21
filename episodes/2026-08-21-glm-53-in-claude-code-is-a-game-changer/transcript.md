---
title: "GLM 5.3 in Claude Code Is A Game Changer!"
video_id: "4HvFqhtCb-A"
youtube_url: "https://www.youtube.com/watch?v=4HvFqhtCb-A"
publish_date: "2026-08-21"
duration: "20:49"
duration_seconds: 1249
view_count: 5571
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  GLM-5.3 runs inside Claude Code and Codex, and the setup takes a few lines. Here is how to add a cheaper AI coding model to the tools you already use without rebuilding your harness.
  
  Grab the guide here:
  https://unlock-ai.natebjones.com/guides/glm-53-in-claude-code-and-codex?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  Full Post:
  https://natesnewsletter.substack.com/p/glm-5-3-claude-code-codex?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening with cheaper models inside Claude Code and Codex?
  
  The common story is that a cheaper model means a cheaper bill, but the real question is what the work costs once you count retries, review, and the context you had to rebuild.
  
  In this video, I share the inside scoop on running GLM-5.3 inside the coding tools you already use:
  
  - Why the harness matters more than the model underneath it
  - How to launch GLM-5.3 inside Claude Code and Codex
  - What carries across a model switch and what does not
  - Where the cheap model earns the work and where it loses
  
  A cheaper model is a real lever, but only after you measure what the result you actually accepted cost you.
  
  Chapters:
  00:00 The $200 problem and the $18 alternative
  01:04 What you keep when you change models
  02:45 Model, harness, project context, conversation
  04:29 Why a late model switch costs more
  06:19 What 96% reused input taught me
  07:09 The Claude Code launcher
  09:15 The six-line handoff
  10:11 Subagents, forks, and two sessions
  12:09 Adding GLM-5.3 to Codex
  14:04 Which jobs belong to the cheap model
  16:13 Plan limits and whether it is actually cheaper
  17:54 Unbundling and the companion guide
  
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
  - "GLM-5.3"
  - "Claude Code"
  - "OpenAI Codex"
  - "Z.AI"
  - "GLM coding plan"
  - "AI coding tools"
  - "cheaper AI coding model"
  - "AI coding costs"
  - "claude code"
  - "z.ai"
  - "saving token"
  - "ai tools"


# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Tools"
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
    - "X"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Codex"
    - "Make"
    - "MCP"
    - "Sonnet"
    - "Projects"
  models:
    []
concepts:
  []
summary:
  - "Five different AI subscriptions, two of them alone can run you 400 bucks a month"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "claude-code"
  - "codex"
  - "coding"
  - "frameworks"
  - "make"
  - "mcp"
  - "meta"
  - "openai"
  - "projects"
  - "sonnet"
  - "tutorials"
  - "x"
---

# GLM 5.3 in Claude Code Is A Game Changer!

We are all guilty of this one. Five different AI subscriptions, two of them alone can run you 400 bucks a month. And now, in the middle of all that, say it's 2:00 in the afternoon, regular day, you hit your limit on one of these. If you get Codex Pro, if you get Claude's top max plan, they're going to cost you $200 a month. Z.ai's GLM coding plan, on the other hand, starts at $18 a month and officially works inside both tools, which most people don't realize. GLM 5.3 can take even some of your coding work off the shoulders of Codex or Claude. The savings can be huge. You've used the API, you know the API costs add up real, real fast. That $18 model can run inside the tool you already know. And the setup just takes a few lines, and I'm going to walk you through it in this video. So, if that's you, if you want to try GLM 5.3 and you don't want to switch out your harness, this is the video for you. I'm going to show you all about it, tell you how to do it in each of them, tell you the trade-offs with Claude and Codex, and I'm relying entirely on both Claude and Codex documentation and also Z.ai documentation, the parent for GLM 5.3. So, let's jump into it. You can keep your files and your instructions and tools and permissions and hooks and habits, all of it that you already built, intact. All you do is change which company supplies the model for the piece of work that you're doing. Put yourself in the obvious situation. It's 2:00 in the afternoon, you're halfway through a real project, and you hit your Claude or Codex limit. Hi, it's me, I've done that. The job still needs to ship, but you don't want to pay more, pay the API pricing, which is way higher than your monthly bill, or spend the rest of the afternoon rebuilding everything in a strange new coding tool. So, you're kind of stuck. The real question is which work you move, what context comes with you, and whether running a cheaper model is still going to save you money once you validate the retries, once you do review, once once you actually get the fully loaded cost. So, this video gives you that answer for both Claude code and for Codex. I'm going to show you the setup, what follows you when you set up a new model, what doesn't, and the different way I would use GLM as a worker in each of those two tools. And then, we're going to sort through four real kinds of coding work and figure out what goes in the cheaper model queue and what do you save for your stronger model queue and why? And then start to measure what each coding result is actually going to cost you when you start to mix in that cheaper model and do it smart. So, stick with me. The $18 plan has smaller limits than the $200 plan. So, this is not saying that one subscription from z.ai just magically replaces a subscription to Codex or Claude. That's not what I'm proposing. That's not the way most people use it. The opportunity here is to stop paying the most expensive model to do every job merely because it came bundled with your coding tool. There are four things people keep mixing together here and I want to separate them out because I think they're often misunderstood. The first is the model. This might be Claude. It might be an OpenAI model. Or in this case, it might be GLM 5.3. It's the part that does the reasoning and produces the response in tokens. The second is, of course, the coding tool. It's often called a harness. Claude code and Codex are programs you operate that are harnesses. They let the model read files in a particular way, run commands, use tools, ask for permission, make changes, and show you the result, what happens. I often call this surrounding environment a harness because it helps you to understand how a model interacts with the setup or the arrangement. And you can think of it as you put your horse in the harness and it toes the cart, right? It's a visual metaphor, too. The third concept is your project context. And these are things you have written down. So, it might be your Claude.markdown file or your agents.markdown file. It might be your tasks, your documentation, your skills, your scripts, your hooks, your project rules. Another session can read those things again just because they live in files, right? They can be read by anything anywhere. They're very portable. And the fourth concept is conversation, right? That's the easiest to understand. It's the temporary history of your particular session, what you asked, what the model read, the decisions you made together, and the corrections you gave it along the way. Changing the model does not mean all four of those things change in exactly the same way. I really want to underline that three times cuz it gets misunderstood. And this distinction is why I've warned people that sometimes cheaper models can be more expensive. You have to look at the fully loaded cost across all of these four modalities to figure out what actually works. Flo Crivello's team at Lindy had moved off of Claude. It ended up rebuilding the harness around the work they actually did so they could take advantage of an open-source model. The lesson here is that you want to look at the whole system when you're making changes. So, let's talk about Claude Code. If you use Claude Code {slash} model command to choose another model inside the current provider, Claude Code keeps the conversation. You don't have to paste the whole thing again. But Anthropic warns that the next response will reread the whole conversation history without the old prompt caches, essentially loading up fresh in the background. And that can make a late switch to a new model slower and much more expensive than people expect, even if the overall model is cheaper. So, moving from Anthropic to Z.ai can be a bigger change, relatively speaking, because you're also changing effectively the internet address, the key Claude Code uses for model requests. There's a lot that's going on under the surface there. So, I would say the practical way to switch models if you're in Claude Code is simply to launch a separate GLM-specific session. It can open the same project. It can reload instructions you saved in files. All of that works, right? It doesn't automatically then inherit the mature conversation from the Anthropic session that you already had open. And so, this gives us maybe our first useful rule of thumb. Start a substantial job on the model that you expect to finish it. Don't build 40 turns of working history with a model with a single provider and then casually move that job to another provider in the final mile. This doesn't mean that you can never use two models on one project. If you're stuck, maybe it's worth jumping over because you've hit your limit. It just means that the boundary between them should be a really clear piece of work and not just sort of a hope that the second model will walk into the conversation magically know everything that the first one learned. The work that I did on token saver made this distinction very real for me, right? I had a tracker. I had, you know, days where I was passing 3 billion, 4 billion tokens across Codex threads and Claude threads. Um and almost 96% of volume, as I shared, was reused input. And so in that world, you have to assume that the calls are carrying project instructions and tool definitions and file context and history and other repeated material. If those important work lessons from your projects exist in only one long conversation thread, they're going to be difficult to move to a new model. On the other hand, if the coding standards and test commands and permissions and definition of done live in files, another model can pick them up very easily. In other words, good hygiene here, context hygiene, makes a lot of economic sense. So, staying with Claude code, I would keep my normal Claude setup exactly as it is. I would create a second private launch command called something obvious like Claude-GLN. That command supplies three things before Claude code opens. The z.ai API key, the z.ai address for Anthropic compatible requests, and the names that map Claude's model choices to GLN 5.3. Keep the API key, obviously, in your own environment or a secret manager. Don't put it in the project. I keep saying that. And leave the normal Claude settings alone. Ordinary Claude will still open an Anthropic session, while Claude GLM will open a z.ai session. If the GLM connection behaves badly, just close it down and go back to the normal command. If this all sounds like Greek to you, I've put the copy and paste command in the companion guide to this piece over on Substack, because we should not be trying to transcribe environment variables, and we should not be playing those kinds of games. So, if you have any doubt about whether you can do that, stick with a secure, safe command, and don't try and handle API secrets yourself on your own. Okay, what happens after the command runs? You want to open the same repository, and Claude code will see the same files, it will read the same Claude.markdown, and it will keep the hooks and the MCP servers, the tools, the permissions experience that you've already configured. All the stuff that goes into your Claude harness. The model answering underneath will now be GLM 5.3. And what comes back is the project context that you saved in files. Now, what won't come back is any old Anthropic conversation you had, any old prompt cache, or decision that you never wrote anywhere outside the chat. Well, that's gone, right? Suppose your Anthropic session spent an hour investigating a bug, right? It ruled out three causes, it learned that one log line is misleading, it agreed not to touch the authentication middleware you have. Those are all decisions, right? If none of that got logged into a file, a fresh session with a new model like GLM 5.3, it's just not going to know about it. And so, you're going to start from scratch. So, before moving a job over, if you have to move a job in the middle, create a handoff file. Insist that the current model document goal, current state, relevant files, constraints, what done means, and the checks to run. And yes, I have a template for that in the Substack guide, as well. So, for example, update these 38 API calls to the new field name. That might be your goal. The current branch is clean and the affected calls are in these two folders. That might be where the current state is. Don't change the public API as a constraint, and the job is done when the old field no longer appears anywhere in the existing tests all pass. And then it will say, "Run X commands before returning to work." Like these are commands that we're in the middle of. That is enough context to get a new model going. It's also much better than pasting an entire conversation history and asking GLM 5.3 or any new model to discover which parts matter along the way. And now we get to Claude Code's multi-agent question. Claude Code already uses and has sub-agents, right? But a normal sub-agent starts with fresh context. It receives the task that Claude delegates and applicable project instructions, not a complete parent conversation or every file the parent has read. And that's on purpose, right? It gives the agent bounded context. And that's one reason sub-agents are really good at specific narrow work. They can keep their logs and research and side investigations outside the main conversation. So, Claude Code also has the concept of forked sub-agents, and that's a different concept. A fork does receive the full conversation and can reuse the parent's prompt cache. The trade-off is that the fork must use the same model as the parent. That leaves a real limitation for this specific setup. Claude Code documents how a sub-agent chooses a model, but it does not document a separate provider address for one sub-agent. If the main Claude Code process is using Anthropic, there's not a simple native setting that says, "Keep Anthropic in charge, but send this one child to that with a gateway or a custom integration, but I would not make that a recommendation for beginners. Instead, I would open up two Claude Code sessions and ordinary Claude is the lead and Claude GLM as the worker. Give the GLM session that six-line handoff I talked about if both sessions will edit at the same time, put the worker in a Git work tree. All that is by the way is a separate copy of the repository. It prevents both agents from changing the same files under each other. And the GLM session just returns changed files and checks that it ran and anything it can't resolve, it goes and fixes. The Anthropic session will review the result when the job is consequential. And it's still one project and it's still one familiar tool. It's just two sessions with a very explicit handoff between them. Okay. Now let's tackle Codex because Codex gives us a different option. The first Codex setup looks a lot like Claude Code. You add z.ai as a model provider in your personal Codex configuration. In plain language, you give Codex the z.ai address and tell it which environment variable contains the key. z.ai provides a responses compatible address specifically for Codex and you create a GLM profile that says two things. Use GLM 5.3 and send the request through that provider. When you want an entire Codex job to run on GLM, you just say, "Hey, launch Codex profile GLM." And ordinary Codex will still use your normal OpenAI setup. So you can run both at once. This is similar to how we configured Anthropic, right? The GLM profile opens the same project, loads the same applicable agents.markdown files, skills, tools, project rules, all the things you're familiar with. And as with Claude Code, you want to treat it as a new job or a carefully handed off job. So the project context will reload. A separate conversation does not magically appear. Now, why does all of this matter? Let's go back to imagining a small software company. What are they doing? They have a technical founder, a senior engineer, a backlog that grows faster than the team because they've got customers with bugs and they've spent months getting Claude Coder Codex to understand their repository. And they have a bunch of jobs that they have to work on and they have token bills. This is the startup that I've had in mind as I've given you examples through this video. So we've talked about the agent having to update 38 calls to a renamed API field. Very plausible startup job. We've talked about the idea that there might be an intermittent authentication failure. That these are jobs that I've referred to through this video. So we've talked about the idea that the agent might have to update API calls, right? There's lots of other jobs like that that startup technical teams have to address like intermittent authentication failures. These are not glamorous things, right? When you are looking for how to farm out this work, I want you to think about it as where do you have clear definition of done, where do you have a repository that contains examples, and where do you have really good tests that can tell you whether the work is acceptable. In those situations, I would start to use whatever harness you're running, whether you're Claude or Codex, and I would start to assign that work out to GLM because it's work that I feel really good about GLM attacking and getting right. It's not too vague, it's not too generalizable. GLM's going to be able to go after it and you're going to be able to save a fair bit on tokens. If you're doing something fairly complex where you're root causing something like that authentication failure I talked about, that could be different because it has hidden state, it may have conflicting evidence as you dig again. A cheap worker might still help gather logs or trace code paths, but I would keep the main investigation with the strongest model I could trust. You see how you need your human judgment to think this through. In a sense, you are figuring out which model inside the harness makes sense to use in which situation. And I want to give you kind of some rules of thumb so you have that. So you'll use GLM when the job has a clear target, it has really clear permissions, and it has a a test objective that you can define really specifically. And you'll keep the smarter model in charge when the hard part is deciding what the job should be at all or resolving hidden state or investigating or weighing a risky trade-off. How difficult it is to hand off work midstream. If you have to pull an entire transcript from the parent conversation, the job is probably too unbounded to handle giving to a model like GLM. And that's also why I would not switch models repeatedly inside a conversation. Be intentional, right? A tool may keep visible history that you can read, but you also have to factor in stuff you can't read like model behavior change over the course of the conversation, prompt caching, etc. So, a new provider has to figure all of that out and that can add cost, that can add uncertainty, that can add more turns. All of that has to be factored in when you're figuring out where to apply these models. The other thing to figure out is whether the work actually is cheaper with an alternate model. The plans are not equivalent. As I called out, Z.ai has both 5-hour and weekly credit limits and the $18 tier is not the same token count or same problem-solving ability as the $200 plan. And so, you want to be thinking about in your particular instance, for your codebase, for your tasks, does this model make sense? And I wish I could sit there next to you and say, "This makes sense, this doesn't." But the reality is right now, you are the one that needs to figure that out for your tasks, your files, your code, and there's no substitute for actually testing. The best I can do is give you a rule of thumb, give you very clear instructions for how to set it up, and remind you always test on your own code because your code has its own level of complexity, and you need to make sure you're trueing up that level of complexity to the model itself. And don't be under ambitious. I don't want you to hear this and say, "Oh, I won't give it tough tasks." I would be really intentional about it. I would look and say, "Let's give it a couple of ambitious tasks in my code base. Let's see how it does. And let's back off as we see failure and see where the true up level for this particular model is. And by the way, that's also something you can use on less frontier versions of existing models from OpenAI and from Claude. So, if you want to use a Sonnet model, if you want to use the Terra or the Luna models, that's the same principle. You want to give them stuff they can tackle, see how complex they can go, and then back them off as you need to. This is going to ultimately give you your maximum token savings without costing you on intelligence capabilities. You know, when I step back here, I've spent a long, long time, years and years building products all the way from, you know, at the 100 million person and more scale down to tiny startups. And I think what's interesting about this moment is that for so long software companies have made bundles feel inevitable. The interface, the workflow, the underlying service all arrive bundled, and you can't pry them apart. And over time you stop asking whether they have to come from different companies cuz you just trained. And I think one of the things I really appreciate about both the Claude team and the Codex team is that both of them feel like they are committing to being willing to unbundle. And I think that that's a strong mark in favor of both teams. Claude code often feels like a cockpit right now where I have to stay close to the work and I steer it and I change direction as the problem becomes clear. Codex can feel more like kind of an ops desk, right? I can dispatch jobs, I can let them run, I can expect inspect what comes back, and I kind of see where I'm at. Those work styles don't disappear because another company supplies some of the intelligence, because the they're kind of endogenous to the harness. They fit with the harness. I can keep Claude code, and I can keep working with it the way I always do, and I'm just steering a GLM session along the way. And so, unbundling allows us to see the importance of the harness in the way we work. So, wrapping up here, I've put the Claude launcher, the Codex profile, the handoff templates, the comparison scorecards all in the companion guide on Substack. You can get them if you want to get started with a cheaper model inside your Codex or your Claude and save big. That's where you can go to get started. Those are much easier to copy from a page than a video, so I would go there if you want to do that. Listen, start with a piece of work that you care about. Figure out what you can challenge a model with that you haven't tried before with a with a subsidiary model or a new kind of open-source model and give it a shot. This is I I've given you how you can figure it. Now you have to have the boldness to actually go out there and try something interesting. And when you see failure, just kind of back off it a little bit. My rule of thumb is I find that bounded tasks that have clear descriptions of done tend to work better. Your mileage may vary because your your code complexity may vary. So, you have to look at that on your own. Best of luck to you. Go grab those companion guides and I will see you next time. And let me know what you are building with your multi-agent setups. What are you building with GLM 5.3? Which harness are you choosing for it? Are you choosing the native z.ai harness? Are you choosing Codex? Are you choosing Claude code? I'd be curious to hear where people come down on that and then how much money are you saving? You saving 200 bucks? Are you saving Cuz let me tell you, if you've used the API, you know the API costs add up real real fast. So, if this is going to save you API costs, it's going to save you big money. All right. Let me know what you build and let's get to it.
