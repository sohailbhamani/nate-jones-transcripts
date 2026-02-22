---
title: "AI News Today: Theory of AI Personhood, Microsoft RAG patent, million chip scaling"
video_id: "WKSwUYEOjTo"
youtube_url: "https://www.youtube.com/watch?v=WKSwUYEOjTo"
substack_url: null
publish_date: "2024-11-08"
duration: "9:10"
duration_seconds: 550
view_count: 890
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "News Roundup"
primary_topic: "AI News"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
entities:
  companies:
    - "Anthropic"
    - "Google"
    - "Microsoft"
    - "Nvidia"
  people:
    []
  products:
    - "Gemini"
    - "Make"
  models:
    - "Gemini"
    - "Gemini 2"
concepts:
  []
summary:
  - "0 looks like when it actually releases I I'm willing to bet you though whenever 2"
keywords:
  - "ai-agents"
  - "ai-news"
  - "anthropic"
  - "coding"
  - "frameworks"
  - "gemini"
  - "google"
  - "leadership"
  - "make"
  - "microsoft"
  - "nvidia"
  - "tutorials"
---

# AI News Today: Theory of AI Personhood, Microsoft RAG patent, million chip scaling

okay six pieces of AI news for you and we'll start with a banger Yuval Harari is not the person I would expect to generate AI news he's an author but one of the things he suggested that I think is compelling and correct is that the likely initial path for AI personhood is not philosophical because there's really no answer to that it is not an intelligence test which some people have suggested it's legal fundamentally if an AI is capable of autonomously incorporating itself it is by definition a legally defined person now it can't vote and that's probably a good thing but it would have the same protections as a corporation would have I think that is likely to happen in 2025 I don't know if that's good I don't know if that's bad I just think that given the level of autonomy that we're seeing in the space given the Simplicity of incorpor a someone is going to figure out how to give an llm a mission to incorporate get it done and the llm will be legally a person and that's couple of months away like that's close now I don't think we're going to see a significant share of Corporations B aai in 2025 simply because there's a lot of Corporations and not every AI use case requires this and this will remain a bit of an edge case but it's worth paying attention to because anytime you talk about artificial intelligence people immediately start thinking about replicants and they start thinking about Blade Runner Etc and I think that yval Harari actually had a really good thesis for where this is going to go all right number two Microsoft has attempted to patent rag you know retrieval augmented generation that we've everyone in AI has been doing for a while they've decided they're going to call it uh I'm getting this right uh response augmented system something like that they oh they change like a couple of words right and they call it ra not rag I'm going to link it and they filed it on Halloween this year October 31st 2024 the thing with patent applications is one they're not immediately granted so nobody building in the space with rack has to stop what they're doing and two you can object to them with prior art which means if you've been doing something that is substantially similar you can say so and so I would expect there to be a lot of objection and push back to this uh because we've been using rag for a long time in AI certainly a long time before October 31st 2024 I'm not quite sure why Microsoft decided they could get away with trying to patent that number three poly Market is worth paying attention to uh because of how they performed in the US election this past week this is a blockchain based solution it is not crypto I would argue it is probably the first blockchainbased solution that is not crypto that is widely understood and used across the world uh in this case they did $4 billion do trading on the election and they were able to call the race 2 to 12 hours faster than official news outlets so that's a significant Improvement in an election with consequences that will Echo across the globe getting that right faster is a big achievement uh and I want to call it out because I think it's the first scaled up use of blockchain we've seen outside of crypto all right number three Google dropped a model labeled Gemini 2.0 and it was briefly available this is the same thing right they dropped them they're briefly available and then we hear rumors about them in this case uh this model was very very fast but failed the strawberry test uh the strawberry test is where you ask it to write strawberry but because llms uh do not necessarily include logical checks by default it can have trouble getting the number of RS in Strawberry correct because there's multiple RS in the same place so it failed the strawberry task which doesn't really argue for a super smart model I I'm not entirely convinced this was actually a 20 model it may well have been an accidental leak and a mislabel we will see we probably will never really know but we'll see what 2.0 looks like when it actually releases I I'm willing to bet you though whenever 2.0 really releases that same week 01 is going to drop I think that open AI is just holding it back and they want to be the last horse at the Corral all right what one two three four I think we're at number four now uh yeah so 01 you were wondering about that leak the icons in Wind windows I know you didn't expect me to go there so you everyone wonders like what are these things going to be used for when they're more advanced and one of the classic uses his coding and that's where I get to icons and windows because it suggests something very interesting someone said again it's a claim we haven't I haven't seen a demo yet but they said that during the brief window last week when L1 is open they were able to code up icons in windows with a world model icons that had physics and weight to them without instructing the model on a lot of physics and weight which meant that the model understood enough about physics to code up icons that looked and behaved and bounced around 3D icons like they were in the real world without much instruction which suggests some degree of practical World model which would be a big deal okay and number five uh this one's super nerdy but it's really important one of the things that is hard about training very large models is that it is hard to physically put the chips in the same place and it is hard to make sure that all of the chips lock up and finish a task at the correct point in the training sequence with the correct response the traditional approach to llm training does require all the trip chips to work in sequence and when you get a very large number of chips like a 100,00 one fault on one chip can screw up that entire data center until it gets fixed now the leader here has always been Google because Google has been running huge data centers since before anybody else they have developed more work around fault tolerant architecture at scale than anybody else I know they actually did train Gemini on a multi- DAT Center footprint which as far as I know is the only model to be trained on a multi-data center footprint and the thing is that doesn't automatically make it smarter and so that's why these other models have been able to keep up is because they have things like synthetic data figured out better than Google Etc but open AI knows and anthropic knows that they have to get multi dat Center figured out to scale because there's just limits to footprint on data centers and so they need for these very large training runs to not just have to put a million chips down in the same place but to actually figure out a fault tolerant architecture that will enable them to add more chips in scale because the other factor with chips is that at a certain point because of um the costs of fault tolerance and because of the transmission costs that go into a single state maintenance across a huge number of chips like the speed of light becomes a factor because you're actually like transmitting things back and forth you actually get diminishing returns on extra chips to a point where it may not be even worth it after a certain point so what you should hear from that is not oh no we don't have any more sort of intelligent scaling capability because of the speed of light and chips that is not the correct take the correct take is we have some inherent architectural flaws with assuming that you have to do training runs with lock steps across all chips at once and we have got a solve for that already on the Google Side open AI is working with Nvidia on another solve Jensen was talking about it and saying that he doesn't see an inherent blocker to it and that fundament we should be able to do multi-data center training which would involve not having to transmit and keep all of the chips and lock step across all the data centers and that in turn unlocks the laws of scaling again and you aren't stuck on adding another chip you aren't as stuck when a chip fails Etc I know that was a long sort of explanation I have a whole link I I'll post as well but I think it's important to understand the underlying architecture that powers these models because it demystifies it it also helps us to to understand what's really going on uh as we head into what is likely a training run aiming for artificial general intelligence in the next year to two years cheers
