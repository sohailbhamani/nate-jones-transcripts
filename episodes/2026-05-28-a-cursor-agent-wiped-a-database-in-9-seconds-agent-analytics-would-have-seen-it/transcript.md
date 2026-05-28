---
title: "A Cursor Agent Wiped a Database in 9 Seconds. Agent Analytics Would Have Seen It Coming."
video_id: "n0nC1kmztSk"
youtube_url: "https://www.youtube.com/watch?v=n0nC1kmztSk"
publish_date: "2026-05-28"
duration: "11:51"
duration_seconds: 711
view_count: 6312
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  Full Post w/ Prompts: https://natesnewsletter.substack.com/p/agent-product-analytics?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  __________________________________
  What's really happening inside an AI agent run that your product dashboard cannot see?
  
  The common story is that agent failures are engineering incidents — but the reality is that most of them are product analytics failures hiding inside the agent run.
  
  In this video, I share the inside scoop on why product analytics for AI agents has to start from the run, not the click:
  
   • Why chat logs and trace data are not product analytics
   • How agent runs replace sessions as the unit of product behavior
   • What the completion vs acceptance gap tells you about trust
   • Where Salesforce's Agent Work Units land in this picture
  
  For operators and product teams shipping AI agents, the opportunity is enormous, but only if the rudder of product analytics is in place before agents are running full speed in production.
  
  Chapters:
  00:00 The agent era changes product analytics
  00:46 Ten billion tokens of agent code in production
  01:34 A Cursor agent deletes a database in nine seconds
  02:25 Why most dashboards miss the actual failure
  03:09 Delegated work is the new unit of product behavior
  04:08 Chat logs are not enough
  05:02 Engineering traces are not product analytics
  05:59 Salesforce Agent Work Units name the work
  07:01 The correction is your most valuable signal
  08:21 The completion vs acceptance gap
  09:42 Three events to ship first
  10:38 Product analytics is the rudder on your agents
  
  Subscribe for daily AI strategy and news.
  For deeper playbooks and analysis: https://natesnewsletter.substack.com/
  
  Listen to this video as a podcast.
  - Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  - Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

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
  - "AI agents"
  - "Salesforce Agentforce"
  - "Cursor agent"


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
    - "Salesforce"
    - "Slack"
    - "Cursor"
  people:
    []
  products:
    - "Cursor"
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "We have never had a chance to look at the impact of our decisions in real time and now we do with agents"
keywords:
  - "ai-agents"
  - "ai-tools"
  - "coding"
  - "cursor"
  - "frameworks"
  - "leadership"
  - "make"
  - "product-management"
  - "prompting"
  - "salesforce"
  - "slack"
  - "tutorials"
---

# A Cursor Agent Wiped a Database in 9 Seconds. Agent Analytics Would Have Seen It Coming.

