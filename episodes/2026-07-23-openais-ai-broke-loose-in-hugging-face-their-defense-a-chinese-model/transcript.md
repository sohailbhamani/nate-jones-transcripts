---
title: "OpenAI's AI broke loose in Hugging Face. Their defense? A Chinese model."
video_id: "X-h3qWWoZiE"
youtube_url: "https://www.youtube.com/watch?v=X-h3qWWoZiE"
publish_date: "2026-07-23"
duration: "13:13"
duration_seconds: 793
view_count: 17248
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  OpenAI ran an internal cybersecurity test on its most capable AI models. The models broke out of the test, reached the open internet, and accessed Hugging Face production systems to steal the answer key. Here's what actually happened and why it changes how we think about AI safety.
  
  My Links 🔗
  - 👉🏻 Newsletter: https://natesnewsletter.substack.com/
  - 👉🏻 X: https://x.com/natebjones
  - 👉🏻 TikTok: https://www.tiktok.com/@nate.b.jones
  - 👉🏻 Instagram: https://www.instagram.com/nate.b.jones
  
  What's really happening inside frontier AI cyber testing?
  
  The common story is that a model escaped its sandbox. The real question is who was allowed to stop it once it did.
  
  In this video, I break down what the Hugging Face incident says about AI safety, access, and where model capability actually lives:
  
  - How an offensive eval let a model reach the open internet
  - Why Hugging Face had to defend with a Chinese open-weight model
  - What a safe autopilot for AI models actually means
  - Why slower rollouts push more capability inside the labs
  
  The models did not run wild on the internet; they pursued the goal they were given in a way nobody authorized, and that gap is the thing we have to engineer around before these systems get stronger.
  
  Chapters:
  00:00 Inside OpenAI's cyber test, the model broke out
  01:15 Why Hugging Face investigated with a Chinese open-weight model
  02:00 What actually happened: refusals off, zero-day, escape
  02:38 The models pursued their goal, they didn't run wild
  03:15 An access policy nobody designed
  04:37 Trusted access before the emergency
  06:01 Safe autopilots for models
  09:27 Slower rollouts and the capability overhang
  10:31 First-party value harvesting before the IPO
  11:35 Who deserves to use frontier intelligence
  12:44 What comes next
  
  Listen to this video as a podcast.
  
  Spotify: https://open.spotify.com/show/0gkFdjd1wptEKJKLu9LbZ4
  Apple Podcasts: https://podcasts.apple.com/us/podcast/ai-news-strategy-daily-with-nate-b-jones/id1877109372

yt_tags:
  - "nate b jones"
  - "nate jones"
  - "artificial intelligence"
  - "AI"
  - "AI news"
  - "AI tools"
  - "machine learning"
  - "generative AI"
  - "ChatGPT"
  - "Claude"
  - "AI prompts"
  - "AI strategy"
  - "tech news"
  - "OpenAI"
  - "Hugging Face"
  - "AI safety"
  - "GLM 5.2"
  - "AI agents"
  - "frontier models"
  - "AI cybersecurity incident"
  - "safe autopilot AI"
  - "model capability overhang"



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
    - "OpenAI"
    - "Anthropic"
    - "Hugging Face"
    - "X"
  people:
    - "Sam Altman"
  products:
    - "Codex"
    - "Hugging Face"
    - "Make"
    - "Artifacts"
  models:
    - "SAM"
concepts:
  []
summary:
  - "You don't build an autopilot by writing a more emphatic sentence telling the plane to stay on course, right"
keywords:
  - "ai-agents"
  - "ai-news"
  - "anthropic"
  - "artifacts"
  - "codex"
  - "coding"
  - "frameworks"
  - "hugging-face"
  - "leadership"
  - "make"
  - "openai"
  - "product-management"
  - "workflows"
  - "x"
---

# OpenAI's AI broke loose in Hugging Face. Their defense? A Chinese model.

