---
title: "JSON: How I Build Perfect Images in NanoBanana Pro"
video_id: "4u48pDYxfHc"
youtube_url: "https://www.youtube.com/watch?v=4u48pDYxfHc"
publish_date: "2025-12-03"
duration: "9:47"
duration_seconds: 587
view_count: 17008
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "prompt engineering"
  - "AI strategy"
  - "large language models"
  - "upskilling with AI"
  - "AI image generation"
  - "JSON prompting"
  - "NanoBanana Pro"
  - "UI design automation"
  - "Gemini"
  - "Google AI Studio"
  - "structured prompts"
  - "AI for designers"
  - "reproducible AI workflows"
  - "AI tools for builders"


# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "Prompting"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Product Managers"
entities:
  companies:
    - "Google"
    - "Notion"
    - "Twitter"
    - "Midjourney"
  people:
    []
  products:
    - "Midjourney"
    - "Nano Banana"
    - "NanoBanana Pro"
  models:
    []
concepts:
  []
summary:
  - "# JSON: How I Build Perfect Images in NanoBanana Pro

I want to let you in on a secret"
keywords:
  - "ai-tools"
  - "career"
  - "coding"
  - "frameworks"
  - "google"
  - "midjourney"
  - "nano-banana"
  - "nanobanana-pro"
  - "notion"
  - "product-management"
  - "prompting"
  - "tutorials"
  - "twitter"
---

# JSON: How I Build Perfect Images in NanoBanana Pro

