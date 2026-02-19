sam  1:20  
You Mark, how are you today?

Mark Mote  2:34  
Hey, doing well? How are you appreciate

sam  2:39  
you taking the time hopefully your

Mark Mote  2:40  
Wednesday is our biggest start. Good so far. Yeah,

sam  2:44  
good. Well, listen, I'll quickly introduce myself, and I would love for you to do the same to Sam. I'm based here in SF, at our HQ, and I joined them probably back in 2024 as one of our first of Friday I hires. So back in those days, we were very scrappy, small team of, like four or five people. Since then, we've grown so well over 100 people, and we developed different role specializations over time. So there's a solution architect function that's more of like a pre sales role that maps to account executives. And then we have a couple other smaller specializations, and the other big one is our forward report engineering organization. So you know, within that org, you know, we're a little bit newer, but we're still a few dozen people at this point, and growing very quickly. So I'm not gonna answer questions you have about the role and what we do day to day, but that's a brief intro to me, and I would love to learn a little bit more about your background. Sure.

Mark Mote  3:35  
Yeah, I'll give you the highest level first. So I'm a two time founder. Originally, my background was aerospace engineering, but my PhD was in robotics. Currently, I'm planning to step down as CTO of Rooster, which is my second startup here. We built AI agents for supply chain workflows. I was the sole production engineer there, so all of the production code I built before that, I founded Python. So it was a computer vision startup at first, but through a long process of iteration, we ended up selling AI agents to actually something like supply chain, but very different than rooster. Yeah. So I think FTE, from what I've heard, sounds great. Really matches all the parts I like about being a founder, but with potentially a lot more scale and impact.

sam  4:33  
Yeah, makes sense in the role, and I'm excited to dive into the background of some of the things you've worked on. I have curiosity like, Why? Why the interest in anthropic as opposed to similar lab? Like, what? What is it about us?

Mark Mote  4:49  
Yeah, yeah. It's hard to answer without rambling, so I think I can compress it into two things, right? So one is, I want to have an impact, right? And anthropic, I think, is, you know, it's the most innovative company out there, right? Every major ecosystem innovation in the past three years that I can think of was anthropic. And the second is alignment, I want to have an impact in a direction that I actually care about. So, you know, AI is going to be the most transformational technology we ever build. And I think, you know, the the implications on both sides of that equation are huge in terms of both benefit and safety, and frankly, anthropic is the only major company that seems to take that very seriously.

sam  5:43  
Yeah, we take it extremely seriously. And it is. It is a major part about how we even think about this role, right? Like we're empowered to work on things that are like going to be in line with our mission, and not work on things that are not in line with our mission.

sam  5:57  
So, yeah, it all tracks.

sam  6:00  
So it sounds like you've, you've found a couple of companies. You can give a background that's like, maybe a mix of hardware and software, if I'm understanding correctly, tell me about the kind of work you want to do. Like, what are you very excited to work on? Like, when you think about what you do in this role, what what comes to mind?

Mark Mote  6:21  
Yeah, yeah. So the way I like to think about it is, there's say there's a spectrum between, you know, all the work I've done in my life, which ranges from be highly theoretical and just write research papers all day, but ship nothing. And on the other end of that is, here are some specs for a very well defined problem that's not open ended. Go ship it quick.

Mark Mote  6:48  
I'm thinking, you know, a quarter of the way to

Mark Mote  6:52  
40, 50% of the way through that spectrum, if that makes sense. So the way I think about it is, you know, the problems I get are open ended. Hopefully I'm working with a great team, with a lot of brainstorming. We whiteboard at the beginning of the day, but by the end of the day, or at least hopefully by the end of the week, we're actually working on shipping something real.

Mark Mote  7:14  
Does that make sense?

sam  7:16  
Yeah, it sounds like you just like the process, like the game, yeah?

Mark Mote  7:21  
Just like open ended challenging problems with Yeah, kind of a balance between, you know, creativity, but actually doing things, yeah,

