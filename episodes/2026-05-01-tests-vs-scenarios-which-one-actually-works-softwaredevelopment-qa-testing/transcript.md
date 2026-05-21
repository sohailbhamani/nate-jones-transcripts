---
title: "Tests vs Scenarios: Which One Actually Works #softwaredevelopment #QA #testing"
video_id: "g2occe4xMHk"
youtube_url: "https://www.youtube.com/watch?v=g2occe4xMHk"
publish_date: "2026-05-01"
duration: "1:33"
duration_seconds: 93
view_count: 7710
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  My site: https://natebjones.com
  Full Story w/ Prompts: https://natesnewsletter.substack.com/p/the-5-level-framework-that-explains?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  ___________________
  What's really happening when 90% of Claude Code was written by Claude Code, yet most developers using AI get measurably slower? The common story is that AI coding tools make everyone faster—but the reality is more complicated when a rigorous study found experienced developers took 19% longer while believing they were 24% faster.
  
  In this video, I share the inside scoop on why the gap between dark factories and everyone else is the most important divide in tech:
  
  • Why StrongDM's three-person team ships production software with no human-written or human-reviewed code
  • How the five levels of vibe coding reveal that 90% of developers plateau at level three
  • What external scenarios and digital twin universes solve that traditional tests cannot
  • Where the bottleneck has moved from implementation speed to specification quality
  
  For engineering leaders watching the frontier pull away, this is not a tool problem—it's a people problem, a culture problem, and a willingness-to-change problem that no vendor can close.
  
  Subscribe for daily AI strategy and news.
  For deeper playbooks and analysis: https://natesnewsletter.substack.com/

yt_tags:
  - "software testing"
  - "AI strategy"
  - "large language models"
  - "LLMs"
  - "AI agents"
  - "future of work"
  - "automation at work"
  - "AI career advice"
  - "upskilling with AI"
  - "AI coding tools"
  - "software engineering AI"
  - "dark factory software"
  - "agentic coding"
  - "prompt engineering"
  - "AI labor market"
  - "junior developer jobs"
  - "AI native startups"
  - "AI jobs for developers"
  - "software team AI"
  - "coding"
  - "programming"
  - "ai assisted coding"
  - "software engineer"
  - "ai coding"


# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Product Managers"
entities:
  companies:
    []
  people:
    []
  products:
    []
  models:
    []
concepts:
  []
summary:
  - "# Tests vs Scenarios: Which One Actually Works #softwaredevelopment #QA #testing

StrongDM doesn't actually use traditional software tests"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "coding"
  - "frameworks"
  - "product-management"
---

# Tests vs Scenarios: Which One Actually Works #softwaredevelopment #QA #testing

StrongDM doesn't actually use traditional software tests. They use what they call scenarios, and the distinction is important. Tests typically live inside the code base. The AI agent can read them, which means the AI agent can, intentionally or not, optimize for passing the tests rather than building correct software. It's the same problem as teaching to the test in education. You can get perfect scores and shallow understanding. Scenarios are different. Scenarios live outside the code base. They're be havioral specifications that describe what the software should do from an external perspective, stored separately so the agent cannot see them during development. They function as a holdout set, the same concept that machine learning users use to prevent overfitting. The agent builds the software, and the scenarios evaluate whether the software actually works. The agent never sees the evaluation criteria. It can't game the system. This is really a new idea in software development, and I don't see it implemented very frequently yet. But, it solves a problem that nobody was thinking about when all the code was written by humans. When humans write code, we don't tend to worry about the developer gaming their own test suite unless incentives are really, really skewed at that organization, and then you have bigger problems. When AI writes the code, optimizing for test passage is the default behavior unless you deliberately architect around it. And, it's one of the most important differences to really understand as you start to think about AI as a code builder.
