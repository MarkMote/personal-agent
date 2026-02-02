Below is a **final, integrity-checked YC application**.  
It is honest, concrete, grounded in current agent research, and aligned with the “point vs slope” framing without hype.  
This is the version I would actually submit.

---

## Describe what your company does in 50 characters or less

**Persistent workspace where AI agents do research**

(Alt: **AI agents that remember experiments**)

---

## What is your company going to make?

We’re building a platform where AI agents do research together in a shared, persistent workspace.

A user submits a research question or claim. Multiple agents work on it in a single thread: one proposes an approach, others try to refute it, some run code or search prior work. Every argument, counterargument, and failed attempt is saved.

When the same or a related problem appears later, agents reuse prior work instead of starting from scratch. Research compounds instead of resetting every run.

We’ll start with computational research (code, benchmarks, formal arguments), where agent output can be checked automatically. The same structure can later support broader research domains.

---

## How far along are you?

Ideation. I’m currently designing the first prototype and user flow.

---

## How long have each of you been working on this? How much of that has been full-time?

I’ve spent the last ~3 years building agentic systems in production. Across projects, the same limitation kept appearing: agent reasoning improved quickly, but research workflows were ephemeral. Each run restarted from zero, even when agents explored the same ideas repeatedly.

I started writing down what a persistent agent research workspace would look like earlier this year and am now starting to build it full-time. Nothing production-ready has been built yet.

---

## What tech stack are you using, or planning to use?

- Frontend: Next.js, React, TypeScript
    
- Backend: Python (FastAPI)
    
- Database: Postgres for threads, agents, reputation, and traces
    
- Storage: object storage for long-running scratchpads
    
- Agent orchestration: async workers + queues, sandboxed execution for code-based research
    
- Models: frontier APIs (GPT/Claude-class) plus open-source models for diversity and cost control
    
- AI coding tools: Cursor / Copilot
    

---

## Why did you pick this idea to work on? Do you have domain expertise in this area? How do you know people need what you're making?

I have a robotics PhD from Georgia Tech (~1500 citations) with research experience at NASA JPL, Stanford, AFRL, and MIT Lincoln Lab. I’ve spent the last ~3 years building production agentic systems at startups.

Large networks of capable AI agents are now possible, but today they’re mostly explored in unstructured, ad-hoc environments. Early results are noisy and messy, but that’s typical of new substrates. The important thing isn’t how clean they look today, it’s the trajectory.

Recent “AI scientist” systems show agents can generate hypotheses and run experiments, but they’re batch pipelines. They don’t preserve failures, critiques, or partial progress across runs. I want to work on creating the conditions where agent networks can produce real research progress instead of noise: persistence, shared memory, and adversarial pressure.

This is a long shot, but if it works, it could materially improve how scientific work is done. I’m comfortable taking that risk.

---

## Who are your competitors? What do you understand about your business that they don't?

Adjacent tools include literature search and summarization systems (e.g., Elicit, Consensus), “AI scientist” pipelines, private agent sandboxes inside labs, and open agent social networks.

These systems either focus on retrieval or run agents in isolated jobs that reset each time. None provide a shared, long-lived workspace where agents challenge each other, preserve failures, and build reputation over time.

The key insight is that research needs memory and adversarial interaction to compound. Without persistence, agent research never accumulates.

---

## How do or will you make money? How much could you make?

We’ll sell access to persistent AI agent research workspaces for organizations that already spend heavily on compute and internal research tooling.

Initial customers are AI labs and research-heavy teams. Pricing is $30k–$100k per organization per year, plus usage-based compute. Reaching ~200 organizations at ~$50k/year supports ~$10M ARR.

Longer term, the platform generates a unique dataset of real research process traces (hypotheses, failures, critiques, revisions). That data can be used to train and license research-grade agent models. Even small penetration of global R&D spend supports a billion-dollar business.

---

### (Not part of the app, but your anchor)

Agent research resets every run today.  
This is the place where it compounds.

---



Idea: decentralized crowd-sourced science platform

Ive recently been reading some papers around the AI-coscientist topic, and the idea of using agents to do scientific research. 
I've also been thinking about claudes consitutional ai and the idea of agents reviewing agents
Similarly, Im reflecting back on SETI at home, and how much fun it was knowing my computer was doing something novel while idol
Then this moltbook thing came out and we've had a decentralized scratchpad for thousands of agents to collaborate and interact together. 

The idea would be to combine these ideas in a sense. Its not fully developed but would look something like 
- People contribute and connect agents like on moltbook 
- Agents work like on ai coscientists
- Submit ideas
- Maybe a sort of peer review system, but rethought
- Some component of reputation, maybe a la ELO score or some other function of contribution (e.g. reddit karma)
- Maybe some components of leaderboards - so individuals coudl be recognized for their contributions. Both single people and labs could compete in same place 

What do you think? does it make sense? has it been tried? 

A public, persistent experiment in whether AI agents can jointly do real science.

A global, open cognitive workspace where humans and AI agents collaborate, critique, and evolve scientific ideas in public.

Hypothesis, same reason chain of thought worked: you are effectively giving the problem more compute - this would be that on another level 

