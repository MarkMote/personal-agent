# Interview Prep - February 2026

## Scheduled Interviews
| Date | Company | Type | Tests |
|------|---------|------|-------|
| 2/6 | Anthropic | Recruiter | Fit only |
| 2/11 | Laurion | Intro | Fit only |
| **2/17** | **Jane Street** | **Technical** | Coding, ML Theory, Data Science |
| ~2/17-21 | D.E. Shaw | Round 1 | Leetcode, Agentic Design, System Design |

## Priority Areas

## P0.1: Review all roostr code and architechture.
- Be able to replicate what was done, and know why it was done that way. 


### **P0: Leetcode Fundamentals** ⚠️ Never done before
- Neetcode 150 (targeted): Arrays, Hashing, Two Pointers, Trees
- Focus on mediums, communicate thought process
- 2-3 problems/day starting NOW

## Basic python familiarity
- Be able to set up fastapi server without ai help
- Async/Await: You must be comfortable writing async Python (FastAPI style).
- Pydantic: Anthropic uses Pydantic heavily for data validation. Know it well.
- Testing: Be ready to write a unit test for your code during the interview.

### **P1: ML Theory** ⚠️ Limited experience
- NN architectures (MLP, CNN, RNN, Transformer basics)
- Training dynamics, failure modes, debugging
- Jane Street explicitly tests this
- PyTorch 60 Minute Blitz https://docs.pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- Zero to hero https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ (Karpathy)  

### **P2: System Design**
- Build a hello world MCP server https://modelcontextprotocol.io/docs/getting-started/intro
- RAG nuances: Semantic search vs. Keyword search, Hybrid search, Reranking logic.
- Agent Patterns: ReAct vs. Chain of Thought. Tools/Function calling.
- Evals: How do you know the model is working? (Review: RAGAS, generic evaluation pipelines).
- ML pipeline design (Jane Street)
- Agentic architecture patterns (D.E. Shaw, Laurion)
- You have strength here from Roostr - refresh, don't rebuild
- Figure out how clawd works - read memory articles on twitter
- BUILD all the example systems, as if you were doing so in leetcode. 
- The Scenario: You are asked to build a "toy" version of a real system. Common examples include: (See prep 2)
    An In-Memory File System[2]
    A Banking Ledger[2]
    A Cloud Storage Rate Limiter[2]
    A Spreadsheets Engine[2]



### **P3: Data Science**
- Dataset exploration, feature analysis
- Statistical intuition (PhD helps here)

### **P4: Domain-Specific (lower priority)**
- OCaml awareness (not fluency)
- Trading concepts (light touch)
- Quant fund dynamics

---

## Detailed Breakdown

### **ML Systems & Theory (Week 1-2 focus)**

**Core Implementation Skills:**
- [ ] Implement neural network from scratch (no PyTorch)
  - Forward/backward pass
  - SGD, Adam optimizers
  - Batch normalization, dropout
- [ ] PyTorch proficiency
  - Custom datasets, data loaders
  - Model debugging, loss not decreasing
  - Distributed training concepts
- [ ] System Design Patterns
  - Model serving architectures
  - A/B testing for ML
  - Data pipeline design
  - Production debugging

