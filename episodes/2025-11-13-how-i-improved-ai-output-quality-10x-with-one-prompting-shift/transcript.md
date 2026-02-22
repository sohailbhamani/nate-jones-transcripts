---
title: "How I Improved AI Output Quality 10X With One Prompting Shift"
video_id: "XfcZujr426o"
youtube_url: "https://www.youtube.com/watch?v=XfcZujr426o"
substack_url: "https://natesnewsletter.substack.com/p/goldilocks-prompting-10x-your-prompt?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true"
publish_date: "2025-11-13"
duration: "12:21"
duration_seconds: 741
view_count: 17596
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI strategy"
  - "prompt engineering"
  - "Goldilocks prompting"
  - "large language models"
  - "Claude"
  - "GPT-5"
  - "Gemini"
  - "Anthropic"
  - "OpenAI"
  - "context engineering"
  - "system prompts"
  - "newsletter example"
  - "model creativity"
  - "prompt templates"
  - "AI workflow design"
  - "AI strategy for teams"
  - "effective prompting"
  - "AI prompting techniques"



# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "Prompting"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "Anthropic"
  people:
    []
  products:
    - "Claude"
    - "Gemini"
    - "Make"
  models:
    - "Gemini"
concepts:
  []
summary:
  - "# How I Improved AI Output Quality 10X With One Prompting Shift

We're gonna talk about Goldilocks prompting"
keywords:
  - "ai-tools"
  - "anthropic"
  - "claude"
  - "coding"
  - "frameworks"
  - "gemini"
  - "make"
  - "microsoft"
  - "prompting"
  - "tutorials"
---

# How I Improved AI Output Quality 10X With One Prompting Shift

