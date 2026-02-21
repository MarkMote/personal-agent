Unknown Speaker  0:17  
It is, This is I

Unknown Speaker  0:48  
Hey there. How are you good?

Unknown Speaker  0:55  
Yeah, nice to meet you. Yeah, likewise.

Unknown Speaker  0:58  
Other quick intro. So I'm Dave head of the automation group here at radical AI. My background is about half in manufacturing engineering design, machine design automation, classic industrial engineering stuff,

Unknown Speaker  1:16  
then pivoted to leading product development teams, so maybe printing space some fancy electrified food trucks and appliances,

Unknown Speaker  1:26  
designing, like electro mechanical products,

Unknown Speaker  1:31  
and then, yeah, I've been here about three months, so relatively new, but I've definitely, like built into it the the team that I'm over. I know you spoke with Ray.

Unknown Speaker  1:45  
So Ray's a roboticist. So we have a few roboticists, electro mechanical engineering, mechanical engineering and project management, or program management, under the automation group in our groups, our group's focus is building out the actual autonomous lab. So the machinery, kind of material handling, the robotic loading on loading vision systems, the

Unknown Speaker  2:13  
kind of orchestration layer. There's like a blurry we do have a software team that works on kind of the orchestration layer, and like, the back end of the system.

Unknown Speaker  2:24  
So there's like a blurry area, like, how far up kind of in the stack we go, but we, we do write some, we write software to interface with that orchestration layer that is basically saying, like, okay, the sample now needs to go to this machine. Now it needs to go to this machine. I have an error because my robot arm gave me, like, a current, an over current. So I want to, like, push that back up and do something with that message.

Unknown Speaker  2:52  
And, yeah, in terms of radical AI, how much do you know about the company?

Unknown Speaker  2:57  
Yeah, I looked at the website.

Unknown Speaker  3:00  
It's so I know it's AI agents and robotics executing on material science research, it seems. Yeah, I'm still trying to figure out exactly, you know, the details around what the business model is, kind of what the scale of the business is. But, yeah, as I understand it, it's, it's kind of like, you know, Google's AI co scientist, but with the robot attached, yeah, yeah. So like, yeah. I mean the product is basically in the value is, like, with accelerated material discovery.

Unknown Speaker  3:37  
So

Unknown Speaker  3:41  
say, a partner. I see you had experience with, like, Air Force Research Lab AFRL, so

Unknown Speaker  3:49  
we they're actually, like a partner of ours.

Unknown Speaker  3:53  
So we ingest desired material properties. So say, say, for like, Mote tough applications like turbine or hypersonic flight, where it's like, okay, we want to metal with this hardness, really high melting point, only 500 C melting point,

Unknown Speaker  4:18  
and it can't, like, oxidize, you know, it can only lose like 5% weight in the chamber at like 1800 degrees. So and then these other properties aren't important to us. So we have an AI model that basically, yes, like Google scientists. It scrapes all like the open source materials databases, 10s of 1000s of research papers on refractory, high entropy models, and then we have our internal base that we're like accumulating from data from this lab that will give some recipes to the lab to make. So it'll say, Okay, make. Make a 20% tungsten, 10% aluminum, 5% Molly, you know, this percent titanium sample, we think that that'll meet these, that might meet these properties. So the lab then executes that. So it'll, it'll like mix the mix pellets of elements, built it into a little ingot, cut up that ingot, Polish sections of it so that it can be used for different characterization machines like diffraction, X ray, fluorescent electron microscope, hardness, compression testing, oxidation, furnace testing. There's

Unknown Speaker  5:38  
kind of like an ever expanding characterization loop,

Unknown Speaker  5:42  
some of those are destructive tests. About half are destructive, half are not destructive. So you kind of have this, like samples kind of go in, like an array of different loops, and then, based on those readings, the AI then takes in those readings. It also analyzes that because some, some of the readings were quantitative, like, this was the percentage aluminum that I started allying. You lose a lot of aluminum for these refractories. Like, this is the percentage

Unknown Speaker  6:15  
after alloying.

Unknown Speaker  6:17  
Some are less stuff, less quantitative, where it's like a picture of a grain structure,

