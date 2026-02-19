Answers to Common Interview Questions 

## UNIQUE TO EVERY COMPANY: 
- Why them 
- Intro 
- Discuss best role fit? especially if FDE 
- Answer to Thiel question

## Need to fit in 
- My Timeline 
- What I'm looking for role-wise

--- 

## What comp range are you looking for? 
I can't say that yet since it depends on too many other factors.  
Can you tell me what you have budgeted for role like this? 

Push #1: 
Really hard to even give a range, really most concerned with the role 

Push #2: 
I'd say 250-350 is the best ballpark, but again that's very subject to change

--- 
## Tell me about yourself (multiple versions)

> I'm a 2 time founder. I have a robotics PhD but my background was originally in aerospace engineering. I'm currently winding down as CTO of a Roostr. There I built the complete production stack of centered around LLM pipelines to automate freight operations. Before before Roostr, I was founder and CEO of Pytheia, a company that did camera based robotic perception

---
## Desired Role? 

> ONE-LINER: I want a role where I feel like I'm learning things: elite team, open-ended problems, whiteboard, shipping. Not implementing predefined specs. 

I'm looking for something in the Research Engineer sweet spot: 
- R&D-oriented work where I'm building real frontier systems and shipping things
	- not just implementing known solutions, or just writing papers. 
- Heavy communication with stakeholders is a plus for me, not a burden.

**The best case scenario** is I am on an **elite team** given a hard and **open-ended** problem, we need to **whiteboard**, implement it, and we actually **ship** something. I'm around people I can learn from, and I'm pushed out of my comfort zone. 

**The worst case** is narrow, already solved problems, where its just implementing specs  

---
## Whats your timeline? 
What to say: 
- I have light commitments there until March 16th, but I'll be part time until then 
- Earliest start date would be April 1st, as I promised my wife a vacation. 

Internal strategy: **Feb 23rd for T0**    |     Feb 18th for T1+ 

---

### Roostr vs Pytheia
Biggest difference is at Roostr, my co-founder sets up the calls and I hop on, at Pytheia, I set up all the calls: from talking to customers to 

## Why are you leaving Roostr
> Roostr is **still operating**, the product works, we are getting **inbound**, and I'm on great terms with my cofounder.
> But at this point the company is mostly in a **sales and operations scaling phase**.
> I'm personally **more excited about building hard systems** than running a logistic operation day-to-day, so this felt like a **natural transition point** for me.

---
## What did you do at Roostr 

I built the complete software stack for Roostr, everything from the payment portal to AI agents to search through email and process documents.

Roostr is a freight forwarder, its like a middle man but for shipping products internationally. 
At a high level, the job is to collect rates from vendors are selling spots on a ship, and sell them to buyers that need to ship.  
- it sounds simple, but its a 200B dollar problem
As our core tech, we built two workflows to automate this.  
- One was to process vendor data. Anytime someone sent us rates in an email, we would automatically process it and get it in the database 
	- this was the more complex of the two
- The second was a more general agent to reference data and answer questions 
Aside from that, we carried out a lot of experiments in other areas, like computer use, sales automation, and automatically managing shipment tracking.
We also did a few iterations in the first year before finding this idea. 

## Tell me about the procurement workflow
Right. 
The job was to automatically process rate contracts coming through email.
A rate contract is essentially all the information that you would need to define 
- how something gets shipped 
- where it gets shipped to
- and who pays for what
What made this difficult was that it had to be extremely robust in terms of what it could handle. 
- we could get 1 rate or hundreds
- could be in an attached document, or in the text of a previous email in the chain
- everyone had their own fees and terminology 
- and if we got anything wrong we had to pay for it. 
## How did the procurement agent work
So the pipeline was really a combination of LLM analysis and structured processing, with a dashboard for human review at the end. 
- first we get the message and decide if its something we want to pay attention to, ignore or respond to
- then we extract the relevant parts of the conversation and where we think the rates are
- based on this, we do anything from call a tool to extract the rates directly to call a tool to extract the rows of a spreadsheet in python 
- The final data get standardized, a confidence ranking is attached and it goes into the database for human review
- One useful thing here is that there is an audit trail, so when we are reviewing rates on the dashboard, we have a comment on exactly where the information was found
	- e.g. the rate from Shanghai to Sandiego has a suspicious price, I found it at row36 of rates.csv

