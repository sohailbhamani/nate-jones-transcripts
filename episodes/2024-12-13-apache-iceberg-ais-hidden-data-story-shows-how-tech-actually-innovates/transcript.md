---
title: "Apache Iceberg: AI's Hidden Data Story Shows How Tech Actually Innovates"
video_id: "B-hhzEbKbiE"
youtube_url: "https://www.youtube.com/watch?v=B-hhzEbKbiE"
substack_url: null
publish_date: "2024-12-13"
duration: "6:32"
duration_seconds: 392
view_count: 1862
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
entities:
  companies:
    - "Amazon"
    - "Netflix"
    - "AWS"
    - "Azure"
  people:
    []
  products:
    - "Make"
    - "Projects"
  models:
    []
concepts:
  []
summary:
  []
keywords:
  - "ai-news"
  - "ai-tools"
  - "amazon"
  - "aws"
  - "azure"
  - "coding"
  - "frameworks"
  - "make"
  - "meta"
  - "microsoft"
  - "netflix"
  - "projects"
---

# Apache Iceberg: AI's Hidden Data Story Shows How Tech Actually Innovates

step into the time machine with me we're going to talk about something that happened way back in 2017 that ended up powering a lot of the way big corporations today are thinking about prepping their data for AI so there's an AI tie-in at the end here so in 2017 Netflix had a problem they had so many movies and shows and people were watching them so much that their traditional table structures and their traditional database were breaking down at the time databases work a lot like I think most me people's mental models of databases operate so just to explain that in detail they have rows they have tables you look up the row you look up the table it sits on a file somewhere it sits on a file on a server somewhere and there you go right now those kinds of databases do match what we imagine but they have problems at scale you cannot uh update them without shutting down the database imagine adding a column and having to shut down the entire database it's a problem uh they don't have versioning so you can't go back in time and see what the data was like before they don't have the ability to overwrite or edit necessarily in the same way they don't have they have performance issues because you have to look across the entire database there's not really a way to do it only partially I could go on there's a lot of issues some of them include storage and Netflix realized they needed to innovate they needed to fix they needed to make something that actually served their needs in 2017 and so what they came up with was what we now know as Iceberg and they developed it inhouse at Netflix in order to serve TVs and movies and shows effectively so all of us streaming contributed to Innovation isn't it's a nice feeling right uh and what they did was they converted the traditional model of the database and they moved it to the cloud and so it has um a core file storage Motion in the cloud like would sit Amazon S3 as an example uh Netflix would use AWS quite famously and it that meant it was infinitely extensible it didn't have to sit in just sort of uh traditional compute limitation it also meant that you could design it differently than a traditional database so it you could update it on the go it had metadata that you could query it did not have downtime if you dropped a column you could use lazy loading on the database which meant that you could pull only the part that you cared about at the time you didn't have to pull the whole thing which made it more performant there were a lot of advantages to Iceberg that essentially added up to Big Data works better here now Netflix could have kept that they could have said no no no this is ours like we don't want to share and our model of competition in Tech suggests that they would but our model is bad because big tech companies both compete and cooperate and in this case tools like this that are the foundational elements of the internet or that power our apps tend to be open sourced more often than not and so Netflix open- sourced it they actually handed it over to the Apache software Foundation which is the software foundation for projects like this they've been running since 1999 and by the time 2021 rolled around this little project that started at Netflix had been incubated by Apache and became a top level project at Apache which means that it uh was considered stable it was maintained by a rich community of developers Etc now you might wonder why what what possible gain would Netflix have to do this other than being nice and Netflix isn't necessarily known for that I can think of one if you are going to have a core part of your infrastructure that you have to maintain over time it would be smarter if you could build it in such a way that you knew that you could get talent in the door to maintain it and upgrade it and improve it over time now you could do that by training laboriously everyone who comes into your company on your special proprietary way of doing things but because this is a foundational part of the internet it makes more sense to just open source it your competitive Advantage is still your shows it's not your database and allow people who have learned it elsewhere to come to Netflix and practice their craft it's a talent advantage moving back Apache makes this a top level project you're still wondering where the AI connection is well it turns out they made it a top level project just before chat GPT exploded like a meteor on the scene and this was a perfect open-source solution to Major data Lakes which means that when all of these companies around the world began to ask themselves how do we collect our data and get it into a state where we can actually build AI models against it build AI models on top of it it was right there and so just like that it began to be adopted all over the industry data bricks has it snowflakes has it AWS has it Azure has it and all of these Cloud providers and uh data providers have figured out that they can use this open- Source tool developed by Netflix to help us with our scrolling and our movie watching to enable large scale data lak that companies around the world can leverage for AI deployments and I think that's a really cool story and if you look at that and you say wow that's that's kind of neat there are so many stories like that that have enabled the world we have today and they're not always viciously competitive like this one actually exemplifies cooperation even after Netflix turned over the software to Apache it took the work of hundreds of developers thousands of developers to mature The open- Source software so it was actually something that was stable enough for large scale deployments at these companies that's a big deal the developer Community is remarkably cooperative and I don't think we talk about it enough and I wanted to do a story that actually shows how that kind of cooperation unlocks capabilities that we are building against to this day so there you go that's the story of Iceberg and how it helped power the future future of AI through cooperation cheers