Unknown Speaker  6:26  
where basically, like, when you zoom in on on a metal we basically get like a kind of like cobblestone street looking thing that tells you, like, how, yeah, tells you

Unknown Speaker  6:38  
like your grain structure, which is critical So that that could go through, like, an AI and kind of machine learning engine to, like, evaluate that, you know, right, right? I'm imagining I can quantify that somehow, exactly, yeah, exactly. So we work on that too, so, and then yeah, and then that, that all feeds, and we just have this loop so, you know, like the premises is kind of even for a company like Oak Ridge lab or 3m like this, this process normally takes like, months,

Unknown Speaker  7:12  
right? Yeah, like, not, like, geared for it, so, yeah, it's basically the and the the we're focusing on metal alloys right now, particularly like high temp.

Unknown Speaker  7:28  
It's a class called refractory, high entropy alloys, where there's like a really big design space for learning, and it's

Unknown Speaker  7:38  
really like an in demand space.

Unknown Speaker  7:41  
But But basically, it's like, just like, essentially, like autumn automating, like the scientific discovery process. You know, you make a hypothesis, you test against the hypothesis, you take your learnings, you make another hypothesis, right, your PhD. So you know that I don't have to

Unknown Speaker  8:00  
explain the scientific method to you. But, yeah, yeah, if you think of, like, anytime you've done like, a big design of experiments that you're like, oh shit, this is going to take like, six months to do, you know, just not going to do this. Like, like our lab is, is just the idea of, like, doing all these, all these experiments, building up all this knowledge, and it gets kind of forever stronger, and it's, it's not just like metallics, high temp, low temp, conductor, thermal, you know, thermal materials, plastic, ceramics. So, like the, the kind of hypothesis, like works for American

Unknown Speaker  8:37  
applications, right?

Unknown Speaker  8:39  
Yeah. So, so our product is the material, in terms of, like, revenue and business model, there's like, you can partner with the company, and you can just say, like, this is your alloy composition. That means your once the I the ideal where we want to get to is more vertically graded, integrated, where we're actually, like, owning the manufacturing through partnerships, or through like acquisition, where we're actually making and selling the metal that way. There are a lot of like, right? We've had it, but there's also, like, a lot of trade secrets in this game. So, yeah, so not just the prototype, but the prototype to product. Yeah.

Unknown Speaker  9:23  
So, yeah, that's, that's the company overview.

Unknown Speaker  9:26  
Wow, yeah, what?

Unknown Speaker  9:29  
What stage is all this in the Apple app that has the core characterization involved so we it's not fully automated at all our Yeah, I'd imagine that's a huge hurdle. Yeah, there are stations that are automated. We've crossed off, like a lot of the simpler ones, like taking up, taking the sample, loading it into an x ray on loading it, loading it into, like a harness test to unload it. So like the simple kind of machine tending, just like loading unloading, stuff that's been automated. We started to automate some of the harder stuff.

Unknown Speaker  10:07  
You know, it's a challenge because, like, a lot of these machines exist with no intention of ever automating. So it's like, you have to make a lot, we have to make a lot of decisions, which is like, do we want to leave the machine as is, and just like, figure out the API to talk to it, like minimum and just essentially automate the manual process? Do we want to, like, do some redesign of the machine? Do we want to just start from scratch, you know, and that each each process kind of has its own, its own path.

Unknown Speaker  10:43  
You know, I know you did vision, there's a couple, there's a couple processes that require some pretty tricky vision.

Unknown Speaker  10:51  
There's also, I'd say, like, a lot of just general processes where kind of simple vision implemented fast would help a lot, just for like, sample location, right? Yeah, instead of, like, dead reckoning.

Unknown Speaker  11:07  
So, so, yeah, a lot of like, the challenge isn't, you know, we're not, not building custom robots.

Unknown Speaker  11:18  
We the challenge is, basically, we're building like a very flexible automation system. So whereas I come from a lot of experience in the industrial space where, like, you're using a robot to do one thing over and over, as fast as you can,

