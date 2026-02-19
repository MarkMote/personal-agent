# Day 6: Streaming & Extended Thinking (~2 hrs)

**Goal:** Add streaming and extended thinking to your agent toolkit. These are differentiators that show you know the API beyond the basics.

---

## Reading (30 min)

1. **Streaming Messages** - https://platform.claude.com/docs/en/api/streaming
   - SSE event types: `message_start`, `content_block_start`, `content_block_delta`, `content_block_stop`, `message_delta`, `message_stop`
   - SDK helper: `client.messages.stream()` with `text_stream`
   - Delta types: `text_delta`, `input_json_delta`, `thinking_delta`

2. **Extended Thinking** - https://platform.claude.com/docs/en/build-with-claude/extended-thinking
   - `thinking={"type": "enabled", "budget_tokens": 10000}`
   - Response includes `thinking` blocks before `text` blocks
   - `max_tokens` must be > `budget_tokens`
   - With tool use: must pass `thinking` blocks back in the assistant message

3. **API Primer** (local: `../anthropic/api_primer.md`) - Streaming + thinking sections

---

## Project A: Streaming Chat (30 min)

### Basic Streaming

```python
import anthropic
client = anthropic.Anthropic()

# Simple streaming - text appears token by token
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a haiku about programming."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()  # newline at end
```

### Streaming with Full Event Access

```python
# Access the full event stream for more control
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain recursion in 3 sentences."}]
) as stream:
    for event in stream:
        # event types: message_start, content_block_start,
        # content_block_delta, content_block_stop, message_delta, message_stop
        if event.type == "content_block_delta":
            if event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)
        elif event.type == "message_stop":
            print("\n[Done]")
```

### Streaming with Tool Use

```python
tools = [{
    "name": "get_time",
    "description": "Get the current time in a timezone",
    "input_schema": {
        "type": "object",
        "properties": {
            "timezone": {"type": "string", "description": "e.g. 'America/New_York'"}
        },
        "required": ["timezone"]
    }
}]

with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What time is it in New York?"}]
) as stream:
    for event in stream:
        if event.type == "content_block_start":
            if event.content_block.type == "tool_use":
                print(f"\n[Tool call starting: {event.content_block.name}]")
        elif event.type == "content_block_delta":
            if event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)
            elif event.delta.type == "input_json_delta":
                print(event.delta.partial_json, end="", flush=True)

# Note: For a streaming agent loop, you'd collect the full response
# from the stream, then process tool calls as before
final_message = stream.get_final_message()
print(f"\nStop reason: {final_message.stop_reason}")
```

---

## Project B: Extended Thinking (30 min)

### Basic Extended Thinking

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{
        "role": "user",
        "content": "What is 127 * 389? Show your work."
    }]
)

# Response contains thinking blocks THEN text blocks
for block in response.content:
    if block.type == "thinking":
        print(f"[Thinking] {block.thinking[:200]}...")
    elif block.type == "text":
        print(f"[Answer] {block.text}")
```

### Extended Thinking with Tool Use

This is the tricky part: you must pass thinking blocks back when continuing the conversation.

```python
tools = [{
    "name": "calculate",
    "description": "Evaluate a math expression",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {"type": "string", "description": "Math expression to evaluate"}
        },
        "required": ["expression"]
    }
}]

def calculate(expression):
    return str(eval(expression))

# First call - Claude thinks, then requests a tool
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    tools=tools,
    messages=[{"role": "user", "content": "What is the square root of 144 divided by 3?"}]
)

print("First response blocks:")
for block in response.content:
    print(f"  {block.type}: {str(block)[:100]}")

if response.stop_reason == "tool_use":
    # CRITICAL: Pass ALL content blocks back, INCLUDING thinking blocks
    tool_use_block = next(b for b in response.content if b.type == "tool_use")
    result = calculate(**tool_use_block.input)

    # Build the continuation - response.content includes thinking + tool_use
    continuation = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        thinking={"type": "enabled", "budget_tokens": 10000},
        tools=tools,
        messages=[
            {"role": "user", "content": "What is the square root of 144 divided by 3?"},
            # Pass the FULL response content (thinking + tool_use)
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": tool_use_block.id,
                "content": result
            }]}
        ]
    )

    for block in continuation.content:
        if block.type == "text":
            print(f"Final answer: {block.text}")
```

### Agent Loop with Thinking

```python
def run_thinking_agent(user_message, tools, tool_functions, max_turns=10):
    """Agent loop that preserves thinking blocks across turns."""
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            thinking={"type": "enabled", "budget_tokens": 10000},
            tools=tools,
            messages=messages,
        )

        # Log thinking
        for block in response.content:
            if block.type == "thinking":
                print(f"  [Think] {block.thinking[:150]}...")

        if response.stop_reason == "end_turn":
            return "".join(b.text for b in response.content if hasattr(b, "text"))

        # IMPORTANT: Pass the FULL content (including thinking blocks)
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                try:
                    result = tool_functions[block.name](**block.input)
                except Exception as e:
                    result = f"Error: {str(e)}"
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

**Key difference from regular agent loop:** The assistant message includes thinking blocks. You pass `response.content` as-is (which includes thinking + tool_use). The API handles the rest.

---

## Project C: Streaming Agent Loop (15 min)

Combine streaming with the agent loop for real-time output:

```python
def run_streaming_agent(user_message, tools, tool_functions, max_turns=10):
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        # Use streaming to show output in real-time
        with client.messages.stream(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            tools=tools,
            messages=messages,
        ) as stream:
            # Print text as it arrives
            for text in stream.text_stream:
                print(text, end="", flush=True)

            # Get the complete message for processing
            response = stream.get_final_message()

        print()  # newline after streaming text

        if response.stop_reason == "end_turn":
            return "".join(b.text for b in response.content if hasattr(b, "text"))

        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"\n  [Calling {block.name}...]")
                try:
                    result = tool_functions[block.name](**block.input)
                except Exception as e:
                    result = f"Error: {str(e)}"
                print(f"  [Result: {str(result)[:100]}]")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(result)
                })

        messages.append({"role": "user", "content": tool_results})

    return "Max turns reached"
```

---

## Drills (15 min)

1. **Streaming** - Write `client.messages.stream()` with `text_stream` from memory. Target: < 1 min.

2. **Extended thinking** - Write a request with `thinking={"type": "enabled", "budget_tokens": 10000}`. What must be true about `max_tokens`?

3. **Thinking + tool use** - What's the critical difference when passing assistant messages back? (Answer: include thinking blocks in `response.content`)

---

## Key Takeaways

- **Streaming:** `client.messages.stream()` + `.text_stream` for simple text streaming
- **Extended thinking:** `thinking={"type": "enabled", "budget_tokens": N}` where `max_tokens > budget_tokens`
- **Thinking + tools:** Must pass `response.content` (including thinking blocks) back as the assistant message
- **Interleaved thinking** (beta): Allows thinking between tool calls - `betas=["interleaved-thinking-2025-05-14"]`
- The streaming agent loop is the same pattern, just using `stream.get_final_message()` to get the complete response for tool processing
- These features are **differentiators** in the interview - most candidates only know the basic loop
