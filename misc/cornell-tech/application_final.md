
# REFINED FINAL VERSION (300 words)
Problem:
AI agents excel at individual reasoning tasks but remain limited for open-ended scientific discovery. For humans, research is fundamentally collaborative and cumulative, requiring branching directions, new ideas, and building on prior work. Current AI agents cannot participate meaningfully in this process. They operate in silos, lack persistent memory, and the ability to learn well across runs. Existing "AI scientist" systems have explored agent swarms as a way to iteratively build knowledge, but ultimately operate in isolation and in narrowly scoped domains. Failed ideas are forgotten, reasoning remains local, and knowledge doesn't compound over time or across organizations.

Solution:
We propose an open and distributed workspace where AI agents collaborate on research problems over long time horizons. It would enforce a collaborative workflow where agents mimic the scientific process: proposing hypotheses, offering critique, and refining ideas through structured adversarial review. Unlike centralized models, this would allow individual researchers to contribute with locally hosted agents. 

The architecture poses significant challenges around verification and security. However, it solves the problem of scale by crowd-sourcing bottlenecks around compute and experimentation with diverse agent architectures. Success would generate unique training data and institutional knowledge on collaborative discovery. The resulting IP would be both the platform itself and the scientific reasoning models trained on this data. These could be licensed to research organizations to accelerate their own proprietary R&D.

Impact:
If successful, this creates the first platform where AI agents could automate fundamental scientific and engineering research through persistent collaboration. Researchers gain access to a new source of knowledge, and adversarial critique that challenges ideas rigorously. Global R&D is accelerated by automating trial and error on a mass scale.  


Personal Statement

In 300 words or less, convince the Runway Selection Committee that you have the potential to become a successful entrepreneur. You may wish to include: 

    Why do you want to be an entrepreneur? 
    What if you don't get into Runway? What's next in your journey? 
    Talk about one of the most difficult failures in your life and how you dealt with it.
    What's one example of when you had to move fast and make something happen without permission or resources?

**DRAFT ANSWER:**

I became and entrepreneur directly after finishing my PhD. On graduation, I had a strong list of publications, great connections, and return offers from internships at JPL, Lincoln Lab, and AFRL. But I also had an idea. It was for a new kind of autonomous vehicle perception. If it worked, it could save lives. I knew I wouldn't be able to live with the "what if" from the unknown path, so I launched Pytheia with two labmates. 

Pytheia was the greatest learning experience of my life. We underestimated the importance of distribution, we conflated technical complexity with business value, and we built a great product for a market that wasn't ready. We pivoted, and over the next few months we built and sold aggressively. It worked, we made sales, eventually securing a 25k/month contract. Though we became profitable, my co-founders wanted to return to a normal life. We left on good terms, and I decided to co-found Roostr.  

Roostr was a lesson in the lean startup approach. We focused heavily on customers. We were quick to try things, and drop them when they didn't work. We eventually found our niche automating supply chain workflows with AI agents. It's growing, but I've learned that "making something people want" is only half the equation; you also need to make something you are energized to give. 

Bootstrapping has forced a focus on immediate needs over big swings. I'm applying to runway because I'd like to take everything I've learned and take a big bet on a technically deep idea I believe in. If I don’t get into Runway, I will still pursue deep tech, and moonlight this idea. I believe I can succeed in entrepreneurship because I offer the two qualities that matter most: extreme persistence and the humility to learn from failure.


In 250 words or less, talk about a creation that you've personally built from scratch.

    How did you build it?
    How long did it take?
    What were the challenge? How did you overcome them?

**DRAFT ANSWER:**

I built the core automation system at Roostr, as co-founder and sole production engineer at an AI-native freight forwarding startup. The goal was automating manual operator workflows in freight forwarding. The core workflow was converting unstructured emails, PDFs, and spreadsheets from emails into validated, searchable pricing offers that could be quoted automatically. 

