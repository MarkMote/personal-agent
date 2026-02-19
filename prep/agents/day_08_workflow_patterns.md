# Day 8: Workflow Patterns (Chains, Routing, Parallel) (~2 hrs)

**Goal:** Build the three key orchestration patterns from Anthropic's "Building Effective Agents" blog. These are simpler than an autonomous agent and often the right answer. Knowing when to use each shows Anthropic-aligned thinking.

---

## Reading (20 min)

1. **"Building Effective Agents" blog** (re-read the patterns section)
   - https://www.anthropic.com/engineering/building-effective-agents

2. **Cookbook: Basic Workflows** - https://platform.claude.com/cookbook/patterns-agents-basic-workflows
   - Implementations of chaining, parallelization, routing

**The complexity ladder (memorize this):**
```
Single LLM call (optimized prompt)
  -> Prompt chaining (sequential steps)
    -> Routing (classify then specialize)
      -> Parallelization (concurrent tasks)
        -> Orchestrator-workers (dynamic delegation)
          -> Evaluator-optimizer (generate + critique)
            -> Autonomous agent (tool-using loop)
```

**Interview signal:** If you can identify that a problem is solvable with chaining instead of a full agent loop, say so. This shows you've internalized Anthropic's "start simple" philosophy.

---

## Pattern 1: Prompt Chaining (30 min)

Break a complex task into sequential LLM calls, where each step's output feeds into the next.

**When to use:** Tasks with clear sequential stages. Each step is simpler and more reliable than one big prompt.

```python
import anthropic
client = anthropic.Anthropic()

def chain_call(prompt, system=None, model="claude-sonnet-4-20250514"):
    """Helper for a single LLM call in a chain."""
    response = client.messages.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
        **({"system": system} if system else {})
    )
    return response.content[0].text

# Example: Research Report Pipeline
# Step 1: Extract key topics from raw text
# Step 2: Generate outline from topics
# Step 3: Write report from outline

def research_report_chain(raw_text):
    # Step 1: Extract
    topics = chain_call(
        f"Extract the 3-5 key topics from this text. Return only a numbered list.\n\n{raw_text}",
        system="You are a research analyst. Be concise."
    )
    print(f"Step 1 - Topics:\n{topics}\n")

    # Gate: Check if we got usable topics
    if "1." not in topics:
        return "Error: Could not extract topics from text."

    # Step 2: Outline
    outline = chain_call(
        f"Create a report outline based on these topics:\n{topics}\n\nFormat: numbered sections with 2-3 bullet points each.",
        system="You are a technical writer."
    )
    print(f"Step 2 - Outline:\n{outline}\n")

    # Step 3: Write
    report = chain_call(
        f"Write a concise 300-word report following this outline:\n{outline}\n\nUse clear, professional language.",
        system="You are a senior technical writer. Write clearly and concisely."
    )
    print(f"Step 3 - Report:\n{report}\n")

    return report

# Test
sample = """
Anthropic recently released Claude 4.5 with improved coding, extended thinking,
and new agent capabilities. The Agent SDK allows developers to build production
AI agents. MCP provides standardized tool integration. The company emphasizes
safety research alongside capability improvements.
"""
result = research_report_chain(sample)
```

### Key Pattern: Gate Checks Between Steps
```python
# Insert validation between chain steps
def chain_with_gates(text):
    # Step 1
    summary = chain_call(f"Summarize in 1 sentence: {text}")

    # Gate: Is the summary good enough?
    quality = chain_call(
        f"Rate this summary 1-10 for accuracy and completeness. "
        f"Return ONLY a number.\n\nOriginal: {text}\n\nSummary: {summary}"
    )

    if int(quality.strip()) < 7:
        # Retry with more context
        summary = chain_call(
            f"The previous summary was rated {quality}/10. "
            f"Write a better 1-sentence summary: {text}"
        )

    return summary
```

---

## Pattern 2: Routing (30 min)

Classify the input first, then route to a specialized handler.

**When to use:** Different input types need different processing. One general prompt can't handle all cases well.

```python
def route_request(user_message):
    """Route a user message to the appropriate handler."""

    # Step 1: Classify
    category = chain_call(
        f"""Classify this user request into exactly one category:
- TECHNICAL: coding questions, debugging, architecture
- CREATIVE: writing, brainstorming, content creation
- ANALYSIS: data analysis, comparisons, research
- GENERAL: greetings, simple questions, other

Return ONLY the category name, nothing else.

User request: {user_message}""",
        system="You are a request classifier. Return only the category name."
    )
    category = category.strip().upper()
    print(f"Routed to: {category}")

    # Step 2: Route to specialized handler
    handlers = {
        "TECHNICAL": handle_technical,
        "CREATIVE": handle_creative,
        "ANALYSIS": handle_analysis,
    }

    handler = handlers.get(category, handle_general)
    return handler(user_message)

def handle_technical(message):
    return chain_call(message, system="""You are a senior software engineer.
Be precise and include code examples. Consider edge cases.""")

def handle_creative(message):
    return chain_call(message, system="""You are a creative writer.
Be imaginative and engaging. Use vivid language.""")

def handle_analysis(message):
    return chain_call(message, system="""You are a data analyst.
Be thorough and evidence-based. Use structured formatting.""")

def handle_general(message):
    return chain_call(message)

# Test
print(route_request("Write a Python function to sort a linked list"))
print("---")
print(route_request("Compare the pros and cons of React vs Vue"))
```

