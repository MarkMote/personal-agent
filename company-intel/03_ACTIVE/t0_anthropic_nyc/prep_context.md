# Anthropic FDE Interview Prep - Context Document

**Purpose:** Feed this to another AI to help prep for Anthropic interview.

---

## The Role: Forward Deployed Engineer, Applied AI

**Company:** Anthropic (AI safety company, ~$15B valuation, makers of Claude)
**Location:** NYC (hybrid, 25% minimum in-office)
**Salary:** $200,000-$300,000
**Travel:** 25-50% to customer sites

### What FDEs Do
- Embed directly with strategic customers to drive AI adoption
- Build production applications using Claude models within customer systems
- Deliver technical artifacts: MCP servers, sub-agents, agent skills
- Provide **white glove** deployment support (high-touch, boutique)
- Identify repeatable deployment patterns and feed insights back to Product/Engineering
- Build long-term customer relationships
- Champion Anthropic's mission in the field

### Critical Context: This Is a Founding Role
**"You will serve as one of our founding FDEs who helps to shape our forward-deployed motion."**

This isn't joining an established team - it's building the function. Implications:
- High ambiguity, high autonomy
- Opportunity to shape processes and culture
- "Represent Anthropic at the highest level in customer environments"
- Significant responsibility and visibility

### Required Qualifications
- 4+ years in technical, customer-facing roles (FDE, consulting, or **technical founding experience**)
- Production LLM experience: prompt engineering, agent development, evaluation frameworks, deployment at scale
- Strong Python + ideally TypeScript/Java
- Ability to navigate ambiguity in complex organizations
- Cross-organizational collaboration skills

### Why They Reached Out
Recruiter (Jessica) specifically mentioned "former founders on the team" - this is an explicit culture fit signal.

---

## The Candidate: Mark Mote

### Quick Summary
Georgia Tech PhD in spacecraft controls/optimization (1,449 citations, h-index 13), turned 2x bootstrapped founder. Rare combination: rigorous math of control theory + chaotic orchestration of LLM agents.

### Current Role: CTO & Co-Founder @ Roostr (2024-present)
AI-native freight forwarder. Sole production engineer.
- Built end-to-end system for automated procurement, quoting, and shipment workflows
- Long-running agent pipeline: messy emails/attachments → validated, normalized pricing offers
- Encoded forwarding SOPs as finite-state policy graph for progressive automation
- Stack: Python/FastAPI (Docker) + Next.js/TypeScript (Vercel)
- One customer attributed ~$1M incremental monthly revenue to faster procurement/quoting
- 40% ownership, $225k raised, ~$100k revenue run rate

### Previous Role: CEO & Co-Founder @ Pytheia (2021-2024)
Computer vision startup → LLM SaaS pivot.
- Built Argus: real-time multi-camera 3D perception system
- Pivoted to LLM-driven data acquisition pipelines and demand-forecasting
- Bootstrapped $20k → $300k ARR
- 2.5 years

### PhD Work (Georgia Tech, 2016-2021)
- Founding team of Robotarium (remotely accessible swarm robotics testbed, 16,000+ experiments)
- Built safety verification tooling for remote robot operation
- Research: spacecraft controls, optimization, safe autonomy
- Research stints: NASA JPL, MIT Lincoln Lab (x2), Stanford, AFRL, KAUST

### Technical Skills Match
| FDE Requirement | Mark's Evidence |
|-----------------|-----------------|
| Production LLM experience | Roostr: agentic pipeline, prompt engineering, deployment |
| Agent development | FSM-based policy graph, sub-agent orchestration |
| Python proficiency | Primary language at both startups |
| TypeScript | Next.js dashboard at Roostr |
| Evaluation frameworks | Safety verification tooling (Robotarium) |
| Customer-facing | CEO at Pytheia (sales, pilots, proposals) |
| Technical founding | 2x founder |
| Ambiguity navigation | Startup DNA |

---

## Interview Process (Based on Research)

### Typical Anthropic Interview Flow
1. **Recruiter Screen** (30 min) - Motivation, background, high-level technical
2. **CodeSignal Assessment** (90 min) - 4 progressively complex questions, practical not LeetCode
3. **Hiring Manager Deep Dive** (60 min)
4. **Onsite/Virtual** (4 hours) - Coding, project discussion, system design, culture/values

### FDE-Specific Rounds (Expected)
- **Tech Deep Dive** - Production experience, architecture decisions
- **Solution Design** - Customer-centric problem decomposition
- **Coding** - Practical implementation, likely Python
- **Leadership/Values** - AI safety alignment, customer collaboration
- **Customer Scenario** - How you'd handle ambiguous customer situations

### What Makes Anthropic Different
- AI safety is woven into hiring process - must speak thoughtfully about it
- **AI use is prohibited during live interviews** (unless explicitly permitted)
- They encourage Claude use for prep, but authentic story matters
- Process takes ~3-4 weeks average

---

## Technical Prep Areas

### 1. Production LLM Systems
- Prompt engineering best practices
- Agent architectures (ReAct, chain-of-thought, tool use)
- Evaluation frameworks and metrics
- Handling hallucinations and failure modes
- RAG systems and retrieval
- Rate limiting, caching, cost optimization
- **Mark's angle:** Roostr's agentic pipeline, FSM policy graph

### 2. MCP (Model Context Protocol)
- How MCP servers work
- Building tools/resources for Claude
- Sub-agent patterns
- **This is core to FDE work - study Anthropic's MCP docs**

### 3. Python Fundamentals
- Async/await patterns
- Type hints and Pydantic
- FastAPI patterns
- Testing strategies
- **CodeSignal format:** Build something iteratively (file system, package manager, in-memory DB)