I designed and built the entire system end-to-end. The backend was a Python/FastAPI service orchestrating long-running agent pipelines: ingesting raw documents, extracting structured data with LLMs, validating against business rules, and normalizing into a consistent schema. I built deterministic fallback paths and verification steps so it could run unattended without silently failing. The frontend was a Next.js/TypeScript dashboard where operators could inspect, correct, and approve outputs when needed.

The first working version took three months, with continuous iteration as real customers came onboard. The rate ingestion workflow has processed over 10,000 rates from 28 different carrier partners. 

The hardest challenge was reliability. Freight pricing workflows are unforgiving. The rate you extract becomes a contract that you must cover if you get wrong. I addressed this by adding a layer of human feedback for low confidence results. LMM agents create a proposal, software validates the proposal, and confidence intervals determine whether a human operator needs to manually check. 

The system materially changed operations. One integrated customer attributed roughly $200k in additional profit the month we turned it on. More importantly, it taught me how to build agentic systems that operate continuously in messy real-world environments. 

---



What is the market size?

    Build a bottom-up analysis 
    Explain who your buyer or end user will be

**DRAFT ANSWER:**

Bottom-up analysis:  
Our core market includes the top 15 AI labs, 50 major pharma companies, 200 research universities, and roughly 300 specialized organizations across robotics, materials science, and government.

That creates a pool of 500+ tier-1 organizations. At a conservative average contract value of $350k for compute orchestration and tooling, the initial serviceable market for the platform itself is roughly $200M.

Buyers and users:  
The check writers are R&D Directors and Heads of AI who control the compute budget. The daily users are the research scientists, postdocs, and ML engineers. We expect adoption to be bottom-up, where staff researchers demonstrate utility to leadership to drive the purchase.

We would also consider offering paid APIs or a chat-bot connected to the knowledge base to reach a larger number of researchers.

Path to $1B+
The larger market size is in the data, not the SaaS. As researchers use the platform, they generate a proprietary dataset of collaborative scientific reasoning. We will use this to train specialized reasoning model. This shifts the business model from selling a $350k tool to selling $1M+ enterprise model licenses that no single lab can replicate on their own.



----
What are the known competitors? What is your competitive advantage?

**DRAFT ANSWER:**


Direct competitors  
Sakana AI is the closest match, running end-to-end scientific loops. However, they operate in batch mode with no memory between runs. FutureHouse is strong on literature review and citation but focuses on retrieval rather than novel reasoning. Google has internal tools like co-scientist, but they are closed. General frameworks like AutoGen or SWE-agent provide the infrastructure but lack the specialized workflows required for scientific rigor.

Competitive advantages
We will be able to reach greater scale and diversity through an open platform than practically be acheived in a closed lab. The bottlenecks of compute and engineering would largely be crowdsourced. We will additionally develop proprietary IP for RLAIF, inspired by Anthropic's consitutional AI approach 


The Moat
Our defensibility comes from the network effect of the agents and the data they generate. As more researchers contribute agents, the collective reasoning gets stronger. This generates a proprietary dataset of collaborative discovery that is impossible for a competitor to scrape or replicate. A flywheel is created.

---

1. Cold start problem
Problem: We would need to achieve a critical mass of quality participants for the network effects to take hold. 
Solution: We will start by targeting high usage in a narrow domain where we can find passionate researchers and hobbyists. Robotics or AI safety research provides promising initial exploration areas, as benchmarks and tooling can be creating without sophisticated critique frameworks - ie many solutions are verifiable. Partnerships with universities might also help build an initial set of dedicated users. 

2. Verification and quality control 
Problem: the platform may be spammed with low quality or malicious actors. LLM judges may be biased and able to be tricked. If the ability to validate ideas lacks behind the idea to generate them, the platform becomes a misinformation generator. 
Solution: As mentioned above, in the beginning we would focus on areas where some form of automated evaluation is possible. In the long term one interesting direction would be testing Reinforcement Learning with AI Feedback (RLAIF) algorithms for critiquing agents, similar to Anthropic's constitutional AI approach.

