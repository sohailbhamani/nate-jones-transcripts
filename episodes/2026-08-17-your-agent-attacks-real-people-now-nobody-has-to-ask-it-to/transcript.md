---
title: "Your Agent Attacks Real People Now. Nobody Has To Ask It To."
video_id: "4f5AJrJPilM"
youtube_url: "https://www.youtube.com/watch?v=4f5AJrJPilM"
publish_date: "2026-08-17"
duration: "21:05"
duration_seconds: 1265
view_count: 3968
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  AI agent security just got real: a booking agent broke a live system, and poisoned agent skills cleared 1.7 million installs. Here's what actually happened, and how to secure the agents you run.
  
  My Links 🔗
  👉🏻 Newsletter: https://natesnewsletter.substack.com/
  👉🏻 X: https://x.com/natebjones
  👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening when AI agents start acting inside other people's software?
  
  The common story is that an agent has to go rogue before it hurts anyone, but the real question is what an ordinary goal does when it meets an unlocked door.
  
  In this video, I share the inside scoop on the agent security incidents that are starting to connect:
  
  - Why a gym-booking agent canceled a stranger's reservation nobody asked it to touch
  - How a clean, approved skill turns malicious weeks after you install it
  - What the AI Security Institute found across 122 evaluation runs
  - Where swarm attacks start, and the two jobs you now own
  
  Agents are still worth running, but the people who do it well decide up front what theirs can touch and how fast they can stop it.
  
  Chapters:
  00:00 nobody in that sentence is an attacker
  00:32 the melbourne agent that booked a gym class
  01:43 zenity labs and 1.7 million poisoned installs
  03:16 how a clean link turns malicious weeks later
  04:31 the scanners were live and it cleared anyway
  05:10 your agent does not share your social conventions
  06:17 the web is now more than half agents
  07:02 the skill that cleared every security scanner
  09:56 the frontier model case is different
  12:33 why swarm attacks come next
  14:40 your two jobs, identity and scope
  17:02 five questions before you run an agent
  
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
  - "AI agent security"
  - "agent skills"
  - "Claude Code"
  - "OpenClaw"
  - "Zenity Labs"
  - "AI Security Institute"
  - "swarm attacks"
  - "agent permissions"
  - "how to secure AI agents"
  - "AI agent attacks explained"
  - "agentic AI risk"



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Agents"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
  - "Founders"
entities:
  companies:
    - "Google"
    - "Nvidia"
    - "GitHub"
    - "Vercel"
    - "Hugging Face"
    - "Cursor"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Cursor"
    - "Hugging Face"
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "One unlocked API call, one person asking a completely reasonable question, and a stranger loses her gym class and never finds out why"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "claude-code"
  - "coding"
  - "cursor"
  - "frameworks"
  - "github"
  - "google"
  - "hugging-face"
  - "make"
  - "nvidia"
  - "tutorials"
  - "vercel"
---

# Your Agent Attacks Real People Now. Nobody Has To Ask It To.

