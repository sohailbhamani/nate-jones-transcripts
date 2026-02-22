---
title: "Why CrowdStrike Really Happened (Time Machine to 2009 Edition)"
video_id: "uQez89MMuE4"
youtube_url: "https://www.youtube.com/watch?v=uQez89MMuE4"
substack_url: null
publish_date: "2024-08-02"
duration: "9:11"
duration_seconds: 551
view_count: 944
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "Microsoft"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  []
keywords:
  - "ai-tools"
  - "career"
  - "frameworks"
  - "google"
  - "leadership"
  - "make"
  - "microsoft"
  - "workflows"
---

# Why CrowdStrike Really Happened (Time Machine to 2009 Edition)

so it's been a couple of weeks since the crowd strike issue the airlines are flying again I want to talk about what happened and why but not necessarily from a technical perspective I actually want to talk about what happened in why from a risk management perspective so it's going to be sort of a step back and we are going to go back in time all the way to 2009 so stay tuned the first thing I want to call out is that when we make software choices like this when companies purchase crowd strike we are making social choices not just rational actor software choices and that really matters when you're talking about something like security because getting security right if you were the cioo or CTO of a major airline or a hospital or a major utility or whatever it was that is a choice that could get you fired and you always are aware of it when you're making that decision and as much as people uh have come into my comments saying hey this is really something where the CTO or the CIO did not do enough due diligence I actually want to push back this is not really a function of due diligence because before the outage that happened this was the premier solution crowd strike was the solution that a responsible CTO or CIO would choose in order to make sure that they were doing the right thing and be perceived as doing the right thing in their job it it is social because if you're going to your CEO and you're presenting this is our security solution you want to be presenting something where the CEO can talk to his buddies at the golf course and they're like oh yeah crowd strike it's good like that's fine and if you think I'm making that up that is actually how a lot of it works that is actually how a lot of those decisions get made and so yes you can come up with three PowerPoint bullets from crowd strike that make it really easy to pick crowd strike absolutely you can put a rational case together if you're a CIO or a CTO super easy in fact there's lots of cases to be made just by reading the crowd strike website the crowd strike sales rep is happy to help you like there's it's a very easy set of cases to make if you were to pick anything else in the industry before the outage the CEO would ask you lots of questions they would want to be sure why are we not going with crowd strike I Googled and crowd strike is the industry leader I checked linkston and crowd strike is something that all of my friends are using as CEOs why not crowd strike and so it's a socially driven choice and that means that we converge onto particular solutions that are socially approved whether or not the actual risk profile is managed and that's going to be a theme as we see so the first piece is that software choices are social choices and that works that in the seite in ways that drive convergence regardless of risk the second point point is that risk is not effectively managed by existing audit mechanisms so that's a fairly technical phrase so let me break it up fundamentally an audit process is run off of a particular imagined risk profile it's a linear process and Auditors like to work against that linear process they have a way of doing things if they are used to auditing your Tech solution as they were with crowd strike it is a much simpler audit process you the CTO or CIO go through less pain the auditor goes through less pain because everybody has done this before and so the auditor comes in and says ah yes I've seen crowd strike this is what we do with crowd strike if you do other Solutions it's not the same thing they open up the big book right they have to go through their process again the auditor is vaguely annoyed you the CTO or CIO probably have more work it is a non-trivial difference simply because crowd strike was more familiar to Auditors and again that isn't actually speaking about their risk it's just saying that the auditor had a set of processes they were familiar with running they had a set of checks that they were familiar with running they had a set of shorthand that they had developed around this company because they'd seen it installed so many times the software installed so many times across technical Footprints at major companies and so there's an incumbency advantage that goes with that there's a sense of we're here we're here to stay we're the responsible actor and you see it in a lot of regulated Industries where effectively the governmental audit process or the governmental regulatory process anoints a market leader regardless of whether that market leader has actually dealt with the real risks underneath the hood and we saw with crowd strike that wasn't actually true they hadn't actually addressed the risks that's the second takeaway is that fundamentally audits don't really do risk if the imagined risk model is static and if it's applied in a way that sort of uses a shorthand for a market leader and that's typically what happens the third thing I want to call out is that our imagined risk model is something that we have a really hard time handling as a species over a long period of time and I'm going to give you this is where we go back in time in the early 2000s Microsoft had a long running antitrust case with the European Union and they finally settled in 2009 and one of the things they agreed to is that security companies could have the same access to the Microsoft kernel as Microsoft did this bug came from the kernel access that the EU pushed Microsoft to Grant to security companies and the reason why this happened fundamentally is that the EU could not imagine a world where a security company would be not necessarily a bad actor but an incompetent actor there was an imagined risk model of the world that didn't match the real risk model and so externalities happened after the settlement that nobody anticipated the EU thought you know what if we give security companies access to the colonel we're going to make for a fair less monopolistic world and security companies have grown and thrived in that environment but it's also opened up risks that we all have to live with and it is one of the root causes that led to the outage now it's not as simple as saying well the EU shouldn't have regulated it because if you listen to the earlier conversation here the one of the the earlier points around sort of audits and how audits tend to annoint Market leaders governmental action that drives monopolistic tendencies in these kinds of security or regulated environments can also accelerate risk and so part of the problem here is that we have auditory action that increased concentration of risk on this vulnerable player in the system crowd strike and so there's this sort of monopolistic Gathering of of risk of customer trust around this one company driven by governmental action and audits at this the same time governmental action designed to decrease monopolistic Tendencies by giving other companies access to the Microsoft kernel was another root cause of this whole mess it is really really hard for people who are trying to understand and design laws regulations audit practices best practices around Market participation it's hard for them to anticipate longterm longtail externality so in other words if it's a longtail externality it is something that has a very small percentage chance of happening but if it happens it's going to be a big deal and it will not happen over a determinate period of time the ruling came down in 2009 and here we are in 2024 and all of a sudden there's been a massive outage and Delta has reported $500 million in uh costs associated with this bug and there's many other players right Del just reported it I I want to call that out because this is not about blaming a particular player it's about understanding how the players work together so that we can figure out how to drisk these systems better we need audit systems that actually match to real risk models we need regulatory systems that do a better job imagining worst case scenarios over the long term we also need social dynamics DCS in the SE Suite that reward people for critical thinking those three things would have made a big difference on the crowd strike bug what else do you think is a root cause here that I didn't talk about