I want to let you in on a secret. I use Nano Banana Pro with JSON prompting and I've had great results. And you might wonder, well Nate, what is JSON? JSON is just computer language that defines parameters. All I'm doing is giving the model machine readable parameters. And I wrote a prompt, so you don't have to know JSON to write JSON for Nano Banana. You can describe in plain English what you want, and the translator I wrote will render it right back into JSON, which will give Nano Banana a lot of structure. But why, right? You're like, "Well, Nate, is this a universal prompt act?" The answer is no. It's not a universal prompt tack. And the reason why is that prompting specification only works when you are sure about what you want. In so many cases with models, what we want is actually to leave the model room to be creative. JSON is actively bad in that situation. It's also objectively not true that JSON is the only correct way to prop models. I have seen some Twitter hypsters claiming that. That's just not the case. models are trained on lots and lots of languages. They prompt well lots of different ways. What is useful about JSON is being clear about what you want for a high stakes proposition. So if you need a marketing image that has a particular look for the can of beverage and you have to have the model wearing a particular thing and you have to have the lighting in a particular way, that's a JSON prompt. I know it sounds funny, but that's a JSON. If you have a UI and you want to define it very specifically and get the colors exactly right, it's a JSON prompt. That is why Nano Banana Pro is so interesting with JSON and we're not talking about it enough because Nano Banana Pro is a renderer. It is not a vibes machine. Midjourney is a vibes machine. You can say I want a neon cyberpunk schema and and Midjourney will just vibe that. Nano Banana Pro thinks about what it's doing and is very precise. It lives and dies on correctness. JSON gives it correctness. It gives it the clarity. One of the things that makes Nano Banana most powerful is its compositional control. You can pivot a camera around the same scene. You can use different themes, different layouts, different notations. JSON makes all of that explicit so that there are actual human readable properties that you can vary to control the camera around the scene. This gives gives each important thing in the image a stable handle, right? You can have a subject that's different from an environment. You can have a component ID in a UI that's distinct. And once those handles exist, which is really all the JSON schema is, you can say regenerate, but only touch this one thing. And that's where Nano Banana shines, right? I'm not turning the whole scene over to the model again. I'm just asking for a very scoped mutation through a computer schema that Nano Banana will understand. Nano Banana also spans many many visual grammars and schemas let you swap those grammars really cleanly. So Nanobanana isn't just a photo app. It's not just a UI app. It spans multiple grammars. It can be photo, it can be diagram, it can be UI. Each of those visual grammars has almost no shared surface level vocabulary, but they do share a pattern. Each domain has a set of core entities and a rigid way that those entities relate. and JSON schemas help you pin down the visual grammarss that underly marketing images that underly diagrams and UI. In other words, all three of them respond to the idea that you will get a structured blob with named fields and your job is to honor those fields. Nano Banana can work with that to create a photo. It can work with that to create a diagram and it can work with that to create a UI. What's particularly valuable is that Nano Banana Pro effectively can use this ability to render correctness to work across all of these domains. And with JSON, you can work across all these domains, too. I can create cool marketing images using JSON. I didn't think I could create cool marketing images, but apparently I can because I understand how to manage Nano. Schemas basically turn Nano Banana Pro into a tool instead of a toy. Right? If Nano Banana Pro is going to sit inside a really serious product stack with design tools, with code generation, you need reproducibility. So, give me the exact same screen again needs to be possible. You need diff. So, show me what changed in this prompt between V3 and V4. You need the ability to actually test whether a prompt worked in a reliable, reproducible way. That is what JSON schemas offers because you can version control the JSON and say, "We added this one thing to the JSON. Look what happened." looked what look what differed between the last run and this run. You can enforce rules like you know don't reduce your tap target for this UI below 44 pixels and that becomes a part of your JSON schema. You can actually encode things like accessibility into a JSON schema. Nano Banana effectively becomes something you can reason about and govern instead of the designer type to prompt into a nice screen. And I guess we have something that looks good but no one knows why. You want to have a more deterministic set of specifications and the combination of an image renderer that values correctness in Nano Banana Pro and JSON schemas help you get there. Let me show what the flow practically looks like. The human will say something messy. I need a mobile habit tracker app app with a dark theme and I have three screens in my mind and a calendar view. I want it to feel sort of like notion meeting Dolingo, right? If you have a prompt like what I'm building here, the LLM will interpret that. It will apply your design convention. It will fill out a JSON schema with the screens, the components, the tokens, and the layout primitives, and it will let you review it. You can then look at it and say, "Oh, yeah, okay. I think this looks good." And then you can pass that to Nano Banana Pro to render. And all of that detail is there for Nano Banana Pro to pick up. And if you want changes, you can just swap out one field at a time. And one of the beautiful things about this approach is it helps people not familiar with JSON learn one of what I believe is the most valuable skills in the world which is learning to read pseudo code. Pseudo code like J this JSON blob is not real code. It just looks like code. All it is is a fancy list that an AI can read and understand and take seriously. If you can learn to read it, you become someone who can read the kinds of structured inputs that AI values. As you'd expect, that helps your career these days. But the larger value from a workflow perspective is that you as a human can retain your current preference. Right? If you like to write paragraphs to describe your work, you can do that. If you like to write bullets, you can do that. And then you can pass it to an LLM with the JSON converter prompt that I've built and you can actually get a complete output where the JSON is going to be there and then you can read it. You can modify it. You can just pass it right to the model. Now you might be wondering, Nate, how does this all work? Can you show me an example? You're just talking to the camera. Yes, I can. Let me show you how I turned a very, very short piece of text for me. one that would be shorter than I would normally use into a really interesting new creative interface. Okay, here we are. This is an actual JSON schema. All I've given it is please respond with a filled out JSON template that is for a very creative UI about aliens. Only respond with the JSON. That is like eight tokens on the UI. I would normally give so much more, but I'm showing you how much power you have just by appending it. And then I give the JSON template and it is a lengthy JSON template, right? Like it goes and goes and goes and goes. You get the idea. It responds with a full JSON template. It's filled it all the way out. It has imagined what an alien UI looks like. If I had wanted to be more specific, it would have filled more specifics in here. But you can see it's being extremely clear about what all of these things are for. Um, and then it goes all the way down and it says we're done. And this is what I get the first time. So, we're going to actually show you. So, I I went through the first time and I said, "What do you think about this?" And you'll notice, by the way, that I said initiate first contact or the JSON did. It has it right there. This is a very faithful rendition and the model actually graded it as very faithful and perfectly on brief. I thought it could be better. I went over to Google AI Studio and I pasted this in and I said, "Hey, I would like you to faithfully follow this JSON and produce a buildable wireframe of this design." Because I thought the angle being tilty was actually not what I wanted and I wanted to remind it to be professional. That is me adding a little bit of instruction over the top, but it's the exact same JSON. Look at how I get a very nice, faithful JSON response. It reads all of this. It's a long response. It thinks it through and now it's given me a perfect highfidelity. This is exactly what it looks like wireframe that is reproducible. Look how reproducible this is. This this is essentially the exact same image. It is just done tilted forward as a professional wireframe. I get reproducibility. I can hit initiate first contact in both of these very very easily. My point here is not that you build alien user interfaces. My point is that if you use JSON and if you take it seriously as a tool, you are going to be able to get farther with professional use cases for Nano Banana Pro because it responds to the precision because it values correctness. So, I'm going to put a bunch of prompts in the Substack that get into this JSON piece, the JSON translator, because I want you to be able to do this for yourself. I want you to be able to do this for photos, for marketing photos, for other kinds of photos. I want you to be able to do this for user interfaces and I want you to be able to do this for diagrams. I think it's important that we be able to actually use the tools that we're given and part of it is discovering how they work and I think that JSON is an undersold value ad for Nano Banana Pro. So hop in. Don't be afraid of the code. It's not really code. It's pseudo code and the LLM translator will help you so much. Cheers.