### Routing with Structured Output

```python
import json

def route_with_context(user_message):
    """Route with structured classification that includes reasoning."""
    classification = chain_call(
        f"""Analyze this request and classify it. Return JSON only:
{{
    "category": "TECHNICAL|CREATIVE|ANALYSIS|GENERAL",
    "confidence": 0.0-1.0,
    "reasoning": "brief explanation",
    "key_terms": ["term1", "term2"]
}}

Request: {user_message}""",
        system="Return only valid JSON."
    )

    try:
        parsed = json.loads(classification)
        print(f"Category: {parsed['category']} (confidence: {parsed['confidence']})")

        if parsed["confidence"] < 0.7:
            # Low confidence - use general handler
            return handle_general(user_message)

        handlers = {"TECHNICAL": handle_technical, "CREATIVE": handle_creative,
                     "ANALYSIS": handle_analysis}
        return handlers.get(parsed["category"], handle_general)(user_message)
    except (json.JSONDecodeError, KeyError):
        return handle_general(user_message)
```

---

## Pattern 3: Parallelization (30 min)

Run multiple independent LLM calls concurrently.

**When to use:** Multiple independent subtasks that can run simultaneously.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def parallel_analysis(topic):
    """Analyze a topic from multiple perspectives in parallel."""

    # Define independent subtasks
    perspectives = {
        "pros": f"List the top 3 advantages of {topic}. Be specific and concise.",
        "cons": f"List the top 3 disadvantages of {topic}. Be specific and concise.",
        "trends": f"What are the current trends related to {topic}? List 3.",
        "alternatives": f"What are the top 3 alternatives to {topic}?",
    }

    results = {}

    # Run all in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(chain_call, prompt): name
            for name, prompt in perspectives.items()
        }

        for future in as_completed(futures):
            name = futures[future]
            try:
                results[name] = future.result()
            except Exception as e:
                results[name] = f"Error: {str(e)}"

    # Synthesize results
    synthesis_prompt = f"""Synthesize these analyses of "{topic}" into a balanced 200-word summary:

Pros: {results['pros']}
Cons: {results['cons']}
Trends: {results['trends']}
Alternatives: {results['alternatives']}

Write a balanced analysis that considers all perspectives."""

    summary = chain_call(synthesis_prompt, system="Write a balanced, concise analysis.")
    return {"perspectives": results, "summary": summary}

# Test
result = parallel_analysis("using AI agents in production")
for key, value in result["perspectives"].items():
    print(f"\n[{key}]\n{value}")
print(f"\n[Summary]\n{result['summary']}")
```

### Parallel with Voting (Aggregation)

```python
def parallel_vote(question, num_voters=3):
    """Get multiple answers and take the consensus."""
    with ThreadPoolExecutor(max_workers=num_voters) as executor:
        futures = [
            executor.submit(chain_call, question)
            for _ in range(num_voters)
        ]
        answers = [f.result() for f in futures]

    # Synthesize
    consensus = chain_call(
        f"""These are {num_voters} independent answers to: "{question}"

{chr(10).join(f'Answer {i+1}: {a}' for i, a in enumerate(answers))}

What is the consensus? If they agree, state the answer. If they disagree, explain the disagreement and give the most likely correct answer.""",
        system="You are an arbiter. Be precise."
    )
    return {"answers": answers, "consensus": consensus}
```

---

## Bonus: Orchestrator-Workers Pattern (10 min concept)

The orchestrator dynamically decides what subtasks to create:

```python
def orchestrator_workers(task):
    """Orchestrator plans subtasks, workers execute them."""
    # Step 1: Orchestrator plans
    plan = chain_call(
        f"""Break this task into 2-4 independent subtasks. Return JSON:
[{{"task": "description", "type": "research|write|analyze"}}]

Task: {task}""",
        system="Return only valid JSON array."
    )

    subtasks = json.loads(plan)
    print(f"Plan: {json.dumps(subtasks, indent=2)}")

    # Step 2: Workers execute in parallel
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(chain_call, st["task"]): st
            for st in subtasks
        }
        results = []
        for future in as_completed(futures):
            st = futures[future]
            results.append({"task": st["task"], "result": future.result()})

    # Step 3: Orchestrator synthesizes
    synthesis = chain_call(
        f"Original task: {task}\n\nSubtask results:\n" +
        "\n".join(f"- {r['task']}: {r['result']}" for r in results) +
        "\n\nSynthesize into a final answer.",
        system="Combine the results into a comprehensive response."
    )
    return synthesis
```

---

## Key Takeaways

- **Chaining:** Sequential LLM calls. Insert gate checks between steps. Use when tasks have clear stages.
- **Routing:** Classify first, then dispatch to specialized handlers. Use when different inputs need different treatment.
- **Parallelization:** Concurrent independent calls. Use ThreadPoolExecutor. Great for multi-perspective analysis.
- **Orchestrator-Workers:** Dynamic planning + parallel execution + synthesis.
- **Interview gold:** If a problem is solvable with chaining/routing, say "this doesn't need a full agent loop - a chain would be more reliable." That's exactly what Anthropic wants to hear.
