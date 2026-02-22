---
title: "AI News This Week: Large Language Models for Developers and Kids!"
video_id: "VxzQiJ8Ngkk"
youtube_url: "https://www.youtube.com/watch?v=VxzQiJ8Ngkk"
substack_url: null
publish_date: "2024-08-12"
duration: "10:06"
duration_seconds: 606
view_count: 300
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
  - "Product Managers"
entities:
  companies:
    - "GitHub"
    - "YouTube"
  people:
    []
  products:
    - "Claude"
    - "Make"
  models:
    []
concepts:
  []
summary:
  - "# AI News This Week: Large Language Models for Developers and Kids"
keywords:
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "claude"
  - "coding"
  - "frameworks"
  - "github"
  - "leadership"
  - "make"
  - "product-management"
  - "youtube"
---

# AI News This Week: Large Language Models for Developers and Kids!

I like to stay up to AI in part by looking at where new products are pushing the edges of llm capabilities and I saw two products this week that I want to call out one is for software developers and one is for kids we're going to cover both of them so the one for software developers first uh it's called Genie it's developed by a company called cosign it was just announced I think today the 12th through yesterday the 11th that jeie is now on the leaderboard the number one performer for a set of tasks that test llm capabilities at solving bugs known aswe bench uh and what that does is if you're not familiar with it you basically give the llm a set of GitHub bugs to resolve and it goes and fixes them and you sort of measure how good it does and it's much better than much B hooded solutions that we have seen previously so Devon came out like like three four five months ago I forget and they were celebrating because they got a score of 133% on re resolving novel GitHub bucks and now the bar is 30% because that's what uh Genie got so jeie is roughly twice as good as Devin and the reason why is kind of why I brought this up they are focusing specifically on pushing the edges of llms around reasoning and that's been one of the big gaps that has proved prevented llm performance in code environments in the past or at least mitigated it or made it less effective so one of the things that sometimes agents will do uh llm agents will do if they're trying to solve a software problem is they they sometimes just sort of throw code at the wall until it works and I've even seen this when I've played with Claude and I've had Claude write JavaScript for me and like if I tell it what the bug is I have to actually give it a fair bit of direction before it starts to sort of adjust the code the way I want it to adjust cosign and the genie product seem to be different because they've worked really really hard on starting to encode reasoning outside the llm itself so the llm can handle the language piece but there's a lot of training on the back end to make sure that the approach is structured the way an engineer would structure and so they emphasize locating code in the correct place in your existing code structure so there's a deep integration component they emphasize planning and structured planning that's where the logic comes in they said they use rag in there they're kind of Cy about what else is in there it's not just rag it's very clear there's something else uh they talk about in place edits as another thing which one of the things I noticed is that like in place edits is something that requires a degree of contextual awareness that typically human Engineers are really much better at because they understand the code base and so they're working on resolving that by making sure that you can do an inpl edit that's contextually aware of the style of your code the architectural principles and then come back and do the final step which uh is agentic validation so they go back and like independently validate and test the in place edits they've made and then if it doesn't work they go and rewrite the code in place until it does and and it's fin result so they are kg this is not something where they're going to publish enough of their methodology that you can replicate it uh they are deliberately not being open sourc they view being closed source as a competitive Advantage which of course they can and I think one of the things I'm keeping an eye on is the overall direction of the market as a product like this comes online because I've noticed in the past when something like this hits the market you wait two months three months someone else is going to beat them and they're going to take the same approach and push it harder one of the hardest things right now is competitive value how do you have durable value when we were building the railroad durable value was literally laying track to a village and you sort of owned the track and you owned access to the village and the trains could go there and you could sort of harvest rents off of the value that you would put down it's not that clear when you were building an llm because llms are expensive you have to train them now you have to have this agented reasoning piece that comes behind it all of the thinking that goes into how you design a system that doesn't just generate tokens but actually plans and reasons and at the end of the day the bar is moving so fast in this market and so much money is being poured into this intelligence development initiative from the industry as a whole that you will be overtaken within 90 days like it's a safe bet it's happened just about every 90day period that whatever the bar is it gets raised about every three months and yet you've put so much into that that you jumped on the treadmill you you've decided to raise your flag and say you're you're a company that focuses on enabling developers and now you're just having to just pump out better and better Solutions and from a developer perspective from a consumer perspective from a working perspective that's fantastic intelligence is getting cheaper and more available but if you're trying to build a company around llm intelligence it is not at all clear right now how you monetize this kind of development so the two takeaways I have are that the technical side is really interesting I love that they're working on the reasoning I think we're going to find out a whole lot more about how they did it in the next 90 to 120 days because someone else is going to do it and the details are going to start to leak and these Solutions are like leaking out faster almost than we can we can track so I would expect we're going to have a real solid sense of how to get reasoning to solve at a 30% Benchmark quite quickly even if they choose not to release how they did it and then the other thing is the competitive pressure means that it's hard to build Moes in this economy like if you are building in AI you have to think really carefully about your distribution advantage and building modes and that brings me to the second development which is in the kids department and I think this is a good example of distribution advantage or at least implied distribution Advantage this is a company uh called magical toys they produce something called Dino I'm going to link these in the in the bottom of the YouTube and the thing that's interesting is that this is an embodied llm and so I'm not saying the llm can sense its surroundings the way a human can but I'm saying that theyve placed the llm inside a plushy or a stuffed animal so that a kid can interact with it and the idea is kids have too much screen time let's make sure the child is talking to and developing verbal skills and interacting with a creature on a daily basis and oh the creature happens to be a plushy with an llm capability and so Mom and Dad can monitor the chats and Mom and Dad kind of keep track and the dino will sort of use positive emotional reinforcement and be supportive and emotionally empathetic and all of that I don't doubt the ability to implement an llm with that kind of emotional parameter right like that is safe to talk to kids that it's going to be emotionally uh supportive of the child's feelings that it's going to be able to help the child learn verbal skills we are headed to a world where children and the elderly are definitely going to be interacting with robots as a part of the human development process and whether or not you and I are comfortable with it it's happening I think the piece that is interesting to me is that they are getting the distribution advantage in the space by literally pushing the product into people's homes and then they have it and they're going to get another one when the next kid comes along and they're GNA up upgrade it when the company releases another one there's a loyalty because Dino is a member of the family and that's a really interesting play for distribution advantage and what is effectively a commoditized llm space and so they're looking to differentiate it by making it more human they're looking to differentiate it by making it more of the family and that's what they actually say on the site welcome Dino into your family we are going to see more plays like that and that lines up with the whole monetizable movement around AI companions which has been one of the few areas where llms have monetized really successfully is as talking companions for people and I think that one of the things that we haven't yet figured out how we as a species feel about is is it more human or less human is it positive for us to practice this human language skill with something that is effectively a robot that we trained on human language and it's really good at it I think net net it will probably make us better at language I would buy that spending two hours a day with Dino for a kid is better for the child's language development than two hours a day with the iPad I think that's pretty logical the interactivity is going to reinforce learning and I still think that we are going to see people who are going to take that learning and say well where is the other children playing with the child that would normally reinforce reinforce language development and so I think we're going to get questions as these companies come into our lives around how they work not just with individuals not just with families but with communities how does Dino work when the child has a play group does Doo pull the child away from the playgroup or not so I will be curious to see how that unfolds I think from a pure distribution perspective they have a distribution Advantage by personalizing the product and I think we're going to see more of that I also think they have an advantage by playing in the emotional space that will help them be not a commodity for the families that purchase them and I am beginning to wonder if that kind of play is something that will help llms breakthrough on the consumer side so two things I'm watching one is on the developer side definitely nerdy looking at agentic reasoning and the other is on the consumer side looking at stuffed animals and how childhood development is aided by interactive llm driven dinosaurs have a great one
