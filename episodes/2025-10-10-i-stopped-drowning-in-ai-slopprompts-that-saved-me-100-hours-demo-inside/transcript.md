---
title: "I Stopped Drowning in AI Slop—Prompts That Saved Me 100+ Hours (Demo Inside)"
video_id: "rY6MOdXv02M"
youtube_url: "https://www.youtube.com/watch?v=rY6MOdXv02M"
substack_url: "https://natesnewsletter.substack.com/p/i-built-a-20-prompt-set-to-kill-ai?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true"
publish_date: "2025-10-10"
duration: "12:10"
duration_seconds: 730
view_count: 8673
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI slop"
  - "LLM quality"
  - "prompt engineering"
  - "AI strategy"
  - "automation at work"
  - "large language models"
  - "Claude"
  - "GPT-5"
  - "AI content"
  - "AI writing quality"
  - "PRD evaluation"
  - "marketing copy"
  - "AI agents"
  - "AI feedback loops"
  - "business automation"
  - "AI for managers"
  - "quality control with AI"
  - "AI workflow design"
  - "AI strategy for teams"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "Career"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Stripe"
    - "Lovable"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Make"
    - "Artifacts"
  models:
    []
concepts:
  []
summary:
  - "# I Stopped Drowning in AI Slop—Prompts That Saved Me 100+ Hours (Demo Inside)

We have a supply explosion of AI content and it is an AI slop issue across every business I talk to"
keywords:
  - "ai-tools"
  - "anthropic"
  - "artifacts"
  - "career"
  - "claude"
  - "claude-code"
  - "coding"
  - "leadership"
  - "lovable"
  - "make"
  - "product-management"
  - "prompting"
  - "stripe"
  - "tutorials"
---

# I Stopped Drowning in AI Slop—Prompts That Saved Me 100+ Hours (Demo Inside)

