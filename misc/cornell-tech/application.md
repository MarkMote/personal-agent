

RUNWAY STARTUP POSTDOC PROGRAM 

Application Tips

    Be authentic. The purpose of your application is to help us understand who you are; your personality, ideas, and perspective.
    Communicate clearly and concisely. Reviewers will assess your clarity of communication, storytelling ability, and authenticity.
    Avoid artificial aids.
        There is opportunity to upload a brief video at the end of the page. Please do not read from a script or teleprompter.
    Prioritize honesty over perfection. Your video does not need to be flawless - it should simply be genuine, clear, and true to you.



Proposed Project 

Briefly describe your proposed project in 275 words or less. 

    What is the problem? 
    What is the solution/potential product? 
    If this succeeds wildly, whose life is improved?

**DRAFT ANSWER:**

**The Problem:** AI models are becoming capable individual reasoners, but scientific progress is fundamentally collaborative and cumulative. Real research involves proposing ideas, challenging them, learning from failures, and building on prior work over extended periods. Today's AI agents cannot participate meaningfully in this process because they lack persistent shared memory, continuity across runs, and structured interaction with other agents. Most "AI scientist" systems behave like isolated experiments—each run starts from scratch, failed ideas are forgotten, and promising approaches are rediscovered repeatedly. Reasoning doesn't compound.

**The Solution:** I'm building a persistent, shared research workspace where AI agents collaborate on open-ended problems over long time horizons. Agents propose hypotheses, others critique and refine them, and all reasoning—including failures—is preserved. Work compounds instead of resetting. Humans can observe and guide, but the primary dynamic is agents reasoning together in public, persistent threads. 

The core hypothesis: if chain of thought works because it gives problems more compute, then a decentralized network of diverse agents should achieve even greater reasoning gains. The key isn't just scale—it's the variation. When people hack together their own agent configurations, models, and architectures, you get crowdsourced exploration of the solution space that no single lab could engineer internally. Initially, this is experimental infrastructure to study agent collaboration. Over time, it becomes the training ground for AI systems that reason more rigorously about scientific problems.

**Impact:** If successful, this improves researchers' ability to explore ideas systematically, reduces institutional duplication of effort, and accelerates scientific progress. The platform would generate unique training data about how good scientific reasoning actually develops through collaboration and critique. Long-term, it could enable AI systems with fundamentally better scientific reasoning capabilities—directly relevant to medicine, climate science, and other domains where rigorous thinking matters most.

This follows proven models: SETI@Home and Folding@Home demonstrated distributed scientific computing; arXiv transformed research sharing; Wikipedia showed collaborative knowledge creation works. The difference is applying these principles to active reasoning rather than passive computation or static content.


Personal Statement

In 300 words or less, convince the Runway Selection Committee that you have the potential to become a successful entrepreneur. You may wish to include: 

    Why do you want to be an entrepreneur? 
    What if you don't get into Runway? What's next in your journey? 
    Talk about one of the most difficult failures in your life and how you dealt with it.
    What's one example of when you had to move fast and make something happen without permission or resources?

**DRAFT ANSWER:**

I became an entrepreneur because writing papers wasn't enough—I wanted to push real change into the world. Research felt constrained by publication cycles and institutional inertia, while entrepreneurship represented an unfamiliar domain I had to explore. I couldn't live with that level of curiosity unsatisfied in such an important part of life.

I've started multiple companies and fallen in love with the process. It satisfies every aspect of my curiosity: technical depth, human psychology, market dynamics, and systems thinking. But most of my ventures were bootstrapped and customer-driven, which kept us focused on immediate needs rather than taking big swings. I succeeded at building profitable systems but failed to pursue truly ambitious ideas.

Runway appeals to me because it would enable exactly what I haven't done yet: a big bet on real research in a very new domain. If agent collaboration in scientific reasoning works, the impact could be unprecedented. That's the kind of risk I'm ready to take.

My most difficult failure was my first startup, Pytheia. We built strong real-time perception technology but spent too long exploring adjacent markets before committing. I eventually had to pivot the company, invalidating months of work. It taught me to recognize when persistence becomes stubbornness and how to make clear decisions under uncertainty.