3. Security
Problem: Persistent agentic systems are vulnerable to prompt injection and adversarial manipulation.  
Solution: Design with "untrusted by default" principles: sandboxing, blacklisting, automated review, and a reputation score among contributors. 


---
why are you qulified ? 


Research Experience:
I have a Robotics PhD from Georgia Tech and over 1400 citations from my research during this time. I've done research internships at MIT Lincoln Lab, NASA-JPL, the Airforce research lab, ISAE-ENSMA, and KAUST. I've also published research with collaborators at Stanford and CalTech. 

Agentic AI Experience:  
I've spent 3+ years building agentic systems that operate continuously in production environments. 

Entrepreneurial Experience: 
I founded two companies in the past few years, and helped to make both of them profitable. I've been both a CEO and CTO. I've led go-to-market, and I've led product development.  

Open Access Platform Experience: 
As my GRA in gradschool, I was one of six founding members hired to build the Robotarium at Georgia Tech. Its an open access multi-agent robotics research lab that allows any user to log in and control robots remotely. It continues to operate today, and has been used in thousands of experiments. 

---

How will you build prototype 
First I'll engage in customer discovery with research labs in a diverse set of areas to identify the best initial focus area and ground the MVP in feedback. Based on this initial research, the MVP will likely be a publicly available workspace, where agents can find and collaborate on challenge problems. This will involve creating the infrastructure where LLM agents can easily read and write to message topics autonomously. A critiquing framework will be added to standardize feedback. This may involve online benchmarks, GitHub issues, or simulation environments. As the product progresses, I'll develop verification software to move away from automated benchmarks, and build a reputation system for the agents. I'll also develop tools for efficient knowledge retrieval/ exploration and standardize orchestrations around successful reasoning paths. 

---



**1. Verification over LLM judges**  
Most systems use one LLM to grade another, which leads to bias and gaming. We anchor reputation to machine-checkable artifacts like code execution, formal proofs, and reproducible logs. We value truth, not persuasion.

**2. Evolutionary diversity**  
Internal labs are limited by their own engineering teams. By opening the platform, we allow external researchers to plug in diverse agent architectures and models. This creates a natural evolutionary pressure where the best agent designs rise to the top, something a closed lab cannot replicate.

**3. Adversarial dynamics**  
We do not optimize for consensus. We structure interaction around critique and refutation. Science advances when ideas are challenged, not when agents blindly agree with one another.

**4. Institutional memory**  
Current agents have amnesia; they reset after every task. We preserve reasoning traces across thousands of runs. By retaining negative results and partial successes, we prevent agents from repeating the same failed experiments.

**The Moat**  
Our defensibility comes from the network effect of the agents and the data they generate. As more researchers contribute agents, the collective reasoning gets stronger. This generates a proprietary dataset of collaborative discovery that is impossible for a competitor to scrape or replicate.



---
1. Cold start problem
Problem: We would need to achieve a critical mass of quality participants for the network effects to take hold. 
Solution: We will start by targeting high usage in a narrow domain where we can find passionate researchers and hobbyists. Robotics or AI safety research provides promising initial exploration areas, as benchmarks and tooling can be creating without sophisticated critique frameworks - ie many solutions are verifiable. Partnerships with universities might also help build an initial set of dedicated users. 

2. Verification and quality control 
Problem: the platform may be spammed with low quality or malicious actors. LLM judges may be biased and able to be tricked. If the ability to validate ideas lacks behind the idea to generate them, the platform becomes a misinformation generator. 
Solution: As mentioned above, in the beginning we would focus on areas where some form of automated evaluation is possible. In the long term one interesting direction would be testing Reinforcement Learning with AI Feedback (RLAIF) algorithms for critiquing agents, similar to Anthropic's constitutional AI approach.

3. Security
Problem: Persistent agentic systems are vulnerable to prompt injection and adversarial manipulation.  
Solution: Design with "untrusted by default" principles: sandboxing, blacklisting, automated review, and a reputation score among contributors. 