We have never had a chance to look at the impact of our decisions in real time and now we do with agents. And we we think of this as a problem. We think of this as oh there's more eval to do. Oh, we have to build in these agent runtime telemetry and agent runtime observability and we get lost in the technicals. It's not about technicals. It's about the the opportunity to have an agent running full speed in real time and we can shape it and steer it if we get good telemetry back. That's so cool. And we've never had that chance. When I tell people that I have had an equivalent line of code production in the last year to 55,000 developer years, maybe you understand why. And that's not an exaggeration. I actually measure the tokens. It's it's it's about 10 billion tokens. Maybe you understand why it's so important to have agents that we can shape, to have agents that we can guide, to have agents that have good boundaries because effectively we have 10xed or 100xed or a thousandxed our ability to get stuff done. We got to shape this speedboat that we built. It's really important. A cursor agent reportedly erased Pocket OS's production database and backups in 9 seconds. That is the kind of sentence that gets passed around by CTO's because it sounds like a horror story. It's a small software company. It's production database, volume level backups, one railway API call, 9 seconds. The obvious story here is that an AI coding agent went rogue, right? I don't think that's the most useful story here. I think the more useful story is that most product analytics would have missed the actual product failure. A normal dashboard might show an active user. It might show a long session. It might show that the AI feature was used. It might even show a lot of messages in chat. But none of that tells you what happened inside the agent run. What instruction was the agent given? What environment did it think it was in? What credential did it find? What tool call did it make? What permission boundary failed? What did it report afterward? Where did the human trust loop break? This this is the new analytics problem. When the user is an agent, product analytics no longer stops at clicks and sessions and messages and funnels. The unit of product behavior is becoming delegated work. And that's the mental model I want to keep in mind for this video. Agent analytics is not a debugging sidebar. It is the way we shape our work. It is the future of product. For most of product analytics history, the question was very simple. Did the user show up? Did they click? Did they move through the funnel? Did they come back? Did they convert? Those questions still matter, but they're not enough. In an agent product, the important action may not be a click. It might be the instruction. The important product event may not be a page view. It it might be a tool call. The important failure might not be a user dropping out of onboarding. It might be the agent retrying the same action, hitting a permission boundary, asking for approval, losing context, or finishing work the user quietly rewrites. Chat logs are useful. They tell you what the user said and what the agent replied. They help with qualitative review. They can reveal weak prompts and missing context and bad tone and obvious hallucinations and places where the product is confusing. But a chat log does not tell you enough about the work. It usually doesn't tell you which tools were available, which tools the agent called, which calls failed, where it retrieded, where permissions blocked the work, or whether the user accepted or corrected or interrupted or finished the task by themselves. Even when some of that signal appears in a chat transcript, it's trapped in text. So a person might be able to read that chat transcript and get some insights, but a dashboard can't pull that up and aggregate it in a way that we can scale when we have hundreds or thousands of agents in production. All of this matters because chat activity can look healthy. And if you live in a chatbot mental model, you think that's what you need. And yet the work can still be failing when agents aren't monitored appropriately. Let me give you an example. A long chat might mean the user is exploring a complicated task, but it might also mean the agent is forcing the user to restate context and correct errors and approve obvious steps and work around missing product structure. And in most monitoring, both of those cases collapse into the same metric, the active session. This is just not enough for Nentic product. Developer observability is closer here, but it's still not the whole answer. And I think most people think it is right. So tracing tools can capture model calls and tool calls and handoffs and guardrails and latency and cost and errors during execution. And that data really matters and engineering teams definitely need it. But trace data is not automatically product analytics. Product analytics has to tell you whether that failure mattered to the user, whether the workflow still completed and whether the user accepted the results and whether the product ought to change. So, a trace can tell you that the agent asked for approval, and product analytics has to tell you whether that approval created real safety or just added friction. A trace can tell you that a run cost 30 cents. Product analytics has to tell you whether that was worth it. So, this is the layer most teams are missing right now. They still have to build. And the right unit to think about is the agent run. A session tells you that a user showed up. An agent run tells you what work was attempted. A run might begin when a user asks for customer support or invoice reconciliation or meeting preparation or candidate movement in the pipeline or account research. The workflow can totally change by product. The analytical problem is very similar because you ask the same questions. What was the user trying to accomplish? Did the agent understand the intent? What tools did it use? Which calls fail? Did it ask for approval? Did a permission policy stop the action? Did the task complete? Did it partially complete? Did it fail? Did it get abandoned? Did the user accept the output or redo the work? Those are now product questions that we have to care about. Now, Salesforce is kind of pointing in this direction already. In its February 2026 fiscal Q4 earnings release, Salesforce introduced agent work units or AWUs. Say that five times fast. To measure tasks accomplished by AI agents, the company said 2.4 4 billion AWUs had been delivered to date across Agent Force and Slack, growing 57% quarter over quarter. And that's a significant shift because that means Salesforce, the biggest SAS company on the planet, is not talking about seats. It's not talking about sessions. It's not even talking about tokens. It's trying to name the work unit. But a work unit is only useful if the team knows what kind of work happened, what workflow it belonged to, whether the tool calls succeeded, whether the user trusted the output, and whether the business outcome improved. Otherwise, the new metric becomes the old problem with a nice name. Instead of staring at chat volume, teams will then stare at work unit volume. The product team still needs a runle view per agent. One of the most valuable signals in that view is the correction. When does a user interrupt an agent, edit an output, deny an approval, give a clarification, or reopen a task in the middle of a run? They are labeling that run. They are telling the product team what the agent misunderstood, what context was missing, which action felt unsafe, and which output didn't meet the standard. That's why agent analytics and eval belong so close together. A denied approval is effectively a test, right? Should the agent have proposed that action? Should the agent have found the relevant preference or policy? A failed tool call can become a schema test. An abandoned workflow can become a research cue. This doesn't mean every prompt and customer record and model output should be thrown into a training system. The privacy treatment has to be explicit. You can't just do it by volume anyway. But it does mean that the product team should shape product analytics that help us understand how people are actually getting work done with agents. And the product team's ability to understand mid aentr run corrections is key. Let me give a few examples here. Completion means the task reached a finish state. Right? Acceptance means the user trusted the result. Those are very different things. If in a product analytic systems the completion rate is high and the acceptance rate is low, the agent is not raising trust, right? It's finishing work users don't trust. If completion is low and acceptance is low, users may be abandoning before the product reaches a reviewable state. If completion is low and acceptance is high, the product may be too conservative, but very valuable when it works. And if completion and acceptance are both high, that's a signal that your workflow may be ready for more autonomy. The gap between completion and acceptance is the part most dashboards have difficulty with today. So, if you're trying to get started, where should you ship first? I would say you want to ship three events. You want to understand when your agent runs start, when your tasks are completed, and when users shape your agent runs in the middle, and you want to tie all to the same agent run ID. That's really critical because it helps you then to get to completion rate and correction rate by workflow. We really have to step back and think about a different set of questions when we're shaping agent work that works this fast. And that's why I emphasize interruptions and retries and handoffs so much because those are the new clicks of the agent era. A good agent product does much more than just produce an answer, right? It moves through work with the right amount of autonomy. It asks for help at the right moments. It recovers from failure. It respects permissions. It uses memory correctly. It produces outcomes that users trust. This is the task you are trying to solve with product analytics. is you're trying to understand to what extent as you build an agent product is the usage you're getting useful? To what extent is the agent that you are working on able to get this work done in a way that's meaningful? You should be asking yourself really regularly whether you have the product analytics views you need to shape agents at the speed at which they run. And that question has never been more high lever. agents are capable of accelerating work a thousandx but the extent to which we're going in the right direction with them is really a function of the rudder on those agents and that rudder is product analytics and I see too many people who are delegating that to engineering who are saying the engineering traces are enough we see the engineering traces and we can shape it and move it those are necessary you have to have engineering traces to build the product analytics on the top but you really really need a good data schema and good product analytics if you're going to have an opinion about the product value of the agent runs and that's what you need to get useful work done otherwise all you're seeing is activity and then terrible results like the database deletion that I started this video with and you're wondering why is that there's probably a technical issue let's bottom it out you should instead be saying what is the history of agent behavior for this workflow that we could have seen understood and predicted off of so that we don't get into the situation where the agent ever gets a chance to delete a production database. You should see the warning signs that agents are having defective workflows, defective runs long before they hit a delete moment like I shared. And you won't do that without product analytics. So if that's you, I've got the start guide over on Substack and I will see you next time. We've got lots more fun stuff coming. AI never really stops. So subscribe and you won't get lost and you won't get left behind.