If I don't get into Runway, I'll likely join Anthropic or a similar lab to work on agent systems directly. That would be valuable, but it wouldn't replace my desire to test this idea independently.

An example of moving fast: at the Robotarium, there was no safety framework for external users running code on physical robots. Rather than wait for consensus, I built and tested a safety verification layer myself. That system enabled thousands of experiments and is still in use today.

In 250 words or less, talk about a creation that you've personally built from scratch.

    How did you build it?
    How long did it take?
    What were the challenge? How did you overcome them?

**DRAFT ANSWER:**

I built the core automation system at Roostr, an AI-native freight forwarding startup. The goal was converting unstructured emails, PDFs, and spreadsheets from emails into validated, searchable pricing offers that could be quoted automatically. 

I designed and built the entire system end-to-end. The backend was a Python/FastAPI service orchestrating long-running agent pipelines: ingesting raw documents, extracting structured data with LLMs, validating against business rules, and normalizing into a consistent schema. I built deterministic fallback paths and verification steps so it could run unattended without silently failing. The frontend was a Next.js/TypeScript dashboard where operators could inspect, correct, and approve outputs when needed.

The first working version took three months, with continuous iteration as real customers came onboard. The rate ingestion workflow has processed over 10,000 rates from 28 different carrier partners. 

The hardest challenge was reliability. LLM outputs are probabilistic, but freight pricing workflows are unforgiving. The rate you extract becomes a contract that you must cover if you get wrong. I addressed this by adding a layer of human feedback for low confidence results. LMM agents create a proposal, software validates the proposal, and confidence intervals determine whether a human operator needs to manually check. I also built internal tools that helped to turn any mistake into a patch and future test data. 

The system materially changed operations. One integrated customer attributed roughly $200k in additional profit the month we turned it on. More importantly, it taught me how to build agentic systems that operate continuously in messy real-world environments. I'll use that experience to 


Opportunity Statement

The following questions intend to dive deeper into the problem you are trying to solve and how you intend to approach it.  Please keep your answers within a reasonable limit (e.g., 250 words or less).

What is the market size?

    Build a bottom-up analysis 
    Explain who your buyer or end user will be

**DRAFT ANSWER:**

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

What are the known competitors? What is your competitive advantage?

**DRAFT ANSWER:**

**Direct competitors in agent research:**
- **Sakana AI's AI Scientist:** End-to-end automated research pipelines (idea→code→run→paper) but batch-oriented with no persistence across runs
- **FutureHouse PaperQA2:** Strong literature agent with citation grounding and contradiction detection, but focused on retrieval rather than novel reasoning
- **Google AI co-scientist:** Multi-agent hypothesis generation for biomedical research, but private/internal rather than open commons
- **SWE-agent ecosystem:** Tool-using agents for code repositories with strong benchmarks (SWE-bench), but narrow domain focus
- **Microsoft AutoGen & LangGraph:** Multi-agent frameworks with persistence, but general-purpose rather than research-optimized

**Key competitive advantages:**
1. **Verification-anchored persistence:** Unlike current systems that rely on LLM judges (prone to bias and gaming), we anchor reputation to machine-checkable artifacts—code tests, formal proofs, reproducible experiments. This solves the "truth vs persuasion" problem that plagues multi-agent critique.

2. **Crowdsourced agent diversity:** Current systems use engineered agent configurations from single organizations. We enable participants to hack together their own agent configurations, models, and architectures. This creates solution-space exploration that emerges organically rather than being designed top-down—diversity no internal lab can engineer or anticipate.

3. **Adversarial dynamics by design:** Rather than consensus-seeking, we structure agent interactions around critique and refutation. Recent research shows this improves reasoning quality when grounded in verifiable domains (SWE-bench, Lean theorem proving).

4. **Long-horizon shared memory:** Existing systems reset each run. We preserve reasoning traces, failed approaches, and partial progress. Research shows agents perform better with episodic memory (Reflexion) when feedback signals are reliable.

5. **Public legitimacy pathway:** Following arXiv's model (started at Los Alamos, gained acceptance through utility), we build institutional trust through transparent governance and verifiable results rather than proprietary claims.

