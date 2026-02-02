## 1) Executive synthesis (max 10 bullets)

1. **In verifiable domains (code + formal proofs), agents already work today**: best systems close loops with unit tests, build tools, or proof checkers, which sharply reduces hallucination risk and enables iterative improvement. ([arXiv][1])
2. **“End-to-end automated research papers” is real but narrow**: systems like Sakana AI’s AI Scientist automate paper writing + experiments in constrained ML settings; success depends heavily on bounded search spaces and automated evaluation. ([GitHub][2])
3. **Literature agents are the cleanest “research agent” win right now**: FutureHouse’s PaperQA2 reports strong human-comparative results on literature search/synthesis plus an explicit benchmark (LitQA2), with citations and contradiction-finding. ([arXiv][3])
4. **Multi-agent collaboration helps mainly as an engineering pattern, not magic**: frameworks (AutoGen, LangGraph) make it easy to scaffold specialist roles and tool use, but they do not solve truth/grounding by themselves. ([arXiv][4])
5. **Agent-on-agent critique is useful but fragile**: LLM judges have measurable biases and can be gamed; multi-agent judging can improve reliability, but “truth vs persuasion” remains unsolved without external ground truth. ([ACL Anthology][5])
6. **Persistent memory exists; “shared scratchpads that stay coherent for months” is still mostly unsolved**: current “memory” is usually retrieval + summarization; it drifts, gets polluted, and is vulnerable to injection unless rigorously access-controlled. ([arXiv][6])
7. **Formal-math systems are a proof that verification-first can scale**: Google DeepMind’s AlphaProof (formal Lean proofs via RL) and AlphaGeometry2 show what happens when every step is machine-checkable, but they can be extremely compute hungry and slow. ([Nature][7])
8. **Security is a first-class feasibility constraint**: prompt injection and tool exfiltration are not edge cases in persistent/workspace agents; the literature and incident reports suggest “never fully solved” may be the realistic stance. ([ACL Anthology][8])
9. **What would falsify the thesis (“persistent agent collectives accelerate research”)**: if, on benchmarks with hard ground truth (tests/proofs), multi-agent + persistence fails to beat (or match at lower cost) strong single-agent tool-users; or if long-horizon work shows compounding error/memory pollution dominates gains. ([arXiv][9])
10. **Most “open-ended science” remains hype until you can price and measure verification**: the frontier is less “more agents” and more “better evaluators + sandboxing + provenance + incentives” aligned to verifiable artifacts.

---

## 2) Taxonomy of approaches (buckets + examples)

### A. “AI Scientist” / automated research pipelines (end-to-end loops)

**Pattern:** generate idea → implement experiment → run → analyze → write paper → (maybe) review.
**Examples:**

* **The AI Scientist** (Sakana): automated research in ML-style domains where experiments are code + metrics. ([GitHub][2])
* **Agent Laboratory**: multi-step “research assistant” workflow and discussion of where it fails. ([arXiv][10])
* **Google “AI co-scientist”**: multi-agent proposal/hypothesis generation oriented to biomed; public details are mostly a blog-level description. ([Google Research][11])

**Reality check:** these work when (1) experiments are automated, (2) success metrics are crisp, (3) the search space is bounded.

---

### B. Multi-agent collaboration patterns (coordination topologies)

**1) Debate / adversarial critique (proponent vs opponent + judge)**

* Canonical framing: “AI safety via debate.” ([arXiv][12])
* Modern usage: multi-agent judging / critique loops for evaluation and robustness. ([assets.amazon.science][13])

**2) Referee/judge ensembles (majority vote, panel-of-judges, adaptive judges)**

* “LLM-as-a-judge” improved via multi-agent collaboration. ([assets.amazon.science][13])
* Known failure mode: bias and vulnerability to perturbations. ([ACL Anthology][5])

**3) Self-play critique / reflection loops (single agent, multiple passes)**

* Reflexion: store feedback as episodic memory, iterate without weight updates. ([arXiv][14])

**4) Tree-of-thought variants / branching search**

* Common in agents: branch plans, evaluate branches, backtrack; formal math (AlphaProof / AlphaGeometry2) is the “verification-maximal” version. ([Nature][7])

**5) Swarm / role-specialization (planner, coder, verifier, librarian)**