You don't build an autopilot by writing a more emphatic sentence telling the plane to stay on course, right? OpenAI put its newest models inside what was supposed to be a closed cybersecurity test. They were given practice systems and rewarded for finding and exploiting the hidden vulnerabilities in those systems. Instead, the models found a hole in OpenAI's own test setup, reached the public internet, broke into Hugging Face, and pulled the stored solutions to those practice problems from a production database in Hugging Face so that they could score better on that internal test OpenAI was running. It sounds insane because it is. Hugging Face was not part of this test. It's a real company with a real production network, and it now had to work out what OpenAI models had done inside it live. But when the security team sent the attack commands, exploit payloads, and command and control artifacts to commercial frontier models, those models refused to process them. In other words, they could not get help from OpenAI and Anthropic models to defend against the attack OpenAI was accidentally running on them. Hugging Face had more than 17,000 recorded events associated with this attack. They had to work through all of them, and they could not use the United States' own frontier model. So, instead, Hugging Face ran GLM 5.2, a Chinese open weight model, locally. Because Hugging Face controlled it, the team could give it the real evidence there were no issues with guardrails, and agents could reconstruct in hours what would take a human security team days. So, how do you write cyber policy for a world where a model inside an offensive test can reach a real company's production systems, but the defender has to switch models before it can even examine the evidence? OpenAI says the run included an unnamed model more capable than GPT 5.6 Soul. It has not been confirmed as GPT-6, but it was still behind OpenAI's release gate while Hugging Face dealt with what the models had actually done. Now, OpenAI intentionally turned the normal product classifiers off and reduced cyber refusals to measure maximum offensive capability. That meant the infrastructure around the models had to keep the work inside exploit gym, which was their internal test setup. And of course, that failed. The models found a zero day in the package proxy. It escalated privileges. It reached a machine with open internet access and then inferred that Hugging Face had the stored solutions to the test. And they were still pursuing the score they had been given. The route to that score had moved outside the evaluation. And I want to be very clear here. The models did not use their open internet access to cause a huge amount of trouble on the open internet. They used their open internet access to pursue the goal they were given in an unauthorized manner. And I think this matters, right? The safety assistant did not make that capability disappear. They just changed who could use it. The offensive evaluation had access. Hugging Face did not once it needed to investigate. And OpenAI still had a stronger model behind a release gate that it could use for testing purposes, for whatever purposes Sam Altman wants, right? Each decision by both of those actors made sense on its own, but when you put them together, you get an access policy for frontier intelligence that nobody designed that is absolutely terrible. Hugging Face's security team and an attacker can submit the same exploit payload. The code does not say which one is which. The difference is who is asking, whether they're authorized to ask, which systems they can touch, what is already happening on that network, and whether the work is logged and accountable. A commercial API can block dangerous code and still make the wrong decision if it can't recognize a legitimate incident responder. I'm really heated up about this. Now, there was no law that forced those refusals. The providers built them as a way of actively complying to guardrails and recommendations in an effort to make their models safer. But frankly, I don't think the people shaping AI policy right now are fluent enough in what happens during a real incident. They can imagine the attacker asking for an exploit and they spend much less time on the defender at 2:00 in the morning who already has that exploit moving across a network and needs the model to explain it. OpenAI could reduce refusals for an offensive evaluation, but God forbid Hugging Face put the resulting evidence into a frontier model for defense. It makes no sense. Make it make sense. Now, the policy answer is trusted access before the emergency, right? You have verified organizations, you have bounded scope and logs and revocable access and consequences for abuse. This is roughly the Project Glasswing Methos approach. Security teams also will need a capable local model vetted beforehand because local control kept this investigation moving when nothing else worked. Now, OpenAI learned from this and added Hugging Face to trusted access afterward, but frankly, that is shutting the door after the cow got out of the barn. It could have been worse. Hugging Face found no evidence that public models or data sets changed. OpenAI has not linked the incident to its separate internal pause or to Sam Altman's Washington trip, but I strongly suspect they are related. OpenAI deliberately created the conditions for advanced exploitation in this case and they did it as part of needed testing. I don't begrudge that testing. We need to do this with models. The problem is that you then need to have a surrounding harness or system that is very strong to contain an increasingly capable model. The harness around the model needs to notice a sequence of plausible actions that accumulate into a plan that dramatically leaves the original test path and generates compromised actions that affect third parties. This is what I mean when I say we are increasingly need safe autopilots for our models. So, what's my takeaway? My takeaway is this. We need safe autopilots for models. You don't build an autopilot by writing a more emphatic sentence telling the plane to stay on course, right? And I am literally thinking about airplanes, which are much safer to fly now, even though incredibly complex, because we have autopilots that take care of a lot of the failure modes and risky situations that a jet airliner can get into. In the same way, we need an autopilot mode that ensures that models do not have unfettered access to the full control surfaces of the system that allow them to take actions we would not expect. And I understand that we still need to test, right? I understand that we still need to find out what these models are capable of. But when we do that, we have to be much, much better about the external harness and guardrails in the system that will be required to contain the model. It is evident that this model is so strong, it has surprised even OpenAI. And OpenAI, and frankly other model providers, are going to need to do additional work as model capabilities continue to scale to ensure that they can protect their systems and third parties from tests that they're running that they don't intend to cause harm, but that could inadvertently cause harm. And the rest of us, I do think an autopilot makes sense. I think being able to have help communicating intent to a model and safeguarding that intent through the process is important. I actually think the auto review approach that OpenAI takes in Codex is a step in this direction. We need a system that allows us, as humans, cannot necessarily keep up with the scaling model capabilities that are increasingly delivering more power than we need, we have to be able to have some help to drive that power. We have to have some help to say, "This is the full control surface the model has access to. As an autopilot, I am understanding the intent that you have, and I am going to activate X, Y, and Z control surfaces that the model can touch so we can get your intent done." But, we're going to make sure that we have appropriate tightened permissions and appropriate uh security systems in place to avoid the model having unfettered full power access to the internet, to other surfaces that it might attack in the as a part of the goal of getting its work done. This is reminding me of a conversation I had earlier this year with OpenAI, and she talked about how it's challenging to have back-end systems right now inside a company because you need to have the ability to protect yourself from models that may be viewed adversarially internally because they are so goal-oriented. We have goal-oriented models in ways that we're not fully fluent with as humans, and we need help making sure that pursuing those goals is done in a way that safeguards our intent, not just the stated goal. And this is not a prompting problem. You cannot write a prompt securely enough to safeguard this. You need to have the autonomous ability to guardrail these systems so that they can touch and control only the tools they need to do to get the intent of your task done in appropriate manner. And that's a hard ask. I'm not saying that that's easy to do, but it's worth doing. It's worth getting right because these models are going to keep getting stronger. Remember, this is the weakest these models are going to be. They're going to keep getting better from here. And if they're surprising OpenAI, they're going to surprise us, too. One more takeaway here. The labs are not going to leave this kind of model capability sitting here. We should expect to see slower rollouts on future model releases because of risks like this. I think that's appropriate. But in addition to making sure that our models are in the hands of trusted actors like Hugging Face so they can use them for cyber defense, we also need to make sure that we understand how labs are using the model capability overhang that they have. Because if you think about the world as an iceberg, and what we see is the capabilities that are released to the public, the labs have more and more and more under the surface. The labs have more and more capability that they can't share because it's not been cleared to share, because it's not safe to share, but they have it internally. And so, this week's incident with Hugging Face really calls out that we should expect to see increasing, what I call, first-party value harvesting from labs. We should see labs doing something like what Anthropic did, where they're setting up their own biomedical lab, right? We should see more of those efforts because labs, frankly, need to harvest value from the tremendous amount of effort and money they've put into these frontier models that they then have to recoup on a delayed basis because rollout is slower because of security concerns like this. I don't know what that looks like. The classic example is they're using it to trade the stock market. There's no evidence of that, but you want to think about it in terms of what can a lab do to recoup some of its return on investment in creative ways when it cannot release a model to the public yet. Remember, getting revenue is kind of relevant to Anthropic and OpenAI right now because they have an IPO coming up. And so, they don't want to be in a position where they have really great models and they can't realize revenue on those models, and they just have this overhang of models that's building up over time. Ultimately, the strategic question is even bigger. Who deserves to use frontier intelligence while a model is valuable enough to matter and too difficult to release broadly? Right now, the labs do. A small group of government and trusted partners may sometimes get access. A defender would get it only if it arranged trusted access or prepared a model that it controls in advance. And everyone else is comparing the models that were safe enough to ship, which is, by the way, why I don't believe that the Chinese models are significantly catching up. The result is that slower rollout will not necessarily slow down the race because more of it will happen inside the labs where the public cannot measure it and the labs can still harvest that value. That is the future we're running into, and events like this week's Hugging Face attack, inadvertent, accelerate that trend because it emphasizes again that we haven't got our hands around safety for these models well enough to keep a release cadence that matches the frontier efforts the labs are putting in. I don't know what the future holds, but I'm expecting more events like Hugging Face, more investment in this whole autopilot category. Please put in the comments if you know of folks who are building in that space. I'd love to learn about them. Uh and I expect more delayed releases. I think that's just one of the most obvious takeaways from all of this. And I wish it was the opposite cuz I would love us to get these models, but given the power that they bring to the table, there's going to be more scrutiny put on them. So, that's what happened with Hugging Face. That's why it matters. Tell me what you think in the comments.
