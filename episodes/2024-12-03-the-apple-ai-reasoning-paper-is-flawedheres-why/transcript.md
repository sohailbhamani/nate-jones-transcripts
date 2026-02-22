---
title: "The Apple AI Reasoning Paper is Flawed—Here's Why"
video_id: "Ahtx-Lo1Oa0"
youtube_url: "https://www.youtube.com/watch?v=Ahtx-Lo1Oa0"
substack_url: null
publish_date: "2024-12-03"
duration: "6:46"
duration_seconds: 406
view_count: 2061
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Executives"
entities:
  companies:
    - "Apple"
    - "YouTube"
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
  - "apple"
  - "career"
  - "frameworks"
  - "leadership"
  - "make"
  - "prompting"
  - "workflows"
  - "youtube"
---

# The Apple AI Reasoning Paper is Flawed—Here's Why

we need to take a few minutes to talk about what good benchmarks and bad benchmarks look like because I am so tired of seeing people in my comments on Tik Tok on YouTube other places trying to argue for the Apple reasoning paper and I've been avoiding talking about it not because I don't want to but because I generally don't like to do takedowns but here we are we're going to do a takeown of the Apple paper on AI reasoning and why I think it's fundamentally flawed and I want to give some credit where it's due Andrew M wrote an incredible blog post articulating some of the flaws in the paper and I want to give him credit he's done a fantastic job calling it out and I want us to reset the bar around what the Stanford study really called for when they asked us to think about as a community what are some benchmarks and tests that would be good for AI to try and hit that AI isn't good at yet this apple benchmark around reasoning is not one of them even though they say it is so GSM symbolic is The Benchmark that Apple proposed in their paper and too long didn't read essentially what they're saying is large language models cannot reason because if you give them symbolic shifts in the problem space that are fairly nuanced and fairly small you get dramatically different outputs which suggest that they can't read through what we would call in human terms a trick question well Apple's researchers took that perspective they ran the test they saw that large language models are bad at this and their conclusion was there's really only one option here which is that the llm is just doing vectorization and pattern matching and there's no reasoning whatsoever going on it doesn't the parallel pathing we all talk about at inference isn't producing value and net net there is no novel reasoning going on here because if there was because their argument was that the AI would be able to reason through the small symbolic differences and nuances the trick questions and get it right well Apple was wrong and the reason why Apple was wrong is because the AI can get it right it just needs to be reminded that it's looking for a little bit of maybe a trick question and if you say oh that's giving the AI too much help I disagree with you and here is why at the end of the day you are measuring two things not one thing which is always a mark of a bad Benchmark when you use the GSM symbolic the GSM symbolic yes it it measures logical reasoning I agree with apple there it also measures naiv it measures whether the large language model is used to being tricked and if you have ever used a large language model you know their entire personality the entire train training process that they go through is all about Earnest questions and Earnest answers they are so helpful in fact one of the real weaknesses they have is it's really hard for them to say no to you when they should and so if you're training a large language model to be incredibly helpful it would make sense that it would assume any question it was asked was actually not a trick question it was an Earnest question asked in good faith and that seems to be what llms are cried for unless you tell them otherwise and so credit to Andrew he went in and he basically said let me take the GSM symbolic data set and let me tweak it not by changing the problems not by asking the AI to solve an easier problem but by giving a prompt at the top that basically says Hey warning sign watch out AI there may or may not be a little weirdness going on in this question and I'm paraphrasing but that's the basic idea he put up a verbal warning sign with line at the top of the prompt basically saying watch out there may be some oddness with this prompt think about it carefully and all of a sudden performance improved by 90% if you can improve performance by 90% by changing one line of the prompt and saying hey watch out and suddenly the AI can magically see through all the trick questions and can reason correctly you don't have a benchmark you have flawed data and a bad paper it's just not correct the evidence we have is actually adding up in favor of AI reasoning and I think that if we're going to demand better benchmarks which Stanford is correct to do and I do appreciate the Apple researchers for attempting to put one together it's a ton of work to produce a paper I don't want to sort of demean or disregard the work that they did it moves the field forward I just think you need to be careful at what you're measuring and you need to measure not just naive but also the ability to reason directly and maybe maybe we should start less skeptically because I think at this point the burden of proof is really on the Skeptics it's not on the people propounding AI reasoning there is enough evidence that AI is doing some kind of reasoning that you have a higher burden of proof or you should have a higher burden of proof If if you want to say the other way and one of the implicit methodology flaws in the paper is it basically assumes AI doesn't reason unless proven otherwise and I actually think that given the year we've had that's incorrect that is not an empirically based assessment of the reality on the ground instead the correct frame is to say empirically speaking AI does appear to reason and we should be thinking about how we can more effectively understand what reasoning looks like and by the way if you're wondering is it really reasoning is it just the appearance of reasoning I would like to say most humans only use the appearance of reasoning I rarely hear tight coherent cogent reasoning in most human conversations or frankly in most human writing if that is the bar then most of us are going to fail it too and so I think in a sense the simplest answer using aam's razor is the easiest if it walks like a duck and it talks like a duck it's a duck if it looks like a reasoning and it acts like it's reasoning and you can write a little prompt that says hey watch out this might be a trick question and suddenly it reasons it's probably reasoning and that's why I think apple is incorrect and I think AI can reason sound off in the comments let me know what you think