In terms of the stack
- nextjs 
- python 
- digital ocean 
- mongo db


## If you were to rebuild X again, what would you do differently?
Procurement agent: 
- 




## How often were you interfacing with customers 



## Tell me about a time you had to push back on a customer request. 



## Can you go into more detail about the procurement agent at Roostr, like how specifically did it work 




## What didn't you get to do? If you were still working on it, what would you want to add? 




## Can you talk about a time you had to work with someone non-technical and explain the product there? What were the challenges? 



## Is there a time a user requested something that you had to push back on. 



## How do you think about making a great UI? 



## Give me a contrarian opinion you have about software 



## Tell me something you were wrong about recently. 
Give example

longer: I'm a baysian, if everything is a probability then youre not wrong just uncalibrated, likewise you are never right, just better calibrated. 



## Out of everything you've worked on, what are you the most proud of? What was the actual impact. 


## If you were to go back and try PYtheia again, do you think the idea would work?





---
## What did you do at Pytheia 
3d camera based perception. 
initially for autonomous vehicles , then for robots, then for analytics 

---
## Why did Pytheia shut down 
A long story 

---
### What are some of the things you learned: 
- Grad school, how to build something complex
- Startup: to stop conflating complexity with value
	- figuring out what to build is usually harder than knowing how to build it
- Distribution is important: people need to know about your product
- Strategic detatchment is everything: one of the most important skills in life is learning to keep a cool head in stressful situations. 

---
## My Evaluation Criteria 
- **Impact**: am I making a real change here? 
- **Alignment**: does the change I'm making align with my interests and beliefs? 
- **Vibe**: do i like the team and day-to-day?  that one is just a feeling, but its important

---
## Why bootstrap

It forced discipline. We had to make customers happy or shut down. If we needed capital to unlock growth we would have raised. At that stage we didnt.

--- 
### Whats your worst quality 
> By the time I become cognizant of the issue, it stops being an issue, but I recently learned the importance of **delegating**. I went from phd student, to founder to founder again. The idea that I can just hand a problem off to someone else rather than taking charge felt wrong. It was more about ego than what was best for the business. But a few months ago, we realized "hey we have a little money to outsource some of the work, it actually makes the business better" - though we mostly applied that to non-technical things, but it was impactful. 


ALT:
It changes month to month, as I become cognizant of something, I try to fix it, then I notice another area to work on. 
Something I'm working on now is to **stop being so biased toward immediate execution**. 
Its a great quality in startups, but if you always treat the thing most immediate as the most important thing in the world, you don't always take the time to solve the bigger problem. 
I was recently thinking back at my time at JPL and I noticed I did it there... 

--- 

## Any regrets:

We probably under-indexed on distribution over product and over-indexed on bootstrapping as an identity rather than strategy. In reality I think you should always just do the thing that works best. Some ideas would have benefited from the extra capital and ability to delegate

---
## Why do you like being a founder. 

The **learning velocity** is unmatched. You’re forced to solve real problems end-to-end under tight constraints, and the **feedback is direct**. Either you made the customer happy or you didn’t. Founding also forces you to engage with the full system rather than just one slice of it, which suits me as a generalist. 

> **ONE-LINER**: The learning velocity is unmatched. You’re forced to solve real problems end-to-end under tight constraints, with direct feedback. And it forces you to always be looking at the bigger picture: for example its not just a problem of how to build something, but what to build.

---
## What do you like
Like 
- Learning velocity of being a founder 
- Creativity and intellectual challenges of research 
- The concrete impact of shipping real systems
Across all those, working with elite teams is a major amplifier, both in terms of learning and day to day enjoyment. 