sam  7:29  
we try to rein in, like overall, like this, like the scope we'll work on, so that it's not like, so open ended that you get pulled into like, ridiculous areas of a given business, like, if I were to go staffing on a project at, like a major financial institution or like a major health insurance company, there are a team that will come out of the woodwork and, like, you know, sap up your time. But, like, we try to keep some bumper rails on things. But by and large, like the the actual solution you said, you said, at a building, is very much something that you have to explain, you know, inject a ton of creativity into and it's just very, very big part of the role. But helping the customer, like scope what they're even looking to do in the first place is often very challenging, and it's definitely a piece of this.

Mark Mote  8:13  
So, yeah, yeah. And that's, yeah, that's what I love. I mean, engineering isn't just solving the problem, it's also figuring out what problem you should be solving, and taking these messy constraints from whoever the stakeholder is and turning that into, you know, some kind of prioritized plan for what actually needs to get done and what doesn't. Yep, it's kind of like meta engineering in a way. You know, you engineer the product, but you also engineer the process for engineering the product.

sam  8:41  
That's right. And the other thing too is that you often work with engineers on the customer side. And a good way to describe the role is that it's kind of like being a fractional CTO. Like, it's often being the fractional CTO is higher leverage than just, like, shipping all of the code for them. Like, if you can, if you can ship some things and then ship through the engineers that are staff and the customer side with you. Sometimes a mix of that is high is higher impact, because that means that the next time the customer might want to build something with our models and our products, they might not need as much hand holding from us, and you can go work under the next novel set. That is how we started to conceptualize it.

Mark Mote  9:19  
Okay, yeah, like that.

sam  9:22  
So on the like, on your within your background, you mentioned your current startup. Lisa Brewster is the current the current company. You ship pretty much everything there you've been the CTO there you're a founder.

sam  9:39  
Can you walk me through, like,

sam  9:41  
one project or feature product you build with llms and just like, take me through the process of building that thing end to end. I know this is an open ended question, but I want to understand, like, the overall shape of some of the things you've worked on.

Mark Mote  9:55  
Yeah, definitely. So yeah, many moving parts is, I think you picked up on the most difficult one was what we call the procurement workflow. So essentially we're a freight forwarder. We receive information on what people are selling, and then we go and offer that to people that want to buy it, which means we get a lot of emails from vendors with what are called rate contracts. And a rate contract is essentially every thing that you need to specify international cargo, so who ships what under what terms, what fees and what timing. We receive this information in the emails and we need to process that automatically to go into the database. Sounds like a straightforward problem, but I think we worked out that, you know, annually, it's, you know, $100 billion of time lost spent on this, actually.

Mark Mote  10:57  
Yeah. So what made it difficult is, I

Mark Mote  11:03  
is one the schema needed to be very reactive, because people have their own fees, their own terminologies. We would discover things that we hadn't accounted for on the fly, and need to react fast. People like to send things in their own way, sometimes their own language. So sometimes they would send us rates just in the email text. Sometimes it was referencing a previous email in the chain. Sometimes it was a PDF or an XLS document. So the core of this was really find something that's extremely robust towards email inputs to get it into a database, and then there's a human review stage after that, which I can talk about later. Are you with me so far,

sam  11:50  
email comes in? Yeah, there's information need to extract these emails. That information is just then written into a dB, and my guess is that there's an LLM that, like, reads the email and, like, maybe calls a tool or just use a structured output so, like, produce the information that information is in written, is that the correct understanding? Or am I missing stuff?

Mark Mote  12:11  
Yeah, yeah, that's it. And really, really, it's like a full flow of What case are you in? So you receive the email, what do you do first? Well, you decide what type of email is this. Should this even go to the procurement workflow? Should it, you know, be processed? Is it a known vendor, or do I need to add a new one? Do I need to respond to it? Or do I need to actually extract the information? If you do need to extract the information, then it's it's really the art of what parts of the problem can you chunk away and do in a more reliable, you know, structured python script, versus purely having the LLM analyze it both for efficiency and and reliability, right? And then you get kind of a proposal. You get an audit trail on where it found the rate, how confident it was. The final step would be cleansing, so you know, if someone referenced a certain port that wasn't in our database, we needed to match it to a standard name, for instance. And then that gets pushed for human review.

