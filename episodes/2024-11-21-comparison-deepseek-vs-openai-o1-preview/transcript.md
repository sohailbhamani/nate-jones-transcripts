---
title: "Comparison: DeepSeek vs. OpenAI o1 Preview"
video_id: "zCvdrME4ErA"
youtube_url: "https://www.youtube.com/watch?v=zCvdrME4ErA"
substack_url: null
publish_date: "2024-11-21"
duration: "5:00"
duration_seconds: 300
view_count: 1210
author: "AI News & Strategy Daily | Nate B Jones"
description: |
  About me: https://natebjones.com/
  DeepSeek: https://www.deepseek.com/

  Story beats:
   • Scaling Laws at Test Time: OpenAI claims smarter answers can emerge by taking more time to think and selecting the best response during inference.
   • DeepSeek’s Novel Approach: A new competitor, DeepSeek, scales intelligence through extended response time but struggles with reasoning outside math and science.
   • Testing Reasoning: Comparing DeepSeek and OpenAI’s O1 preview model using a custom detective scenario to evaluate logic and coherence.
   • Evaluation Challenges: Current evaluation methods focus on standard knowledge domains, missing opportunities to assess novel reasoning capabilities.
   • The Need for Better Evals: Calls for new benchmarks that go beyond domain-specific problems to measure reasoning and adaptability.

  Takeaways:
   1. Inference Time Scaling: OpenAI’s scaling law claim suggests intelligence improves with additional thinking time and parallel processing during test time.
   2. DeepSeek’s Strengths and Weaknesses: While strong in math and science, DeepSeek struggles with reasoning and logic in ambiguous scenarios.
   3. O1 Outperforms in Logic: In a reasoning-focused test, OpenAI’s O1 preview model demonstrated superior logical coherence and evidence integration.
   4. Flaws in Current Evaluations: Existing benchmarks overly focus on mathematical, scientific, and language-based tasks, overlooking novel reasoning.
   5. Importance of Novel Tests: Evaluating intelligence models requires custom problems to measure adaptability and reasoning under uncertainty.
   6. Transparency in Scaling Claims: Clearer commitments to inference time evals are necessary to validate claims about scaling intelligence during test time.

  Quotes:
  “We need better evals for claims about inference time scaling, especially outside standard knowledge domains.”
  “DeepSeek may excel at math and science, but reasoning tests revealed its limitations compared to O1.”
  “If we’re going to claim scaling laws work, we must test reasoning ability with novel and ambiguous problems.”

  Summary:
  I explored OpenAI’s claim that test-time inference improves intelligence and compared its O1 preview model to a new competitor, DeepSeek. While DeepSeek is strong in math and science, it struggled with reasoning when tested using a custom detective scenario. In contrast, O1 demonstrated superior logical coherence and evidence integration. This highlights the need for better evaluation methods that measure adaptability and reasoning under uncertainty. If scaling laws are to be validated, inference time evaluations must extend beyond domain-specific problems and consider novel reasoning challenges. DeepSeek shows promise but needs refinement in logic-based scenarios.

  Keywords:
  OpenAI, DeepSeek, scaling laws, test-time inference, O1 preview model, reasoning evaluation, novel intelligence, logic puzzles, AI benchmarking, inference compute.

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
    - "YouTube"
  people:
    []
  products:
    - "Make"
    - "o1"
  models:
    - "DeepSeek"
    - "o1"
concepts:
  []
summary:
  []
keywords:
  - "coding"
  - "frameworks"
  - "make"
  - "o1"
  - "openai"
  - "prompting"
  - "youtube"
---

# Comparison: DeepSeek vs. OpenAI o1 Preview

one of the things that we need to talk more about is whether or not the open AI claim that test time inference has a scaling law is true I'm going to unpack that statement so roughly speaking the scaling law that open AI is claiming they've unlocked is that if you take more time to think about the problem if you run parallel paths with your AI system and you come back you're going to have a smarter answer if you can select the best response and the reason why we need to talk about whether that scales or not is because we have our first legitimately different competitor outside the big model maker set that's called Deep seek it came out came out of China and it is specifically designed to scale intelligence through test time inference and what I mean by that is when you chat it takes extra time to respond now I obviously went and immediately tried it because I'm me and I wanted to give a problem that I thought would be out of left field or an interesting Challenge and I did not want to give it a problem that would align with what I was seeing as reported as good by the model I want to give it something different to test new capabilities so deep seek was actually reported as being very very good at mathematical and scientific problems less good at language and coding I didn't really want to test language or coding or mathematics or science I wanted to test reasoning I wanted to test logic and so I came up with a detective scenario I actually gave a short synopsis of a murder mystery problem to both open ai's 01 preview model and also deep seek and I wanted to see with the exact same scenario what they would do and I noticed a couple of things one even though everyone is saying that deep seek is able to use that additional time it takes to respond to give a better answer that was not true when it wasn't being tested with a scientific or mathematical question this was just a pure logic puzzle with a lot of uncertainty and a lot of ambiguity and conflicting evidence thrown in to make it difficult and so really I was trying to measure whether the system could sort through all of that conflicting evidence come back with a logical response and at the end of the day when I compared the two 0's response was a lot better 0 came back and it had tightly argued logical reasoning for the choices that it had made it had clearly examined all of the evidence I had given it in the murder mystery prompt it had thought about it it had put it together and it just came back with a really rational response deep SE came back it named a different murder suspect it spit out all of the reasoning token so I was just sitting there looking at gray text coming down the screen and when it gave its response it wasn't as logical it could not logically articulate the reason why it had made the choices it had made with the same degree of coherence that 01 brought and if I were to go into like the whole murder mystery and the whole response it would take a long time longer than you want to spend on this YouTube channel so I'm summarizing for you but I want to call it out because I think we need better evals for these kinds of claims like if we are going to claim that the scaling law holds for inference time we need to have evals that are outside standard knowledge domains we need to not just say here's the rean hypothesis or here's a physics problem and also can you remember dostoevski and write a story like dooi like those are one way to measure intelligence but I wanted to look at something that actually measures novel intelligence and reasoning ability across a new problem so the problem I gave it was not a murder mystery from books it was actually a net new murder problem scenario and when I look at all of that it just reminds me that if we're going to make claims about how inference compute works we need to be making equivalent commitments to inference time evals and if we're not we're really not not in a position to correctly compare a bunch of models that come out so that's my thought I was not super impressed with deep seek from that test I realize it's only one I'm not saying that the people who are testing Math and Science problems are incorrect when they're saying it's great at it it probably is every model has its pros and cons but in this particular case I felt like if you were testing just reasoning 01 clearly came out ahead so give deep seek a try compare it to 01 preview let me know what you think
