---
title: "How to Use AI on Files You're Not Allowed to Upload"
video_id: "EuVvLwWZ5wc"
youtube_url: "https://www.youtube.com/watch?v=EuVvLwWZ5wc"
publish_date: "2026-07-24"
duration: "13:40"
duration_seconds: 820
view_count: 3298
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  How to use AI on sensitive files you can't upload. I built an on-device Mac app that strips what a model doesn't need and rebuilds a clean copy, so your private data never leaves your computer.
  
  Get Airlock: https://natesnewsletter.substack.com/p/use-ai-sensitive-files?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening when the AI you're told to use meets the files you're told not to upload?
  
  The common story is that you just shouldn't paste sensitive data into a chatbot. The real question is what a model actually needs to see, and who has to decide it.
  
  In this video, I share the inside scoop on using AI without handing over the sensitive stuff:
  
  - Why "don't upload the file" stopped being useful advice
  - How to separate what a task needs from what a file contains
  - What Airlock strips out, and what it deliberately leaves alone
  - Where a clean copy can safely go, and where it cannot
  
  The upside is real work moving faster on private material, but a sanitized copy is not authorization, so you still read what leaves before it goes.
  
  Chapters:
  00:00 The file I would never upload
  00:39 Why the warning stops too soon
  01:16 Airlock demo and protected terms
  02:39 Keep or cut: what the model actually needs
  04:03 Rebuild the file instead of redacting it
  04:50 Hand the clean copy to a frontier model
  05:57 Why this suddenly feels urgent
  07:45 What people in my community really do
  09:26 Verizon on shadow AI at work
  10:09 Security fatigue and better defaults
  11:06 Redaction that keeps the work useful
  12:44 Begin with the job
  
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
  - "AI privacy"
  - "shadow AI"
  - "on-device AI"
  - "PII redaction"
  - "data security"
  - "how to use AI on sensitive files"
  - "AI privacy at work"
  - "local AI for private files"
  - "ai"
  - "data privacy"
  - "chatgpt"
  - "claude"



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "Career"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Box"
    - "X"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# How to Use AI on Files You're Not Allowed to Upload

This week I used AI on a file I would never ever upload cuz it was way too sensitive and the model never saw the original file"
keywords:
  - "ai-news"
  - "ai-tools"
  - "box"
  - "career"
  - "coding"
  - "frameworks"
  - "leadership"
  - "make"
  - "product-management"
  - "tutorials"
  - "x"
---

# How to Use AI on Files You're Not Allowed to Upload

