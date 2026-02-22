---
title: "Let's Talk THAT Apple AI Paper—Here's the Takeaway Everyone is Ignoring"
video_id: "I9tYAvjkOQk"
youtube_url: "https://www.youtube.com/watch?v=I9tYAvjkOQk"
substack_url: null
publish_date: "2025-06-09"
duration: "11:20"
duration_seconds: 680
view_count: 44491
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "General"
entities:
  companies:
    - "OpenAI"
    - "Anthropic"
    - "Google"
    - "Apple"
    - "X"
  people:
    []
  products:
    - "Claude"
    - "Gemini"
    - "Make"
  models:
    - "Gemini"
    - "DeepSeek"
concepts:
  - "That right now llms don't have a super standard, understood, accepted uh framework for calling for help when they run into difficult situations"
  - "What you're supposed to do with tower of hanoi is carefully move the discs so that a bigger disc never sits on top of a smaller disc"
summary:
  - "# Let's Talk THAT Apple AI Paper—Here's the Takeaway Everyone is Ignoring

The internet is melting down over the Apple research paper"
keywords:
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "apple"
  - "claude"
  - "frameworks"
  - "gemini"
  - "google"
  - "make"
  - "openai"
  - "prompting"
  - "x"
---

# Let's Talk THAT Apple AI Paper—Here's the Takeaway Everyone is Ignoring

