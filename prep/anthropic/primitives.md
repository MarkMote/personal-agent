# Anthropic Agent Build — Primitives List

Master these atomic skills. Every interview problem is a combination of them.

---

## Tier 1: MUST know cold (the agent loop lives here)

### P1. Client setup
```python
import anthropic
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
```

### P2. Basic message call
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.content[0].text)
```

### P3. System prompt
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="You are a helpful data analyst. Be concise.",
    messages=[...]
)
```

### P4. Multi-turn conversation
```python
messages = [
    {"role": "user", "content": "What's 2+2?"},
    {"role": "assistant", "content": "4"},
    {"role": "user", "content": "Multiply that by 3"},
]
# Stateless API — always send full history
```

### P5. Define a tool
```python
tools = [{
    "name": "get_weather",
    "description": "Get current weather for a city. Returns temp and conditions.",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "City and state, e.g. NYC, NY"}
        },
        "required": ["location"]
    }
}]
```

### P6. Send message with tools
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    tools=tools,
    messages=messages,
)
```

### P7. Check stop_reason and extract tool calls
```python
if response.stop_reason == "tool_use":
    for block in response.content:
        if block.type == "tool_use":
            tool_name = block.name
            tool_input = block.input
            tool_use_id = block.id
elif response.stop_reason == "end_turn":
    final_text = response.content[0].text
```

### P8. Return tool results
```python
# Append assistant response, then tool results as a "user" message
messages.append({"role": "assistant", "content": response.content})
messages.append({"role": "user", "content": [
    {
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": str(result)  # string or list of content blocks
    }
]})
```

### P9. Handle tool errors
```python
try:
    result = func(**block.input)
except Exception as e:
    result = f"Error: {str(e)}"
    # Still must return a tool_result — model needs it
    tool_results.append({
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": str(result),
        "is_error": True
    })
```

### P10. The agent loop (CORE PATTERN)
```python
def run_agent(user_message, tools, tool_functions, system="", max_turns=10):
    messages = [{"role": "user", "content": user_message}]

    for _ in range(max_turns):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=system,
            tools=tools,
            messages=messages,
        )

        # Done — no more tool calls
        if response.stop_reason == "end_turn":
            return response.content[0].text

        # Process tool calls
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                try:
                    result = tool_functions[block.name](**block.input)
                except Exception as e:
                    result = f"Error: {e}"
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

---

## Tier 2: SHOULD know (likely needed in any real problem)

### P11. Structured output via tool_choice
```python
# Force Claude to return structured JSON by defining a "tool" for output
extract_tool = {
    "name": "extract_info",
    "description": "Extract structured information",
    "input_schema": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "summary": {"type": "string"}
        },
        "required": ["name", "age", "summary"]
    }
}

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=[extract_tool],
    tool_choice={"type": "tool", "name": "extract_info"},
    messages=[{"role": "user", "content": "John is 30 and works in AI."}]
)
# Result is in response.content[0].input (the tool input IS your structured data)
structured_data = response.content[0].input
```

### P12. Parallel tool calls
```python
# Claude may return MULTIPLE tool_use blocks in one response
# Your loop already handles this — just iterate all blocks
for block in response.content:
    if block.type == "tool_use":
        # Execute each tool, collect ALL results
        ...
# Return ALL results in a single "user" message
messages.append({"role": "user", "content": tool_results})
```

### P13. Image input (base64)
```python
import base64
with open("image.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

messages = [{"role": "user", "content": [
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_data,
        }
    },
    {"type": "text", "text": "What's in this image?"}
]}]
```

### P14. Image input (URL)
```python
messages = [{"role": "user", "content": [
    {
        "type": "image",
        "source": {
            "type": "url",
            "url": "https://example.com/photo.jpg",
        }
    },
    {"type": "text", "text": "Describe this image."}
]}]
```

### P15. PDF input (base64)
```python
import base64
with open("doc.pdf", "rb") as f:
    pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

messages = [{"role": "user", "content": [
    {
        "type": "document",
        "source": {
            "type": "base64",
            "media_type": "application/pdf",
            "data": pdf_data,
        }
    },
    {"type": "text", "text": "Summarize this document."}
]}]
```

