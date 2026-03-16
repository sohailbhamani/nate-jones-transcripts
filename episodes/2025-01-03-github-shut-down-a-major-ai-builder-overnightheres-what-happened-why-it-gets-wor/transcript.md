---
title: "GitHub Shut Down a Major AI Builder Overnight—Here's what happened why it gets worse in 2025"
video_id: "OVTJUykc6B0"
youtube_url: "https://www.youtube.com/watch?v=OVTJUykc6B0"
substack_url: null
publish_date: "2025-01-03"
duration: "5:39"
duration_seconds: 339
view_count: 14287
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  About me: https://natebjones.com/
  My links: https://linktr.ee/natebjones
  My substack: https://natesnewsletter.substack.com/
  Shutdown thread: https://x.com/lovable_dev/status/1875091208181309540

  Takeaways:
   1. Unprecedented Growth Rates: Lovable.dev’s AI-powered platform created GitHub repositories at a rate of one every two seconds, highlighting the impact of exponential AI-driven workflows on traditional infrastructure.
   2. Outage Triggered by Limits: GitHub enforced a terms of service violation block overnight, causing an 8-hour outage for Lovable.dev, despite prior assurances that rate limits wouldn’t be an issue.
   3. Emergency Workaround: Lovable attempted to shift operations to Amazon S3 to maintain service, but the workaround underscored the challenges of finding alternatives to GitHub’s social and technical ecosystem.
   4. Architectural Challenges Ahead: AI workflows and autonomous coding agents are driving exponential growth, requiring infrastructure providers to rethink their systems for 2025 and beyond.
   5. Dependency Risks: Lovable’s reliance on GitHub highlights the importance of platform redundancy, especially as AI adoption accelerates usage beyond traditional human coding speeds.
   6. Future Infrastructure Demands: SaaS platforms and developer tools must adapt to AI-driven user interactions, which will radically shift usage patterns and introduce new security and authentication challenges.
   7. Call for Proactive Refactors: Infrastructure providers must address scalability, redundancy, and security now to avoid outages and support the growth of AI-augmented workflows.

  Quotes:
  “We’re facing exponential growth from AI-driven coding—and this is just the beginning.”
  “AI workflows are reshaping infrastructure demands, forcing providers to adapt to new usage patterns at an unprecedented scale.”
  “The Lovable.dev outage isn’t just a glitch; it’s a warning for 2025 as AI agents change how we build and use systems.”

  Summary:
  The Lovable.dev outage, caused by GitHub’s enforcement of repository creation limits, revealed the challenges traditional platforms face as AI-driven workflows grow exponentially. Lovable attempted an emergency workaround on Amazon S3 but exposed the risks of heavy platform dependence. With a 10X increase in coding activity from AI tools and autonomous agents, infrastructure providers must urgently refactor architectures to handle massive traffic spikes, security risks, and shifting user patterns. This incident underscores the need for scalable, redundant systems to support AI-augmented workflows in 2025 and beyond.

  Keywords:
  Lovable.dev, GitHub, AI workflows, repository creation, outage, terms of service, exponential growth, autonomous agents, infrastructure refactor, redundancy, scalability, 2025 technology trends, platform dependence, SaaS tools, AI-driven usage, security challenges, authentication systems, LLM, agentic workflows.

yt_tags:
  []



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
  - "Founders"
entities:
  companies:
    - "Amazon"
    - "GitHub"
    - "X"
    - "Lovable"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# GitHub Shut Down a Major AI Builder Overnight—Here's what happened why it gets worse in 2025

GitHub took down lovable"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "amazon"
  - "coding"
  - "frameworks"
  - "github"
  - "leadership"
  - "lovable"
  - "make"
  - "product-management"
  - "startups"
  - "x"
---

# GitHub Shut Down a Major AI Builder Overnight—Here's what happened why it gets worse in 2025

GitHub took down lovable. deev today and I want to talk about it because at the end of the day we are in a situation where that kind of thing is going to get much much worse in 2025 I'll explain the competing exponential growth curves that we're on here and how this all broke down so overnight in the US lovable. deev suddenly was unable to continue to create GitHub repos and this quickly snowballed into a major outage because at the end of the day their exponential growth has been so fast lovable. devs has that they were creating GitHub repos at the rate of one every two seconds absolutely insane speed and they said that they had previously checked before the holidays with GitHub and said look we're growing we are growing really fast we're depending on GitHub to be up are you good are we going to hit quotas or rate limits and GitHub told them no well no one is quite s saying what happened I've dug in GitHub won't say lovables being polite about it all that is actually occurring is that there's a terms of service violation that lovable ran into sometime during the night hours on January 2nd in the US GitHub was all asleep and it's the holiday so like you're really waking up a developer who's somewhere skiing at this point and no one was on call really and certainly they weren't responsive because love was hard down for hours overnight a major client of theirs hard down for hours they said they tried and tried and tried to wake up lovable and got nobody they tried to build a workaround on Amazon S3 during the night to keep people up because it's they're a European startup it's like the first working day of the year in Europe and people are like coming in with their New Year's resolutions and they want to build stuff and it's hard down so they're desperately scrambling to get stuff over to S3 building a workaround and it's like you can read on X the different sort of updates that come through and it's always like more bad news coming through until they finally got GitHub to wake up this morning and GitHub took them back out of jail and allowed them to start creating repositories again now reading between the lines I strongly suspect that one of the takeaways for lovable on this is they can't be that dependent on GitHub and so they probably will eventually move to Amazon S3 as a way to start to scale this which is not exactly ideal because one of the things that's really nice about GitHub is everyone knows what it is everyone goes over to GitHub and knows what you've done and there's just not a good substitute for that social quality that GitHub brings to code and so it's sort of sad to see a situation where you have an AI tool trying to build on top of GitHub trying to reinforce the GitHub flywheel and GitHub just isn't set up for the volume and this is something that I want to call out because I think there's two exponential curves that are happening in 2025 that are stacking each other and they are going to make life even worse for providers like GitHub if you are in the infro business that has anything to do with uh Dev building at all brace yourself do an architectural refactor now and the reason why is because over the last 20 years your entire business model has been Engineers committing Cod at the speed that humans can write code not anymore now in 2024 you've had like a massive 10x explosion in the number of people who are interested in coding because they can code with llms and so there's a bunch of AI driven code being committed to repositories like GitHub and that's about to get even worse because now stack on top of that sort of massive explosion in humans using AI to code now agent will be using AI to code because we're going to have autonomous agents coding within the next couple months here so now like 10x to 10x and you're going to get even more code being committed look I am not saying that this is all high quality code we're not talking about that here we're just saying that from a sheer volume perspective if you are in Tech you should be doing a refactor now you should be looking at your architecture and looking at the ways people use your systems and ask yourself if these people suddenly get access to AI tooling that enables them to be much more productive how will their usage of my system change how will it change let me give you an example that's not even GitHub let's just say you're running a nice little SAS business for marketers let's say your marketer suddenly gets a hold of project Mariner it gets a hold of a browser that's agentic right and they're like oh thank God I don't have to go and get the freaking uh report downloaded off of off of this tool I can just go and have the agent do it for me every morning and then now they feel free so they're going to code up five or six different agents give them different tasks they're going to be all over your system they will be using this person's login with or without your knowledge and suddenly your usage patterns are going to completely change and that's a light version of what could happen imagine the consequences for like security and oth so we have a lot to work on when it comes to agentic and I think the GitHub example is an early 2025 warning of how bad it could get if we are not careful so I'm glad lovable is back up but unfortunately because of the fundamentals in the space right now I expect more of this to happen in the coming year
