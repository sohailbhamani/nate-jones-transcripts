---
title: "Transformers are Universal Learning Machines"
video_id: "-igxoH9mPeE"
youtube_url: "https://www.youtube.com/watch?v=-igxoH9mPeE"
substack_url: null
publish_date: "2025-05-08"
duration: "10:26"
duration_seconds: 626
view_count: 7748
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Career"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Stripe"
  people:
    []
  products:
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# Transformers are Universal Learning Machines

What if transformer-based models were universal learning machines"
keywords:
  - "ai-tools"
  - "coding"
  - "frameworks"
  - "leadership"
  - "make"
  - "product-management"
  - "stripe"
---

# Transformers are Universal Learning Machines

What if transformer-based models were universal learning machines? We had an interesting taste of that today with a little tweet from Gautam Kadia at Stripe. I want to go into it because I think it has profoundly disruptive implications for the industry. We're used to thinking of transformers as languagebased. The transformer reads all my books and it's a large language model transformer and it comes back with English or Croatian. Well, actually that's a bit of a joke because they don't speak Croatian in some cases because Croatians uh hit decline on so many of their responses. It's a little sidebar, but it is possible to get models to substantially change their trained behavior if enough users hit a negative feedback button. And in this case, you can look it up. There's an actual story where a model stopped speaking Croatia Croatian because Croatians didn't like the responses so much. But that being said, that's your humor for the day. Let's get back to Stripe. TLDDR. Stripe built a transformer-based learning model to detect fraud and it worked really really well. So for context, if you work in the payment space, machine learning is nothing new. Um, and machine learning models trained to detect fraud are nothing new. I used to work in payments myself. We use things like payment method, zip code, lots and lots of other features of the payment to improve the ability to detect fraud. And these are basically adding feature by feature by feature effects that basically work to maximize the odds that someone who's a legitimate purchaser can get through and obviously minimize fraudulent transactions. But at the end of the day, everything is driven around the future. Everything requires very specific training in classical machine learning to implement. And so each model has to think about authorization and fraud and disputes separately. And so the question that Stripe asked themselves was looking at how transformer architectures actually work. They're very generalized, right? They look across very wide swaths of data. Would an LLM approach work? And to be honest, it's I'm frankly I was skeptical. Like when I looked at this, I was like, "No way this actually worked." Because I didn't assume that payments were like language. Language has a grammar to it, right? Language has a sequence and it has rules. Well, what Stripe is discovering here is that payments do, too. Payments have some structural similarities to grammar. Now, there are things that that aren't the same. Uh there's many fewer tokens, for instance. Um the the principles that organize payments are not really like as rich as they are in linguistic grammar. Does it work? Apparently, yes. Uh so what Stripe did is they built a self-supervised network. It embeds vectors for every transaction. It's trained on at Stripe scale, right? So it's trained at the scale of tens of billions of transactions. Um, and it takes all of the key signals for a particular transaction and it distills it into a single embedding which means that you have a huge distribution of tens of billions of payments in vector space, right? Highdimensional vector space, which is a concept if you know large language models that you're very familiar with. And if you don't know large language models, I don't know, go read about it on the Substack. Uh, but the location of the embedding ends up capturing rich data the way the location of an embedding for a word captures rich data with LLMs. And that's what got my head spinning because it means that it's a generalized learning tool in a way that even I hadn't realized. And so basically, Stripe figured out that payments relate to each other in unexpected ways that transformers are able to articulate and understand better than classical machine learning techniques. and better than humans. And so payments that share similarities tend to nest next to each other in highdimensional vector space. And those that you know have even more similarities. Maybe they're from the same bank, maybe they're from the same email address, maybe they're from the same credit card number. Those nest even closer together. And what's fascinating about that is it lets you start to consider the relationships between payment structures in highdimensional space as potential fraud vectors. And so you can spot adversarial patterns and fraud techniques much more accurately. and previously like it's if you work in payments you know this there's an arms race that goes on that's silent every single day between fraudsters and legitimate payment providers where the payment providers are the front line of defense and fraudsters are trying to run fraudulent payments through the system and every day the fraudsters wake up and it's like uh wy coyote and the roadrunner everybody's trying to get a little bit faster and so this is a significant development in this arms race because it means that you can start to look at relational patterns and attack vectors that would not appear in traditional machine learning techniques that look at individual success uh goals or individual that optimize against individual transaction patterns. So for example, if you're optimizing around fraudulent patterns at login, you're not optimizing at the same time around fraudulent patterns at checkout or fraudulent patterns um with a particular uh presentation of payment method. So machine learning is sort of like a scalpel and LLMs which are machine learning but it's a different kind of learning architecture are much more generalized and they allow you to capture relationships between these patterns like what if someone has a certain pattern of login that then relates to a certain zip code that then relates to a certain payment method. Traditional machine learning techniques don't do a good job capturing that stuff and if you're at scale you can't necessarily pull that out individually by hand either. And so another example that Stripe actually gave was card testing. So with traditional machine learning approaches um you know where you engineer a new feature, you label attack patterns, you retrain models, you can reduce card testing a fair bit. You they said they reduce it at stripe by 80%. But the most sophisticated card testers still hide attack patterns in large company payment volumes and it makes it very very difficult to spot. But with a classifier that ingests the embeddings from the foundation model, you can predict if a particular traffic slice is going to be under attack. A particular traffic slice from a from a large company. which means you can leverage transformers to detect patterns in transaction sequences like their sentences and this can be done according to Stripe in real time so that you can block attacks before they hit businesses. So what they're saying is this particular model improved the detection rate for card testing attacks on large users from 59% to 97% overnight. Instant impact on Stripe's largest customers. And then they go on to say the real power of this is we can apply these same embeddings elsewhere. This is a foundation model. We're going to apply it to disputes. we're going to apply it to authorizations. Um, and then they call out the obvious to me, which is that payments have semantic meaning, like words in a sentence, right? If you make a payment, it has sequential dependencies and latent feature interactions that are not captured by manually listing features, which is exactly what transformers get at. Transformers get at hidden grammar, things that we don't know how to describe that describe English or describe another language. Transformers are very good at getting it. And so when I think about that and this is where I want to close. Fundamentally what Stripe has done is they have shown the way to disrupt a an industry that has used machine learning, that has used AI, that has lots of engineers, that is super bright, that is super focused on a particular problem and just completely upend it overnight by building a new foundation model based on transformers because they figured out that transformers are universal learning models. And so I want to ask the question, what other spaces are vulnerable to disruption if we thought about them as places where transformers could usefully learn? Do healthc care billing cycles have semantic meaning? I bet they do. Do treatment patterns and hospitals have semantic meaning? I know I'm zeroing in on on healthcare. That's where my head is at today, but that's that's just one example. Obviously, if Strike can do this part for fintech, you can see it on the stock side with Robin Hood relatively easily. What about education? Does a student's grade patterns through a particular school trajectory have semantic meaning? What about, I don't know, marketing? Do your leads, tracks, and or contacts through a particular pattern through the buyunnel? Does the buyunnel have semantic meaning? You see where I'm going here? Basically, ask yourself the question, what has semantic meaning in your world that you thought maybe is best mapped through traditional methods? Maybe it's not. Maybe it needs a transformer model and we just haven't built one yet. Which suggests that if there is a way to easily build new foundational models for these spaces, there's huge breakthroughs around the corner. So, think about it. What in your space is learnable by transformers that we haven't thought about
