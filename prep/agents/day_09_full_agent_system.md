# Day 9: Full Agent System (~2 hrs)

**Goal:** Combine everything into a complete, polished agent system. This is the dress rehearsal - build something interview-quality from start to finish.

---

## Reading (15 min)

1. **Agent SDK overview** (skim) - https://platform.claude.com/docs/en/agent-sdk/overview
   - Not for building in the interview, but know it exists
   - Built-in tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
   - Hooks, subagents, permission modes
   - `claude_agent_sdk` package for Python/TypeScript

2. **Agent Skills** (skim) - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
   - Skills = modular, filesystem-based capabilities
   - Progressive disclosure: metadata always loaded, instructions on-demand, resources as-needed
   - Pre-built skills for PDF, Excel, PowerPoint, Word

**These are "know it exists" topics.** If asked, you can discuss the architecture, but the interview project will use the raw Messages API.

---

## Project: Research & Report Agent (1 hr 30 min)

Build a complete agent that can research a topic using multiple tools and produce a structured report. This is a realistic 45-minute interview scenario.

### Step 1: Define the Tool Suite (15 min)

```python
import anthropic
import json
from datetime import datetime

client = anthropic.Anthropic()

tools = [
    {
        "name": "search_web",
        "description": "Search the web for information on a topic. Returns a list of search results with titles and snippets. Use this as the first step when researching any topic.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query - be specific for better results"
                },
                "num_results": {
                    "type": "integer",
                    "description": "Number of results to return (1-10)",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "read_url",
        "description": "Fetch and read the content of a web page. Returns the text content of the page (up to 5000 chars). Use after search_web to read promising results in detail.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "URL to fetch"
                }
            },
            "required": ["url"]
        }
    },
    {
        "name": "take_notes",
        "description": "Save important findings to your research notes. Use this to accumulate key facts, quotes, and data points as you research. Each note is tagged with a source.",
        "input_schema": {
            "type": "object",
            "properties": {
                "note": {
                    "type": "string",
                    "description": "The finding or fact to save"
                },
                "source": {
                    "type": "string",
                    "description": "Where this information came from"
                },
                "category": {
                    "type": "string",
                    "enum": ["fact", "statistic", "quote", "opinion", "question"],
                    "description": "Type of note"
                }
            },
            "required": ["note", "source", "category"]
        }
    },
    {
        "name": "generate_report",
        "description": "Generate the final structured report from accumulated research notes. Call this only after you have gathered sufficient information using search_web, read_url, and take_notes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Report title"
                },
                "format": {
                    "type": "string",
                    "enum": ["brief", "detailed", "executive_summary"],
                    "description": "Report format"
                }
            },
            "required": ["title", "format"]
        }
    }
]
```

### Step 2: Implement Tool Functions (15 min)

```python
# In-memory state for the agent
research_notes = []

# Mock implementations (replace with real APIs in production)
MOCK_SEARCH_RESULTS = {
    "anthropic ai agents": [
        {"title": "Building Effective Agents - Anthropic", "url": "https://anthropic.com/agents", "snippet": "Anthropic's guide to building AI agents with Claude..."},
        {"title": "Agent SDK Overview", "url": "https://platform.claude.com/docs/agent-sdk", "snippet": "Build production AI agents with the Agent SDK..."},
        {"title": "MCP Protocol", "url": "https://modelcontextprotocol.io", "snippet": "The Model Context Protocol standardizes AI tool integration..."},
    ],
    "default": [
        {"title": "Example Result", "url": "https://example.com", "snippet": "Some relevant information about the topic..."},
    ]
}

MOCK_PAGES = {
    "https://anthropic.com/agents": "Anthropic recommends starting with simple prompt chaining before building full agents. Key patterns include routing, parallelization, and orchestrator-workers. The Agent SDK provides built-in tools for file operations and web access.",
    "https://platform.claude.com/docs/agent-sdk": "The Agent SDK (formerly Claude Code SDK) lets you build autonomous agents in Python and TypeScript. Features include built-in tools (Read, Edit, Bash, Glob, Grep), hooks for lifecycle events, and subagent spawning.",
    "default": "This page contains relevant information about the requested topic."
}

def search_web(query, num_results=5):
    results = MOCK_SEARCH_RESULTS.get(query.lower(), MOCK_SEARCH_RESULTS["default"])
    return json.dumps(results[:num_results])

def read_url(url):
    content = MOCK_PAGES.get(url, MOCK_PAGES["default"])
    return content

def take_notes(note, source, category):
    entry = {
        "note": note,
        "source": source,
        "category": category,
        "timestamp": datetime.now().isoformat()
    }
    research_notes.append(entry)
    return json.dumps({"saved": True, "total_notes": len(research_notes)})

def generate_report(title, format="brief"):
    if not research_notes:
        return json.dumps({"error": "No research notes. Use take_notes first."})

    report = {
        "title": title,
        "format": format,
        "generated_at": datetime.now().isoformat(),
        "notes_count": len(research_notes),
        "notes": research_notes,
        "categories": {}
    }

    for note in research_notes:
        cat = note["category"]
        if cat not in report["categories"]:
            report["categories"][cat] = []
        report["categories"][cat].append(note["note"])

    return json.dumps(report, indent=2)

tool_functions = {
    "search_web": search_web,
    "read_url": read_url,
    "take_notes": take_notes,
    "generate_report": generate_report,
}
```

