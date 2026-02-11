# D.E. Shaw — Interview Prep Guide

**Interview:** Fri 2/13, 2pm ET (WebEx + possibly CoderPad)
**Role:** Applied AI Engineer (GenAI team, 6-10 people, NYC hybrid)
**Round:** First round — "Generative AI Technical"
**Prep day:** Thursday 2/12

---

## What This Round Is

From Max Ma's email, they will cover:
- "Different areas of generative AI and computer science"
- "Programming, algorithm, and logical thinking questions"
- "Your previous academic, research, and/or professional experiences, particularly your individual contributions"
- "Your creative accomplishments"
- "What excites you about the work we do at D.E. Shaw"
- CoderPad **may** be used (not guaranteed)

From Marcus (updated 2/10 call):
- **One-size-fits-all process** — 5 calls, 3 rounds
- **Round 1 (Fri 2/13):** Likely one leetcode easy or medium. Standard leetcode. Examples: calculate square root function, binary search.
- **Round 2 (if pass):** High-level design. Things you've built. "How would you build an agent to do X end-to-end" — document processing, doc search feature, how would you do eval for agents.
- **Final round:** Meet with Mark and Max (Mark's boss). If you get to onsite, it's essentially a formality.
- All about agentic workflows and GenAI. Will want to know what you did at Roostr.
- They like founders: scrappy, ship fast, care about code quality and fundamentals

**Round 1 format (updated):** Mostly behavioral/experience + one leetcode easy-medium. Less GenAI technical than originally estimated.

---

## Part 1: Behavioral Prep (Thursday morning, ~1.5 hrs)

Practice these out loud. 2-3 minutes max per answer. Use a timer.

### Must-nail questions

**"Tell me about yourself"** (2 min)
> I'm a two-time founder with a robotics PhD. Currently winding down as CTO of Roostr, where I built the entire production stack centered around LLM pipelines to automate freight operations. Before Roostr, I was founder and CEO of Pytheia, which started as a computer vision startup and pivoted into enterprise AI. My PhD at Georgia Tech was in optimization for spacecraft controls.

**"What did you build at Roostr?"** (3 min)
Walk through the rate ingestion pipeline specifically:
- Email ingestion via Nylas, map conversations to clients
- Hybrid extraction: programmatic parsing for CSVs/XLS, LLMs for semantic interpretation
- Schema validation, SSOT normalization (ports, incoterms, carriers)
- Searchable rate engine, quoting workflows
- Impact: customer attributed ~$1M incremental monthly revenue to faster quoting

Then mention: quoting agent, Slackbot, internal debugging tooling. Emphasize you were the sole production engineer.

**"How does your experience map to this role?"**
> This sounds like Roostr for finance. I built agentic systems for non-technical freight operators: document processing, multi-step workflows, stakeholder-facing tools. The domain changes but the problem shape is the same: understand messy unstructured inputs, orchestrate multi-step workflows, deliver reliable outputs to non-technical users.

**"Why are you leaving Roostr?"**
> Roostr is still operating, the product works, we're getting inbound, and I'm on great terms with my cofounder. But the company is in a sales and operations scaling phase now. I'm more excited about building hard systems than running a logistics operation day to day.

**"Why D.E. Shaw?"**
> The combination of a new team building from scratch, the caliber of people Shaw attracts, and the fact that you explicitly want startup backgrounds. I like being early to something. And honestly, I've been curious about quantitative finance since grad school.

**"What are your individual contributions?"**
D.E. Shaw cares about this a lot. Be precise:
- Roostr: sole production engineer. Every line of production code. Backend, frontend, auth, infra, agents, data pipeline.
- Pytheia: built Argus (multi-camera 3D perception system) end-to-end. Also did all sales and customer discovery.
- PhD: individual thesis on optimization for spacecraft controls. Collaborative work on the Robotarium (your piece was safety verification).

**"What would you do differently in retrospect?"**
- Validate distribution earlier at Pytheia instead of assuming product quality would sell itself
- Hire a part-time contractor sooner at Roostr instead of doing everything solo
- Pursue more exploratory research at JPL instead of optimizing for near-term deliverables

**"What excites you about GenAI work at D.E. Shaw?"**
> Building real agentic systems at an organization that has both the technical bar and the scale to make them matter. Internal tools at most companies are afterthoughts. At Shaw, internal tooling directly affects how billions of dollars are managed. The feedback loop between building something and seeing it used by quantitative teams is much tighter than selling SaaS to external customers.

### D.E. Shaw specific angles (from their prep guide)

**"How has your approach to solving problems evolved?"**
Think about: early Pytheia (build everything from scratch, monolithic) vs Roostr (lean on existing tools, hybrid LLM + deterministic, modular). You learned to optimize for iteration velocity over theoretical elegance.

**"How do you uphold high standards?"**
Golden dataset testing, SSOT normalization, human review queues, zero tolerance for persistent errors. The "SpaceX strategy": ship fast but fix everything that breaks. Not sloppy, fast.

**"Tell us about collaboration / working with teams"**
At Roostr, two-person founding team: you owned all tech, Jacky owned all ops/sales. Clear ownership, daily syncs on what customers were saying. At the Robotarium, collaborative research with 5+ PhDs. Your safety verification layer enabled 16,000+ external experiments.

---

## Part 2: GenAI Technical Discussion (Thursday afternoon, ~2 hrs)

These are "how would you build X" and "how do you think about Y" questions. Practice talking through architectures out loud.

### Agentic design patterns — know these cold

**ReAct loop:** Thought -> Action -> Observation -> repeat. When to use: open-ended tasks requiring reasoning + tool use.

**Tool use:** How do you define tools? Schema validation on inputs/outputs. What happens when a tool fails? Retries, fallbacks, human escalation.

**Planning:** Single-shot plan vs iterative refinement. When do you need a planner vs a simple chain?

**Memory:** Conversation history, summary compression, RAG for long-term memory. Context window management.

**Guardrails:** Input validation, output validation, loop detection, rate limiting, human-in-the-loop checkpoints.

### System design questions to practice

**"How would you build a document search feature for legal/compliance?"**
This is literally what the team builds. Walk through:
1. Document ingestion: PDFs, emails, attachments. Parsing strategy (programmatic for structured, LLM for unstructured).
2. Chunking: sentence-level vs paragraph vs semantic. Overlap strategy.
3. Embedding: model choice (trade off quality vs latency vs cost). Indexing (FAISS, pgvector, Pinecone).
4. Retrieval: top-k similarity search. Reranking. Hybrid search (keyword + semantic).
5. Generation: prompt construction with retrieved context. Citation generation.
6. Evaluation: how do you know it's working? Relevance scoring, user feedback, golden test sets.
7. Failure modes: hallucination, missing context, stale documents, permission leaks.

**"How would you build an internal coding assistant (like Cursor)?"**
Their team literally built one (DESCHAT). Think through:
1. Interface: IDE plugin vs web app vs CLI. Context injection (current file, repo structure).
2. Code understanding: embedding codebase, chunking by function/class, AST-aware chunking.
3. Generation: prompt engineering for code. Few-shot examples. Output validation (does it parse? does it run?).
4. Security: code doesn't leave the firm. On-prem model serving vs API with guardrails.
5. Evaluation: user acceptance rate, edit distance from suggestion to final code.

**"How would you build an agent that automates a multi-step workflow?"**
Draw from Roostr directly:
1. Define the workflow as a state machine (policy graph). Each node: required state, validation, actions.
2. Agents manage state transitions. Deterministic guards prevent invalid transitions.
3. LLMs handle the ambiguous parts (classification, extraction, reasoning). Deterministic code handles the rest.
4. Human-in-the-loop: when confidence is low, escalate. Don't automate everything.
5. Monitoring: log every decision, every state transition. Debug any failure in minutes.
6. Failure modes: infinite loops (agent replies to itself), data drift (inconsistent naming), hallucinated actions.

### Failure modes — have concrete examples

From Roostr:
- **Infinite loops:** agent replied to its own emails. Fix: sender blacklists, message ID tracking.
- **Data drift:** "Shanghai" vs "CN SHG" vs "CNSHA". Fix: SSOT normalization with canonical mappings.
- **Hallucinated extraction:** LLM invented rates that weren't in the document. Fix: schema validation, confidence thresholds, human review queue.
- **Context overflow:** long email threads exceeded context window. Fix: relevant message extraction before passing to LLM.

### Key concepts to be crisp on

- **RAG vs fine-tuning:** when to use each. RAG for knowledge that changes. Fine-tuning for behavior/style/format.
- **Prompt engineering:** system prompts, few-shot, chain-of-thought, structured output (JSON mode).
- **Model selection:** when to use small vs large models. Cost/latency/quality tradeoffs. Your tiering approach at Roostr (small for classification, large for extraction).
- **Evaluation:** how do you test non-deterministic systems? Golden datasets, A/B testing, LLM-as-judge.
- **Why not LangChain:** needed full control over state transitions, prompt context, tool boundaries, debuggability. Built custom Planner -> Tool -> Intent abstraction.

---

## Part 3: Coding Prep (Thursday evening, ~1.5 hrs)

If they use CoderPad, expect one medium-level problem. Given the GenAI focus, likely something practical rather than pure algorithms.

### Most likely problem types

1. **Data structure design** — LRU cache, hash map, rate limiter (you're already prepping these)
2. **String/parsing** — parse a log format, extract structured data from text
3. **Graph traversal** — topological sort, BFS/DFS (course schedule style)
4. **System simulation** — build a simple scheduler, queue, or state machine

### Quick drills for Thursday

Do these timed, 25 min each, on a blank CoderPad:

1. **LRU Cache** (LC 146) — if you haven't done it yet this week, do it now. It's the single most likely problem type.

2. **Parse and aggregate** — Given log lines like `"2026-02-01 10:00:01 | USER_123 | LOGIN | SUCCESS"`, parse them, store them, and return top-k users by event count in a time window. (This is Thursday's Log Parser problem but do it fresh and timed.)

3. **Design a simple key-value store with get/set/delete** — No transactions, just the basics. Clean code, error handling, think about edge cases out loud. Then if time: add TTL support.

### Python things to have ready

```python
# Collections you should be fluent with
from collections import defaultdict, Counter, deque, OrderedDict
import heapq
from typing import Optional, List, Dict

# OrderedDict for LRU
d = OrderedDict()
d.move_to_end(key)           # move to most recent
d.popitem(last=False)        # evict oldest

# heapq
heapq.heappush(heap, (priority, item))
heapq.heappop(heap)          # smallest first
heapq.nlargest(k, iterable, key=None)

# defaultdict
counts = defaultdict(int)
graph = defaultdict(list)

# Counter
c = Counter(items)
c.most_common(k)

# deque for sliding window
q = deque()
q.append(x)
q.popleft()
```

---

## Part 4: Questions to Ask Them

Pick 2-3 of these. Prioritize ones that show you understand what they're building.

1. "What's the most complex agentic workflow the team has shipped so far?"
2. "How do you evaluate whether an internal AI tool is actually working? What metrics matter?"
3. "What's the biggest technical challenge the team is facing right now?"
4. "How much autonomy does an engineer have in defining what to build vs requirements coming from stakeholders?"
5. "What does the tech stack look like? Any constraints on model providers or frameworks?"
6. "What does success look like in the first 6 months?"

---

## Day-of Checklist (Friday morning)

- [ ] Light warmup: one easy neetcode problem (10 min, just get fingers moving)
- [ ] Re-read this doc, especially Part 2 (GenAI discussion points)
- [ ] Review the behavioral answers in story-bank/Q&A.md (D.E. Shaw section)
- [ ] Test WebEx link: https://deshaw.webex.com/deshaw/j.php?MTID=m2fd8b23271134e6203d1ebea6bc7bb7f
- [ ] Have CoderPad sandbox open in a tab (in case they send a link)
- [ ] Have water, quiet room, camera on
- [ ] Mindset: this is a conversation, not an exam. They want to see how you think, not if you memorized algorithms.

---

## Interview Details

- **Time:** Fri 2/13, 2pm ET
- **Platform:** WebEx
- **Meeting ID:** 2341 653 2515
- **Password:** V3wjBgSfD56
- **Link:** https://deshaw.webex.com/deshaw/j.php?MTID=m2fd8b23271134e6203d1ebea6bc7bb7f
- **CoderPad:** link sent right before interview if used
- **No LLMs during interview** (they explicitly asked)
- **Recording:** they may record with your permission
