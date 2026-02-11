
Thoughts
- Strongly suspect that building around a single model would be much less robust
	- models have sensitivity in a lot of areas, heterogeneity regularizes
- Smells a lot like taking what worked for alpha go and adapting it to open ended problem solving
- Wonder if RLMs would be of use in this area
- I mean the biggest issue with agents is that they dont have taste. research taste or design taste. Its interesting to see if you can solve that essentially with more compute and a clever architechture. 
- Wonder whats the best way to stick HITL
- If you could add an approach like this to an area where you had clearer evaluation framework, like robotics, it would be be strong. 
- Still seems siloed in some ways. Would be interesting to have a concept of branching, parallel tree search over hyptheses 
- For hypthesis generation i had a particular method i used a lot in grad school
- What happens when you reach a dead end? 
- Two most critical parts:
	- hypothesis generation: thinking outside of the box is hard 
	- Review: LLMs lack taste
- Robustness and improvement 
	- heterogeneity 
	- prompt variations. very likely you would be over-indexing on certain things
	- could be more interesting hypothesis generation strategies: give it partial info and let it guess for instance. Its creativity through hallucination. 
	- maintain library of tools 
- 

Questions
- What are core agents? how many? 
- what does tournament look like? 
- what does the "evolution" look like? What exactly iteratively improves? 
- what is an agent swarm, is this one? 
- whats the architechture of an individual agent?
- How is memory handled? Rag.
- Do the agents themselves change as part of the tournament? 
	- would be interesting to see the actual prompts and architecture evolve 
- What does interim feedback look like? what should it look like
- I see something about ELO, how is that used? 
- Is it all on Gemini 2? 
- Still dont get what the overall structure / information loop looks like
	- who talks to who
	- when does it end? 
- Whats evolved in this area in the year since pubication? 


General Agent questions
- How are people building memory for llms today? what are the hot methods? heirarchical memory sysetms? RLMs? Rag? 
- What are the basic components of an agent in 2026: tools, React loop, what else? 


Notes
- multi-agent architecture 
- tournament evolution process for self improving hypothesis generation 
- Idea seems to be using agents to mirror the reasoning process of the scientific method
	- Hypothesis generation
	- Reflection 
	- Evolution 
- Uses tournaments and self play
- Core components: 
	- Natural language interface 
	- Asynchronous Task framework 
		- supervisor agent to manage worker task queues, allocate resources
	- Specialized worker agents
	- Context memory
- Specialized agents
	- Generation Agent: plans the process
	- Reflection Agent: simulates peer review
	- Ranking Agent: different proposals ranked 
	- Proximity Agent: consolidates similar ideas 
	- Evolution Agent: refines top ranked hypotheses
	- Meta-Review agent: 
- How it evolves: 
	- Hypotheses have ELOs 
	- Evolution agent looks at high ELO ideas and mutates based on critique 
	- Mutated hypothesis goes to supervisor and the process repeats
	- Meta-review agent decides stopping point and if there is consensus 
- Memory: 
	- maintains a project knowledge graph
	- does RAG over this 
- New things
	- Agentic tree search: like monte carlo tree seach in hypothesis space 
- hypothesis object: like a git repo of scientific thought 
	- core statement
	- evidence log
	- refutation file
	- simulation code 
	- elo rating 
	- lineage 