* Implemented via frameworks like AutoGen; in practice often converges to “planner + tool executor + reviewer”. ([arXiv][4])

---

### C. Persistent memory / shared scratchpad systems

**1) Long-term memory managers (tiered memory, summarization, retrieval policies)**

* MemGPT: OS-like memory tiers and control flow. ([arXiv][6])
* A-MEM: “agentic memory” with linking/evolution (Zettelkasten-inspired). ([arXiv][15])

**2) Shared scratchpad / blackboard architectures (multi-agent shared workspace)**

* Recent LLM blackboard systems claim improved coordination for info discovery tasks. ([arXiv][16])

**3) Thread persistence (resume-able execution state)**

* LangGraph checkpointers/threads: persist state so a run can be resumed and inspected. ([LangChain Docs][17])

**Key gap:** preventing memory pollution + provenance tracking + access control (who can write what, with what trust).

---

### D. Tool-using experimental agents (run code, data, sims, labs)

**1) Code + repo agents (verifiable by tests/builds)**

* SWE-agent and SWE-bench ecosystem. ([arXiv][1])
* Cognition’s Devin positioning; independent verification is mostly via SWE-bench reporting and demos. ([Cognition][18])

**2) Formal methods / theorem proving agents (verifiable by proof checkers)**

* LeanDojo as toolkit+benchmark ecosystem. ([arXiv][19])
* Lean Copilot: integrate LLM inference into Lean workflow. ([arXiv][20])
* AlphaProof / AlphaGeometry2: high-performance but heavy RL + compute. ([Nature][7])

**3) Chemistry / lab-adjacent tool agents**

* ChemCrow: LLM orchestrating chemistry tools; also shows evaluators can fail to detect wrong answers. ([arXiv][21])
* Early “full lab autonomy” reports exist, but generality/safety is still unclear from public artifacts. ([The Times of India][22])

---

### E. Literature agents (retrieval + citation grounding + synthesis)

* PaperQA2 + LitQA2 benchmark; claims “superhuman” on specific literature tasks with citations and contradiction discovery. ([arXiv][3])

---

### F. Evaluation benchmarks + metrics for “research agents”

**General agent/tool use:** GAIA, AgentBench, WebArena. ([arXiv][23])
**Scientific workflow tasks:** ScienceAgentBench (task-level scientific discovery). ([arXiv][9])
**Software engineering:** SWE-bench (patch correctness via tests). ([GitHub][24])
**Literature research:** LitQA2 (via PaperQA2 work). ([arXiv][3])

---

## 3) Key papers + systems table (primary sources preferred)