sam  13:22  
Gotcha, yeah. And then, you know, there's a human review step at the end, but like I would imagine that you want to reduce human review time and reduce the amount of time where humans have actually going to make edits, because that's more costly than just saying I can check the box, and this is correct, right? Absolutely. Yeah. How did you think about evaluating success and making the system better over time.

Mark Mote  13:42  
Yeah, so in terms of evals,

Mark Mote  13:47  
probably the best thing that we did, obviously, we had smoke tests and tests on each module and all that, but was have a good loop for every time that we saw a case that it failed on, we could then go add back into the test suite, right? And it was being able to do that in a matter of hours rather than days, that was the trick, right? So keep a very long list of every tricky case that you encounter, and make sure that after every update, it at least passes all those cases. Yep,

sam  14:26  
out of curiosity. So this is like, very workflow shaped, right? It's like very on rail system. How familiar are you, like, with, like, the world of agents and like anthropic sneaking on agents and like that, that space. Have you dipped your toes into that water at all? Yeah.

Mark Mote  14:44  
So, I mean, ironically, the easier problem was the agent we built to answer questions. So basic, react loop, we didn't do rag, but I think that would have been the nice next step would be to index every email and be able to search through better, sorry, I'm getting a calendar pop up. Yeah, so that would be just a basic loop with a scratch pad with different tool calls to the database and the email that could iteratively find the information and answer questions. We we initially built that for to sell it as SaaS, but ended up using it internally, mainly because of how our business evolved. So yeah, lot of familiarity with the different workflows and types of building agents, and, you know, a decent level of experience

sam  15:41  
gotcha one, aspect of our I'll just tell you this. One aspect of our interview process is, like, we put you in an interview the session, this is the next round put you in an interview module, where it's just you in a collab, where you have, like, just a bra, like Python, SDK, and the task is to just build an agent in 45 minutes that basically is like that while loop. Okay, yeah, tell me about the loop you built. Was it? Was it just using like the end, turn from like the stop, reason to like break? Were you? Were you basically doing it? What kind of on rails where you have like, sort of a dagger prompts? How did the React work for the assistant.

Mark Mote  16:23  
Yeah, so it's definitely the type of thing I should have reviewed more recently. I built it about a year ago. So yeah, I would say keep a scratch pad. First step is planning. So let me think through the tool calls would have been database and email,

Mark Mote  16:48  
and eventually slack, we hooked into it.

Mark Mote  16:53  
And then, yeah, see if you could answer the question. Try to look it up again. Have a have a sub agent that you're using to, you know, search through emails if you can't find the right email, and

sam  17:10  
then on the planning step, how would you implement that?

Mark Mote  17:15  
Yeah, so you could do it as a tool call. I think I forget what exactly I did, but you have it essentially, I'll put a JSON for each step in the plan, and you have it re evaluate at the end. Is this going as planned? Do I need to reassess the plan? So I guess the word for that is reflection, right? First step, execute, find the information, reflect on how the plan is going, whether you need to replan. And then have some sort of flag for Max iteration depth, gotcha.

sam  17:55  
And then you would So, what about like the just like the scratch pad that's built into like the model outputs, like with extended thinking or something like that, why not just use that instead of

sam  18:05  
having the call tool plan?

Mark Mote  18:08  
Yeah, because it's, it's a bit of an iterative process. So the the thing might be,

Mark Mote  18:16  
what's the cost of

Mark Mote  18:20  
a rate from or a 40 foot container of tables from Shanghai to San Diego. You can't really just use reasoning for that, because it requires a database lookup, and worst case, searching through emails to at least return something useful if we don't have the rate right? So it's more like, check this, did I get the right answer? If you did, that's the optimistic case. Then you can return it very quickly. If you didn't, well, search through the information that you do have and try to at least return something helpful.

sam  18:59  
If we go back to the to the initial system you walk through, or even, like any other products you built in your most recent startup, if you were to restart from scratch today, what might you do differently? If anything at all, it's okay to say, No, yeah,