Unknown Speaker  11:38  
right? So as fast as you can and as reliably, we're like, a total you put like, our those values are kind of like on their head here, like robustness over optimality, it seems, in a way, yeah, exactly, exactly. So it's like, how can we use a lot of Cobots or Universal Robots?

Unknown Speaker  11:58  
So it's like, how quick can we take this six degree of freedom robot, have this like Ripper family that we've already brought, you know, integrated staff for have this like vision. Have these like, three different vision systems that we've already like, integrated, right? How can we like, make that really scalable?

Unknown Speaker  12:18  
So we have a lab in Manhattan right now East 29th Street that we've like, maxed out. It's kind of amazing. We've been able to do this in Manhattan, but we have a space at the Brooklyn Navy Yard over building 20. Okay, yeah, I live in Williamsburg, so not too far away. Yeah, we took over the nanotronics space. If you look at building 20, it's like an unbelievable space, okay,

Unknown Speaker  12:52  
it's like, super modern. It's an 1800s building, but the inside is like, looks like, like a modern, Scandinavian. I interesting.

Unknown Speaker  13:03  
So we'll be moving there in the next, I don't know, three ish months. Okay?

Unknown Speaker  13:09  
And that gives us, but we have, so we have machines coming in that we can't put in our location, but we can put there just because of, like, their size and the utility requirements. That makes sense. Yeah, yeah. So that's kind of, that's, that's like, the challenge, I'd say, is, is really, like, moving fast, because we have, we have a lead in this space time wise. But there are, there's, like, a lot of attention right now to

Unknown Speaker  13:41  
to, like, autonomous labs using AI or material science. I mean, yeah, I'd imagine it's such a valuable problem if you can figure it out exactly, exactly. So, yeah, we need to just move really fast to kind of, kind of win this game. Yeah, yeah, that makes sense. What would you say is the biggest bottleneck, I mean, out of material science, agentic research robotics. So a lot of like, the character, a lot of the characterization equipment is,

Unknown Speaker  14:17  
it's like, really, like, legacy equipment, like, like, we bought this million dollar piece of equipment that does, like, extreme thermal load testing. So it brings it up super it's like 175 amps it brings it up, and we're doing this tiny sample, so it brings it up to like, 2000 degrees in like seconds, and then puts these forces on it. But you know that this basic design has been around for like, 20 years, like, no intent to, like, automate, and now we're trying to, like, reverse engineer and automate that.

Unknown Speaker  14:52  
And you know, with automation, like, first, like, there is value and there's there's just like value in having, like, a total closed loop system.

Unknown Speaker  15:02  
You know, there are challenges there. Because, like, full, lot of full, fully closed loop. Like, once you dig into things, it's like, Oh, yeah. But this person's like, changing, like a sanding pad once every 20 minutes, right? Yeah? Definitely has, like, a fat tail of exceptions, yeah, yeah. So, like, so, like, there's challenges and just that, like, it becomes a really deep pit of, like, projects that you find, the machine example, is just a challenge of, like, integrating with the machine. And that's like, a one of a kind machine in the world, like, there's one company that makes that, and we have to, so we have to, like, use that. Some of these machines have, like, six to 12 month lead times, which for us is like, completely insane, like, right? We're a different company every six months, you know? So

Unknown Speaker  15:51  
just like moving moving fast in a space that just traditionally does not move fast,

Unknown Speaker  15:58  
yeah, yeah, that makes sense, and it's good, because if it was easy, then, like, it wouldn't be so valuable. You know, like, these are the reasons why, like, people have done this for, like, liquids dispensing, you know, where you're, like, pipette dispensing different liquids and optimizing things by having chemicals. But that's it's just like, people have done that because it's like, easy. It's from a hardware standpoint, it's easy, right? That makes sense, yeah, like, melting, melting metals that don't want to really melt together. It's just, like, really tough.

Unknown Speaker  16:33  
So if we, I'm always looking for, like, okay, what can we actually do? Like, where can we, like, get our edge,

Unknown Speaker  16:42  
you know. So not just like, taking a person out of the loop, but what can we actually, like, do better than a person can do either because of, like, environmental conditions, the using vision, you know, that's that's how we can set ourselves up. So, and then the challenge. There's always a challenge of just, like prioritization. We want to do a million things.

