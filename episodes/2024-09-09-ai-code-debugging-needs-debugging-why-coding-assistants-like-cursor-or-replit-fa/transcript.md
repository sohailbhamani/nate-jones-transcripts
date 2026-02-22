---
title: "AI Code Debugging Needs Debugging: Why coding assistants like Cursor or Replit fail to fix code"
video_id: "E3Mry80TEgs"
youtube_url: "https://www.youtube.com/watch?v=E3Mry80TEgs"
substack_url: null
publish_date: "2024-09-09"
duration: "4:33"
duration_seconds: 273
view_count: 592
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Tools"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "Anthropic"
    - "Cursor"
    - "Replit"
  people:
    []
  products:
    - "Cursor"
    - "Make"
    - "Sonnet"
  models:
    []
concepts:
  []
summary:
  - "# AI Code Debugging Needs Debugging: Why coding assistants like Cursor or Replit fail to fix code

You know, code repair is a long way behind code authorship from an AI perspective, and I think it's a"
keywords:
  - "ai-agents"
  - "ai-strategy"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "coding"
  - "cursor"
  - "frameworks"
  - "make"
  - "prompting"
  - "replit"
  - "sonnet"
  - "tutorials"
  - "workflows"
---

# AI Code Debugging Needs Debugging: Why coding assistants like Cursor or Replit fail to fix code

You know, code repair is a long way behind code authorship from an AI perspective, and I think it's a missed opportunity. At the end of the day, the only thing that really matters is working code that you can use to get your job done. And right now, so much of the work that I've seen has gone into crafting coding experiences that enable someone who is new to coding to get started and get into coding fast. And so you have things like the Replit AI agent that dropped, where it's like, hey, let me get started, let's do a multi-step plan, and then you can kind of like go from there. And it's often the things that work are a simple experience, right? Like it's like, let me go through this multi-step plan and knock up a quick HTML website for you. But there's been a lot less work put into the complexities of how you edit and adjust code reliably with AI and how AI can fix its mistakes. I was using Replit this weekend and it ended up just sort of giving up and saying, please go talk to a real person at Replit because I can't fix this. And it was a mistake that it made itself. It had tried six different times to fix it and it had not thought through systematically despite my hints what was going on. I used the yellow duck method. I like talk to myself and kind of talk through what the coding issue was. I suggested this is the actual thing that's happening. And I suggested a plan forward and it just couldn't engage. And there are absolutely opportunities. There are dollars being left on the table here for an AI that is able to be more self-critical, that is able to actually think about what has been written previously and not over-index on it. And there's actually really good reasons from a LLM perspective why it's hard for AIs to correct their mistakes within a chat. But there are also really good fixes that are on the table if you think about the interface. So the reason why they fail to correct their mistakes reliably is because LLM chat is context dependent. And so when they make the initial mistake in the chat, they are predisposed rereading the chat through the context window to make the same mistake again. And that's why you just get into this loop where it says, if you've ever been coding with AI, I'm adding debugging. so that this will figure this out. Well, that's a death knell because at the end of the day, it adds the debugging or so it says, and it doesn't actually debug. It doesn't do the logical thinking process that goes with debugging. And when you think about it, that's the part that matters. It's not the writing the AI debugging log reads, right? Like you can get an audit log of everything that happened in the code. And if you don't do critical thinking about it, It's not going to help you very much, is it? So the context window is super important for understanding why LLMs tend to get into these loops, these spirals. But you can also think as a company about how to not get hampered by that architecture limitation. For example, you could say, it seems like there's multiple responses in the same vein here. Maybe I should spin up a new chat and on the back end, give it a sys prompt that basically summarizes the issue and see if the new chat can help unlock the user here. Like that's a really simple one that I've seen nobody do. It would not take any new technology. It's just a slightly different experience. And it would help us get out of these sort of endless loops of debugging and code that don't go anywhere. And so I guess my challenge is if you want to make workflows more useful, maybe focus on the workflow that's already happening with code authorship and not just on the net new workflow you want to start. Look, there's a ton of value that's clearly being unlocked as Cursor and as Replit AI come online, other tools come online that help new people learn to code. I love that. I think it's going to be impactful. I think it makes sense from a business perspective, but it also makes sense to help people who work in code to edit more effectively. And I know Sonnet 3.5 is working on that with AI for Enterprise and Anthropic, and that's great. It feels like we have a ways to go with strong critical thinking edits on code, and I would love to see more investment in that direction.