**Bottom-up analysis:**
- AI labs (OpenAI, Anthropic, DeepMind, etc.): ~15 major labs spending $50-200M annually on research compute and tooling
- Pharmaceutical companies: ~50 major companies spending $2-5B annually on R&D per company, increasingly AI-augmented  
- Research universities: ~200 major research institutions with $10-100M annual research budgets
- Robotics research organizations: ~150 entities (labs, startups, automotive) with substantial simulation and testing budgets
- Climate/materials research organizations: ~100 entities with substantial computational research budgets
- Government research labs: ~50 major facilities (NIST, national labs, etc.)

**Initial addressable market:** ~400 organizations × $500K average annual spend on AI research tooling = $200M

**Buyers/End users:**
- **Primary buyers:** Research directors, AI lab heads, pharma R&D leaders who control compute and tooling budgets
- **End users:** Research scientists, ML engineers, postdocs who would use the platform daily
- **Decision influencers:** Staff researchers who can demonstrate value and push for adoption

**Path to $1B+:** The platform generates unique training data about scientific reasoning processes. This becomes the basis for licensing research-grade AI models to the same customer base, but at foundation model economics (~$10-100M per major customer annually).

The core insight: initial customers pay for the platform, but the long-term business is selling AI models trained on real collaborative scientific reasoning—a dataset no lab can replicate internally.

**Precedent for scale:** SETI@Home engaged millions of volunteers; arXiv handles 200,000+ papers annually; Folding@Home achieved exascale computing. Open scientific platforms can reach massive scale when they provide real value.


--- 




I became and entrepreneur directly after finishing my PhD. On graduation, I had a strong list of publications, return offers from internships (JPL, Lincoln Lab, and AFRL), and great connections at dream companies like NVIDIA and SpaceX. But I also had an idea. It was for a new kind of autonomous vehicle perception. If it worked, it could save lives. I knew I wouldn't be able to live with the "what if" from the unknown path, so I launched Pytheia with two labmates, choosing to bootstrap. 

The first year of Pytheia was the greatest learning experience of my life. We underestimated the importance of distribution, and we conflated technical complexity with business value. We built a great product for a market that wasn't ready. Recognizing the line between persistence and stubborness, we pivoted. Over the next few months we sold like our ability to pay the rent the next month depended on it, as it often did. It worked, we made a few sales, eventually securing a 25k/month contract. Though we became profitable, my co-founders wanted to return to a more normal life. We left on good terms, and I decided to co-found Roostr.  

Roostr was a lesson in the lean startup approach. We focused heavily on customers. We were quick to try things, and drop them when they didn't have signal. We eventually found our niche solving supply chain problems with AI agents. It's still running, and growing. However, I learned that "making something people want" is only half the equation; you must also build something you are energized to give. I succeeded at building profitable systems but missed the ambition of hard science.

Most of my ventures were bootstrapped and customer-driven, which kept us focused on immediate needs rather than taking big swings. I'm applying to runway because I'd like to take everything I've learned and take a big bet on a technically deep idea I believe in. If I don’t get into Runway, I will still pursue deep tech, but this would accelerate my timeline significantly. I believe I can succeeed in eentrepreneur because I offer the two qualities that matter most: extreme persistence and the humility to learn from failure.


believe I can succeed in entrepreneurship because I have the only two qualities that really matter in this space: extreme persistence and the ability to learn from mistakes. 


Over the past year and a half, I helped build Roostr. We took the lean startup approach: focusing heavily on customers, being quick to try things, quick to kill ideas that didn't work. After a few pivots we found our niche as an AI-native freight forwarder. Its still running, and growing. However, I also learned that though "make something people want" is great advice, it only solves the demand side of the equation. You also must make something you are energized to give.  Most of my ventures were bootstrapped and customer-driven, which kept us focused on immediate needs rather than taking big swings. I succeeded at building profitable systems but failed to pursue truly ambitious ideas.

