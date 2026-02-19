# Day 10: Timed Practice & Review (~2 hrs)

**Goal:** Simulate the actual interview. Do a 45-minute timed build, then review and solidify weak areas.

---

## Warm-Up: Speed Drills (15 min)

From memory, no notes. Time each one.

### Drill 1: Agent Loop (target: 5 min)
Write the complete `run_agent(user_message, tools, tool_functions, max_turns=10)` function.

Checklist:
- [ ] messages list
- [ ] for loop with max_turns
- [ ] client.messages.create()
- [ ] stop_reason check
- [ ] assistant message append (full response.content)
- [ ] tool_use block processing with try/except
- [ ] tool_results list with tool_use_id
- [ ] user message append with tool_results

### Drill 2: Tool Definition (target: 2 min)
Define a tool `search_database(query: str, limit: int = 10)` with a detailed description.

### Drill 3: Error Handling (target: 2 min)
Write the tool execution block with:
- try/except
- is_error flag
- always returns tool_result

### Drill 4: Structured Output (target: 2 min)
Write a request that forces JSON output using `tool_choice={"type": "tool", "name": "format_output"}`.

**If all 4 are done in under 12 minutes, you're ready.**

---

## Timed Build: 45 Minutes (45 min)

Set a timer. Pick ONE of these prompts (or have someone pick for you). Build it in Colab.

### Prompt A: Customer Support Agent
> Build an agent that handles customer support for an e-commerce store. It should be able to look up orders, check inventory, and create support tickets. Given a customer message, the agent should resolve their issue or escalate appropriately.

Tools to implement:
- `lookup_order(order_id)` - returns order status, items, dates
- `check_inventory(product_id)` - returns stock level and availability
- `create_ticket(customer_id, issue, priority)` - creates a support ticket

### Prompt B: Data Analysis Agent
> Build an agent that can analyze a dataset. It should be able to query data, compute statistics, and produce a summary. Given a question about the data, the agent should use its tools to find the answer.

Tools to implement:
- `query_data(sql)` - run a SQL query on the dataset
- `compute_stats(column, operation)` - mean/median/std/min/max on a column
- `plot_chart(x_col, y_col, chart_type)` - generate a chart description

### Prompt C: Code Review Agent
> Build an agent that reviews code for quality issues. It should be able to read files, search for patterns, and produce a review with findings and suggestions.

Tools to implement:
- `read_file(path)` - read a source file
- `search_pattern(pattern, path)` - grep for a regex pattern
- `list_files(directory, extension)` - list files matching a type

### Time Allocation
| Time | Action |
|------|--------|
| 0-3 min | Read prompt, plan approach, identify which pattern to use |
| 3-8 min | Define tools (schemas + descriptions) |
| 8-15 min | Implement tool functions (can be mocks) |
| 15-22 min | Write agent loop (from muscle memory) |
| 22-30 min | Wire together, test basic case |
| 30-38 min | Handle edge cases, add error handling |
| 38-42 min | Test with 2-3 different inputs |
| 42-45 min | Clean up, add comments |

---

## Post-Build Review (15 min)

After the timed build, review your code against this rubric:

### Must-Haves (will they fail you without these?)
- [ ] Agent loop works end-to-end (sends message, processes tools, returns answer)
- [ ] At least 2-3 working tools with clear schemas
- [ ] Error handling (try/except around tool execution)
- [ ] Tool results always sent back (even on error)

### Strong Signals (will set you apart)
- [ ] Detailed tool descriptions (3+ sentences)
- [ ] System prompt that guides agent behavior
- [ ] Observability (prints each step)
- [ ] Handles parallel tool calls
- [ ] Tested with multiple inputs

### Bonus Points (if you have time)
- [ ] Structured output at the end
- [ ] Gate checks or validation
- [ ] Discussion of trade-offs (why agent loop vs. chain?)
- [ ] Mention of Anthropic-specific concepts (ACI, complexity ladder)

---

## Review: Key Concepts Flashcards

Go through these quickly. If you can answer all from memory, you're ready.

**Q: What's the basic message flow for tool use?**
A: Define tools -> send message -> Claude returns tool_use blocks -> you execute tools -> send tool_result back -> Claude responds or calls more tools

**Q: What goes in a tool_result message?**
A: `{"type": "tool_result", "tool_use_id": "...", "content": "..."}` — goes in a user message

**Q: How do you handle tool errors?**
A: try/except, set `"is_error": True` in the tool_result, always return a result

**Q: What's `response.content`?**
A: A list of content blocks (TextBlock, ToolUseBlock, ThinkingBlock). Not a string.

**Q: What's `stop_reason`?**
A: `"end_turn"` (done), `"tool_use"` (wants to call tools), `"max_tokens"` (ran out of space)

**Q: How do you force structured JSON output?**
A: Option 1: `tool_choice={"type": "tool", "name": "..."}` with a formatting tool. Option 2: `output_config={"format": {"type": "json_schema", "schema": {...}}}`

**Q: What's Anthropic's agent philosophy?**
A: Start simple. Prompt chaining before routing. Routing before agents. Agents are the last resort. Invest in tool design (ACI).

**Q: What's the complexity ladder?**
A: Single call -> chaining -> routing -> parallelization -> orchestrator-workers -> evaluator-optimizer -> autonomous agent

**Q: What's MCP?**
A: Model Context Protocol. Standardized JSON-RPC protocol for connecting AI to tools and data. Exposes Tools, Resources, and Prompts.

**Q: How does extended thinking work with tool use?**
A: Pass thinking blocks back in the assistant message along with tool_use blocks. Use `thinking={"type": "enabled", "budget_tokens": N}` where `max_tokens > N`.

**Q: What are the key differences from OpenAI?**
A: `stop_reason` (not `finish_reason`), `content` is a list of blocks (not a string), tool results go in user messages as `tool_result` blocks (not `tool` role), `tool_use` blocks (not `function_call`)

---

## Final Prep Reminders

1. **Set up your Colab** before the interview:
   - `!pip install anthropic` in the first cell
   - Verify API key works with a hello-world call
   - Have the agent loop function ready to paste (but don't paste it until you need it)

2. **During the interview:**
   - Ask clarifying questions first (2-3 min)
   - Say which pattern you're going to use and WHY
   - Get the basic loop working before adding polish
   - Talk through your design decisions out loud
   - If you finish early, discuss improvements you'd make

3. **What to say if stuck:**
   - "Let me think about the tool schema for a moment"
   - "I'm going to start with the simplest version and iterate"
   - "This could be solved with [simpler pattern], but I'll build the agent loop since that's what you asked for"

4. **What NOT to do:**
   - Don't spend 15 min on perfect tool descriptions before writing any code
   - Don't try to add streaming, thinking, MCP, etc. unless specifically asked
   - Don't forget to test - even one successful run is better than untested code
   - Don't apologize for using mocks - that's expected in a 45-min build