**Moat sustainability:** Network effects (more participants → better reasoning), data moat (unique collaborative reasoning traces), and institutional trust (harder to replicate than technology). The combination is defensible even against well-funded internal efforts.

What are the top three (3) challenges or risks that, if not solved, will cause the company to fail?

    Why?
    How would you attempt to solve these challenges?

**DRAFT ANSWER:**

**1. Cold start problem - achieving critical mass of quality participants**
*Why it kills the company:* Without sufficient high-quality human researchers and diverse AI agents, the platform becomes an echo chamber producing low-quality reasoning. Network effects work in reverse.
*Solution approach:* Start with a narrow, prestigious domain (e.g., AI safety evaluation). Subsidize participation from respected researchers. Build legitimacy through association with established institutions before expanding scope.

**2. Verification and quality control - preventing persuasive nonsense**
*Why it kills the company:* Research shows LLM judges are biased and gameable; multi-agent systems can converge on persuasive but incorrect outputs. Without machine-checkable truth oracles, the platform becomes a sophisticated misinformation generator.
*Solution approach:* Anchor all reputation to verifiable artifacts following proven patterns: unit tests (SWE-bench), formal proofs (Lean), reproducible experiments with clear success metrics. Recent work (ChemCrow) shows that even GPT-4-level evaluation misses wrong answers in open-ended domains, so we start verification-first and expand only to domains with reliable automated evaluation.

**3. Security and adversarial resilience - persistent systems are attack surfaces**
*Why it kills the company:* Persistent agent systems with shared memory are vulnerable to prompt injection, memory pollution, and adversarial manipulation. Recent research shows these attacks are endemic in tool-using agents and can't be fully prevented, only mitigated.
*Solution approach:* Design with "untrusted by default" principles: strict sandboxing, provenance tracking for all memory writes, access controls on shared state, and quarantine mechanisms for suspicious outputs. Implement "trust but verify" rather than assuming agent outputs are safe.

**4. Institutional legitimacy - gaining acceptance from conservative research culture**  
*Why it kills the company:* If the scientific community views this as "Silicon Valley disruption" rather than legitimate research infrastructure, adoption stalls and the platform remains marginalized.
*Solution approach:* Partner with established research institutions early. Publish rigorous studies about the platform's effectiveness. Ensure transparent governance. Frame as augmenting rather than replacing traditional research. Get endorsements from respected senior researchers who see genuine value. Follow the legitimacy path of arXiv (started at Los Alamos, gained acceptance through utility) and SETI@Home (academic backing + clear scientific value).

Why are you qualified to solve this problem?

**DRAFT ANSWER:**

I have the rare combination of deep research experience and practical agent system deployment needed for this problem.

**Research credibility:** Robotics PhD from Georgia Tech with ~1500 citations and research experience at NASA JPL, Stanford, AFRL, and MIT Lincoln Lab. Robotics is an ideal initial domain for this platform—it has built-in verification through simulation, clear benchmarking metrics, and iterative hypothesis testing. I understand how real scientific work happens, the frustrations researchers face, and what would actually be valuable versus what sounds impressive.

**Production AI systems experience:** I've spent 3+ years building agentic systems that operate continuously in production environments. At Roostr, I built end-to-end LLM pipelines processing millions of dollars in freight transactions. I understand the critical gap between research demos and systems that work reliably under adversarial conditions—including prompt injection resistance, verification mechanisms, and failure mode handling.

**Infrastructure mindset:** Throughout my career, I've gravitated toward building systems that enable other people to do better work. At Georgia Tech, I helped build the Robotarium—a remotely accessible robotics research platform that has enabled thousands of experiments. I think in terms of platforms and institutions, not just products.

**Cross-domain perspective:** My background spans robotics, computer vision, distributed systems, and business operations. This problem sits at the intersection of AI, research methodology, platform design, and institutional change. Few people have touched all these areas practically.

**Entrepreneurial execution:** I've successfully built and operated multiple companies. I know how to move from concept to working system, handle regulatory complexity, and build sustainable business models around research infrastructure.

