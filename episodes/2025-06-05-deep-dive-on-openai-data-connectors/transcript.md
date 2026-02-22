---
title: "Deep Dive on OpenAI Data Connectors"
video_id: "UvC33D6lwRI"
youtube_url: "https://www.youtube.com/watch?v=UvC33D6lwRI"
substack_url: null
publish_date: "2025-06-05"
duration: "11:39"
duration_seconds: 699
view_count: 7756
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "AI Strategy"
difficulty: "Advanced"
audience:
  - "Executives"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Google"
    - "Notion"
    - "GitHub"
    - "Zapier"
  people:
    []
  products:
    - "Claude"
    - "Zapier"
    - "Make"
    - "MCP"
    - "Operator"
  models:
    []
concepts:
  []
summary:
  - "# Deep Dive on OpenAI Data Connectors

Open AAI released data connectors yesterday"
keywords:
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "claude"
  - "deep-dives"
  - "frameworks"
  - "github"
  - "google"
  - "leadership"
  - "make"
  - "mcp"
  - "notion"
  - "openai"
  - "operator"
  - "prompting"
  - "tutorials"
  - "zapier"
---

# Deep Dive on OpenAI Data Connectors

Open AAI released data connectors yesterday. Data connectors are basically OpenAI's answer to Claude connecting you to Gmail and Claude connecting you to calendar etc. being open AI, uh they added a bunch more that Claude had not previously added because of course this is a competitive arms race. And so they added GitHub, they added Linear, they added Zapier, they added a bunch of things. And then they also of course had Gmail, they had Outlook, they had Sharepoint, they had Google Calendar. Essentially they are saying that you can now search in your plus teams and pro account across a lot of the personal information that you create as you do work and they are careful to call out to their credit that this is not a perfect search mechanism. They specifically call out this shouldn't be used if you're searching for example in Google Drive for doing extended work across uh ma math on sheets. And so if you're doing a spreadsheet analysis, deep research is probably not best positioned for that. I'm sure they're right. But even when I gave it several queries, deep research, that were not designed to test it against what OpenAI suggested, it still didn't work. In other words, I tried to stay away from the warning spots. I tried to give it challenging queries similar to what I'd given deep research in the past when it only worked on the open web and it really fell down on local information and I was actually able because you can see the chain of thought for deep research to pull up that chain of thought during the queries I sent and pull screenshots of what deep research said it was doing. And I learned some fascinating stuff. It turns out that the API result that it is relying on to get results from calendar, to get results from Gmail, tops out at 15. In other words, if you want to say like you would to, I don't know, a poor hardworking executive assistant, please do a comprehensive analysis of last month, last month's email volume, cohort it out. Tell me who I need to be focused on. Tell me how I can use my time more efficiently. give me a sense of the types of emails that I need to respond to and the ones I don't. It can't do that. It has access, but because of the thinness of the data pipe it's working with, it is absolutely impossible. And trust me, I tried. I tried to do an email analysis of the last 100 emails. I tried to do a calendar analysis of the last 100 calendar docs. And this is me being kind. I would have said a thousand if I could, but I had a feeling. Uh I tried to do an analysis of the last 100 uh Google Docs that I created. It does extremely limited searching. I could find evidence in in my query for a 100 docs. I found evidence of it calling back three. In my query for a 100 emails, it could not produce exact counts. It just kind of waved its hand in the air and gave me approximate numbers. And as someone who gets the email every day, I knew that it had correctly ga guessed categories, but it had wildly incorrectly guessed numbers. The numbers it was guessing for whole groups of my email were completely off and it just didn't do the groundwork of actually checking the email even though the data connector was there. So it just failed like we just don't have to call it anything else. Where did it succeed? You might wonder. Well, I will say I gave it a specific topic to look into and it did much better there. So, if you give it, let's say you give it a webinar you're planning or you give it an event that you want to do, something that has a defined time focus and you say, "Look across the web. Look across my email, my calendar, give me a comprehensive briefing for just this very tight topic that's very clearly delineated by keyword." Then it does pretty well. It can use that keyword as a guidepost across Gmail, across calendar, across the open web, across your Google Docs, and come back with something that is actually a decently good comprehensive briefing. How does it that it do that well? Because each individual data source is not going to be a ton of individual units of data. It's not going to be more than 15 in many cases. and it can then assemble that out into something that's really comprehensive by inferring and reasoning across all of them together which 03 does very well. It also helps if that event has a public presence because then it can do what uh deep research does best which is reason across the entire web at scale. So to me when I look at this if I step back I see this in the context of ongoing competition both between model makers between anthropic and open AI which I laid out at the beginning and also between model makers and specific verticals they want to go after. One of the questions that I got uh as this came out was is anything safe? Like they keep going after these verticals. Who's next? Granola. Did they get eaten? Because one of the data sources here is that like teams will now record your calls. Look, to be honest with you, I think the common rationale across these recent moves by both Anthropic and Open AAI is all about tokens and data in. It's all about training data. Everybody's hungry for it. And so they're building connections to Gmail for training data, for calendar for training data, anything they can get. They're building the meeting transcripts piece for training data. They're building um Anthropic is cutting off access to models in Windsurf, which was acquired by OpenAI in order to cut OpenAI off of training data. Now, it doesn't really matter because Windsurf can get thirdparty access instead of first-party access. But the point is like the intent the intent is to cut them off on training data to keep your your rival from getting training data. And so if you're building in the space, the question you should be asking yourself is how easy is it for a model maker to get access to training data that they would find high value that would have real rewards if they got it right. And so my proposal to you is to look for places where that data would be hard to get where they couldn't just add an MCP server and get the data because that is basically what OpenAI did. And I think the question is not would they add an MCP server to get the data if they could. It is is collecting the data to do this in line with their larger vision that they have stated for the company because you know throwing elbows between open AI and anthropic aside this is right in line with what we would expect. OpenAI has been really clear about their plan to be the default OS for the enterprise. If you're going to be the default operating system for work, well, you got to do meetings. Shouldn't have surprised anybody. You got to do Gmail. You got to do Calendar, you got to do Outlook, you got to do SharePoint. This isn't that surprising. Now, are they doing it well enough that I would trust them with all of that now at the enterprise level? No, they're not. In fact, this is reminding me a lot of the initial release of Operator back in January when Operator came out and it was frankly pretty terrible. I used it about three or four times and uh it was inaccurate. It was slow. It took forever. It froze up on easy things like add to cart. They just didn't use it anymore. Well, I had a feeling they would make it better because after all, it's in beta. And last week they did. They added their 03 model as the driving model behind operator. Operator got about 10 times faster and 10 times more accurate. It's actually a useful tool now. They didn't make as big a fanfare out of it, but I now find that I actually go to it and imagine specific use cases because it is fast enough. I used it for a real task. I did not pre-plan just this week. Uh, and if you're wondering, it was flight planning. And yes, I know they trained for flight planning and all of that, but it wasn't even usable for flight planning in January. So, it's not just that they trained for it, it's that they got the right model. They took the time. They probably collected data anonymously from some of us users as we were using it. um and they were able to eventually make the model better at browsing the internet. I expect the same thing to happen with this connectors play. This is a long-term play. I don't consider it particularly usable today. I consider the move toward data for the enterprise and workplace something that is not surprising and something where open AI is going to get much better at this over the next six months. They need more data to reason across. Now, this doesn't mean that they will immediately become 10 times more intelligent at handling all of that data. I do think there are real questions about the ability of these models to reason well across very large data streams that are incredibly messy that are created by humans. Have you looked in your notion or your wiki at work? It's probably pretty dirty. Everyone kind of rolls their eyes and throws stuff in there. When you have a dirty repository of unstructured text data like that, it is inherently not a great place to ask the AI to start to make meaning. And yet that is often the case for a lot of our text repositories. And so I think my challenge to you is how good is your prompting and how precisely are you asking for work to be done? One of the characteristics that we are learning for AI in 2025 is that when you prompt well, when you prompt cleanly and clearly with a very specific task in mind, you often get surprisingly good results. But when you ask for something fuzzier, harder, more like you would ask a very senior researcher where you don't even fully know the question, you often get quite poor results. And that really explains how my experience went with connectors today. I was able to get my specific query around, you know, events and webinars and understanding how they all uh assembled into a briefing and kind of give me the sense of the emails and the calendar and the agenda and the public profile for this specific event. That went well. It was a very specific query. My more generalized discovery question around patterns in my email and patterns in my calendar that went terribly. like it just did not go well at all and it could not pull the volume of data needed to make sense of it. And so I am taking away from that that part of the challenge for work here in 2026 is how can we more effectively structure our queries so we precisely ask what we intend. That takes a lot of human work. It's not easy but I think that's a big work skill that we all can stand to get better at. Clearly, I could stand to get better at it because I batted like one for three, one for four on my test queries today. I need to figure out ways to use this tool that are more more like a scalpel and less like a chainsaw. This is not a chainsaw tool. It's a very precise tool right now. It may get higher bandwidth as they increase the scope of those connectors. It's not that high bandwidth now. So, that is the skinny on what happened with data connectors. I hope you enjoyed this quick review and uh we'll get into a bit more of like AI and work I think in the next piece because there's a lot more that is behind the scenes of this move that I want to dig deeper on. All right. Cheers.
