# Anthropic Agent Build Prep

Build a working agent in a Colab notebook in 45 minutes using the Anthropic Python SDK.

**Interview:** TBD (next round after HM screen with Samuel Flamini, which went well 2/18)
**Format:** Google Colab, 45 min, build an agent for a given task
**Samuel's advice:** Read the agent docs and tool use docs

---

## Priority 0: Anthropic's Agent Philosophy (know this, it's cultural)

From their "Building Effective Agents" blog — **this is how they think about agents:**

1. **Start simple.** Don't build an agent when a single LLM call with good prompting works.
2. **Workflows before agents.** Fixed orchestration patterns (chaining, routing, parallelization) are more predictable than fully autonomous agents.
3. **Agents are the last resort.** Only use autonomous agent loops when the task genuinely requires dynamic decision-making.
4. **Invest in tool design.** Think of tool descriptions and schemas as an "agent-computer interface" (ACI). Clear descriptions, good examples, minimal formatting overhead.
5. **Transparency.** Show the agent's planning steps. Don't hide what's happening.

**Complexity ladder (only climb as needed):**
```
Single LLM call (optimized prompt)
  → Prompt chaining (sequential steps)
    → Routing (classify then specialize)
      → Parallelization (concurrent independent tasks)
        → Orchestrator-workers (dynamic delegation)
          → Evaluator-optimizer (generate + critique loop)
            → Autonomous agent (tool-using loop)
```

**In the interview:** If you can solve it with a simpler pattern, say so. Building the agent loop when a chain would suffice is a red flag at Anthropic.

---

## Priority 1: Anthropic Python SDK Basics (know cold)

### Client Setup
```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)
print(response.content[0].text)
```

### Tool Use (Function Calling)
This is the core of agent building. Know this pattern cold.

```python
# 1. Define tools
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
]

# 2. Send message with tools
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}]
)

# 3. Check if model wants to use a tool
# response.stop_reason == "tool_use" means it wants to call a tool
# response.content is a list of blocks:
#   - TextBlock(type="text", text="...")
#   - ToolUseBlock(type="tool_use", id="...", name="get_weather", input={...})
```

### The Agent Loop (most important pattern)
```python
def run_agent(user_message, tools, tool_functions, max_turns=10):
    messages = [{"role": "user", "content": user_message}]

    for _ in range(max_turns):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            tools=tools,
            messages=messages,
        )

        # If model is done (no more tool calls), return final text
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Otherwise, process tool calls
        # Add assistant's response to messages
        messages.append({"role": "assistant", "content": response.content})

        # Execute each tool call and collect results
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                # Execute the tool
                func = tool_functions[block.name]
                result = func(**block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        # Feed results back
        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

---

## Priority 2: Common Agent Patterns

### Pattern A: Research Agent (search + synthesize)
Tools: `web_search(query)`, `read_url(url)`
Loop: search → read results → synthesize answer

### Pattern B: Data Agent (query + compute)
Tools: `run_sql(query)`, `calculate(expression)`, `plot(data)`
Loop: understand question → query data → compute → present

### Pattern C: Task Agent (plan + execute)
Tools: `read_file(path)`, `write_file(path, content)`, `run_command(cmd)`
Loop: plan steps → execute each → verify → report

### Pattern D: Customer Support Agent
Tools: `lookup_order(id)`, `check_inventory(sku)`, `create_ticket(details)`
Loop: understand issue → gather info → take action → confirm

**For each pattern, practice:**
1. Define 2-3 tools with clear schemas
2. Write the tool execution functions (can be mocks in Colab)
3. Wire up the agent loop
4. Handle edge cases (tool errors, unexpected inputs)

---

## Priority 3: Things That Impress

### Error Handling in Agent Loop
```python
# Wrap tool execution
try:
    result = func(**block.input)
except Exception as e:
    result = f"Error: {str(e)}"

# Always return a tool_result even on error — the model needs it
```

### System Prompt for Agent Behavior
```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    system="You are a helpful assistant. Use tools when needed. Think step by step.",
    tools=tools,
    messages=messages,
)
```

### Streaming (bonus, if time)
```python
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

---

## Priority 4: Anthropic-Specific Concepts to Know

### MCP (Model Context Protocol)
- Standard protocol for connecting AI models to external tools and data
- Servers expose tools and resources via JSON-RPC over stdio
- Relevant if they ask about architecture, not likely in 45-min build