### P16. Prefill assistant response
```python
# Steer output format by pre-filling the assistant turn
messages = [
    {"role": "user", "content": "Classify: 'I love this product'"},
    {"role": "assistant", "content": '{"sentiment": "'},
]
# Claude continues from where you left off
```

### P17. Chain of thought prompting
```python
# In system prompt or user message:
system = """Think step by step before answering.
Wrap your reasoning in <thinking> tags, then give your final answer."""

# Or force it with prefill:
messages.append({"role": "assistant", "content": "<thinking>\n"})
```

### P18. XML tags for structure
```python
# Anthropic models respond well to XML structure in prompts
user_msg = """
<context>
The user is a data scientist working with pandas.
</context>

<task>
Write a function to clean this dataset.
</task>

<rules>
- Handle missing values
- Remove duplicates
- Return a pandas DataFrame
</rules>
"""
```

---

## Tier 3: GOOD to know (differentiators, use if relevant)

### P19. Extended thinking
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{"role": "user", "content": "Solve this complex problem..."}]
)

for block in response.content:
    if block.type == "thinking":
        print(f"Thinking: {block.thinking}")
    elif block.type == "text":
        print(f"Answer: {block.text}")
```

### P20. Extended thinking + tool use (preserve thinking blocks)
```python
# CRITICAL: pass thinking blocks back when continuing conversation
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    tools=tools,
    messages=messages,
)

# When appending assistant response, include ALL blocks (thinking + tool_use)
messages.append({"role": "assistant", "content": response.content})
# This already works because response.content includes thinking blocks
```

### P21. Streaming
```python
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### P22. Strict mode (guaranteed schema compliance)
```python
tools = [{
    "name": "extract",
    "description": "...",
    "strict": True,  # Guarantees output matches schema exactly
    "input_schema": { ... }
}]
```

### P23. Force any tool use vs specific tool
```python
# Force Claude to use ANY tool (must pick one):
tool_choice = {"type": "any"}

# Force a SPECIFIC tool:
tool_choice = {"type": "tool", "name": "get_weather"}

# Let Claude decide (default):
tool_choice = {"type": "auto"}

# Prevent tool use:
tool_choice = {"type": "none"}
```

### P24. Rich tool results (images/content blocks back to Claude)
```python
# Tool results can include images, not just text
tool_results = [{
    "type": "tool_result",
    "tool_use_id": block.id,
    "content": [
        {"type": "text", "text": "Screenshot captured:"},
        {
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": screenshot_b64
            }
        }
    ]
}]
```

---

## Agent Patterns (combinations of primitives)

These aren't new primitives — they're named combinations. Know when to use which.

### Pattern A: Simple chain (P2 + P3 + P4)
Sequential LLM calls where output of one becomes input of next.
Use when: Fixed multi-step pipeline. No dynamic decisions.

### Pattern B: Router (P2 + P3 + P11)
Classify input → dispatch to specialized handler.
Use when: Different input types need different processing.

### Pattern C: Tool agent (P5-P10, the full loop)
Claude decides which tools to call and when to stop.
Use when: Open-ended tasks requiring dynamic tool selection.

### Pattern D: Structured extractor (P11 + P13/P14/P15)
Force structured output from unstructured input (text, image, PDF).
Use when: "Parse this into JSON" type tasks.

### Pattern E: Evaluator-optimizer (P10 + two-agent setup)
Generate → evaluate → refine loop.
Use when: Quality matters and first draft won't be good enough.

---

## Quick Reference: What to Combine for Common Tasks

| Task | Primitives |
|------|-----------|
| "Build an agent that..." | P1 + P3 + P5-P10 (full loop) |
| "Extract data from PDF" | P1 + P15 + P11 |
| "Analyze these images" | P1 + P13/P14 + P3 |
| "Multi-step pipeline" | P1 + P3 + P4 (chain) |
| "Parse + act on results" | P11 → P10 (extract then agent loop) |
| "Complex reasoning task" | P19 + P10 (thinking + tools) |
