---
title: "CrowdStrike Root Cause Doc: Breakdown of Lessons Learned"
video_id: "404cxJdCinA"
youtube_url: "https://www.youtube.com/watch?v=404cxJdCinA"
substack_url: null
publish_date: "2024-07-25"
duration: "6:49"
duration_seconds: 409
view_count: 191
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Deep Dive"
primary_topic: "AI Strategy"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Microsoft"
    - "Uber"
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
  - "deep-dives"
  - "frameworks"
  - "leadership"
  - "make"
  - "microsoft"
  - "product-management"
  - "uber"
---

# CrowdStrike Root Cause Doc: Breakdown of Lessons Learned

so crowd strikes error correction document dropped that means that they're looking into the root cause of what happened with the massive crowd strike failure last week and they're trying to understand what is the root cause and why I want to talk about the fact that there are some absolutely glaring issues that they are saying they are going to correct that should never ever have been there in the first place and I think that as I read into this more I am recognizing that we need to expect Chief technical officers at client companies to hold a higher standard when it comes to the kinds of software they're willing to deploy on their systems so we're going to go into six related issues I think you're going to see what I mean so number one crowd strike did not test on crowd strike production deployments I just want to take a minute for that they tested in a staging environment this is for something that is going to roll out globally and they they just stopped it testing and staging and apparently that was a normal thing and they say they're going to fix that they should never ever have been only testing for that kind of a change in staging I'll also add and and this is sort of a little bit to the defense of Chief technical officers or clients who obviously are super busy have a lot on their plates there's not really a structured way to evaluate these kinds of deployments on Windows machines and that's something Microsoft could take on as a fix for the ecosystem as a whole since so much of our Global infrastructure does rely on Windows how can we get better as a Tech Community at providing reliable third-party risk assessments of particular deploys I don't have an answer for that but it feels like an opportunity so the third thing I want to call out is crowd strike deployed fast they deployed simultaneously they did not have an option to roll back once there was a bug that bricked the machines or generated a blue screen of death and so that was a one-way door they were deploying in a one-way door Fashion on the assumption that either there would be no bug or they would always be able to roll back and that just isn't always a valid assumption because certain kinds of bugs do exactly what we saw last week where the machine is no longer updatable over the air but crowd strike never anticipated that apparently they never anticipated that kind of bug could exist which is all the more astonishing because their CEO previously had a very similar bug happen at McAfee this was back in I think 2010 and this is related to sort of a fourth issue I want to call out they had no Canary testing and they had no phased roll out that's kind of the correct remedy that's the best practice that you could use a canary test you're testing on a very small subsection of users in live environments this would have been caught rolled phase out is a little bit more in this context but at least you're rolling it out and not just assuming that it works for everybody at once by launching to the entire world and so a phased roll out you're sort of turning the dial up to half a percent of the total footprint then 1% if it works then 10% so you sort of roll it out and a canary test you're actually just saying here's 50 machines with crowd strike installed at actual customer locations let's see what happens I think both of those approaches would have caught this I think canar is probably slightly stronger and would have minimized the impact of the footprint regardless none of it was tried none of it was tried it was just like let's hit production right like let's go buy you only live once it's absolutely astonishing given what they were changing they should not have been able to write to colel and then change like that it's horrifying okay the the last thing I want to call the sixth thing is oh I guess it's no it's the fifth thing there will be a sixth thing losing track here so the fifth thing I want to call it is there's no control of deploy for clients typically if it's this important to deploy I would expect that CTO would be able to have some governance over how deploys are enacted they should be able to assess the risk to their systems and say for example I do not want to be in the first tranch of deployment I do not want want to be on the front wave of deployment this is a production system perhaps I'm the Delta CTO this is managing all of my flight Crew Scheduling I do not want to have this computer updated over the air when I'm not looking at it I want it updated after everything is validated after production testing has occurred at the end of your phased roll out and I want to make sure it's updated in a way I can predict so for example never push it on Fridays none of that optionality was available to clients that should be fixed the sixth thing now we're at the sixth thing I I cannot believe that I have to say this out loud there was no release noting going on they say they're going to add release notes everybody does release notes I do not understand how they got to be a company this big deploying fixes like this and just decided not to do release notes how no idea apparently they they're thinking about starting which is a good thing to do I want to leave you with an Easter egg here at the end so apparently and we're learning this from clients we're learning this from partners of crowd strike they decided that their apology to maintain client relationships after this globally impacting bug that grounded Airlines and severely impacted hospitals and all the rest of it is to send out and I am not making this up $10 Uber Eats gift cards but you think you you might be like pausing to laugh and like face pal there it gets worse they're $10 Uber Eats gift cards and clients and partners are saying they were impacted by Uber Eats grading these as fraudulent gift cards and so they can't even redeem their $10 gift cards that they got for this globally impacting outage I'll just leave you with that and I guess the Nugget is always always respect your clients and customers enough to think about what would happen if something you wrote actually caused a really severe bug for them otherwise you're going to end up in this boat there's a cultural issue at crowd strike and it needs to be addressed