One unlocked API call, one person asking a completely reasonable question, and a stranger loses her gym class and never finds out why. Nobody in that sentence is an attacker. That's the whole problem, and it's why an agent does not have to turn against its owner to become your attacker. And that should scare you. Today, I'm going to talk to you about the three or four major stories in AI security that are all coming together, the implication for swarm attacks in the next few months, and what you can do to stay safe. A man in Melbourne asked his AI agent to book him a gym class. It booked the class. It also broke the booking system, canceled the stranger's reservation, and moved him up the list. He never asked for that. An agent doesn't have to turn against its owner to become your attacker. Now, here's the detail that matter. First, it worked out how to book him weeks further ahead than the gym allowed, and then it went back in and found out that it could cancel a reservation without anybody checking. So, it decided to test that on a real person. It canceled the booking of the person sitting first on the wait list and moved the the owner of the open claw from fourth to third. Now, this is a responsible person, and he said, "Please undo the damage." And it came back to him with bad news, "Can't put it back." Now, before we go further, the company that is responsible for the booking software have said they don't discuss security matters, and they will not confirm whether or not this was fixed. But, you should care even if you don't have an open claw and you're not worried about gym membership, and you think it's just a funny story. Because multiple other disclosures around AI attacks have landed in the same stretch of days, and they say the same thing. Start with Black Hat, August 6th. Zenity Labs disclosed a campaign of poisoned agent skills. One family of them cleared more than 1.7 million aggregate installs by August 2nd. And Zenity is really explicit that those installs, they don't even know how many people they affected. Like, you can't count installs for people, and so that's scarier to me cuz you don't know how many people were actually affected. If you use Claude code or cursor or open claw, you've seen skills. A skill is a folder, and every one of them has a file at the center called skill.markdown. That file tells the agent what the skill does and what steps to follow. We all use them all the time in tech. That folder, though, can carry scripts, it can carry reference material, it can carry links to documentation somewhere else on the internet. Hold on to that last part because that's the key to this attack. Because when you put a poisoned link into a skill.markdown file, you get a lot of advantages as an attacker. Because the skill is already inside an agent with a given permission and authority to act, the skill is not something that may have been individually checked by the user, although you should be checking your skills, especially after I tell you this. And the poisoned link can therefore give instructions to the agent from an external source that you never intended to give the agent. And a poisoned link can therefore give instructions to the agent that you never intended. And what's even worse is that an external link can be changed at any time. In this case with the Xzenity attack, the link sat there for weeks building installs and building trust, and it was genuinely innocent at that time. The link pointed nowhere harmful. And then the attackers changed the setup instructions, and the new instructions told the agent to download and run code from a server they controlled. That code went hunting for SSH keys, for cloud credentials, for get tokens, and there's a there's sort of a longer list, right? Your agent ended up being the delivery mechanism because your skill got poisoned, and at the time you downloaded it, it was innocent. This is why you really have to be careful who you get your skills from. Getting skills from random people is sort of like getting random zip drives and sticking it into your laptop in the early 2000s. It's sketchy. What Zenity found is that more than 30% of the dangerous skills they identified were abusing Claude code and open Claude in exactly this way. And what's even scarier is that you might never know you were attacked. There's no warning screen, there's no ransom. It just extracts the credentials and it exfiltrates them and it takes them over to the attacker's servers and you would never know. It doesn't help if you already installed the skill. The copy would still be on your machine and deleting a listing somewhere doesn't revoke the fact that your key got stolen, right? And what's even scarier to me is that Vercel had automated security audits running on that same registry since February. It had three scanning vendors, more than 60,000 skills, audit results published on every single skill page, warnings before install. And that was all live. Like it was Vercel was trying to be a good citizen here. And this campaign ran underneath that security infrastructure from July 11th to August 2nd and it cleared 1.7 million installs anyway. An agent does not have to turn against its owner to become your attacker. It only has to trust the wrong page and then your own agent can become your own attacker. You say move me up the list and you assume a whole set of social conventions, right? Don't break into anything. Don't hurt another customer. Don't test a vulnerability on a real human being. You're a good citizen. Your agent might not be a good citizen because all your agent sees is a goal, a tool, an endpoint that accepts a command. It doesn't see your rules. It doesn't see your social conventions. You never gave it a sense of the social conventions, so it just doesn't understand them. Agents are only as aligned as we are and less so because agents don't understand some of the implicit guardrails in society that guide our alignment. So now in that world, imagine someone malicious hands one a malicious goal. That's the one we all think about. That's scary. Now imagine someone careless hands their agent an ambiguous goal. That's even scarier to me because the lack of intent allows the agent to drop all of those assumed social conventions, to drop any of the rules that we might assume for ordinary and healthy execution and the agent is just free to pursue an ambiguous goal. Now in the gym story, the agent didn't invent the vulnerability it found, right? It didn't hack into the software, change the code and say now there's a vulnerability. It just found a door somebody left unlocked and walked through it in software terms. And that is also something that should worry you because most web security still assume a human is coming through the front door and most humans aren't good at computers. But the web is now more than half agents and agents are very very good at computers. It's where they live. And so they are checking every single door in the software. Every single one, including ones you didn't know were there. So every week authorization check on the internet just got a much larger population of things capable of finding it. Including the one sitting behind your own products. An agent security company called AIR published research. Two of their researchers built a working skill in under an hour that promised to generate a branded landing page using Google's Stitch design tool. And and the skill actually worked, right? They submitted it to GitHub marketplace. Maintainers reviewed it, they merged it in. Then AIR advertised it on Instagram and targeted marketers, designers, sales people. And then they ran it through their scanners. So basically what they did was they got the skill under the wider internet. They got it merged into a repo that was reputable and well-maintained and very popular. They advertised that that repo and that skill. And then after that, they ran the install through popular security scanners. And AIR says they ran the skill against Cisco scanner, Nvidia scanner, and every scanner on skills.sh, and all of them cleared that skill. Those scanners did not miss malware. At the moment they ran, the skill was clean. There was nothing bad in the file. The malicious part was on a web page the file pointed to. The skill said it needed startup docs for the Stitch SDK, and sent the agent to an address that researchers controlled. That page served legitimate documentation right up until it didn't. And then they changed it, and the new page told the agent to download and run a script. The agent had already been told that the address was trusted, so it treated the new instructions as part of the job. AIR says the skill reached more than 26,000 agents. The thing that I noticed is that we are starting to get a common attack pattern. Both of the attack patterns I've described here are patterns where you can poison a skill and turn the skill into something toxic after it's previously been declared safe. The good news is, if you have a common attack pattern, you can start to design security perimeters that guard against that. You can start to isolate and call out any skill that has an external link. You can start to scan those links every single day. There's all sorts of things we can do now that we understand that's a common attack factor. It doesn't remove the larger risk, which is agents are able to follow instructions, and once they're told follow instructions, they tend to do so very consistently. That is the root behind everything I've talked about, from the gym membership to Zenity to this AIR story. They're all about the agent following instructions, but doing so in a way that is ultimately misaligned to society. Now, the Mythos 5 story, which I talked about in the UK Security Institute study last week, that is a little bit different. That is a case where, yes, the agent followed instructions, but in this case, the guardrails were off and the instructions were malicious. And so, in this situation, we have a case where you could actually have what I would describe as the movie version of a misaligned agent. The evil henchman says, you know, "Dear agent, do something evil in the world." And the agent goes off and does the evil thing. Now, let me jump over to the AI Security Institute report. I covered this last Monday. And I want to summarize what it means for us in the wider context of agent attacks. So, AISI ran one cyber evaluation 122 times across seven different frontier models. Internet access was deliberately turned on. The developers' cyber classifiers were deliberately off. Those are not conditions you get from public versions of the model. In most of the runs stayed inside the test. But 10 of those runs produced 19 unsanctioned actions and it included attacks against real people and real organizations, which I covered last Monday. Now, this is where it starts to get interesting, scary, and more like that bad movie that we all don't want to be in. Because in all the other stories I've told you so far, agents are not necessarily misaligned from a malicious perspective. All they're doing is trying to get their work done. In this story, the mythos story, what made it scary is that the agent deliberately targeted the human. It started to pressure the human. It started to create fake human credentials. It tried to attack the human and socially engineer them to accept malicious code in the repository. That is really scary. That is something that you don't want to see. And it does show that as these models get more and more and more capable at the frontier, they are going to be capable, if you can get the guardrails off, of some very scary things. I think that leads us to two main threat vectors, right? I think the frontier model threat vector is the one that we all stay up at night worrying about, and we should. And there are people who are working to make sure that the guardrails stay on. The people who have the guardrails off have appropriate controls and use it for cyber defense. And that if the guardrails were off and models were to attack, our software would still be safer because we've scanned it for vulnerabilities. Those are all good precautions to take. For the rest of us, the story this week has been about this second case, the the misaligned by accident case, the gym membership case. Which I think unfortunately is going to be a lot more common and a lot more damaging to us on most days. Because really, even in a case where you were hacked and and the skill was poisoned, that your agent didn't mean to attack you. Your agent was just following instructions. It's not a malicious act at all. Now, the hackers are malicious, absolutely. But they're just taking advantage of the fact that the agent just wants to follow instructions and if there aren't guardrails yet around links and skills that ensure that these things are protected. I think that we are likely going to see swarm attacks of agents coming and I think those attacks are going to move across several vectors at once. And I say swarm attacks on purpose because if you think about it, agents are designed to collaborate. We see evidence of collaboration with the hugging face incident. We see all of the individual pieces in place for agents to start to take action against their owners. And they already have demonstrated that in the wild. All you have to do is put those ingredients together and you get a successful swarm attack where a swarm of agents can be told to coordinate from various people's individual computers to do something that any individual agent doesn't view as malicious, but the collective is very dangerous. This would not be one agent making a lot of calls. It's more like multiple different agents and their actions compound together and there may be some guidance from a hacker somewhere or a hacker's agent somewhere in the process that kind of shapes where the swarm moves. That's a very different kind of cyber threat. It's not very easy to predict because agents are non-deterministic. And it doesn't require a shared master plan. There's no one computer to shut off. And once all the elements I've described connect, the agent swarm can actually do a whole lot of damage on the wider internet, right? Because you have the pathway for stealing credentials. Well, now that agents can get into things, which is exactly what we've already seen that they can do. Now, once they can get into things, they can establish a base there and attack other companies. We've already seen them do that. That was part of the hugging face attack. Now, once they do that, they can start to leave messages for each other in those boards and start to propagate and start to get their skills poisoned out into other repos and start to actually get more agents to come and help. And that's something that we've seen in pieces with the skill poisoning that we saw in this story. All of this can happen and the people involved may not know. They may not know that their agents are participating in any of this. You may not know where your token burn is going, right? Your agent may just have a skill and suddenly you're like, "Wow, what is this agent doing?" That is a world that we are like 1 2 3 months away from. This is coming up right now. Ultimately, it means that you and I, we now have two jobs. We have to keep our own agents inside acceptable boundaries. And we have to make sure our systems survive agents operated by people that we will never meet. And And tip number one here is identity and authority. Give every agent you run its own identity instead of handing it your credentials. And so, what I mean by that is use tokens that expire, scope each one to the exact system and action the task needs. Your design agent does not need your SSH keys. Your research agent does not need your deploy rights. And the agent booking the gym class, well, in this case, what you should have done is give it a better prompt. You should have said, "These are the norms that I expect when you interact with external software. I do not want you to look for vulnerabilities to get your work done. That alone would have helped a lot. All we're trying to do here is limit the scope the agent has. And the things I described, if they sound really technical, it probably means you're not doing them. You don't have SSH keys to hand over if you're not a technical person. Uh and so in that sense, simplest things you can do is just not don't download random skills on the internet from people you don't know. It's as old as time, right? You download a file from someone you don't know, it turns out to be poisoned, and now you're in trouble. And so, there's some really basic stuff that I think we need to sort of teach and socialize as part of digital hygiene that even non-technical people can use, and I think it's going to be really important. Because agents are going to be everywhere. And if we don't know how to use responsible rules of the road with our personal agents, we're going to end up metaphorically driving a bunch of car crashes. And if you're in IT, you should build the stop button before you need the stop button. You should be able to kill the agent, cut the network, disable every child it spawned, revoke the credentials, and keep the record of what happened, and know which of your systems were touched. In other words, you need to build a stop all agents button if you're in IT, because you want the option to shut down a particular agent at any time and say, "This is bad. I'm stopping it right now." Make sure if you are setting up agents, you're setting up your systems, there's going to be a bunch of excitement about it, but make sure that ability to pull the rip cord and say, "No, we're done." Make sure that you have that in case the agent goes off the rails, so you limit the damage. It's just a responsible infosec thing, and I think it's going to be part of standard deployments for agents very, very soon. Now, I want to make this very simple. If you're running an agent at home, it should come down to five questions for you. What identity is your agent using? What can it read or change? Who can give it instructions? Can it delegate? Can it open accounts? Can it contact people without asking you? And if it starts doing something strange, are you going to see it in time? And can you actually stop it? If you can't answer these, you should not be handing your agent a bunch of information. You shouldn't be handing your agent anything. You shouldn't be driving an agent right now. An agent is sort of like you got to pass a driver's test, right? You have to be able to responsibly tell the agent what it can do and not do because it's much more powerful than a traditional piece of software. And I'm excited for agents. The larger question still matter to answer. You should know what your agent is doing. You should know what it has access to. If you don't, you're going to regret it. You just are. And your neighbors may regret it, too. And that's why I started with the gym story. One of the things we are going to see with irresponsible agent owners is we're going to see accidental prompting that has vague instructions lead to real-world consequences for a lot of us because someone's agent was misinformed. It's going to be like the 21st century version of the email reply all chain that would just spam through companies in the 1990s where someone would reply all and not realizing they were reply all and they take down the entire email server. It's going to be very, very similar, but it's going to have more widespread and difficult to manage social consequences cuz there's so much that runs on software and so much of that software is not properly maintained because everyone thinks humans aren't that good at code and so we can fix things that are way, way below the level of core internet functionality that are just like the home gym membership software. It doesn't have to be super secure. It just has to have your name down. And it'll be fine approximately. Nothing that is fine approximately will be fine. The agents will find it. So, make sure that you take managing your software seriously no matter what tier or level of software you're at. If you're in infosec, make sure you build that stop button. Make sure that you take identity and permissioning extremely seriously for your agents. Make sure you have replayability. You have to have all of this stuff built in because if you don't, you're going to regret it. Ultimately, the world is going to come down to a few frontier agents that may have malicious intent or be directed by malicious actors. That's the mythos story and a whole bunch of undirected, possibly swarm attacked agents who are part of our ordinary daily lives. They're They may be our agents on our computers and they may be part of these larger attacks. The latter is the one that we're not talking about enough and it concerns me because the stories I'm telling you connect through the shape of a swarm. They connect because you can start to see all the pieces of a swarm attack there. I think we're going to see more swarm attacks in the next few months and I think that that is going to impose a rapidly escalating requirement for zero vulnerabilities in software on on all of our systems. And we need to get ready for that. We cannot assume that is not coming. And we have to do our part to make sure our agents are not a part of that story by securing them with really common sense rules, which is exactly what I described in this video. In a sense, I had to make this video because if I didn't make this video, it would be irresponsible for me to not make it. I had to make it because I want you and your agents to not be a part of that world. I don't want your agent to be a part of an attack swarm. I don't want your agent to be accidentally implicated in breaking someone else's software. We need to be responsible owners of our agents. That's the expectation. So, you tell me in the comments what you're doing to secure your agent. You tell me maybe the horror stories from agents that you've seen go wrong or things that you've seen go bad with agents and we'll all learn together.