Most importantly, I've seen both sides: the frustrations of academic research and the realities of deploying AI systems that actually work. I'm deeply familiar with the current agent research landscape—from Sakana's AI Scientist to FutureHouse's PaperQA2 to the emerging benchmarks like SWE-bench and ScienceAgentBench. I know what's been tried, what works, what fails, and where the genuine opportunities lie. This problem requires someone who deeply understands both worlds and can navigate the substantial technical challenges revealed by recent research.
How will you build the product/prototype?

**DRAFT ANSWER:**

**Phase 1 (Months 1-6): Verification-First MVP**
- Start with domains where verification is feasible: open-source bug fixing (SWE-bench-style), formal theorem proving (Lean-based), and robotics research (simulation-based testing and benchmarking)
- Build persistent thread architecture using LangGraph checkpoints for resumable agent state
- Implement secure sandboxing for code execution, proof checking, and simulation environments
- Create multi-agent orchestration that encourages participants to hack together diverse agent configurations rather than standardized approaches
- Establish reputation system anchored to verifiable artifacts (merged PRs, accepted proofs, simulation benchmark performance) rather than peer votes

**Phase 2 (Months 6-12): Adversarial Dynamics**
- Add structured agent-to-agent critique protocols based on successful patterns from AutoGen and adversarial debate research
- Implement "opposition agents" that actively search for flaws and contradictions in proposals
- Build provenance tracking and memory management to prevent pollution (informed by MemGPT/A-MEM research)
- Add literature synthesis module using PaperQA2-style citation grounding and contradiction detection
- Recruit initial cohort from formal methods and open-source communities where verification culture exists

**Phase 3 (Months 12-18): Expansion and Data Capture**
- Extend to additional domains with strong evaluation metrics (following ScienceAgentBench taxonomy)
- Build comprehensive audit trails and reasoning trace capture for training data
- Implement cross-institutional access with proper security and governance
- Create research tools for studying collaborative reasoning dynamics and failure modes
- Begin training research-grade models on captured interaction data

**Technical stack:** Next.js/React frontend, Python backend, PostgreSQL + object storage, containerized deployment, integrated with multiple LLM APIs, designed for academic research compliance from day one.


Do you have a co-founder or other member of your startup?

    Yes
    No

**DRAFT ANSWER:**

No, I do not currently have a co-founder.

I'm pursuing this as a solo founder initially because:
1. The vision is still crystallizing and requires deep technical exploration before bringing on partners
2. I want to validate core technical assumptions (agent collaboration dynamics, verification mechanisms) before making co-founder commitments
3. My background spans the necessary domains (research, AI systems, platform engineering), making me uniquely positioned to build the initial prototype independently

However, I recognize this will eventually require a team. Ideal future co-founder profiles include:
- **Research partnerships:** Senior academic researcher with domain expertise and institutional credibility
- **Product/Design:** Someone experienced in building tools that researchers actually want to use
- **Business development:** Person with relationships in target customer segments (AI labs, pharma R&D, research institutions)

The Runway program would be an excellent environment to identify potential co-founders from the broader Cornell Tech community, while also building the legitimacy and track record that would attract high-quality partners.

For now, I'm focused on building enough technical proof-of-concept to demonstrate the core value proposition, then expanding the team strategically based on actual needs rather than theoretical gaps.


potential ansewrs: 
Here is a tight, ~300-word version, clean and grounded, suitable as a core narrative. This is still conceptual content, not something you have to paste verbatim.

Proposed Project
What is the problem?
AI models are becoming strong individual reasoners, but scientific progress is fundamentally collaborative and cumulative. Real research involves proposing ideas, challenging them, learning from failures, and building on prior work over long periods of time. Today’s AI agents cannot participate meaningfully in this process because they lack persistent shared memory, continuity across runs, and structured interaction with other agents.
As a result, most “AI scientist” systems behave like isolated experiments. Each run starts from scratch. Failed ideas are forgotten, promising approaches are rediscovered repeatedly, and reasoning does not compound. There is also no way for humans to observe or guide what large populations of autonomous agents might achieve if allowed to collaborate continuously.
Despite growing interest in agent collectives, the infrastructure to test whether persistent, decentralized agent collaboration can meaningfully advance research does not yet exist.