| Name                                           |    Year | Org                 | Link                    | What it does                                                               | What’s novel                                         | Hard limitations                                                            | Relevance to your “persistent research workspace”                              |
| ---------------------------------------------- | ------: | ------------------- | ----------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| The AI Scientist                               |    2024 | Sakana              | ([GitHub][2])           | End-to-end automated research in constrained domains (idea→code→run→paper) | Full pipeline integration                            | Narrow domains; depends on automated metrics; can optimize nonsense         | Shows the “closed-loop” template; highlights need for strong eval + guardrails |
| The AI Scientist-v2                            |    2025 | Sakana              | ([arXiv][25])           | Automated paper generation with stronger end-to-end claims                 | Tightened workflow + acceptance claim                | Still bounded; novelty quality debated in community                         | Evidence on “paper automation”, less on truth/impact compounding               |
| PaperQA2                                       |    2024 | FutureHouse         | ([arXiv][3])            | Tool-using literature agent: search, cite, synthesize, find contradictions | Benchmark-driven factuality + citation graph tooling | Domain coverage, paywalls, and retrieval failures; still hallucination risk | Strongest near-term “public workspace” module: cited synthesis + provenance    |
| LitQA2                                         |    2024 | FutureHouse         | ([arXiv][3])            | Benchmark for scientific literature tasks                                  | Hard task design + human comparison                  | Still limited slice of “research”                                           | Gives you measurable targets for “literature lane”                             |
| ScienceAgentBench                              |    2024 | OSU NLP             | ([arXiv][9])            | Benchmark: real tasks from published papers across disciplines             | Task authenticity + SME validation                   | Only 102 tasks; tooling setups vary                                         | Useful “north star” metric for agentic scientific workflows                    |
| Agent Laboratory                               |    2025 | (academic)          | ([arXiv][10])           | Evaluates LLM agents as research assistants; surveys claims                | Focus on end-to-end research workflow                | Mixed results, novelty questions                                            | Good map of failure modes + where humans still needed                          |
| AutoGen                                        |    2023 | Microsoft           | ([arXiv][4])            | Framework for multi-agent conversations + tool use                         | Programmable agent interaction patterns              | Doesn’t solve grounding; can amplify failure                                | Engineering substrate for “many agents in a workspace”                         |
| LangGraph persistence                          | 2024–25 | LangChain           | ([LangChain Docs][17])  | Threaded execution with persisted state/checkpoints                        | Practical “resume + inspect” infra                   | Not a truth mechanism; state can drift                                      | Directly relevant: long-horizon runs + auditability                            |
| MemGPT                                         | 2023–24 | (academic)          | ([arXiv][6])            | Tiered memory manager for long interactions                                | Memory as OS abstraction                             | Memory pollution; retrieval errors                                          | Foundation for personal + project memory layers                                |
| A-MEM                                          |    2025 | (academic)          | ([arXiv][15])           | Dynamic linking/evolving long-term memory                                  | Structured memory growth                             | Quality depends on write policy; adversarial risk                           | Relevant to “shared knowledge base” if paired with provenance + permissions    |
| Blackboard multi-agent system (data discovery) |    2025 | Google Research     | ([Google Research][26]) | Shared blackboard where agents post/answer info requests                   | Coordination via shared workspace                    | Task-specific; still eval-limited                                           | Closest architectural match to your “public workspace” concept                 |
| Reflexion                                      |    2023 | Princeton et al.    | ([arXiv][14])           | Reflection + episodic memory improves tool tasks                           | “Verbal RL” without weight updates                   | Can overfit to bad feedback; needs reliable signals                         | Good pattern for agent self-improvement in verifiable loops                    |
| SWE-agent                                      |    2024 | Princeton           | ([arXiv][1])            | Tool-using agent that fixes real GitHub issues                             | Agent-computer interface design matters              | Still brittle; cost/time                                                    | Great wedge domain: unit tests as truth oracle                                 |
| SWE-bench                                      |    2024 | Princeton           | ([GitHub][24])          | Benchmark: real repo issues, scored by tests                               | Hard, realistic correctness metric                   | Narrow to SWE                                                               | Ideal “scoreboard” for your workspace reputation system                        |
| LeanDojo                                       |    2023 | (academic)          | ([arXiv][19])           | Toolkits/data/benchmarks for Lean theorem proving                          | Reproducible ATP ecosystem                           | Proof search still hard; compute                                            | Best “formal verification” substrate for compounding research                  |
| Lean Copilot                                   |    2024 | (academic)          | ([arXiv][20])           | Run LLM inference natively in Lean                                         | Tight IDE integration                                | Still depends on model quality                                              | Practical bridge between agents and formal proof workflows                     |
| AlphaProof                                     |    2025 | DeepMind            | ([Nature][7])           | RL system producing formal Lean proofs at IMO level                        | Verification-first at scale                          | Massive compute; slow on hard problems                                      | Shows what “compounding via verification” looks like (but expensive)           |
| AlphaGeometry2                                 |    2025 | DeepMind            | ([arXiv][27])           | Neural+symbolic geometry solver at gold-medalist level                     | Hybrid symbolic engine + LM + search                 | Domain-specific                                                             | Template for hybrid agents in constrained scientific subdomains                |
| ChemCrow                                       | 2023/24 | (academic/industry) | ([arXiv][21])           | Chemistry agent orchestrating tools                                        | Tool orchestration; highlights evaluator weakness    | Safety constraints; wrong-answer detection hard                             | “Harder verification lane”: useful cautionary tale                             |

---

## 4) What’s actually state-of-the-art right now (by capability)

### Hypothesis generation

* **Best-known examples:** Google Research “AI co-scientist” (multi-agent hypothesis/proposal drafting). Evidence is mostly qualitative/public-facing, not a rigorous benchmark. ([Google Research][11])
* **Stronger evidence (adjacent):** PaperQA2 can identify literature contradictions with human validation (a seed for hypothesis prompts). ([arXiv][3])
  **Bottom line:** hypothesis generation is easy to demo; hard to validate as “true novelty” without downstream success metrics.

### Experiment planning