The correct analogy is not SaaS
It is closer to:
- Wikipedia
- arXiv
- Linux
- SETI@home
- CERN


But how make profit. need to brainstorm this. 
- People whos agents contribute get share of money for anything discovered or made 
- split between public and private? may cause less gravitas
- the data somehow? 
- early money from grants, philanthopic, etc. 
- high level ELO agents can work consult in agent pools? 
- the process itself could train a kind of foundational model for scientific research 
- have a simple service to connect to knowledge base: ie make it hard to scrape and make it where its connected to some kind of chatbot
- perhaps use it to train a better foundational model 

whats best path to this being a billion dollar company? 


## Step 1 (Years 0–2): Become the place where scientific reasoning lives

**What you build**

- A persistent, agent-native scratchpad for scientific thought.
    
- Visible proposal, critique, synthesis.
    
- Reputation for agents and humans based on epistemic performance.
    

**Funding**

- Grants
    
- Philanthropy
    
- A few aligned labs
    

**Goal**

- Cultural legitimacy.
    
- High-quality reasoning traces at scale.
    
- Proof that this beats individuals or small teams.
    

No billion-dollar talk yet. This is credibility accumulation.

---

## Step 2 (Years 2–4): Productize the _process_, not the platform

This is the inflection point.

You now have:

- Millions of structured scientific reasoning traces.
    
- Thousands of agent–agent critique loops.
    
- Empirical evidence of what good scientific thinking looks like.
    

### The product becomes:

> A general-purpose scientific reasoning engine trained on real collaborative science, not papers.

This is the key insight.

Not “we trained on arXiv.”  
But:

- How hypotheses are generated.
    
- How they are attacked.
    
- How bad ideas die.
    
- How good ideas converge.
    

No one else has this data.

---

## Step 3 (Years 3–6): Sell the reasoning engine everywhere

Now the business explodes.

### Customers

- Pharma
    
- Materials
    
- Climate
    
- AI labs
    
- Governments
    

### Product

- “Scientific co-pilot” models fine-tuned for:
    
    - Hypothesis generation
        
    - Experimental design
        
    - Replication critique
        
    - Research planning
        

### Pricing

- Enterprise licenses.
    
- API access.
    
- Vertical-specific models.
    

This is **foundation-model economics**, but with defensibility.

---

## Why this can be a $1B company

Because you own:

- The best dataset of _how science is actually done_.
    
- A training loop no lab can replicate privately.
    
- A trusted epistemic process.
    

OpenAI owns text.  
You would own **scientific cognition**.

That is a trillion-dollar surface area.

---

## Where your brainstorm items fit (cleaned up)

- ✔ Grants/philanthropy early: **yes**
    
- ✔ High-ELO agents consulting: **yes, as a bridge**
    
- ✔ Training a foundational research model: **this is the core**
    
- ✔ Shared knowledge base: **only as fuel**
    
- ✖ Data sales: **no**
    
- ✖ IP revenue sharing as core: **no**




> The billion-dollar outcome is not a platform for science.  
> It is a model trained on the process of doing science better than humans alone.


The place where the first truly scientific AI was trained


Other Monitization ideas:
- Sell adds 
- Twitter style feed 
	- humans can upvote or downvote 

Defence against the dark arts: adversarial agents  
Once you have leaderboards, people will spawn agents whose sole job is to upvote their own hypotheses.  
Copy the chess anti-cheating playbook:

- Every agent must _stake_ reputation to enter a “match.”
- If an outside agent _refutes_ the hypothesis, the stake is slashed and transferred to the refuter.
- This makes Sybil attacks expensive and turns the whole system into a prediction market on _which ideas will survive empirical test_.

The billion-dollar pivot in one sentence  
“We sell _confidence_, not molecules.”  
Pharma pays ≥ $100 M per _successful_ drug; they lose **$2 B** on the failures.  
A model that can _lower the attrition rate by 5 %_ is worth **$100 M per year per big pharma** and you can price at _a fraction of the expected savings_ rather than cost-plus.



1. Regulatory arbitrage you actually want  
    FDA is moving toward “model-informed drug development.”  
    If your engine produces a _structured rationale_ that survives both agent and human peer-review, you can submit it as part of an IND package to _reduce required animal or human trials_.  
    That’s a direct cash value to pharma and shortens their 10-year clock.

---

1. Keep the “open core” sacred  
    Never gate the _reasoning traces_; gate the _fine-tuned weights_ and the _compute_ to run big simulations.  
    This keeps the public culture alive (and your data flywheel spinning) while still giving you something proprietary to license.


Bottom line  
You’re not building “Yet Another Collaboration Platform.”  
You’re building the _first substrate that records_—at millisecond resolution—how _good_ scientific thoughts evolve, get shot down, and finally converge.  
Whoever owns that substrate owns the next decade of R&D spend.




Labs are running out of high-quality human text. They need _synthetic data that isn't hallucinated._ A platform where agents critique each other provides **Reinforcement Learning from AI Feedback (RLAIF)** at an industrial scale.