We have a supply explosion of AI content and it is an AI slop issue across every business I talk to. Every single one, they're like, "What do we do with AI slop?" We have product managers producing PRDs that are not good. We have marketers who are producing marketing copy and it's not good. But we managers or frankly any individual who wants to know they're actually writing well with AI, we don't know what to do. How do we know that what we're shipping is good quality? It's not about did the AI help. We're past that point. The AI is helping. It is about is the quality output good and we humans don't have the time to assess all of it because AI is so good at producing it. So we are in a world now where marketers have gone from can I write a blog post today to I could stamp out 50 and now you have to ask yourself can I assess the 50 that have been produced? Are they actually good? Are they brand aligned? Is the content right? Etc. And you know what people are doing for that? they're using their eyes or they're skipping it because there hasn't really been a good quality gate. But that's fixable. And what I want to tell you about is how I'm fixing it. So it is really simple. What you need to do is adopt the mindset that LLM attention is going to be the predominant attention mode in your business and everybody else's business going forward. You want to make sure you use that to your advantage. So if you think about a world where in your organization you have only so many human eyeballs but you have nearly infinite AI eyeballs. Well use the AI eyeballs to your advantage and get them to check the work. But it's not as simple as you know as saying please check this. Is it good? Right? Like I've seen people do that and you get widely varying results. It depends on the AI you're using. Is it chat GPT? Is it clot? Etc. It also depends on what the LLM already thinks of as good based on its training data and maybe it's past conversations with you. It's not predictable. And so we need to get to a point where we have much more robust prompting for quality. Think of it this way. A lot of what I talk about is robust prompting for what we would call the supply side. Robust prompting to make your work that you produce better. So I've talked about Excel in the past. I've written up guides for that. PowerPoint, etc. Talked about claude code. But what about the other side? What about the filter side? The side where you need to test work and see is it good? Maybe it's your own work. Maybe it's someone else's work. Maybe you're a manager and you're testing your team's work and you could get like a 100 blog posts in today from two or three team members and you don't have time to go through it. You'd be up all night. Well, that's where the prompt comes in. That's where you can get help. or you're an engineer and you're looking at this explosion of lovable vibecoded, you know, prototypes or PRDs that are coming from PMs and you don't know whether it's good. Again, a prompt can help fix it. I think specifics are really useful here. So, in a moment, I'm actually going to go through a real prompt with you that I wrote for this and I'm going to explain how it works. And I I I'm going to do several of these, right? This is very much a case where the attention filter, the quality filter needs to be per use case and per job family or else it's not any good. Like you need to have one that is PRD specific, that is blog post specific because otherwise you don't have enough context to effectively ask the AI to help filter for you. And your goal should be to have the AI do most of the reading to do what Andre Carpathy has suggested which is to have LLMs be 98% of our attention and the human eyes have the 2% attention that matters. And so I want to give you the right 2% the highest quality pieces and effectively filter out the slop. That's my goal. Like if you are in a world where you have a 100 blog posts what are the two that matter? What are the two that are super high quality that you should surface now? That's super valuable information. But where is the PRD that is really well thought through? That is promotable information. Like if a PM is able to do that with AI, they should be on a promotion track. And you want to know that quickly. So that's what I'm setting out to do. How do I do it? Let me show you a sample prompt and we'll work through it together. Okay, here we are. Right on the prompt. We set the RO first. You're evaluating a product requirements document and your job is to determine if an engineering team can build this without needing three clarifying meetings. I love that specificity. You obviously could flip it around and like change it a bit. But what I want to be frank about in this prompt is how painful the current version is because whether it's three clarifying meetings for for PRDS or whether it is I can't tell which blog post to post or whether it is I don't know which of these customer email drafts or I can't tell which of these sales uh reachout drafts or I don't know about the webinar uh invite and the webinar event schedule. All of them you were having meetings. You were having human conversations. you were putting human eyeballs on them if they don't work. So let's set the stakes and then I define the axes. This is this gets very specific to the PRD and that is the point, right? So we ask about the completeness of the document. And by the way, this is somewhat scalable. You can ask about completeness of other artifacts too. In this case, we can ask about acceptance criteria. We can ask about whether edge cases are present. We can ask about whether non- goals are explicit or implicit. We can ask about sort of whether we and we can extend this, right? Like if I wanted to add to this, I could say, do we have at least seven requirements clearly enumerated? That's a bit of a random number. I chose not to include it here, but if you have a particular format for a particular artifact, it's easy to modify and add that in. And then I give right in right in the prompt, I give a score rubric, right? Like a five score looks like a measurable edge case documented non-goals prevention. It's a good score, right? A zero is it's untestable, right? It has a vague statement. And I have seen this as a PM. I have seen other people write really vague goals and it's just terrible and we all know it's bad. And by the way, I think the AI slop conversation is somewhat overhyped because I remember seeing phrases like this long before AI. In a sense, what we complain about as AI slop is the latest version at volume of a larger issue, which is that we have always had bad work problems and sloppy work problems. And now maybe now we have the tools to address it regardless of who wrote it. I don't care if AI wrote it. I care if it's good. So then we go down to the next one. Is it testable? So this is a very PRD specific thing, but you can do something similar with other types of documents. So, for example, you could ask if it's readable for a sales follow-up email, right? Does it read at an eighth grade level would be a reasonable test to have? And you can go through and sort of define that. And I've done that, right? Like this is not the only prompt I have. I have a bunch of prompts for different goals. My goal is to give you a complete pack that gives you a filter that you can apply to various business functions. And so again, we have the scoring, we have test cases, success rates, failure states, example inputs and outputs. This ensures that it's actually testable. Scope clarity. Uh this is another example of something that is PRD specific. We have our scoring. You can imagine how this can be somewhat different. If it's uh a customer announcement email that you're sending for a new product, uh you can ask if the product is clearly explained. The point here, and the reason I'm pulling in these examples from across the business, is because this is how many different places the AI slot problem touches. Everywhere I look, there's a slot problem. and we need to have a filter and that's why I was like you know what we're just going to write some prompts and make it easy decision framework key choices is the rationale explained or the trade-offs acknowledged etc very prd specific and then we get into scoring right so we go through these five right we have dependency mapping at the end there and we have an elements check is everything here and then we give it an output and what I want with this output that look I am not someone who's going to tell you JSON is magic JSON is not magic but it is certainly useful in cases where you want the LLM them to understand a particular rubric and output schema and follow it. In this case, what we really want is we want to understand a grading score. And so we want to be able to say based on these scores, how do we write this in plain English? And then how do we write a key sentence that someone can use as feedback? And this is where the magic lies, right? Because it's no good if you just can go through the elements at the top here and say, "Oh, this is bad." Right? Like, okay, it scored zero or it scored one. What you want to do is go through and say what is the actionable feedback someone can take and actually cycle through and sophisticated writers will be able to pull this JSON and feed it into an LLM along with the draft and get very actionable feedback for how to improve and use AI to actually power better writing higher quality writing and come back. And so I think that this is the beginning of a really interesting feedback loop to actually build an anti-slot machine at work. And so we have for each of these we have specific actionable feedback that we're specifying as an example. And then we have thresholds which you can you know what which you can be specific about right you can say I accept a three or overall or more or a 4.8 8 or whatever, right? But you have a score, you have a revise, accept, reject, and you have feedback. And really, isn't that all we need? We need someone who can say, "You've got to specify the Stripe API because if you don't specify the version, engineering is going to have to come back." And it's not that hard. Specify the most recent API version, but just be clear about it. That is the kind of feedback that LLMs are very good at providing if properly prompted, but that humans are stuck with providing now because we haven't had prompts to fix it. and that's why I built this. So there you go. I think slop is a fixable problem. I don't think it can be fixed with one magic bullet. There's not one magic prompt for this. Nor do I think just instituting this as a filter is the only way to fix it. I do think I've written lots of prompts for this. You have to write better too. But let's assume because every organization I've met has this problem. Let's assume you have an AI slot problem. Great. Safe assumption. How do you filter? That's what this is about. How do you make sure that you can use AI as a weapon in your favor so that you focus your attention where it matters so you scale useful feedback? And I think walking through this prompt structure should be helpful for you to understand this is how we think about grading a piece of work in context. And you'll notice I don't need to know a ton about your organization to do this. I can just assess the gates and say, "Okay, well, I think that from a good best practice PRD perspective, this is probably weaker." And the nice thing about a prompt is you can tweak it and say, "Okay, well, we're not an API business, right? Like maybe that's not what we care about. We care about front end." Okay, well, you can you can adjust that pretty quickly. You can have the same degree of specificity and it works. So, my challenge to you is this. Assume you live in a world where 2% of human attention matters and you need to put it in the right place. Find the mechanisms in your business. Find the mechanisms in your workflow that enable you to put that 2% attention where it matters. This is one of those. This is one of those that helps you to weed out AI slop. This is so much more useful than the deceptive AI detector stuff because the AI detector pretends that if you can detect AI, which they can't, then you will stop slop. But slop has always been a problem. We humans have produced poor quality work. As I've been saying, I've seen bad quality PRDs for a long time before AI. Well, this is really about raising the quality bar. We don't care how you wrote it. We care that you're accountable to raising the quality bar. And then this becomes a really useful feedback tool for yourself, for your manager, for whoever to improve the quality of the outputs. And so I'm putting together a complete prompt pack for different business purposes. So you get a sense of how this works for marketing, for CS, for sales, for product, etc. for engineering. And that's the goal, right? The goal is to give you a starter on a filter gate so you can put your attention where it matters and you stop drowning in the slot. It's a vlog.