We're gonna talk about Goldilocks prompting. So, Goldilocks prompting is the idea that you can prompt too much and you can prompt too little. I know that might sound funny to some of you because I'm the guy who does the prompts and people think I'm known for these long prompts. I am here to help you prompt more effectively. And I want to remind you that there is an optimal level of clarity for the goals that you set out to accomplish with the model. And you can be over clear, you can be over long. And so we're going to talk about Goldilocks prompting and why it makes such a difference. I'm actually going to show you an example of the incredible improvement in model output quality that you can get when you actually use Goldilocks prompting. What is Goldilocks prompting? Very simply, it is giving the model enough context so it doesn't assume stuff about you that isn't true and the problem. and then giving the model enough guidelines that it knows the direction to go in. It also includes giving it like clarity on what tools it can or should use etc. It is not exhaustively listing every single thing you want done. So if you're making a PowerPoint for example, you could say I want you to make the font exactly this. I want you to make every single slide exactly in this way with this headline size with this layout with this particular bullet style with each of these individual bullets in exactly this text. Here's the pie chart that goes on slide seven. You get the idea. Or you could say, "Make me a PowerPoint. Make it good. The board's going to be looking at it." We would probably not do that one, but we might be tempted to do the make it specific. And one of the things that I've been thinking about a lot as I've wrestled with prompting and context engineering over the past couple of months, call it longer than that really. There is an optimal level of detail and there's a tradeoff involved. If you want to give the model as much clarity as I described where you're describing every minute detail, the model will go there, especially the newer ones. It will increase the token burn so you're more likely to run into memory issues. it will reduce the creativity because you're not engaging the creative circuits, for lack of a better term, of your model. So, it's a trade-off. You have to decide, do you want to be so specific that the model's going to burn through a lot of context and follow your exact design and maybe that's not what you want. Maybe it is. Or do you want to back off and give a more general purpose ask that allows the model to be a little more creative and might be more token efficient. In my experience, 20% of the time you do want that level of specificity. you you're like, "This is going to be a lot, but I need it to be exactly like this. Don't mess it up." And about 80% of the time, you want to prompt at the right altitude. You want a Goldilocks prompt. That is actually tougher than it looks. It's really, really tough to prompt at the right altitude because it's so tempting to either overescribe or underdescribe. I want to give you some tools to help with that. And I think one of the things I can do to help is just to give you a visual example of what good looks like in terms of a prompt. This is directly from Anthropic. I didn't make this one up. They put it out in public on their context engineering blog. I thought it was really helpful. I'll just pop it up and then we'll keep going and I'll get to the demo I created shortly. All right. Here we are. This is the system prompt example that Claude is showing us for good, bad, and ugly. So good is here, bad is here, and ugly is here. Basically, if you have the right level of detail, Claude is going to understand the role it has. I'll just zoom this in for you. Claude understands the role it has. It understands the tools it can call. It understands how it can respond, and it understands the guidelines. And now we're done. This is all for like Claude's bakery. It's a nice madeup example. Uh, this is really bad. So, this is just a very short prompt and it doesn't give Claude anything that it can do to actually be effective in its role. There's no shared context that Claude can invoke here. And this I'm going to call this one ugly because it's so specific. Here's an exhaustive list of cases. Here's the user intent. This this prompt is trying to do everything. This prompt might actually be six or eight prompts in a trench coat and like it just keeps going. It doesn't want to stop. So that's a visual example of how much of a difference it makes to have a prompt that works well. I am finding that one of the one of the things I can do to make prompting easier when you're trying to prompt at that right altitude is I set myself a token limit. I set myself a rough number of tokens that I want to stay under in order to ensure that I think at the right altitude for the prompt. Now again, this is for the 80% where you want to allow some creativity. There will be those 20% prompts and I, you know, I've written those that are super long and like very detailed and we can go there. They sometimes consume more model resources. They can be very precise. They're a tool in the toolbox. These 80% prompts can be shorter, easier to understand, easier to iterate on, and that's why I call them Goldilocks prompts. They they're good for a lot of things. They feel the right size for a lot of things. I tend to keep these under 500 tokens. And I want to show you how much of a difference it makes. And what we're going to do, we're just going to have fun with this. I'm going to show you a vanilla prompt where I just say make it and it's super vague and I don't give Claude the context. It's just a basic prompt. and I'm going to say make a Thanksgiving newsletter, right? Because it's Thanksgiving. And you're going to see what it does. And then I'm going to show you the difference it makes when I actually add an extra set of Goldilocks prompts so that Claude knows what it's doing. Let's dive in. Okay, here we are. That prompt on the left there, can you create a family newsletter? That's all I gave the model. And this is what Claude comes back with. It's super basic. You can see it has a few visual elements here. And it has these sort of annoying orange highlights. It has a spot to add family photos, but of course that's not clickable or usable. And the copy is pretty generic. And that's that. It is a family newsletter I would not want to send to my family. But what if we choose to add a more effective prompt? All right, here we are looking at the exact same prompt except I've added some Goldilocks prompting. In fact, this is a little bit of an advanced technique. I have stacked up some Goldilocks prompts. The advantage of having some shorter ones is that you can be more effective. So, I have a layout prompt here that focuses on non-anoying layouts and specifies those. I have a color prompt that talks about the kinds of colors that would convey trust or be modern or whatever. I also have a font prompt. All of these are important for getting this into better shape. If we move over here, we see the font has been chosen carefully. We see the impact of the layout. We see the colors are chosen much more carefully and the overall impression is readable. I'm not going to say this is the most beautiful family newsletter you've seen, but I got to be honest with you, I have seen much worse formatted family newsletters. And so, this is not too bad. It even includes a really handy like sidebar with a quote that's not horrific and a nice little footer. So, what's the point of showing newsletters about Thanksgiving when you're trying to learn prompting? You want to start to get a sense of whether these prompts make a difference. And what I'm trying to convey to you is that adding these like slugs, adding these context snippets can help Claude or Chat GPT know the difference and actually build a better newsletter. And yes, I did try this on chat GPT as well. And Chad GPT also was able to code up a nicel looking newsletter. You can decide whether it's more or less nice. It's more of a font heavy approach, but at least it followed the prompt. It followed the Goldilocks prompt and it's useful. Here it is. So, this is Chat GPT's effort to respond to the exact same prompt. You'll notice less of a visual element, but they absolutely like you see the investment in the fonts. You see some really fun fonts here. You see the use of that layout piece. You see the ability to bring pop outs out. It It's not perfect, right? Some of this layout stuff I don't think they've done as good a job on, but I found it very readable. It was easy to read and easy to understand, and it was certainly better than just the vanilla version. You know, sometimes people see my demos and they're like, "Nate, I could make a better newsletter. Why are you trying to show this?" And the answer is, you probably could make a better newsletter. The point is to give you tools to do that effectively. Fantastic. Go make a better one. My goal here is to show you that you can take these slugs of context and actually use them to make useful work. You can do this same thing with business writing, with documentation standards, with engineering standards. Basically, you can take anything that you need Claude or Chat GPT or Gemini to have an opinion on that is at the right altitude and apply this set of principles. I will show an actual prompt here because I think that that gets at the principles that I want to All right, here we have Claude working on a specific skill. And yes, if you're wondering if these can be skills, they can be skills. is a bit difficult to read, but essentially all you're doing is telling the LLM what really matters here. System design should solve real problems, not patterns. Avoid premature abstraction. Never use microservices as a default, a repository pattern before you have multiple data sources, etc. In other words, we are taking things that might be tempting for LLMs to do because they converge toward commonly seen patterns on the web and we're saying not on my watch and we're giving the LLM examples of pragmatic architectural choices that could be better like hey maybe it's a small enough codebase you should use a monolith maybe you should just build the straightforward solution and add patterns only when you feel pain. So, I think one of the things I want to call out here is that what I'm showing you, I deliberately am covering both code and design. I'm trying to show you the span, the tool that I'm giving you. And yes, I'm putting all of these up into uh both skills and prompts. They're small enough that you can literally copy and paste them as prompts into any LLM, into, you know, Quen, into Grock, into Chad GBT, into Gemini, etc. But they're super powerful because they focus you on the right level of abstraction. They give you a feel in your fingertips of what is the right level of abstraction. That's what I mean by Goldilocks prompting. You should start to get a feel for what is the right sized prompt for that 80% of use cases where you want to allow the LLM some creativity and judgment to solve the problem. I think that's underprompted. I think we often try to tell people to use their best judgment for that. I want to give you a sense that Goldilocks prompting is a learnable skill. It's also a sharable skill. I'm going to share a bunch of these prompts with you so you can start to build them, modify them. If you don't like my examples, use different examples. But if you keep it to relatively the same length if you use a similar structure, you're going to end up in a place where you have guidelines, useful context, a scaffold if you will, for large language models to use, but not so much that it is a brittle prompt that often fails. And that's what I want you to have. I want you to have a toolkit that feels like a well-worn chisel in the woodshed and a well-worn hammer. Something you can use every day for a wide variety of tasks and not get lost on. So there you go. That is my plea to start thinking in terms of the altitude you're at. Thinking in terms of Goldilocks prompting, asking yourself, am I prompting at the right level for the task I'm asking for? Good luck with Goldilocks prompting.