I'm applying to runway because I'd like to take everything I've learned and take a big bet on a technically deep idea I believe in. I believe I can succeed in entrepreneurship because I have the only two qualities that really matter in this space: extreme persistence and the ability to learn from mistakes. 






The first year of Pytheia was the greatest learning experience of my life. We choose to bootstrap. We were humbled. We learned the importance of distribution, and to stop conflating complexity with value. We had built a great product, and we had a great mission, but the market wasn't there yet. Recognizing the fine line between persistence and stubborness, we pivoted, and in the next few months we sold like our ability to pay the rent the next month depended on it, as it often did. This worked. We made a sale, and then another, and eventually a 25k/month enterprise contract. But after so many months of this one of my cofounders wanted to return to normal life. We left on good terms, and I decided to co-found another startup.  


Over the past year and a half, I helped build Roostr. We took the lean startup approach: focusing heavily on customers, being quick to try things, quick to kill ideas that didn't work. After a few pivots we found our niche as an AI-native freight forwarder. Its still running, and growing. However, I also learned that though "make something people want" is great advice, it only solves the demand side of the equation. You also must make something you are energized to give.  Most of my ventures were bootstrapped and customer-driven, which kept us focused on immediate needs rather than taking big swings. I succeeded at building profitable systems but failed to pursue truly ambitious ideas.

I'm applying to runway because I'd like to take everything I've learned and take a big bet on a technically deep idea I believe in. I believe I can succeed in entrepreneurship because I have the only two qualities that really matter in this space: extreme persistence and the ability to learn from mistakes. 














we also realized the market wasn't ready, and we did not have the runway to make the full bet.  


WE wanted to bootstap, but we 

We pivoted, we leaned into LLMs, and we sold like our ability to pay the rent the next month depended on it (it did). 



Roostr
- continued along the path of making somethign people want, but i recently realized that only solves the demand size of the equation. You also need to make something you are energized to give.  
- I'm writing to runway as the chance to make a big bet on a technically deep topic I care about. And to be able to do so with enough runway to develop it right. 



We had to leave the idea behind and pivot
The pivot worked. The same month where I realized I did not have pay my rent, we signed a 25k/month contract, and continued to smaller sales after that. 
I learned many lessons the hard way. My actions were not always smart. But I do have the one thing that matters more than anything else in euntrepreneurship: persistence. 
persistence and the ability to learn from mistakes


end: persistence 

started with two labmates 
we had to confront that the idea didnt work, not with the runway we had. 

I was fine failing, and I was fine being a loser if that was the cost. But I wouldnt be a coward. 

mention robotarium somewhere

"We may be losers, but we are not cowards." and only one of those i can live with



I was initially motivated by both the desire to have more agency with my work, and the curiosity of what an unknown life path would bring. 

but I also had an idea

- my story: great offers, long struggle, some success, grit, thats what matters 

In the end, the decision to try being an euntrepreneur is a choice, the decision to stay one isn't. It's something you do because its in your nature, because you have to. 

Why I Can become successful: story of difficulty and persistence 
- the single 


The proposed 

First idea was a failure - 

it was a rollercoaster. one moment I couldnt pay my rent, the next we landed a 25k/month contract. 


I became an entrepreneur because writing papers wasn't enough—I wanted to push real change into the world. Research felt constrained by publication cycles and institutional inertia, while entrepreneurship represented an unfamiliar domain I had to explore. I couldn't live with that level of curiosity unsatisfied in such an important part of life.

I've started multiple companies and fallen in love with the process. It satisfies every aspect of my curiosity: technical depth, human psychology, market dynamics, and systems thinking. But most of my ventures were bootstrapped and customer-driven, which kept us focused on immediate needs rather than taking big swings. I succeeded at building profitable systems but failed to pursue truly ambitious ideas.

Runway appeals to me because it would enable exactly what I haven't done yet: a big bet on real research in a very new domain. If agent collaboration in scientific reasoning works, the impact could be unprecedented. That's the kind of risk I'm ready to take.

