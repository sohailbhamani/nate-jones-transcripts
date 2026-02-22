---
title: "Nov 2025: My Personal AI Stack—Pros, Cons, and Pitfalls"
video_id: "lY6voDZpu3Y"
youtube_url: "https://www.youtube.com/watch?v=lY6voDZpu3Y"
substack_url: "https://natesnewsletter.substack.com/p/my-ai-stack-what-im-actually-using?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true"
publish_date: "2025-11-07"
duration: "11:04"
duration_seconds: 664
view_count: 19333
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI strategy"
  - "prompt engineering"
  - "AI tools"
  - "Claude"
  - "ChatGPT"
  - "Perplexity"
  - "Grok"
  - "AI for operators"
  - "Claude Code"
  - "Codex"
  - "AI writing assistant"
  - "AI agents"
  - "agentic browsers"
  - "upskilling with AI"
  - "AI productivity stack"



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Product Managers"
entities:
  companies:
    - "Google"
    - "GitHub"
    - "Box"
    - "Perplexity"
    - "LinkedIn"
    - "X"
    - "Lovable"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Perplexity"
    - "Make"
    - "MCP"
    - "Sonnet"
    - "Atlas"
  models:
    - "Claude Sonnet"
    - "Sonnet 4"
concepts:
  []
summary:
  - "# Nov 2025: My Personal AI Stack—Pros, Cons, and Pitfalls

Today I'm going to do something I've never done"
keywords:
  - "ai-tools"
  - "anthropic"
  - "atlas"
  - "box"
  - "career"
  - "claude"
  - "claude-code"
  - "deep-dives"
  - "frameworks"
  - "github"
  - "google"
  - "linkedin"
  - "lovable"
  - "make"
  - "mcp"
  - "perplexity"
  - "prompting"
  - "sonnet"
  - "tutorials"
  - "x"
---

# Nov 2025: My Personal AI Stack—Pros, Cons, and Pitfalls

