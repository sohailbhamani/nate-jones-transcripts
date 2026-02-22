---
title: "Open AI o1: The Strawberry AI Reasoning Revolution + 3 Specific prompts and example responses"
video_id: "oQrSoXg5Q4I"
youtube_url: "https://www.youtube.com/watch?v=oQrSoXg5Q4I"
substack_url: null
publish_date: "2024-09-13"
duration: "9:01"
duration_seconds: 541
view_count: 1007
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Cursor"
  people:
    []
  products:
    - "Claude"
    - "Cursor"
    - "Make"
    - "o1"
  models:
    - "o1"
concepts:
  []
summary:
  []
keywords:
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "cursor"
  - "frameworks"
  - "leadership"
  - "make"
  - "o1"
  - "openai"
  - "product-management"
  - "prompting"
---

# Open AI o1: The Strawberry AI Reasoning Revolution + 3 Specific prompts and example responses

it's been less than 24 hours since Chad GPT dropped their new strawberry model or more precisely a preview of what will be their new strawberry model they had been rumoring this for October and lo and behold on September 12th they dropped the 01 model they really have to get better at naming these things and it's available in two forms in apps if you're on the Mac or in the web app preview as well it's 01 preview it's also mini which is supposed to be faster at reasoning both of them are focused heavily on reasoning they are touting the benefits of 01 for things like really hard math problems which I got to tell you I do not do a lot of at work so apparently International math Olympiad problems which I bet I couldn't solve uh it can solve 83% of the time whereas chat GPT 40 only gets a 133% score maybe that's more like me I don't know I haven't taken a math Olympiad problem in a little bit um so that's the basic idea it does a lot of reasoning I think the architecture underneath is part of what makes that model feel so different if you've worked with it at all you can feel when you talk to it how different it is so what's happening under the hood is that they have taken the idea of token completion and added a time element to it and they actually include charts that talk about this as they release the model and so fundamentally what happens is that the model goes back and automatically does that Chain of Thought work that you were taught to tell the llm to do if you were studying prompting so remember how up to yesterday you had to tell large language models explain yourself think thoughtfully I think the last time I did that with Claude was yesterday like it's just what you do if you want a very careful precise thoughtful answer you no longer have to do that with strawberry with the 01 model it just does it automatically and it does it because it takes time to answer and it's not just time to go back and like retrieve something that matches out of a vectorized uh training set and come back with a feature that that aligns I'm I'm assuming you know what a feature is a feature is a feature inside a neural network and it goes back and matches against it in the traditional llm and then it comes back out and there's the output that's not how this works fundamentally there's an extra step in there that takes time and they're giving it elastic time to work with and that's a huge ad Advantage long term because it can choose to take more time to answer your response it's not trying to go as fast as it can it can choose to take time for inferring and what it what open AI says is that it's actually doing reasoning during that time and so there's this New Concept called reasoning tokens which are hidden from the user most of the time and you have to put them in your max token limit and it will use the reasoning tokens to solve problems and then discard them before giving you back your output and so open AI has chosen not to make that reasoning visible to the user I supect it helps because it's a closed model and they want to keep it closed and they want to keep it proprietary they don't want to explain exactly how they're doing the reasoning this is a significant breakthrough anyway regardless they keep the reasoning out of view and they discard the tokens and then they put a response in front of you but in my experience playing with this they still explain their work so so the model still tells you what it did it just doesn't give you the granular detail of the reasoning that it technically could if it actually threw the reasoning output at you and so it will give you a summary let me give you an example I asked the model to calculate the number of people who work in Tech who also like Legos just for fun just to see like what it would do with it and it would require it like thinking through in order like what assumptions to use what population estimates to use what percentage estimates to use for people who like playing with Legos as adults and it came back and generated an entire response apparently there are uh a few million of us at least according to that estimate two and a half million people anyway um and when it came back and sort of revealed the estimate it did describe in plain English the way it had thought through things it just did so at a very high level so it did things like say this is a rounded estimate this is what I think based on Census Data like it talked a little bit about how it was inferring I could see that again when I gave it a different challenge I gave it a challenge of looking at 50 assorted job titles and only based on those job titles determine the average salary of the job titles in the sample right so if you have 50 assorted job titles that's the only information you get what is the average salary that would take a human hours perhaps days at least hours it did it in I want to say 20 seconds and it showed its reasoning so it basically went through and it built a table and it went through and fetched a reputable source for job title information out of its training set I don't think it's connected to the internet yet and it listed this is the salary on average that I get for each of these job titles and it showed its work so I could see and check it and like I put CEO in there and the CEO salary was very low uh so it's not perfect but it gave me an estimate and then it walked me back through and then it did an average and the average is actually the average and that is something that when you're just doing next token prediction you are not doing math and so one of the notorious problems with mathematics with traditional llms is they're just predicting the next token and so they can predict the next token incorrectly and there's no way for them to sort of catch that internally and now it's reasoning and now it's thinking with those reasoning tokens and and is checking its work I don't know how they did that either it took a team of like 60 people at open AI to figure this out over the course of a year it's a massive achievement this is the first model that has really broken through the gp4 class barrier now here's the thing it's not perfect it is still slower than the other models and it's intended to be slower in fact it's kind of a badge of honor to make it think for a while because it means you gave it a hard problem it has a token it has a rate limit for asking questions so it's like what 20 30 questions a week so this is not going to be your everyday model it's very much in preview mode because it's computationally expensive but to be honest with you how often am I facing problems that are this complex for example I fed it a pricing structure question that I've been having I got a novel response back I don't know that I entirely like the response but it actually laid out a pricing structure in great detail in response to a detail prompt from me about a tough B2B SAS pricing problem and it gave me a really reasonable response it gave me something new to think about I don't really need to go back and ask it again about that because that's a problem that is sort of a need to think about it need to go back and have some conversations it's not a rush answer and I think there's going to be more of those kinds of questions and so I'm not sure in practice how much the question limit matters to a user in the wild now if you're testing it it's going to drive you nuts uh because you're going to run into it right away and that brings me to my last point which is that we are already at a point where we have these sort of raggedy edged models that are super super good at certain things and we have to figure out what we're using them for and that's sort of on us it comes back to this idea of intelligence allocation if I want to do text work I don't know that I'm going to this model to do text work I might stick with Claud Sonet if I want to do multi-step reasoning I'm absolutely using the 01 and if I want to describe basic concepts very quickly jet GPT 40 is going to be really useful you have to get a feel for these models by playing with them to figure out what they're actually going to be good at and that's on us it's on us to try it's on us to figure out I'm really curious what are you using the 01 model for I haven't even touched on the coding side I did get it to write a little bit of code for me it was extremely fast it was clear it is not it is really bothering me after repet after cursor it's not have this thing working in a development environment uh inside the app I know you can call it in there like obviously you can get the API for 01 preview I think that's in beta now and so it's going to be in development environment soon but if you're just trying to sort of code in the browser and it throws a code snippet at you like it's just not the best experience so I'm sure we'll get that solved right it'll get an API we'll get that in what are you using it for what do you think what did I miss about strawberry strawberry is here all right cheers
