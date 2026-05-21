---
title: "Your Apps Don't Need an API Anymore. Codex Just Proved It."
video_id: "2d9ZmA-4QzU"
youtube_url: "https://www.youtube.com/watch?v=2d9ZmA-4QzU"
publish_date: "2026-04-23"
duration: "21:00"
duration_seconds: 1260
view_count: 190772
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Full Story w/ Prompt Kit: https://natesnewsletter.substack.com/p/grab-the-workflow-audit-that-tells?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  ___________________
  What's really happening inside OpenAI's Codex revamp when they shipped a desktop agent that can drive any Mac app in the background while you do other work?
  
  The common story is that this is a coding tool update — but the reality is that Codex shifted categories entirely, and the gap to Claude's computer use is wider than I expected after running them side by side for a week.
  
  In this video, I share the inside scoop on what OpenAI is really building and why it looks so different from Anthropic:
  
   • Why Codex finishes in two minutes what takes Claude five or six with fumbles and retries
   • How the Workflow-to-Shortcuts-to-Sky team made background agents actually usable
   • What Chronicle tells you about training signal for computer use
   • Where Conway fits into Anthropic's bet that the ecosystem will cooperate
  
  Leaders who keep waiting for vendors to ship agent-ready interfaces are missing that Codex doesn't need the software industry to build for agents — the body just uses whatever's already there.
  
  Chapters
  00:00 Codex is no longer really a coding tool
  02:30 The brain is built, the work is on the body
  04:30 Computer use side by side: Codex vs Claude
  06:30 GPT 5.4 benchmarks above human baseline on GUI control
  08:30 Deep OS-level wizardry and parallel background agents
  10:30 Anthropic's body vs OpenAI's body
  13:00 The Workflow to Shortcuts to Sky acquisition
  15:00 Chronicle and the training signal for computer use
  17:00 Conway: Anthropic's event-driven agent environment
  19:00 What to watch: MCP adoption velocity
  20:30 If software has a screen, an agent can drive it
  
  Subscribe for daily AI strategy and news.
  For deeper playbooks and analysis: https://natesnewsletter.substack.com/
  
  Listen to this video as a podcast.
  - Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  - Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "AI strategy"
  - "OpenAI"
  - "computer use"
  - "Claude"
  - "Anthropic"
  - "desktop agents"
  - "GPT 5.4"
  - "Chronicle"
  - "Conway"
  - "MCP"
  - "enterprise automation"
  - "AI agents"
  - "legacy software"
  - "agentic AI"
  - "AI strategy for teams"
  - "ai"
  - "artificial intelligence"
  - "ai agents"
  - "codex"


# AI-enriched metadata
content_type: "Framework"
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
    - "Apple"
    - "Salesforce"
    - "Notion"
    - "Slack"
    - "Box"
    - "Cursor"
    - "X"
  people:
    - "Greg Brockman"
  products:
    - "Claude"
    - "Claude Code"
    - "Cursor"
    - "Codex"
    - "Sora"
    - "Shortcuts"
    - "MCP"
    - "Opus"
    - "Atlas"
    - "Computer Use"
  models:
    - "SAM"
concepts:
  []
summary:
  - "OpenAI revamped Codeex completely and I am blown away by how useful that new app is"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "apple"
  - "atlas"
  - "box"
  - "career"
  - "claude"
  - "claude-code"
  - "codex"
  - "coding"
  - "computer-use"
  - "cursor"
  - "frameworks"
  - "mcp"
  - "notion"
  - "openai"
  - "opus"
  - "product-management"
  - "prompting"
  - "salesforce"
  - "shortcuts"
  - "slack"
  - "sora"
  - "tutorials"
  - "workflows"
  - "x"
---

# Your Apps Don't Need an API Anymore. Codex Just Proved It.

