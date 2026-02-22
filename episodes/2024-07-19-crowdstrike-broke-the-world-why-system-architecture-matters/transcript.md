---
title: "Crowdstrike broke the world: why system architecture matters"
video_id: "DxH3jtsqbtg"
youtube_url: "https://www.youtube.com/watch?v=DxH3jtsqbtg"
substack_url: null
publish_date: "2024-07-19"
duration: "8:51"
duration_seconds: 531
view_count: 1700
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Strategy"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    []
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
  - "ai-news"
  - "ai-tools"
  - "coding"
  - "frameworks"
  - "leadership"
  - "make"
  - "workflows"
---

# Crowdstrike broke the world: why system architecture matters

I want to talk about the inherent vulnerabilities of the way we've constructed our computer networks today it's a nerdy topic but you all are going to care about it because the world just broke because of this issue so crowd strike is a global security company and cyber security in particular and their whole mission statement their whole goal is to protect the fleets of computers that they are installed on by making sure that malware doesn't run on them that hackers can't get access to them uh they also do monitoring of employees which is a lot more controversial and I just want to take a minute for the fact that it's this company it is this company that released a Sy content update that then bricked every computer they're installed on and that is a massive number worldwide they are a big company they're $83 billion company traded on the stock market or they were uh and they released a Content update that was so defective Airlines ground to Halt hospitals were affected in the Netherlands all three major US airlines for the first time that I think I can recall were grounded by a tech error at the same time so American Delta United all down airports from Zurich to Melbourne to Amsterdam were all down hospitals in Illinois were having trouble because their 911 system was down Catalonia was having trouble getting Health updates so these are actually serious issues right like on the one hand like it's easy to chuckle and say wow they really messed up but people's lives are affected because we all have come to depend on Computing so much and that's kind of what I want to talk about here we have an opportunity to think about the way we architect our security response protocols the way we architect our expectations for security fixes because at the end of the day what crowd strike sold was a oneandone piece of Mind solution to chief executive officers hey I know that you worry at night about being on the front page of the newspaper tomorrow because of some sort of Cyber attack we will protect you from this trust us we're the ones that have been you know investigating uh North Korean hacking attempts for the last decade were the ones that have been called in by the US government to investigate in other situations don't worry we're the ones who are responsible here right like we're the we're the grown-ups and we can protect you and if you're a CEO and you don't know a ton about the details of the Tech you it's an easy line to buy right it sounds like it's responsible they're a publicly traded company so you invest and so many of our IT solutions are purchased on that basis and then they come and install this client software on all of these machines and you you've now introduced a common point of failure across all of your machines in the name of security and therefore your entire ability to sustain your business is indirectly linked to this security company and you've done it because you're so worried about cyber attacks but if you think about it what just happened with this blue screen of death affecting hundreds of millions of computers worldwide was worse than a most cyber attacks it was worse this is what Y2K was supposed to be like I remember back in 1999 at midnight on December 31st everyone thought this is what was going to happen all of our machines were going to turn to the blue screen of death and we weren't able to get anything done and because of heroic efforts from a lot of intrepid programmers that did not happen but that's because we saw it coming and you can't see a defective bug in a Content file coming it's just human people are going to make mistakes and the problem is we built a system where a single human I guarantee it's one engineer somewhere can make a mistake and shut down hundreds of millions of machines worldwide and there will be a lot of CEOs that are thinking about their security deployments as a result because this is a terrifying amount of corporate vulnerability one of the other things that I want to call out is that at the end of the day when these things happen or if these things happen we also have to get better at how we handle the the systemic implications of distributed systems because what they're having to do they can't push the update the machines won't take it they're having to tell it managers responsible for these individual fleets to go through a four-step process that essentially involves reinstalling the channel file that had the bad content update this Sy file and so all of these it managers individually around the world who are responsible for fleets of machines are having to go through the same four-step process to fix their machines and I love the it departments I've worked with they're absolute Heroes they're having an awful day today but it's also not fair to them to impose a globally distributed system and then force them to be the local front lines for that system when something breaks like that is fundamentally not the way the system should be designed and we need to revisit our assumption around security architecture we need to think about what it takes to have a more resilient system where a Content file like that could be fixed from a central point where a Content file like that could be fixed before it reaches deployment and that's a different conversation I don't want to get too far into that today but from a technical perspective the first thing I think about is how you prevent these things in future and I think it's about systems design I don't think that we can fix it by saying we're going to have good intentions and we're just not going to do it again which is basically what Crow Drake is is saying it's like well this is this is you know this was a normal update it was just one little aberration easy fix available off you go well it's kind of underselling the impact of what they did to the world today and we owe it to ourselves as people who work in Tech to think about and design our system so that they are more resilient and less susceptible to the kinds of globally systemic crashes that could be attributable to a single person making mistake it's it's just not sustainable for us because we're human we're going to make mistakes and if you think the answer is AI or llm generated code that's really buggy too that's that's not the answer here uh I've messed around with LM generated code and it it produces bugs so much uh so it's a little aside but the point is there's not an easy fix with AI there there so rarely is a magic one fix with AI and this is another case where that's not not true we actually have to think about the systems architecture of what we're deploying and we have to think about our business models and our expectations like as leaders in corporations we need to be insistent that we do a degree of due diligence on the solutions we deploy not just in terms of whether the company is professional but whether the company is able to design systems that are actually resilient and that level of due diligence is rarely done so much due diligence I see basically amounts to is this a legitimate company do they have lots of policies written I guarantee you crowd strike had lots of policies that did not save them they actually needed to build resilient Technical Solutions and nobody apparently had been checking them that they would do that and that's really the core issue you shouldn't be buying a client software that installs on all of your machines if you don't have confidence that they're going to be able to actually build a resilient system and I realize that's an easy thing to say and a hard thing to do because you have to buy your software from somewhere you can't just go and not have cyber security software if you have a significant Fleet of computers you need it somewhere there's relatively few providers and so it's not it's not necessarily an easy thing to go out and change tomorrow it's something that the whole Community has to come together and think about and I guess that's my challenge how do we think about building more resilient systems so that's where I'll leave it uh I hope you get over your blue screen of death soon if that's you um and if not spare a thought for the it managers who are absolutely suffering today