Today I'm going to do something I've never done. I'm going to share with you my personal AI tool stack all the way through end to end what I use things for, where they work, where they don't work, where I'm frustrated, where I'm also working around things so that you get a sense of how this works. And we're going to do it quickly. We're going to do it in less than 10 minutes. So stay with me. Number one, Chad GPT. Everyone uses Chad GPT. What do I use it for? I use it for analysis specifically. So, if I'm needing something that has some memory, that can handle a lot of context, I don't run out of context window, and I need it to think clearly, not for writing, for thinking, for getting the idea right, for being a thought partner back and forth. Chad GPT5 thinking mode is very, very useful. What's interesting is that the auto mode, the fast mode is becoming increasingly useful for digesting large amounts of context quickly. So, if I need a rough pass, I can do that. But I do not use it for writing. I find that chat GPT can be used for writing if I push it, but almost always I go somewhere else because the default voice for chat GPT is not good enough. I also don't use chat GPT right now for PowerPoint and I don't use it for Excel. I don't find that the finished quality of work is really there. I will use it to produce CSV files if it's just a simple one sheet spreadsheet and it's got to be a table. Chad JPT does great at that. Moving on. I use Claude Sonnet 4.5 a lot. I use it specifically for writing because it's very very good at picking up voice and at following my instructions and actually getting voice right. Especially if I give it a sample with that voice. And so one of the things that I like to do is I like to ask it to brainstorm in my voice back and forth with me. How can I write this better? Can I tweak this paragraph? Can I do a better job formulating this point? It's a writing assistant. It doesn't just sort of produce it for me and I walk away. I keep emphasizing this with writing. You are accountable for every word you write. So, if you're going to put something out there, you better own it, however you made it, whether you're writing with AI or without AI. And so, I find it's a great thought partner when I work with it that way. Bonnet 4.5 is also what I go to when I'm doing Excel analysis right now. It's got a great tool set for that. I have a whole guide out on that and I find it super useful because I can actually dig in and understand what's in the box and produce a useful analysis or edit an existing file. All of those things are possible with Claude. That being said, there's an even better tool out there for PowerPoint and that just came out recently and I'm really torn about it. I'm going to tell you about it and I'm going to give you the caveats because this you're getting a tour of the workshop, right? You get to see how Nate does his personal stack. Kimmy K2 is an open- source model out of China and they have done a phenomenal job of putting together a PowerPoint skill that enables you to make useful PowerPoint presentations that look really good. And I will show one with the Substack write up. You can see it's a very simple prompt, but you get a very useful PowerPoint out of it. That being said, because of the where the data is located, you cannot really use this in the US or the EU for corporate data. It's just the protections aren't there. And so if you're doing a fairly generic presentation where you're not, you know, you're using publicly available information off the internet, it's phenomenal. If you're using it for personal use and you don't mind, it's phenomenal. Great job. If you need corporate data protections, I find that Claude Sonnet 4.5 is super super useful for PowerPoint creation. It's just a little bit less designed. I tend to prefer a spare, elegant, minimalist approach with my PowerPoints. I wrote up a whole guide on this I can link. It's it's going to be what you need it to be with with Claude. It's going to be usable. It's going to be presentable. But if you have a very elaborate PowerPoint style, got to be honest with you, you're not going to get what you want out of Claude. You're not going to get what you want out of any AI right now. The AIs that are doing the work with PowerPoint either have fairly strong preset styling or they're very clean and minimalist and elegant. One thing I will call out is I do not use Kimmy K2 for thinking. I don't use it despite the benchmarks that it recently took. like I find that it's just not as useful in practice. This is why you don't trust benchmarking and instead I use chat GPT for thinking and I can pull outlines and put them into Kimmy K2 if the data is not sensitive. So that's the PowerPoint piece. That's the Excel piece. There's a little bit of the writing piece in there. You may wonder what about formatting word docs. Sonnet 4.5 is actually surprisingly useful for formatting word documents. You just have to ask it and kind of be specific about what you want. And so that's another useful tip. The weakness, and I know people are going to call this out, so I'll just say it. I struggle with it, too. Claude has context window limitations. In particular, if you are building in a lengthy Excel or PowerPoint skill, you will struggle at some point with Claude running out of context. How do I deal with that person? Well, I wrote in my guide on PowerPoints that that you want to think about chunking the deck, right? You don't necessarily want to generate the whole deck in Claude at once. You want to break it up into pieces, maybe five or six or eight slides each. That's true. You also want to separate out the data and the narrative piece on bigger decks so that you can get those right beforehand and you don't burn tokens on those in a debt creation conversation. If I run into issues once in the chat, I always go back and I restart the chat with a smaller ask. I have very little patience for running into issues more than once. And so if I run into to context window issues on claude, I'm always going to condense the ask down and go piece by piece and I will find out where the context window runs out and I will get usable information in the meantime. And so yes, do I start again? I absolutely do, but I'm very careful not to repeat my mistake. I do not want to go back and have to have multiple times hitting the context window. So if I ask for a PowerPoint and it hits a wall at the end of the context window, I never repeat that ask. If I do that with Excel, I never repeat that ask. What about search? So, with search, I love perplexity. I find the perplexity is really useful for most general purpose searches. I love the research piece. Uh, and I wrote about this recently, too. I love the research piece. I love the labs piece where you can dive in on discovery and understanding and creating reports. It's super fun, but it's not perfect. And there is one use case where it really struggles and that is finding recent information on social networks about a trending topic. It just not as good. And so as funny as it sounds 4 is really really good at just that piece. And so I use Gro for that. I will go and say tell me what people are saying on Reddit on X about this particular issue. Especially if you have like an AI topic that is trending or a brand new uh product launch and you want to know what people are saying about it. Grock is super super useful for digging in and understanding that. I don't necessarily trust it for larger scale thinking. I don't trust it for outlining. I don't trust it for general web research. But for that particular thing, it is very very good for finding social conversation. What about web browsers? So I am really torn on this one. My generalpurpose web browser remains Comet. So I'm using Comet a lot. I use it and I like the data ins and outs it has. I'm particularly fond of its ability to do generative you. So if I'm sending a message in LinkedIn, it will literally generate a message pane for me and let me approve a message I send and all of that. That's great. And it has data ins and outs to a few places uh including LinkedIn where it's very easy for me to not have to go. I got to be honest, I don't love LinkedIn. I don't like to be there. Having a data in and out where I don't have to interact with the site is fantastic for me. But beyond that, it's very useful because it combines perplexity search powers with an agentic browser. And so it's easy for me to get a chat next to the browser to understand what the page is doing to ask for the to do other things off page for me, which I find really useful and to keep the power of perplexity in the meantime. And that's actually a use case that I I don't know about you, but I like the idea of the agent going off and doing things for me. And comet really sort of fulfills that. I think the Atlas use case is really interesting. Atlas came out recently. I have found things I can do in Atlas that don't work as well anywhere else, but that feels like I am still figuring out where those use cases are. I think one of the big differences is this is a chat GPT first browser. So, it brings my memories in. It is also chat GPT first from a search perspective. It is also chat GPT first from an engineering perspective. And so, you get all the strengths that that comes with that the model remembers you. The model talks to you like it knows you. The model understands your preferences. And in fact, the more you use the model, the more it understands how you think about the internet. So, this is all good, but it also means that you're going through chat GPT for search versus Google. And that's a design choice they've decided to make. It makes sense from a product perspective, but it's something you have to decide if you want to live with. Um, and it also means that you are sort of committed to their vision of the agentic future, which is frankly a little bit more button-down and safety first. like they are keeping the AI agent on the tab with you for now. You were keeping an eye on it for sensitive tasks. They have walled off certain tasks that you can't do things around banking etc. that make sense to me like I wouldn't want it to be able to do that initially. So they're assuming that the AI agent is not entirely trustworthy yet and designing around that which I appreciate. One last piece to call out on Atlas, it is it has the chat GPT brain for code and that makes it super useful if you are trying to understand how to build something or how to review something. So I used Atlas to look at a GitHub repo and that was super useful because I could pull out a lot of the details of the code and get it into a format I could understand and process really quickly. I also used it when I was looking at Lovable. So, if you want to drive a build off of lovable using Atlas autonomously, you can do that, which is really cool. Now, we're going to come to the terminal and the command line. Yeah, you thought I was done. I'm not done yet. I love both Claude Code and Codeex. I find that Codeex is an extraordinary strategic thinker in the command line. I go to Codeex almost daily when I'm trying to think through a problem and I need succinct, clear, strategic analysis. Codeex is also really good at finding and fixing bugs. I love that. that I can throw a really messy repo at it and it just kind of digs in and finds them. I love Claude code because it is so sort of rich as an ecosystem. I can tie in cloud skills. I can tie in my local files. I love that I can tie in the MCP servers that I want to and I love that it's for lack of a better term it has a friendly feel. Like I love that it goes and does tasks and checks back in. That being said, Cloud Code has a very strong bias for action and Codeex is more thoughtful before engaging. And so you have to know which one you're going to choose because otherwise Claude Code is going to be very tempted to just run. So that's my personal stack. I got it to you in just over 10 minutes. I would be curious what your personal stack is. And of course I'm going to get you uh all of the guides that I've written that go with this and also some extra details just for this based on my own experience in the last uh week or two because this always changes and so I want to make sure that you get the latest information. Uh you're best informed. Best of luck with your AI stack.