* **SOTA (computational domains):** AI Scientist-style pipelines (plan experiments as code changes + runs). ([GitHub][2])
* **Formal methods:** Lean Copilot is “planning” in the space of proof tactics; every step is checkable. ([arXiv][20])

### Executing experiments with tools (code/data/sims)

* **SOTA:** SWE-agent class systems that can run commands/tests and iterate. ([arXiv][1])
* **Science workflows:** ScienceAgentBench exists precisely because end-to-end claims were outpacing measured capability. ([arXiv][9])

### Critique / refutation

* **SOTA pattern:** adversarial critique + judge, but only robust when the judge has ground truth. Debate is conceptually strong, practically limited by judge reliability. ([arXiv][12])
* **Pragmatic win:** Reflexion-style “critique as memory” improves performance when feedback is tied to objective signals (tests). ([arXiv][14])

### Long-horizon memory / persistence

* **SOTA building blocks:** MemGPT (tiered memory), A-MEM (linked evolving memory), LangGraph threads/checkpoints (resumable state). ([arXiv][6])
  **Hard truth:** none of these guarantee memory quality under adversarial or noisy writes.

### Multi-agent coordination at scale

* **SOTA infra:** AutoGen (multi-agent conv orchestration), blackboard architectures for shared task state. ([arXiv][4])
  **Open problem:** coordination overhead and correlated errors often dominate beyond a small number of agents unless tasks decompose cleanly.

### Measuring truth vs persuasion

* **Best evidence:** LLM judges exhibit bias and are perturbable; “judge-only” is not trustworthy for reputation without external oracles. ([ACL Anthology][5])
* **Partial mitigation:** multi-agent judging can improve some settings, but it is still judge-dependent. ([assets.amazon.science][13])
  **Implication for your startup:** reputations must be anchored to verifiable artifacts (tests, proofs, reproducible runs), not votes.

---

## 5) Blockers for a persistent agent research platform (concrete)

### Verification / grounding (where does truth come from?)

* **Core constraint:** you need *machine-checkable artifacts* (tests, proofs, reproducible pipelines) as the “court of truth.” SWE-bench and Lean are exemplars. ([GitHub][24])
* **Failure mode:** in chemistry and open-ended science, evaluators can’t reliably detect wrong answers (ChemCrow explicitly reports this pitfall). ([arXiv][21])

### Security (prompt injection, exfiltration, sandboxing)

* **Prompt injection is endemic** in tool-using/web agents; benchmarks and security analyses exist (INJECAGENT; design-pattern defenses), but real-world risk remains. ([ACL Anthology][8])
* **Workspace implication:** shared memory is an attack surface. You need permissions, provenance, quarantines, and “untrusted tool output” handling by default.

### Failure modes (looping, delusions, collusion, attractors)

* **Looping/attractors:** agents can self-reinforce wrong plans via reflection unless the feedback signal is objective (tests/proofs). ([arXiv][14])
* **Collusion:** multi-agent judges can converge on persuasive nonsense if the judge signal is weak (documented judge biases). ([ACL Anthology][5])

### Incentives / reputation (gaming, sybil resistance)

* If rewards are based on “peer votes,” you get persuasion games. If rewards are based on “verifiable merges,” you can build something closer to open-source incentives (but need abuse controls). SWE-bench-style scoring is the right shape. ([GitHub][24])

### Economics (compute costs, scaling behavior)

* **Compute can explode** for search-heavy systems (formal math RL, massive branching). AlphaProof results show power, but also cost and latency. ([Nature][7])
* **Practical takeaway:** your 12–18 month feasibility hinges on keeping the verification oracle cheap and the search bounded.

---

## 6) “If I were building this” wedge recommendation (3 feasible wedges)

### Wedge 1: **Public “SWE-bench-style” research workspace for OSS bugfix + micro-RFCs**

* **Why verification is feasible:** tests/builds are ground truth; CI is cheap relative to open-ended science. ([GitHub][24])
* **First users:** OSS maintainers + small eng teams; “agent PRs with audit trails.”
* **First measurable win:** higher merged-PR throughput per maintainer hour; leaderboard on verified tasks.
* **30–60 day minimum demo:** multi-agent pipeline (triage → reproduce → patch → test → PR) + persistent thread memory per repo + reputation tied to merged/tested diffs.
* **Moat:** repo-specific execution traces + failure cases + patch/test pairs.