OpenAI revamped Codeex completely and I am blown away by how useful that new app is. On April 16th, OpenAI turned Codeex into a desktop agent that operates every single app on your Mac. Clicking, typing, running in the background while you work. It's faster and more reliable than Claw's version of computer use, and it's by a much bigger margin than I expected. That matters because most enterprise software doesn't have modern APIs, and Codeex doesn't need them. I'm going to walk you through what Codeex is now, how it got this good, what OpenAI is really building, and where both labs are going, and of course, what you should do about it. The reason to pay attention goes deeper than the capability gap. In a recent interview with Ashley Vance, Greg Brockman said, "Models have gone from being the product to being part of the product." I think he's correct. The brain is effectively built. The work now from the hyperscalers is on the body. Both labs have decided the body is priority one, but they're building very different approaches. And Codex's April release shows that split really cleanly. Let me start with what Codex is now. When OpenAI launched the original Codeex command line in April 2025, it was a command line tool for developers. You typed prompts. It wrote code. That was essentially the whole product. A year later, Codeex has become a full desktop application that can see your screen, click and type across the Mac, generate images, browse the web in its own built-in browser, remember what you've been working on, schedule itself to wake up on longunning tasks, and run multiple agents in parallel without hijacking what you're doing. The transformation has happened in stages, but you can see the direction. February 2, the Mac OS desktop app launched. March 4, Windows support. March 5, GPT 5.4 for folded C codeex's coding capability into the general purpose model line. In March 19, OpenAI confirmed the super app consolidation plan. April 16, the release that made Codex what it is now was all about computer use, inapp browser, image generation, memory, and 90 plus new plugins in one app. The heart of that transformation is computer use. Codex can operate any Mac OS application by just seeing your screen and just clicking and typing like a person. It does this in the background, which means multiple agents can run in parallel while you work on something else. That's not a feature update. That's actually codec shifting the category. Codeex is no longer really a coding tool. It's a desktop agent that can do anything a person can do through a graphical interface. And yes, it still codes too. Does it actually work? Yes, and in two specific ways that matter. I've been running Codeex and Claude side by side on the same workflows for the last week or so. And what I see is this. Codeex is fast. It moves through a workflow at something close to the speed of a person who already knows that software. Claude's version is slower, like the cursor hesitates, the agent rethinks and sometimes retries. Tasks that finish in 2 minutes on Codeex can take five or six on Claude. And Claude is limited in where it can go. Claude prefers Chrome. Codeex can touch anything on the desktop. So, the gap isn't subtle. Codeex is also reliable. The failure mode of computer use products for the last year plus has been really specific. The agent gets partway through the task, hits an unexpected modal dialogue or some other issue, fumbles, and you have to take over and restart, and then why do it at all? Codeex's implementation, generally speaking, doesn't fumble. It backs up when it needs to. It finishes, and it does so quickly. That's what moves the capability from impressive for demos to, I could actually use this. Sam said something in a recent Ashley Vance interview that lines up with what I've been seeing. Asked about Codeex versus Claude today, his read was, "Our product is ahead in many ways." Of course, he said that. But on computer use specifically, I do agree with him. Some of that gap comes from the model. GPT 5.4 is the first general purpose model OpenAI has shipped with native computer use capabilities baked in. It benchmarks in the mid70s on OS World, which puts it above the human baseline for graphical user interface control. That's right, better than humans. But the model isn't the whole story. Alexander Emiricos who works on the codeex team at OpenAI called the background computer use implementation basically deep OS level wizardry. I feel it when I use it. The specific architectural choice he was pointing at is that background agents don't hijack your cursor or steal focus from the app you're working in. You can keep typing in one window while an agent is clicking around in another. That's what makes parallel agents actually usable instead of theoretical. Three codeex agents on three unrelated tasks. You can walk away. You can come back 20 minutes later. The three tasks are just done. And that's changed how I schedule my day. It's not just me. Since the release, early users on X have been posting their first real workflows with Codeex. And the range of what's working is wider than I would have expected. Stuff like mass clearing Slack, right? Reading and triaging hundreds of unread bot messages and daily digest so the inbox starts clean. Or building a Spotify playlist by driving the desktop app from a verbal description. Or walking through a front-end app to catch visual regressions while the developer keeps shipping the next feature. or reproducing a browser bug, screenshotting the reproduction, pasting the images straight into a pull request description, or running end-to-end tests on the app you just built, and then self-fixing the issues it finds, or driving a legacy internal dashboard that never had an API, exactly the software category automation has given up on for years. One person wired up a daily recap that pulls get commits, issue tracker updates, and calendar events, writes the meeting minutes to notion, and then drops prioritized to-dos into Apple reminders. Another one has Codex play daily login routines in the background so they don't have to. Another detects when the user is slouching on their webcam and pops open a stretching video. None of those are demos. They're actually workflows people ran and then decided to keep running. And that's the tell. Computer use stops being a novelty when you reach for it the second time. And that's really the line codeex crossed. A desktop agent that can drive any Mac app runs in the background and actually finishes the work is the dream. Which brings us to the next piece. What is OpenAI really building with this launch? And why does it look so different from what Enthropic is doing? Enthropic pivoted out of the coding box first. In January, they shipped co-work inside the existing clawed desktop app. Co-work is claude code for people who don't write code. You point the agent at a folder on your Mac, describe what you want done, and it does multi-step knowledge work for you. From there, it was compound moves, right? adding plugins, scheduled tasks, computer use, and research preview on Mac. And then on Windows, dispatch that lets you assign tasks from your phone. And by April, the Claw Desktop app holds three modes on one surface, right? It has chat for discussion, co-work knowledge work, and code for software, plus a plug-in layer for specialized capabilities like claw design. Both labs made the same high-level move. Both got out of the coding box. Both built desktop apps, but they did not move in the same direction. Anthropic pivoted toward knowledge work toward synthesis, research, writing, analysis, the kind of work where you define an outcome and the agent does the intellectual labor. Open AI pivoted towards something broader. Sam Alman admitted in the Vance interview that OpenAI started the year behind Anthropic on real world coding data. He gave Anthropic real credit for being earlier and said OpenAI only appreciated the gap in hindsight. But when OpenAI made their move, they moved wider. In the same interview, Brockman described OpenAI strategic vectors, the Agentic platform, computer work specifically, and personal AGI that does things for you in the real world. And he drew a line between knowledge work and computer work. Computer work is broader. It's anything that happens on a computer, whether or not it requires deep knowledge. Ops work, creative work, research, automation. Knowledge work sits inside that surface, but the surface is actually bigger. That aperture difference maps directly to the mechanism each lab chose. If the model is the brain and the work is the body, what is the body made of is the question here. For Enthropic, it's structured interfaces, file operations and co-work, MCPU servers, connectors, the 30,000 plus integrations already in the cloud ecosystem. And Conway, the always on agent environment that leaked in early April with its own sidebar UI, its own extension format, web hook triggers, browser control, etc. All of that is excellent architecture. It really is. But it also depends on the ecosystem cooperating. Every MCP server has to be built by someone. Every connector has to be maintained. Every web hook has to be configured. How far the body can reach depends entirely on how fast the world ships agent ready interfaces. Open AAI is building a different kind of body. OpenAI's body is computer use. The agent drives the same graphical interface that you drive. And that changes the math completely because the body's reach is now bounded by how much software has a graphical interface which is effectively all of it. Legacy enterprise software works. Internal tools works. SAS that will never build an MCP server works. The vendor portal your ops team tolerates works. The app your company built in 2019 and never touched again works. Open AAI doesn't need the software industry to build for agents. The body just uses whatever is already there. The two products look similar on a feature matrix, but the bodies underneath the way the agents are hooked into harnesses. It's not the same. And you can see this in how the two apps are shaped. Anthropics Claude app is built like a tool that assumes you know the work you're in. Every mode has a scope permission model and when you open co-work it asks you to point at a folder before it does anything. That friction is the product choice. It communicates what's about to happen so you can be deliberate. The whole app is explicit in the way the rest of anthropic strategy is. Explicit scopes, explicit permissions, explicit interfaces. OpenAI's codeex app is the opposite. It's built like a tool that assumes you don't want to think about modes. You describe the outcome. The agent decides whether to open files, whether to drive a graphical user interface, run a plugin, browse the web, or write code. Computer use is the escape hatch when nothing else works. Plugins are opinionated bundles invoked without explicit selection. Memory keeps context flowing between tasks, and the app is implicit in the same way the rest of codeex is. The agent figures out what to do because you shouldn't have to tell it which interface to use. That's what OpenAI is actually building. A body that doesn't need the world to cooperate. A product that doesn't ask you to think in modes. A road map where the model is the input and the body is the whole product. Which leaves the question, how did Codeex get here? Codex's computer use didn't come from nowhere. It came from a team OpenAI bought 6 months before the April release. In October 2025, OpenAI acquired a 12person company called Software Applications Incorporated. The company was the team behind Sky, an unreleased Mac OS native AI interface that was doing essentially what Codex's computer use does now. All 12 members joined OpenAI. One of the co-founders, Ariestein, is now a designer at OpenAI. And when Codeex shipped, he publicly credited his team by name for the cursor motion work. The specific detail that makes background computer use feel like a co-work instead of malware. What makes this team one of one? Weinstein and his co-founder Conrad Kramer previously built Workflow, the iOS automation app Apple acquired in 2017 and turned into Shortcuts. Shortcuts is now the system level automation layer across iOS, iPad OS, and Mac OS. Skye's third co-founder, Kim Bever, spent 10 years at Apple as a senior program manager working on Safari WebKit Privacy Messages Mail Phone, FaceTime, and SharePlay. That's a decade plus build of exactly the skill set that makes Codeex's computer use work the way it does. deep Mac OS integration, accessibility and screen recording, permission handling, motion paths that don't feel robotic, the kind of OS level work that takes years of Apple experience to do well. The line from workflow to shortcuts to sky to codecs, it only exists in one place with this team. OpenAI paid for it and the payoff is in the April 16 release. The deep OS level wizardry embaros described that's not a metaphor. It's a specific team's specific accumulated knowledge now applied to a product where it matters commercially. The same pattern shows up elsewhere. Anthropic Recept acquisition earlier this year, the team that shipped Claude's Windows desktop control within 4 weeks of joining. It's a parallel move on their side. Then there's IO Johnny Ives hardware startup OpenAI bought for several billion dollars, which is the larger version of the same thing. The labs are essentially spending on narrow, hard to replicate human expertise, not for the intellectual property, often not for the product, for the team. That's a consistent pattern. Models are starting to converge. Capabilities that used to take 2 years can now be replicated in 6 months or less. What isn't being commoditized is a specific team with a specific history. Those teams are a very scarce resource in the valley right now. If you're watching the lab-to-lab competition, the acquisition pattern is telling you as much about where advantage will live as benchmark scores might. So, we know what Codeex is. We know what OpenAI is really building and we know how Codeex got this good. The last big question is this. Where are both labs going from here? Both labs are converging on the same destination. an agent that's persistent, ambient, event driven, and works across all of your surfaces, and that does things on your behalf without you prompting it every time. The two clearest signals of how each lab plans to get there are Chronicle and Conway. Chronicle is OpenAI's latest step. They shipped it on April 20th, 4 days after the main release, as a research preview for Chat GPT Pro users on Mac OS. Chronicle captures your screen periodically and processes the images on OpenAI servers and writes local markdown memory files that Codex pulls into future sessions as context. Tibo, who heads Codex, called it early and token hungry, but said it had changed how he and many people at OpenAI work. Altman described it as telepathy like what's Chronicle actually doing here? The shallow read is that it's an ambient memory feature. The deeper read is that it's the training signal for computer use. If your agent is going to drive the same graphical interface you drive, it sure benefits enormously from watching how you drive it. Chronicle is the layer that makes driving your software smarter over time. So your workflows, your app preferences, your muscle memory patterns, they all become context the agent inherits. The privacy trade-off is that the screen captures are sent to OpenAI servers. They have unencrypted local memories and they're not available for that reason in the EU, UK, or Switzerland. And that's a cost OpenAI accepted because the feature works better with it and because the data makes the agent better at driving your software over time. Conway is a different kind of signal. On April 1st, Anthropic accidentally published the Clawed Code source code, roughly 500,000 lines of TypeScript when a packaging error pushed it to a public registry. Buried inside that was Conway, an always on event-driven agent environment with its own sidebar UI, three panels called search, chat, and system, web hook, triggered invocation, a proprietary extension format, browser control via cloud and Chrome, and deep connector integration. I've written about this at length separately, so I'll keep it short here. Conway assumes the world is going to build for agents with structured triggers, explicit extensions, event- driven execution. It's designed to plug into agent native interfaces that other companies will build over the coming year or two. Does that assumption hold? Anthropic wins this bet if MCP adoption accelerates, if enterprise software ships clean integrations, if the standards mature quickly enough for Conway to have a rich substrate to act on. It's a good bet in many ways. MCP is already spreading very fast. It's become a deacto standard. Anthropic is the company pushing it the hardest. The developer ecosystem around cloud code has tremendous momentum, but it requires the ecosystem to move and enterprise software ecosystems tend to move slowly. The long tale of internal tools is not getting agent interfaces on a timeline that matters. Open AI does not need that. The agent drives whatever software you use yourself. No vendor has to cooperate. No integration has to get built. Anthropic needs the whole software industry to show up and build and OpenAI does not. So my read is the second scenario is more likely on the time scale that matters. But it's a hypothesis. If enterprise software moves faster than I think that picture could change in Claude's favor. One more piece worth laying out because it tells you how serious OpenAI is about this specific direction. In the Vance interview, Brockman and Altman described three strategic vectors. The Agentic platform itself, computer work specifically, and personal AGI that does things for you in the real world. That's what they say their whole road map is, those three things. The clearest signal of how serious they are is in what they cut. Sora got shut down. A drug discovery effort got pulled. Not because the work wasn't interesting or important, but because the use cases didn't ladder up to those three vectors. That's an unusually disciplined cut for a company that's been accused of sprawl for a while, and it tells you leadership is willing to kill popular products to stay focused. One more nugget here. Compute is explicitly a profit center now, not just a constraint. Open AAI is monetizing the scarcity, which means the super app consolidation plan. Chad GPT is a conversation hub. Codeex is an agent. Atlas is a browser. That's not just a product bet. It's a bet on routing users into a platform where compute gets built at margins OpenAI chooses. And that changes the financial shape of what they're building. So that's where both labs are going. Two paths, two bets, and two road maps that are really quite different. Which leaves the last question. What do you do with all this if you're using these tools or making decisions about them? Computer use is the one capability where the gap between codeex and claude is wide enough to change what you actually use. If your work involves driving software that doesn't have good APIs, and for most operators, a lot of it does, Codeex is a product that's ready today. Claude will probably get there. The research preview is improving visibly, and I know that they like to close these competitive gaps. But today, Codex wins on this specific capability by a wide enough margin to matter. If you're tackling dashboards, if you're tackling front-end visual testing, if you're dealing with Slack and email at the same time, with bug reproduction, with cross- app workflows that you'd otherwise be copying and pasting between tools, anything where the bottleneck is the friction of the interface rather than the reasoning, Codeex feels like a good fit. Now, on scoped and bounded work, Claude is often still tighter and more efficient. co-works point in a folder and describe the outcome ergonomics are cleaner than Codeex's one agent figures it out for tasks where you want that explicit control over what the agent touches. Claude Code remains rightly loved for its developer friendly ergonomics and its recent focus on deploying multi-agent workflows for coding. Codex retains an advantage in refactoring very complex code bases and going after longrunning tasks. Although that gap has narrowed with the release of Opus 4.7, those parameters are kind of set and they're not changing super quickly. The difference to me still boils down to the value for computer use and the differing design philosophy of codeex versus claude on cross tool triage on longrunning parallel agents on ambient work that doesn't fit into a single mode. Codeex is the default now. Chronicle actually accelerates that gap for anyone on pro who's willing to turn it on. Parallel background agents work reliably enough that queuing three or four tasks in codecs before stepping out has become a real workflow instead of a party trick. So use both. Which one should you lean on? It depends on where your work lives. If it lives in knowledge work that's going to get proper agent integrations over the next year or so or has them already, Claude's architecture will get cleaner and more reliable. If it lives in computer work more broadly, the longtail, the legacy tools, the internal systems nobody maintains, Codex is the one that reaches that long tail. So, what do you watch for over the next few months to see which way all of this trends? Two things. First, Conway. If Enthropic announces it publicly, event-driven agents become a real category alongside ambient context agents and the two paths framing starts to really crystallize. If Enthropic delays it or maybe even kills it, it tells you they've lost confidence in the ecosystem cooperates bet on a time scale that matters and more of the category converges on computer use plus ambient context by default. Second, watch for MCP adoption velocity. Anthropic's bet on the ecosystem only pays off if MCP spreads faster than it currently does. If a major wave of enterprise vendors ships on MCP servers in the second half of the year and Salesforce was a good hint in that direction, Enthropic's architecture looks better and better and better. If they don't or if they ship thin wrappers that don't work as well as the actual UIs, driving the UI directly stays the better path. What's the one thing to take away from all of this? Look, I'll keep it simple. 6 months ago, any piece of software that did not have an API was effectively outside the automation conversation. You could not get an agent into it. You had to wait for the vendor to ship hooks or you had to build the integration yourself. That's just not the state of things anymore. Codeex's computer use means that if the software has a screen, an agent can effectively drive it. That widens what's automatable by a much, much bigger margin than most people are really budgeting for. For anyone thinking about automating operations, the surface of what's possible is so much larger today than it was at the end of last year or even a month ago. And the reason it's possible, the reason Codeex can actually drive your software well enough to deploy, that's not the model per se. The model's the brain. Codex is the harness around it. It's the body. And OpenAI built that body specifically by buying a team with a very clear, specific history of expertise. Keep an eye on that acquisition pattern. It's going to tell you as much about who wins the next phase of this as any benchmark chart is going to give you. Now, if you want to lay this all out and get into the details of how to use codeex today to drive your workflows, if you want to dive deeper on the Conway leak details, on the full comparison with Claude, I wrote that all up on Substack link is in the description. Hit subscribe if you want these the moment they drop.