> I’m drawn to fast learning loops, hard technical creativity, and shipping real systems. Strong teams amplify all of that.

---
## What's your superpower?

> Adaptability: my whole career has been a cycle of facing some hard ambiguous problem, needing to get up to speed quickly. It was how I operated in grad school, and it is how you are forced to operate in startups. 

> Strategic detachment: Getting the benefits of stress and insecurity without the stress and insecurity themselves. 

> Really listening to what people are really saying rather than what they are telling you. A customer might tell you everything is great but be on the verge of churning. There's no magic bullet you just have to pay attention and go through it a lot of times. 

---
### Ever ship a bug to production
Story: chris and his dad 


---
## What were biggest learnings from Roostr and Pytheia? 



-----
## How do you think having a phd would give you an edge in this role? 


--- 

## Where do you see yourself in 5 years? 


--- 
## Tell me about a time you and a cofounder disagreed on something. 


---
## What motivates you? 
Impact, alignment, vibe 

--- 
## Whats your greatest acheivement? 


--- 
## How do you handle criticism? 
I steelman their case first, then I try to repeat it back to them so that its clear I've understood. Ultimately its data. If its a person I feel really comfortable with, and I have disagreements, I'll explain my reasoning. We will work collaboratively on finding the gradient. 

---

## How do you stay up to date? 
In grad school i had google scholar updates set up for all my favorite authors, 
now I subscrible to a lot blogs and newsletters, its also the main reason I use x. I also talk with friends about tech a lot. Finally, if I need to do something new, I'll ask a language model to give me a breif or do an analysis of tradeoffs and recent updates. 

---

## How do you measure success? 
Depends on the system;,. 

--- 
## Leadership philosophy
People are everything
Invest in high IQ high EQ high integrity high curiousity 
Good faith 

---
## What makes you unique? 



## Motivations beyond money? 


--- 

## How have you handled ethical decision-making?

*Tip: Not a trick question. They want to see you've thought about it.*

Think about: at Roostr, automating jobs that real people do. You chose to build tools that augment operators rather than replace them wholesale. At Pytheia, camera-based perception raises privacy questions. Your PhD work on collision-inclusive trajectories was literally about minimizing harm when things go wrong.

--- 


# 3. What did you learn from Roostr and Pytheia?

You don’t need all of this. Pick 2–3 bullets depending on flow.
- The gap between what looks good on paper and what works in reality is massive. I learned to ground systems thinking in real operational data and user behavior.
     
- Fast iteration applies to product as much as hiring. Treat experiments as default-dead and let evidence revive them.
     
- Distribution matters more than first-time founders expect. Great products don’t matter if nobody discovers them.
     
- I've become more pragmatic about capital. Bootstrapping was valuable for focus, but I now view funding as a tool to accelerate impact when used deliberately.

---

## How do you prioritize when everything is on fire?
In a 2-3 person startup, everything is on fire. You learn to ask: what kills us if I don't do it today?
For the 

Don't burn your house down to stay warm. 


- At a 2-person startup, everything is always on fire. You learn to ask: what kills us if I don't do it today?
- Framework: urgency vs irreversibility. Urgent and irreversible gets done now. Urgent but reversible can wait. Most things feel urgent but aren't.
- Roostr example: customer escalation vs fixing a data pipeline bug vs investor update all due same day — the pipeline bug was the only one that compounded if ignored.

---

## How do you balance speed vs quality?

- Depends entirely on what phase you're in and what the cost of failure is.
- Prototyping / exploring: speed wins. Ship ugly, learn fast, throw it away.
- Production / safety-critical: quality wins. My PhD was literally about this — safe autonomy means knowing where the line is.
- The real skill is knowing which mode you're in. Most mistakes come from applying startup speed to production systems, or production rigor to throwaway experiments.

---

## What kind of team or culture do you thrive in?