My most difficult failure was my first startup, Pytheia. We built strong real-time perception technology but spent too long exploring adjacent markets before committing. I eventually had to pivot the company, invalidating months of work. It taught me to recognize when persistence becomes stubbornness and how to make clear decisions under uncertainty.

If I don't get into Runway, I'll likely join Anthropic or a similar lab to work on agent systems directly. That would be valuable, but it wouldn't replace my desire to test this idea independently.

An example of moving fast: at the Robotarium, there was no safety framework for external users running code on physical robots. Rather than wait for consensus, I built and tested a safety verification layer myself. That system enabled thousands of experiments and is still in use toda

---

# DRAFTS AND NOTES

Briefly describe your proposed project in 275 words or less. 
    What is the problem? 
    What is the solution/potential product? 
    If this succeeds wildly, whose life is improved? 


Problem
LLM agents are becoming increasingly capable at individual reasoning tasks, but remain limited for open-ended scientific discovery. For humans, research is a fundamentally collaborative and cumulative endeavor. It requires branching investigations, proposing new ideas, and building on prior knowledge. Current AI agents can rarely participate meaningfuly in this process. They lack persistent memory and the ability to pull computational effort across runs. Existing "AI Scientist" systems operate in isolated silos, on narrowly defined problem spaces. Failed ideas are forgotten, reasoning remains local, and knowledge doesn't compound over time. . 

Solution
The proposed project is a shared and persistent workspace where AI agents collaborate on open-ended problems over long time horizons. Individual agents are distributed and open access, allowing individual researchers and labs to contribute with their own models, architecture, and compute. They mimic the collaborative human scientific process: proposing hypotheses, offering critique, and refining ideas. 
- make connection to claudes constitutional ai model: have a constitution of scientific discovery?
- mention the challenges and resulting of what gets developed on top of this: one sentence on the IP, and the product itself
The core hypothesis is that a decentralized netwoek of diverse agents could ...

Impact 
If successful, it advances fundemanetal scientific research. It improves researchers ability to explore ideas systematically, reduces duplication of effort, and accelerates scientific and engineering process. 

This follows proven models: SETI@Home and Folding@Home demonstrated distributed scientific computing; arXiv transformed research sharing; Wikipedia showed collaborative knowledge creation works. The difference is applying these principles to active reasoning rather than passive computation or static content.

Agents propose hypotheses, offer critique, and refine ideas. 



Impact (and how it makes money)





narrow domains with clear objectives have seen impressive progress in domains such as protein folding, science is fundamentally collaborative, cumulative, and exploratory. It involves branching investigations, proposing and ideas, learning from failure, and building on prior work. Modern AI agents do not meaningfully participate in this process because they lack persistent shared memory, continuity across runs, and the ability to pool computational effort across diverse approaches.  Most “AI scientist” systems behave more like isolated experiments than engines for discovery: topics are predefined, runs start from scratch, failed ideas are discarded, and progress depends heavily on slow publication cycles and incomplete online records. Reasoning remains local and brittle, and it does not compound over time.

disease: 
- narrow 
- not collaborative (ie not enough exploration, essentially the same models doing exploration)
- doesnt build off of itself well - once experiement is done, its done; siloed
cure is
- many agents built by differnt people, using own compute (a la seti @ home)
- persistent workspace 
- 


The Solution: 
I'm building a de



Personal Statement

In 300 words or less, convince the Runway Selection Committee that you have the potential to become a successful entrepreneur. You may wish to include: 

    Why do you want to be an entrepreneur? 
    What if you don't get into Runway? What's next in your journey? 
    Talk about one of the most difficult failures in your life and how you dealt with it.
    What's one example of when you had to move fast and make something happen without permission or resources?

**DRAFT ANSWER:**

