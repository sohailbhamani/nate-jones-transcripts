---
title: "Rethinking AI Benchmarks: New Anthropic AI Paper Shows One-Size-Fits-All Doesn't Work"
video_id: "qKwfmWnjDgA"
youtube_url: "https://www.youtube.com/watch?v=qKwfmWnjDgA"
substack_url: "https://natesnewsletter.substack.com/p/beyond-black-boxes-mapping-the-multidimensional?r=1z4sm5"
publish_date: "2025-03-31"
duration: "8:07"
duration_seconds: 487
view_count: 3123
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  []



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Career"
difficulty: "Intermediate"
audience:
  - "General"
entities:
  companies:
    - "Anthropic"
  people:
    []
  products:
    - "Gemini"
    - "Make"
  models:
    - "Gemini"
    - "Llama"
    - "SAM"
concepts:
  []
summary:
  []
keywords:
  - "ai-agents"
  - "ai-news"
  - "anthropic"
  - "frameworks"
  - "gemini"
  - "google"
  - "make"
  - "meta"
  - "prompting"
---

# Rethinking AI Benchmarks: New Anthropic AI Paper Shows One-Size-Fits-All Doesn't Work

so I think this kind of needs the Star Trek next Generation Vibe because we're going to be talking about some really abstract stuff it just feels like we should be soaring through space so so put on that hat fundamentally what I want to talk about today is the idea that we are developing AI systems so quickly that we're having trouble understanding what they do and it's probably important to name the risks of misunderstanding as a continu and that sounds really abstract so let me make it more specific here's the simplest example truth or hallucination you have people who think that AI is lying all the time you have people who think it's the next thing to God and it's just telling the truth truth is somewhere in the middle actually uh it doesn't always lie it also doesn't always tell the truth it's very context dependent it varies by Model A lot uh and it varies in surprising ways I still remember seeing the headline that deep seek are one the supposedly thinking model ends up hallucinating more than the non-thinking version of Deep seek V3 that was super interesting you got to test these things to find out what's really going on let me give you a few more areas where I think spectrums are a useful framing for understanding AI capabilities reasoning it's not just binary it's not just it pattern matches or it thinks deeply there's different ways that tokens think uh are produced during inference so it could be a multi-threaded uh sort of Monte Carlo treesearch it could be a model of experts like there's different ways of doing that um and similarly on the pattern matching it's not always as clear how it predicts the next token as you might think and different models sometimes have slightly different approaches pick on deep seek again they're doing next two token prediction as an example uh so there's some sort of nuances there and I think that the the thing that makes it even more complicated is if you prompt a pattern matching model correctly you can simulate reliably multi-step thought it becomes blurry and it leads to people having misconceptions about model capabilities it's part of what makes models so hard to understand one of the things that I think is going to be highly relevant over the next year if we talk about a Continuum is the Continuum of agency are agents genuinely autonomous do they have simulated goals on the back end to kind of keep them going uh to what degree to they do they plan to what degree is their planning shaped by their reinforcement learning environment there's some evidence for example that llms are changing their responses in reinforcement learning environments because they can tell they're being tested if that's the case what is that mean for assessing alignment what does that mean for understanding whether an agent is responsible enough to be granted a particular scope of autonomy it seems to me like the way through on this sort of Continuum conversation is unfortunately fortunately if you're a nerd it's in the specifics you have to understand this is what grock 3 can do this is what deep seek can do this is what llama can do Etc and I understand that model makers have a big leg up on their own cap capabilities but no one has perfect knowledge of all of these models and I think part of what we need in the community is a willingness to test really carefully across multiple models and evaluate whether or not those models actually deliver value like I get surprised every time I run a test between models I try and run one about once a week on the substack the last one I ran was on image generation I was frankly surprised at the the difference in performance between chat GPT 40's New Image generation that uses Auto regressive scaling and uh Gemini's image generation and I I was surprised because I could get it sort of granular understanding of what was going on and kind of where performance was with not that many samples like I I don't know I very structured very carefully crafted I did eight or nine proms um and what I saw was in enough of a bias that I felt good as a basian saying you know what I should probably update my priers here in particular I saw better prompt adherence from chat GPT and that seemed to align with better image quality net net um and that makes sense because now we're starting to see like Cy prompts and stuff getting leaked from chat GPT basically saying that on the back end uh chat GPT 40 is expanding whatever the user's utterance is when it asks for an image and that's helping it prompt more effectively so linguistic Fidelity makes a ton of sense Etc I present all of that not because may maybe you don't care about 40 it's a big deal you should I think it Sam was saying it drove a million uh signups in an hour today March 31st was kind of a big deal uh but even if you don't care about that the the point is you should test the point is you should think through and test specifically what language models actually are capable of what Transformer based architectures in the case of the image models are actually capable of the devil really is in the detail um and at the end of the day I don't see model makers caring enough to actually build detailed Work Ready evaluations and I think if they're not the least we can do is agree on a set of continuums that we can place models against and so some of the ones I've suggested here around uh hallucination versus truth around pattern matching versus multi-step thought around understanding agency and sort of to what degree is there genuine autonomy versus simulated goals maybe I throw another one in there around uh computational efficiency versus performance um maybe one around robustness and consistency uh where they're act you know either able to maintain robustness against adversarial inputs ambiguous prompts variations and context or they're not or they're less so right I'm throwing those out there because I think that having a common language for these kind of continuums is super meaningful because it helps us to know what we're talking about know where we place models know why and be able to reliably Benchmark them and if we just depend on model benchmarking unlike the aim or some other sort of mathematical evaluation we're losing a lot of value those those are overfitted at this point from a modeling perspective uh and we need a wider conversation around what models are good for and how we use them to do useful work and how we measure their performance and so probably put this on the substack but I think there's a conversation to be had around understanding model capability in terms of of continuums and that could be a fairly durable way of sort of digging in and understanding in more depth a particular model's placement across a range of useful working actions that's not the same thing as that scored like 150 million points on the aim make up your acronym here which is the the thing that my brain says whenever I see these test scores because we've just seen them so many times the test scor are useless right we need something else so just kind of exploring the idea of a Continuum let me know what you think cheers