- Small, high-caliber, low-ego. People who care more about getting it right than being right.
- I do my best work when there's real ownership — where I can see the connection between what I build and the outcome.
- High trust, direct feedback, low process. I'd rather have a 5-minute whiteboard conversation than a 30-minute standup.
- I actively dislike: politics, performance theater, and environments where the goal is to look busy.

---

## What are you looking for in a manager?

- Someone I can learn from. Doesn't have to be technical — could be strategic thinking, product instinct, or just how they run a team.
- Clear expectations, direct feedback, then get out of the way. I don't need hand-holding but I do want honest signal on how I'm doing.
- I've been my own boss for 5 years, so I'm not looking for someone to tell me what to do — I'm looking for someone who makes me better at deciding what to do.

---

## Why not start a third company?

- I might, eventually. But right now the highest-value move is to join a team where I can go deep on hard problems with people better than me.
- Founding teaches you breadth under constraints. I want the inverse for a while: depth with resources.
- Also honest about timing: I want financial stability to start a family. That's easier to build inside a strong company than from zero again.

---

## Describe the most complex system you've architected end-to-end.

- Two candidates depending on what they care about:
- **Argus (Pytheia):** Real-time multi-camera 3D perception — detection, tracking, 2D→3D projection, Kalman filtering, multi-camera fusion via Hungarian matching. Hardest part wasn't ML, it was calibration across heterogeneous hardware and maintaining real-time performance.
- **Roostr ops stack:** Long-running LLM agent pipeline that ingested messy emails/attachments, extracted structured pricing data, validated against business rules, and automated 50+ step shipment workflows. Hardest part was reliability — wrapping stochastic LLM outputs in deterministic control logic.
- Pick based on audience: Argus for robotics/perception roles, Roostr for AI/agent roles.

---

## How do you approach an unfamiliar domain?

- I've done it enough times that I have a pattern: aerospace → CV → retail → freight → LLMs.
- Step 1: Talk to people who live in the domain. Customers, operators, domain experts. Listening > reading.
- Step 2: Build something small and ugly immediately. You learn more from a bad prototype than a week of research.
- Step 3: Find the structural analogies to domains I already know. Freight forwarding turned out to have a lot in common with finite-state control systems.
- The PhD trains you to get comfortable being confused. Startups train you to get uncomfortable staying confused.

---

## How do you give feedback?

- Direct but with good intent. I try to separate the person from the work.
- I learned at Pytheia that tension accumulates silently on teams. So I created a bi-weekly "state of the business" ritual — open forum, no agenda, just honest check-in. Chick-fil-A afterwards. That's why we're still close friends.
- When giving technical feedback: I try to frame it as a question first. "Have you considered X?" lands better than "X is wrong." But if something is actually wrong, I'll say so directly.

---

## Why should we hire you over someone with more [X] experience?

- Framework: depends on what [X] is, but the honest answer is usually range.
- Most people who have more years in one area have fewer years across areas. I've shipped production systems in perception, LLMs, controls, and full-stack product. That cross-domain pattern recognition is rare.
- I also have the founder filter: I know what matters and what doesn't. I won't over-engineer, I won't build the wrong thing, and I won't wait for permission to fix a problem.
- If the role needs a narrow specialist with 10 years in one stack, I'm not the right hire. If it needs someone who can own ambiguous, cross-cutting problems — that's me.

---

## What does good engineering look like to you?

- Good engineering solves the right problem simply. Coding was never the hard part — taste and judgment are.
- Concretely: clear interfaces, explicit state, fast feedback loops. Systems designed for the world as it is, not as you wish it were.
- The thing I respect most is engineers who know when NOT to build something. Restraint is underrated.
- Bad engineering is complexity that exists to make the engineer feel smart rather than to serve the user.

--- 
## Thoughts on AI and coding
First I'd say its important to not confuse means with ends. Your goal is to produce a great robust solution, how you do that is not important. 
Second: 
Coding was never the hard part, the hard part was figuring out what to build, how to understand customers needs and bring something ambiguous  to reality. Producing great code has always been important, but really great people are great because their taste and their judgement. 

