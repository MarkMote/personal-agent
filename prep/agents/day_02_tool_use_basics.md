# Day 2: Tool Use Basics (~2 hrs)

**Goal:** Understand how tool use works in the Anthropic API. Define tools, handle tool_use responses, return tool_result blocks. Build a working calculator agent.

---

## Reading (30 min)

1. **Tool Use Overview** - https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
   - How client tools work (the 4-step flow)
   - Tool definition format: `name`, `description`, `input_schema`
   - `stop_reason == "tool_use"` signals Claude wants to call a tool
   - Response contains `ToolUseBlock` with `id`, `name`, `input`

2. **How to Implement Tool Use** - https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use
   - Best practices for tool descriptions (detailed > brief)
   - `tool_choice` options: `auto`, `any`, `tool`, `none`
   - Parallel tool calls (Claude may call multiple tools at once)
   - `strict: true` for guaranteed schema validation

3. **API Primer tool use section** (local: `../anthropic/api_primer.md`, lines 273+)

**Key mental model:**
```
You send: tools + messages
Claude returns: text blocks + tool_use blocks (stop_reason="tool_use")
You execute: the tool with the provided input
You send back: tool_result blocks in a user message
Claude returns: text (stop_reason="end_turn") or more tool_use blocks
```

---

## Concepts to Know Cold

### Tool Definition Schema
```python
{
    "name": "get_weather",           # ^[a-zA-Z0-9_-]{1,64}$
    "description": "Get the current weather...",  # BE VERY DETAILED
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
```

### Response Content Blocks
```python
# response.content is a LIST of blocks:
# [TextBlock(type="text", text="Let me check..."),
#  ToolUseBlock(type="tool_use", id="toolu_xxx", name="get_weather", input={"location": "NYC"})]
```

### Tool Result Format
```python
# Goes in a "user" message:
{
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": "toolu_xxx",    # Must match the tool_use block's id
        "content": "72°F and sunny"     # String result
    }]
}
```

### Error Results
```python
{
    "type": "tool_result",
    "tool_use_id": "toolu_xxx",
    "content": "Error: location not found",
    "is_error": True                    # Tells Claude it failed
}
```

---

## Project: Calculator Agent (1 hr)

### Step 1: Define Tools (10 min)
```python
import anthropic
client = anthropic.Anthropic()

tools = [
    {
        "name": "add",
        "description": "Add two numbers together. Use when the user wants to compute a sum.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers together. Use for multiplication operations.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "divide",
        "description": "Divide the first number by the second. Returns the quotient. Raises error if dividing by zero.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "Numerator"},
                "b": {"type": "number", "description": "Denominator (must not be zero)"}
            },
            "required": ["a", "b"]
        }
    }
]
```

### Step 2: Implement Tool Functions (5 min)
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

tool_functions = {
    "add": add,
    "multiply": multiply,
    "divide": divide,
}
```

### Step 3: Single Tool Call (15 min)
```python
# Send a request that should trigger tool use
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What is 17 + 28?"}]
)

# Inspect the response
print(f"Stop reason: {response.stop_reason}")  # "tool_use"
for block in response.content:
    print(f"  {block.type}: {block}")

# Extract and execute the tool call
for block in response.content:
    if block.type == "tool_use":
        print(f"\nClaude wants to call: {block.name}({block.input})")
        func = tool_functions[block.name]
        result = func(**block.input)
        print(f"Result: {result}")

        # Feed the result back
        messages = [
            {"role": "user", "content": "What is 17 + 28?"},
            {"role": "assistant", "content": response.content},  # Include ALL content blocks
            {"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": str(result)
            }]}
        ]

        # Get final answer
        final = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )
        print(f"\nFinal answer: {final.content[0].text}")
```

### Step 4: Multi-Step Tool Use (30 min)
```python
# This requires multiple tool calls: (3 + 5) * 2 / 4
# Claude should call add(3,5) -> multiply(8,2) -> divide(16,4)

def run_calculator(user_message, max_turns=10):
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            tools=tools,
            messages=messages,
        )

        print(f"\n--- Turn {turn + 1} (stop_reason: {response.stop_reason}) ---")

        # If done, return the text
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Add assistant response to history
        messages.append({"role": "assistant", "content": response.content})

        # Process tool calls
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  Calling: {block.name}({block.input})")
                try:
                    func = tool_functions[block.name]
                    result = func(**block.input)
                    print(f"  Result: {result}")
                except Exception as e:
                    result = f"Error: {str(e)}"
                    print(f"  Error: {result}")

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"

# Test it
print(run_calculator("What is (3 + 5) * 2 / 4?"))
```

---

## Drills (30 min)

From memory, without notes:

1. **Define a tool** - Write a tool schema for `search_web(query: str, num_results: int)` with good descriptions. Target: < 2 min.

2. **Process a tool_use response** - Given a response with `stop_reason == "tool_use"`, write the code to extract the tool call, execute it, and build the tool_result message. Target: < 3 min.

3. **Full single-step tool call** - Write a complete request/response cycle: define 1 tool, send message, handle tool_use, return result, get final answer. Target: < 5 min.

4. **tool_choice** - Write requests using:
   - `tool_choice={"type": "auto"}` (default)
   - `tool_choice={"type": "any"}` (must use a tool)
   - `tool_choice={"type": "tool", "name": "add"}` (must use specific tool)

---

## Key Differences from OpenAI (Know These)

| Anthropic | OpenAI |
|-----------|--------|
| `stop_reason` | `finish_reason` |
| `content` is list of blocks | `content` is string, `tool_calls` is separate |
| `tool_use` blocks in assistant content | `function_call` or `tool_calls` in message |
| `tool_result` blocks in user message | `tool` role messages |
| `tool_use_id` | `tool_call_id` |

---

## Key Takeaways

- Tools are defined with `name`, `description` (be detailed!), and `input_schema` (JSON Schema)
- `stop_reason == "tool_use"` means Claude wants to call tools
- Assistant response may contain BOTH text blocks AND tool_use blocks
- Tool results go back as `tool_result` blocks in a user message, with matching `tool_use_id`
- Always pass `response.content` (the full list) as the assistant message, not just the text
- Claude can make parallel tool calls (multiple tool_use blocks in one response)
