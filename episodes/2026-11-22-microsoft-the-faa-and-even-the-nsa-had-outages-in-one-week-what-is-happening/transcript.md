---
title: "Microsoft, The FAA And Even The NSA Had Outages In One Week. What Is Happening?"
video_id: "fFeyE4nINqs"
youtube_url: "https://www.youtube.com/watch?v=fFeyE4nINqs"
publish_date: "2026-11-22"
duration: "13:23"
duration_seconds: 803
view_count: 22199
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  AI cyber defense is now a race between attackers who can get deep access in as little as 15 minutes and defenders who need days or weeks to put systems back. The past week's outages at Microsoft, the FAA, several banks and the NSA show how hard repair is, and why AI-assisted attacks make it harder.
  
  Full post:
  https://natesnewsletter.substack.com/p/ai-cyber-defense-business?utm_source=youtube&utm_medium=video&utm_campaign=ai-cyber-defense-business-launch&utm_content=description
  
  Nate's Library MCP (every prompt kit and guide, inside the AI you already use):
  https://unlock-ai.natebjones.com/guides/how-to-connect-nates-library?utm_source=youtube&utm_medium=video&utm_campaign=ai-cyber-defense-business-launch&utm_content=description
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/?utm_source=youtube&utm_medium=video&utm_campaign=ai-cyber-defense-business-launch&utm_content=description
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  System outages are exposing the fragility of our digital infrastructure. Learn how recovery efforts can trigger cascading failures.
  
  Recent disruptions affecting Microsoft services and banking reveal a dangerous trend: engineering teams are struggling to defend against AI-speed attacks. When initial fixes fail, the recovery process itself can worsen the situation, leading to prolonged downtime across critical networks.
  
  This breakdown covers the progression from a single scam email to the deployment of millions of autonomous agents. We examine why modern automation surface vulnerabilities create such high-stakes risks for global logistics and what engineers must change to prevent these cascading failures in the future.
  
  In this video, I share the inside scoop on why cyber defense is harder than cyber attack:
  - Why Microsoft's recovery traffic took down its own healthy servers
  - How AI agent frameworks like ARTEX shrink the team an attack needs
  - What ConnectWise shows about cutting off access versus restoring it
  - Why the first step in patching Java is finding every copy
  
  For operators and business leaders, AI speeds up defense too, but how long you stay down depends on knowing what you run and how to bring it back.
  
  Chapters:
  
  00:00 When the fix makes things worse
  00:52 A week of outages, from Microsoft to the NSA
  01:42 Why one bank problem shows up everywhere
  02:59 Why attackers get the better deal
  04:02 What ARTEX is and why it matters
  05:34 Fifteen minutes to break in, weeks to restore
  07:05 Finding every copy of Java
  08:01 Why cyber defense is harder than attack
  08:40 When Microsoft's repair didn't take
  09:20 Who's defending the internet
  10:48 Three takeaways
  12:54 What you can do now
  
  Subscribe for weekly AI strategy breakdowns, and comment whether you think these system outages are a sign of a permanent shift in digital security.
  
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
  - "cybersecurity"
  - "AI cyber defense"
  - "Microsoft outage"
  - "ARTEX"
  - "ConnectWise breach"
  - "Java vulnerability"
  - "AI agents"
  - "AI cyber attacks"
  - "why everything is going down"
  - "cyber defense for business"
  - "system outages"
  - "digital infrastructure"
  - "AI-speed attacks"
  - "automation surface"
  - "cascading failures"


# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Google"
    - "Microsoft"
    - "Vercel"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  - "All of that firepower is deployed against just finding any given vulnerability, any one vulnerability in an incredibly complex system"
summary:
  - "# Microsoft, The FAA And Even The NSA Had Outages In One Week"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "career"
  - "coding"
  - "frameworks"
  - "google"
  - "make"
  - "microsoft"
  - "vercel"
  - "workflows"
---

# Microsoft, The FAA And Even The NSA Had Outages In One Week. What Is Happening?