The internet is melting down over the Apple research paper. I am losing track of the number of meme posts that basically add up to the statement that AI is fake. AI is dead. Apple has proved reasoning wrong. It's become a meme. And I am begging everybody to sit down to read the paper to understand what Apple is actually claiming and to understand where it actually meets the road in terms of systems design for AI systems because it is not nearly as dramatic a paper as people are trying to make out. First, if you haven't read it, I'm going to give you a quick TLDDR on what Apple actually did. Apple's research team wanted to test whether reasoning language models actually reason. And I want to be very precise here. They did not use multiple past models. They did not use big uh long inference time models. Uh they did not want to burn a lot of tokens. And they did not use the opensource clawed released reasoning trace framework that anthropic released. I think I said that badly, but basically Enthropic released a reasoning trace framework and you can use it to actually trace thoughts through an LLM. It's super cool. It's very new. This paper was written before that. So, they didn't use it. Instead, they used uh the models stated chain of thought as a way of tracing reasoning and determining reliability. I could have told them model stated chain of thought is a somewhat iffy relationship to model performance, but here we are. We're testing it anyway. They took four different models. Uh, one from Claude, Gemini, Deepseek, and OpenAI's 03 Mini. Again, this is all about model timing. They're using smaller models. Um, and they did not use like the Frontier 03 model from OpenAI. They did not use 2.5 Pro Pro from Gemini. Uh, they seemed to deliberately be wanting to test chain of thought versus long inference time. And those are different things. Then they tested the models they chose on custom puzzles. They weren't allowed to Google search. They weren't allowed to use Python. They were not given any tools at all. It would be like giving a human an exam and no pencil, no paper, no calculator, no tool use whatsoever, just the model and a token budget for thinking. They wanted to make the puzzles they chose something that would not be heavily trained on so that the models wouldn't have memorized the answer through pattern association and they wanted to make it something that they could dial the complexity on. The one that is getting the most attention I will describe for you because I didn't really know what it was either. It's called Tower of Hanoi. It's a very famous mathematical puzzle and basically it is a lot like uh if you've ever had a kid, you have these little uh wooden rods and you have differentiz wooden discs with holes in them and the kid like sticks the the discs onto the wooden rod and it's good for their manual coordination and all of that. Well, being mathematicians, mathematics turned it into a puzzle that has mathematical implications. Fundamentally, what you're supposed to do with Tower of Hanoi is carefully move the discs so that a bigger disc never sits on top of a smaller disc. And it has different problem complexities, right? Uh and so Tower of Hanoi with three discs is obviously easier than with four discs and easier than with five discs. The same idea with logic uh is the river crossing problem where you have constraints in people that cross the river. There's actually fairy tales about this, right? like you cross with like a wolf and a watermelon and I forget what the other one is. There's different versions in different cultures, but the idea is if you don't cross in the right order, I think the goat is in there and the goat can eat the watermelon, the wolf can eat the goat and you have to figure out the right order to cross uh the river in. The point is logic in both cases. Tower of Hanoi, river crossing, logic, checker jumping games, also logic. Apple is trying to test the ability of a model with no tool use, no inference time, just state of chain of thought to reproduce its reasoning with state of chain of thought accurately. Intuitively to me, as someone who spends a lot of time with these models, this feels like a fool's errand. I feel like it would do very badly at this. It turns out that it does kind of better than I thought. Uh, extra thinking tokens do seem to help with medium complexity problems. uh and plain models that have uh no thinking or no chain of thought at all seem to do worse. So that's great. Uh and then what's called high complexity uh the models just don't do well at all. They fall off a cliff. And this is the big finding that Apple is trumpeting or really maybe not Apple because give the researchers credit. They did not overcommit in their paper. Uh, and it would probably be inappropriate to them and unkind to the hard work they did to accuse them of all the meme wars that have started. It's not really their fault. But what people are saying from their work is that this cliff that they discovered around high complexity problems means that AI is useless. And so I want to like the internet lost its mind and I want to back up and I want to talk about it a little bit because at the end of the day what this is really saying is that if the LLM doesn't have tools and doesn't have inference time at a certain point it runs out of the ability to probabilistically figure out novel problems. Okay. I also do that. One of the really sort of sharp takes I I saw on X was someone saying most of my uni University of Michigan graduate students seem to use uh non-logical thinking and lots of pattern matching as well. So I don't know why this is a particularly novel thought because humans do this too. My thought was that most humans do post hoc reasoning which is the closest analogy that I found to the idea of chain of thought being accurate. It's like humans do a lot of post hawk reasoning. LLMs tend to sort of produce train of thought and like it makes sense of the patterns for them. I I just consider it a fairly meh response. I actually think the more interesting take on this paper is how do you get LLMs to call for help? So if you remember um this is going to really age me, but Who Wants to be a Millionaire was a game show that was on for a while and one of the things you could do is call for help. And that is obviously other other game shows do this too. I know who wants a millionaire is not the only one. Um but but the concept is basically if you're at the end of your lifeline and you don't have a way to figure out the problem, call for help. I think that is actually the most practical and useful takeaway for AI systems builders out of this Apple paper. Basically, there are definitely going to be applications where you want no inference time and you want minimal tool use because those add expense and they add time. And in cases where you don't have a lot of time and expense to burn, you kind of need your models to perform well without those things. So, as an example, a customer service bot on the phone, low latency is of the essence. You can't burn a minute and a half of thinking time. It doesn't work. If you're flagging fraud on a transaction, you have uh very very little time to make the fraud decision after the card is submitted. So, does this matter? It absolutely does matter in that sense. There will be times when LLMs need to be able to make good decisions and they won't have tool use and they won't have inference and the Apple paper squarely applies. In those situations, you want the LLM to know when to call for help. Just like the game show, you want them to know now is the time to get a bigger model involved and then gracefully handle the continuation. Maybe that looks like the customer service chatbot keeping the customer on the phone for a second with an innocuous question while the LLM reasons in the background. Maybe that looks like the transaction saying, "hm, it's taking a little longer than usual." And spinning the disc a bit. There are lots of ways to be graceful about this. But the key insight is that right now LLMs don't have a super standard, understood, accepted uh framework for calling for help when they run into difficult situations. And if we want multi- aent systems to succeed, we need to have trigger points that we all understand how to implement a defined framework if you will for trigger points so that we understand when an LLM hits a certain complexity threshold and it is very unlikely to succeed given the parameters of that model, given the testing done on that model, given the latency requirements, given the lack of tools, given the lack of inference time, then we go and ask for help. And right now I feel like a lot of that is being done on sort of a best effort basis by teams designing systems. And I would love it if we as a community came together to actually work on some systems thinking around when it makes sense to have a lifeline to call for help not necessarily even to a human to a smarter model. A model with Python a model with inference time a model that can figure out the problem. Because I will tell you if you give the same problems the tower of Hanoi, the river crossing, if you give the uh checkers problems to models that have tools and inference time and internet access, they can solve them. Just like if you give graduate students more tools, they can solve better problems. We humans are tool users and it's actually not a surprise. It's very well known that LLMs sort of like humans do better with tool use. So when you have a task that is more expensive. If we have a defined framework for that, you can go get the expensive model to solve the hard edge case. Imagine a world where the low latency uh tiny model can answer 98% of customer queries and then 2% of the time it has to go call upstairs to the smart model and have the smart model sorted out. We need a framework so that we all understand what the triggers are for calling upstairs for help. And I think that is one of the most applicable takeaways. I do not think it is helpful to run around saying that reasoning doesn't work. Oh my gosh. In fact, I think the entire thing probably needs to be rerun with tool use. It needs to be rerun with internet access. It needs to be rerun with more advanced models. It needs to be rerun with inference time. It needs to be rerun with the reasoning trace framework that Anthropic released. And if someone says, "Hey, that's pretty expensive." My answer is, hey, Apple's sitting on a lot of cash. They can afford to do this test if they really care about it. And I actually think that if AI is going to be transformative to society, it's probably worth budgeting for a little bit of experimentation to understand how these models reason because it's pretty hard to solve for alignment with these models if we can't figure out how they reason. So, to me, this feels like money well spent. And so, I don't mind that they produce the paper. I certainly don't want to attack them. I think more work in this area is better. I think there's practical takeaways and I think the internet lost its gosh darn mind. It needs to settle down.