### 4. System Design
- Distributed systems basics
- LLM-specific scaling (inference, batching)
- Designing for reliability and observability
- **FDE angle:** Design for customer integration, not just internal systems

### 5. AI Safety Concepts
- Constitutional AI (Anthropic's approach)
- RLHF (Reinforcement Learning from Human Feedback)
- Alignment problem basics
- Model interpretability
- Responsible deployment practices
- **Mark's angle:** Safe autonomy research directly translates - formal verification, runtime assurance, control barrier functions

---

## Behavioral/Values Prep

### Key Themes to Hit
1. **Safety-first mindset** - PhD thesis was literally about safe autonomy
2. **Customer empathy** - CEO experience, direct customer work
3. **Ambiguity tolerance** - Startup founder, pivoted twice
4. **Technical depth + breadth** - PhD rigor + full-stack shipping
5. **Mission alignment** - Genuine belief in AI's importance and risks
6. **Low ego, high collaboration** - JD explicitly calls this out; demonstrate willingness to learn, credit others, adapt

### Likely Questions
- "Why Anthropic specifically?" (Not just AI safety - why this company's approach)
- "Tell me about a time you built something for a technical user" (Robotarium, Roostr tooling)
- "Describe a safety-first decision you made" (Robotarium safety verification, any pivot decision)
- "How do you handle ambiguous customer requirements?" (Pytheia pilots, Roostr customer work)
- "What's your experience with production LLM systems?" (Roostr end-to-end)
- "How do you think about AI safety in deployed systems?" (Connect PhD work to LLM deployment)
- "What excites you about being on a founding team?" (This is a founding FDE role - speak to building from scratch, shaping culture, high ownership)
- "Tell me about a time you had to represent your company at a high level" (Investor pitches, customer presentations, conference talks)

### Mark's Narrative Arc
**The Safety → AI Journey:**
Career driven by building safe autonomous systems. PhD focused on spacecraft control safety. Started CV company for safer self-driving. When LLMs achieved breakthrough, pivoted - not chasing a trend but recognizing a fundamental threshold had been crossed.

Roostr was ambitious LLM application. Now wants to help shape foundational technology itself, during the most critical period in AI development. FDE combines product engineering experience with direct impact on responsible AI deployment.

---

## Things to Know Cold

### About Anthropic
- Founded 2021 by ex-OpenAI researchers (Dario & Daniela Amodei)
- Constitutional AI is their alignment approach
- Claude is the product (Claude 3.5 Sonnet, Claude 3 Opus, etc.)
- ~50% of staff have PhDs
- Mission: "Reliable, interpretable, and steerable AI systems"
- Raised $7.3B+, valued at ~$15B+

### Anthropic's Culture (From JD)
- **"Big science" mentality** - Work as single cohesive team on few large-scale efforts
- **Impact over puzzles** - Value advancing long-term goals, not smaller specific problems
- **Empirical science view** - AI research has "as much in common with physics and biology as with traditional CS"
- **Extremely collaborative** - Frequent research discussions
- **Communication skills highly valued** - Called out explicitly
- **Low ego required** - JD explicitly mentions "low ego and collaborative approach"

### About the FDE Role
- **This is a founding FDE role** - you'd help shape the forward-deployed motion
- Team includes former founders (explicit mention from recruiter)
- Customer types: Financial services, healthcare/life sciences, enterprise
- Technical artifacts: MCP servers, sub-agents, agent skills
- Not pure engineering - consulting/customer success hybrid
- "White glove deployment support" - high-touch, boutique work
- Travel is real (25-50%)
- Locations: NYC, SF, Seattle, Boston, Chicago, Atlanta, Austin, DC

### Key Reading
- Dario Amodei's "Machines of Loving Grace" essay
- Anthropic's Constitutional AI paper
- MCP documentation (anthropic.com/docs)
- Cold Takes "Most Important Century" series
- **Anthropic's recent research papers** - JD explicitly says "easiest way to understand our research directions is to read our recent research"
- Prior work by the team: GPT-3, Circuit-Based Interpretability, Multimodal Neurons, Scaling Laws, AI & Compute, Concrete Problems in AI Safety, Learning from Human Preferences

---

## Questions Mark Should Ask

**About the Role:**
- What does "forward deployed" mean day-to-day?
- How does FDE interface with research teams?
- What's the split between customer-facing work and internal development?
- What kinds of applied AI challenges are customers struggling with?

**About the Team:**
- How big is the FDE team currently?
- What's collaboration like between NYC and SF?
- What background do most successful FDEs come from?

**About Growth:**
- How is Anthropic balancing safety research and commercial applications?
- Where do you see the FDE organization in 12-18 months?

---

## Red Flags to Watch For
- Vague answers about role responsibilities
- No clear next steps or timeline
- Misalignment on NYC vs SF expectations
- Heavy emphasis on sales over engineering

---

## Sources
- [Anthropic FDE Job Posting](https://job-boards.greenhouse.io/anthropic/jobs/4985877008)
- [Anthropic Interview Guide - IGotAnOffer](https://igotanoffer.com/en/advice/anthropic-interview-process)
- [Anthropic Interview Questions - Glassdoor](https://www.glassdoor.com/Interview/Anthropic-Interview-Questions-E8109027.htm)
- [Anthropic Technical Interview Guide - Jobright](https://jobright.ai/blog/anthropic-technical-interview-questions-complete-guide-2025/)
- [2025 Anthropic Interview Experience - Medium](https://medium.com/@anqi.silvia/my-2025-anthropic-software-engineer-interview-experience-9fc15cd81a99)
- [Anthropic Interview Questions - interviewing.io](https://interviewing.io/anthropic-interview-questions)