Unknown Speaker  17:06  
We're trying to hire, like a technical hardware team in New York City where, which is tough, you know, you find, like, really good people, but it's a small pool, right? Yeah, yeah, yeah. Uh,

Unknown Speaker  17:23  
but yeah. So that's, that's, that's like a pretty, I think, a pretty good description of, like, where we're at.

Unknown Speaker  17:31  
We have about 40 people total company, and it's like of the 40 people, like 37 of them are, like some sort of engineer, so material science PhD. Oh, really, okay, yeah, which I, like, love, it's, it's actually, like, my first job where it's, you know, we're like, marketing person, and, you know, we'll be doing those things, but, um, yeah, I'm used to, like, customer support, sales go to market planning. You know, there's meetings every day. So this, this is really great for me, yeah, but maybe so, Ray told me a little bit about your Convo.

Unknown Speaker  18:11  
And, yeah, you don't have, like, a traditional resume in that fight. Yeah, you went all the way up to PhD, but then you did some entrepreneurship stuff, yeah, which are kind of two ends of some kind of spectrum in a way. Yeah, exactly, exactly.

Unknown Speaker  18:28  
So I talked to Ray, and I was like, does he, like, actually want to do this job? So my first question, so, so yeah, maybe tell me,

Unknown Speaker  18:38  
yeah, like, a little bit about kind of your chronology, like how you came to this and, like, what are what you're really looking for? Now, sure, yeah, it's a great question.

Unknown Speaker  18:50  
Yeah, let me decide how far back I want to go.

Unknown Speaker  18:53  
Started in aerospace engineering, actually, I wanted to be a pilot, and then I realized I like the math a lot more than being up in the sky where you're essentially a bus driver.

Unknown Speaker  19:07  
Yeah, I the most. What intrigued me about aerospace was control systems. That led me into robotics. So did the robotics PhD thesis on safety critical control essentially, you know, building safety filters, you can think of like when you're in the car and it breaks for you, but more general than that, essentially, you know, have you moved fast without breaking things?

Unknown Speaker  19:34  
And then, yeah, I,

Unknown Speaker  19:40  
I was really thinking JPL after graduating, and, you know, there were a few robotics companies that were really interesting, but also I just, I had this idea that I really wanted to see through so, and this was in robotic perception and for autonomous vehicles, kind of a shared model of the world where multiple robots can collaboratively solve the perception problem.

Unknown Speaker  20:10  
Yeah, so did that. Tried it out. Ended up just really liking the founding lifestyle.

Unknown Speaker  20:17  
I think we took the YC advice, which was, you know, build something people want, which means we iterated a ton and eventually ended up in supply chain with AI agents.

Unknown Speaker  20:30  
And then that led me to my next startup, which was supply chain with AI agents.

Unknown Speaker  20:35  
But, yeah, I want to move back to robotics, because, you know, build something people want is kind of only, you know, half the half the equation. I think you also want to build something that's actually energizing for you and that you know you're passionate about. So, yeah, that's, that's kind of where I am now.

Unknown Speaker  20:56  
My co founder just, is

Unknown Speaker  20:59  
it that like, when you were doing the business that you kind of do, kind of want to position yourself back in where you're spending like 95% of your time on, like engineering, technical problems, versus, like, the supply chain woes of, you know, a startup or, yeah, that's essentially it. I mean, at a bigger scale than you can get with the startup, I think something more in the area I'm passionate about, which is robotics, ideally, you know, a great application, which I think this is. And then I'd say, you know, on the spectrum between, you know, here is where you're only doing deep research and writing papers. And here's where, you know, hey, here are some specs. Go implement them.

Unknown Speaker  21:48  
I'd maybe want to be a quarter of the way to half the way. So, you know, ideally it's, you know, you start the day on a whiteboard, and it's a very challenging, open ended problem No one knows how to solve, but by the end of the day, or at least the end of the week, you're actually trying to ship something, right? Yeah, not ship in this case, just, but

Unknown Speaker  22:15  
when I, when I came here, I realized, like, the robotics team says, like, oh yeah, we're gonna ship it, which just makes like, launch it in the lab, right? Yeah.