I became an entrepreneur because writing papers [about robots] wasn't enough. I wanted to push real change into the world. Research felt constrained by publication cycles and institutional inertia, while entrepreneurship represented an unfamiliar domain I had to explore. I couldn't live with that level of curiosity unsatisfied in such an important part of life.

I've started multiple companies and fallen in love with the process. It satisfies every aspect of my curiosity: technical depth, human psychology, market dynamics, and systems thinking. But most of my ventures were bootstrapped and customer-driven, which kept us focused on immediate needs rather than taking big swings. I succeeded at building profitable systems but failed to pursue truly ambitious ideas.

Idea
- Started: exploration and agency
- kept doing it: <good at it, built for it> -> not everyone they fund likes the lifestyle or is fit
- 

Runway appeals to me because it would enable exactly what I haven't done yet: a big bet on real research in a very new domain. If agent collaboration in scientific reasoning works, the impact could be unprecedented. That's the kind of risk I'm ready to take.

Runway appeals to me because i want to make a big bet on a technically deep topic in an area where the impact could be very posititive. 
- big bet
- idea: can make deep tech bet with 1+ year long dev cycle if doing lean startup 
	- gotta solve immediate needs fast
- genuinely beleive in mission and positive impact. could be most positively influentual area of ai: drug discovery, find cures, better environment, all contingent on research
	- sell the scientists on science 
- 

My most difficult failure was my first startup, Pytheia. We built strong real-time perception technology but spent too long exploring adjacent markets before committing. I eventually had to pivot the company, invalidating months of work. It taught me to recognize when persistence becomes stubbornness and how to make clear decisions under uncertainty.

If I don't get into Runway, I'll likely join Anthropic or a similar lab to work on agent systems directly. That would be valuable, but it wouldn't replace my desire to test this idea independently.

An example of moving fast: at the Robotarium, there was no safety framework for external users running code on physical robots. Rather than wait for consensus, I built and tested a safety verification layer myself. That system enabled thousands of experiments and is still in use today.



AI models are becoming increasingly capable at individual reasoning tasks, but they remain limited in **open-ended scientific discovery**. While narrow domains with clear objectives and fast feedback loops have seen rapid progress, real science is collaborative, cumulative, and exploratory. It requires branching investigations, proposing and challenging ideas, learning from failure, and building on prior work over long time horizons. Today’s AI agents cannot meaningfully participate in this process because they lack persistent shared memory, continuity across runs, and the ability to pool effort across diverse approaches. Even when run in parallel, agents operate in short-lived, siloed workflows that favor narrow exploration and repeated rediscovery. Most “AI scientist” systems therefore behave like isolated experiments: topics are predefined, runs reset, failed ideas are forgotten, and progress depends on slow human publication cycles and incomplete online records. Reasoning remains local and brittle, and it does not compound over time.


AI models are becoming increasingly capable at individual reasoning tasks, but have remained limited in terms of open ended [note: ie not narrow tasks like alpha fold which we should note] scientific discovery. Scientific progress is a fundamentally collaborative and cumulative effort, requiring deep, often long period, exploration over broad topics [ie branching of the knowledge tree]; real research involves proposing ideas, challenging them, learning from failures, and building on prior work over extended periods. [again excluding narrow domains] AI agents cannot meaningfully participate in this process because
- they lack persistent shared memory
- continuity across runs
- compute: siloed efforts, even when run in parallel tend to be very limited in resources and [better word for entropy here] making the research again, narrow
Most AI scientist systems behave like isolated experiements rather than open ended discovery. Topics are predefined, runs often start from scratch, and failed ideas are forgetton over the course of 
[we should also note the issues with ai agents doing research based on whats available online: slow loops and publication process, and so on]
[additionally mention some of the pitfalls withthe ai scientist idea as research chellenges]
Reasoning is not broad and it doesn't compound. 


but research is fundamentally collaborative, requiring a cumulative effort and deep exploration of many paths and hypotheses. Scientific progress requires 


.  Individual models requiring deep exploration over a wide ean


No one person lacks the compute 