### Multi-turn Conversation Structure
- Messages alternate: user → assistant → user → assistant
- Tool results go in a "user" message (as tool_result blocks)
- Assistant messages can contain both text AND tool_use blocks

### Key Differences from OpenAI
- `stop_reason` not `finish_reason`
- `content` is a list of blocks, not a single string
- Tool results are `tool_result` blocks in user messages, not `function` role
- No `function_call` — it's `tool_use` blocks in assistant content

---

## Docs to Read Before Interview

Links saved in `prep/anthropic/links.md`. Prioritized reading list:

### Must Read (1-2 hours total)
- [ ] **"Building Effective Agents" blog** — https://www.anthropic.com/engineering/building-effective-agents
  - Anthropic's official philosophy. Key takeaway: **start simple, only add complexity when it measurably helps.**
  - Patterns (in order of complexity): augmented LLM → prompt chaining → routing → parallelization → orchestrator-workers → evaluator-optimizer → autonomous agents
  - They value simplicity, transparency, and good tool design (ACI = agent-computer interface)
  - **Showing you've read this signals cultural alignment**

- [ ] **Tool use docs** — https://platform.claude.com/docs/en/build-with-claude/tool-use/overview
  - Exact API mechanics: `input_schema`, `stop_reason == "tool_use"`, `tool_result` blocks
  - Response content is a LIST of blocks (TextBlock + ToolUseBlock)
  - Claude can make parallel tool calls (multiple tool_use blocks in one response)
  - `strict: true` on tool definitions guarantees schema validation
  - Tool results go in a "user" message as `tool_result` blocks with matching `tool_use_id`

- [ ] **Cookbook: Basic workflows** — https://platform.claude.com/cookbook/patterns-agents-basic-workflows
  - Code for 3 patterns: prompt chaining, parallelization, routing
  - Uses `ThreadPoolExecutor` for parallel, XML tags for structured routing

### Should Skim (30 min)
- [ ] **Cookbook: Customer service agent** — tool use with order lookup, ticket creation
- [ ] **Cookbook: Calculator tool** — simplest possible tool use example
- [ ] **Cookbook: ReAct agent** — ReAct pattern implementation
- [ ] **Cookbook: Programmatic tool calling** — advanced pattern, reduces latency by having Claude write code that calls tools

### Skip Unless Asked
- MCP course (Skilljar link) — conceptual, won't be tested in 45-min build
- RAG cookbooks — only if they specifically ask for retrieval
- Vision, fine-tuning, batch processing cookbooks

---

## 45-Minute Battle Plan

Assuming they give you a task like "build an agent that does X":

| Time | Action |
|------|--------|
| 0-3 min | Read prompt, ask clarifying questions |
| 3-8 min | Define tools (schemas + mock implementations) |
| 8-15 min | Write agent loop (copy from muscle memory) |
| 15-25 min | Wire everything together, test basic case |
| 25-35 min | Handle edge cases, add error handling |
| 35-40 min | Test with a few different inputs |
| 40-45 min | Clean up, add comments, discuss improvements |

**The agent loop is the core deliverable.** Get it working first, then polish. A working agent with 2 tools beats a broken agent with 5 tools.

---

## Practice Exercises

### Exercise 1: Calculator Agent (15 min)
Build an agent with tools: `add(a, b)`, `multiply(a, b)`, `divide(a, b)`
Test: "What is (3 + 5) * 2 / 4?"

### Exercise 2: File Q&A Agent (25 min)
Build an agent with tools: `list_files(directory)`, `read_file(path)`, `search_text(query, path)`
Test: "Find all Python files and tell me which one has the most functions"

### Exercise 3: Data Pipeline Agent (30 min)
Build an agent with tools: `fetch_data(url)`, `parse_json(data)`, `compute_stats(values)`, `format_report(stats)`
Test: "Fetch the data from this URL, compute average and median, and give me a summary"

### Exercise 4: ReAct Agent from Scratch (30 min)
See `interview_problems/original/01_applied_ai.md` Problem 9 — ReAct agent with injected LLM. Good practice for understanding the loop without API dependencies.

**From existing repo also relevant:**
- Problem 10: MCP Server (hello-world)
- Problem 14: Tool-Calling Agent Loop (async, with error handling)
- Problem 23 Part B2: Agent without LangChain (raw SDK)
