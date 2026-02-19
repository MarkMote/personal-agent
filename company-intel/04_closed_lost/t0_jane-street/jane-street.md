# Jane Street

## Quick Facts
- **Location:** NYC (250 Vesey Street, Brookfield Place)
- **Stage:** Established quant trading firm
- **Focus:** Quantitative trading, ML for trading strategies

## The Opportunity
Jane Street is one of the most PhD-friendly quant firms. They train ML models on thousands of GPUs for trading in nonstationary, competitive multi-agent environments. Strong research culture, $300k base + significant bonus.

## Target Role
**Machine Learning Engineer** (they rerouted from our ML Researcher application)

Key responsibilities:
- Train deep learning models for trading strategies
- Build and maintain training and inference infrastructure
- Work with nonstationary datasets, multi-agent competition
- Debug distributed training, study model behavior in production
- Collaborate with researchers, engineers, and traders

**Secondary:** They evaluate for all roles continuously — may consider Quantitative Researcher or ML Researcher based on interview performance.

## Your Angle
**Resume:** Distinguished Academic

**Why you (narrative):**
- **Nonstationary dynamics** = your wheelhouse. Trading with regime shifts (pandemics, elections) is structurally analogous to adaptive control problems in spacecraft systems.
- **Optimization expertise** directly applicable - regularization, mathematical foundations
- **Research taste** - PhD training in navigating ambiguous problems
- **RL background** aligns with their ML work
- **Production ML** - built real systems at Roostr (LLM pipeline) and Pytheia (CV)

## Key People
| Name | Role | Path |
|------|------|------|
| Hannah Hasen | Recruiting (primary contact) | hhasen@janestreet.com, responded to application |
| Matt Horder | Recruiting (cc'd) | mhorder@janestreet.com, on thread |
| Laura Parsons | Experienced Hire Recruiting | Original outreach target (LinkedIn) |
| Greg Mannix | Technical Recruiting | 2nd degree (mutual: Anand Chaturvedi) |

## Application Notes
- Applied online 2026-01-23 (ML Researcher) + LinkedIn outreach to Laura Parsons
- Hannah responded 2026-01-28, rerouted to ML Engineering position
- Human review, ~1 week response
- No finance background required
- They evaluate for all roles continuously

## Interview Process

### Overall Structure (from Hannah's email + ML interview guide)
1. **Round 1: SWE Coding** — Zoom/CoderPad (35-60 min) — **THIS IS TUE 2/17 10:30am**
2. **Subsequent Zoom rounds** — ML-focused (model training, theory, data science)
3. **Full day onsite** — Final round, in-person at 250 Vesey

### Round 1: SWE Coding (Tue 2/17) — What to expect
- **Interviewer is a standard SWE.** They won't have specific ML role context.
- **Format:** Progressive coding problem on CoderPad, gets harder in stages
- **Example from their blog:** Memoization problem in 3 parts:
  - Part 1: Implement a caching function (hash table). Should be quick and bug-free.
  - Part 2: Address memory concerns — FIFO eviction with O(1) complexity
  - Part 3: LRU caching — trade-offs between O(n) and O(1) implementations (doubly-linked list)
- **Most passing candidates** complete parts 1-2. Part 3 distinguishes strong performers.
- **They care about:** clean code, clear communication, proactive issue identification, complexity analysis
- **They do NOT test:** mental math, logic puzzles, algorithm bingo, "aha moment" problems
- **Use Python.** They say use whatever you're strongest in. OCaml not expected.
- Write real code, not pseudocode.

### Later ML Rounds — What to expect
Three question categories across the ML-focused interviews:
- **Coding/ML:** Write code that trains a model (tree-based or neural net). Justify choices (model, loss function, metrics, hyperparameters). They care about the "why" behind decisions.
- **ML Theory:** Here's a NN architecture — how would you expect it to perform? How would you improve it?
- **Data science:** Here's a dataset — explore it, discuss features, discuss how to model it.

**ML Engineer focus areas** (from their guide):
- Actual implementation and workflow around training and serving models
- Knowledge of open-source ecosystem tools
- Code refactoring instincts — mention improvements as you see them
- Efficiency awareness — understand what computation is happening under the hood

### Zoom Details (Round 1)
- **Date:** Tue 2/17 10:30am ET
- **Zoom:** https://janestreet.zoom.us/j/89330730615?pwd=ild3L7yDuHjqUYaUM9xbE9YEIHibYP.1
- **Meeting ID:** 893 3073 0615
- **Passcode:** 989585
- **CoderPad:** Interviewer will provide session key at start of call

### Key quotes from their materials
- "The journey through the interview matters much more than the snapshot of the solution at the end of it."
- "We're primarily trying to get a sense for what it's like to work with you!"
- "Less emphasis on clever algorithms and more on system design"
- "Please don't use PyTorch just because you think it will make us happy. We want to see you at your best."

## Prep Resources (from Jane Street)
- [ML Interview Guide (PDF)](https://www.janestreet.com/static/pdfs/ml-interview-guide.pdf)
- [Preparing for a Software Engineering Interview](https://www.janestreet.com/preparing-for-a-software-engineering-interview/) — mock question walkthrough
- [What a Jane Street Dev Interview Is Like (blog)](https://blog.janestreet.com/what-a-jane-street-dev-interview-is-like/) — the memoization example
- [Software Engineering Mock Interview (video)](https://www.janestreet.com/mock-interview/)

## Notes
**2026-01-23:** Applied for ML Researcher + sent LinkedIn InMail to Laura Parsons.
**2026-01-28:** Hannah Hasen responded. Rerouted to ML Engineering position. Requested Feb 17 week for first round.
**2026-02-09:** Interview confirmed Tue 2/17 10:30am. First round is SWE coding (not ML-specific). Interviewer is standard SWE, no ML role context. ML interview guide PDF reviewed.
**2026-02-17:** Round 1 completed. Felt it went generally well.
**2026-02-18:** Rejected via email. "We've decided not to move forward with your candidacy at this time."