Unknown Speaker  22:24  
Okay, cool. What's your what's your like handle, hands on, experience with programming robots to do tasks like the Android vision systems. Experience, what was the last part of that question? Oh, basically, like, hands on experience programming like robots and setting up vision systems just to orchestrate tasks, sure, yeah, be or do an inspection, yeah? Any kind of like application, yeah, yeah. So wide range of projects in grad school, but, you know, that was mostly on the prototype part. You know, real hardware, but you're only getting it to the point where you write a paper about it at pi fear, we did vision. That was our main product. It was admittedly in a pretty narrow area, but it was, you know, 3d camera based

Unknown Speaker  23:25  
multi camera perception, which means you identify the object and then you track it in 3d space.

Unknown Speaker  23:33  
So, yeah, that was very hands on.

Unknown Speaker  23:37  
Coded on that just about every day for the first year. Okay, yeah,

Unknown Speaker  23:44  
okay. So a lot of what were you?

Unknown Speaker  23:49  
What were you actually doing, making like point clouds and analyzing that or, yeah. So the wasn't point clouds, it was more get a bounding box. And so first step is identify what the object is, use something like, you know, YOLO, and then track it, and then project it into onto a ground plane, essentially add a Kalman filter, and then you get both the position and the pose.

Unknown Speaker  24:19  
We experimented with some things like key point detection so that we could get better bounding boxes. But you know, essentially, what you would get is, you see a person, you get a cylinder around them, you see a car, you get a box around it, and this is all protected into spatial coordinates. Got it, yeah, okay,

Unknown Speaker  24:39  
if you're, if you're, like, given a project here, that's just

Unknown Speaker  24:46  
say, like, programming like a universal robot for, like, a machine tending. So say, so like, you have some IO from the machine that you have to take in, and then you know you're giving some some signals, just to say, like, Okay, I've loaded now, close Jaws, okay, I'm done. The machine's done. Now, open Jaws, tell the robot it's okay to pick it up. Robot goes on track. Like, how would you how would you want to, like, kind of come up to speed and, like, learn, learn how to do that we use, mostly like Ross, right?

Unknown Speaker  25:24  
Programming, right?

Unknown Speaker  25:28  
Yeah. So the question is, essentially, you know, for for the basic loops that you're in, how would I come up to speed on how you're doing it? Yeah, yeah. So, I mean, definitely the way I like to approach any problem is to try to solve it naively first. So just, you know, I would think about, without looking at their code, what am I actually doing? Spend a couple hours that way, look at the actual code, get familiar with kind of the software and frameworks. Probably ask a few questions, and yeah, figure out what my gaps are.

Unknown Speaker  26:03  
Okay, okay, cool.

Unknown Speaker  26:12  
And you're in New York City now, yep, okay, cool, oh, yeah, yeah, okay, great,

Unknown Speaker  26:21  
yeah, I think what I'd what I'd like to do is set you up to talk to Hassan. Was like, kind of like we, I mean, him and Ray are similar experience. They just have different experiences. But just to talk through, like the tech a little bit

Unknown Speaker  26:39  
he can,

Unknown Speaker  26:42  
I'm I'm, like, my I'm like, a mechanical engineer by training. I know enough to, like, manage some software engineers, but I don't actually, like get into the code, you know, makes sense, like, super well commented for more code doing something on the machine. So I'd like to connect you with a son who can, unlike, maybe a half an hour call, who can go more like into the tech with you. Sure? Yeah, that that'd be very interesting. Yeah. Okay, great.

Unknown Speaker  27:14  
Any other questions I can answer for you?

Unknown Speaker  27:19  
Let's see.

Unknown Speaker  27:23  
We got the big ones,