This week I used AI on a file I would never ever upload cuz it was way too sensitive and the model never saw the original file. It still found the three assumptions most likely to break my launch after I removed all the sensitive stuff. The customer name, the home address, private medical note that was in there, an API key, and unreleased price. The model needed an operating plan. It sure didn't need any of that PII stuff. And the original, it stayed on my computer. And the useful work still got done by a frontier model. And that is the world I want to live in and I couldn't live in it, so I built it myself. Most privacy advice stops too soon. It says, you know, don't paste your sensitive information into AI. Raise your hand if you seen slides like that. Great. I agree. Now what? The contract still needs a risk review, right? The performance review still needs to be written and yes, you can talk into WhisperFlow and try and get a lot of your thoughts out, but it needs to be organized. Sensitive work does not stop being work. If the safe path means doing all of the cleanup by hand or giving up on AI as a useful tool, the warning hasn't solved the problem. It's just handed it back to us, right? That's why I built Airlock. This pricing plan that I'm going to show you here is synthetic. I made it for the camera, but the problem is not. Let me show you exactly what I kept, what I removed, and why. I'm choosing the pricing plan here. Before I do anything else, Airlock asks me to define my protected terms. And this is where I can enter a customer name, a project name, an internal product code name, or any other ordinary looking phrase that means something specific and confidential inside my company. Now, why do I have to do that? Because a string like Project Lantern, that doesn't look private to a machine, but it might be a super sensitive phrase cuz it ties into a bunch of confidential work. Context is doing a lot of the work in understanding PII and confidential information. And some of that context exists only in our heads as we work. So, we have to give Airlock that context, and then Airlock can check the document, bring the patterns it recognizes, plus the terms I told it to protect, all under one screen. If there's any uncertainty, the starting choice is to just hide that item. That's our default, right? I can keep it, but I have to decide to keep it on purpose. And this is the question that matters a lot more than just building a nice detector. What do we need to do to get this job done, right? Like the whole point is to use AI to get useful work done. The model needs to know that all three warehouses move in the same week. So, we want to keep that detail. It needs to understand that the plan assumes an ERP integration will be ready before the first billing cycle. We got to keep that. It needs to know that training is supposed to happen during normal shifts. Yeah, so we got to keep that, too. But does it need to know that this made-up person, Alice Meridian, has a home address? No, it doesn't need to know that stuff. Does it need her email? Obviously not. Does it need any private medical note that we have here from the operations director? Definitely not. So, all of these things that are personal, like API key, there's no conceivable reason for that credential to be inside the task. It just happens to be bundled into the files, which is how so much confidential information gets leaked into the cloud and into frontier models. It's just kind of bundled in. We don't really need it. Now, the price is a little more interesting. If I were asking the model to evaluate the pricing itself, the number might be part of the work. And for this question, what assumptions could break the operating plan, it's not. So, in this case, I can leave the price behind as well. So, I have to start with a job, not the file. The same price can be essential for one question and irrelevant for another. And once I make those choices, Airlock builds a new Word document for me. It does not draw black rectangles over the old one, right? That matters because Word files are strange little containers, right? Comments, track changes, author names, old edits, and external relationships can accidentally remain even when the page you're looking at looks clean. So, the safer approach is simply to rebuild the approved material into a separate file and leave the original alone. Now, I have two docs. The original is still untouched on my computer. The smaller copy contains the warehouse plan and the relationships the model needs without the customer identity, without the home address, without all the stuff I talked about, right? The personal and confidential information that came along for the ride, to be honest. So, I open the clean copy and I read it. This is the only version I have to review now. And then I give that copy to any frontier model I want. And I ask, "Hey, can you help me think through this? Can you help me identify the assumptions that are most likely to break this plan before launch? Explain them to me clearly, and can you recommend a mitigation for me?" Right, this is the kind of work we like to do with our frontier models cuz it requires thoughtfulness. And look at what comes back. The model catches that the all-at-once warehouse migration and the ERP readiness assumption and the assumption that training will reduce throughput. They're all pretty big assumptions. They're load-bearing. It recommends staging the rollout, proving the integration before the first billing cycle, and building training time into the operating plan. Hey, these sound pretty sensible. This is why I built this. I don't want privacy to become a second project that cancels out the time AI was supposed to save. I want help separating the information the task needs from the information the file happens to contain, and then I want to get back to work. I want to get back to work. Now, why does this feel newly urgent? Sensitive documents and cloud software have both been around for a really long time. One, I think AI changed the amount of information we want to move. A couple of years ago, a normal AI interaction was a general question in an empty chatbot. Write the email explain the concept, give me 10 ideas. That was super normal in 2024. A lot of the useful work begins with your material. The the real detailed proposal you are actually sending, the contract you're actually negotiating, the meeting notes that nobody really organized, right? Or or the code base your team is actually trying to understand. This is a much bigger chunk of work. We've we've hundred x or a thousand x the kind of data that we can reasonably give to a model. And for work like this, the relevant context is exactly what makes the model useful. And that's why these files are so tempting to upload. Look, I get it. You want the model to do useful work, you have to give it a lot of context to do useful work, so you kind of need to put the docs in, but because you have 10 x or 100 x more docs, it's really hard to clean them all out. But along the way from 2024 to 2026, what happened to us? We we made intelligence almost frictionless, and then we handed all of us the job of deciding what can leave, where it can go, what has to remain for the answer to be useful. It's like we're all individually privacy filters on top of our other jobs. And nobody, including me, grew up with instincts for that. Word can hide old comments in places many of us don't look, right? We have retention, we have memory, we have enterprise logging, those are all different things. Yet we ask people to work it out when the upload button can save an hour. And then we put pressure on them to deliver faster. So no wonder the upload button is really tempting, right? I asked people in my community this week what they actually do around privacy, not what the policy says they should do. One person gave me an answer I cannot stop thinking about. I am relying on trust more than I'm comfortable admitting. That's a really honest answer. And this was not someone being casual, right? This is someone who has a team plan with training off, scoped connectors, and agents limited to development data. They're being really responsible, right? They're doing the things a sophisticated user is supposed to do. And still, the just don't paste anything sensitive rule has stopped being a realistic operating model. And I think that that's just true. Like at this point, asking someone to not do that is sort of malpractice because the models need so much data and our sensitive information is so intermixed. Someone who works in health care gave me the opposite answer in my community. The cost of one public incident involving patient information feels so high that his organization just mostly keeps all the valuable data away from AI. They use AI only around the edges where the information looks much more like every other industry. While the data that could support the most powerful work remains absolutely out of reach because it's just too risky. Think about those two answers. One careful person goes forward and relies partly on trust. Another careful person abstains. This is why I don't think another annual training course solves the problem. The benefit arrives immediately and the possible cost is delayed. It's uncertain. It's often invisible. Verizon saw this in its enterprise telemetry this year. The share of employees using an AI platform at least once every 15 days on a corporate device rose from 15% to 45%. And among those users 2/3 of them were accessing AI through non-company accounts. It's the shadow IT problem. In the data policy events Verizon observed involving outside systems, source code was the most common material submitted because again, there's that pressure to work and deliver more value. Now, you can read that as a story about irresponsible employees. I think that misses the more useful question here. Why is the unapproved route so much easier to find and use than the approved route? NIST has a very plain phrase for what happens next, security fatigue. When the same security decisions pile up, the easiest option starts to win. We already know how to build around that, right? Your phone asks about the camera when an app wants the camera, not randomly, right? Your browser handles the certificate check without asking you to become some kind of cryptographer first. We know that we can't expect users to carry that load in so many other parts of software, but AI has a lot of this backwards. We put astonishing intelligence behind an empty box and then put the privacy system in policy pages, in admin consoles, in document menus, in vendor contracts, and the user is expected to hold all of this in memory and somehow make the right decision. Do you always make the right decision? It's right? Like do you? Do I? How can we know? It lives in our memories. The obvious answer is redaction. Just remove the sensitive information. But the more I worked on building Airlock, the more I realized that redaction is easy if you don't care whether the model can still help you. It's real hard if you care whether the model can still help you. Because if you just say delete every name, every number, every date, every role, every relationship, every price, and every location, you can delete all of that and you can produce a wonderfully empty document. It will also be useless because the hard part is meaning making. Which facts make this task solvable and which facts only came attached for the ride and we can get rid of them. That is why when I demonstrated Airlock earlier in this video, I called out that you have to make some of those decisions. Take a contract. If you want AI to find renewal dates or unusual indemnity language or termination obligations, the model may need the clauses and the dates. It probably doesn't need the home addresses of the signatories, right? Negotiated prices, well, the model's going to need the numbers, right? There's no way around that. If you want to rewrite the cover email, maybe you don't need those numbers. It's about your intent. And I've said that a lot on this channel. It's about intent and understanding what we want to do with the models. Take a medical record. Sometimes the full history is the reason the analysis has value. Removing the sensitive information would remove the task. And in that case, Airlock, honestly, it's the wrong route. The work belongs in a governed environment built for the full record or it should not be involved with AI at all. This is why I keep coming back to the job. What are you asking the model to do? What is the minimum context that makes the answer useful? And once you know that, you can start making intelligent decisions about the file. The next time you open a document and you think AI could help, but I can't upload this file, begin with the job. What does the model actually need to see and where is that smaller copy allowed to go? You should not have to become a privacy engineer before lunch to get your work done. AI made intelligence frictionless. Intelligence needs information and safety has to live in the same path as convenience to make all of this work. So, that's why I made it. If you want to check it out, the link is below. Tell me what you think. Tell me how you're dealing with privacy. I'd love to see some privacy horror stories. Give me some privacy horror stories in the comments. And let's build something great together.