Email, flights, banks, even the NSA had trouble this week. Microsoft needed nearly a day to restore email. Microsoft sent traffic to healthy servers during the recovery process and that extra traffic took those servers down too. Now we're asking engineers to defend against attackers moving at AI speed, but what strikes me is how fast can you safely act when your last fix just made things worse? That's what happened with Microsoft. Google has documented attackers using the open source artex framework gaining deep access to a company system in 15 minutes. That's the dichotomy. That is part of why things are so hard right now. So we're going to talk about what happened, how we can understand it as part of the new information wars, and what we can do to prepare for a safer internet. Let's get into it. So on Thursday, Microsoft email started failing. A lot of people thought early weekend, right? Ahead of GTA 6. Friday, the FAA stopped departures nationwide. That was less fun. On Monday, customers at several banks were waiting for their money. United had a computer problem of its own and researchers found malicious code turning up on all kinds of news organizations from the BBC to CNN and hundreds of others. By Tuesday, iCloud and App Store were having trouble. Then the NSA, a hyper secure network, said part of its internal network was down and that happened for at least two days. Some of those incidents really were connected, but not quite in the way people have said. A lot of people have hypothesized we have one big attack that's happening over and over again. The evidence is more nuanced than that and I think it tells a more important story about where we are in cyber defense in 2026. Here's an example though of how these incidents do start to connect and drive entanglements. The folks looking at dots and connecting them, they're not entirely wrong. If you have a problem at Chase as we had this week, it can absolutely show up as unaccountable problems a lot of other places. I to have like a lot of personal experience in money payment rails because I used to work in Fintech. Fintech is basically the story of stitching a nice-looking web page across a bunch of very very old systems and software that move money around. And so part of the problem, one of the things I'm emphasizing here is that we are in a position where our systems are very complex to the point where trying to dramatically change them generates really big risks. But also trying to defend them is getting exponentially harder in the age of cyber attacks. We're in a bad spot either way. And in many ways, the simplest thing we can do is scale up AI model intelligence on the cyber defense side as a way of more rapidly patching our vulnerabilities. We built an internet that can move money and route planes and deliver email and let hundreds and hundreds of companies work together really smoothly. In many ways, we think that internet just works, but it's quite fragile. When something goes wrong, it can take a lot longer to understand what happened than it can take an attacker to do lots. That's what I mean by information complexity. And it gets especially expensive when someone else can take advantage of the time you spend sorting it out. And so right now, that's what cyber attackers are doing. An attacker gets a really good deal in this environment. They have to understand just of enough of a system to find something that they can use as an in. They have a lot more tools at their disposal with AI. Some of the attackers in the Binance hack actually created an entire fake company to interview engineers at the company in order to get them to upload a particular assignment from a work computer and download a particular response and in that way infect their work computers. That is how sophisticated attackers are getting. And fundamentally, all of that firepower is deployed against just finding any given vulnerability, any one vulnerability in an incredibly complex system. And that's why our text Artex is an open-source attack harness that went viral. Software that's built to coordinate AI agents is being used specifically to coordinate them for attack purposes. Microsoft documented a China-aligned group using it to automate parts of attacks targeting hundreds and hundreds of organizations in the last few months. The FBI issued a warning about it on Friday, the same day the FAA stopped departures. And by then, the developer had decided things were getting too hot and taken down the original repository, but people had copies all over the internet. It's not going away. Now, we've had automated attacks before AI. You could send a scam email to a million people and come back tomorrow and kind of see who replied. But the problem is we have been able to scale up the full automation surface. So it's not just sending a million emails anymore. It's being able to coordinate hundreds or thousands of AI agents, finding vulnerabilities, putting vulnerabilities together, building attack profiles, and then going after those websites. And what that means is a really sophisticated nation-state attack that would have required hundreds of people three or four years ago could now plausibly require one or two people. Just as we have started to get excited about being in a world where we can have a one-person billion-dollar company, we are now unfortunately living in a world where that same firepower is being directed against the incredibly complex and valuable enterprise systems that sustain the internet. Google measured one Artex-linked actor going from first compromised account to deep access inside a company in 4 hours, and in one case, in as little as 15 minutes. Hours or minutes, like this is very fast. Microsoft separately documented the use of Artex in the compromise of ConnectWise, which provides cloud backups. And ConnectWise published exactly what its defenders did so we can follow their work from the inside. This is also all recent, right? At 7:00 in the morning on October 17th, ConnectWise disabled seven application identities and revoked credentials because it had detected an attack. Those identities were how the backup service acted inside its own customers Microsoft 365 environments. Cutting that access was something that the provider could do centrally, but restoring it was really, really hard. And so in October 19th, the company completely reset all of its accounts and credentials in the affected environment. And then they were still not done. Here on October 28th, it was still trying to figure out how to bring partners back online. The internet is much harder to repair and build than it is to break. To resume backups and restores, partners had to authorize the replacement application separately for every single Microsoft 365 customer environment. So revoking seven identities to stop a cyber attack initiated by Artex took one decision. Putting everything back took weeks and lots of coordination. And that's a relatively small company in the scale of the internet. Now scale that out to a flaw in software that thousands of institutions can run. During this particular week with all the outages, the US Cyber Agency urged organizations to patch the serious problem in Java right away. Now Java is everywhere. And its first instruction was to find all the places that had Java. Come on, guys. Java can be bundled inside applications, inside equipment. It may never show up under its own name in a software inventory. For equipment that bundles Java, the team may need its own supplier to confirm what's installed before it can even begin to finish the first step in the job. That's what I mean by we're patching the world at once. The discovery is happening of vulnerabilities all at the same time right now for 25 years of of software work. The work of getting that fixed into service is happening all at once. This is why Bank of America is hiring so many contractors to figure out how to fix vulnerabilities. It was in the news. And so I don't want you to take away that we're not using models for cyber defense. I want you to take away the idea that defense is harder than cyber attack and using models to put together defensive positions, defensive profiles, defensive repair, defensive discovery, defensive inventory. It's much faster with models, but it's still much much harder and more difficult because the systems are so complex than attacking is. And patching itself, the fix that we deploy, that can leave systems vulnerable too, not because they're vulnerable to a bug per se, but because they don't come back the way we expect because they're so complex. Microsoft experienced that when it was trying to repair from the latent bug that it had sleeping for 3 months or so in its systems that ended up causing the outage for email and everybody else this prior Thursday. Now, to be clear, Microsoft has not disclosed that this was an Artex initiated attack or even an AI attack of any kind. And they took hours and hours partly because they kept having trouble rolling back onto their servers. The fixes did not take the way they wanted them to. And the internet really is real physical servers somewhere, guys. It is hard to bring them back online. It is difficult to repair even when the repair is correct. The other thing we're seeing that's a pattern is this arms rush for cyber defense. And that's a really good thing. If you're looking for hope, that's an example of hope. People are competing to find ways to make the internet safer. And we saw it on display in the Optimizedly attack this week because malicious code could reach card details typed directly into affected pages in theory. But what we found is that when a payment provider hosted the card field separately, the browser kept those details out of reach. In other words, browser security methods, browser security engineers, people at Mozilla, people who are building browsers like Chrome figured out what are the common attack vectors regardless of the website. And that happened to be a good design that kept people safe. The point here is that we are a position where we see organizations like Cloudflare or Vercel or folks building browsers acting to defend the internet because they end up being the fronts for a lot of traffic. And that's something I deeply appreciate. The engineers at those organizations are doing really important work because they're not just defending their own company's surfaces. They acknowledge that they have a surface that touches so much more the internet and they're using that power wisely. They're using it to put in place good preventative rules that make it safer for people to browse the web and that reduce the impact of attacks like this. So what can we take away from all of this? Number one, please understand that the internet is real servers built by real engineers who are having to put together bug fixes in record time for decades and decades and decades of software issues that normally we never would have caught. And AI has made catching them easy. So you have to understand that the engineers are having to do all of like 20 30 years of bugs in a few months. Two, fixing those systems is really really hard because we've made them so complex to sustain the internet we have. That goes for banks, it goes for email, it goes for the flight logs that the FAA tracks, it goes for the NSA. Any of these systems we're talking about, they're incredibly complicated, much more complicated than they seem. They have a simple surface and the rails underneath are really really really hard to understand, measure, build, patch, and put back together. Number three, understand that attack is easier than defense and that is part of the inherent information asymmetry that we have right now. And that is part of why defenders need good cyber defense built by AI, powered by AI that helps them make sense of patterns quickly, that helps them figure out how to put things back quickly. Imagine a world in 2027 where instead of Microsoft grinding through, figuring out that their servers weren't going to be able to come online the way they wanted to, they could run that simulation in ultra fast mode, discover the servers knocking over, and then figure out how to do it another way, which is ultimately what they had to do. They just had to live through it in real time. It could have cut the outage by hours and hours and hours and ironically given us email back sooner, which not everyone would have been happy about. But that's my point. Like those kinds of worlds where we can simulate cyber defense activities, where we can understand the full implications. They're coming, but they're going to come a few months after the cyber attack comes. It's just a harder problem. And so we're going to need to live through this bumpy world together. Make sure you have a good password manager. Obviously have a safe word with your family. I've said this repeatedly. Make sure you have a good prep kit. These are just basic things that we need to do anyway and it's extra important right now because we depend on the internet and the internet is more vulnerable than ever. We're going to get through it. It's going to be okay. We're going to have a much more secure internet at the end, but we have to get through this bumpy period first where we patch all these bugs. All right, I'll see you next time.