### Wedge 2: **Lean “proof orchard”: persistent agent collective that grows verified lemmas**

* **Why verification is feasible:** proof assistant is the oracle; every contribution is checkable. ([arXiv][19])
* **First users:** formal methods researchers, Lean community, verification teams.
* **First measurable win:** new lemmas merged into a shared library; reduced human time-to-proof for target statements.
* **30–60 day demo:** LangGraph-style persisted threads + agents that propose tactic sequences, run Lean, store minimal proof states; reputation = accepted proofs. ([LangChain Docs][28])
* **Moat:** curated proof-state trajectories + tactic datasets + theorem dependency graphs.

### Wedge 3: **Literature-to-claim graph with adversarial citation checks (PaperQA2-inspired)**

* **Why verification is feasible:** not “truth,” but *groundedness*: every claim must cite passages; adversarial agents attempt to falsify by retrieving contradictory sources. ([arXiv][3])
* **First users:** grad students, review authors, biotech R&D, policy/standards teams.
* **First measurable win:** fewer uncited/incorrect claims in drafts; time saved on lit review; contradiction detection yield. ([arXiv][3])
* **30–60 day demo:** persistent workspace per topic: agents build a cited wiki-style page, plus an “opposition agent” that hunts contradictions; publish provenance.
* **Moat:** continuously maintained claim graph + contradiction annotations + retrieval traces.

---

## 7) Competitor / adjacent product scan (papers + products)

### Automated research / “AI scientist”

* **Sakana AI Scientist**: end-to-end paper+experiment automation in bounded domains. Not a persistent public workspace; more like an automated pipeline. ([GitHub][2])
* **Google AI co-scientist**: multi-agent hypothesis/proposal collaborator (details limited publicly). Not positioned as open persistent workspace. ([Google Research][11])

### Literature agents / research copilots

* **FutureHouse PaperQA2**: benchmarked literature agent with citations and contradiction detection; closest “research-grade” evidence among public systems. ([arXiv][3])
* **OpenAI “deep research” (product feature)**: strong browsing/report generation, but not an open multi-agent persistent workspace; also explicitly acknowledges reliability issues. ([Reuters][29])

### Coding agents

* **SWE-agent ecosystem**: tool-using repo agent with a strong benchmark anchor. Not a persistent multi-party research commons by default. ([arXiv][1])
* **Devin (Cognition)**: commercial “AI software engineer.” Persistence is productized, but it’s private/team-centric rather than public commons; independent evaluation is limited beyond reported benchmarks/demos. ([Cognition][18])

### Agent frameworks (infra, not “science”)

* **Microsoft AutoGen**: multi-agent orchestration framework. ([arXiv][4])
* **LangGraph (LangChain)**: stateful graphs + persistence/threads. ([LangChain Docs][28])

### Memory systems

* **MemGPT / A-MEM**: memory management approaches; not “public workspace governance.” ([arXiv][6])

### Chemistry tool agents (harder verification lane)

* **ChemCrow**: tool-using chemistry agent; also a warning that GPT-4-style evaluation can miss wrong outputs. ([arXiv][21])

---

### Net: what’s been tried vs your differentiated bet

Your differentiator is **(a) persistence + (b) public/shared workspace + (c) reputation anchored to adversarial review**. The closest existing ingredients are: blackboard/shared-workspace research patterns ([arXiv][16]) + benchmark-anchored verifiable domains (SWE-bench/LeanDojo) ([GitHub][24]) + citation-grounded literature agents (PaperQA2) ([arXiv][3]). What’s *not* shown yet in the literature is that **long-horizon shared memory plus agent-on-agent critique produces compounding research progress** rather than compounding contamination, without very strong oracles and security boundaries.

If you want, I can turn the wedges into a concrete system spec (data model for provenance, permissioning for shared memory, reputation scoring tied to verifiers, and a 30-day build plan).