### Step 3: The Agent Loop (use from Day 3, with improvements) (10 min)

```python
def run_research_agent(query, max_turns=15):
    """Complete research agent with observability."""
    global research_notes
    research_notes = []  # Reset for each query

    system = """You are a thorough research agent. Your process:
1. Search for relevant information
2. Read the most promising results
3. Take structured notes on key findings
4. When you have enough information, generate a report

Be systematic: search broadly first, then dive deep into the best sources.
Always take notes before generating the report."""

    messages = [{"role": "user", "content": query}]

    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=system,
            tools=tools,
            messages=messages,
        )

        # Log
        print(f"\n--- Turn {turn + 1} | {response.stop_reason} ---")
        for block in response.content:
            if hasattr(block, "text") and block.text:
                print(f"  [Think] {block.text[:150]}")

        if response.stop_reason == "end_turn":
            final = "".join(b.text for b in response.content if hasattr(b, "text"))
            print(f"\n{'='*60}\nFINAL OUTPUT:\n{final}")
            return final

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  [{block.name}] {json.dumps(block.input)[:100]}")
                try:
                    result = tool_functions[block.name](**block.input)
                except Exception as e:
                    result = f"Error: {str(e)}"
                print(f"  -> {str(result)[:100]}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"

# Run it
result = run_research_agent(
    "Research how Anthropic recommends building AI agents. Produce a brief report."
)
```

### Step 4: Add Quality Checks (15 min)

```python
def run_research_agent_with_eval(query, max_turns=15):
    """Agent with self-evaluation step."""
    # Phase 1: Research
    report = run_research_agent(query, max_turns=max_turns)

    # Phase 2: Self-evaluate (evaluator-optimizer pattern)
    eval_response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Evaluate this research report on a scale of 1-10:

Query: {query}
Report: {report}

Score on:
1. Completeness (did it answer the question?)
2. Accuracy (are facts correct and sourced?)
3. Structure (is it well-organized?)

Return JSON: {{"completeness": N, "accuracy": N, "structure": N, "overall": N, "gaps": ["..."]}}"""
        }]
    )

    eval_text = eval_response.content[0].text
    print(f"\n[Self-Eval] {eval_text}")

    return {"report": report, "evaluation": eval_text}
```

### Step 5: Test Edge Cases (15 min)

```python
# Test 1: Simple query
run_research_agent("What is MCP?")

# Test 2: Complex multi-step query
run_research_agent(
    "Compare the Agent SDK with building agents from the raw Messages API. "
    "What are the trade-offs? When should you use each approach?"
)

# Test 3: Query with no good results
run_research_agent("What is the population of Mars colony in 2026?")
```

---

## Checklist: Is Your Agent Interview-Ready?

Run through this checklist for any agent you build:

- [ ] **Tools defined with detailed descriptions** (3+ sentences each)
- [ ] **Agent loop handles:** end_turn, tool_use, max_tokens, errors
- [ ] **Error handling:** try/except around every tool call, always returns tool_result
- [ ] **Parallel tool calls:** Loop processes ALL tool_use blocks, not just the first
- [ ] **Observability:** Prints each step (tool name, input, result)
- [ ] **System prompt:** Guides agent behavior and workflow
- [ ] **Max turns guard:** Prevents infinite loops
- [ ] **Edge cases tested:** Bad input, tool errors, no results

---

## Key Takeaways

- A complete agent = tools + tool functions + agent loop + system prompt + observability
- **Tool design matters as much as the loop** - Anthropic calls this "ACI" (agent-computer interface)
- Use `take_notes` / accumulation tools to build state across turns
- Self-evaluation (evaluator-optimizer pattern) is a cheap add-on that impresses
- In the interview: get the basic loop working in 15 min, add tools by 25 min, test by 35 min, polish by 45 min