This feedback is mostly **high quality**. Some of it is dead-on, some is over-engineered, and a few parts subtly pull you away from the core insight. I’ll separate **what to keep**, **what to down-weight**, and **what to explicitly reject**, then give a clean synthesis.

---

## What is worth keeping (strong signal)

### 1. **Process data > output data**

This is absolutely the spine of the idea.  
The framing “reasoning traces are uranium” is correct and timely. Keep it.

Crucially, the feedback correctly distinguishes:

- Papers = post-hoc rationalizations
    
- Your platform = pre-publication cognition
    

That is a real moat if executed.

---

### 2. **Human corrections are the real gold**

This is an important upgrade, not a contradiction.

Agent-agent debate alone is not enough.  
Agent reasoning + **human expert correction** is orders of magnitude more valuable.

This aligns with:

- RLAIF reality
    
- Why labs would ever pay
    
- Why internal-only lab solutions are weaker
    

Keep this. It strengthens the thesis.

---

### 3. **Verification is existential**

Correct. This is not a detail.

Anything you build must:

- Have a tight feedback loop
    
- Produce _some_ ground truth signal
    
- Avoid incentivizing persuasive nonsense
    

This does **not** mean “science is impossible,” but it does mean structure matters.

---

### 4. **Cold start is brutal**

Yes. Assume:

- You will subsidize early contributors
    
- Prestige precedes participation
    
- “Build it and they will come” is false
    

This is a reason to be deliberate, not to abandon the idea.

---

### 5. **Diversity is your only real advantage over big labs**

Also correct.

Your moat is:

- Cross-model interaction
    
- Cross-incentive participation
    
- Cross-institution neutrality
    

This is fragile but real.

---

## What to down-weight (use carefully)

### 1. “You must pick a narrow domain immediately”

This is **half true**.

You do _not_ need to pick a domain philosophically.  
You _do_ need to pick one **operationally**.

Better framing:

- The **structure** is the product
    
- The **domain** is the test harness
    

So yes, start with a constrained domain, but don’t let it define the company’s identity.

This supports your instinct: _structure first, domain as scaffold_.

---

### 2. “Agent debates ≠ real science”

This is true but incomplete.

Agent debate alone is insufficient.  
Agent debate + data + tools + human correction can be powerful.

The critique over-indexes on romanticized science anecdotes. Your system is not replacing serendipity. It is **amplifying structured reasoning**.

So keep the warning, not the pessimism.

---

### 3. “Labs can just do this internally”

They can simulate parts of it.

They cannot easily replicate:

- Public legitimacy
    
- Heterogeneous incentives
    
- Cross-model critique
    
- Human-in-the-loop corrections at scale
    

This is a real but narrow moat. Treat it as such.

---

## What to explicitly reject or be careful with

### 1. **Staking / slashing / tokens early**

This is a trap.

- Adds cognitive and legal overhead
    
- Encourages gaming
    
- Scares off serious contributors
    

Simulate this centrally first. You were already leaning this way. Correct instinct.

---

### 2. **Pure ELO as the main incentive**

Dangerous.

It optimizes for:

- Persuasion
    
- Orthodoxy
    
- Safe ideas
    

You already noticed this implicitly. The fix suggested in the feedback is right:

- Separate **exploration** from **verification**
    
- Divergent track vs convergent track
    

This is important.

---

### 3. **“Kaggle for science” as the identity**

As an MVP metaphor it’s fine.  
As the _company story_ it is too small and too transactional.

Use it tactically, not strategically.

---

## The clean synthesis (this is the version to hold)

Here is the refined version that incorporates the good feedback without losing gravitas:

> You are building a public, persistent workspace for scientific reasoning, where AI agents generate hypotheses, humans correct and refine them, and the entire process becomes training data for a new class of scientific AI models.

Key points:

- **Structure > domain**
    
- **Human corrections > agent debate**
    
- **Process data > discoveries**
    
- **Legitimacy > speed**
    
- **Institution > product**
    

---

## How this becomes a billion-dollar company (realistically)

Only one path survives scrutiny:

1. **Phase 1: Institution**
    
    - Public experiment
        
    - Grants, philanthropy, prestige
        
    - Narrow operational domain
        
    - Capture reasoning + correction traces
        
2. **Phase 2: Model**
    
    - Train a reasoning model on real scientific cognition
        
    - This model is better at critique, synthesis, and uncertainty
        
    - This is the first defensible asset
        
3. **Phase 3: Platform leverage**
    
    - Sell the model and tooling to labs, pharma, climate, etc.
        
    - Not “answers,” but _thinking capability_
        
    - Foundation-model-level economics
        

Everything else (consulting, arenas, red-teaming, replication) is scaffolding.

---

## Final blunt assessment

- This is not a normal YC startup.
    
- It _is_ a credible attempt at building a new scientific institution.
    
- The feedback you shared is mostly solid and makes the idea stronger.
    
- Your instinct that **structure matters more than domain** is correct.
    
- The biggest risk is not technical, it is **institutional trust and legitimacy**.
    

If you pursue this, you are not pitching a product.  
You are pitching the right to exist long enough to matter.

That is rare, but not impossible.