Mark Mote  19:19  
I think I would have used MCP a little bit more rather than rolling my own tools. And let's see, I think this is more of something that we really didn't get around to because it wasn't a big enough need. But I think indexing the emails would have helped a lot in terms of being able to look up relevant information.

Mark Mote  19:53  
So do some kind of semantic search on all your message history. Makes sense?

sam  20:02  
One other important part of his job is working very closely with customers. As we kind of mentioned earlier, right? That's sort of like whiteboard to debt, to demo, to iterate, to iterate, iterate, iterate. That's like ready, but it's like very close to what our costs might look like for giving customer how did you work with customers in your various roles as a founder? Did you ever like, yeah, did you do like, still recalls with them? Ever like, just would love to understand what you've done

Mark Mote  20:32  
in your customer facing context, sure. Yeah. So as at Python, I was CTO, so that was my main job, and building was my second job at Rooster. My job is to code and occasionally hop on the calls, which is nice because I don't need to set them up. But yeah, so Python was probably more experienced there, right? We did a lot of discovery on every idea. Tried to run the sales process as much as possible. Try to understand when customers actually didn't like the thing that they were saying was okay. So being able to, you know, read the thin line between being nice and not liking it. Yeah, I can dig into any of these parts, if you like.

sam  21:21  
So one thing that's really important about this role is that when you're first like, imagine you're in that let's use like, the metaphorical whiteboarding session again, when you're in that room for the first time, you're like, meeting people for the first time. Yes, you walk in with like, the anthropic brand behind you, but sometimes, especially, like very, very, like, established enterprises, you don't, like, live in our bubble, right? You're just like, at first, you're just a little bit of an outsider, right? And they're kind of like, listen, I know we signed up to, like, build this thing with you, but they're skeptical, right? They're like, I've been working on this thing for the last 17 years. You know, who are you to tell me that, like, you're gonna build a better time. So, like, how do you build trust in an environment like that? Like, what is your process for going from like that first meeting to the customer loving you and you're getting it in a nice iterative feedback? What is your what is your how would you handle that?

Mark Mote  22:17  
Yeah, I mean, it's all about listening, right? If someone doesn't, if someone's skeptical that you should even be there, then you need to understand why that is, and in such a way where you could repeat it back to them. I think that's the first step in building trust, right? If I've found you can lower an amazing amount of barriers with people, if you actually just can repeat back to them in your own words, what? What is uncomfortable about the situation? So I'd say, go in there with low ego. I mean, we're Hey, I'm working for you. If this doesn't work out, I'm gone. I want to make your job better in some way. And I'd like to really learn from you that's, that's kind of how I would approach it.

sam  23:11  
Did you ever run into any situations? Look, all of

sam  23:15  
our customer engagements are actually quite nice, like this. Rarely ever happens. But you ever into a situation where you're just, like, misaligned with the customer? The customer is like, you know what? You told me you're gonna build this thing I built like, you know, it's not without what I want. Or like, maybe they misunderstood you. And if so, like, how did you how did you handle that? Or how would you handle that? I guess

Mark Mote  23:38  
so. The question is, misaligns.

Mark Mote  23:42  
Misaligned. Maybe they don't like what you're building, or you think, you know,

sam  23:48  
misaligned customer expectations. You ever end anything like that? Yeah, yeah.

Mark Mote  23:52  
So I think we were selling SAS. We had this one customer, who they, you know, they were very non technical, and they had very high expectations on, you know, what we could build even in the course of the week. So they would say something like, Hey. I mean, I would, I would love an agent that makes it where the no one at my company has to respond to an email ever again, right? And you need to kind of go through and say, like, well, here's what I can do, here's what I can't do, right? So in that case, it was misaligned, both arguably, in an ethics territory of, you know, I'm I, anything I build in a week, shouldn't be responding to emails to your customer. Second was in more of a technical realm, which is, we have other contracts and, you know, that's, that's, it's a lot to try to push in a week. Yeah, so what? What I told them was, you know, just hey, let's find the middle ground. Let's carry out this experiment. Let me give you a demo. It'll be a dashboard where you will look at the responses that this AI comes up for your emails. You'll hit this in button. You'll hit the approved button if you like it. We can continue with that, yeah?