Unknown Speaker  27:28  
yeah, what's, what's been your impression over the past three months? Just kind of vibe wise about the company, to be honest. Like, like, this is honest. Like, yeah, I guess I've been in industry for like 20, like, 25 years, this is, like, the best start I've had any job reflecting on, like, Why do I like this job so much? Like, it is a, you know, like, like any New York City startup it is, you know, the work can be, like, stressful. Sometimes feels overwhelming. I mean, you can do it again, more than more than anyone, and that's like, that's like, par for the course for startups, right? So, like, there is that it's but, yeah, I was reflecting, like, a couple of weeks ago on, like, why? Like, why do I even though this job is hard, like, Why do I like it more? And I think it's like a few things, the one reason is what I explained before that, like, a lot of my stress at other jobs is, like, you know, dealing with operations, dealing with customer support, like supply chain issues. You know, here I spend, like, pretty much, like, my entire day, like, working on, like technical problems and like managing technical people, which is like pleasure for me, you know? Yeah, absolutely, yeah. So it's like, and then the team I love, like, I've done, like, you know, the remote work from home, stuff I've done, like, the split model, we're 100% in office.

Unknown Speaker  29:11  
And honestly, like, I love, I love it, like having the whole team in every day.

Unknown Speaker  29:18  
Before I took the job, I was like, it would, it would be nice to still be able to do like, a hybrid thing, but, and the company's like, really hardcore about that being a requirement, effort person, you're kind of done that's made things like, really great, just in terms of, like, team, team dynamic, and it's really helped because, like, decisions are made, like, on the fly. So if people aren't here, even with people here, like, people are still like, oh, like, this decision was made two days ago. Like, why didn't I hear that? You know, yeah, there's still communication issues. But like, it's just the team really, like, drives off.

Unknown Speaker  30:01  
There's, like, it's like, a high skill, fairly low ego team, right? People are with like, high performers. You get like, strong willed people, which is good, like, you want that challenge as a manager, you know, you don't want people just like, oh, whatever, to be going, yeah, it makes it super easy to manage, but not very productive. So, so we have like, a great, great mix of people that's like, you know, you only get in like, New York City or San Francisco. We have like, a lot of different backgrounds coming together, right? So, so, like, everyone learns a lot from each other.

Unknown Speaker  30:42  
Oh yeah. It's great to have like the material science PhDs to just like, walk up to and ask questions like, What are you exactly working out of this test? Like, is this more valuable to you, or is this more valuable?

Unknown Speaker  30:54  
Is really awesome. And also to have like the AI ml team here, which is something that, like me is primarily a hardware engineer I haven't had like, exposure to, but they're, like, a really talented group, and it's just, like, super interesting to see that process as well.

Unknown Speaker  31:11  
Yeah, yeah, yeah, no, I like the way all that sounds. I mean, the the in office is, you know, it's kind of a pain, but I think it's worth it, right? It's like, yeah, you hate to go to the office, but you love to be there.

Unknown Speaker  31:29  
And then the wide range of backgrounds definitely sounds like a plus. Just, I'm a generalist at heart. Sounds like most people there are. So, yeah, yeah, absolutely, yeah.

Unknown Speaker  31:41  
I think, oh, yeah, I guess the last thing is, like, when, I mean, whenever I look for, like, any job, it's just like, like, I like, I like a challenge, like a bold vision, you know, where, like, success is not assured, but like it's gonna, you know, it's like foreseeable, like, like you, like you have the resources to actually, like, get there the goal. So, like, we've, we've, we've done it. We did a good raise.

Unknown Speaker  32:07  
Really good seed raise.

Unknown Speaker  32:10  
So the founders, you know, when I'm interviewing, it's like, always like, do the founders, like, know what's required to actually, like, get where they want to get? You know,

Unknown Speaker  32:23  
a lot of the times it takes a lot more resources than, like you first think to get somewhere.

Unknown Speaker  32:30  
But I'd say, like, the founders are pretty level headed on like, what it's going to take to to reach our goals. So you kind of, like, have had this vision. The vision is exciting, and then you have to have the resources to actually, like, actually show that, like, the team can actually make it there, you know, right, yeah, so, like, That combination is here,

Unknown Speaker  33:00  
okay, yeah, I see we're at time. I can keep talking about this all day, but I'll let you go.

Unknown Speaker  33:09  
I'll connect you with the sun, and then, yeah, that'll be the next step. Cool. Sounds good? Really enjoyed the talk. Thanks for hopping on. Yeah. Great. Thank you.

Transcribed by https://otter.ai
