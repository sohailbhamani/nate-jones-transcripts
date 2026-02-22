---
title: "NEW Study: 84% of Companies Have Data Stacks That Won't Work With AI"
video_id: "9IETDveRCQs"
youtube_url: "https://www.youtube.com/watch?v=9IETDveRCQs"
substack_url: "https://natesnewsletter.substack.com/p/executive-briefing-why-84-of-companies?r=1z4sm5&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true"
publish_date: "2025-11-09"
duration: "12:51"
duration_seconds: 771
view_count: 10578
author: "AI News & Strategy Daily | Nate B Jones"

yt_tags:
  - "AI strategy"
  - "data architecture"
  - "AI agents"
  - "enterprise AI"
  - "data governance"
  - "zero copy architecture"
  - "AI readiness"
  - "Salesforce survey"
  - "AI infrastructure"
  - "business intelligence"
  - "automation at work"
  - "AI transformation"
  - "data quality"
  - "LLMs"
  - "executive briefing"
  - "AI for teams"
  - "AI scaling"
  - "AI adoption"
  - "AI-driven organizations"



# AI-enriched metadata
content_type: "Framework"
primary_topic: "Career"
difficulty: "Advanced"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Salesforce"
    - "X"
  people:
    []
  products:
    - "Make"
    - "Projects"
  models:
    []
concepts:
  []
summary:
  - "# NEW Study: 84% of Companies Have Data Stacks That Won't Work With AI

This week's executive briefing is all about the glamorous subject of AI ready data architectures"
keywords:
  - "ai-agents"
  - "ai-strategy"
  - "ai-tools"
  - "career"
  - "frameworks"
  - "leadership"
  - "make"
  - "product-management"
  - "projects"
  - "salesforce"
  - "x"
---

# NEW Study: 84% of Companies Have Data Stacks That Won't Work With AI