sam  25:23  
I mean, I think that the ethics thing is actually quite important here too, because we get, yeah, we can, you can imagine, we get similarly, like crazy

Mark Mote  25:31  
asks, yeah, there's a lot of AI hype, right? And people Yeah, they think you're just

sam  25:37  
gonna, like, sprinkle magical dust. The situation, exactly, yeah.

sam  25:46  
What questions you have for me about the role?

Mark Mote  25:52  
A lot. So what

Mark Mote  25:56  
does the team look like? Is maybe where I would start. What does the average person on the team look like in terms of backgrounds? What's the size?

sam  26:07  
Yeah, so the backgrounds are a mix of

sam  26:11  
people who came from larger either whether it's like big tech or enterprise environments where they were like, the person who went really really deep on AI and, like, went to the rest of the company and built all the AI tools that they use. Or, like, maybe they worked on a cutting edge product one of those companies before, and they wanted to come work at a lab. There's also a lot of there's a lot of ex founder backgrounds, for people that were, like, very early hired at startups, who are, like, good under ambiguity, and like, really think on their feet and ship things. It's a mix between those two profiles. I would say,

Mark Mote  26:47  
what was the second part of your question? Oh, I guess just the size of the team. Oh, size

sam  26:51  
of the team today. We are, I believe,

sam  26:57  
30 people globally right now.

sam  27:00  
Okay, mix between London, New York, NSF,

Mark Mote  27:04  
okay. And presumably a lot of travel.

sam  27:09  
There is a fair bit of travel, a little bit less maybe we would have expected, and most of the travel is usually within region. So if you're in New York, most of your travel will be to like various customer HQs in New Jersey and New York. Specifically use it if you're on the West Coast. You know, if you're based in SF, a lot of the travels, like tip throughout the Bay Area, but there will be customer engagements where we have to go to, like Minneapolis or Houston, that those are going to happen, right? But even in those cases, I think the model will end up looking like, you go there for a week a month, you go there for maybe two weeks in a given month, if you have more of an intense sprint, and then you can do some work remotely, too. Like, I think that unless it's a really, really locked down customer, that model, I think will be, will be effective.

Mark Mote  27:57  
Okay, how does the the the the information that I would be learning as an FTE and iterating with customers. How does that feed back into the product, if at all?

sam  28:14  
Great question. So our play outward actually came out of product back in the day. So we have, like, just maintain a really good, like, line of communication with them. And what we try to do is we try to allow folks, especially when you're in between projects or ramping up, we push folks to go work on an internal product or research works, you know, so like, for example, I thought people on the team go ship features within hard code. There's research initiatives that I can't talk too much about, that folks have, like, tapped in and worked on, and it's a great thing to do when you have like, a little bit of downtime, because every once in a while you'll have like, three weeks between projects. In that three weeks like, that's a great time to go take on, like, a product workstream. And usually it's just like a fun thing to do. Yeah, you add value internally. And it also is, like a huge credibility booster. When you go talk to your customer, you can say, Yeah, I should that thing. We can

sam  29:03  
plug it,

Mark Mote  29:05  
yeah. I mean that, that would be a dream, right? Yeah.

Mark Mote  29:10  
So how would you how's the split between the time? Maybe, if I, if I'm guessing, 90% hands on keyboard, 10% interacting with customers? Yeah.

sam  29:21  
It actually really varies depending on what the where the product, the project itself, is. I think it's more like 7030 Okay,

sam  29:29  
7030 and

sam  29:30  
there are, like, early stages in the process where it's like just that, again, that loop where it's like whiteboard, demo iterate, that's like a very customer interview process, such as, you like, by yourself in a room, writing code. It's like an hour long conversation with the customer, then you by yourself writing code for four hours, then communicating with the customer again, and then, like, it's that kind of route, right? It's not purely, it's not purely, just like doing edge work and then throwing it over the fence. It's very, very

Mark Mote  30:00  
collaborative, right? That makes sense. What do you think is most difficult for new people to

Mark Mote  30:07  
get up to speed on? Typically,