**Theory (refresh, don't memorize):**
- [ ] Loss functions and when to use each
- [ ] Regularization techniques (L1/L2, dropout, early stopping)
- [ ] Optimization dynamics (learning rate schedules, gradient clipping)
- [ ] Common failure modes (vanishing gradients, overfitting, mode collapse)

### **Algorithmic Fundamentals (Ongoing, 1-2 hrs/day)**

**NeetCode 150 - Targeted Categories:**
- [ ] **Arrays & Hashing** (15 problems)
  - Two sum, product except self, group anagrams
  - Data manipulation fundamentals
- [ ] **Two Pointers** (5 problems)
  - Time series analysis patterns
- [ ] **Dynamic Programming** (12 problems)
  - Your optimization background gives you an edge here
  - Knapsack, LCS, coin change
- [ ] **Trees & Graphs** (10 problems)
  - DFS/BFS, shortest path
  - Network analysis for trading systems

**Skip These Categories:**
- Bit manipulation (low ROI for your targets)
- Advanced graph algorithms (union find, etc.)
- Hard edge cases (focus on mediums)

### **Domain-Specific Prep**

**Jane Street (Week 3 focus):**
- [ ] OCaml syntax basics
  - Pattern matching, recursion, immutability
  - Not fluency, just awareness
- [ ] Financial concepts (light touch)
  - Market making, arbitrage concepts
  - Multi-agent competitive dynamics
- [ ] Trading system design
  - Low latency considerations
  - Risk management systems

**Anthropic/Research Roles:**
- [ ] Transformer architecture deep dive
- [ ] Safety research concepts (alignment, robustness)
- [ ] Research code quality patterns

**Robotics ML (Nominal, Percepta, FAIR):**
- [ ] RL fundamentals refresh (2-3 hrs)
  - PPO, SAC conceptually (not implementation)
  - Reward shaping, sparse rewards problem
  - Spinning Up in Deep RL (OpenAI) - skim intro + PPO section
- [ ] Sim-to-real basics (1-2 hrs)
  - Domain randomization concept
  - Reality gap, system identification
  - Why simulation alone isn't enough
- [ ] Mujoco awareness (1 hr)
  - What it is, when it's used
  - Run one tutorial if time permits
- [ ] Skim 2-3 recent papers (titles/abstracts + key ideas)
  - RT-1/RT-2 (Google robotics transformers)
  - Diffusion Policy (action generation via diffusion)
  - Just know they exist and the high-level approach

**Your Optimization Background (refresh):**
- [ ] Convex optimization fundamentals
- [ ] Control theory → ML connections
- [ ] Nonstationary dynamics (regime changes)

### **Research Storytelling**

**Core Narrative:**
- [ ] PhD research → real-world impact story
- [ ] Safety/verification expertise relevance to ML
- [ ] Startup systems experience + research rigor

**Demo Preparation:**
- [ ] Update Robotarium demo materials
- [ ] Pytheia Argus system walkthrough
- [ ] Roostr LLM agent architecture explanation

**Technical Examples Ready:**
- [ ] Control barrier functions → ML safety
- [ ] Multi-agent coordination → trading strategies
- [ ] Runtime assurance → production ML reliability

---

## Weekly Schedule

### **W05 (Jan 27 - Jan 31) - Current**
- **Focus:** Leetcode foundations (arrays, hashing) + ML theory basics
- **Daily:** 2-3 leetcode problems + 1-2 hrs ML content
- **Goal:** Break the seal on leetcode, establish routine

### **W06 (Feb 2 - Feb 6)**
- **Focus:** Continue leetcode (two pointers, stack) + ML theory depth
- **Daily:** 2-3 problems + ML architecture study
- **Fri 2/6:** Anthropic recruiter screen (11am) - light prep, fit only
- **Goal:** 20+ problems done, solid on NN fundamentals

### **W07 (Feb 9 - Feb 13)**
- **Focus:** Trees/graphs + system design + narrative practice
- **Daily:** 2 problems + system design patterns
- **Wed 2/11:** Laurion intro call (1pm) - fit only, no coding
- **Goal:** 35+ problems, can explain ML pipeline design

### **W08 (Feb 16 - Feb 20) - Interview Week**
- **Mon-Tue:** Final review, light practice, rest
- **Tue 2/17:** Jane Street technical (10:30am)
- **~Feb 17-21:** D.E. Shaw Round 1
- **Goal:** Peak performance, execute

---

## Key Resources

**ML Implementation:**
- [Neural Networks from Scratch](https://nnfs.io/) 
- [PyTorch tutorials](https://pytorch.org/tutorials/)
- [ML System Design Interview](https://github.com/chiphuyen/machine-learning-systems-design)

**Algorithms:**
- [NeetCode.io](https://neetcode.io/practice) - Curated problems
- Focus on video explanations for pattern recognition

**Jane Street Specific:**
- [OCaml tutorial](https://ocaml.org/docs/first-hour)
- Jane Street tech talks on YouTube
- [Real World OCaml](https://dev.realworldocaml.org/) (skim, don't deep dive)

**Research Prep:**
- Your own publications (refresh the narrative)
- Recent Anthropic safety papers (alignment tax, constitutional AI)

**Robotics ML (if time):**
- [Spinning Up in Deep RL](https://spinningup.openai.com/) - Part 1 + PPO section only
- [Mujoco quickstart](https://mujoco.readthedocs.io/en/stable/overview.html)
- RT-2 paper abstract + figures (skim)

---

## Success Metrics

**W05:** Leetcode routine established, 10+ problems, basic NN theory solid
**W06:** 20+ problems total, can explain CNN/RNN/Transformer at high level
**W07:** 35+ problems, can whiteboard ML system design, narrative polished
**W08:** Peak readiness, execute interviews

**Remember:** You're not a new grad grinding for FAANG. You have production systems experience and a PhD. The goal is interview fluency, not algorithm mastery. Leverage your strengths.