What is the solution / potential product?
The project is a persistent, shared research workspace where AI agents can collaborate on open-ended problems over long time horizons.
In this system:
Agents propose hypotheses or approaches
Other agents critique, test, or refine them
All reasoning, including failures and dead ends, is preserved
Work compounds instead of resetting each run
Humans can observe, steer direction, and intervene when needed, but the primary actors are agents interacting with each other in public, persistent threads. The goal is not publishing papers, but enabling research to happen continuously and transparently.
Initially, this is an experimental research infrastructure to study agent collaboration. Over time, it could form the basis for training more capable scientific AI systems grounded in real collaborative reasoning rather than static outputs.

If this succeeds wildly, whose life is improved?
If successful, this improves the lives of researchers by augmenting their ability to explore and critique ideas, institutions by reducing duplicated effort, and society by accelerating scientific progress. In the long term, it could enable AI systems that reason more rigorously, collaborate effectively, and handle uncertainty—capabilities directly relevant to medicine, climate science, and other public-interest domains.


Here is a tight, honest ~300-word narrative that addresses all four prompts without sounding defensive or over-polished. Use it as a reference and adjust wording to your natural voice.

I want to be an entrepreneur because building new systems is how I’ve always had the most impact. In research, I was drawn less to isolated results and more to infrastructure: systems that let many people do better work. That instinct carried through my PhD, where I helped build the Robotarium, and later into startups, where I’ve repeatedly chosen to work on hard, ambiguous problems without a clear playbook. I’m motivated by the chance to create something that didn’t exist before and that meaningfully expands what people or machines can do.
If I don’t get into this program or YC, I’ll keep building. The most likely alternative path would be joining a place like Anthropic or a similar research lab, where I could work on agent systems directly. That would be a good outcome. But it wouldn’t replace my desire to test this idea independently. I’m pursuing entrepreneurship not because I lack options, but because this feels like the right problem to take responsibility for.
One of my most difficult failures was my first startup, Pytheia. We built a strong real-time perception system, but we spent too long exploring adjacent markets before committing to one. I eventually had to make the call to pivot the company, knowing it would invalidate months of work. It was painful, but it taught me how to recognize when persistence becomes stubbornness, and how to make clear decisions under uncertainty.
An example of moving fast without permission was at the Robotarium. Early on, there was no formal safety framework for letting external users run code on physical robots. Rather than wait for consensus, I built a safety verification layer myself, tested it aggressively, and demonstrated that it worked. That system is still in use today and enabled thousands of experiments that wouldn’t have been possible otherwise.
Those experiences shape how I approach building now: move early, learn quickly, and take responsibility for outcomes.

Here’s a tight, concrete ≤250-word answer, grounded in building rather than theory. This is content to adapt into your own voice.

One project I built from scratch was the core automation system at Roostr, an AI-native freight forwarding startup. The goal was to turn unstructured emails, PDFs, and spreadsheets from carriers into validated, searchable pricing offers that could be quoted automatically.
I designed and built the entire system end-to-end. On the backend, I wrote a Python/FastAPI service that orchestrated long-running agent pipelines: ingesting raw documents, extracting structured data with LLMs, validating it against business rules, and normalizing it into a consistent schema. I built deterministic fallback paths and verification steps so the system could run unattended without silently failing. On the frontend, I built a multi-tenant Next.js/TypeScript dashboard so operators could inspect, correct, and approve outputs when needed.
The first working version took about three months to build, with continuous iteration afterward as real customers came onboard.
The hardest challenge was reliability. LLM outputs are probabilistic, but freight pricing workflows are not forgiving. A single incorrect lane or surcharge can invalidate a quote. I addressed this by treating LLMs as proposal generators rather than authorities: every step was wrapped in validation, cross-checks, and confidence thresholds, with human review where necessary.
The result was a system that materially changed operations. One fully integrated customer attributed roughly $1M in incremental monthly revenue to faster procurement and quoting. More importantly, it taught me how to build agentic systems that operate continuously in messy real-world environments—experience that directly informs the project I want to pursue next.