sam  30:13  
that's a really good question. I mean, I think it's, it's a mix between the just like inhaling all the information about what, what like a great deployment looks like. I'm like, a frontier use case. So, like, using our models like the the nth degree, sometimes that that is just like a lot to take in at once. Most people don't have any issues with that, though. Honestly, most of the most of the challenges are around, like, the questions I pushed on earlier around, like, hey. Like, how do you build trust with the customer, right? Yeah, so we usually have to coach more there.

Mark Mote  30:45  
That makes sense. Okay, yeah. I mean that

Mark Mote  30:48  
that is the hard part, right? And that's, that's the part you want to be good at.

Mark Mote  30:53  
I think kind of related one is, is what,

Mark Mote  30:57  
what does it really take to be successful? So you know, in any year, when you're reflecting on this, what would I need to do so that you look back and think that was the best decision I've ever made?

sam  31:12  
Yeah, I mean, it's a great question, I think, like the biggest thing is going from, Hey, I just showed up at this company. I got hired. I started to impact soon, like, jumping on the project within, like, your first month is sometimes helpful. And it's like, you would be like training and onboarding, you have process and stuff. But from there, it's like, can you take ownership over, like, a critical part of the worship of the customer? You take on, like, a very big, important aspect of it and ship the thing, doing that a number of times, and it being a go to person, we can say, you know, what, if, if Mark is on this project, it's going to go well, because that's really what we're trying to get to then, right? Like, I would, like, I want everyone to be like the caliber of person who can be just like a linchpin, right? Project, I can take, like, the most important thing we have in the pipeline, put it on your plate and just be like, sleep soundly at night knowing that you've got it. That's bad,

Mark Mote  32:07  
that's good. I can also see why you you focus a lot on people with founding backgrounds. That makes sense?

sam  32:13  
Yeah, it's often

sam  32:16  
a helpful background profile, right?

Mark Mote  32:19  
What surprised you the most since you joined anthropic or, I guess, since you've been here for a while, maybe a surprising change?

sam  32:29  
That is a good question, and you have to run in a minute. I'm a little bit late for another call. I'll answer this one, and we can drop, I think, in terms of surprising things, so many things. I think the big thing is just like, the speed of growth has been insane, you know, like, much faster than I would thought. In many ways that's That's amazing, and, like, I wouldn't have had it any other way. But in other ways, it's just like, creates, like, incredible demands on timelines that are just, like, really, really compressed.

sam  33:00  
And the speed

sam  33:02  
at which this place evolves is truly insane. It is, it is, like, it is a lot. So that's like the biggest thing, I'd say. But it's less surprising and more so, like, just, like a good feature of this place, yeah, absolutely. But it does. It does, again, the compressed timelines and like, the speed at which things move is it always will. It always says, creep up on you, even if you can, like, intellectually come around to like, yeah, it's gonna move as fast, you know,

Mark Mote  33:32  
intuitively feeling it and understanding it as a different thing, yeah, I got you. Okay. Last thing is, just, did I forget to ask you anything that you anything that you think is important that

sam  33:45  
I should have asked. No, I don't think so. My recommendation for you would be like, You should read up on like, everything that we put out on building agents. Yep, you should read up on our tool use documentation. Just like, get really familiar with like, how we view like an agent loop. And just like, I would recommend showing up to, like, next, like, the next interview you do very prepared on that front, like,

sam  34:11  
just like a point of view on, you know,

sam  34:14  
again, how you build an agent and

Mark Mote  34:17  
then how you might make it better, yeah, yeah, that makes sense. So rather than, you know, thinking through very slowly a question, you asked me about something I built a year ago and kind of stumbling a bit. So yeah, I'm

sam  34:30  
a big believer in, like,

sam  34:33  
there's certain things you can learn. And most founders

sam  34:37  
have you really learn things incredibly quickly. I just, I would want you to show up to the next interview prepared on that regard, because that's like the main, the main,

Mark Mote  34:46  
yes, yeah, that's, that's great advice, yeah, some tips

sam  34:49  
for future rounds. Okay, Mark, it was good to you.

Transcribed by https://otter.ai