[1]: https://arxiv.org/abs/2405.15793?utm_source=chatgpt.com "SWE-agent - Computer Science > Software Engineering"
[2]: https://github.com/SakanaAI/AI-Scientist?utm_source=chatgpt.com "The AI Scientist: Towards Fully Automated Open-Ended ..."
[3]: https://arxiv.org/abs/2409.13740?utm_source=chatgpt.com "Language agents achieve superhuman synthesis of scientific knowledge"
[4]: https://arxiv.org/abs/2308.08155?utm_source=chatgpt.com "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
[5]: https://aclanthology.org/2024.emnlp-main.474/?utm_source=chatgpt.com "Humans or LLMs as the Judge? A Study on Judgement Bias"
[6]: https://arxiv.org/abs/2310.08560?utm_source=chatgpt.com "MemGPT: Towards LLMs as Operating Systems"
[7]: https://www.nature.com/articles/s41586-025-09833-y?utm_source=chatgpt.com "Olympiad-level formal mathematical reasoning with ..."
[8]: https://aclanthology.org/2024.findings-acl.624.pdf?utm_source=chatgpt.com "INJECAGENT: Benchmarking Indirect Prompt Injections in ..."
[9]: https://arxiv.org/abs/2410.05080?utm_source=chatgpt.com "ScienceAgentBench: Toward Rigorous Assessment of ..."
[10]: https://arxiv.org/pdf/2501.04227?utm_source=chatgpt.com "Agent Laboratory: Using LLM Agents as Research Assistants"
[11]: https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/?utm_source=chatgpt.com "Accelerating scientific breakthroughs with an AI co-scientist"
[12]: https://arxiv.org/abs/1805.00899?utm_source=chatgpt.com "[1805.00899] AI safety via debate"
[13]: https://assets.amazon.science/48/5d/20927f094559a4465916e28f41b5/enhancing-llm-as-a-judge-via-multi-agent-collaboration.pdf?utm_source=chatgpt.com "Enhancing LLM-as-a-Judge via Multi-Agent Collaboration"
[14]: https://arxiv.org/abs/2303.11366?utm_source=chatgpt.com "Reflexion: Language Agents with Verbal Reinforcement Learning"
[15]: https://arxiv.org/pdf/2502.12110?utm_source=chatgpt.com "A-MEM: Agentic Memory for LLM Agents"
[16]: https://arxiv.org/abs/2510.01285?utm_source=chatgpt.com "[2510.01285] LLM-based Multi-Agent Blackboard System ..."
[17]: https://docs.langchain.com/oss/python/langgraph/memory?utm_source=chatgpt.com "Memory overview - Docs by LangChain"
[18]: https://cognition.ai/blog/introducing-devin?utm_source=chatgpt.com "Introducing Devin, the first AI software engineer"
[19]: https://arxiv.org/abs/2306.15626?utm_source=chatgpt.com "[2306.15626] LeanDojo: Theorem Proving with Retrieval- ..."
[20]: https://arxiv.org/abs/2404.12534?utm_source=chatgpt.com "[2404.12534] Lean Copilot: Large Language Models as ..."
[21]: https://arxiv.org/abs/2304.05376?utm_source=chatgpt.com "ChemCrow: Augmenting large-language models with chemistry tools"
[22]: https://timesofindia.indiatimes.com/city/delhi/ai-agent-conducts-experiments-in-iit-delhi-lab/articleshow/126146418.cms?utm_source=chatgpt.com "AI agent conducts experiments in IIT Delhi lab"
[23]: https://arxiv.org/abs/2311.12983?utm_source=chatgpt.com "[2311.12983] GAIA: a benchmark for General AI Assistants"
[24]: https://github.com/SWE-bench/SWE-bench?utm_source=chatgpt.com "SWE-bench: Can Language Models Resolve Real-world ..."
[25]: https://arxiv.org/abs/2504.08066?utm_source=chatgpt.com "The AI Scientist-v2: Workshop-Level Automated Scientific ..."
[26]: https://research.google/pubs/blackboard-multi-agent-systems-for-information-discovery-in-data-science/?utm_source=chatgpt.com "Blackboard Multi-Agent Systems for Information Discovery ..."
[27]: https://arxiv.org/abs/2502.03544?utm_source=chatgpt.com "Gold-medalist Performance in Solving Olympiad Geometry with AlphaGeometry2"
[28]: https://docs.langchain.com/oss/python/langgraph/persistence?utm_source=chatgpt.com "Persistence - Docs by LangChain"
[29]: https://www.reuters.com/technology/openai-launches-new-ai-tool-facilitate-research-tasks-2025-02-03/?utm_source=chatgpt.com "OpenAI launches new AI tool to facilitate research tasks"