This week's executive briefing is all about the glamorous subject of AI ready data architectures. Why? You might be thinking, are we going to do that? The reason is simple. Salesforce published data this week from 6,000 plus enterprise data leaders. 84% said their data strategies needed a complete overhaul before AI works. And at the same time, 63% of executives in the survey believe their companies are already data driven. In other words, the perception gap is why most AI initiatives are failing. Leaders walk in to these AI conversations assuming they are datadriven. And what they find in reality is that they're not. Is that the data is not ready for the demands of AI. And so I ask myself, why is that? I look at my own projects I've worked on, projects I've worked on with clients, and I ask, "What can we learn here that will help leaders get over the perception gap and be more likely to establish a successful AI ready data architecture?" So, we're going to go through seven principles that separate the call it 16% who are successfully scaling AI over everybody else. Number one, diagnose before you deploy. So before you run your AI initiatives, you need to be running tests. And there's two big ones that come to mind. Number one, make sure that your system can answer factual questions about your data in less than 5 seconds without human intervention. Am I making it up as like it has to be 5 seconds? Kind of. Yeah. But it's a reasonable proxy. Essentially, if you cannot put in place a system that is able to get a performant query that is very simple through the system in less than 5 seconds, you're probably not ready for anything more sophisticated. And I'm talking really simple like what's our inventory for product X in our warehouse houses right now. Something at that scale. Second, the second test is can you assemble a complete customer view across sales, support, billing, and shipping with no missing data in a similar time envelope. And so, you notice how I'm asking you about performance at the beginning. There's a reason for that. If the tests fail, what you're finding is that you need infrastructure work because your data sets are not designed to be performant in the era of AI. They're designed for slow retrieval, retrieval that might take 30 minutes and be one row in a large report your data analyst prepares, not agentic retrieval that happens on the fly very quickly. And so the challenge for you is to figure out how do you start to change your data architecture so that you can actually deploy AI agents reliably. So the first step just be honest with yourself. Diagnose before you deploy. Principle number two, zero copy architecture is a philosophy. It's not tooling. I'll get into what that means. So, traditional data warehouses copy data to central locations. They clean it up overnight. Then they make it available for reporting. But depending on your needs, Agentic AI cannot wait for overnight batch jobs. If you want real time data today, that won't work. So agents need real time data access to authoritative source systems if you want real-time conversations with your data. Now if you are okay with having day delayed or longer data and you just you're fine with that and most of your use cases are with last week's data or last month's data, this gets easier. But even in that situation, you still have a lot of work to do to make sure that the data sets that you prepare of your historical data are performant in keeping with principle one. The key shift to think about is that the behavior of the business user is also evolving. So part of why in the Salesforce survey, companies were 34% likely more likely to succeed if they used a zero copy approach, which is where you don't copy it to a central location. You just tell the AI to query the data where it lives in all of your different systems. Part of why they were more successful is because they were able to architect the entire system exactly the way they wanted without trying to buy from different vendors and cobble a system together. And so this is in line with other surveys we've seen of executive leadership that have emphasized that it is really important for executives to invest in internal capacity for architecting systems if you want the ability to build and sustain AI long term. And so as much as principle number two is about, hey, we're not going to have copies of our data. We're going to be able to query real time and that's going to make us more likely to be successful because business user behaviors are shifting toward real-time querying. All of that makes sense. But the underlying story that I think that is interesting is that that only works if you are investing in your ability to build those systems internally because your own fingerprint configuration of data is going to be somewhat unique and will require that internal capacity. Principle number three, context matters more than volume. So 49% of organizations draw incorrect conclusions because their data lacks business context. again drawing from this Salesforce survey. So as an example, let's say that the data says revenue is $2 million and the customer is Acme Corp and it's the third quarter revenue number, but maybe that particular database row or that particular fragment retrieved by the AI does not specify that the $2 million was a one-time contract, not recurring revenue, and your agents are now inappropriately adding $2 million in ARR to your reporting. What I'm saying is that is not uncommon and that is a great illustration of how the context really matters when you are trying to construct efficient agentic systems. You have to get context that works. So you need semantic layers that encode business definitions, relationships and logic. Asians should be able to understand the difference between booking and revenue, between gross and net active churn customers from universal single source definition sources of truth. And if you don't have that, if you don't have a semantic layer that defines the meaning across the top of your data at a high level, then the more data you add without context just means more confidently wrong answers. If you're wondering, can you give me an example of a semantic layer? I would actually say there's vendors that do this and this might be a case if you don't have the capacity internally where a vendor makes sense because in this sense you're not asking the vendor to patchwork across all of your data. You're just trying to put a single lens across the data set and interact with it cleanly. And so up to you cube is a vendor out there. There are other vendors out there as well. The principle is not whether you go with a vendor or not here. The principle is that you need to think about your data queries as needing the context that comes from executive insight to interpret well. If you ask these kinds of sophisticated questions and most of the time the data that you have encoded does not carry that context internally in the rows of the database. You have to find a way to add it. So if you want to build that yourself and find a way to add that in that's great. Or this might be a spot because there's only one sort of one point in the architecture to inject this. Maybe it's not irrational to add a vendor here. Principle number four, governance enables speed. It does not slow you down. And so this is one of those things where you need to have governance framed as accountability rather than process. And so governance councils at enterprise scale need to be accountable to quality metadata policies, remediation approaches. And your goal is not to push things through human processes, but to actually have your governance structure encoded as automated quality monitoring so that you can route data issues through the exact same severity model you would use for production software outages. This is not bureaucracy. This is what lets you move quickly if you automate that process. The 16% successfully scaling in the Salesforce survey are doing so with strong governance practices. And there's not really a substitute for it. And I and I want to emphasize again, if nobody owns data quality, the data will not be quality. You need someone to care about data quality in order to ensure that you can actually make the most of the AI investment you're making. But the person who owns it needs to have an automation mindset because otherwise they're going to slow things down. And so that's why I'm trying to give you the nuance and the tension there. So principle number five, the honest timeline is not as fast as anybody wants. The plan in most enterprises is probably 18 to 36 months and you're showing progress in phases. And so you might be fixing critical pipelines. You might be implementing a zerocopy architecture for your top domains. You might be piloting agents where data is trustworthy in year one. Year two, you may be expanding toward real-time capabilities. You may be automating governance year three. Now you're scaling agents. This feels really slow when vendors are going to promise six-month transformations. But those timelines assume your infrastructure is already ready, which is exactly what Salesforce is calling out here. For most organizations, it's not. And so the disciplined approach is to be honest about your shortcomings and fix infrastructure while running AI pilots that show proof of concept and then scale as you see that the foundations are actually solid. Principle number six, you want to close the perception gap between business and technical leaders. The fact that 63% of executives think they're data driven underlines this business technical gap because at this rate, business leaders are making purchases for vendors selling AI tooling on timelines that are completely divorced from the reality of the data architectures. Business and technical leadership need to get on the same team. Otherwise, they're going to end up blaming each other, blaming AI, or blaming their own teams. Misaligned expectations here are a leadership issue and it's something where technical leaders I am convinced need to take the lead. Step up, educate your executives on the technical realities that are constraining AI development in your organization. Be really honest. Make the infrastructure work visible, not hidden beneath the technical teams. This is not a time to hide the dirty details from leadership. You actually need that to avoid writing checks you're going to regret and making promises that you can't deliver on. Principle number seven is all about strategy. The strategic choice that you're facing is time bound. I keep emphasizing this and I'm going to say it again. Data runs on a clock. If you are going to have to spend 18 to 36 months regardless in the middle of the AI revolution fixing infrastructure and scaling AI, it is better to start that clock sooner than later because you are going to fall exponentially farther behind the longer you wait. This is a point I make often, but it's a point that we have trouble as humans processing. So I feel the need to repeat it. We have trouble with exponentials. We are living in an exponential from an AI capability perspective. And when we are living in that space of a curve that's accelerating, we have got to be okay with making bets assuming that the environment is going to continue to accelerate. We need to make bets assuming AI models are going to keep getting better. That means we need to frontwate and really prioritize investments that unlock that AI capability. And I see that willingness, but as we've discussed in this video, it's often business leaders who are overoptimistic about the boring parts of the organization, namely the data stack, who are saying, "We want AI. We're ready to invest. We're buying vendors." And that leads to problems. And so the strategic choice is now, but technical and business leadership need to get on the same page to make sure that the willingness to invest is aligned with where you actually need to put technical leverage to drive AI forward in the business. The organizations that successfully scale AI aren't smarter about prompting. They're not smarter about model selection. They fixed their data infrastructure. They did the boring work first. They ran the diagnostics. They accepted an honest timeline. They did work. And that's how you close the perception gap between we're data driven and actually our data can't support AI and this vendor implementation is doomed from the start. That is an execution gap. That is something an organization can choose to close if it wants to. And if you don't close it, you are going to regret it. So there you go. That is how I read one of the most interesting surveys of the year out of Salesforce. Good luck with your data architecture. We all need it.
